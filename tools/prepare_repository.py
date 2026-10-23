"""Make research Markdown portable, rebuild navigation, and verify the archive.

Run from any directory: python tools/prepare_repository.py
Original PDFs, source texts, JSON catalogs and third-party snapshots are read only.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from datetime import datetime, timezone
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ['Basic Idea', 'Literature_Library', 'Literature_Review', 'Research_Notes', 'tools']
SNAPSHOTS = ROOT / 'Research_Notes' / 'venue_check_sources'
LINK = re.compile(r'\]\((?:<([^>\n]+)>|([^\s)]+))\)')


def portable_links(path):
    original = path.read_bytes()
    text = original.decode('utf-8')
    prefix = ROOT.as_posix() + '/'
    def replace(match):
        raw = match.group(1) or match.group(2)
        if not raw.casefold().startswith(prefix.casefold()):
            return match.group(0)
        target = ROOT / raw[len(prefix):]
        if not target.exists():
            raise ValueError(f'Broken absolute link in {path}: {raw}')
        relative = Path(os.path.relpath(target, path.parent)).as_posix()
        return f'](<{relative}>)'
    updated, replacements = LINK.subn(replace, text)
    if updated != text:
        path.write_bytes(updated.encode('utf-8'))
        return sum(1 for m in LINK.finditer(text)
                   if (m.group(1) or m.group(2)).casefold().startswith(prefix.casefold()))
    return 0


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    converted = sum(portable_links(p)
                    for name in ['Literature_Library', 'Literature_Review']
                    for p in (ROOT / name).rglob('*.md'))
    # Include only tracked files and nonignored task artifacts; never traverse .git.
    raw = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT)
    paths = sorted({Path(x.decode('utf-8')) for x in raw.split(b'\0') if x})
    lines = ['# 全项目资料索引', '',
             '相对链接用于GitHub在线阅读及克隆后的目录浏览。原始资料、文献归档、研究核查与独立署名判断分别列出。', '',
             '[返回项目入口](README.md)', '']
    for name in SECTIONS:
        group = [p for p in paths if p.parts[0] == name]
        lines += [f'## {name}（{len(group)}份文件）', '',
                  '| 文件 | 类型 | 大小 |', '|---|---|---:|']
        for p in group:
            label = p.relative_to(name).as_posix().replace('|', '\\|')
            lines.append(f'| [{label}](<{p.as_posix()}>) | {p.suffix.lstrip(".")} | {(ROOT/p).stat().st_size:,} B |')
        lines.append('')
    (ROOT / 'PROJECT_INDEX.md').write_text('\n'.join(lines), encoding='utf-8')

    checked = 0
    broken = []
    absolute = []
    for p in [ROOT/'README.md', ROOT/'PROJECT_INDEX.md'] + [
        ROOT/q for q in paths if q.suffix == '.md' and q.parts[0] in SECTIONS]:
        # Verbatim, attributed external documentation keeps its upstream links.
        if p.parent == SNAPSHOTS and p.name.startswith('marvel_'):
            continue
        # Archived source README is also a third-party snapshot.
        if p.name == 'yoo_README.md':
            continue
        for match in LINK.finditer(p.read_text(encoding='utf-8-sig')):
            target = match.group(1) or match.group(2)
            if re.match(r'^[A-Za-z]:[/\\]', target):
                absolute.append({'file':str(p.relative_to(ROOT)), 'target':target})
                continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checked += 1
            resolved = (p.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                broken.append({'file':str(p.relative_to(ROOT)), 'target':target})

    library = ROOT/'Literature_Library'
    catalog = json.loads((library/'00_目录与下载记录/library_catalog_80.json').read_text(encoding='utf-8'))
    verified = 0
    for record in catalog['records']:
        d = record['download']
        if d['status'] == 'pdf_downloaded':
            p = library / d['path'].replace('\\', '/')
            assert hashlib.sha256(p.read_bytes()).hexdigest() == d['sha256'], record['id']
            verified += 1
    original = ROOT/'Literature_Review/2026-10-22/literature_catalog.json'
    snapshot = library/'00_目录与下载记录/catalog_80_snapshot.json'
    assert original.read_bytes() == snapshot.read_bytes()
    report = {
        'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'local_markdown_links_checked':checked,
        'broken_local_links':broken,
        'machine_absolute_markdown_links':absolute,
        'third_party_snapshot_links':'Preserved as upstream; see source attribution',
        'original_catalog_records':len(catalog['records']),
        'primary_pdf_sha256_verified':verified,
        'original_catalog_matches_frozen_snapshot':True,
        'pending_fulltext_ids':[r['id'] for r in catalog['records'] if r['download']['status']=='pending_fulltext'],
        'framing_studies':14,
        'results_studies':16,
        'all_80_results_reviewed':False,
    }
    assert not broken and not absolute, json.dumps(report,ensure_ascii=False)
    out = ROOT/'tools/repository_validation.json'
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'converted_absolute_links':converted, **report},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
