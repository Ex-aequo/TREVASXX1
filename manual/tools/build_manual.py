#!/usr/bin/env python3
"""Gera manual_pt.json a partir do manual em Markdown (EN) e da tradução PT (mesma estrutura linha a linha).
Uso: build_manual.py <manual_en.md> <manual_pt.md> <versao> <saida.json>
Ambos os .md são o corpo do manual (a partir de '**PART I — INTRODUCTION**' / '**PARTE I …**'), com os títulos
no formato **N.N Título** ou **PART X — Título**."""
import re, sys, json, subprocess, html as H
en_path, pt_path, version, out = sys.argv[1:5]
HRE = re.compile(r'^\*\*((PART|PARTE) ([IVX]+) — (.+?)|(\d+(?:\.\d+)+[a-z]?|\d+\.\d+[a-z]?)\.? (.+?))\*\*\s*$')

def split(lines):
    secs, cur = [], None
    for l in lines:
        m = HRE.match(l)
        if m:
            if cur: secs.append(cur)
            if m.group(2):
                cur = {'num': 'PART ' + m.group(3), 'id': 'part-' + m.group(3).lower(), 'title': m.group(4), 'level': 0, 'lines': []}
            else:
                n = m.group(5)
                cur = {'num': n, 'id': 's' + n, 'title': m.group(6), 'level': n.count('.') + 1, 'lines': []}
        elif cur is not None:
            cur['lines'].append(l)
    if cur: secs.append(cur)
    return secs

en = split(open(en_path, encoding='utf-8').read().split('\n'))
pt = split(open(pt_path, encoding='utf-8').read().split('\n'))
assert len(en) == len(pt), f'nº de secções difere: EN {len(en)} PT {len(pt)}'
for a, b in zip(en, pt):
    assert a['id'] == b['id'], f"secção desalinhada: {a['id']} vs {b['id']}"
ids = {s['id'] for s in pt}

def to_html(md):
    r = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html', '--wrap=none'], input=md, capture_output=True, text=True, check=True)
    h = r.stdout
    h = re.sub(r'<table>', '<div class="mtbl"><table>', h)
    h = h.replace('</table>', '</table></div>')
    def xref(m):
        n = m.group(1)
        return f'<a class="xref" data-sec="s{n}">§{n}</a>' if ('s' + n) in ids else m.group(0)
    # só em texto (fora de tags / <code>)
    parts = re.split(r'(<[^>]+>)', h)
    out_parts, in_code = [], False
    for p in parts:
        if p.startswith('<'):
            if p.startswith('<code'): in_code = True
            if p.startswith('</code'): in_code = False
            out_parts.append(p)
        else:
            out_parts.append(p if in_code else re.sub(r'§(\d+(?:\.\d+)*[a-z]?)', xref, p))
    return ''.join(out_parts)

secs = []
for s in pt:
    md = '\n'.join(s['lines']).strip()
    secs.append({'id': s['id'], 'num': s['num'], 'title': s['title'], 'level': s['level'], 'html': to_html(md) if md else ''})
data = {'version': version, 'lang': 'pt_PT', 'sections': secs}
json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(f'{len(secs)} secções → {out} ({len(json.dumps(data, ensure_ascii=False))//1024} KB)')
