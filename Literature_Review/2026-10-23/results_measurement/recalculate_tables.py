"""Recalculate two published checks from archived tables/annotation labels.

This does not call an LLM or alter the archived paper files.
"""
from pathlib import Path
from collections import Counter
import json, math

ROOT = Path(__file__).resolve().parent

def fleiss_kappa(rows):
    if not rows:
        return None
    observed = sum((sum(n*n for n in Counter(row).values())-3)/6 for row in rows)/len(rows)
    counts = Counter(x for row in rows for x in row)
    expected = sum((n/(3*len(rows)))**2 for n in counts.values())
    return (observed-expected)/(1-expected)

def main():
    categories = {"left", "neutral", "right"}
    quote_categories = ["left", "right", "left -> right", "right -> left"]
    triples = {x: [] for x in ["aggregate", "headline", "conclusion", "quotation"]}
    n_articles = 0
    for path in sorted((ROOT/"audit_sources").glob("explicit_*_.json")):
        for run in json.loads(path.read_text(encoding="utf-8")):
            for article in run.get("articles", []):
                n_articles += 1
                row = [article.get(k, "").strip() for k in ["Human's Bias", "Human's Bias(1)", "GPT's Bias"]]
                if all(x in categories for x in row):
                    triples["aggregate"].append(row)
                raters = [article.get(k, {}) for k in ["Human's analysis", "Human's analysis(1)", "GPT's analysis"]]
                for metric, key in [("headline", "headline"), ("conclusion", "Conclusion (article/model thoughts)")]:
                    row = [r.get(key, "").strip() for r in raters]
                    if all(x in categories for x in row):
                        triples[metric].append(row)
                quotes = []
                for rater in raters:
                    labels = {}
                    for category in quote_categories:
                        raw = rater.get("Supporter (interview respondent) quote", {}).get(category, "")
                        for name in raw.split(","):
                            if name.strip():
                                labels[name.strip()] = category
                    quotes.append(labels)
                for name in set().union(*(set(q) for q in quotes)):
                    row = [q.get(name) for q in quotes]
                    if None not in row:
                        triples["quotation"].append(row)
    yoo = {"articles": n_articles,
           "results": {k: {"n_units": len(v), "fleiss_kappa": fleiss_kappa(v)} for k, v in triples.items()},
           "scope": "Recomputed from authors public annotation labels; not independent recoding or a rerun of the judge."}
    table = [[276, 74, 18, 32], [190, 97, 41, 72]]
    columns = [sum(row[j] for row in table) for j in range(4)]
    statistic = sum((value-columns[j]/2)**2/(columns[j]/2) for row in table for j, value in enumerate(row))
    # Closed-form survival function of chi-square with 3 degrees of freedom.
    p = math.erfc(math.sqrt(statistic/2)) + math.sqrt(2*statistic/math.pi)*math.exp(-statistic/2)
    awwad = {"counts": table, "chi2": statistic, "df": 3, "p": p,
             "cramers_v": math.sqrt(statistic/800),
             "english_security_pct": 69.0, "arabic_security_pct": 47.5,
             "total_variation_distance": sum(abs(table[0][j]/400-table[1][j]/400) for j in range(4))/2,
             "scope": "Recomputed from published pooled table; not response-level reproduction."}
    result = {"yoo_2025": yoo, "awwad_2026": awwad}
    (ROOT/"recalculation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
