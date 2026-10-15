#!/usr/bin/env python3
"""Extrai a vista 3D (e os escudos, se existirem) de um player_page_Vnnn.html / player_page_MAX_Vnnn.html.
Uso: extract_3d.py <player_page.html> <pasta_destino_do_painel>
Escreve <destino>/mapa3d.html e (só na versão MAX, que traz as imagens embutidas) <destino>/images/shields/*.png"""
import re, sys, json, os, base64
src, dest = sys.argv[1:3]
s = open(src, encoding='utf-8', errors='ignore').read()
k = s.find('const PP3D_SRC = ')
if k < 0: sys.exit('PP3D_SRC não encontrado — a página não tem vista 3D')
k += len('const PP3D_SRC = ')
lit = s[k:s.find('";\n', k) + 1]
doc = json.loads(lit)
doc = doc.replace('<title>Army Map 3D Demo</title>', '<title>Mapa 3D</title>')
os.makedirs(dest, exist_ok=True)
open(os.path.join(dest, 'mapa3d.html'), 'w', encoding='utf-8').write(doc)
print('mapa3d.html', len(doc) // 1024, 'KB')
ms = re.findall(r"'(images/shields/shield-[^']+)':'data:image/[a-z]+;base64,([A-Za-z0-9+/=]+)'", s)
if ms:
    os.makedirs(os.path.join(dest, 'images', 'shields'), exist_ok=True)
    for name, b in ms:
        open(os.path.join(dest, 'images', 'shields', name.split('/')[-1]), 'wb').write(base64.b64decode(b))
    print(len(ms), 'escudos')
else:
    print('sem escudos embutidos (usa a versão MAX para os extrair)')
