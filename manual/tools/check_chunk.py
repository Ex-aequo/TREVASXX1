import sys,re
n=sys.argv[1]
en=open(f'/home/claude/manualwork/en/c{n}.md',encoding='utf-8').read().split('\n')
pt=open(f'/home/claude/manualwork/pt/c{n}.md',encoding='utf-8').read().split('\n')
def sig(L):
    return (len(L), sum(1 for l in L if l.startswith('|')), sum(1 for l in L if l.startswith('> ')), sum(1 for l in L if re.match(r'^\*\*(PART|\d+\.\d)',l)), sum(1 for l in L if l.startswith('- ')))
print(n,'EN',sig(en),'PT',sig(pt),'OK' if sig(en)==sig(pt) else 'DIFF')
nums=lambda L:sorted(re.findall(r'\d+(?:[.,]\d+)?',' '.join(L)))
a,b=nums(en),nums(pt)
from collections import Counter
d=Counter(a)-Counter(b); e=Counter(b)-Counter(a)
print(' nums missing',sum(d.values()),'extra',sum(e.values()), list(d.items())[:8], list(e.items())[:8])
