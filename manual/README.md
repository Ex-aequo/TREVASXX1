# Manual PT — como atualizar

O separador **📖 Manual** do painel lê `manual_pt.json` (na raiz do repositório). Esta pasta guarda as fontes e as ferramentas para o regenerar.

Ficheiros
- `manual_en_vNNN.md` / `manual_pt_vNNN.md` — corpo do manual (EN oficial e tradução pt_PT), mesma estrutura linha a linha.
- `glossario.md` — regras e glossário EN→pt_PT (termos de jogo em português com o inglês entre parênteses).
- `tools/update_manual.py` — compara um manual novo com o antigo e prepara só o que mudou.
- `tools/build_manual.py` — gera `manual_pt.json` (HTML por secção) a partir dos .md.
- `tools/check_chunk.py` — verifica a tradução (nº de linhas, tabelas, números).

Quando sai um manual novo (pedir ao Claude: "atualiza o separador do manual com este ficheiro")
1. `python3 tools/update_manual.py prepare MANUAL_NOVO.docx manual_en_vANTIGA.md manual_pt_vANTIGA.md trabalho/`
   → lista as secções novas/alteradas e escreve `trabalho/todo_en.md`.
2. Traduzir `todo_en.md` → `trabalho/todo_pt.md` (glossário + mesma estrutura linha a linha).
3. `python3 tools/update_manual.py assemble trabalho/ manual_pt_vANTIGA.md` → `trabalho/new_pt.md`
4. `python3 tools/build_manual.py trabalho/new_en.md trabalho/new_pt.md vNOVA manual_pt.json`
5. Guardar `new_en.md`/`new_pt.md` como `manual_en_vNOVA.md`/`manual_pt_vNOVA.md`, subir o `CACHE_NAME` em `sw.js` e publicar.
