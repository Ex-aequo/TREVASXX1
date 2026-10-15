#!/usr/bin/env python3
"""Atualização do manual PT quando sai um manual novo.

1) prepare <manual_novo.docx|.md> <manual_en_antigo.md> <manual_pt_antigo.md> <pasta_trabalho>
   - converte o docx (pandoc -t gfm --wrap=none), isola o corpo do manual,
   - compara secção a secção (pelo número §) com o manual EN antigo,
   - copia as secções iguais da tradução antiga (nada a traduzir),
   - escreve em <pasta>/todo_en.md só as secções NOVAS ou ALTERADAS (a traduzir, mesma regra linha-a-linha),
   - escreve <pasta>/plan.json e <pasta>/new_en.md (corpo completo do manual novo).
2) (traduzir todo_en.md → <pasta>/todo_pt.md, seguindo glossario.md; ver check_chunk.py)
3) assemble <pasta>
   - junta: secções inalteradas (da tradução antiga) + todo_pt.md → <pasta>/new_pt.md
   Depois: build_manual.py new_en.md new_pt.md <versao> manual_pt.json
"""
import re, sys, json, subprocess, os
HRE = re.compile(r'^\*\*((PART|PARTE) ([IVX]+) — (.+?)|(\d+(?:\.\d+)+[a-z]?|\d+\.\d+[a-z]?)\.? (.+?))\*\*\s*$')

def body_lines(md):
    L = md.split('\n')
    idx = [k for k, l in enumerate(L) if l.startswith('**PART I — INTRODUCTION') or l.startswith('**PARTE I — ')]
    return L[idx[-1]:]            # a 1.ª ocorrência está no índice; a última é o corpo

def split(lines):
    secs, cur, order = {}, None, []
    for l in lines:
        m = HRE.match(l)
        if m:
            key = ('PART ' + m.group(3)) if m.group(2) else m.group(5)
            cur = {'key': key, 'lines': [l]}
            secs[key] = cur; order.append(key)
        elif cur is not None:
            cur['lines'].append(l)
    return secs, order

def norm(lines):
    return [re.sub(r'\s+', ' ', l).strip() for l in lines]

def prepare(new, old_en, old_pt, work):
    os.makedirs(work, exist_ok=True)
    if new.endswith('.docx'):
        md = subprocess.run(['pandoc', new, '-t', 'gfm', '--wrap=none'], capture_output=True, text=True, check=True).stdout
    else:
        md = open(new, encoding='utf-8').read()
    new_body = body_lines(md)
    open(f'{work}/new_en.md', 'w', encoding='utf-8').write('\n'.join(new_body))
    ns, norder = split(new_body)
    os_, _ = split(open(old_en, encoding='utf-8').read().split('\n'))
    ps, _ = split(open(old_pt, encoding='utf-8').read().split('\n'))
    plan = {'order': norder, 'same': [], 'changed': [], 'new': [], 'removed': [k for k in os_ if k not in ns]}
    todo = []
    for k in norder:
        if k in os_ and norm(os_[k]['lines']) == norm(ns[k]['lines']) and k in ps:
            plan['same'].append(k)
        else:
            (plan['changed'] if k in os_ else plan['new']).append(k)
            todo += ns[k]['lines']
    open(f'{work}/todo_en.md', 'w', encoding='utf-8').write('\n'.join(todo))
    json.dump(plan, open(f'{work}/plan.json', 'w'), indent=1)
    words = sum(len(l.split()) for l in todo)
    print(f"iguais: {len(plan['same'])} · alteradas: {len(plan['changed'])} · novas: {len(plan['new'])} · removidas: {len(plan['removed'])} · a traduzir: ~{words} palavras")
    print('alteradas/novas:', ', '.join(plan['changed'] + plan['new']) or '—')

def assemble(work, old_pt):
    plan = json.load(open(f'{work}/plan.json'))
    ps, _ = split(open(old_pt, encoding='utf-8').read().split('\n'))
    tp = f'{work}/todo_pt.md'
    ts, _ = split(open(tp, encoding='utf-8').read().split('\n')) if os.path.exists(tp) else ({}, [])
    out = []
    for k in plan['order']:
        if k in plan['same']: out += ps[k]['lines']
        else:
            if k not in ts: sys.exit(f'falta traduzir a secção {k}')
            out += ts[k]['lines']
    open(f'{work}/new_pt.md', 'w', encoding='utf-8').write('\n'.join(out))
    print('ok →', f'{work}/new_pt.md')

if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'prepare': prepare(*sys.argv[2:6])
    elif c == 'assemble': assemble(sys.argv[2], sys.argv[3])
    else: print(__doc__)
