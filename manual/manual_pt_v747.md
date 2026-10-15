**PART I — INTRODUÇÃO**

**1.1 O que é o TREVASXXI?**

O TREVASXXI é um jogo de estratégia por turnos (turn-based), assíncrono e executado no navegador, para 2–N jogadores e um GM (Mestre de Jogo). Os jogadores comandam uma de sete raças assimétricas que competem por território (territory), recursos (resources) e domínio num mapa (map) de hexágonos. O jogo não tem condição de vitória integrada — as condições de vitória são definidas pelo GM para cada campanha.

Em cada turno (turn), os jogadores enviam ficheiros de ordens (orders) ao GM. O GM executa o Processador de Turnos (Turn Processor) para resolver todas as ordens em simultâneo e distribuir um relatório (report) por reino.

**1.2 As Três Aplicações**

O TREVASXXI funciona através de três aplicações HTML separadas. Todas correm localmente num navegador. Não é necessário nenhum servidor para jogar — mas a **assinatura e a cifragem** dos relatórios exigem um contexto seguro (localhost ou HTTPS, por exemplo python3 -m http.server); aberto através de file://, o Processador de Turnos corre sem assinatura disponível. Os ficheiros são trocados em JSON.

|   |   |   |
|---|---|---|
| **Aplicação** | **Quem a usa** | **Finalidade** |
| Editor de Mapas (Map Editor) (map_editor_V\<N\>.html, o N mais alto) | Só o GM | Criar e editar o mapa da campanha; definir terreno (terrain) dos hexágonos, locais de produção (sites) e recursos iniciais |
| Processador de Turnos (Turn Processor) (turn_processor_V\<N\>.html, o N mais alto) | Só o GM | Carregar todos os ficheiros de ordens enviados pelos jogadores; processar o turno completo; gerar relatórios; o 🗺 **WORLD MAP** mostra o mundo inteiro tal como o GM o vê — os exércitos (armies) e as frotas (fleets) de todos os reinos, sem nada oculto — em vista plana ou, com **🧊 3D VIEW**, na mesma vista 3D que os jogadores têm |
| Página do Jogador (Player Page) (player_page_V\<N\>.html, o N mais alto — a que o GM enviou com o teu último relatório) | Cada jogador | Carregar o relatório pessoal; emitir ordens; exportar o ficheiro de ordens para envio |

**Usa sempre a Página do Jogador que o GM distribuiu com o teu último relatório.** A página tem um número de versão. O Processador de Turnos mantém um **limiar** (floor) — a página mais antiga cujas ordens aceita sem aviso (EXPECTED_PP_VERSION) — e eleva-o sempre que uma página mais antiga pré-visualizaria um preço, um rendimento ou uma regra que o motor já não respeita, ou ofereceria uma ordem que o motor agora recusa. Uma página igual ou acima do limiar não gera aviso mesmo que exista uma mais recente, pelo que a regra continua simples: usa a última página que o GM enviou. Uma página abaixo do limiar ainda submete — o servidor é a autoridade e o turno é processado — mas pré-visualiza preços, rendimentos e capacidade de pagamento que o motor já não respeita. O registo do GM assinala todos os ficheiros de ordens provenientes de uma página desatualizada, e o teu próprio relatório traz um cartão **"Outdated Player Page"** com a versão que usaste e o limiar (vai buscar a página mais recente, que pode ser mais nova do que o limiar), com o lembrete de que todas as ordens foram cobradas às taxas do motor, não às da página; o teu relatório mostra também um aviso quando a lista de unidades da página está desatualizada — recarrega a página que o GM enviou quando acontecer qualquer um dos casos. Duas cópias podem partilhar o mesmo número de versão se o GM editou a página no próprio ficheiro, pelo que "o mesmo número" não é prova; usa o ficheiro que o GM enviou por último.

O separador **Kingdom** da Página do Jogador tem também um botão **🖨 Print Map (PDF)**: imprime a vista atual do mapa (aquela para a qual deslocaste e ampliaste) numa página em paisagem — escolhe *Guardar como PDF* na janela de impressão do navegador. É uma comodidade para registo e partilha e não tem qualquer efeito na jogabilidade.

**Os separadores Army e Navy.** Cada separador abre com uma **tabela-resumo**, uma linha por exército ou frota: o que faz neste turno (a marcha e o destino, a postura (stance) em vigor, recrutas, um embarque, uma transferência; para as frotas a rota, Bloqueio (Blockade), Raide ou Caça (Hunt), navios em construção, o alvo de desembarque), o seu estado, tropas (ou navios) e poder, manutenção (upkeep) por turno, hexágono e onde se encontra — as frotas mostram também a sua **carga**. Uma linha marcada com **⚠** precisa de ti, e o cabeçalho conta-as (*⚠ 2 need you*). Por baixo da tabela dos exércitos, os custos de movimento por terreno da tua raça são listados uma só vez.

- **Todos os cartões começam recolhidos** numa linha: nome, local, poder, estado, manutenção e a ordem deste turno. Um cartão recolhido que precisa de ti di-lo nessa linha — *⚠ no order — stands at ×1.00* (um exército que ficaria parado sem postura), *⚠ no troops — struck at end of turn unless you recruit*, ou *⚠ needs you · …* para qualquer outra coisa que peça uma decisão: um cerco (siege) às tuas muralhas, um cerco teu que estagnou, falhas ou ponto de rutura, uma oferta de ligação de um aliado, uma Siege March sem nenhum sítio para cercar, um exército a bordo de uma frota, estado abaixo de 34%, uma frota que não é amiga no mesmo hexágono, uma frota ligada prestes a ser arrastada para uma guerra por um bloqueio. A linha da tabela e a linha do cartão concordam sempre.

- **▸ Open** e **▾ Fold** em cada cartão. Um cartão que abres fica aberto enquanto lhe dás ordens; ▾ Fold fecha-o. Um exército ou frota que levantas neste turno abre com a lista de unidades (roster) pronta.

- **Dentro de um cartão.** A lista abre em **＋ Recruit / build** (frotas: **＋ Build ships** — uma frota no mar mostra apenas *Return to port to build*) como uma linha por unidade; passa o rato sobre o nome de uma unidade para ver a sua descrição, e a lista abre sozinha enquanto houver recrutas em fila para esse exército. **Reorganise** (dividir e transferir) abre em **▸ Split / transfer** e fica aberto enquanto houver uma operação em fila. O cabeçalho mostra a manutenção total do exército ou da frota por turno, e a caixa Enlisted Units mostra a sua parte de tropas de outros povos (§2.12.1). Quando Blockade, Raid ou Hunt não podem ser usados, os motivos partilham uma só linha: *Unavailable here: …*.

> ***▶ Example — reading the Army and Navy tabs.** Hyperborea abre o seu separador Army no turno 41. A tabela diz I HOST — ⚠ no order — stands at ×1.00, II HOST e V HOST — Ambush (in force), IV HOST — Garrison (in force), e o cabeçalho ⚠ 1 needs you; os quatro cartões estão recolhidos. Um clique na linha de I HOST abre o seu cartão; escolher 🛡 Defensive limpa o aviso, e o cartão fica aberto enquanto as restantes ordens são planeadas. No separador Navy, III ARMADA — com 26% de estado — diz ⚠ needs you · holds at sea: aberta, é enviada de volta a casa para descansar.*

**1.3 Como Funciona uma Campanha**

1\. O GM cria o mapa no Editor de Mapas e exporta o estado inicial do jogo.

2\. O GM executa o Turno 0 no Processador de Turnos para gerar os relatórios iniciais dos jogadores.

3\. Cada jogador recebe o seu ficheiro de relatório do Turno 0 e carrega-o na Página do Jogador.

4\. Os jogadores emitem ordens e exportam o seu ficheiro de ordens. *(Um turno a meio pode ser posto de parte: 💾 TEMP SAVE na barra superior grava um \`draft\_\<Kingdom\>\_turn\<N\>.json\` com todas as ordens em fila até ao momento — a primeira gravação pergunta onde o guardar (escolhe a pasta onde mantens a Página do Jogador; o Chrome e o Edge lembram-se dela em todas as gravações e carregamentos seguintes, os outros navegadores usam a pasta Transferências); mais tarde, carrega de novo o relatório do mesmo turno e usa 📂 TEMP LOAD nesse rascunho para retomares exatamente onde ficaste. O rascunho não é um ficheiro de ordens — SUBMIT TURN continua a ter de ir para o GM — e só serve para o reino e o turno em que foi gravado. Também restaura o que as tuas ordens já tinham gasto do mapa: a população que um recrutamento levantou, a tripulação que um navio levou e os colonos que uma fundação enviou, juntamente com os contadores que limitam o recrutamento à parte de um turno. No TEMP LOAD a página volta a verificar a regra de nunca coexistir: uma marcha ou rota guardada pertencente a uma unidade que é membro de uma ligação é descartada com um aviso — um membro segue o seu líder, e um rascunho de uma página mais antiga poderia, de outro modo, plantar no mapa um trajeto fantasma impossível de cancelar. Um rascunho também recorda de que processamento do turno veio o seu relatório: se o GM processou esse turno de novo e carregas o rascunho sobre o novo relatório, a página pergunta primeiro —* This draft was made on ANOTHER processing of Turn N… *— porque o rascunho traz de volta as posições e os stocks de exércitos do processamento antigo. Cancelar mantém o relatório que carregaste (planeia a partir dele); OK carrega o rascunho de qualquer forma, e as tuas ordens indicam então ao GM em que processamento foram planeadas)* *(Num telemóvel — na vertical ou na horizontal — a página está organizada para o dedo: o menu é uma faixa no topo que fica no ecrã enquanto deslizas, cada separador abre no seu início, e o texto e os botões têm tamanho adequado ao dedo. Os seletores de ficheiros mostram todos os ficheiros, de modo que um relatório que a tua aplicação de correio guardou com outro nome (\`report\_….json.txt\`) ainda pode ser escolhido; a página verifica o conteúdo e avisa quando um ficheiro não é um relatório. Um computador mantém a disposição habitual; numa janela demasiado estreita para toda a barra superior, a barra passa para uma segunda linha, mantida à direita, de modo que SUBMIT TURN fica no canto superior direito.)* *(Num telemóvel ou tablet, a exportação — e 💾 TEMP SAVE — abre a folha de partilha do sistema em vez de uma transferência. Para o ficheiro de ordens (SUBMIT TURN), envia-o diretamente ao GM por correio ou conversa. Para um rascunho de TEMP SAVE, escolhe Guardar em Ficheiros e conserva-o tu — não é para o GM, e 📂 TEMP LOAD abre-o a partir de Ficheiros. Cancelar a partilha não envia nem guarda nada; carrega de novo no botão. Num ecrã tátil, toca num botão a cinzento (ou prime longamente qualquer botão) para ler porque está desativado ou o que faz — as explicações que um rato mostra ao passar por cima.)*

5\. O GM recolhe todos os ficheiros de ordens e carrega-os no Processador de Turnos juntamente com o estado atual do jogo. *(Dois ficheiros do mesmo reino — um jogador que voltou a exportar — são assinalados na lista de ranhuras assim que são carregados, ficando marcado para manter o submetido mais tarde; o turno não será processado enquanto um deles não for removido.)* *(Cada execução de processamento grava um id no seu \`gm_state\` e em cada relatório, e o ficheiro de ordens traz de volta o id do relatório em que foi planeado. Se processares um turno duas vezes, envia os relatórios da execução cujo \`gm_state\` mantens: um ficheiro de ordens planeado na outra execução é assinalado na lista de ranhuras e no registo — os seus exércitos podem não estar onde as suas ordens esperam. O turno é processado na mesma.)*

6\. O GM executa o turno. O TP processa todas as fases (phases), gera um relatório por jogador mais um registo do GM.

7\. Os jogadores carregam o seu novo relatório. O ciclo repete-se a partir do passo 4.

> ***▶ Example — a turn processed twice.** O GM processa o turno 52 (execução 1), repara num ficheiro de ordens tardio do reino A e processa o turno de novo com ele (execução 2). Os relatórios da execução 2 seguem por engano, mas o gm_state_turn52.json da execução 1 é o que é mantido. A planeia o turno 53 sobre o relatório da execução 2, em que o seu Army II ainda está um hexágono aquém das muralhas; na execução 1, o estado de que o turno 53 continua, o Army II já está acampado junto às muralhas. Quando o GM carrega as ordens do turno 53 de A, a linha da ranhura de A fica vermelha — ⚠ planned on another processing of last turn (report run T52-…, gm_state run T52-…) — e o registo abre com ⚠ Orders From Another Run. O turno ainda pode ser processado; o GM decide se o processa mesmo assim ou se envia a A o relatório certo e pede novas ordens. Um jogador que faça **TEMP LOAD** de um rascunho feito sobre o relatório da outra execução é questionado primeiro, porque o rascunho traz de volta as posições dos exércitos dessa execução.*

**Option A State Architecture.** O Processador de Turnos é a única autoridade sobre todo o estado do jogo. Quando o TP carrega os ficheiros de ordens dos jogadores, substitui imediatamente todo o estado submetido pelos jogadores pelo estado do jogo autoritativo do GM antes de processar quaisquer ordens. Os jogadores não podem obter vantagem manipulando o seu ficheiro de estado submetido. Todos os efeitos das ordens são reaplicados de raiz sobre o estado autoritativo.

**1.3.1 Adicionar um Reino a uma Campanha em Curso (GM)**

Um novo jogador pode juntar-se a uma campanha que já está em curso. O Editor de Mapas exporta um **GM State Patch** que leva o estado em curso mais o recém-chegado, e o Processador de Turnos introduz o recém-chegado numa fase *Mid-campaign Starters* durante o processamento seguinte. Faz isto **entre dois processamentos** — depois de os relatórios do turno N terem saído, antes de o turno N+1 ser processado — sobre o gm_state_turnN.json que o TP acabou de escrever (guarda uma cópia intacta).

**Antes de começares.** Tem à mão os dados do jogador (nome do reino, raça, cor, nome do jogador, correio eletrónico, telefone, palavra-passe) e o nome do senhor — os nomes de personagens (characters) são únicos em todo o mundo, incluindo os dos mortos. Decide o início: os valores por omissão sorteados são ouro 2,500–4,000, comida 1,500–2,500, ferro 100–250, cavalos 0–20, madeira 100–500, pedra 100–500, sem exército e sem frota.

**No Editor de Mapas**

1\. **Import JSON** → escolhe gm_state_turnN.json. O editor confirma *"GM State Turn N imported"* e passa para o modo de patch. A capital ★ de cada reino existente aparece a partir das marcas de sede da campanha (o TP nunca persiste capital_hex; a capital em vigor é o hexágono marcado como sede de recrutamento) — nada para voltar a clicar. A partir daqui usa apenas o botão dourado **Export GM State Patch** — o *Export JSON* simples grava um mapa nu, sem exércitos, recursos nem diplomacia, e repunha a campanha a zero.

2\. No painel do reino **adiciona o reino**: raça, cor, os campos do jogador e o nome do senhor. Qualquer reino que não estivesse no estado importado é marcado automaticamente como inicial (starter) na exportação.

3\. **Pinta os hexágonos do reino.** Cada hexágono que lhe atribuíres precisa de uma **construção** de uma família que a sua raça possa usar (§3.7), ou não tem população e não rende nada. Pintar sobre um hexágono de outro reino transfere-o; os exércitos que lá estão não são movidos — verifica primeiro o mapa.

4\. **Designa a capital** com o botão ★ no cartão do reino, depois clica no hexágono. A exportação recusa um reino sem capital; o patch grava esse hexágono como sede de recrutamento do recém-chegado e capital original, pelo que é o terreno de recrutamento desde o primeiro turno. (Nos reinos existentes o ★ é apenas de visualização — uma sede só muda por sucessão, §2.13.10.)

5\. Opcional — **Starter Setup** no cartão do reino: recursos iniciais exatos (um campo em branco mantém o valor sorteado); tropas iniciais como linhas unitId contagem, introduzidas como Army I na capital; navios iniciais como linhas shipId contagem, introduzidos como Fleet I num local de **porto** possuído que tem de estar vazio de frotas. O TP valida os ids contra a lista da raça e **descarta** os desconhecidos com um aviso no registo do GM.

6\. **Export GM State Patch.** O editor executa as suas verificações (terrenos retirados, capitais designadas, nomes de senhores duplicados, mapa circular (wrap)) e escreve gm_state_patch_turnN.json: o mapa inteiro com **todos os campos de campanha por hexágono intactos** (população, dano às muralhas, cercos em curso, marcas de sede, reivindicações de origem), o estado de cada reino existente intocado, os preços de mercado e as bandeiras da campanha, e o recém-chegado assinalado como inicial sem estado ainda. Voltar a pintar um hexágono para um dono diferente retira ao antigo dono o cerco e a sede nele, mas mantém a sua gente. Alterar a **família ou o nível** de uma construção existente dá-lhe uma muralha nova e completa para o novo nível — o registo do GM seguinte mostra uma linha *Walls Reseeded* por cada hexágono assim, o que é esperado (um patch intocado não mostra nenhuma). A população acima do novo teto fica onde está e simplesmente deixa de crescer (§3.8); **remover** uma construção remove a sua população, e qualquer cerco a ela, consigo — nunca retires o hexágono de sede ★ de um reino: a sede fica lá de qualquer forma (§2.13.10), pelo que os seus exércitos se reuniriam num hexágono vazio sem nada para recrutar; o editor avisa antes de exportar. Voltar a pintar terreno remodela as rotas marítimas e os caminhos terrestres de todos — certifica-te de que nenhuma frota ou exército está parado nos hexágonos que alteras, ou a navegar por eles.

**No Processador de Turnos**

7\. Carrega gm_state_patch_turnN.json **em vez do** ficheiro de estado, com as ordens do turno N+1 dos outros jogadores como habitual. O novo reino não submete nada neste turno.

8\. **Processa o turno.** A fase *Mid-campaign Starters* corre primeiro: introduz o estado do recém-chegado (recursos, Army I e Fleet I se definidos, o seu senhor mais um conjunto de candidatos à corte de três, opinião 90, imposto 5%, em **paz** com todos — aliado do seu suserano, se definiste um — e memória explorada da sua própria terra) e escreve um **relatório inicial**, report\_\<Kingdom\>\_turnN+1_starter.json. A bandeira de inicial é consumida: o processamento seguinte trata o reino como um reino normal.

9\. Envia ao recém-chegado esse relatório inicial e a Página do Jogador atual. Com relatórios cifrados (§1.2), configura primeiro o jogador — o relatório inicial é escrito cifrado como qualquer outro.

10\. A partir do turno N+2 o novo jogador submete ordens como todos os outros.

**Duas coisas que apanham os GM.** O patch tem de ser o estado do turno **atual** — um mais antigo faria recuar no tempo todos os reinos passivos. E um ficheiro de ordens que nomeie um reino que não está no mapa, ou o novo reino antes de o seu relatório inicial ter sido emitido, é recusado de imediato (§2.5), pelo que o novo reino não pode apresentar ordens antes de existir o seu relatório inicial.

**1.3.2 Verificar um Turno Processado (GM)**

Quando um jogador relata algo estranho, volta a executar o turno em vez de adivinhar. node tools/replay_turn.mjs \<gm_state_turnN.json\> \<orders-folder\> repete o turno **N+1** sem interface com o Processador de Turnos mais recente: carrega o estado através do carregador do próprio Processador de Turnos, toma todos os orders\_\*\_turn\<N+1\>.json da pasta, valida o resultado e imprime os cartões de cada reino (--kingdom Name e --grep text restringem a saída).

- **Emparelha os ficheiros corretamente.** As ordens que produziram report\_\*\_turnK pertencem com gm_state_turn\<K-1\>. Um desencontro é recusado, e a ferramenta lista os turnos para os quais tem ordens — nunca mudes a etiqueta de um ficheiro de ordens para o fazer correr: isso aplica as mesmas ordens duas vezes sobre um estado que já as contém.

- **Não altera nada.** --out \<new folder\> escreve os relatórios repetidos apenas para estudo: não estão cifrados, foram sorteados com dados novos e não levam dados de contacto dos jogadores — **nunca os envies aos jogadores**.

- **Mostra como um turno se resolve, não os números exatos.** Os dados são relançados e é usado o Processador de Turnos mais recente, pelo que os números que os teus jogadores receberam serão diferentes.

**1.4 Como Ler Este Manual**

- floor(x) = arredondar para baixo. ceil(x) = arredondar para cima. min(a,b) / max(a,b) = mínimo/máximo de dois valores.

- Os **termos com maiúscula inicial** são termos de jogo definidos. Todos os termos aparecem no Glossário da Parte X.

- Os intervalos numéricos A–B são inclusivos em ambas as pontas.

- Todos os valores têm origem nos atuais turn_processor_V\<N\>.html e player_page_V\<N\>.html (o N mais alto na pasta do projeto). Os comentários de código inline nesses ficheiros estão frequentemente desatualizados; as atribuições reais de constantes são as que fazem fé.

**1.5 Código de Conduta e Aviso Legal (Code of Conduct & Disclaimer)**

O texto abaixo é o Código de Conduta do Jogador autónomo que todos os jogadores recebem; é reproduzido aqui na íntegra para que o manual esteja completo por si só. Aderir a uma campanha significa aceitá-lo.

Lê isto antes de aderires. Ao aderires a uma campanha de TREVASXXI, aceitas tudo o que se segue.

**1. Um projeto de passatempo**

TREVASXXI é um jogo de estratégia gratuito e sem fins comerciais, dirigido por um Mestre de Jogo (Game Master, GM) voluntário para um grupo privado de jogadores. Nada nele tem valor monetário no mundo real, e nada pode ser comprado, vendido ou trocado por dinheiro.

**2. Fornecido "tal como está"**

O jogo está em desenvolvimento ativo. As regras, os preços, as unidades e o equilíbrio podem mudar entre campanhas e, quando necessário, durante uma. Podem ocorrer erros de software, turnos perdidos ou atrasados, perda de dados e interrupções de campanha. O GM agirá de boa-fé para corrigir os problemas, mas não dá quaisquer garantias e não aceita responsabilidade por qualquer perda, direta ou indireta. O GM pode suspender, alterar ou terminar uma campanha a qualquer momento.

- Quando o GM verifica que um turno foi processado incorretamente, pode corrigir o resultado ou processar esse turno de novo. Isso não é uma alteração de decisão; é repor o jogo nas suas próprias regras.

**3. Ficção**

Todos os reinos, personagens, povos, religiões e acontecimentos são fictícios. Alguns nomes, títulos e culturas inspiram-se livremente na história, na mitologia e na literatura de fantasia. Isto inclui títulos como Sultanato, Emirado ou Jarldom, e povos como os Aesir ou os Imperiais. São usados apenas como ambientação e não expressam qualquer opinião sobre, nem apoio a, qualquer cultura, fé, nação ou pessoa reais. O jogo retrata a guerra e a conquista como parte do seu cenário; não tolera a violência.

**4. Sem afiliação**

TREVASXXI não é afiliado, apoiado nem patrocinado por qualquer autor, editor, estúdio ou titular de direitos cujas obras possam ter inspirado o seu cenário, nomes ou arte. Todas as marcas registadas pertencem aos respetivos proprietários.

**5. Os teus dados**

- O GM guarda o teu nome de jogador, o teu endereço de email e os ficheiros de jogo que envias e recebes (ordens e relatórios de turno). São usados apenas para dirigir a campanha.

- Os relatórios de turno são enviados por email através de um serviço de entrega de terceiros, que trata o teu endereço exclusivamente para os entregar.

- Os outros jogadores veem o nome e o estandarte do teu reino nos seus próprios relatórios, e a sua posição em todas as classificações — apenas posições, nunca os teus valores.

- Os teus dados não são vendidos, nem partilhados para qualquer outro fim.

- Quando uma campanha está encriptada, as ordens e os relatórios são protegidos com uma palavra-passe. Mantém a tua privada: o GM não consegue recuperar dados bloqueados por uma palavra-passe perdida.

- Podes pedir ao GM a qualquer momento que apague os teus dados de contacto depois de saíres de uma campanha.

**6. Código de Conduta**

Aderir a uma campanha significa aceitar este Código de Conduta. Há tolerância zero: infringir a regra 6.1 ou 6.2 implica a expulsão da campanha (6.6).

\##### 6.1 Respeito

- Sem insultos, assédio, ameaças ou discriminação contra qualquer jogador ou o GM, dentro ou fora do jogo (chat, email, redes sociais, presencialmente). A rivalidade, a traição e a diplomacia dura entre reinos fazem parte do jogo; os ataques pessoais à pessoa por trás de um reino não.

- Mantém as disputas fora do jogo fora do jogo. Se algo te incomodar, diz-o ao GM em privado.

- Não publiques mensagens, relatórios ou capturas de ecrã de outro jogador sem o seu consentimento.

\##### 6.2 Jogo limpo

- Sem batota nem adulteração de qualquer tipo: editar ficheiros de ordens, relatórios de turno, dados de gravação ou a Página do Jogador (Player Page); falsificar ou reenviar ordens; explorar erros; usar scripts ou outras ferramentas para escrever ordens ou ler ficheiros de jogo por ti; ou obter os relatórios, mensagens ou palavra-passe de outro jogador sem o seu consentimento.

- Encontraste um erro? Comunica-o ao GM — não o uses. Explorar deliberadamente um erro conhecido conta como batota.

- Um jogador, um reino. Sem contas alternativas, e sem jogar (ou dar ordens) por um reino que não é o teu.

- Não te faças passar por outro jogador ou pelo GM, e não adiras sob a identidade de outra pessoa. Os pseudónimos são permitidos.

- A tua palavra-passe é pessoal. Nunca a partilhes — nem com outros jogadores, nem com o GM.

\##### 6.3 Diplomacia

- A diplomacia fora do jogo (chat, email, chamadas, presencialmente) é permitida.

- Apenas as ordens que o GM recebe alteram o jogo. Uma promessa feita dentro ou fora do jogo é cumprida ou quebrada pelos jogadores que a fizeram; o GM não a faz cumprir.

\##### 6.4 Compromisso

- Envia as ordens até ao prazo que o GM anunciar. Um turno falhado é jogado passivamente: o rendimento, a manutenção e as tuas defesas continuam a funcionar, mas não é executada nenhuma ordem nova.

- Falhar turnos repetidamente sem aviso implica a perda do teu reino. O GM anuncia, antes de a campanha começar, o número de turnos falhados que implica a perda de um reino.

- Se precisares de abandonar a campanha, diz-o ao GM. Um reino que seja abandonado, perdido ou expulso passa a ser controlado pelo GM ou é retirado do mapa, à escolha do GM.

\##### 6.5 O GM

- As decisões do GM sobre regras, resultados e disputas são definitivas. Pede esclarecimentos, mas aceita a resposta.

- O GM não tem favoritos e não partilha informação privada entre jogadores.

- O GM pode atualizar este documento. Os jogadores são informados de cada alteração, e continuar a jogar significa aceitar a versão atualizada.

\##### 6.6 Expulsão Infringir a regra 6.1 ou 6.2 implica a expulsão da campanha, a critério exclusivo do GM, sem aviso e sem recurso.

Ao aderires a uma campanha de TREVASXXI, confirmas que leste e aceitas este Aviso Legal e Código de Conduta.

**PARTE II — REGRAS BASE (PART II — CORE RULES)**

**2.1 O Mapa de Hexágonos (The Hex Map)**

O jogo disputa-se numa **grelha hexagonal de deslocamento Odd-R**: uma matriz retangular de hexágonos em que as linhas de número ímpar estão deslocadas meio hexágono para a direita. Os hexágonos são identificados por coordenadas (col, row).

Cada hexágono tem:

- Um tipo de **Terreno (Terrain)** (ver Parte III)

- Um **local de produção (Site)** opcional (quinta, mina, porto, serração, pedreira ou forja — ver §3.6)

- Um valor de **População (Population)**

- Um **Reino (Kingdom)** proprietário (ou sem dono/neutro)

- Opcionalmente: um contador de **Progresso do Cerco (Siege Progress)** e o ID do reino de **Cercado Por (Besieged By)**

**Mover o mapa.** Arrasta o mapa do reino com o rato para o mover e roda a roda para ampliar; os botões **+** / **−** (teclas + e -) também ampliam, e **Fit to map** (tecla 0) mostra-o por inteiro. Num ecrã tátil, arrasta-o com um dedo e faz o gesto de pinça com dois para ampliar; enquanto o dedo estiver no mapa a página não se desloca — desloca-a a partir de fora dele.

**Lupa.** O botão 🔍 por baixo de **Fit to map** ativa uma lente redonda que segue o cursor sobre o mapa do reino (teclado: L, e Esc fecha-a). Não aumenta a imagem — volta a desenhar essa parte do mapa com maior ampliação, de modo que o terreno, os ícones de locais e os numerais dos exércitos se mantêm legíveis. Num telemóvel, segue o teu dedo. A lente nunca altera a posição do mapa: desliga-a e ficas exatamente onde estavas.

**Vista 3D.** O botão **🧊 3D VIEW** no fim da linha de camadas do mapa do reino troca o mapa por uma vista tridimensional do mesmo terreno; carrega nele outra vez para regressar. Num telemóvel (um ecrã com 700 píxeis de largura ou menos) a vista 3D ocupa o ecrã inteiro, com a linha de camadas por cima. Mostra o que o mapa plano te mostra — o mesmo nevoeiro e os mesmos hexágonos recordados, os teus exércitos e frotas onde as tuas ordens em fila os levam, e os exércitos e frotas estrangeiros que o teu reconhecimento revela. Uma força estrangeira aparece como uma companhia ou um navio sob o escudo e o nome do seu reino, e nada mais: a sua força permanece desconhecida, tal como no mapa plano. Passa o cursor sobre um hexágono para ver os detalhes — num ecrã tátil, toca nele. Arrasta para rodar, arrasta com o botão direito para deslocar e usa a roda para ampliar (num ecrã tátil: um dedo roda a vista, dois dedos em pinça ampliam e deslocam), ou usa o painel no ecrã (teclado: WASD ou as setas deslocam, Q/E rodam, R/F inclinam, +/− ampliam, H repõe a vista). Os botões de camada filtram a vista 3D como filtram o mapa plano: com **Terrain** desligado, o terreno mantém o relevo e o mar o seu nível, mas perdem as cores, as árvores e os picos; **Constructions+** mostra apenas os povoados, qualquer cerco à sua volta, as fronteiras dos reinos e os sinais de obras das tuas ordens de povoado em fila, cada povoado com o seu código de construção. Um exército é desenhado como uma companhia de figuras que cresce com os seus soldados — uma figura para um soldado, duas para dois, e a partir de três soldados cerca de uma figura por cada dez (nunca menos de três), até 12 (6 em **Detail: low**) — pelo que mostra o tamanho e a composição, não uma contagem de cabeças: todos os tipos de tropa que contém aparecem enquanto houver espaço (primeiro as máquinas de cerco, como as suas máquinas; acima do limite os tipos mais pequenos ficam de fora), e um exército ainda sem soldados mostra apenas o seu estandarte. Cada povo constrói e navega no seu próprio estilo, e os povoados de um reino pirata aparecem como refúgios de piratas; todas as frotas navegam no estilo do seu reino, sejam quais forem os cascos que contêm, e as frotas de um reino pirata hasteiam a bandeira negra com a caveira e os ossos cruzados. Um povoado é desenhado com muralha apenas se a tiver. Um hexágono de que só te lembras é desenhado esbatido em sépia, tal como foi visto pela última vez — seja qual for o que o botão **Terrain** diga — e a sua dica diz isso mesmo; um povoado recordado é desenhado com muralha se o seu nível tiver uma, e o seu dono não é recordado. **Labels** esconde as etiquetas de nomes, nunca os sinais de obras; **Detail: low** desliga as sombras e reduz as florestas e as companhias para computadores mais lentos, e um telemóvel ou tablet começa nele, a menos que escolhas o contrário. Um dispositivo cujo navegador não consegue executar gráficos 3D é informado disso e mantém o mapa plano; se um telemóvel recuperar a sua memória gráfica (por mudança de aplicação ou falta de memória), a vista fica em pausa com uma mensagem e regressa por si — ou fecha-a e abre-a de novo. Se a vista parar alguma vez com uma mensagem de erro, recarrega a página; o mapa plano não é afetado. A vista serve apenas para observar: as ordens dão-se no mapa plano e nas outras vistas. Os escudos dos reinos vêm da pasta de imagens da página, tal como os do mapa plano.

**Ecrã inteiro.** O botão **⛶ FULLSCREEN** ao lado de **🧊 3D VIEW** preenche o ecrã com o mapa do reino — a linha de camadas e o mapa, plano ou 3D — e podes alternar entre os dois em ecrã inteiro. Carrega em **✕ EXIT FULLSCREEN** ou em Esc para regressar; o mapa plano mantém a sua posição e ampliação. Os navegadores que não conseguem mostrar um elemento da página em ecrã inteiro, como o Safari no iPhone, não mostram o botão.

**Ordens de construção no mapa.** Um hexágono com uma das tuas ordens de construção em fila (§2.11.1: construir, melhorar ou arrasar um local de produção, fundar ou melhorar um povoado, reparar a sua muralha; uma por hexágono) mostra um sinal de obras — um sinal de aviso triangular de cantos arredondados: um trabalhador preto com uma picareta sobre branco, dentro de uma borda vermelha — no canto superior direito do hexágono, onde estão os ícones de produção, ou como um pequeno emblema no canto inferior esquerdo do ícone de produção que já lá esteja. Um arrasamento mostra o sinal invertido: um trabalhador branco sobre vermelho, dentro de uma borda branca. O sinal acompanha a camada do que se constrói — **Productions** para um local de produção, **Constructions** ou **Constructions+** para um povoado — e aparece também na vista 3D. A mudança de um acampamento Nómada mostra antes a sua seta de rota. Passa o cursor sobre o hexágono e a sua dica indica a ordem, no mapa plano e na vista 3D. O sinal permanece até cancelares a ordem ou carregares o relatório do turno seguinte.

**Povoados no mapa.** A camada **Constructions** marca cada povoado com o seu código de construção numa pequena etiqueta; **Constructions+** mostra apenas os povoados, cada um como a imagem do seu povo (§2.11.9) com o seu código por baixo.

**2.2 Adjacência (Adjacency)**

Cada hexágono tem até seis vizinhos, calculados com tabelas de direção ODD-R que têm em conta a paridade das linhas. A mesma função de adjacência rege a validação do percurso de movimento, a adjacência de cerco e o reconhecimento do nevoeiro de guerra (um bloqueio não a usa — atua sobre o porto onde a frota se encontra, §2.9.3). Os hexágonos na fronteira do mapa têm menos de seis vizinhos.

**2.3 Propriedade (Ownership)**

Um hexágono pertence ao reino cujo ID está registado no seu campo de reino. A propriedade muda quando:

- Um exército toma um hexágono estrangeiro indefeso durante a Fase 5

- Um exército vence uma batalha campal ou um assalto e o defensor é destruído ou retira (Fase 5)

- Uma frota desembarca um exército que vence a batalha anfíbia resultante (Fase 6)

- Um cerco cai automaticamente (Pré-Fase, antes da Fase 1)

Capturar um hexágono elimina qualquer Progresso do Cerco nesse hexágono.

**2.4 A Sequência do Turno (The Turn Sequence)**

A tabela abaixo lista todos os passos **na ordem exata em que o Processador de Turnos (Turn Processor) os executa** — lê-a de cima para baixo e essa é a sequência em que as tuas ordens (orders) se resolvem.

|                     |                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Passo**           | **Nome**                                                                                                                                                                                                                                                                                                                                                                                      |
| Pré-Fase 1          | Reposição de Estado Opção A (Option A State Reset)                                                                                                                                                                                                                                                                                                                                            |
| Pré-Fase 2          | Criar / Dissolver / Reaplicar Embarque (Create / Disband / Embark Re-apply)                                                                                                                                                                                                                                                                                                                   |
| Pré-Fase 2b         | Recrutamento (Recruitment) (os soldados e as máquinas juntam-se aos seus exércitos — antes de todas as batalhas do turno)                                                                                                                                                                                                                                                                     |
| Pré-Fase 3          | Resolução de Cerco e Postura de Assalto (exércitos cercados fixados, surtidas ordenadas combatidas, depois os sitiantes estacionários avançam e os Assaltos tomam de assalto). **No teu relatório estes têm o seu próprio cabeçalho ⚙ PRE-PHASE 3 — Sieges & Assaults, antes de PHASE 1 — Income** — aconteceram mesmo primeiro, antes de o dinheiro do turno ser contado e muito antes de qualquer marcha, e uma cidade tomada aqui caiu antes de tudo isso |
| Pré-Fase 4          | Queda Automática do Cerco (Siege Auto-Fall)                                                                                                                                                                                                                                                                                                                                                   |
| Fase 1              | Crescimento da População e Rendimento (Population Growth & Income)                                                                                                                                                                                                                                                                                                                            |
| Fase 2              | Manutenção e Fome (Upkeep & Starvation)                                                                                                                                                                                                                                                                                                                                                       |
| Fase 3              | Mercados e Construção (Markets & Construction)                                                                                                                                                                                                                                                                                                                                                |
| Fase 4              | Navios e Contratação (Ships & Hire) (o recrutamento decorre na Pré-Fase 2b)                                                                                                                                                                                                                                                                                                                   |
| Fase 4.5            | Transferências de Exércitos (Army Transfers)                                                                                                                                                                                                                                                                                                                                                  |
| Fase 4.6            | Transferências de Frotas (Fleet Transfers)                                                                                                                                                                                                                                                                                                                                                    |
| Fase 5              | Movimento de Exércitos e Combate Terrestre (Army Movement & Land Combat) (primeiro o varrimento de acampamento: os exércitos em guerra acampados juntos combatem)                                                                                                                                                                                                                             |
| Fase 6              | Movimento Naval (Navy Movement)                                                                                                                                                                                                                                                                                                                                                               |
| Fase 7              | Espiões (Spies)                                                                                                                                                                                                                                                                                                                                                                               |
| Fase 8              | Diplomacia (Diplomacy) (mudanças de postura)                                                                                                                                                                                                                                                                                                                                                  |
| Fase 8 · Vassalagem | os juramentos do último turno respondidos (os aceites jurados), renúncia, e depois os juramentos deste turno oferecidos; uma guerra entre suserano e vassalo termina o vínculo no momento em que começa, em qualquer fase (resolve-se **antes** das mensagens)                                                                                                                                |
| Fase 8 · Mensagens  | mensagens, \[CEASEFIRE\], \[TRIBUTE\]                                                                                                                                                                                                                                                                                                                                                         |
| Fim do turno        | Transferências de Recursos (Resource Transfers) — primeiro as ofertas de caravana do último turno respondidas, depois send_resource + \[TRIBUTE\] (direto / oferta / recusado consoante a posição, §2.8.3)                                                                                                                                                                                     |
| Fim do turno        | Varrimentos de forças vazias e de integridade de ligações (tudo o que esvazie uma força: nenhum exército sem soldados nem frota sem cascos, e nenhuma ligação através de uma relação quebrada, sobrevive ao turno)                                                                                                                                                                            |
| Fim do turno        | Experiência de Forja (Forge Experience) (exércitos Anões)                                                                                                                                                                                                                                                                                                                                     |
| Fase 10             | Mexericos e Rumores (Gossip & Rumours) — um rumor anónimo por reino com um Mestre de Espiões, para todos os reinos (§8.8.7)                                                                                                                                                                                                                                                                   |
| Fim do turno        | Experiência das Personagens (Character Experience) (crédito de turno de competência de cargo, §7.10)                                                                                                                                                                                                                                                                                          |
| Fim do turno        | Geração do Relatório (Report Generation)                                                                                                                                                                                                                                                                                                                                                      |

Nenhuma fase pode afetar o resultado de uma fase anterior no mesmo turno. Três pontos de ordenação surpreendem habitualmente os jogadores:

- **Os recrutas são pagos antes de tu seres pago.** O recrutamento (Pré-Fase 2b) é cobrado a partir da tesouraria de fecho do último turno, antes do rendimento, do tributo e dos preenchimentos de mercado deste turno (§2.6a).

- \**Os cercos avançam em* dois sítios diferentes*. Um sitiante estacionário avança na Pré-Fase 3*\*, antes do rendimento, e um avanço acima do limiar faz o hexágono cair na Pré-Fase 4 (§2.6b). Uma marcha sobre um forte estrangeiro assalta-o antes na Fase 5 (§5.8.0), e uma Marcha de Cerco acampa — fechando o anel de imediato se for suficientemente forte — e avança a partir do turno seguinte.

- **A vassalagem resolve-se antes das mensagens.** Apesar das etiquetas internas "8b/8c", o Processador de Turnos executa o bloco da **vassalagem** *antes* do bloco das **mensagens** — pelo que um vínculo de vassalagem (e a sua aliança forçada) já está em vigor quando uma mensagem \[TRIBUTE\] ou \[CEASEFIRE\] do mesmo turno é lida.

**2.5 Pré-Fase 1: Reposição de Estado Opção A (Pre-Phase 1: Option A State Reset)**

Antes de quaisquer ordens serem processadas, o Processador de Turnos descarta todos os dados de estado do ficheiro de ordens submetido por cada jogador e substitui-os pelo estado correspondente com autoridade do GM. Isto neutraliza qualquer estado que o jogador possa ter manipulado — recursos, contagens de unidades dos exércitos, registos diplomáticos. Apenas as listas de ordens são lidas dos ficheiros submetidos.

**Um reino sem estado guardado.** O turno 0 e um início a meio de campanha escrevem ambos o estado de cada reino nos registos do GM, pelo que a sobrescrita acima tem sempre algo para repor. Se um reino chegar a um turno sem ele, o Processador de Turnos verifica os recursos submetidos face aos intervalos em que são sorteadas as reservas iniciais de todos os reinos — comida 1,500–2,500, ouro 2,500–4,000, ferro 100–250, cavalos 0–20, madeira 100–500, pedra 100–500 — alterados apenas pelas ordens de mercado desse mesmo ficheiro, a última por mercadoria tal como o mercado as executa: partindo do topo de cada intervalo, as suas vendas (não mais do que essa reserva) e depois as suas compras (não mais do que o ouro compra), cada ordem contada apenas até ao limite por ordem do mercado (§2.11.4) e apenas em unidades inteiras, dão o máximo que um ficheiro honesto pode declarar. Qualquer valor acima disso, ou abaixo de zero, recusa o ficheiro inteiro; um valor abaixo do intervalo é aceitável, já que a Página do Jogador deduz da reserva que declara os gastos em fila. Essas ordens de mercado não são executadas de novo — as reservas que o ficheiro declara já as incluem — pelo que não geram cartão de mercado nem movem preços. Tudo o resto — exércitos, frotas, corte, candidatos, diplomacia, vassalagem, espiões, ofertas e caravanas — é reconstruído como no início da campanha de um reino, e as outras ordens do ficheiro são aplicadas sobre isso — os seus custos são cobrados às reservas declaradas, que a Página do Jogador já tinha reduzido por elas, pelo que o registo do GM assinala todos os reinos que seguem este caminho para o GM lhes dar um estado guardado. Um ficheiro de ordens de um reino recém-adicionado cujo relatório inicial ainda não foi emitido é recusado de imediato.

**Ordens malformadas.** Uma ordem que a Página do Jogador não poderia ter escrito — uma postura diplomática que não seja guerra, paz, aliança ou comércio, ou uma dirigida ao teu próprio reino — é descartada e referida no registo do GM; o resto do ficheiro mantém-se. As coordenadas em qualquer ordem são lidas como números inteiros — uma que não seja um número não aponta para nenhum hexágono, pelo que a sua ordem é recusada como "hex not found"; uma rota ou uma lista de alvos de ligação que não seja uma lista conta como vazia.

> ***⚠ O que isto significa —** Tudo o que alterares na tua Página do Jogador e que não seja expresso como uma ordem é descartado quando o GM processa o turno. Editar à mão os teus recursos, contagens de tropas ou diplomacia no ficheiro não resulta em nada — o TP sobrescreve tudo com os seus próprios registos e só depois volta a aplicar por cima a tua lista de ordens. A vantagem: também não podes perder progresso por uma falha da interface ou um mau gravar, porque a cópia do GM é a única fonte de verdade. Trata o teu ficheiro como uma forma de enviar ordens, nunca como uma forma de definir o estado.*

**2.6 Pré-Fase 2: Criar / Dissolver / Reaplicar Embarque (Embark Re-apply)**

Depois de a Opção A repor todo o estado, create-army, disband-army, **dismiss-units** (disband_units, abaixo), disband-fleet, **scuttle-hulls** (disband_ships, abaixo), embark-army, create-fleet e todas as ordens de ligar/desligar (link_armies, link_accept, unlink, link_fleets, fleet_link_accept, fleet_unlink — §5.11) são reaplicadas ao estado autoritativo antes de qualquer outro processamento. A Opção A apagou os objetos de exército (army) e frota (fleet) a que outras ordens (orders) se referem; este passo de reaplicação restaura-os antes de a Fase 1 arrancar. Estes tipos de ordem não são processados de novo na Fase 4, na Fase 5 nem na Fase 6.

> ***▶ Dispensar unidades — parte de um exército, não o exército todo.** No separador Exército, cada linha de unidade de um exército em terra tem um botão **✂**: escolhe quantas unidades desse tipo dispensar (qualquer número até à pilha inteira) e saem do exército quando o turno é processado, nesta mesma Pré-Fase 2 — pelo que a sua manutenção (upkeep) e comida (food) deixam de contar neste turno. **Nada regressa:** nem ouro, nem material, e ninguém volta à população de uma cidade — os soldados dispensados desaparecem simplesmente, tal como numa Dissolução completa. Também se podem dispensar engenhos. Dois limites, aplicados pelo Processador de Turnos e espelhados na página: **não a bordo de uma frota** (desembarca primeiro — um exército embarcado não pode ser dissolvido nem dispensado, §2.14.6), e **não se podem dispensar soldados abaixo da tripulação de que os engenhos do exército precisam** (5 soldados por engenho, o mesmo rácio (ratio) que a salva das muralhas usa — dispensa primeiro os engenhos). Um terceiro: **dispensar as tuas próprias tropas não pode deixar o exército com mais de 20% de tropas de outros povos** (§2.12.1). A página deduz previamente as unidades e mostra **−N ✂** na linha, com um **↩** para anular até as ordens serem enviadas; o relatório traz um cartão por dispensa, com a contagem, o remanescente e a regra de não reembolso. Só podem sair unidades que já constem do efetivo: os recrutas deste turno chegam na Pré-Fase 2b, depois de as dispensas se resolverem, por isso a página limita a contagem ao stock existente (anula antes o recrutamento), e enquanto uma transferência de unidades tocar o exército no mesmo turno o ✂ é recusado — cancela primeiro a transferência (a anulação da própria transferência restaura o exército como estava). Dispensar os últimos soldados de um exército esvazia-o, e um exército vazio não sobrevive ao turno (§2.12): é riscado dos registos no fim do turno e o seu lugar é libertado.*
>
> ***▶ Afundar cascos — parte de uma frota, não a frota toda.** O gémeo naval: no separador Marinha, cada linha de navio tem um botão **✂** — escolhe quantos desse casco (hull) afundar e são desmantelados quando o turno é processado, na Pré-Fase 2, pelo que a sua manutenção deixa de contar neste turno. **Nada regressa** (nem ouro, nem ferro, nem madeira), qualquer tipo de casco pode sair — incluindo cascos de presa (prize) — e funciona **em qualquer lugar**, no mar ou no porto. O único limite, aplicado pelo Processador de Turnos e espelhado na página, é o **espaço de carga**: uma frota que transporte um exército pode afundar os cascos que lhe **sobrem**, mas não aqueles de que o exército ainda precisa. Os cascos que ficariam têm de continuar a comportar a tonelagem desse exército — infantaria conta 1, montada conta 2 — e um transportador nunca pode afundar-se até ficar sem casco nenhum. É o mesmo teste que uma **transferência de navios** de uma frota carregada usa (§2.14.6). A recusa é **total, nunca um parcial silencioso**, e o cartão indica a aritmética — "Fleet I carries Army I (tonnage 150); the hulls it would keep hold 100." Afunda menos, ou desembarca primeiro. A **Dissolução da frota inteira** é diferente e continua absoluta: é recusada enquanto houver qualquer exército a bordo, tanto pela página **como** pelo motor. A página deduz previamente os cascos e mostra **−N ✂** com um **↩** para anular; o relatório traz um cartão por afundamento, com a contagem, o remanescente e a regra de não reembolso. Uma frota ligada pode afundar livremente (só uma Dissolução completa quebra a ligação). Aplicam-se os mesmos dois limites do próprio turno: os cascos lançados neste turno ainda não podem ser afundados (anula antes a construção), e uma transferência de navios que toque a frota bloqueia o ✂ até ser cancelada. Afundar o último casco esvazia a frota, e uma frota vazia não sobrevive ao turno (§2.12).*

**Rejeição de criação de frota**: uma ordem create_fleet é rejeitada neste passo se o reino for **Orc ou Anão** (restrição de raça, abaixo), se o alvo **não for um porto que o reino possua** no início do turno, se o reino já tiver **5 frotas** em campo (o limite a nível do reino, §2.14.2), ou se o porto já contiver **3 frotas em qualquer combinação não beligerante** — o limite de coabitação (§2.14.2), que é um limite POR HEXÁGONO e se mantém em 3 mesmo que um reino possa ter cinco. **Uma frota criada neste turno ocupa o seu cais desde o momento em que é comissionada, com ou sem cascos** — não podes criar uma quarta no mesmo porto no mesmo turno, tal como não se pode criar um quarto exército num hexágono de recrutamento cheio. Uma frota **neutra** ou **aliada** atracada no teu porto **não** te bloqueia — limita-se a ocupar uma vaga no mesmo limite contra o qual as tuas próprias frotas se acumulam. **Uma inimiga também não**: a nova frota é comissionada e combate-a como defensora do porto na varredura de coabitação da Fase 6, antes de qualquer frota se mover, com os cascos que lhe tenham sido construídos nesse turno — a ×1.00, uma vez que o bónus de porto pertence apenas a uma frota que começou o turno lá (§5.9.2); sem cascos, é afundada no estaleiro (§2.14.2). Quando rejeitada, a frota não é comissionada, não se gastam recursos, e o jogador recebe uma notificação de bloqueio que indica qual dos casos se aplicou. A Página do Jogador oferece apenas portos que possuis, recusa um porto cuja pilha esteja cheia e assinala um porto com uma frota **inimiga** como um combate em vez de um bloqueio (*"your new fleet fights it this turn"*); funciona com dados de nevoeiro do turno anterior e não vê uma frota que chegue no mesmo turno — a verificação de pilha do Processador de Turnos apanha esses casos.

**Restrição de raça**: os reinos Orc e Anão não podem ter frotas. As ordens create_fleet e build_ship dessas raças são rejeitadas pelo Processador de Turnos, e a secção Marinha da Página do Jogador é substituída por um aviso de "não disponível".

**2.6a Pré-Fase 2b: Recrutamento (Recruitment)**

**O recrutamento de unidades resolve-se aqui**, logo a seguir ao passo de reaplicação e **antes de todas as batalhas do turno** — os cercos e assaltos em curso da Pré-Fase 3 tal como as marchas da Fase 5. Uma regra, para os dois lados: **as tropas recrutadas neste turno combatem neste turno, faça o seu exército o que fizer.** O preço dessa posição:

- **Pago pela tesouraria tal como o relatório a mostra** — antes do rendimento, do tributo e das ordens de mercado deste turno, pelo que "comprar ferro e depois recrutar" é um circuito de dois turnos (a verificação da página: §2.12.1). Uma recusa por falta de materiais di-lo no seu cartão ("paid in Pre-Phase 2b, from the treasury as your report showed it"), e os próprios cartões de recrutas trazem um distintivo **PRE-PHASE 2b · Recruitment** e ficam em primeiro lugar no relatório.

- **Faturado no turno em que chegam.** A manutenção e a comida da Fase 2 incluem os novos homens (a página reserva essa fatura, §2.12.1).

- **Limite sobre a população que o relatório mostra** (antes do crescimento, §2.12.1).

- **Os recrutas frescos são mobilizados com estado 100** e diluem o estado do exército pelo número de efetivos *antes* de este combater.

- **Um hexágono que tomes neste turno recruta para ti a partir do turno seguinte.** O recrutamento corre antes da tempestade da pré-fase, da queda automática e das marchas que capturam hexágonos, pelo que um exército acampado numa fortaleza inimiga ainda não pode recrutar aí (regra do hexágono próprio/aliado); os engenhos são a exceção (construídos em qualquer lugar, §5.8.6).

- **A Fase 1 conta também os recrutas.** A reprodução Orc procria sobre a contagem de infantaria *incluindo* os recrutas deste turno (§2.9.10), e a manada de cavalos procria sobre o que sobra depois de pagos os recrutas montados deste turno (§2.9.9). Ambos de propósito.

- **Recrutar para uma guarnição no ponto de rutura compra homens que se rendem uma hora depois.** Um recruta destinado a uma guarnição cujo hexágono cai automaticamente neste turno (Pré-Fase 4) é pago e as unidades perdem-se com a guarnição.

As contratações e construções de navios não mudaram — continuam na Fase 4 (§2.12).

**2.6b Pré-Fase 3: Resolução de Posturas de Cerco e Assalto (Siege & Assault Stance Resolution)**

Entre o passo de reaplicação e a Queda Automática de Cerco, o Processador de Turnos resolve as posturas (stances) de todos os exércitos que estão **a manter posição** — um exército que não submeteu nenhuma ordem de movimento neste turno:

- A **surtida (sally) ordenada** combate-se aqui primeiro, antes de qualquer tique de cerco ou assalto (assault) nesse hexágono (§2.13.7). Ninguém faz surtidas sem ordem.

- Um **sitiante estacionário** (um exército em postura de cerco já parado numa construção amuralhada inimiga) **avança o seu Progresso de Cerco em 1 aqui, antes da Fase 1** — a menos que um exército que não lhe seja amigo — neutro incluído — esteja acampado no exterior: nesse caso combate esse exército, e a batalha custa o progresso do turno (§5.8.2). Esta é a razão discreta por que um cerco paciente se resolve um segmento inteiro mais cedo do que um em marcha: o seu contador avança *agora*, e se esse tique o fizer ultrapassar o limiar o hexágono cai logo no passo seguinte (§2.7), tudo antes do rendimento.

- As ordens de postura no local (siege, assault, ambush, defensive, garrison) para exércitos estacionários são lidas neste ponto, juntamente com a postura **guardada** de cada exército (Siege, Defensive, Garrison e Ambush mantêm-se em vigor até serem alteradas; Assault é uma ordem por turno — §5.4). Apenas siege, assault e sally *atuam* aqui (a Surtida primeiro, §2.13.7); um Cerco ou um Assalto combate primeiro qualquer exército hostil acampado fora das muralhas (§5.8.0). garrison também importa aqui: uma ordem Garrison dada neste turno já confere o seu ×1.30 a um assalto resolvido neste bloco. Um exército **cercado** (besieged) mantém Garrison ou ordena Sally (§2.13.7). defensive, no resto dos casos, produz efeito quando alguém ataca o exército na Fase 5/6. Nas muralhas, **todas as posturas exceto Garrison ficam FORA** a partir deste ponto (§5.8.0). Uma Ambush **inválida** é guardada e comporta-se como Defensive durante todo o processo. Um exército sem ordem de postura **e sem nenhuma guardada** conta como estando em movimento (um cercado conta como Garrison); um reino que não submeteu ordens mantém as suas posturas guardadas, e os seus exércitos **sem** postura nas suas muralhas ou nas de um amigo são postos em Garrison enquanto houver espaço e nenhum exército em guerra com ele estiver acampado no exterior (§5.8.0).

- **Os recrutas já lá estão.** O recrutamento corre na Pré-Fase 2b (§2.6a), pelo que um cerco ou assalto estacionário ataca com os recrutas deste turno, e uma guarnição que é assaltada, ou um exército que faz uma surtida, também combate com eles.

Um exército *em movimento* leva a sua postura para o seu combate da Fase 5 — e uma marcha para um forte estrangeiro é um **assalto à chegada** da Fase 5 (§5.8.0), não um evento de pré-fase. Assim, o combate resolvido aqui é o tique de cerco do sitiante estacionário, a surtida ordenada de um exército cercado, e um assalto completo às muralhas por qualquer exército estacionário em postura de assalto já parado numa fortificação inimiga (um assaltante repelido permanece no hexágono). Este passo não gasta recursos e não faz marchar nenhum exército; só as batalhas movem exércitos aqui — os sitiantes batidos por uma Surtida recuam, e um assaltante que toma as muralhas avança para dentro.

**2.7 Pré-Fase 4: Queda Automática do Cerco (Siege Auto-Fall)**

Se algum hexágono tiver um contador de Progresso de Cerco que **exceda** o seu Limiar de Cerco, o hexágono cai para o sitiante antes da Fase 1. Isto corre antes do rendimento e antes de qualquer movimento de exércitos (as transferências de recursos acontecem no fim do turno, pelo que não são afetadas).

**Limiares** (Thresholds, §5.8.3): uma construção amuralhada vulgar cai quando o progresso excede 4 — **cinco** turnos de pressão; a sede de recrutamento (muster seat) quando excede 5 — **seis**.

**Na queda automática:**

- O hexágono (hex) passa para o sitiante. O Progresso de Cerco volta a 0. Não se combate nenhuma batalha (battle): o exército do sitiante, já no seu novo hexágono, encontra-se agora dentro das muralhas (walls).

- Todos os exércitos do **dono** das muralhas que estejam dentro **rendem-se**: todas as unidades são destruídas. Cada um deles é uma Guarnição (Garrison) cercada, seja qual for a ordem que deu (§2.13.7). O exército de outro reino lá dentro — mesmo um em Garrison — não é a guarnição do dono: é expulso (abaixo). O sitiante apodera-se do arsenal rendido (60–80% do seu ferro e cavalos, §2.13.11).

- Os outros exércitos defensores nesse hexágono — na prática apenas um exército do dono que esteja fora das suas próprias muralhas (qualquer exército do dono que não esteja em Garrison), pois todos os do dono lá dentro são Guarnições cercadas — retiram (retreat) (até 3 saltos por terra — nunca atravessando o mar, §5.5.6), abandonando os seus engenhos (§5.8.6). **Se não for encontrado hexágono de retirada, são abatidos na debandada, exatamente como o exército de um terceiro em guerra com o sitiante** (o ponto abaixo): o sitiante despoja os destroços como faria a um arsenal rendido (§2.13.11), e sofres uma penalização de **−2 a −4 de opinião** pelo exército perdido, somada à do próprio povoado. Em qualquer dos casos o destino do exército é comunicado: um cartão para a debandada, ou um cartão para o recuo.

- **Ninguém dentro das muralhas é espectador quando elas caem** (§5.6): todos os reinos lá dentro estão em guerra com o sitiante, pelo que o seu exército recua pelas regras de retirada acima ou é abatido se encurralado — nunca *"holds its camp"*, nunca uma última resistência em tempo de paz.

- O exército de um **terceiro reino** acampado **fora** das muralhas do hexágono caído que seja **aliado mútuo, vassalo ou suserano do sitiante permanece** — o terreno pertence agora a um amigo seu, e recebe o cartão *"holds its camp"* (a mesma regra de um hexágono assaltado, §5.11). Qualquer outro exército de um terceiro reino é **expulso** — recua pelas mesmas regras de retirada e o seu dono é notificado. Se não tiver para onde fugir, a sua relação com o sitiante decide: um reino **em guerra** com o sitiante é **abatido na debandada** — o sitiante despoja os seus destroços (§2.13.11), e o seu dono sofre a penalização normal de opinião do perdedor (−2 a −4); um reino **em paz** com ele faz antes uma **última resistência**, exatamente como quando as muralhas são assaltadas — declara guerra, combate aí o exército do sitiante, e retoma o terreno se vencer.

> ***▶ Exemplo — as muralhas caem.** A cidade amuralhada de Aldoria (12,7) tem o Exército I de Aldoria e o Exército II da sua aliada Sylvane. O III de Gruk-Mor, acampado às portas, ordena Siege no turno 5; esse primeiro tique cerca a cidade (progresso 1) e declara guerra também a Sylvane. A partir do turno 6 ambos os exércitos lá dentro estão cercados; nenhum ordena Sally. O progresso sobe 2, 3, 4 (o cartão do defensor diz Collapse imminent!), depois 5 no turno 9 — e na Pré-Fase 4 do turno 9 a cidade cai. O I de Aldoria **rende-se** (um exército cercado é uma Guarnição; Gruk-Mor recupera 60–80% do seu ferro e cavalos). O II de Sylvane, aliado e não guarnição do dono, é **expulso** até 3 hexágonos por terra — ou abatido e despojado se não tiver para onde ir. O III de Gruk-Mor, agora no seu próprio hexágono amuralhado, fica dentro das muralhas.*

- Qualquer frota (fleet) defensora atracada no hexágono caído **faz-se ao mar** — corre para o hexágono de **mar alto** livre mais próximo, e só pode viajar *através* de água para lá chegar. Uma frota não pode escapar por terra, nem se refugiar no porto amigo ao lado (um porto é um hexágono de terra): o mar é o seu único caminho. Pode navegar **por** um hexágono que outra frota já ocupe, mas tem de terminar num livre — vazio, ou uma pilha amiga com espaço sob o limite de 3 frotas. **Se não houver água livre ao alcance, a frota é destruída no ancoradouro** — as tripulações incendeiam os cascos em vez de entregar uma esquadra ao inimigo, e qualquer exército a bordo perde-se com ela. Ambas as perdas são comunicadas.

- **Degradação** (§5.6.3): o local de produção (site) e o povoado perdem cada um um nível, nunca abaixo do nível 1.

- **O que te é comunicado**: o dono do hexágono caído recebe um cartão que indica o **tamanho e a forma da força que o tomou** — Besieging force: 88 troops (16 mounted, 72 foot). Viste-os acampados fora das tuas muralhas durante turnos, pelo que esta é a força mais bem observada do jogo e o relatório di-lo claramente. Conta todos os exércitos do reino sitiante que estavam efetivamente a pressionar o cerco, e chega até ti quer tenhas submetido ordens nesse turno quer não. **Não** indica os tipos das suas unidades — isso continua a ser trabalho de um espião (§8.8; vê a escada de informação em §2.13.4).

- Sem lançamentos de combate. A queda do cerco é administrativa — mas faz oscilar a opinião como uma batalha ganha e uma perdida (§8.5.3).

**2.8 Transferências de Recursos (Resource Transfers) (fim do turno)**

Há duas formas de enviar recursos — **o mesmo sistema subjacente**: o painel **🐪 Shipments → 📦 Send Resources** (ordens send_resource, uma por mercadoria) **e** o símbolo \[TRIBUTE: amount resource\] dentro de uma mensagem diplomática (§8.7). Qualquer um pode enviar **ouro (gold), comida, ferro, cavalos, madeira ou pedra**, deduzidos no **fim do turno**, *depois* de toda a tua própria despesa (manutenção, construção, recrutamento) — apenas o excedente, e parcial se ficares aquém — e transportados por caravana (caravan, §2.8.2) para quem a tua posição permitir (§2.8.3). A página permite **um envio por mercadoria por turno**; se um ficheiro de ordens trouxer mesmo assim vários envios da mesma mercadoria para o mesmo reino, o Processador de Turnos **funde-os numa única caravana** que leva a soma (um cartão de expedição para cada lado, um lançamento de bandidos) — nunca várias.

**2.8.1 Devolver terra capturada (Returning captured land) (transferência de hexágono)**

Um reino pode devolver um hexágono ao seu **dono original** — o reino que o detinha no início da campanha — se os dois estiverem numa **aliança mútua** (ambos os lados com postura de Aliança; unilateral é inerte, como em todo o lado). Ordena-o a partir do painel **Shipments → 📦 Send Resources** ("🤝 Return Captured Land", listado automaticamente quando tens hexágonos elegíveis); o hexágono, a sua população e qualquer local de produção mudam de soberano no **fim do turno**, intactos — é uma entrega pacífica, não uma conquista, pelo que não se aplica degradação de conquista. No máximo **um hexágono por reino por turno**.

Restrições: só o reino original do hexágono o pode alguma vez receber (cada hexágono lembra-se para sempre do seu fundador — nunca pode ser oferecido a mais ninguém, e a terra que era neutra no início da campanha nunca pode ser "devolvida"); capitais, sedes de recrutamento e hexágonos cercados não podem ser cedidos.

**Nota do GM — preenchimento de origem para campanhas em curso:** no primeiro processamento depois desta atualização, cada hexágono é carimbado com o seu dono ATUAL como origem permanente (os hexágonos neutros são carimbados como de ninguém). Os hexágonos conquistados ANTES da atualização aparecem, portanto, como terra original do conquistador. Para tornar um desses hexágonos devolvível, edita uma vez o gm_state_turnN.json atual: encontra o hexágono ("col":C,"row":R) e define o seu "origin_kingdom" para o id do verdadeiro reino original. As campanhas novas não precisam de preenchimento.

**2.8.2 Mecânica das Caravanas (Caravan Mechanics)**

**Tempo de trânsito:** 1 turno, mais 1 por cada 5 hexágonos completos de distância entre as sedes de recrutamento das capitais (1 + ⌊distance/5⌋, mínimo 1) — mesmo vizinhos diretos enviam a caravana *neste* turno, e ela \**chega no fim do* próximo *turno. Exemplo: uma distância de 20 hexágonos → \`1 + floor(20/5)\` = 5 turnos de trânsito*\*; expedida no fim do turno 5, chega no fim do turno 10.

**Risco de bandidos** — Em cada turno que a caravana passa na estrada — incluindo o turno de chegada e qualquer perna de regresso — sofre um **ataque de bandidos de 3%, tudo ou nada**. As caravanas perdem-se por inteiro se o lançamento acertar; não há perda parcial. Tanto o remetente como o destinatário são notificados na expedição ("expect arrival at the end of turn N"), na chegada ou perda, e **ambos** são avisados se a caravana der meia-volta (abaixo) — o destinatário uma vez, *"The caravan of N \<commodity\> from \<sender\> turned back"*, para que uma remessa prometida nunca simplesmente desapareça da sua lista de Inbound. O registo do GM regista cada expedição, chegada e perda com todo o detalhe.

**Meia-volta por destruição do reino** — O estado do reino recetor é verificado em cada turno que a caravana passa na estrada, não apenas quando chega. No momento em que o reino de destino já não tiver sede de recrutamento ou deixar de existir, a caravana dá meia-volta e segue para casa, demorando a regressar tanto quanto já tinha viajado quando a verificação a apanhou. A carga é novamente creditada na tesouraria do remetente quando a caravana chega a casa. Se o reino do remetente também não tiver sede de recrutamento quando o regresso chegar, a caravana perde-se nas estradas — a carga dispersa-se, nunca é recuperada.

**Sem garantia de entrega** — As caravanas são frágeis. O lançamento de 3% por turno significa que uma viagem de 5 turnos tem uma **probabilidade de perda acumulada de 1 - (0.97^5) ≈ 14%** só por bandidos; uma meia-volta acrescenta um lançamento por turno de regresso. Os reinos de fronteira, ou os cercados bem dentro de território hostil, devem esperar que uma fração significativa das suas caravanas nunca chegue. Planeia em conformidade.

**Tributo de vassalagem** (o pagamento automático vassalo→suserano) continua **instantâneo** — é pago diretamente a cada turno, sem atraso de viagem. As ordens de compra/venda no mercado também se resolvem instantaneamente (Fase 3) — só as transferências diplomáticas de recursos (painel Send Resources + símbolo de mensagem \[TRIBUTE\]) viajam por caravana.

**O separador Shipments** reúne tudo o que está na estrada num só lugar: o painel 📦 Send Resources (com os envios em fila deste turno e os respetivos chips ✕ Cancel), uma lista **📤 Outbound** — cada caravana que tens em trânsito, com destino, mercadoria, quantidade, turno de expedição, turno de chegada e turnos restantes (uma caravana que deu meia-volta mostra antes **↩ returning home from \<kingdom\> · back turn N** — o seu turno de chegada significa agora *casa*, por isso sem seta e sem "arrives") — e uma lista **🤝 Caravan Offers** (ofertas de reinos sem pacto, com ✓ Accept / ✕ Decline, e as tuas próprias ofertas à espera de resposta — §2.8.3), uma lista **📥 Inbound** de todas as caravanas que outros reinos têm neste momento na estrada *para ti* (remetente, mercadoria, quantidade, turno de chegada, turnos restantes). Uma caravana criada por um símbolo \[TRIBUTE\] leva uma etiqueta **🏛 tribute** em qualquer das listas. A lista de entrada **não tem nevoeiro**: já foste informado na expedição pelo cartão *Caravan inbound*, por isso a lista limita-se a manter esse conhecimento visível até as mercadorias aterrarem. Ambas as listas são só de leitura — uma caravana expedida saiu das mãos do remetente e ninguém a pode chamar de volta.

**2.8.3 A quem podes enviar — ofertas de caravana (Caravan offers)**

**Porque existe a regra.** Quando uma caravana (caravan) parte, o cartão *Caravan dispatched* do remetente indica quantos hexágonos (hexes) de estrada separam as duas sedes de recrutamento (muster seats). Isso é útil para um amigo e perigoso nas mãos de qualquer outro: enviar 1 de ouro (gold) a um desconhecido diria exatamente a que distância fica a sede dele, e dois reinos a comparar notas poderiam determiná-la. Por isso é o **recetor** quem decide se um desconhecido pode saber isso.

**A regra — lida no fim do turno (turn), depois da diplomacia desse turno:**

|                                                                                                         |                                                                                                            |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **A tua posição perante o recetor**                                                                     | **O que acontece ao teu envio**                                                                            |
| **Pacto comercial (trade pact) ou aliança (alliance) mútuos** (ambos têm Trade ou Alliance), ou são **suserano e vassalo** | Enviado **diretamente**: deduzido e despachado no fim deste turno (§2.8.2).                               |
| **Em guerra (At war)** — um dos dois tem War                                                            | **Recusado.** Nada é deduzido, recebes o cartão *Shipment/Tribute not sent* e o inimigo não ouve nada.    |
| **Qualquer outro caso (neutro)** — incluindo um pacto que só *tu* tens                                  | Torna-se uma **oferta**. Nada sai das tuas reservas neste turno; o recetor decide no turno seguinte.      |

Como a posição é lida *depois* da diplomacia da Fase 8, um pacto comercial que ambos os lados concluam neste turno já envia diretamente, e uma guerra declarada neste turno já bloqueia o envio.

**Como decorre uma oferta.**

1\. **Turno N — envias.** O painel Send Resources assinala cada reino como *direct*, *offer* ou *at war* antes de escolheres. Para um recetor neutro, a tua ordem pendente diz *Offering…* e as tuas reservas **não** diminuem. Também **não ficam reservadas**, por isso mantém a quantidade total nas reservas até a oferta ser respondida. No fim do turno recebes o cartão *Caravan offered*, e o recetor recebe o cartão *Caravan offer*, que indica o teu nome e os bens e nada mais — nem distância, nem sede.

2\. **Turno N+1 — respondem.** A oferta aparece na lista **Shipments → 🤝 Caravan Offers** do recetor, com **✓ Accept** e **✕ Decline** (clica outra vez na resposta escolhida para a retirar). A tua própria cópia fica na mesma lista como *awaiting their answer*.

3\. **Fim do turno N+1 — o resultado.**

- **Aceite:** a caravana parte **com a quantidade total oferecida, ou não parte de todo**. Se no fim desse turno já não tiveres tudo, a oferta fica **nula**: nada é enviado, ambos os lados recebem o cartão *Caravan offer void*, não é mostrada qualquer distância e o recetor não é informado de quanto tinhas. O recetor concordou com *aquela* dádiva, por isso um remetente não pode oferecer 5,000 e enviar 1 só para ler o comprimento da estrada. Se a quantidade total sair, é uma caravana normal a partir daqui (§2.8.2): ambos os lados recebem os cartões de despacho/chegada, e passas a saber o comprimento da estrada. Foi isso que o recetor aceitou ao aceitar.

- **Recusada:** nada se move; ambos os lados recebem um cartão.

- **Sem resposta** (incluindo um recetor que não enviou ordens): a oferta **caduca** após esse único turno e recebes um cartão. Oferece de novo se ainda o quiseres.

- **Guerra entretanto:** se os dois reinos estiverem em guerra no fim do turno N+1, uma oferta aceite é recusada em ambos os lados.

O símbolo \[TRIBUTE: …\] segue a mesma regra do painel. Um tributo (tribute) a um neutro torna-se uma oferta e mantém a etiqueta 🏛 depois de aceite. Um tributo a um inimigo é recusado. A mensagem em si é entregue na mesma, porque só os bens ficam retidos. O separador Messages avisa-te de ambos os casos quando colocas a mensagem em fila. Se os dois trocarem \[CEASEFIRE\] no mesmo turno, a paz é feita antes de o tributo ser lido, pelo que o tributo sai como oferta em vez de ser recusado.

> ***▶ Exemplo — um turno, três envios** (reinos inventados). No turno 12, Valdoria envia 500 de ouro a cada um de três reinos:*
>
> *• **Ostmark** tem um pacto comercial com Valdoria, e Ostmark tem um de volta. Os 500 de ouro saem no fim do turno 12, o cartão de Valdoria diz "The road is 12 hexes of country; expect arrival at the end of turn 15" (1 + ⌊12/5⌋ = 3 turnos), e Ostmark recebe o cartão Caravan inbound.*
>
> *• **Kheshet** está em paz com Valdoria; não há pacto. A tesouraria (treasury) de Valdoria **não** diminui. Valdoria recebe o cartão Caravan offered, e Kheshet recebe "Valdoria offers you 500 gold … answer in the Shipments tab next turn", sem distância em lado nenhum.*
>
> *◦ Se Kheshet aceitar no turno 13, o ouro é deduzido e sai no fim do turno 13, desde que Valdoria ainda tenha os 500 nessa altura. Só agora o cartão de despacho de Valdoria indica o comprimento da estrada. Se Valdoria tivesse gasto até ficar com 499 de ouro, a oferta seria nula: nada sai e não é mostrada qualquer distância.*
>
> *◦ Se Kheshet recusar ou a ignorar, nada se move e Valdoria só fica a saber a resposta.*
>
> *• **Drakmoor** está em guerra com Valdoria. O envio é recusado de imediato; a página nem sequer o coloca em fila. Uma ordem editada à mão seria recusada no fim do turno, com Valdoria a receber "Shipment to Drakmoor not sent — no caravan crosses a war" e Drakmoor sem ser informado de nada.*
>
> *O resultado: o amigo de Valdoria recebe o ouro e Valdoria fica a conhecer a estrada até ele. O desconhecido guarda para si a sua localização, a menos que escolha aceitar o ouro. O inimigo não recebe nada e não fica a saber nada.*

**2.9 Fase 1 (Phase 1) — Crescimento da População e Rendimento (Population Growth & Income)**

Esta fase corre para cada reino. Todo o rendimento (income) é calculado a partir do estado do mapa pós-Pré-Fase e aplicado aos recursos (resources).

**2.9.1 Crescimento da População (Population Growth)**

Cada hexágono de construção (construction) possuído cresce 1–3% do **limite de população** do seu nível em cada turno, e pára no limite; os hexágonos vazios nunca crescem. Fórmula, limites e o caminho legado dos hexágonos vazios: §3.8. O cartão **👥 Population grew** do relatório (report) indica o ganho do turno e o novo total, e nomeia todos os povoados já no limite do seu nível: estes só voltam a crescer após uma melhoria.

**2.9.2 Rendimento do Terreno (Terrain Income)**

- **Hexágono de planície (sem local de produção)**: +1 de comida (food) por cada hexágono de planície elegível possuído

- **Não há ouro de terreno.** Todo o ouro vem do imposto (tax) sobre a população, dos portos e do comércio.

Um hexágono de planície com qualquer local de produção (site) **não** gera o +1 fixo de comida; o seu local substitui a produção de comida do terreno.

**2.9.3 Supressão por Bloqueio (Blockade Suppression)**

Uma frota (fleet) em postura de **Bloqueio (Blockade)** suprime todo o rendimento do porto (port) inimigo em que **se encontra**. Navega primeiro para o hexágono do porto — se uma frota inimiga estiver atracada lá, combates com ela à chegada, e ela defende-se com o bónus do porto se começou o turno lá (§5.9.2) — e ordena o Bloqueio no turno seguinte. Uma frota ao lado de um porto, ou no seu próprio porto junto a um inimigo, não bloqueia nada. Um porto bloqueado não gera ouro nem comida nesse turno. O bloqueio exige estado de guerra ativo entre os dois reinos. A posição tem um preço: uma frota que bloqueia perde **2 STATUS por turno** e não pode recuperar até se retirar (§5.10).

**Quem é informado.** O relatório de quem bloqueia traz *"Fleet N — Blockade active"* com o nome do porto em que se encontra, e o do proprietário traz *"N port(s) under naval blockade!"*, que nomeia cada porto bloqueado, cada frota que o bloqueia (o seu comandante, cascos, navios e WP tal como estava quando o bloqueio se iniciou — nunca a sua carga) e cada frota **ligada** a quem bloqueia, listada com esse bloqueio (o grupo bloqueia como um só: todos os membros pagam a sua manutenção (upkeep), e o reino de um membro que ainda não esteja em guerra contigo é declarado em guerra ao navegar nele — o cartão di-lo); qualquer outra frota estrangeira ali ancorada é listada como **não** bloqueando, com o motivo (em paz contigo, tua aliada, ou em guerra mas sem ordem de Bloqueio) e em cuja ligação navega.

**Guardado enquanto morde** (o gémeo naval do Cerco (Siege) guardado). Ordena-o uma vez e a frota mantém a posição turno após turno — a suprimir e a sangrar — sem necessidade de repetir a ordem, enquanto permanecer parada dentro de um porto de um reino com o qual está em guerra. No momento em que isso deixa de se verificar (paz, o porto muda de mãos, a frota é expulsa) a posição é abandonada e recebes o cartão *"Blockade lapsed"* com o motivo; uma ordem de navegação ou outra postura (stance) termina-o em silêncio. Um Bloqueio ordenado em qualquer outro lado nunca é guardado, e a ordem recebe o cartão *"Blockade not in force"* com o motivo. Um bloqueio que se mantinha no início de um turno mas não pode continuar — o porto mudou de mãos durante esse turno — recebe o cartão *"Blockade ends"*. **A Incursão (Raid) nunca é guardada** — é uma ação, ordenada a cada turno. A Página do Jogador (Player Page) carrega um bloqueio guardado já selecionado e marca o botão com *(in force)*; planear uma navegação para essa frota repõe-na em Sailing na página, tal como o motor fará.

**Uma frota que navega não bloqueia nesse turno** (o gémeo naval da regra dos exércitos): um Bloqueio registado junto a uma ordem de navegação é lido como Sailing durante todo o turno — sem supressão, sem sangria da posição — e a página mantém os dois mutuamente exclusivos em ambos os sentidos: uma navegação planeada recusa o gémeo do Bloqueio ("Set Sailing first"), e clicar em Bloqueio sobre uma navegação planeada apaga a viagem. Se o par ainda assim chegar ao motor (uma página desatualizada), o teu relatório traz *"Blockade not applied"* para essa frota, e se a frota já mantinha um bloqueio guardado o cartão diz que essa posição terminou: navega neste turno, ordena Bloqueio no turno seguinte sem navegação, e ele morde a partir de onde a frota então estiver. A Incursão é diferente: uma incursão de âncora dispara antes do movimento, pelo que "incursão e partida" é legal (§2.14.3).

**2.9.4 Rendimento dos Locais de Produção (Site Income)**

**Quinta (Farm)** (comida, sorteada de novo em cada turno por quinta — §3.6.1) e **Mina (Mine)** (ferro — §3.6.2) pagam a partir da população do seu hexágono neste passo.

**Porto** (planície em qualquer mapa construído hoje, **e, só para um reino Elfo, floresta costeira sob uma construção Élfica** (§2.11.1) — um povoado costeiro em colinas, montanha ou pântano não pode albergar um porto, pelo que o sítio onde o teu reino encontra o mar decide se podes ter uma marinha; tem de ser adjacente a pelo menos um hexágono de mar; **reinos Orc e Anão nunca podem construir ou melhorar um** — não têm marinha, pelo que um porto seria investimento morto. Um porto que conquistem continua a produzir para eles; simplesmente nunca cresce): ouro = floor(pop × goldMult) — Nv1: ×0.20, Nv2: ×0.40, Nv3: ×0.60 — **o ouro nunca é aleatório** comida = floor(pop × rate) — **nenhum nível de porto tem uma taxa fixa de comida: cada porto sorteia a sua, de novo, em cada turno** — Nv1 entre **0% e 5%** da população, Nv2 entre **0% e 10%**, Nv3 entre **0% e 15%**. O sorteio é por porto e por turno, pelo que dez portos pequenos se compensam enquanto um grande é um jogo de azar, e **uma má estação paga quase nada** — qualquer sorteio acima de 0% paga pelo menos 1 de comida, pelo que só um sorteio de exatamente 0% (possível, mas praticamente nunca visto) não paga nada. O ouro tem mínimo de 1 enquanto o hexágono tiver alguma população, e a comida também se a taxa for superior a zero; um 0% sorteado paga 0, e um porto cujo fator de escalão chegue a 0 não rende nada de qualquer forma. Um porto bloqueado não produz nenhum dos dois.

> ***▶ O que a melhoria realmente te dá.** Cada nível aumenta o ouro (×0.20 → ×0.40 → ×0.60, garantido) e alarga o sorteio de comida (0–5% → 0–10% → 0–15%), pelo que a colheita tem em média ~2.5% / ~5% / ~7.5% da população e pode descer para quase nada em qualquer nível. A escada é monótona: um porto de nível superior nunca é pior em média.*

**Porque se move a comida do teu porto.** O cartão Ports do teu relatório lista os teus portos um a um: o ouro de cada porto, a sua comida e a % que sorteou neste turno, um porto bloqueado marcado como bloqueado, e um porto além dos teus primeiros cinco marcado com a sua taxa reduzida. A tua Página do Jogador **não** consegue prevê-la — a página conta a comida sorteada como **zero** em todos os valores que chama garantidos, deliberadamente, para nunca te poder prometer uma colheita que o motor não concedeu. O separador Production mostra a colheita possível de cada porto como um intervalo (p. ex. 600g + 🎲 0–149f/turn para um porto Nv3 de 1,000 de população — o máximo é o melhor que o sorteio pode realmente pagar, que em muitas populações redondas fica um abaixo da percentagem), pelo que um 0 aí é o fundo do sorteio, nunca uma previsão. Um porto que o teu relatório marca como **bloqueado** — marcado apenas enquanto um bloqueio ainda o mantém no fim do turno, pelo que um bloqueador que expulsaste não deixa marca — conta como 0 na previsão de rendimento da página e no seu cartão Production, porque um bloqueio mantido morde de novo no turno seguinte. Planeia em função do ouro, e trata a comida como o tempo.

**Escalões de portos (Port brackets).** Os portos de um reino pagam em escalões de **5**, ordenados do **maior primeiro** pelo rendimento em ouro: os portos 1–5 recebem a taxa completa, os portos 6–10 recebem **90%**, 11–15 **80%**, 16–20 **70%**, e assim por diante descendo 10% por escalão (um 51.º porto seria o primeiro a não render nada). Ouro e comida são cortados por igual, e o corte recai sempre nos teus portos mais pequenos. Um porto bloqueado continua a ocupar o seu lugar. A Página do Jogador avisa-te no momento em que colocas em fila uma construção de porto que cairia num escalão reduzido (o aviso e o cartão da ordem indicam a posição e a taxa), o separador Production marca cada porto cortado com a sua taxa (⚓ 90% …), a discriminação do rendimento conta quantos portos foram reduzidos, e o cartão Ports do relatório do turno, ativo ou passivo, diz quantos dos teus portos foram pagos à taxa reduzida.

**Serração (Lumbermill)** (madeira — §3.6.5) e **Pedreira (Quarry)** (pedra — §3.6.6) também pagam a partir da população do seu hexágono neste passo.

**2.9.5 Imposto sobre a População (Population Tax)**

Taxa de imposto definida pelo jogador: 1–10 (por omissão 5). **Todas as taxas cobram na totalidade** — 10% do valor do teu povo é 10%.

rawTax = floor(totalPop × taxRate / 100)

totalPop = soma de todas as populações dos hexágonos possuídos após o crescimento deste turno — e depois de os recrutas deste turno terem sido retirados dela (Pré-Fase 2b, §2.6a): recrutar baixa a base de imposto do mesmo turno.

**Imposto num relance** — o que cada taxa cobra, quanto isso rende com 25,000 pessoas, e o que faz à opinião (opinion) em cada turno (§2.9.13). Uma opinião baixa fica então com a sua quota PENALTYTAX do que é cobrado (§2.9.6). A coluna do ouro escala com a população; a coluna da opinião é igual para qualquer reino.

|              |                             |                        |
|--------------|-----------------------------|------------------------|
| **Taxa de imposto** | **Ouro de 25,000 pessoas** | **Opinião em cada turno** |
| 1%           | 250                         | +8                     |
| 2%           | 500                         | +6                     |
| 3%           | 750                         | +4                     |
| 4%           | 1,000                       | +2                     |
| 5%           | 1,250                       | sem alteração          |
| 6%           | 1,500                       | −2                     |
| 7%           | 1,750                       | −4                     |
| 8%           | 2,000                       | −6                     |
| 9%           | 2,250                       | −8                     |
| 10%          | 2,500                       | −10                    |

Mais imposto é sempre mais ouro; o preço é a opinião.

> ***▶ Exemplo — imposto, depois a penalização de opinião.** Um reino de 26,000 pessoas mantém 7% de imposto com Opinião 35 no início do turno.*
>
> *• **Imposto:** rawTax = floor(26,000 × 7 / 100) = 1,820 de ouro.*
>
> *• **Penalização de opinião (§2.9.6):** a Opinião 35 está no escalão 31–40, 4% → penaltyAmt = floor(1,820 × 4 / 100) = 72 → netTax = 1,748 de ouro.*
>
> *• **Opinião (§2.9.13):** manter 7% move a opinião −4 → 31 no turno seguinte. Se o reino tivesse mantido 5%, teria cobrado 1,300 de ouro, pago a mesma penalização de 4% (netTax = 1,248) e mantido a Opinião 35 — 500 de ouro por turno comprados com 4 de opinião por turno, até a opinião chegar ao escalão de penalização seguinte.*

**2.9.6 Penalização de Opinião sobre o Imposto (Opinion Penalty on Tax)**

Se a Opinião for **50 ou inferior**, uma parte do rendimento bruto do imposto perde-se (os relatórios designam esta dedução **PENALTYTAX**; repara que exatamente 50 já é penalizado). A quota é lida da tua opinião no **início** do turno, antes de a taxa de imposto deste turno a mover (TP_TAX_PENALTY_BANDS):

|                   |                 |
|-------------------|-----------------|
| **Intervalo de Opinião** | **Penalização de Imposto** |
| 51–100            | 0%              |
| 41–50             | 2% do imposto bruto   |
| 31–40             | 4% do imposto bruto   |
| 21–30             | 6% do imposto bruto   |
| 11–20             | 8% do imposto bruto   |
| 0–10              | 10% do imposto bruto  |

penaltyAmt = floor(rawTax × penaltyTax / 100)

netTax = max(0, rawTax − penaltyAmt)

**2.9.7 Bónus de Rendimento das Personagens (Character Income Bonuses)**

Aplicados depois de estabelecido o rendimento base:

- **Tesoureiro (Treasurer)** (atribuição treasury): bonusGold = floor(netTax × economics × 0.2 / 100) — **apenas ouro de imposto**; o ouro dos portos é do gabinete do Mestre dos Portos, e nenhum ouro é contado por ambos (não há ouro de terreno — §2.9.2)

- **Mestre das Quintas (Master of Farms)** (atribuição farms): bonusFood = floor((farmFood + portFood) × management × 0.2 / 100) — repara que portFood contém a colheita **sorteada** de todos os níveis de porto (§2.9.4), pelo que este bónus herda essa oscilação: uma estação em que os teus portos sorteiam mal paga menos ao teu Mestre das Quintas sem culpa dele.

- **Mestre das Minas (Master of Mines)** (atribuição mines): bonusIron = floor(mineIron × management × 0.2 / 100)

- **Mestre dos Portos (Master of Ports)** (atribuição ports): bonusGold = floor(portGold × management × 0.2 / 100) — portGold é o total reduzido por escalões e por bloqueio, exatamente o valor do cartão Ports. Não disponível para reinos Orc ou Anões (sem portos).

- **Mestre das Serrações (Master of Lumbermills)** (atribuição lumbermills): bonusWood = floor(lumberWood × management × 0.2 / 100)

- **Mestre das Pedreiras (Master of Quarries)** (atribuição quarries): bonusStone = floor(quarryStone × management × 0.2 / 100)

- **Mestre dos Cavalos (Master of Horses)** (atribuição horses): acrescenta management × 0.02 **pontos percentuais** à taxa de reprodução da manada — não uma quota da produção, que numa manada a crescer 1–3% por turno valeria quase nada (§2.9.9). Disponível para todas as raças.

> ***▶ Exemplo — o Tesoureiro ao lado de um Mestre dos Portos.** Um reino cobra 1,552g de imposto e 8,583g dos seus portos. O seu Tesoureiro tem Economia 96 (+19.2%) e o seu Mestre dos Portos Gestão 94 (+18.8%). O Tesoureiro acrescenta floor(1,552 × 19.2 / 100) = **297g** — os portos não são para o Tesoureiro contar; o Mestre dos Portos acrescenta floor(8,583 × 18.8 / 100) = **1,613g**. Nenhuma moeda de ouro é contada por ambos os gabinetes, e nenhum dos bónus entra na base do pacto (§2.9.8) nem na base do tributo (§2.9.11). Para um reino que vive dos seus portos, o Mestre dos Portos é o gabinete que paga; para um que vive dos impostos, o Tesoureiro.*

Os atributos das personagens (characters) vão de 1–100 na criação, pelo que o bónus máximo base por personagem é 20%; a experiência (§7.10) pode elevar um atributo a min(150, base + 20%), ou seja, um bónus até 30%. O Mestre dos Cavalos funciona em pontos: +2 com management 100, até +3 com 150. O livro-razão **Profile** da Página do Jogador mostra, na linha de cada recurso, o Mestre que ocupa o gabinete e o que acrescenta neste turno (um gabinete atribuído neste turno paga a partir do seguinte).

> ***▶ Exemplo — ler uma linha do livro-razão Profile.** A linha de Ouro de um reino diz: 💰 Gold 28,070 · +8,988 · 51,744 people at 3% tax · 4 ports (2 Lv3 · 1 Lv2 · 1 Lv1) · −3,057 upkeep · Treasurer ✓ +297 💰 (+19.2%) · Master of Ports ✓ +1,613 💰 (+18.8%). A linha soma: imposto 1,552 + portos 8,583 + os 19.2% do imposto do Tesoureiro (297) + os 18.8% dos portos do Mestre dos Portos (1,613), menos 3,057 de manutenção, dá os **+8,988** por turno. Cada fonte e cada dreno da linha é uma linha da tabela Production Income por baixo, pelo que as duas nunca discordam; cada contagem de locais traz os seus níveis, do mais alto para o mais baixo; um Mestre atribuído neste turno diz assigned this turn — pays from next turn.*

**2.9.8 Rendimento de Pacto Comercial / de Aliança (Trade / Alliance Pact Income)**

Um **pacto mútuo** concede um bónus de ouro em cada turno — ambos os reinos em trade **ou melhor** um para o outro (trade↔trade, trade↔alliance ou alliance↔alliance; o par misto conta como pacto comercial e exige a fronteira — ver abaixo):

- Cada par mútuo concede 0–2% da base de ouro do reino — **imposto + portos**, sem os bónus do Tesoureiro nem do Mestre dos Portos

- Sorteio por parceiro: floor(rand×3) → **0, 1 ou 2%** (em alguns turnos um pacto não paga nada)

- Apenas ouro; acumula entre os teus parceiros comerciais ou aliados mútuos — **no máximo 5 pagam num turno**: com mais, 5 são sorteados ao acaso em cada turno e os restantes nada trazem (*Market saturated — your merchants cannot find a market for so many trade partners*); ambos os reinos sorteiam de forma independente

- **O comércio exige uma fronteira comum**: só podes formar um pacto comercial com um reino diretamente adjacente ao teu território, e ele só paga nos turnos em que ainda faças fronteira com ele — a fronteira é verificada de novo em cada turno: perde-a (o território muda de mãos) e o pacto fica **dormente** — não paga nada e ambos os relatórios trazem um cartão 📦 *"trade pact dormant — no shared border"* até voltarem a ser vizinhos (ou melhorarem para aliança mútua completa, que não precisa de fronteira). Um par trade↔alliance continua a pagar enquanto a oferta de melhoria estiver de pé; o relatório de quem propõe mostra 🤝 *"alliance proposed — trade pact still active"* e o cartão de oferta de aliança do outro lado nota que o pacto continua a pagar em qualquer dos casos

- **As alianças não têm requisito de fronteira** — alia-te a um reino distante para ganhar um bónus de pacto pelo mapa; é assim que obténs um pacto económico com um não vizinho

- Vassalo e suserano são aliados, pelo que também recebem este bónus — para além do tributo, a qualquer distância

- Funciona com **qualquer** reino, incluindo os controlados por IA ou ausentes (passivos) (o comércio continua a exigir a fronteira; a aliança não)

Nenhuma das posturas é espelhada automaticamente — ambos os reinos têm de a definir de forma independente (§2.16.2); um pacto verdadeiramente unilateral (o outro lado em paz ou pior) não paga nada.

> ***▶ Exemplo — sete aliados, cinco pagam.** O reino A tem alianças mútuas com sete reinos, e a sua base de ouro neste turno (imposto + portos) é 10,000g. Em cada turno, cinco dos sete são sorteados para pagar; cada um sorteia 0, 1 ou 2% — juntos 0 a 1,000g, cerca de 500g num turno médio. Os outros dois nada trazem, e o relatório de A di-lo: Market saturated — 5 of 7 trade partners paid … This turn C, F brought nothing. No turno seguinte o sorteio recomeça, pelo que outro par pode ficar de fora. Cinco aliados ou sete, o rendimento de pactos de A nunca passa 5 × 2% = **10%** da sua base de ouro.*

**2.9.9 Criação de Cavalos (Horse Breeding)**

Se um reino possuir pelo menos 2 cavalos (horses) (um par reprodutor), estes reproduzem-se em cada turno — um cavalo isolado não se pode reproduzir: gained = ceil(horses × (growthPct + masterPts) / 100) onde growthPct = 1 + floor(rand×3) = 1–3% e masterPts = management × 0.02 de um **Mestre dos Cavalos (Master of Horses)** (§2.9.7; 0 se não houver) — **arredondado PARA CIMA** (um par reprodutor ganha sempre pelo menos 1). Exemplo: 1,000 cavalos com um sorteio de 2% e um Mestre com gestão 90 reproduzem-se a 2% + 1.8 = 3.8% — 38 poldros em vez de 20. O Mestre também precisa do par reprodutor: abaixo de 2 cavalos nada se reproduz.

**A manada reproduz-se com o que sobra depois de pagar a cavalaria deste turno.** O recrutamento (Pré-Fase 2b) gasta 1 cavalo por cada recruta montado *antes* de a Fase 1 contar a manada. Exemplo com um sorteio de 2%: com 100 cavalos e 50 cavaleiros recrutados, a manada reproduz-se sobre 50, dá 1 poldro e termina com 51. Se reduzires a manada a um único cavalo, ela não se reproduz nesse turno.

**2.9.10 Reprodução dos Orcs (Orc Reproduction)**

Cada exército Orc com **10 ou mais soldados de infantaria Orc** que **esteja num hexágono de pântano** ganha tropas em cada turno:

- **Só em pântano.** A posição do exército **quando a Fase 1 é executada** — depois de os cercos, assaltos e embarques da pré-fase estarem resolvidos, antes das marchas deste turno — tem de ser terreno de pântano: qualquer pântano, seja ou não seu. Em qualquer outro terreno, ou a bordo de uma frota, a horda não se reproduz; o relatório di-lo por exército ("no swamp underfoot"), nunca em silêncio.

- Taxa de crescimento: 5 + floor(rand×3) = 5–7% da infantaria desse exército. **A contagem inclui a infantaria recrutada neste turno:** o recrutamento (Pré-Fase 2b) é executado antes da Fase 1, pelo que os goblins recém-chegados reproduzem-se no turno em que chegam, e uma horda abaixo do limiar de 10 de infantaria que recrute para além dele reproduz-se nesse mesmo turno. Exemplo com um sorteio de 6%: uma horda de 20 num pântano que recruta 30 reproduz-se sobre 50, cresce 3 e termina com 53.

- gained = ceil(footCount × growthPct / 100) — **arredondado PARA CIMA**, pelo que todo o exército elegível ganha pelo menos +1 por turno

- Distribuído proporcionalmente pelas pilhas de unidades de infantaria do exército

- As unidades montadas não se reproduzem. **Só os soldados de infantaria Orc se reproduzem e contam:** as tropas de outros povos num exército Orc (§2.12.1) e as máquinas de cerco não se reproduzem, e não fazem parte da contagem de infantaria nem do limiar de 10 soldados

- Quando a reprodução de um turno faz o total de soldados de infantaria Orc em todos os exércitos ultrapassar 300, 500 ou 1000 pela primeira vez, todos os outros reinos recebem uma mensagem de aviso. Ultrapassar um limite apenas por recrutamento ou fusão não é anunciado — só a reprodução o faz.

- **A previsão da Página do Jogador (Player Page) é uma previsão.** O cartão 🧬 apresentado no momento da submissão lê o hexágono de cada exército na página; o Processador de Turnos (Turn Processor) decide na Fase 1. Existe um desfasamento conhecido de um turno (propositado): no turno imediatamente a seguir a um reino **reconquistar a sua capital original**, a página ainda coloca um exército recém-erguido na antiga sede alternativa, enquanto o TP já usa a capital original — se exatamente uma das duas for pântano, a previsão está errada nesse único turno; o relatório está certo.

- **Turnos sem crescimento.** Com o ganho arredondado para cima, uma horda elegível *em pântano* cresce sempre. O crescimento nulo a nível do reino é rotineiro: sempre que nenhuma horda esteja num hexágono de pântano, o relatório inclui o cartão 🧬 neutro *"a horda está em terra seca"* com a lista de cada horda em terra seca. O cartão *"no new boyz this season"* mantém-se apenas como recurso defensivo para uma horda em pântano cujo sorteio arredonde para 0, o que a matemática com arredondamento para cima nunca produz.

- **Os sorteios são mostrados, exército a exército.** Ambos os cartões de reprodução (crescimento e crescimento nulo, relatórios ativos e passivos) detalham o sorteio de cada exército elegível — p. ex. Army I: +3 (5% of 41) · Army II: +1 (6% of 12) — seguido de cada horda em terra seca que não se reproduziu — p. ex. Army III: no swamp underfoot (plains) — did not breed — e o registo de turno do GM tem uma entrada 🧬 *Orc Reproduction* correspondente com o mesmo detalhe por exército.

**2.9.11 Tributo de Vassalo (Vassal Tribute)**

Os vassalos (vassals) pagam tributo ao seu suserano depois de o rendimento da Fase 1 ser calculado:

- Taxa: 1–5% (definida pelo suserano, por omissão 3%), limitada no código: max(1, min(5, rate))

- tributeBase = netTax + portGold — os bónus do Tesoureiro e do Mestre dos Portos do vassalo não são tributados, a mesma base dos pactos (§2.9.8)

- tributeAmt = floor(tributeBase × tributeRate / 100)

- O ouro é deduzido ao vassalo e acrescentado ao suserano. Se o vassalo não conseguir cobrir o montante total, só é retirado o que tiver.

- O tributo cessa a partir do turno seguinte ao fim da vassalagem — renunciada, ou quebrada por uma guerra entre os dois (§2.16.4); uma guerra iniciada antes do rendimento da Fase 1 (um cerco ou assalto em curso) faz-no cessar nesse mesmo turno.

> ***▶ Exemplo — um vassalo com bons Mestres.** Um vassalo a 5% recolhe 1,552g em imposto e 8,583g dos seus portos; o seu Tesoureiro acrescenta 297g e o seu Mestre dos Portos 1,613g. O tributo é floor((1,552 + 8,583) × 5 / 100) = **506g**. Os 1,910g dos dois Mestres ficam com o vassalo — o suserano tributa o rendimento do reino, não a competência dos seus oficiais.*

**2.9.12 Rendimento Aplicado (Income Applied)**

totalGold = netTax + portGold + treasurerBonus + masterPortsBonus + tradePactBonus

totalFood = plainsFood + farmFood + portFood + masterFarmsBonus

totalIron = mineIron + masterMinesBonus

totalWood = lumberWood + masterLumbermillsBonus

totalStone = quarryStone + masterQuarriesBonus

plainsFood é o +1 de comida por hexágono de planície sem local de produção (§2.9.2). Não existe termo de ouro do terreno: o ouro provém apenas do imposto, dos portos, dos bónus de personagens e dos pactos.

O tributo de vassalo é depois deduzido ao ouro acumulado do vassalo.

> ***▶ Exemplo — o rendimento da Fase 1 de um pequeno reino.** Uma construção de sede de recrutamento (pop 10,000) + duas construções menores (pop 5,000 cada) + três construções em planície, cada uma com uma quinta de Nível 2 (pop 2,000 cada). Taxa de imposto 5, Opinião 60, sem personagens, sem pactos comerciais.*
>
> *• **Ouro do terreno:** nenhum (§2.9.2).*
>
> *• **Imposto:** população total = 10,000 + 2×5,000 + 3×2,000 = 26,000; rawTax = floor(26,000 × 5 / 100) = 1,300 de ouro. A Opinião 60 está acima de 50, pelo que não há penalização de imposto → netTax = 1,300.*
>
> *• **Comida das quintas:** uma quinta de Nível 2 sorteia a sua taxa em cada turno em \[0.20, 0.50\] (§3.6.1), pelo que cada uma destas rende entre floor(2,000 × 0.20) = 400 e floor(2,000 × 0.50) = 1,000 de comida → **1,200 a 3,000 de comida**, e um valor diferente em cada turno. O que tens garantido é o mínimo: 1,200. Os três hexágonos de planície têm um local de produção, pelo que **não** produzem também o +1 fixo de comida do terreno.*
>
> *• **Neste turno:** 1,300 de ouro, 1,200–3,000 de comida (1,200 garantidos), 0 de ferro.*
>
> *Agora atribui um Tesoureiro com Economia 80: o ouro sobe floor(1,300 × 80 × 0.2 / 100) = floor(208) = 208 → 1,508 de ouro. Uma única personagem bem colocada vale mais do que um povoado inteiro.*

**2.9.13 Alterações da Taxa de Imposto (Tax Rate Changes)**

Uma ordem tax_change produz efeito no fim da Fase 1 (o rendimento deste turno já está calculado à taxa antiga, pelo que a **nova taxa só se aplica ao rendimento do próximo turno**).

Podes alterar a taxa em no máximo **1 ponto percentual por turno** (p. ex. 5→6 ou 5→4, nunca 5→7). Isto é imposto pelo **Processador de Turnos**, e não apenas pela Página do Jogador: um ficheiro de ordens editado à mão para pedir um salto maior é **limitado a ±1** a partir da tua taxa atual real (e registado junto do GM), pelo que não há maneira de saltar para uma taxa alta num único turno.

**Alterar a taxa não custa opinião por si só. A taxa que mantiveres move a opinião em cada turno**, segundo a taxa que cobrou o imposto desse turno:

opinionChange = (TP_TAX_OPINION_NEUTRAL − taxRate) × TP_TAX_OPINION_PER_POINT — +2 por ponto abaixo de 5%, −2 por ponto acima (todas as taxas na tabela *Tax at a glance*, §2.9.5).

Não se lançam dados. A alteração ocorre na Fase 1, logo a seguir ao imposto, e a opinião mantém-se entre 0–100. Como uma tax_change se aplica depois do rendimento, **o turno em que ordenas uma nova taxa ainda move a opinião à taxa antiga**; o valor da nova taxa começa no turno seguinte, juntamente com o seu ouro. Aplica-se a todos os reinos, incluindo um que não tenha enviado ordens. A opinião **não recupera por si própria**: além de uma taxa abaixo de 5%, só sobe através de eventos — qualquer batalha ganha, um reino que te declare guerra, a conclusão de uma paz ou de um cessar-fogo (§8.5.3). O teu cartão de rendimento indica a alteração que realmente ocorreu (· opinion −6 (tax 8%) — menos, ou nada, quando a opinião já está em 0 ou 100), e a Página do Jogador mostra o valor em Opinião Pública (Public Opinion) e junto de uma alteração de imposto em fila.

**2.10 Fase 2 — Manutenção e Fome (Phase 2 — Upkeep & Starvation)**

**2.10.1 Manutenção em Ouro (Gold Upkeep)**

Manutenção total em ouro = soma de upkeep.gold × count em todos os exércitos (todas as pilhas de unidades) mais todas as frotas (todas as pilhas de navios). Deduzida às reservas de ouro. Os recrutas erguidos neste turno (Pré-Fase 2b, §2.6a) já estão nas listas e são faturados aqui; a Página do Jogador reservou essa fatura do primeiro turno quando os puseste em fila.

**2.10.2 Consequências do Défice de Ouro (Gold Deficit Consequences)**

Se a manutenção em ouro exceder o ouro disponível:

- Deserção: 5 + floor(rand×11) = 5–15% de todas as tropas em todos os exércitos não destruídos — arredondada **para baixo** por pilha de unidades sem mínimo, pelo que nunca leva o último soldado de um exército (uma pilha com menos de 7 não perde ninguém, mesmo a 15%)

- Aplicada a todas as pilhas de unidades proporcionalmente

- Penalização de opinião: −(5 + floor(rand×8)) = −5 a −12

**2.10.3 Manutenção em Ferro (Iron Upkeep)**

A manutenção em ferro é deduzida às reservas de ferro. A falta de ferro não tem consequências para as tropas nem para a opinião — as reservas ficam a 0 e param.

**2.10.4 Consumo de Comida (Food Consumption)**

A comida é consumida em cada turno de acordo com o número de efetivos dos exércitos — **1 de comida por soldado de infantaria, 2 por montado** — igual para todas as raças exceto os **Nómadas**, cujas unidades montadas comem apenas 1 (§4.8).

foodConsumed = footCount + mountedCount × 2 (as contagens incluem os recrutas deste turno — §2.6a)

Os exércitos embarcados consomem comida normalmente.

**2.10.5 Fome (Starvation)**

Se foodConsumed \> foodAvailable:

- **Orc**: 10 + floor(rand×11) = 10–20% de perda de tropas

- **Todas as outras raças**: 3 + floor(rand×8) = 3–10% de perda de tropas

- Aplicada proporcionalmente a todos os exércitos não destruídos

> ***▶ Exemplo — quando é que os meus soldados passam fome?** O consumo de comida é footCount + 2×mountedCount. Um exército de 200 de infantaria + 50 montados come 200 + 2×50 = 300 de comida neste turno. Se as tuas reservas tiverem apenas 250, todos os exércitos do reino passam fome: uma força não Orc perde 3–10% das suas tropas, uma força Orc perde 10–20%. Repara na ordem das operações — **a manutenção (Fase 2) é executada antes do movimento (Fase 5)**, por isso armazena comida suficiente antes do turno em que planeias uma grande marcha — ou um grande recrutamento: os homens que ergueres neste turno comem neste turno — e não depois.*

**2.11 Fase 3 — Mercados e Construção (Phase 3 — Markets & Construction)**

**Ordem dentro da fase:** as **ordens de mercado (market orders) de cada reino são executadas primeiro**, depois as suas ordens de construção — uma venda ou compra posta em fila neste turno fica disponível para as construções, fundações, melhoramentos e mudanças de acampamento deste turno. Os preços são os preços fixos do turno para todos; a passagem de pressão de compra/venda que move os preços do próximo turno é executada depois de todos os reinos terem negociado. (Os recrutas e as máquinas resolvem-se antes, na Pré-Fase 2b, e nunca veem o mercado deste turno — §2.6a.)

**2.11.1 Construção de Locais de Produção (Site Construction)**

Os jogadores submetem ordens de construção para hexágonos específicos. Elegibilidade de terreno:

|            |                                             |                                                                                                                |          |                                         |
|------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------|
| **Local de produção (Site)**   | **Terreno Exigido**                        | **Requisito Adicional**                                                                                     | **Custo** | **Probabilidade**                              |
| Quinta (Farm)       | Planície                                      | Sem local de produção existente; **o hexágono tem de ter uma construção**                                                             | 1000g    | 100%                                    |
| Mina (Mine)        | Montanha / Colinas / Deserto / Planície / Floresta | Sem local de produção existente; **o hexágono tem de ter uma construção**                                                             | 1000g    | **25% / 15% / 7% / 7% / 5%** conforme o terreno |
| Porto (Port)       | Planície *— ou Floresta, apenas reinos Elfos*\*†  | Sem local de produção existente; hexágono adjacente a pelo menos um hexágono de mar; **não Orc nem Anão**; **o hexágono tem de ter uma construção** | 5000g    | 100%                                    |
| Serração (Lumbermill) | Floresta                                      | Sem local de produção existente; **o hexágono tem de ter uma construção**                                                             | 1000g    | 100%                                    |
| Pedreira (Quarry)     | Planície, Colinas ou Montanha                  | Sem local de produção existente; **o hexágono tem de ter uma construção**                                                             | 1000g    | 100%                                    |

A construção de uma mina é uma **prospeção**. O ouro é gasto na tentativa, qualquer que seja o resultado — sem reembolso em caso de falha. A profundidade da mina é limitada pelo terreno — montanha Lv3, colinas/deserto Lv2, planície/floresta Lv1 — e o poço de Lv3 é **exclusivo dos Anões** (a conquista degrada um local de produção capturado em um nível — §5.6.3 — pelo que um Lv3 Anão capturado chega como Lv2, e só um dono Anão o pode voltar a escavar); os hexágonos de pântano e de mar não podem ser prospetados de todo.

\\ A planície é o único terreno de porto aberto a **todas** as raças num mapa construído hoje (a exceção Élfica abaixo é o único acrescento). O motor aceita também os dois terrenos **legados** cidade e capital, que o Editor de Mapas já não pinta e que nenhum mapa atual contém — existem para que um jogo guardado antigo ainda carregue. Se jogas num mapa feito depois de esses terrenos terem sido retirados, lê isto como "planície".\*

† \***A exceção Élfica.** Um reino **Elfo** — e nenhum outro — pode também erguer um porto num hexágono de **floresta** costeira. Os Elfos instalam-se na floresta e, como todo o local de produção precisa de uma construção por baixo (abaixo), um reino Élfico pode ter uma costa inteira e, ainda assim, não possuir nenhum hexágono onde um porto possa legalmente ser erguido. A exceção é uma lista branca de terrenos, não uma licença: um Elfo é recusado em costas de colinas, montanha, pântano e deserto exatamente como todos os outros, e a proibição dos Orcs/Anões prevalece sobre ela (uma hipotética costa florestal Orc continua fechada). Duas consequências a ter em conta no planeamento: o hexágono **continua a ser floresta**, pelo que um porto Élfico é defendido em terra com o pleno bónus florestal Élfico (§5.2 — ×1.30) que nenhum outro reino tem nos seus portos; e, depois de construído, o porto sobe a Lv2 e Lv3 nos termos normais, já que só a construção inicial olha ao terreno. **Apenas sob uma construção Élfica:** o hexágono de floresta tem de ter uma construção da família **Elfo** (§3.7) — os construtores navais Elfos só constroem onde os Elfos construíram. Uma floresta sob uma construção Genérica ou de qualquer outra família nunca aceita um porto Élfico; a ordem é recusada com o motivo e os 5000g são reembolsados. Um porto já existente num hexágono desses não é afetado, e os portos em planície também não.\*

**Um local de produção só pode ser construído onde exista uma construção.** A produção do local depende da população (§3.8) e a população vive apenas dentro de construções, pelo que uma quinta, mina, porto, serração ou pedreira num **hexágono vazio não produziria nada, para sempre** — e nunca o poderias corrigir, porque só o GM coloca construções. Em vez de te deixar comprar isso, o jogo recusa: **os hexágonos vazios não são oferecidos no painel de construção e o Processador de Turnos rejeita a ordem**, reembolsando o custo. O mesmo se aplica ao **melhoramento**: um local de produção que, de algum modo, esteja em terreno vazio (colocado pelo GM, ou tomado por conquista) fica fixado no seu nível e mostra "✓ Fully upgraded" — não há nada a ganhar em aprofundá-lo.

A tabela de terrenos acima continua a determinar *que* terreno cada local de produção exige. A construção determina *se* o hexágono é sequer edificável.

O Processador de Turnos aceita **uma ordem de construção por hexágono por turno**, e os seis tipos de ordem de construção partilham essa única vaga: construir local de produção, melhorar local de produção, arrasar local de produção (§2.11.6), melhorar construção (§2.11.7), reparar muralha (§2.11.8) e fundar uma nova construção (§2.11.9). Se emitires duas para o mesmo hexágono no mesmo turno, a primeira é mantida e a segunda recusada como duplicada. Uma ordem em fila aparece no mapa do reino como um sinal de trabalhador (§2.1).

**Calendário — o rendimento começa no turno SEGUINTE.** A construção resolve-se na Fase 3, mas o rendimento (Fase 1) é calculado mais cedo no mesmo turno. Assim, um local de produção que construas (ou melhores) neste turno **não produz nada neste turno** — a sua comida / ferro / ouro começa no turno **seguinte**. Uma quinta construída no turno N produz comida pela primeira vez no turno N+1 (o seu rendimento é sorteado em cada turno — §3.6.1). As quintas, portos, serrações e pedreiras ficam concluídos no turno em que os ordenas (100%); uma mina pode demorar vários turnos só para aparecer (5–25%/turno conforme o terreno), e só depois começa a produzir, no turno a seguir ao seu aparecimento. É o mesmo desfasamento de um turno de uma alteração de imposto (§2.9.13) — tudo o que começares neste turno compensa a partir do próximo, porque o rendimento é a primeira fase.

**2.11.2 Melhoramentos de Locais de Produção (Site Upgrades)**

|            |                  |          |                                                                                                             |
|------------|------------------|----------|-------------------------------------------------------------------------------------------------------------|
| **Local de produção (Site)**   | **Nível Alvo** | **Custo** | **Probabilidade**                                                                                                  |
| Quinta (Farm)       | Lv1 → Lv2        | 2000g    | 100%                                                                                                        |
| Quinta       | Lv2 → Lv3        | 3000g    | 100%                                                                                                        |
| Mina (Mine)       | Lv1 → Lv2        | 2000g    | 30% — apenas montanha, colinas ou deserto (uma mina em planície ou floresta fica em Lv1; a ordem é recusada e reembolsada) |
| Mina       | Lv2 → Lv3        | 3000g    | 50% — apenas reinos Anões, apenas montanha                                                                  |
| Porto (Port)       | Lv1 → Lv2        | 10000g   | 100%                                                                                                        |
| Porto       | Lv2 → Lv3        | 15000g   | 100%                                                                                                        |
| Serração (Lumbermill) | Lv1 → Lv2        | 2000g    | 100%                                                                                                        |
| Serração | Lv2 → Lv3        | 3000g    | 100%                                                                                                        |
| Pedreira (Quarry)     | Lv1 → Lv2        | 2000g    | 100%                                                                                                        |
| Pedreira     | Lv2 → Lv3        | 3000g    | 100%                                                                                                        |

Em caso de falha, o ouro é gasto e o nível não aumenta. Nível máximo: 3. **Os reinos Orcs e Anões nunca podem melhorar um porto** (§3.6) — um porto que tomem por conquista continua a produzir, mas fica congelado no nível em que o capturaram. E **nenhum local de produção pode ser melhorado num hexágono sem construção** (§2.11.1): um povoado é aquilo a que um local de produção pertence, pelo que um que esteja em terreno vazio fica congelado onde está.

**2.11.3 Regras de Reembolso (Refund Rules)**

Toda a ordem que o Processador de Turnos **recusa na validação** é reembolsada — hexágono capturado por um inimigo neste mesmo turno, terreno errado, sem construção, restrição de raça, vaga duplicada, e semelhantes. Só os **falhanços de dados** não são reembolsados: uma prospeção de mina falhada e uma falha no aprofundamento de uma mina gastam o ouro (a mina é a única construção que sorteia — §3.6.2).

**2.11.4 O Mercado (The Market)**

Cinco mercadorias: **Comida (Food)**, **Ferro (Iron)**, **Cavalos (Horses)**, **Madeira (Wood)**, **Pedra (Stone)**.

Preços de base: Food 8g, Iron 12g, Horses 20g, Wood 5g, Stone 7g.

- **Preço de compra**: preço de mercado atual por unidade

- **Preço de venda**: max(1, round(currentPrice × 0.6)) — 60% do preço de compra, arredondado ao ouro mais próximo (nunca abaixo de 1g)

- **Mercadorias transacionáveis: comida, ferro, cavalos, madeira, pedra.** O ouro é a moeda, não uma mercadoria — nunca pode ser comprado nem vendido no mercado (o servidor descarta qualquer ordem dessas), embora **possa** ser *enviado* a outro reino através do painel 📦 Send Resources (§2.8).

O Processador de Turnos revalida no servidor todas as ordens de mercado: uma compra é **limitada** ao que o teu ouro cobre e uma venda ao que o teu armazém contém (preenchimento parcial, indicado como "of N requested"). Só é descartada uma ordem que não preencheria nenhuma unidade. **A Página do Jogador aplica o mesmo limite a uma compra enquanto a pões em fila**: se pedires mais do que o teu dinheiro disponível cobre, ela põe em fila o que podes pagar e diz-te ambos os valores — não recusa a ordem inteira. Como a página conta apenas o dinheiro (nunca o rendimento deste turno), o motor pode preencher ligeiramente *mais* do que a página pôs em fila, nunca menos.

A Página do Jogador valida as ordens de **venda** contra o **dinheiro disponível** (§2.12.1) — apenas o armazém que já tens; a produção que chega neste turno não é vendável na página, mesmo que o Processador de Turnos verifique o armazém na Fase 3, depois de o rendimento e a manutenção terem sido aplicados. As ordens de **compra** continuam a exigir o ouro em mão.

Uma ordem por mercadoria por reino por turno (as duplicadas são eliminadas, ficando a última submetida). Cada ordem está limitada a **999 unidades** — o campo da Página do Jogador pára aí e o Processador de Turnos limita qualquer valor maior a 999.

**Cancelar uma ordem em fila** inverte-a exatamente — mas só enquanto o seu produto ainda estiver livre. Uma **compra** não pode ser cancelada depois de os bens comprados estarem já comprometidos com outras ordens pendentes (p. ex. a construção de um navio posta depois da compra — os recrutas nunca podem depender de uma compra em fila, pois são validados sem ela); uma **venda** não pode ser cancelada depois de o seu ouro estar comprometido. Cancela primeiro as ordens dependentes.

**2.11.5 Dinâmica de Preços do Mercado (Market Price Dynamics)**

Depois de todas as transações serem executadas, os preços são atualizados para o próximo turno. O que move um preço é o **volume transacionado**, não o número de reinos que transacionaram: comprar 1 unidade pesa um milésimo de comprar 999.

- **Volume líquido** — cada unidade **comprada** menos cada unidade **vendida** dessa mercadoria neste turno, por todos os reinos em conjunto, contando o que foi realmente transacionado (uma ordem que a tua tesouraria ou o teu armazém não conseguiu preencher conta apenas pelo que preencheu). Compradores e vendedores anulam-se mutuamente.

- **Profundidade** — **metade de tudo o que o mercado poderia transacionar num turno**: reinos ativos × 999 unidades × 50%. Com 40 reinos ativos a profundidade é de cerca de 20,000 unidades; com 5 é de cerca de 2,500.

- **A variação** — o preço muda em proporção ao volume líquido face à profundidade, até **±15% por turno**: um volume líquido de metade da profundidade move-o 7.5%; a profundidade inteira ou mais move-o os 15% completos, nunca mais.

- **Mercado calmo** — quando o volume líquido é inferior a **5% da profundidade**, o preço em vez disso deriva **1g por turno de volta para o seu preço de base** — mas nunca contra a transação: um preço acima da base que ainda está a ser comprado, ou abaixo da base que ainda está a ser vendido, mantém-se onde está.

|                                                     |                                                                   |
|-----------------------------------------------------|-------------------------------------------------------------------|
| **Volume líquido (40 reinos ativos, profundidade ≈ 20,000)** | **Variação**                                                          |
| +1,000 (um reino compra 999 dele)                 | +0.75% (a partir de 41 reinos isto é um mercado calmo: o preço mantém-se) |
| +10,000                                             | +7.5%                                                             |
| +20,000 ou mais                                     | +15%                                                              |
| −20,000 ou mais (uma enxurrada de vendedores)                | −15%                                                              |

**As transações usam ouro inteiro; o preço por trás delas não.** O mercado guarda cada preço com decimais, pelo que as pequenas variações se acumulam de turno para turno; cada compra, venda, relatório e cartão usa esse preço **arredondado ao ouro mais próximo**, com mínimo de **1g**. Não há limite superior.

A profundidade conta **apenas os reinos ativos (que submetem ordens)** — os reinos passivos/IA não transacionam, pelo que não a diluem. Num jogo pequeno a profundidade é pequena: um reino a transacionar os seus 999 completos move o preço de forma notória; num jogo grande, só muitos reinos a transacionar da mesma maneira o fazem.

**2.11.6 Demolir um local de produção (Razing a Site)**

Podes ordenar a demolição de qualquer local de produção (site) do teu reino (separador Produção → cartão do local → **🏚 Raze**, confirmado com um segundo clique). A demolição é **gratuita, instantânea e definitiva**: o local — seja qual for o seu nível — desaparece quando o turno é processado, e nada é aproveitado. O hexágono só pode receber um novo local a partir do turno seguinte, nunca no mesmo turno (uma ordem de construção por hexágono por turno, e a demolição conta).

Duas exceções:

- **As Forjas não podem ser demolidas** — o seu ofício está para além de qualquer equipa de demolição.

- **Um porto com uma frota no porto de abrigo** — tua ou de qualquer outro — recusa a demolição até o porto estar livre. (Um porto com uma demolição pendente também não pode criar uma nova frota nem iniciar construção naval neste turno.)

Demolir antes de um invasor chegar é uma defesa legítima de terra queimada: a demolição resolve-se na Fase 3, antes de os exércitos avançarem na Fase 5, pelo que um porto ou uma pedreira condenados podem ser negados ao seu futuro conquistador. Ainda assim, o local perde-se para ti da mesma forma.

**2.11.7 Melhorar uma construção (Upgrading a Construction)**

Subir uma construção um degrau na sua escada de família (§3.7.1) ordena-se a partir do **separador 🏰 Constructions** — a lista de povoações por baixo do painel de fundação (§2.11.9). **Não há lançamento de dados** — todas as condições são verificadas primeiro, e nada é gasto a menos que todas passem.

A ordem é recusada, sem custo, se se verificar qualquer uma destas situações — verificadas por esta ordem, pelo que o motivo que te é mostrado é o primeiro que falhou:

|        |                          |                                                                         |
|--------|--------------------------|-------------------------------------------------------------------------|
| **\#** | **Recusa**               | **Significado**                                                         |
| 1      | Duplicada                | Outra ordem de construção já reclamou este hexágono neste turno (§2.11.1) |
| 2      | Não é teu                | O hexágono foi-te tomado neste mesmo turno — o ouro é reembolsado       |
| 3      | Sem construção           | Não há nada no hexágono para melhorar                                   |
| 4      | **Família estrangeira**  | A construção não é nem da tua raça nem Genérica (Generic)               |
| 5      | Cercado                  | O cerco corta os materiais exteriores                                   |
| 6      | No nível máximo          | Já está no topo da escada da sua família                                |
| 7      | População abaixo do limite | A população ainda não atingiu o limite do nível **atual**             |
| 8      | Ouro insuficiente        | A tesouraria não chega para o custo do nível seguinte                   |
| 9      | Material insuficiente    | Não há pedra/madeira suficiente para o incremento da muralha            |

**Nunca podes melhorar uma construção estrangeira capturada.** Uma fortaleza Anã que tomes de assalto continua a funcionar para ti — aloja população, cunha milícia, guarnece as suas muralhas, e podes repará-la (§2.11.8) — mas nunca crescerá mais um nível sob o teu estandarte. Isto é incondicional e **não** consulta a matriz de compatibilidade racial; essa matriz rege apenas o recrutamento (§2.12). A única exceção é **Genérica (Generic) (POP)**, que qualquer dono pode melhorar.

**Quanto custa.** Ouro igual ao custo listado do nível **seguinte**, mais material igual **apenas ao incremento da muralha** — a diferença entre a muralha do nível seguinte e a do atual, não a muralha nova inteira. O material é o **tecido da própria construção**, não o do teu reino: madeira para as famílias Aesir, Nómada e Orc, pedra para todos os outros. Assim, um reino Imperial que repare ou amplie uma povoação Orc capturada gasta **madeira**, e tem de ter madeira em armazém para o fazer.

**Mestres construtores Anões.** As construções da família Anã pagam ceil(points / 2) — uma pedra compra dois pontos de muralha. Esta é apenas uma vantagem de *custo*; a muralha em si não é mais resistente do que o seu valor listado.

**O que obténs.** Nível +1. A muralha sobe o incremento e depois é limitada ao novo máximo, pelo que uma muralha danificada é parcialmente curada ao ampliar — a reparação cobre o que o incremento não cobrir. **A população mantém-se exatamente como estava** e simplesmente retoma o crescimento rumo ao novo limite, mais alto, no turno seguinte (§3.8).

> ***▶ Exemplo.** Uma FI10 Imperial com população 1,000 (o seu limite) e uma muralha de 500 pontos, a melhorar para FI11: custa **4,000 de ouro** (o preço da FI11) e **500 de pedra** (o incremento de muralha de 1,000 → 500). A muralha termina em 1,000/1,000, a população mantém-se em 1,000, e no turno seguinte começa a crescer rumo ao limite da FI11, de 2,000.*

**2.11.8 Reparar uma muralha (Repairing a Wall)**

A integridade da muralha **não** se regenera sozinha. Reconstruí-la exige uma ordem explícita repair_wall — um hexágono, sem parâmetros, a reparar tanto quanto o limite e as tuas reservas permitirem.

Recusas, de novo por ordem de verificação: duplicada; não é teu; sem construção; **sem muralha** (um nível de família sem muralha — Orc Lv.1–3, Generic Lv.1–4, §3.7.2); **cercado**; **muralha intacta** (nada para reparar); material insuficiente.

**Quanto.** No máximo **10% do máximo da muralha** por turno — floor(wallMax × 0.10) — e nunca mais do que o dano realmente existente. Esse valor é depois limitado de novo pelo que consegues pagar: **uma unidade de material por ponto** reparado, ou ceil(points / 2) para construções da família Anã. **Uma reparação parcial continua a ter sucesso** — se só podes pagar metade, reparas metade e gastas o que tinhas.

Duas regras que decidem cercos:

- **Só um cerco ativo bloqueia a reparação.** Um exército hostil meramente *acampado* no teu hexágono — às portas sem postura de Cerco (Siege) — não impede os teus pedreiros. Trata-se de uma troca deliberada: um atacante que acampa mantém as opções em aberto mas deixa-te reconstruir; um atacante que se compromete com a postura de Cerco impede as reparações mas fica comprometido.

- **Quem repara é o dono atual, seja quem for que a construiu.** Ao contrário da melhoria, aqui não há barreira de família estrangeira. Toma uma fortaleza Anã e podes reparar as suas muralhas — pagando na pedra da família Anã, à taxa favorável da família Anã.

> ***▶ Exemplo.** Uma FI11 Imperial (máximo de muralha 1,000) reduzida a 800 tem 200 pontos em falta, mas o limite do turno é floor(1,000 × 0.10) = 100. Com 2,000 de pedra na tesouraria, repara exatamente **100 pontos** por **100 de pedra**, terminando em 900/1,000. Com apenas 50 de pedra disponíveis, repararia **50** e terminaria em 850 — continua a ser um sucesso, apenas menor.*

**2.11.9 Fundar uma construção (Founding a Construction)**

Um reino não está limitado às povoações que o GM colocou no início da campanha. Qualquer reino pode fundar uma povoação nova em terreno livre que detenha: um grupo de colonos parte da tua sede de recrutamento (muster seat), e onde parar ergue-se uma construção da tua própria família.

**Onde vive a ordem.** O **separador 🏰 Constructions** — um separador próprio na navegação à esquerda da Página do Jogador. O painel de fundação fica no topo ("🏗 Found a New Settlement"), e por baixo dele está a lista de todas as construções que já possuis, com os respetivos botões de melhoria e reparação de muralha. Cada cartão de povoação, e cada nível de fundação, ostenta a imagem do povo a cuja família pertence — uma fortaleza Anã capturada mantém a fortaleza de montanha — a mesma que a camada **Constructions+** do mapa desenha: uma yurt para os Nómadas, uma casa comprida para os Aesir, um palácio élfico para os Elfos, uma fortaleza de montanha para os Anões, um acampamento de guerra para os Orcs, um templo de colunas para os Imperiais, uma cidadela para os Bárbaros, e uma aldeia para uma povoação comum (POP). **O separador Produção cobre apenas locais de produção** (quintas, minas, portos, serrações, pedreiras, forjas — §2.11.1–§2.11.6).

**Sem lançamento de dados, e uma recusa é gratuita.** Tal como na melhoria, a fundação é decidida inteiramente pelas barreiras abaixo. São verificadas **por ordem, antes de se gastar uma única moeda**, pelo que uma ordem que falha não te custa absolutamente nada — nem ouro, nem material, nem colonos. O painel reflete as mesmas barreiras e não te oferecerá um hexágono que o motor vá recusar.

**A fundação exige um mapa de era.** Esta ordem não existe até que pelo menos uma construção já se encontre em algum lugar do mapa. Um mapa antigo (legacy) sem nenhuma ainda não tem economia de população a que a fundação se possa ligar — ativá-la com uma única ordem poria a zero a população dos hexágonos livres de todos os OUTROS reinos no mesmo turno, pelo que o jogo recusa de todo até o GM ter colocado a primeira construção do mapa.

**As recusas, na ordem exata em que o jogo as verifica.** Se mais do que uma se aplicar, és informado da primeira — resolve-a, e a seguinte pode ainda estar à espera.

|        |                       |                                                                                                                    |                                                                                                                                                                                                                                                        |
|--------|-----------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\#** | **Recusa**            | **O que significa**                                                                                                | **O que fazer a respeito**                                                                                                                                                                                                                             |
| 1      | Sem carta de fundação | O mapa não tem qualquer construção, pelo que a fundação não existe nesta campanha                                  | Nada a fazer — só o GM pode colocar a primeira povoação do mapa                                                                                                                                                                                        |
| 2      | Já fundou             | A tua corte já fundou uma povoação neste turno — **uma por reino por turno**, quantos hexágonos quer que qualifiquem | Cancela a fundação em fila se preferires o outro hexágono, ou espera um turno                                                                                                                                                                          |
| 3      | Não é teu             | O hexágono não está no mapa, ou não o detinhas quando o turno foi processado                                       | A posse é lida no momento do processamento, não do planeamento — escolhe um hexágono que tenhas confiança de continuar a deter                                                                                                                         |
| 4      | Mar alto              | Os colonos não podem ser plantados num hexágono de mar                                                             | Escolhe terra                                                                                                                                                                                                                                          |
| 5      | Ocupado               | Já existe uma construção ali                                                                                       | Melhora-a (§2.11.7) em vez de fundar. Nota que um *local de produção* num hexágono livre **não** impede a fundação — podes povoar um hexágono que já tenha uma quinta ou mina inativa, e ela começa a render no turno a seguir à chegada dos colonos (§2.11.1) |
| 6      | Cercado               | Há um cerco nesse terreno                                                                                          | Quebra primeiro o cerco (§5.8), depois envia os colonos                                                                                                                                                                                                |
| 7      | Exército hostil       | Um exército estrangeiro não amigável está no hexágono alvo (ver abaixo)                                            | Expulsa-o, ou povoa outro sítio neste turno                                                                                                                                                                                                            |
| 8      | Família estrangeira   | Tentaste fundar numa tradição que não é nem a da tua raça nem a Genérica comum                                     | Escolhe a tua própria família ou Genérica (Generic) no seletor de família do painel                                                                                                                                                                    |
| 9      | Sem sede              | Não detêns nenhuma sede de recrutamento de onde enviar colonos — incluindo o caso em que a tua sede foi **capturada neste turno** | Retoma uma sede, ou espera: a tua sede muda sozinha de local no turno seguinte à sua queda (§2.13.10)                                                                                                                                  |
| 10     | **A tua própria sede** | O hexágono que escolheste **é** a tua sede de recrutamento                                                        | Escolhe outro hexágono — os colonos são enviados *para fora* da sede, nunca de volta para ela (ver abaixo)                                                                                                                                             |
| 11     | Colonos insuficientes | A população da tua sede está abaixo do limiar necessário para enviar um grupo e ainda assim manter-se de pé        | Vê "o limiar de colonos" e "a armadilha" abaixo — esta tem uma versão desagradável                                                                                                                                                                     |
| 12     | Ouro insuficiente     | A tesouraria não chega para a planta (blueprint) de 500 de ouro                                                    | Arranja primeiro o ouro; a tesouraria é lida no momento do processamento, depois do rendimento deste turno                                                                                                                                             |
| 13     | Material insuficiente | Não há pedra ou madeira suficiente em armazém para a muralha da nova povoação                                      | Compra-o no mercado (§2.11.4), ou funda um nível sem muralha                                                                                                                                                                                           |

Pode ainda surgir mais um cartão que não é uma barreira: **duplicada**. Todos os seis tipos de ordem de construção partilham **uma ranhura por hexágono por turno** (§2.11.1), pelo que, se o hexágono alvo já tiver em fila uma ordem de construção, melhoria, demolição ou reparação, a fundação é descartada como duplicada — a primeira ordem a entrar prevalece.

**Quanto custa.** Toda a fundação paga a mesma **planta de 500 de ouro**, seja qual for a família e seja qual for o nível, mais **100 colonos** enviados da tua sede de recrutamento, mais o **máximo total de muralha** do nível de fundação no material de construção da família — não um incremento, a muralha inteira, porque não há muralha existente a partir da qual incrementar. A fundação da família Anã paga a habitual taxa de mestres construtores de ceil(points / 2) de pedra (§2.11.7). **Um nível sem muralha não custa qualquer material**: são o Orc Nível 0 (abaixo), o Nómada Lv.1 (o acampamento de colonos) e o Genérico Lv.1, que ficam com muralha 0 (§3.7.1a).

**O limiar de colonos — com o que fica a tua sede.** O grupo que parte é sempre exatamente de **100 pessoas**, e é exatamente isso que a tua sede perde: uma sede de 1,000 fica com 900. O recrutamento (Pré-Fase 2b) retira da sede *antes* de a fundação ser testada na Fase 3, pelo que, com um grupo de colonos em fila, a Página do Jogador recusa qualquer recruta na sede que deixasse menos do que o limiar (a mensagem indica a contagem que restaria); coloca a fundação em fila depois dos recrutas e o mesmo teste corre de imediato. O que o limiar controla é se o grupo pode sequer partir — a tua sede tem de ter **300** no momento do processamento. Abaixo disso a ordem é recusada (barreira 11) e ninguém se move. Assim, uma sede com população 300 pode fundar por pouco, e termina o turno com 200; uma sede com população 299 não pode fundar de todo. O painel de fundação imprime o valor resultante para a tua sede real antes de te comprometeres, e **no instante em que colocas a ordem em fila a página retira os 100 da população da tua sede** — o total 👥 e o valor da própria sede descem ambos de imediato, exatamente como já acontece com um recruta retirado desse hexágono, e cancelar a ordem repõe-nos.

**Não podes fundar na tua própria sede de recrutamento.** A barreira 10 recusa-o de forma categórica. A tua sede já é um lugar povoado com um papel próprio — é o hexágono de onde os colonos marcham *para fora*, e enviá-los para fora só para os plantar de volta no mesmo chão não é um movimento que o jogo reconheça. O painel de fundação também não lista a sede como alvo, pelo que num turno normal nunca verás esta recusa; ela existe porque o motor, e não a página, é a autoridade.

**A fundação nunca destrói população.** A nova povoação abre com **o maior valor entre os 100 colonos e o que o hexágono já tinha**. Num mapa de era limpo, um hexágono livre não tem ninguém, pelo que a resposta é simplesmente 100. Num mapa mais antigo ou migrado, um hexágono livre já pode ter gente — fundar ali reúne-a na nova povoação e não acrescenta nada, em vez de a substituir. Uma ordem de fundação nunca pode baixar a população de um hexágono, em lugar algum do mapa.

**Uma povoação fundada neste turno não participa nos combates desse turno.** Durante o resto do turno conta como **sem fortificação**, exatamente como o hexágono livre que era há uma hora:

- não confere **qualquer bónus de fortaleza** a um defensor e não impõe **qualquer penalização ao atacante**;

- não tem **zonas de muralha interior/exterior** — o hexágono combate sob a regra plana habitual de empilhamento;

- **não pode ser cercada nem assaltada**, e não há postura de guarnição a tomar nela;

- **as máquinas de cerco não lhe causam dano**, porque ainda não há nada para bater.

A muralha é, ainda assim, real desde o momento em que é construída: fica guardada com integridade total, pode ser reparada e melhorada a partir do turno seguinte, e um espião que olhe para o hexágono vê-a. A razão da regra é a justiça de calendário. A fundação resolve-se na Fase 3; as marchas chegam na Fase 5 e os desembarques marítimos na Fase 6. Sem isto, 500 de ouro gastos *depois* de um inimigo já ter escrito as suas ordens transformariam uma marcha sobre terreno aberto num assalto contra muralhas que não existiam quando qualquer dos lados planeou o turno. **Um combate já em movimento trava-se no terreno contra o qual ambos os lados planearam.** Nota a assimetria prática: para Orc (Nível 0), Nómada (FNO1) e Genérico (Lv.1), cujo nível de fundação não tem qualquer muralha, esta regra não muda nada — nunca houve muralha para desligar.

**⚠ A armadilha: uma sede pequena nunca pode fundar, por muito que esperes.** O crescimento da população **satura no limite do nível que pagaste** (§3.8) e pára aí. Daqui resulta que, se o nível atual da tua sede de recrutamento tiver menos de 300 pessoas, essa sede **nunca** atingirá o limiar de colonos por crescimento — ficará no seu limite para sempre, recusa após recusa. Seis das oito famílias começam com um limite de Lv.1 de **100**, pelo que uma sede novinha ou recém-degradada está muitas vezes exatamente nesta posição.

Só há uma saída: **melhorar a sede** até o seu limite ser 300 ou mais, e depois deixá-la crescer (§2.11.7). Nada mais funciona — em particular, **a tua taxa de imposto não tem qualquer efeito no crescimento da população**, nem o rendimento, a comida ou qualquer coisa que possas gastar. O painel de fundação di-lo no local: quando o nível da própria sede limita abaixo do limiar, nomeia o limite e diz-te para melhorar a sede.

**A família é permanente.** A raça com que fundas — a tua, ou Genérica — é a família dessa povoação enquanto ela existir. Não há nenhuma ordem para a mudar depois; só a conquista (§5.6.3) e o bloqueio de melhoria de família estrangeira (§2.11.7) voltam a tocar-lhe.

**Uma por turno, partilhando também a ranhura por hexágono.** Um reino pode fundar no máximo uma nova povoação por turno (barreira 2), por muitos hexágonos elegíveis que detenha. O hexágono alvo continua a competir pela mesma ranhura única de ordem de construção que todos os outros tipos de ordem de construção usam (§2.11.1).

**Um exército estrangeiro não amigável no hexágono bloqueia a fundação de todo.** A barreira 7 recusa a ordem antes de se gastar o que quer que seja: dispara perante qualquer exército no hexágono alvo que não seja teu, nem de um aliado mútuo, nem do teu suserano, nem de um dos teus vassalos. Esses quatro nunca a acionam — a povoação ergue-se à volta deles exatamente como dantes. A regra é de uma linha — se um inimigo está lá, não a podes povoar — e aplica-se a toda a fundação, com ou sem muralha.

> ***▶ Exemplo.** Um reino Imperial com uma sede de população 1,000 funda uma povoação FI1 num hexágono livre: planta de 500g + 500 de pedra (a muralha completa da FI1) + 100 colonos. A sede desce para 900; o novo hexágono abre com população 100, muralha 500/500 — e durante o resto desse turno combate como terreno aberto. Um reino Orc que faça o mesmo funda antes FOR0: 500g + 100 colonos apenas — sem madeira gasta, porque o Nível 0 não tem muralha.*

**2.11.10 Mover um Acampamento (Moving a Camp) — apenas Nómadas**

Um povo Nómada não constrói para ficar. **Um acampamento por turno** (turn) pode levantar as tendas e voltar a montá-las noutro hexágono (hex) que controles, **até 2 hexágonos de distância**, por **1,000 ouro** (gold). Cada acampamento **descansa 6 turnos** antes de poder mover-se outra vez. A ordem (order) encontra-se no painel **⛺ Move a Camp**, no topo do separador Constructions, acima de "Found a New Settlement".

**Que acampamentos se podem mover.** Qualquer construção (construction) da **família FNO (Nómada)** situada num hexágono que controles. Uma povoação de qualquer *outra* família — Genérica, ou conquistada a um vizinho Imperial ou Elfo — nunca se move: foi construída em pedra e argamassa e fica onde foi erguida. Um acampamento que capturaste a *outro reino Nómada* é FNO e **pode** ser movido — com uma exceção: se albergar a **capital ancestral** desse reino (o hexágono onde o reino foi fundado), fica preso a esse chão e não pode ser levado dali. Um acampamento conquistado chega também com o que restar do descanso do seu antigo dono.

**Uma ordem, dois passos, um turno.** O movimento de um acampamento não é resolvido no momento em que o ordenas:

1\. **Fase de Construção (Construction phase, Fase 3).** Todas as condições abaixo são verificadas e o **1,000 ouro é cobrado**. Nada se moveu ainda. O teu relatório (report) traz um cartão **"Camp packing up"** com os dois hexágonos e a taxa.

2\. **Fim do turno**, depois de todo o recrutamento, marchas, combates e desembarques navais terem terminado. As condições que podem ter mudado entretanto são verificadas *de novo*, e só então as tendas descem de facto. O teu relatório traz **"Camp moved"** — ou **"Camp move cancelled"**, com o 1,000 ouro de volta na tua tesouraria. Uma ordem que falhe uma condição no passo 1 traz, em vez disso, **"Camp move refused"** e não custa nada.

**Porque no fim do turno.** Serve o mesmo princípio da pausa do turno de fundação (§2.11.9), por outros meios: *uma batalha já em curso é travada no terreno contra o qual ambos os lados planearam.* A fundação mantém as muralhas de uma povoação nova fora dos combates desse turno; o movimento de um acampamento limita-se a não acontecer até o combate terminar. O teu acampamento fica exatamente onde o inimigo o esperava durante todo o turno em que foi atacado, e só parte depois de a poeira assentar. Nunca podes usar um movimento para fugir a um combate que já se aproxima.

**Um acampamento atravessa apenas o seu próprio chão.** Um acampamento é transportado, não voa: um movimento de **2 hexágonos** passa por um **hexágono intermédio**, e pelo menos um hexágono intermédio tem de ser **terra tua, livre de exércitos e frotas estrangeiros, durante todo o turno**. Em linha reta há um hexágono intermédio, e tem de estar livre. Fora da linha reta há dois, e basta um livre. Um movimento de **1 hexágono** não tem hexágono intermédio, por isso esta regra nunca se lhe aplica — as regras do destino abaixo aplicam-se na mesma.

"Estrangeiro" significa qualquer pessoa exceto tu, um aliado mútuo, o teu suserano ou o teu vassalo. Só contam a terra e as forças: uma povoação, população ou local de produção (production site) no hexágono intermédio não o bloqueiam. Um hexágono intermédio está fechado se:

**Verificado quando dás a ordem (uma recusa, nada pago) e de novo no fim do turno:**

|                                   |                                            |
|-----------------------------------|--------------------------------------------|
| **O que o fecha**                 | **O que o cartão diz sobre esse hexágono** |
| É mar aberto                      | *is open water*                            |
| Ninguém o controla                | *belongs to no one*                        |
| Um aliado, suserano ou vassalo controla-o | *is an ally's land (only your own counts)* |
| Outro reino controla-o            | *is another realm's land*                  |
| Um exército estrangeiro está nele | *holds a foreign army*                     |
| Uma frota estrangeira está no seu porto | *has a foreign fleet in its port*    |

**Verificado apenas no fim do turno, depois de as marchas e a navegação terminarem (cancelam um movimento aceite, e o 1,000 ouro regressa):**

|                                                                                                                          |                                                   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| **O que o fecha**                                                                                                        | **O que o cartão diz sobre esse hexágono**        |
| Era teu quando deste a ordem e foi tomado durante o turno                                                                | *was taken from you this turn*                    |
| Um exército estrangeiro entrou nele durante o turno — atacou o teu exército ou as tuas muralhas aí, ou tomou o hexágono e voltou a perdê-lo | *was entered by a foreign army this turn*         |
| Uma frota estrangeira entrou no seu porto durante o turno, mesmo que tenha seguido viagem                                | *had a foreign fleet put into its port this turn* |
| Houve combate nele sem que nenhum exército entrasse — uma incursão que a milícia da tua povoação repeliu, ou um desembarque | *saw fighting this turn*                          |

Um exército estrangeiro não atravessa a tua terra em paz: entrar no teu hexágono é sempre um combate — com o teu exército, as tuas muralhas ou a tua milícia — pelo que um exército estrangeiro que se aproxime do teu hexágono intermédio deixa sempre atrás de si uma dessas marcas. Só é dada uma razão por hexágono: a primeira que se aplicar, pela ordem das tabelas. O cartão tem por título *"No clear way for the tents:"* e nomeia **todos** os hexágonos intermédios com a respetiva razão, para saberes sempre que caminho estava fechado e porquê. Não diz de quem era a força.

> ***▶ Exemplo — o caminho de passagem.** O teu acampamento está em (27,31).*
>
> *• **Para (29,31), em linha reta a leste.** Há um hexágono intermédio, (28,31). Se for teu e estiver livre, o acampamento move-se. Se um vizinho controlar (28,31), a ordem é recusada e não custa nada: "No clear way for the tents: (28,31) is another realm's land".*
>
> *• **Para (29,32), fora da linha reta.** Há dois hexágonos intermédios, (28,31) e (28,32). O vizinho continua a controlar (28,31), mas (28,32) é teu e está livre: **o acampamento move-se** — um caminho livre chega.*
>
> *• **A mesma ordem, com uma frota neutra no porto do teu (28,32).** Ambos os caminhos estão fechados, e a recusa nomeia os dois: "(28,31) is another realm's land, and (28,32) has a foreign fleet in its port".*
>
> *• **A mesma ordem, com (28,32) livre quando dás a ordem.** A Fase 3 aceita-a e cobra o 1,000 ouro. Depois, durante o turno, acontece uma destas coisas:*
>
> *– um exército inimigo marcha para (28,32) e toma-o → cancelado: "(28,32) was taken from you this turn";*
>
> *– (28,32) tem uma das tuas povoações (isso, só por si, nunca bloqueia), uma incursão inimiga ataca-a e a sua milícia repele-a → cancelado: "(28,32) saw fighting this turn". Um hexágono vazio não tem população nem milícia, pelo que uma incursão nele toma-o (a linha acima);*
>
> *– uma frota neutra entra no porto de (28,32) e volta a sair → cancelado: "(28,32) had a foreign fleet put into its port this turn".*
>
> *De cada vez o 1,000 ouro regressa e o acampamento nunca sai de (27,31).*
>
> *• **Para (28,32), ao lado.** Um movimento de 1 hexágono não tem hexágono intermédio, por isso o caminho de passagem nunca o fecha — quem quer que controle a terra em redor. O próprio destino tem de passar todas as condições da tabela abaixo: terra tua, sem povoação, sem população, sem cerco, sem exército estrangeiro.*

**O que viaja e o que fica:**

|                                                                                   |                                                         |
|-----------------------------------------------------------------------------------|---------------------------------------------------------|
| **Viaja com o acampamento**                                                       | **Fica para trás**                                      |
| Toda a sua população                                                              | Locais de produção (quinta, mina, pedreira, serração, porto) |
| A paliçada, com a integridade **atual** — uma muralha a 180/300 chega a 180/300   | Frotas atracadas num porto do hexágono antigo           |
| O nível do acampamento e, por isso, o seu limite de população                     | Exércitos estacionados **na capital** (ver abaixo)      |
| O seu contador de descanso, que recomeça no novo hexágono                         | A posse do hexágono antigo — continua a ser teu, apenas vazio |
| A tua **sede de recrutamento**, se estava neste acampamento                       | Qualquer memória que um inimigo tenha do acampamento (ver abaixo) |

**O hexágono que deixas fica vazio, não perdido.** Continua a ser território teu, mas a sua população desce para **zero** e — porque os hexágonos vazios nunca são povoados nem crescem (§3.8) — mantém-se em zero até haver de novo um acampamento aí. Isso significa sem imposto (tax) proveniente dele, sem milícia nele e nada para um local de produção trabalhar.

**Um local de produção deixado para trás fica dormente, não abandonado.** Um local de produção rende com a **população** do seu hexágono, e num mapa de construções só um hexágono com povoação a tem (§3.6, §3.8) — pelo que um local cujo acampamento partiu não produz absolutamente nada. A pedreira de que te afastas mantém o nível e **não produz nada** até haver de novo um acampamento aí — volta atrás, ou funda lá, e rende exatamente como antes, ao nível que tinha. Este é o verdadeiro preço de mover, e é por isso que um acampamento crescido junto de um bom porto raramente se move. Uma consequência a ter em conta no planeamento: um **porto** cujo acampamento partiu continua a funcionar como doca para as tuas frotas, mas, sem ninguém a viver no hexágono, já não consegue equipar um casco (§2.12.3).

**A tua sede viaja com o acampamento em que está.** Esta é a única exceção a "a tua sede só muda por conquista" (§2.13.10). A *classificação* de sucessão não é afetada e continua a correr apenas quando um hexágono de sede é capturado — um acampamento em movimento limita-se a levar consigo a sede existente. Os exércitos estacionados **na capital** **não** vão a reboque: tornam-se exércitos de campo na terra que o acampamento deixou, incluindo os que recrutaste nesse mesmo turno. O teu cartão "Camp moved" nomeia-os.

**O descanso entre movimentos.** Um acampamento que se move no turno *N* pode mover-se de novo no turno *N + 6*. **A fundação também inicia o descanso**, pelo que uma povoação que fundes neste turno não pode partir durante outros seis. Três coisas **não** o fazem: um acampamento que o GM pintou no início da campanha nunca foi montado e está pronto no turno 1; **melhorar** um acampamento não reinicia o seu descanso; e um acampamento que **captures** chega com o que restar do descanso do seu antigo dono. O painel Move mostra o estado de cada acampamento, e um cartão de recusa nomeia o turno em que ficará pronto.

**Os mapas inimigos não o veem partir.** Um reino que não consiga ver o hexágono nesse momento mantém o acampamento desenhado no seu mapa, esbatido, exatamente como o viu pela última vez (§2.19). Não fica a saber nada até olhar de novo. Nada na sua página anuncia que um acampamento se moveu.

**Ordenar o movimento e anulá-lo.** Escolhe o acampamento e o seu destino no painel **⛺ Move a Camp**. A lista de acampamentos mostra todos os acampamentos FNO que controlas com o respetivo estado — *ready*, ou *resting — ready on turn N*, ou cercado, ou bloqueado por um exército estrangeiro — e a lista de destinos oferece a terra que controlas ao alcance, sem nada nela e, para um movimento de 2 hexágonos, um caminho pela tua própria terra livre de todos os exércitos estrangeiros que consigas ver — exércitos escondidos de ti, frotas e tudo o que acontece durante o turno são avaliados pelo Processador de Turnos (Turn Processor), e o cartão diz-te o que encontrou. O painel nomeia também qualquer local de produção que ficará inativo e avisa-te quando a tua sede está prestes a viajar. Pôr a ordem em fila retira logo o 1,000 ouro da tesouraria apresentada, para que o resto do teu planeamento reflita com honestidade o que ainda podes pagar, e desenha uma seta dourada no mapa do teu reino, do acampamento até ao destino (com a camada de construções ativa). **Cancel**, no mesmo painel, devolve o 1,000 inteiro e liberta os dois hexágonos. Enquanto o movimento está em fila, **nenhum dos hexágonos aceita outra ordem de construção**, porque um movimento reserva a vaga em ambos.

**Condições, pela ordem em que o motor as verifica.** Nada é gasto até todas terem passado, e uma recusa não custa nada:

|        |                 |                                                                                                                                                               |
|--------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\#** | **Recusa**      | **Significado**                                                                                                                                               |
| 1      | not_era         | Esta campanha não tem construções de todo.                                                                                                                    |
| 2      | not_nomad       | Só um povo Nómada move acampamentos.                                                                                                                          |
| 3      | already_moving  | Já foi **aceite** um movimento de acampamento para ti neste turno — uma ordem recusada não gasta o teu turno.                                                 |
| 4      | no_construction | Não há acampamento nesse hexágono.                                                                                                                            |
| 5      | foreign_family  | Não é um acampamento FNO.                                                                                                                                     |
| 6      | foreign_seat    | O acampamento alberga a capital ancestral de outro reino.                                                                                                     |
| 7      | dest_missing    | O destino não está no mapa.                                                                                                                                   |
| 8      | out_of_range    | O destino é o próprio hexágono do acampamento, ou está a mais de 2 hexágonos.                                                                                 |
| 9      | duplicate       | Outra das tuas ordens de construção já reserva o **destino** — um movimento ocupa a vaga em ambos os hexágonos.                                                |
| 10     | dest_not_yours  | O destino não é terra que controles.                                                                                                                          |
| 11     | dest_not_land   | O destino é mar aberto.                                                                                                                                       |
| 12     | dest_occupied   | O destino já tem uma povoação.                                                                                                                                |
| 13     | dest_inhabited  | Já vive população no destino — raro num mapa normal, onde um hexágono sem povoação não tem população, mas possível num mapa feito à mão ou migrado.          |
| 14     | path_blocked    | Um movimento de 2 hexágonos não tem hexágono intermédio de terra tua livre de exércitos e frotas estrangeiros; o cartão nomeia cada hexágono intermédio e porquê (ver a tabela acima). |
| 15     | besieged        | Um cerco (siege) está sobre o acampamento ou sobre o destino.                                                                                                 |
| 16     | hostile_army    | Um exército estrangeiro está no acampamento ou no destino.                                                                                                    |
| 17     | on_cooldown     | O acampamento ainda está a descansar; o cartão nomeia o turno em que fica pronto.                                                                             |
| 18     | no_gold         | O 1,000 ouro não está disponível quando o turno é processado.                                                                                                 |

Uma nota sobre essa tabela. Se registares uma segunda ordem de construção no hexágono **do próprio** acampamento, a verificação que todas as outras seis ordens de construção partilham recusa uma das duas, e o cartão que escreve tem o título **"Camp move from (col,row)"** — o movimento é a ordem que é descartada, por isso põe as duas em fila pela ordem que mais te importa.

**A segunda verificação, no fim do turno.** Um movimento em fila é cancelado — e o **1,000 ouro reembolsado** — se, terminado o combate: o hexágono do acampamento ou o destino mudou de mãos; o acampamento desapareceu; há agora algo no destino, ou a população se instalou aí; um cerco se fechou em torno de qualquer dos hexágonos; um exército estrangeiro está em qualquer dos hexágonos; o caminho entre eles fechou — nenhum hexágono intermédio continua a ser teu e livre, por qualquer razão da tabela acima (tomado, uma força parada ou em passagem, combate); ou **o acampamento foi disputado em combate durante o turno**. Este último teste é o simples: qualquer batalha (battle) no hexágono do acampamento prende-o — um assalto repelido, uma captura, um bombardeamento, um desembarque. Um acampamento que viu combate não levanta as tendas, qualquer que seja o resultado e esteja ou não o inimigo ainda presente.

> ***▶ Exemplo.** Um acampamento FNO4 de 1,089 pessoas com uma paliçada de 300 pontos e uma pedreira Lv.2 está em (27,31), e é a tua sede. Ordenas-lhe que vá para (29,32), a dois hexágonos — o limite — por (28,31) e (28,32), ambos teus. Na Fase 3, o 1,000 ouro sai da tua tesouraria e recebes um cartão "Camp packing up". O combate do turno decorre em torno do acampamento onde ele está. No fim do turno todas as 1,089 pessoas chegam a (29,32), a paliçada chega a 300, a tua ★ dourada move-se com ele, e o Exército I — que estava na capital — fica em (27,31) como exército de campo. A pedreira fica em (27,31) e não rende nada até um acampamento regressar. O acampamento pode mover-se de novo no turno N+6.*

**2.12 Recrutamento (Recruiting, Pré-Fase 2b) e Fase 4 — Navios & Contratação (Ships & Hire)**

**2.12.1 Recrutar Unidades (Recruiting Units)**

As unidades são recrutadas para exércitos (armies) específicos. Os custos são deduzidos na **Pré-Fase 2b** (Pre-Phase 2b, §2.6a — antes do rendimento, da manutenção e dos mercados); os recrutas fazem parte do exército em **todas** as batalhas do turno, estando parado ou em marcha. A população é deduzida do hexágono de recrutamento — **exceto os engenhos de cerco, que não consomem população de todo** (são *construídos*, não levantados — ver as regras dos engenhos abaixo e §5.8.6).

**A tesouraria (treasury) é um muro rígido.** O Processador de Turnos (Turn Processor) concede apenas o que as tuas reservas cobrem por inteiro, *verificado antes de se cunhar o que quer que seja*: uma ordem que a tesouraria não consegue pagar na totalidade é **reduzida à quantidade comportável** (um cartão indica a redução e o recurso limitativo) e uma ordem que não consegue pagar de todo é **recusada em absoluto — nada cunhado, nada cobrado**. O mesmo se aplica à construção naval (a tripulação só é retirada para os cascos efetivamente construídos), aos **locais de produção** (um edifício ou melhoria que não consigas pagar é recusado antes da tentativa — incluindo prospeções de minas) e às **missões de espionagem** (uma missão não paga *não é enviada*: nenhum agente parte, nada é cobrado, e o cartão di-lo claramente — nunca com a formulação "agente perdido"). Não existe descoberto nem défice perdoado em lado nenhum.

**A capacidade de pagamento é o dinheiro disponível menos as saídas deste turno.** A Página do Jogador (Player Page) só te deixa comprometer a tesouraria que o teu relatório mostra **menos a manutenção, a comida do exército e o tributo de vassalo que o Processador de Turnos cobrará na Fase 2** — e, no caso dos recrutas, a sua própria manutenção e comida do primeiro turno — e valida recrutas, construções de navios, contratações, espiões, construções e fundações face a esse valor; o rendimento deste turno, embora o Processador de Turnos o credite (Fase 1) antes de cobrar a maioria das ordens (Fases 3–4), **não** conta na página. Daqui decorrem duas regras de ordenação do servidor: uma **venda de mercado em fila conta para as construções, fundações, melhorias e deslocações de acampamento deste turno** (os mercados resolvem-se antes da construção, dentro da Fase 3 — §2.11) mas **nunca para recrutas ou engenhos** (Pré-Fase 2b, antes de qualquer mercado — §2.6a), e uma **compra** ou **envio** em fila é deduzido na página de imediato, mesmo que o servidor o cobre mais tarde — de modo que a página pode ser mais restritiva do que o servidor, nunca mais permissiva. Uma ordem que a página permite é sempre uma que o Processador de Turnos consegue pagar, e o saldo mostrado nunca fica negativo.

**Locais de recrutamento e limites por turno:**

|                  |                         |                          |
|------------------|-------------------------|--------------------------|
| **Tipo de hexágono** | **Restrição de terreno** | **Limite por turno**  |
| Território próprio | Qualquer com população | 5% da população do hexágono |
| Território aliado | Qualquer com população | **1%** da população do hexágono |

O limite aplica-se à população do hexágono **tal como o relatório a mostra** — o recrutamento (Pré-Fase 2b) resolve-se antes do crescimento da Fase 1 deste turno, pelo que a pré-visualização da Página do Jogador e o limite do servidor são o mesmo número. O limite é arredondado por defeito (24.7 → 24) em ambos os lados.

Fórmula do limite: max(1, floor(hexPop × capPct)), medido face à população do hexágono no **início da Pré-Fase 2b** (antes do crescimento deste turno, registada quando o recrutamento toca pela primeira vez no hexágono). Este é um **total** por turno: dividir o recrutamento por várias ordens não o aumenta — depois de um hexágono ter dado os seus 5% (próprio) ou 1% (aliado) no turno, o recrutamento adicional aí é reduzido a zero até ao turno seguinte. Os 5% do proprietário e o 1% de um aliado no mesmo hexágono são margens separadas. **As tripulações dos navios saem da mesma margem**: as pessoas que um build_ship da Fase 4 retira num porto contam para os 5% desse hexágono no turno, depois dos recrutas do turno — ver §2.12.3. Se a população do hexágono for zero, o recrutamento falha. Um exército já no mar (embarcado num turno anterior) não pode recrutar — desembarca primeiro. Podes, contudo, recrutar num porto e embarcar o mesmo exército no mesmo turno: o exército embarca primeiro (Pré-Fase 2), os recrutas são levantados no porto um instante depois (Pré-Fase 2b) e são contados a bordo antes de a frota zarpar na Fase 6 — coloca os recrutas em fila *antes* da ordem de embarque; a Página do Jogador recusa o inverso.

**Recrutas a partir de uma construção, e ela determina o que podes levantar.** A população vive apenas dentro de construções (§3.8), pelo que um exército parado em terreno vazio não levanta absolutamente nada — não há ninguém ali. Mais ainda: *que* unidades um hexágono irá mobilizar depende de **a quem pertence o povoado**.

|                                    |                                                                                                       |
|------------------------------------|-------------------------------------------------------------------------------------------------------|
| **A construção em que estás**  | **O que levantará para ti**                                                                        |
| **Da tua própria raça**             | Todo o teu elenco — tudo o que o teu reino pode construir                                                  |
| **Genérica (POP)**                  | Todo o teu elenco. A genérica não tem gente própria, por isso mobiliza a tua                             |
| **De uma raça estrangeira**, compatível   | **Apenas o par de duas unidades dessa raça** (abaixo) — nunca as tuas tropas, nunca elites, nunca engenhos de cerco |
| **De uma raça estrangeira**, incompatível | Nada                                                                                               |
| **Nenhuma** (hexágono vazio)                | Nada                                                                                               |

**A compatibilidade é mútua** — se os Anões mobilizam para os Elfos, os Elfos mobilizam para os Anões. Quem se entende com quem:

|                        |                                                      |
|------------------------|------------------------------------------------------|
| **Reino recrutador** | **Levantará tropas nestas construções estrangeiras** |
| Imperial               | Todos — o Império negoceia com todos                 |
| Bárbaro              | Imperial, Anão, Orc, Aesir, Nómada                   |
| Anão                  | Imperial, Elfo, Bárbaro, Aesir                      |
| Elfo                    | Imperial, Anão                                  |
| Aesir                  | Imperial, Anão, Orc, Bárbaro                      |
| Orc                    | Imperial, Bárbaro, Aesir                           |
| Nómada                  | Imperial, Bárbaro                                  |

*(A genérica é compatível com todos e não consta da lista. Um reino é sempre compatível com a sua própria raça.)*

**Os pares de duas unidades** que um povoado estrangeiro oferecerá — as suas tropas mais comuns, nunca as melhores:

|            |                          |
|------------|--------------------------|
| **Família** | **Oferece**               |
| Imperial   | Velites, Legionnaire     |
| Bárbaro  | Berserker, Raiders       |
| Elfo        | Swordmaster, Bladedancer |
| Anão       | Ironclad, Warrior        |
| Orc        | Goblin, Uruk-Hai         |
| Aesir      | Shore Raider, Axe Thane  |
| Nómada       | Rajjala, Naffatun        |

**As tropas de outros povos são, no máximo, 20% de um exército.** "Outros povos" são unidades de qualquer raça exceto a do teu próprio reino — na prática os pares acima, levantados num povoado estrangeiro. Todas as unidades do exército contam para o total, **engenhos de cerco incluídos**. O limite é verificado sempre que a composição de um exército muda por ordem tua:

- **Recrutamento.** A margem restante é o maior número de tropas estrangeiras que as mantém em **20% ou menos** do exército inteiro *depois* de chegarem — um quarto das unidades próprias (não estrangeiras) do exército, arredondado por defeito, menos as tropas estrangeiras que já tem: 20 próprias → margem para **5**; 80 próprias → **20**; 100 próprias → **25**; 80 próprias + 20 estrangeiras → **0**. Se pedires mais, o Processador de Turnos recruta apenas o que couber; o cartão de recrutamento diz *Reduzido: pedidos 30, obtidos 20 (tropas estrangeiras no máximo 20% de um exército)* ou, quando não há margem nenhuma, *Recrutamento falhado* com a contagem do exército.

- **Um novo exército não pode começar estrangeiro.** Um exército sem tropas não tem margem — recruta primeiro nele a tua própria gente. Se forem recrutadas no **mesmo turno**, contam: os recrutas da própria raça e os engenhos são sempre contados antes dos estrangeiros, qualquer que seja a ordem em que os registes.

- **Quando é contado.** O recrutamento resolve-se na Pré-Fase 2b — **depois** das dispensas deste turno e **antes** das transferências e divisões deste turno (Fase 4.5). Assim, uma transferência em fila neste turno ainda não dá nem retira margem para os recrutas deste turno; a Página do Jogador conta da mesma forma.

- **Transferências, fusões e divisões** são recusadas por inteiro se qualquer dos exércitos ficasse **acima de 20% estrangeiro** — ou, para um exército já acima, **mais estrangeiro do que era** (comparado como proporção). Entregar tropas *próprias* de um exército misto também conta: as tropas que ficam para trás tornam-se mais estrangeiras. Uma divisão não pode criar um exército acima de 20% estrangeiro.

- **As dispensas** seguem o mesmo teste: dispensar as tuas tropas próprias é recusado se deixasse o exército acima de 20% estrangeiro (ou mais estrangeiro do que era); dispensar tropas estrangeiras é sempre permitido. A Página do Jogador também recusa uma dispensa que não deixasse margem para recrutas estrangeiros que já puseste em fila neste turno — desfaz primeiro alguns deles.

- **Um exército que fica acima de 20% mantém todos os soldados que tem.** Isso acontece quando já estava acima antes desta regra, ou por **perdas em batalha** e **atrito**, que nunca são recusados. Simplesmente não aceita mais tropas estrangeiras; a tua própria gente pode sempre juntar-se-lhe, e uma transferência ou divisão não pode torná-lo mais estrangeiro.

- **O que vês.** A caixa de Unidades Alistadas mostra a proporção de cada exército (*Outros povos: 20 de 100 (20%) · limite 20%*, a vermelho quando excedido). Num povoado estrangeiro, cada unidade oferecida indica *margem para mais N* e fica a cinzento com o motivo quando não há; uma transferência, divisão ou dispensa recusada nomeia o exército e a sua contagem.

> ***▶ Exemplo — a regra dos 20% ao longo de um turno.** O Exército I (80 Legionnaires) está numa fortaleza anã capturada; o Exército II (10 Legionnaires) está ao lado.*
>
> *- **Recrutar.** Ordenas 30 Ironclads para o I. A margem é 80 ÷ 4 = **20**, pelo que chegam 20 (20 de 100 = 20%) e o cartão diz que a ordem foi reduzida. No turno seguinte o I já não tem margem: 20 de 100 já é o limite.*
>
> *- **Entregar tropas próprias.** Ordenas ao I que transfira 50 Legionnaires para o II. O I ficaria com 30 Legionnaires + 20 Ironclads — 20 de 50 é 40% — pelo que a transferência é **recusada**.*
>
> *- **Uma transferência mista.** Em vez disso, envias 10 Legionnaires e 5 Ironclads do I para o II: o I fica com 15 de 85 (17.6%), o II passa a 5 de 25 (20%) — ambos dentro do limite, pelo que é aceite.*
>
> *- **Uma divisão.** Separar os 20 Ironclads num novo exército tornaria 20 de 20 estrangeiros — **recusado**.*
>
> *- **Um exército já acima.** Um exército de 10 Ironclads (de antes da regra) mantém-nos. Não aceita mais tropas estrangeiras, mas 10 Legionnaires podem juntar-se-lhe (10 de 20 — menos estrangeiro do que antes).*

**Os engenhos de cerco são construídos, não levantados.** Os engenhos ficam fora de todo o sistema de construções acima. Um **exército parado** constrói os engenhos da sua própria raça **onde quer que esteja em terra — terreno próprio, de um aliado, neutro ou o acampamento de cerco inimigo, indistintamente**, com construção ou sem ela, sem consumir **qualquer população** e pagando **apenas materiais** (250g + 50w + 10i cada, diretamente das tuas reservas, sob a regra do muro rígido acima). Restam quatro limites: **(1)** apenas o engenho da **tua própria raça** — nenhum projeto estrangeiro, seja qual for a construção por baixo; **(2)** a ordem tem de nomear um **exército existente** — uma ordem de engenho nunca pode levantar um novo; **(3)** um exército **embarcado no mar** não pode construir (tal como qualquer recruta); **(4)** o **rácio de tripulação**: cada engenho precisa de uma tripulação de **5 soldados**, contada como rácio *permanente* — o total de engenhos do exército depois da construção nunca pode exceder floor(soldiers ÷ 5), em que **só as unidades que não são engenhos contam como tripulação** (engenhos não tripulam engenhos). 25 soldados sustentam no máximo 5 engenhos, neste turno ou sempre, até o exército crescer. As baixas nunca destroem engenhos retroativamente — um exército reduzido simplesmente não pode construir mais, e só os engenhos tripulados disparam (§5.8.6). As ordens além do rácio ou da tesouraria são reduzidas com um cartão explicativo.

Tudo isto se aplica **de forma idêntica num hexágono aliado**; só o limite muda (**1%** em vez de 5%). **As reservas são independentes:** o teu 1% e os 5% do próprio proprietário são tetos separados na mesma povoação, e dois aliados que a mobilizem no mesmo turno recebem cada um o seu 1% — uma povoação pode perder até 5% mais 1% por cada recrutador aliado. **O teu aliado é avisado:** cada levantamento numa povoação aliada coloca no relatório do proprietário um cartão *Recrutamento aliado em (col,row) — −N população* que nomeia quem recrutou o quê e a população da povoação antes e depois. O teste de compatibilidade corre sempre entre a *tua* raça e a raça *da construção* — a raça do teu aliado nunca entra nele. Assim, num povoado orc capturado de um aliado, um Elfo não levanta nada, porque Elfos e Orcs não mobilizam um para o outro, seja quem for o dono do terreno.

> ***▶ Exemplo.** Um exército Imperial que ocupe uma fortaleza anã capturada pode levantar aí **Ironclads e Warriors** — tantos quantos couberem no limite de 20% abaixo — e nem um único Legionnaire, porque um povoado estrangeiro nunca mobiliza a tua própria gente. Para levantar legiões, marcha para um hexágono com uma construção Imperial ou Genérica.*

**Limites de forças.** Um reino pode ter no máximo **10 exércitos** (ranhuras I–X) e **5 frotas** em simultâneo. A pilha por hexágono (3 exércitos), o grupo de ligação (3) e a margem na sede de recrutamento (muster seat) continuam a aplicar-se: com dez exércitos nunca podes levantar mais de três antes de mover alguns, nem marchar mais de três em conjunto. No separador Exército da Página do Jogador, os exércitos levantados têm cartões completos; as ranhuras por levantar dobram-se numa única faixa no topo — um chip por ranhura, a ranhura seguinte com o botão Levantar, uma ranhura destruída a manter o seu 💀 até ser levantada de novo, e uma linha de aviso a explicar porque está o levantamento bloqueado (Orcs e Anões não têm frotas de todo), mais até **10 personagens vivas**. Estes limites são impostos pelo **Processador de Turnos**, não apenas pela UI da Página do Jogador — um ficheiro de ordens editado à mão que peça um 11.º exército ou uma 6.ª frota é rejeitado no servidor. Dissolver (ou perder) um exército/frota liberta uma ranhura.

> ***▶ Um exército ou frota vazio não sobrevive ao turno.** No fim de cada turno, qualquer exército **sem soldados** e qualquer frota **sem navios** é riscado dos registos e a sua ranhura é libertada. O recrutamento e a construção naval resolvem-se mais cedo no turno, pelo que **levantar uma força e enchê-la no mesmo ficheiro de ordens é seguro** — mas levantar uma e deixá-la vazia não é: será dissolvida antes de o turno acabar e terás de a levantar de novo. Não podes guardar uma ranhura vazia em reserva.*
>
> *Um exército sem tropas não pode ser encontrado, combatido nem mantido. As ranhuras são **I–X** para exércitos e **I–V** para frotas, e nada mais: o Processador de Turnos recusa uma ordem create_army/create_fleet que traga qualquer outro numeral, nomeando as ranhuras válidas no cartão de recusa.*

Nos mapas da Página do Jogador (minimapa e mapa do Exército) e nos cartões de exército, os teus exércitos são marcados com o **escudo de nação** do teu reino (o mesmo escudo mostrado no separador Perfil — reinos da mesma raça recebem escudos distintos automaticamente) com o numeral do exército **I a X** num pequeno emblema na parte inferior do escudo. Os exércitos aliados (qualquer aliado confirmado — uma aliança declarada ou mútua, o teu suserano ou um dos teus vassalos) também ostentam o **escudo de nação** desse aliado no minimapa e no mapa do Exército — sem o emblema numérico, pois os números internos dos seus exércitos não te são mostrados. Os exércitos de reinos com quem estás em **guerra** mostram um emblema inimigo distinto, e os exércitos de reinos **neutros** (paz ou sem declaração) mostram um emblema neutro distinto, nesses mesmos dois mapas; o escudo de nação de um rival nunca te é mostrado. **As frotas são marcadas da mesma forma, com uma âncora (⚓) acrescentada ao escudo para o marcar como frota e não como exército:** as tuas frotas mostram o teu escudo de nação com o numeral da frota **I a V** e a âncora; as frotas estrangeiras mostram o emblema de postura do dono — um escudo de nação aliado, ou um escudo naval distinto de guerra ou neutro — cada um com a âncora. Estes marcadores de escudo aparecem de forma consistente nas três superfícies — o minimapa, o mapa do Exército e o mapa da Marinha (os exércitos terrestres estrangeiros no mapa da Marinha também ostentam os seus escudos de postura).

Se o exército referido não existir no estado do GM, o TP tenta a recuperação criando-o na tua **sede de recrutamento** (apenas no hexágono próprio).

Os novos exércitos são mobilizados na tua **sede de recrutamento** — a tua capital designada pelo GM (§3.7.3), ou a sua sucessora se for conquistada (**§2.13.10 Sucessão da Capital**).

> ***▶ Exemplo — o limite de recrutamento esgota-se depressa.** Um hexágono com 2,000 de população limita o recrutamento em território próprio a max(1, floor(2,000 × 0.05)) = 100 soldados neste turno; ao recrutar no hexágono de um aliado, o limite é apenas floor(2,000 × 0.01) = 20. A população é gasta à medida que recrutas, por isso o limite encolhe no próprio turno — não podes drenar um hexágono até zero num só turno. Uma aldeola minúscula continua a permitir pelo menos 1 recruta (o mínimo de max(1, …)), mas um hexágono com população zero não permite nenhum. Para levantar rapidamente um grande exército, recruta em paralelo de vários hexágonos populosos em vez de martelar um só.*

**2.12.2 Mistura de Experiência no Recrutamento (Experience Blending on Recruitment)**

Os novos recrutas juntam-se a uma pilha com WP base e diluem proporcionalmente a sua experiência (§5.3.4).

**2.12.3 Construir Navios (Building Ships)**

Os reinos Orc e Anão não podem construir navios — as ordens build_ship destas raças são rejeitadas.

**A frota tem de estar atracada num dos teus próprios portos.** Uma frota no mar — ou atracada num porto aliado, neutro ou inimigo — não pode construir; o Processador de Turnos rejeita a ordem (a Página do Jogador bloqueia-a antes de a poderes submeter). O porto memorizado de uma frota é simplesmente o **último porto em que atracou**, seja quem for o dono — só a própria ordem de construção verifica a propriedade — pelo que podes construir em **qualquer** porto próprio em que entres, não apenas onde a frota foi levantada pela primeira vez. **Um bloqueio não impede a construção**: uma frota tua atracada num porto bloqueado pode construir aí, e pode ser levantada uma nova frota — embora, ao lado do bloqueador, combata-o antes de qualquer frota se mover (§2.6).

Os navios são acrescentados à frota especificada. Custos deduzidos na Fase 4 (a capacidade de pagamento é o dinheiro disponível, §2.12.1).

A tripulação é deduzida da população do hexágono do porto: **\`crewPerShip = the hull's wood cost\`**. Um casco leva tantas pessoas quantas a madeira que custa:

|           |            |              |                 |
|-----------|------------|--------------|-----------------|
| **Raça**  | **Casco**   | **Capacidade** | **Madeira = tripulação** |
| Imperial  | Drommund   | 100          | 50              |
| Imperial  | Cog        | 200          | 90              |
| Imperial  | Galley     | 300          | 130             |
| Bárbaro | Wolfship   | 80           | 45              |
| Bárbaro | Reaver     | 120          | 65              |
| Bárbaro | Tigress    | 200          | 100             |
| Elfo       | Moonskiff  | 60           | 40              |
| Elfo       | White Ship | 100          | 60              |
| Elfo       | Swan Ship  | 150          | 85              |
| Aesir     | Snekkja    | 80           | 45              |
| Aesir     | Longship   | 140          | 75              |
| Aesir     | Busse      | 220          | 105             |
| Nómada     | Dhow       | 100          | 50              |
| Nómada     | Shini      | 140          | 70              |
| Nómada     | Harraqa    | 60           | 45              |

Os Orcs e os Anões não constroem navios e não têm linha.

**As tripulações contam para o teto de população por turno do hexágono.** Um hexágono de porto dá no máximo max(1, floor(hexPop × 5%)) pessoas por turno a **recrutas e tripulações em conjunto** — o mesmo registo e o mesmo total corrente que em §2.12.1, primeiro os recrutas (Pré-Fase 2b), depois as tripulações (Fase 4). Uma ordem que precise de mais é **reduzida** aos cascos que ainda podem ser tripulados, os cascos reduzidos não são cobrados, e o cartão diz que foi o teto de população a causa (*"PARCIAL: pediste N, mas o hexágono do porto dá P pessoas por turno a recrutas e tripulações em conjunto — só M puderam ser tripulados"*). Quando nada resta, a ordem é recusada com a mesma explicação. A Página do Jogador reduz da mesma forma antes de poderes pôr a ordem em fila.

> ***▶ Exemplo — 900 Dhows numa só ordem.** A capital da Nemedia tem 15,000 pessoas, e uma ordem pede **900 Dhows**. O hexágono dá floor(15,000 × 5%) = 750 pessoas por turno a recrutas e tripulações em conjunto. Um Dhow custa 50 de madeira, pelo que leva **50 de tripulação**. Sem recrutas nesse turno, são encomendados floor(750 / 50) = 15 Dhows e 885 são reduzidos; se 400 soldados tivessem sido recrutados lá primeiro, restariam 350 pessoas e só 7 Dhows largariam. Uma frota é uma sangria para um povoado, não uma linha na tesouraria.*

**Um porto que não consegue tripular os cascos não constrói nada.** Depois da redução do teto acima, se o hexágono do porto ainda tiver menos pessoas do que a tripulação de que a ordem reduzida precisa — foi drenado depois de o turno começar — a **ordem inteira é recusada** e nada é cobrado. Os navios precisam de braços, e os braços vêm do povoado nesse hexágono. Isto pesa mais num porto cujo acampamento se mudou (§2.11.10): o porto continua a funcionar como doca, mas sem ninguém a viver lá não consegue tripular nada.

**2.12.4 Contratar Personagens (Hiring Characters)**

Custo por omissão: **1000g**. Em cada turno a tua corte atrai **3 candidatos** (o conjunto de candidatos), cada um com atributos fixos (Militar, Economia, Gestão, Política — 1–100) sorteados pelo Processador de Turnos e listados no teu relatório. Abre **Contratar**, escolhe o candidato que queres e dá-lhe um nome. Os atributos são **definidos pelo servidor e fixos**: recarregar o teu relatório mostra os mesmos candidatos — não podes voltar a sortear para obter números melhores. Os candidatos ficam na corte até serem contratados; cada contratação é substituída por um candidato novo. Um senhor contratado junta-se à tua corte no turno seguinte — atribui-lhe então o papel (ver Parte VII).

**2.12b Fase 4.5 e 4.6 — Transferências de Exércitos (Army) e Frotas (Fleet)**

Depois do recrutamento (Recruitment, Pré-Fase 2b) e antes do movimento, podes **redistribuir forças dentro do teu próprio reino**:

- **\`transfer_units\` (Fase 4.5)** move unidades de um dos teus exércitos para outro; **\`transfer_ships\` (Fase 4.6)** move navios entre duas das tuas frotas.

- Os dois exércitos (ou frotas) têm de estar no **mesmo hexágono (hex)**. Adjacente não chega — faz marchar ou navegar ambos para o mesmo local primeiro. A posição é medida a partir das **posições do início do turno**, nunca a partir de onde uma deslocação pendente te colocaria, e uma transferência recusada por distância traz um cartão com os dois hexágonos, pelo que nunca pode falhar em silêncio. Um **exército** de origem não pode estar embarcado nem destruído.

- **Frotas carregadas.** Uma frota que transporta um exército pode **receber** cascos (hulls) livremente — a capacidade só aumenta e o exército embarcado continua a bordo. Também pode **ceder** cascos, mas apenas os de que o seu exército não precisa: os cascos que **mantém** têm de continuar a comportar a tonelagem do exército (infantaria ×1, montada ×2 — a mesma medida do embarque), e **um transportador nunca fica vazio**. A tonelagem é lida na **contagem em tempo real** quando as transferências são resolvidas (após a Fase 1), não no que viste durante o planeamento. Um pedido que viole qualquer dos limites é **recusado por inteiro** — sem preenchimento parcial — com um cartão que indica o exército, a sua tonelagem e o espaço que ficaria. *Transferir Tudo (Fundir)* não é oferecido num transportador.

- **O cartão da Marinha diz-te o que podes ceder.** Numa frota carregada, o painel Transferir Navios mostra *"Transporta o Exército X — carga T / capacidade C: podes libertar até S de capacidade, e nunca o último casco"*, limita cada linha de casco ao que esse tipo, sozinho, poderia libertar (uma linha que não pode ser dispensada fica a cinzento) e volta a verificar uma seleção mista quando clicas. Quando uma frota com cascos **não tem parceiro elegível**, o painel não desaparece: indica o motivo — nenhuma frota neste hexágono · a frota aqui tem uma rota planeada (cancela-a) · já enviou cascos neste sentido · nenhum dos teus cascos pode ser dispensado.

- Um exército ou frota de origem pode fazer **uma transferência por turno (Turn)**; uma segunda transferência da mesma origem é recusada com um cartão.

- Não podes transferir em **ambos os sentidos** entre o mesmo par no mesmo turno.

- **Um recetor pode marchar ou navegar no mesmo turno.** As transferências são resolvidas antes do movimento (Fase 4.5/4.6), pelo que o exército ou a frota que recebe unidades ou cascos desloca-se com a sua força **fundida**: o seu movimento é definido pela unidade ou casco mais lento **depois** da fusão — a infantaria que se junta a cavalaria marcha ao passo da infantaria. Nada se move duas vezes (as unidades vieram do mesmo hexágono), e um recetor continua a não poder passá-las adiante (regra seguinte). Na Página do Jogador, planeia a fusão **primeiro** e a rota **depois** — o painel de transferência pede-te que cances uma rota já planeada para o recetor, para que a rota seja replaneada ao passo fundido. Dois conflitos continuam a recusar a *transferência*: um recetor **a embarcar** — o exército sobe à sua frota logo no início do turno, muito antes de as transferências serem resolvidas, pelo que não se podem entregar unidades a uma força que já está a subir a bordo. **Cláusula de ligação:** um **recetor ligado cujo LÍDER do grupo tenha uma ordem de movimento** também recusa a transferência (cartão viaLink) — a marcha do líder pode pertencer a um **soberano aliado**, e a tua transferência nunca cancela o movimento de grupo de outro reino; desliga primeiro, ou deixa o líder manter-se parado.

- **Um exército ou frota que recebeu uma transferência neste turno não pode ceder uma.** Uma força que recebeu unidades ou cascos não os pode passar adiante até ao turno seguinte — as cadeias de retransmissão no mesmo turno (A→B→C) são recusadas (pode, contudo, marchar ou navegar com eles). Ceder primeiro e receber depois no mesmo turno é permitido: nada se move duas vezes. *(Esta regra é aplicada pelo Processador de Turnos (Turn Processor) — uma transferência infratora simplesmente falha, e o teu relatório traz um cartão a explicar porquê.)*

- As tropas transferidas mantêm a sua experiência: a experiência do destino passa a ser uma média ponderada pelo número de unidades entre a sua própria e a das unidades que chegam (a mesma mistura usada ao recrutar tropas novas).

- **Transferir Tudo move a contagem em tempo real.** Um envio de pilha completa é marcado no momento do planeamento, e o Processador de Turnos transfere o que essa pilha contiver quando as transferências são resolvidas (Fase 4.5) — incluindo soldados de infantaria obtidos por reprodução dos Orcs na Fase 1 do mesmo turno. O exército de origem esvaziado é sempre dissolvido automaticamente; os recém-nascidos nunca são deixados para trás num resto de um só goblin. Para frotas, *Transferir Tudo* também esvazia e dissolve a origem — razão pela qual nunca é oferecido numa frota que transporte um exército.

- **As tropas de outros povos ficam dentro de 20% de cada exército** — uma transferência, fusão ou divisão que levasse qualquer dos exércitos acima desse valor (ou deixasse um exército já acima com mais estrangeiros do que tinha) é recusada (§2.12.1).

- **Uma transferência pode ser anulada neste turno.** Depois de submetida, o painel de transferência mostra um botão **✕ Cancelar transferência** que a reverte por completo — as unidades (ou navios) movidas regressam ao seu exército ou frota original, e uma origem que uma *Transferir Tudo (Fundir)* dissolveu automaticamente é restaurada. (Emite de novo qualquer ordem de movimento ou de postura que a força dissolvida tivesse; essas não são restauradas.)

Isto é pura reorganização interna — consolida uma força dispersa numa única pilha forte, ou retira veteranos para criar um novo exército ou frota. Nada é transferido para outros reinos.

> ***▶ Dividir — retirar um novo exército ou frota de um já existente.** Os cartões do Exército e da Marinha trazem um painel **Dividir** ao lado de Transferir: indica quantas de cada unidade (ou casco) retirar, e o **próximo espaço vazio** é criado **no mesmo hexágono** quando o turno é processado — os exércitos na Fase 4.5, as frotas na Fase 4.6, exatamente onde as transferências são resolvidas, sobre as posições do início do turno. Assim, a divisão precisa de um espaço livre (10 exércitos / 5 frotas por reino) e de lugar no hexágono (3 exércitos ou 3 frotas), e a nova força **fica parada neste turno**: não pode marchar, navegar nem ceder uma transferência no turno em que nasce (uma ordem de movimento editada à mão para ela é recusada com um cartão), e recebe as suas próprias ordens a partir do turno seguinte — a página mostra-a como um cartão tracejado pendente com **✕ Cancelar divisão**. A nova força **herda o estado de prontidão da origem** e cada pilha **mantém a sua experiência**; começa em postura de Movimento, **fora de qualquer ligação**, **sem comandante** (a origem mantém o seu). Nada é reembolsado nem perdido. Recusados, com um cartão: uma origem **a bordo de uma frota** ou uma frota **que transporta um exército** (vai para terra ou desembarca primeiro), uma divisão que **esvaziaria a origem** (isso é uma fusão — usa Transferir Tudo, ou Dissolver), e soldados deixados abaixo da **tripulação de que os seus engenhos precisam** em qualquer das metades. Uma frota pode dividir-se **em qualquer lugar**, no mar ou no porto; uma frota dividida no porto fica atracada aí. Uma origem dentro de um **grupo de ligação** ou em **Cerco** pode dividir-se — a nova força fica fora do grupo, e um anel de cerco passa a contar menos efetivos a partir daí. Uma divisão por origem por turno, e a página recusa uma divisão (ou uma transferência, dispensa, recrutamento, construção naval, anulação de recrutamento, dissolução ou embarque) que toque num exército ou frota que já esteja a dividir-se neste turno — cancela primeiro a divisão. A força pendente não é oferecida em lado nenhum (nem como alvo de transferência, candidata a ligação ou frota onde embarcar) até existir; o espaço no hexágono é avaliado onde as forças **se encontram** no início do turno, não onde planeiam estar.*

**2.13 Fase 5 — Movimento de Exércitos e Combate Terrestre (Army Movement & Land Combat)**

> ***Nem toda a conquista terrestre acontece nesta fase.** A Fase 5 abrange o combate conduzido por exércitos **a marchar em terra** — batalhas campais, tomadas de hexágonos e assaltos alcançados por terra. Um hexágono também pode mudar de mãos na **Fase 6**, através de um **desembarque anfíbio** (§2.14.6), que é resolvido **depois** desta fase. Assim, um hexágono que passou pela Fase 5 intacto ainda pode cair no mesmo turno perante um desembarque na praia — não leias "sobreviveu à fase terrestre" como "seguro durante o turno". Vê o aviso de ordenação em §2.14.6.*

**2.13.0 A Marcha, Passo a Passo (The March, Step by Step)**

**Ordens em vigor.** O registo do teu turno abre a Fase 5 com um cartão de **Ordens em vigor**: uma entrada por exército, que mostra onde se encontra (e de que lado das muralhas), o seu estado, a postura **em vigor** nesta fase e de onde veio essa postura — *mantida do turno anterior* ou *ordenada neste turno* — e a ordem que leva neste turno. A postura mostrada é aquela que as suas batalhas vão usar, depois de todas as regras aplicadas: uma marcha deixa o exército sem postura (Movimento), e uma postura que não se pode manter no seu hexágono di-lo (*a tua Guarnição não se mantém aqui* em terreno aberto, onde combate em Defensiva). Um exército ligado mostra o líder que segue; um exército embarcado mostra a frota que o transporta. Um reino que faltou ao turno também recebe o cartão — é quando as suas posturas guardadas mais importam.

**Dentro das muralhas.** Num hexágono com muralhas de pé, apenas um exército em **Guarnição (Garrison)** — do dono ou de um amigo — fica **dentro**, atrás das muralhas; todas as outras posturas ficam **fora**, em terreno aberto, e um exército **cercado (besieged)** permanece dentro enquanto o anel se mantiver (§5.8.0, §2.13.7). Uma Guarnição nunca sai para combater; só sai um exército cercado que **ordene Surtida (Sally)**. Assim, o cartão indica a zona, e se um cerco te prende:

|                                                                       |                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **O cartão diz**                                                      | **Significado**                                                                                                                                                                                                                       |
| *inside the walls*                                                    | Este exército está em Guarnição: um ataque tem de vencer primeiro os exércitos de fora e depois tomar as muralhas de assalto — e este exército defende-se atrás delas a ×1.30.                                                        |
| *inside the walls · besieged by X — Garrison or Sally only, no march* | Um reino em guerra contigo cerca estas muralhas (§2.13.7): este exército mantém **Guarnição** (qualquer que fosse a sua postura), não pode marchar para fora, e pode ordenar **Surtida** — ou embarcar (um embarque em porto apenas no teu próprio porto; caso contrário, uma recolha na praia). |
| *outside the walls*                                                   | O teu exército acampa diante de muralhas que não são tuas (ou está fora das tuas, em qualquer postura exceto Guarnição, ou com o seu líder de ligação fora).                                                                           |

Quem toma de assalto ou cerca muralhas fica em guerra com todos os reinos que estão lá dentro, incluindo o seu próprio aliado (§5.6).

> ***▶ Exemplo — atrás das muralhas.** O teu Exército II (Guarnição) e o teu Exército III (sem postura) estão no teu hexágono amuralhado (29,27): a linha de II diz inside the walls, a de III diz outside the walls. Uma marcha inimiga encontra primeiro III, em campo aberto; derrotado, III entra na Guarnição, e o assalto segue contra ambos (o percurso completo está no exemplo trabalhado de §5.8.0).*
>
> *Army II (29,27) inside the walls · 92% · Garrison (kept from last turn) — order: none*
>
> *Army II (29,27) inside the walls · besieged by Aquilonia — Garrison or Sally only, no march · 81% · Garrison — after the Sally fought in Pre-Phase 3 — order: stays ← the turn it ordered Sally*

Um quadro sequencial de tudo o que acontece a um exército em marcha num turno — cada passo aponta para a secção que detém o pormenor.

**Antes de a marcha começar:**

1\. **Pré-fase** — formam-se os grupos de ligação (líder + membros, incluindo ligações ordenadas *neste* turno), os embarques são reaplicados, e os **recrutas juntam-se (Pré-Fase 2b, §2.6a — combatem tudo o que se segue)**, depois resolvem-se as posturas de cerco/assalto em vigor. Um exército que apresenta uma marcha juntamente com Cerco ou Assalto marcha, e a postura é ignorada nesse turno (*Stance Ignored*); ordenar a um exército "estacionário" que marche lê-se como a postura de Movimento; um exército **cercado** não pode marchar de todo — a sua marcha é recusada (§2.13.7).

2\. **Fase 4** — apenas navios e contratações; nada se junta aqui a um exército (os recrutas juntaram-se no passo 1, Pré-Fase 2b — §2.6a — e contam para o efetivo da marcha e para as contas da tripulação).

3\. **Fase 4.5** — primeiro as divisões (um novo exército retirado de um existente é criado no mesmo hexágono e **fica parado**, §2.12b), depois as transferências: um exército que recebeu unidades neste turno **ainda pode marchar** ao seu passo fundido, e o cedente também, com o que manteve. A Página do Jogador não te deixa planear uma rota para um exército criado por divisão, e só deixa um exército embarcar numa frota que recebe cascos se o exército couber **sem** esses cascos — os exércitos embarcam antes de as transferências serem resolvidas.

**A Fase 5 abre com o varrimento de acampamento (camp sweep):** os exércitos já em guerra acampados na mesma zona de um hexágono combatem antes de qualquer marcha (§2.13.5); um exército que combateu não descansa neste turno.

**Receção de ordens (a Fase 5 começa):**

4\. Elegibilidade: o exército existe, não está destruído, não está embarcado. **Ordens de movimento duplicadas** — só a primeira por exército é respeitada (um cartão).

5\. **Um membro de uma ligação não se pode mover por si** — a sua ordem é ignorada com um cartão; a ordem do líder move o grupo inteiro, ao passo do seu membro mais lento.

6\. **Reclamar o terreno onde estás (§2.13.2b)** — um exército que inicia a marcha em terreno **aberto** estrangeiro e não aliado combate primeiro por *esse* hexágono: a disputa com a população, **antes do salto 1**, com guerra declarada conforme necessário (§2.13.8). Uma origem **amuralhada** nunca é disputada por uma partida — o exército simplesmente marcha dali.

7\. O **orçamento de pontos de movimento** fixa o preço do percurso: 60mp a pé / 90mp totalmente montado, custos de terreno e de raça por hexágono (§2.13.2) — e **um exército que arrasta engenhos de cerco é uma coluna de cerco: um hexágono por turno**, os saltos extra são descartados com um cartão (§5.8.6).

**A marcha em si — por rondas, um hexágono de cada vez (§2.13.1):**

8\. Todo o exército em marcha torna-se um cursor e avança **exatamente um hexágono por ronda**, por ordem de ESTADO reordenada a cada ronda (§2.13.1). Isto é toda a "aleatoriedade" do movimento: só importa quando dois exércitos disputam o mesmo hexágono na mesma ronda.

9\. **Cada salto reverifica a realidade**: o exército continua vivo (as baixas de uma batalha anterior na mesma ronda contam), o que diz o orçamento *agora* (é recalculado a partir da composição em tempo real — perde o teu último cavalo a meio da marcha e o salto seguinte é cobrado como a pé; o orçamento só pode diminuir, nunca aumentar a meio da marcha), e qual é *realmente* o terreno (um salto planeado para o nevoeiro resolve-se contra o mapa verdadeiro — o exército pára onde já não pode pagar, ou se o hexágono oculto for mar).

10\. **Entrar num hexágono resolve-se, de imediato**: um exército de campanha inimigo → **batalha** (§2.13.5; vence com pontos e rondas de sobra → segue em marcha; perde → retirada, ou aniquilação apenas se cercado); uma **construção amuralhada** estrangeira → uma batalha contra os exércitos **de fora** primeiro e depois, se vencida, um **assalto precipitado à chegada** contra a Guarnição lá dentro, mesmo um detentor que a tenha tomado mais cedo nesta fase (§5.8.0, §2.13.6b; repelido mas vivo → acampado às portas); um **hexágono aberto com população** estrangeiro → a disputa de apreensão pela milícia (§2.13.4); um **hexágono cheio** (3 exércitos amigos, com consciência de zona antes das muralhas) → bloqueado com um cartão (§2.13.3).

11\. **Uma paragem é definitiva.** Qualquer bloqueio, derrota ou orçamento esgotado fecha o cursor — o resto do percurso é descartado para o turno, mesmo que o obstáculo se afaste depois.

**Depois da fase terrestre:** os exércitos embarcados movem-se com as suas frotas na **Fase 6** — incluindo desembarques anfíbios que podem tomar um hexágono *depois* de a Fase 5 o ter deixado intacto (vê o aviso no topo desta secção); os exércitos deixados em guerra numa zona encontram-se no varrimento de acampamento seguinte (§2.13.5); um exército que nem se moveu nem pressionou um cerco **recupera +33 de ESTADO** — a menos que esteja acampado num **hexágono fortificado estrangeiro** (§5.10.5); e todo o hexágono em que um exército pisou (mais o seu anel) passa a ser *recordado* no teu mapa, para sempre (o nível de nevoeiro só de terreno, §2.19).

**2.13.1 Iniciativa — Prontidão Primeiro (Initiative — Readiness First)**

Todas as ordens de movimento entram num único conjunto de movimento. O movimento é resolvido em **rondas**: cada exército do conjunto avança **um hexágono por ronda**, e a ronda seguinte só começa depois de todos os exércitos ativos terem dado o seu salto. A ordem dentro de cada ronda segue o **ESTADO atual do exército** (o mais alto primeiro, reavaliado a cada ronda — marchar faz o exército descer na fila), com sorteio aleatório apenas entre iguais (§5.10). A prontidão compra ritmo: os descansados atacam primeiro, e um exército exausto encontra o campo de batalha já mudado quando chega a sua vez. Um exército sai do conjunto quando completa o seu percurso, fica sem pontos de movimento, é bloqueado, é travado por uma batalha ou toma de assalto um povoado. **Um exército bloqueado pára durante o turno** — não volta a tentar em rondas posteriores, mesmo que o bloqueador se afaste. Dois exércitos que se movem ambos neste turno só se encontram, portanto, **se os seus percursos disputarem o mesmo hexágono na mesma ronda**: um exército que sai de um hexágono na ronda 1 não está lá quando chegas na ronda 2 — não há interceção por adjacência nem zona de controlo, por desenho. Apanhas um exército prevendo o seu **destino**, ou atacando o que ele tem de defender; nunca perseguindo o último hexágono onde foi visto, que está sempre um turno desatualizado no teu relatório de nevoeiro. A fase de cerco/assalto pré-movimento e o movimento de frotas (§2.14.1) usam esta mesma regra de ordenação por ESTADO primeiro.

**2.13.2 Regras de Movimento**

Os jogadores submetem um caminho (uma lista ordenada de coordenadas de hexágonos **adjacentes**). O exército (army) avança **um hexágono (hex) por ronda de movimento** (§2.13.1), gastando **pontos de movimento (MP)** por hexágono consoante o terreno (terrain). O movimento pára se o exército for travado por combate, for destruído, ficar sem MP, encontrar a zona de aproximação exterior de um hexágono fortificado já no seu limite (§5.8.0), ou concluir o seu caminho.

O orçamento de MP de um exército é **60** a pé (qualquer unidade não montada na pilha) ou **90** quando todas as unidades são montadas. **Um comboio de cerco arrasta-se**: um exército que transporte máquinas de cerco — ou que lidere um grupo LINK em que qualquer membro as transporte — marcha no máximo **um hexágono por turno (turn)**, e abandona as suas máquinas numa retirada (retreat) (§5.8.6). Esse orçamento é **reverificado em cada hexágono face à composição atual do exército e só pode diminuir à medida que a marcha prossegue** — uma perda que atrase o exército (a queda da sua última unidade montada numa batalha travada a meio da marcha, por exemplo) produz efeito imediato, no salto seguinte; o orçamento também nunca sobe a meio da marcha, mesmo quando o membro mais lento de um grupo ligado é destruído e a sua remoção faria subir o mínimo do grupo. O custo por hexágono depende do terreno e da raça (as planícies são as mais baratas; as montanhas, o pântano e o deserto são os mais caros; os Anões atravessam colinas/montanhas a baixo custo, os Elfos as florestas, os Orcs o pântano, os Nómadas o deserto). Um caminho pode encadear **qualquer sequência de hexágonos adjacentes até ao orçamento de MP — incluindo recuar ou revisitar um hexágono** (por exemplo A→B→A "para cima e para baixo" entre dois hexágonos de planície gasta 60 MP). As únicas restrições são a adjacência, o orçamento de MP e a proibição de hexágonos de mar (embarcar primeiro). Marchar para uma construção (construction) estrangeira com muralhas é permitido — é um **assalto (assault) precipitado** nesse turno (§5.8.0), que declara guerra (war) a todos os reinos lá dentro, incluindo o teu próprio aliado (§5.6), e toma de assalto quem quer que detenha as muralhas, mesmo que as tenha tomado mais cedo na mesma fase (§2.13.6b). Na Página do Jogador (Player Page) a rota de ida é desenhada a dourado e qualquer **troço repetido (de regresso) é deslocado para o lado a ciano**, para que ambos os troços fiquem visíveis. Podes **planear um salto para um hexágono em nevoeiro (terreno desconhecido)** enquanto ainda tiveres pontos de movimento: o painel mostra-o como ❔ Desconhecido (nevoeiro) com o preço do mínimo otimista (≥30mp) e um aviso ⚠, porque o custo real está oculto. O Processador de Turnos (Turn Processor) resolve então o movimento no terreno **real** e pára o exército onde já não puder prosseguir — um salto em nevoeiro pode não se concluir se o hexágono oculto custar mais MP do que os que te restam ou for mar aberto (os exércitos não podem entrar); se o hexágono oculto se revelar uma construção estrangeira com muralhas, o exército entra e desencadeia um **assalto precipitado** às suas muralhas (§5.8.0). Nunca pode levar o exército além do seu verdadeiro orçamento de MP.

\**Uma marcha que* começa *em terreno hostil luta primeiro pelo seu próprio acampamento — o hexágono de origem é reivindicado (disputado em terreno aberto — as muralhas nunca são tomadas de assalto por um exército que parte) antes do primeiro salto. Regras completas e um exemplo prático em §2.13.2b*\*.

**Custo de MP por hexágono, por raça e terreno** (a tabela exata que o jogo usa — descontos raciais no terreno natal a **negrito**; os Aesir não têm deliberadamente NENHUM desconto em terra — a sua mobilidade é a frota):

|             |                                      |               |         |         |           |           |           |
|-------------|--------------------------------------|---------------|---------|---------|-----------|-----------|-----------|
| **Terreno** | **Imperial**                         | **Bárbaro**   | **Elfo** | **Orc** | **Anão**  | **Aesir** | **Nómada** |
| Planície    | 30                                   | 30            | 30      | 30      | 30        | 30        | 30        |
| Colinas     | 45                                   | 45            | 45      | 45      | **30**    | 45        | 45        |
| Floresta    | 45                                   | 45            | **30**  | 45      | 60        | 45        | 45        |
| Montanha    | 60                                   | 60            | 60      | 60      | **30**    | 60        | 60        |
| Pântano     | 60                                   | 60            | 60      | **30**  | 60        | 60        | 60        |
| Deserto     | 60                                   | 60            | 60      | 60      | 60        | 60        | **30**    |
| Mar         | — os exércitos não podem entrar (embarcar primeiro) |               |         |         |           |           |           |

A pé (60 MP): dois hexágonos de planície por turno, um de montanha; um Anão faz dois hexágonos de montanha onde todos os outros fazem um. Montado (90 MP): três hexágonos de planície. Não há terreno mais barato do que 30 — o desconto de uma raça baixa o seu terreno natal até ao preço da planície, nunca abaixo. (Cada hexágono em que se entra custa também ESTADO (readiness) consoante a raça e o terreno, §5.10.3.)

As **frotas (fleets)** movem-se em hexágonos de **mar** (e para portos (ports) — qualquer porto, seja quem for o dono, §2.14.2) a um custo fixo de **30 MP por hexágono**, mas o orçamento de MP de uma frota é o **mp do seu navio mais lento** — um comboio é ritmado pela sua embarcação mais pesada: **60 MP → 2 hexágonos**, **90 MP → 3 hexágonos**, **120 MP → 4 hexágonos** (o mp por casco (hull) vem listado no Ship Roster de cada raça, Parte IV). Esse orçamento também é **reverificado em cada hexágono face aos cascos atuais da frota e só pode diminuir a meio da viagem** — capturar um casco de presa (prize) mais lento a meio da batalha atrasa o comboio ao ritmo da presa a partir desse hexágono (um cartão honesto explica o abrandamento), mas perder um casco lento nunca volta a acelerar uma viagem já em curso. Uma frota mista move-se, portanto, ao ritmo do seu casco mais lento, e transportar um exército não a atrasa. As frotas podem igualmente revisitar hexágonos / navegar para trás e para a frente dentro desse orçamento, com a mesma exibição de caminho dourado na ida / ciano no regresso. *(Orcs e Anões não têm frotas. O escalão de 120 MP pertence unicamente ao Snekkja dos Aesir, §4.7 — uma frota só de Snekkja é a coisa mais rápida que flutua.)*

Os exércitos embarcados (transportados por frota) não se movem na Fase 5.

**A tua própria rota.** Um exército que marcha através de dois ou mais hexágonos é informado de todos os hexágonos em que entrou, por ordem. Uma marcha que termina sem oposição em terreno próprio ou de um aliado recebe o seu cartão *marched to* com a rota — *Army I marched to (2,2) · route (3,2) → (2,2) · 2 hop(s) · plains*. Uma marcha que termina de qualquer outra forma — uma batalha, uma conquista, um assalto a muralhas, um bloqueio — leva a rota no cartão que lhe pôs fim: *Conquered (2,2) — plains · No resistance · Army I route (3,2) → (2,2)*. Uma retirada não faz parte da rota (o cartão da batalha diz para onde o exército recuou). Uma marcha de um só salto não leva rota: o cartão já nomeia o hexágono.

**Avistamentos de rota.** Quando um dos teus exércitos **entra** num hexágono onde já se encontra um exército estrangeiro — ou onde há uma frota atracada no porto desse hexágono — ambos os lados são informados, mesmo que as duas forças terminem o turno fora da vista uma da outra. Um exército só de máquinas de cerco, sem soldados (soldiers), não encontra nada e não é encontrado. Ficas a saber o reino, o número do exército ou da frota e a sua dimensão (cascos exatamente, soldados arredondados às 10 unidades mais próximas, nunca menos de 10; um aliado, suserano ou vassalo (vassal) mostra também o seu retrato completo). A frota de um amigo (aliado, suserano ou vassalo) nomeia também o exército que transporta como carga; o que uma frota estrangeira transporta permanece oculto (§2.14.2). A força em que entraste fica a saber de onde vieste e, enquanto ainda lá estiver, a ronda em que partiste e o hexágono para onde passaste — não é informada se foste mais longe (se esse foi o teu último passo, é onde paraste). Só conta o **mesmo hexágono**: marchar ao lado de uma força num hexágono vizinho não reporta nada, e as forças que lutam contigo aí são cobertas pelo cartão da batalha. Num hexágono com muralhas, quando as duas estão em lados opostos das muralhas — uma dentro, outra acampada fora — essa linha di-lo em vez disso (*No contact — … is outside the walls, your Army N inside*): é essa, e não uma passagem, a razão de ninguém ter lutado. Estar no teu hexágono de partida não é um encontro; voltar a entrar nele mais tarde no turno é. Uma troca frontal — dois exércitos a trocar de hexágonos na mesma ronda — é um só encontro. Cada força recebe um cartão — *Army N crossed paths on its march* para o exército que se moveu, *Foreign forces passed Army N at (c,r)* para o exército em que se entrou; quando ambas ainda estão no hexágono no fim do turno, os títulos di-lo em vez disso (*Army N marched in beside foreign forces* / *Foreign forces camped beside Army N at (c,r)*) e a última linha do cartão diz que o visitante *remains on the hex* (quando o visitante é um exército aliado já registado num cartão como a passar pelas tuas terras, a linha junta-se a esse cartão) — e os mapas (maps) marcam o hexágono do encontro com um anel tracejado na cor do outro reino, rotulado com a ronda (**R1**, **R2**…), a menos que esse reino já mostre aí um marcador do mesmo tipo (frota ou exército) no fim do turno. Os encontros são reportados apenas para esse turno.

**Batalhas testemunhadas.** Se se travar uma batalha (battle) num hexágono onde está o teu exército, nenhum exército teu luta nela, e o teu reino for amigo (aliado, suserano ou vassalo) de qualquer dos lados, recebes o cartão da batalha como observador — *Battle beside your Army N at (c,r)* — com o painel de combate completo, quem venceu, e se o teu exército estava dentro das muralhas. O teu exército não perde nada e não começa nenhuma guerra.

> ***▶ Exemplo — a batalha que não travaste.** A floresta com muralhas de Hyperborea em (24,34) tem dois exércitos: o **Army II** da própria Hyperborea numa **Emboscada (Ambush)** válida — pelo que está **fora** das muralhas, escondido — e o **Army VI** (**Guarnição (Garrison)**, 10 soldados) do seu aliado Nemedia **dentro** — só uma Guarnição fica dentro (§5.8.0). Aquilonia, em guerra com ambos, marcha para dentro com 120. O atacante encontra primeiro o emboscado a céu aberto (§5.8.0 Caso D) e vence-o; tendo vencido às portas, **toma de assalto as muralhas no mesmo turno**.*
>
> *\| Quem \| O que faz \| O que diz o seu relatório \|*
>
> *\|---\|---\|---\|*
>
> *\| Hyperborea II \| Luta (e perde) em Emboscada ×1.40. Derrotado fora das suas muralhas, vai **para dentro, em Guarnição** (§5.8.0), e defende o assalto que se segue. A partir deste turno todos os mapas estrangeiros o desenham: uma emboscada desencadeada não esconde nada. \| Army II stands outside the walls, o seu cartão de derrota (Beaten outside your walls, your survivors went inside them, into Garrison), depois o cartão do assalto \|*
>
> *\| Nemedia VI \| Não participa na batalha das portas — uma Guarnição nunca sai (§2.13.5). Defende depois o assalto ao lado do II, em Guarnição ×1.30 com as muralhas e a milícia. \| Battle beside your Army VI at (24,34) — Aquilonia vs Hyperborea (cartão de observador com o painel completo: "took no part: it stood inside the walls"), depois o cartão do assalto \|*
>
> *\| Aquilonia VII \| Vence às portas, depois toma de assalto as muralhas contra o II e o VI. Com 120 contra o resto do II e 10 soldados, toma-as: o II e o VI recuam para fora da cidade perdida, e o VII fica dentro em Guarnição como conquistador. \| Cartão de vitória, depois Walls breached, depois o cartão de conquista — por esta ordem (§2.13.4) \|*
>
> *Se o VI de Nemedia estivesse em **Defensiva (Defensive)**, ficaria **fora** ao lado do II e travaria com ele a batalha das portas a ×1.20; derrotados, ambos iriam para dentro defender o assalto. Se Aquilonia tivesse **perdido** às portas, teria recuado e nunca chegaria às muralhas.*

**2.13.2b Reivindicar o Terreno Onde Estás**

Como é que um exército acaba num terreno cujo dono não é seu amigo? Quase sempre, **a diplomacia mudou debaixo dos seus pés**: estava acampado no hexágono de um aliado mútuo (uma visita legal e totalmente reportada — §2.13.3) e a aliança (alliance) terminou depois, por tua mão ou por mão deles; ou uma vassalagem foi libertada. Seja como for, o exército começa agora o seu turno num terreno onde não tem direito de estar. O terreno onde se encontra é a primeira coisa por que tem de responder.

**A regra.** Uma ordem de movimento cujo exército **começa** em terras de outro reino, quando esse dono **não é um amigo** (não és tu, nem um aliado mútuo, nem o teu suserano, nem o teu vassalo), faz o exército lutar pelo seu hexágono de origem **antes do primeiro salto** — exatamente como se tivesse acabado de marchar para ele. **Paz não é amizade**: um dono meramente neutro desencadeia a reivindicação tal como um inimigo; a reivindicação declara então a própria guerra (abaixo). A natureza selvagem sem dono nunca desencadeia uma reivindicação — só se pode reivindicar terra com dono.

**O que nunca toca:**

- Um exército **estacionário** não reivindica nada. Sem ordem de movimento, sem reivindicação — simplesmente estar em terra estrangeira continua a ser incruento e legal, exatamente como antes. A reivindicação é uma consequência de *escolher agir*, nunca uma penalização ambiente.

- Os exércitos em **postura de Cerco ou Assalto** estão isentos — o seu combate no hexágono já se resolve no passo da postura, antes do movimento.

- Um exército que deixa uma origem **fortificada** (muralhas de pé) **nunca toma de assalto as muralhas contra as quais estava acampado**, em qualquer postura: desengaja-se e simplesmente marcha. Um povoado com muralhas toma-se por postura de Cerco ou Assalto, ou marchando **para dentro** — nunca afastando-se. A partida não declara guerra e a marcha mantém o seu orçamento completo. O registo do GM anota uma linha *Fort Departed*.

- Os exércitos **embarcados** nunca reivindicam (são carga — §2.14).

- O **terreno amigo** (o teu, o de um aliado mútuo, do teu suserano ou do teu vassalo) nunca é reivindicado.

- Os **outros exércitos acampados no mesmo hexágono** (até 3 — §5.11) **não** fazem parte da luta de reivindicação em si — esta disputa a população (as muralhas nunca são reivindicadas por uma partida) — mas, uma vez ganho o terreno, resolvem-se como **espectadores** (§5.5): um acampado hostil retira-se ou, encurralado, faz uma última resistência que pode recuperar o hexágono. Um co-acampado hostil é um problema distinto para uma ordem distinta.

**Em terreno aberto** (sem muralhas — terreno nu ou um escalão de construção sem muralhas), a reivindicação é a disputa normal de apreensão contra a milícia do hexágono (§2.13.4). Um **grupo LINK disputa em conjunto**: conta o WP de todo o grupo, e seguem-se baixas (casualties) de todo o grupo (§5.11). Três desfechos:

- **Ganha** — o hexágono passa para ti com tratamento completo de conquista: cartões de apreensão e de hexágono perdido de ambos os lados, os mortos da milícia deduzidos à população (population) do hexágono, despojos onde se aplicam (§2.13.11), dano de conquista à construção como em qualquer mudança de dono, e baixas proporcionais ao combate na tua força. A marcha prossegue então **com todo o seu orçamento de MP intacto** — e a reivindicação **não cobra entrada em terreno** — o custo de estado da própria batalha (§5.10.4) continua a ser pago, como em qualquer luta: o estado paga os hexágonos em que *entras* (§5.10), e o exército entrou neste há muito tempo.

- **Repelida** — sofres baixas, o hexágono continua do dono, e a luta **consumiu a marcha**: o exército mantém a posição e o seu caminho planeado é cancelado (um cartão "Army Repelled" explica-o).

- **Aniquilada** — como em qualquer apreensão, uma força desesperadamente inferior pode ser destruída por completo pela população.

**Numa construção fortificada** (muralhas de pé — pontos de muralha acima de zero) **não há reivindicação nenhuma**. O exército parte, as muralhas ficam intactas e o caminho ordenado decorre como planeado. Só uma postura de Cerco ou Assalto, ou uma marcha *para dentro* do povoado, alguma vez atacam muralhas.

**A guerra declara-se a si própria.** Reivindicar declara guerra ao dono do hexágono exatamente como marchar para o seu território o faria (§2.13.8), com as mesmas consequências de opinião (opinion) — **e a declaração mantém-se mesmo que a reivindicação seja repelida**: a tentativa é o ato de guerra, não o resultado. Lê com atenção o corolário estratégico: **depois de uma aliança se quebrar, não há maneira discreta de voltar a casa.** Um exército acampado em terra de um ex-aliado não pode escapulir-se — o seu primeiro passo é uma luta pelo seu próprio acampamento, e essa luta começa a guerra. Se pretendes terminar uma aliança (ou suspeitas que o teu anfitrião está prestes a fazê-lo), marcha primeiro com os teus exércitos visitantes para fora das terras dele; a partir do turno em que a aliança morre, cada exército que deixaste para trás é uma reivindicação à espera de acontecer.

**Temporização.** As reivindicações resolvem-se logo no início da Fase 5, antes de qualquer exército em qualquer lugar dar o seu primeiro salto — uma origem reivindicada é terreno assente (ou uma derrota assente) antes de as rondas ordenadas por ESTADO (§2.13.1) começarem.

> ***▶ Exemplo — a aliança quebrada.** No turno passado o teu vizinho pôs fim à vossa aliança. O teu exército de **10 Praetorians (≈1,200 WP)** continua acampado numa das planícies abertas dele, população **600**, e ordenas uma marcha de dois hexágonos para casa. Antes do primeiro salto, a reivindicação dispara: a população apresenta floor(600 × 5%) × 20 = 600 de WP de milícia. A cerca de dois para um, vences decisivamente — o hexágono é **teu**, é declarada guerra, cai uma fração proporcional de Praetorians, e o exército ainda completa **ambos** os hexágonos da sua marcha (a reivindicação não custou MP nem entrada em terreno; o custo de estado da própria batalha, de §5.10.4, é pago, como em qualquer luta). Agora repete com **3 velites (≈129 WP)**: a turba vence — o exército é empurrado de volta para as suas tendas, ferido; o hexágono continua do teu ex-aliado; a marcha é cancelada; e a guerra é **na mesma** declarada, porque a própria tentativa é o ato de guerra. E se o acampamento fosse um dos **povoados com muralhas** deles, nenhuma das disputas se aplica — não haveria reivindicação nenhuma: o exército parte e as muralhas ficam intactas (§2.13.2b).*

**2.13.3 Empilhamento e Bloqueio (Stacking and Blocking)**

Cada hexágono (hex) comporta no máximo **3 exércitos** (por zona num hexágono com muralhas), e todos os exércitos contam, seja qual for a sua bandeira — exceto que **os inimigos não ocupam lugar perante um ataque**: uma marcha sobre um exército em guerra com o atacante combate-o em vez de parar com *hex full* (§5.11). O que acontece quando um exército entra num hexágono ocupado depende de QUEM o detém e de ONDE:

**Quem é combatido quando vários exércitos partilham o hexágono.** Em terreno próprio ou de um aliado, uma marcha ou um desembarque (landing) combate o exército com o qual estás **em guerra**, mesmo que um exército amigo esteja ao lado dele — um amigo no hexágono nunca esconde um intruso, e o intruso nunca ocupa lugar contra ti: combates com ele em vez de parar com *hex full*. Entre vários exércitos do mesmo estatuto — dois em guerra contigo, por exemplo — é combatido aquele cujo id de reino é o mais baixo, nunca aquele cujo ficheiro de ordens calhou ser lido primeiro.

- **O teu próprio exército ou um exército genuinamente amigo** (aliado mútuo, vassalo, suserano) em **terreno teu ou aliado** → **coabitas** (co-locate): o exército entra a par deles, até 3 exércitos no hexágono. Um hexágono **cheio** (já com 3) detém a marcha com um aviso 🚧 — um exército em paz contigo que lá esteja ocupa um lugar como qualquer outro, e um grupo de ligação (link group) que não caiba **inteiro** pára inteiro, sem deixar ninguém para trás. Se um membro do teu grupo que chega aí estiver em guerra com um exército já presente no hexágono, **ataca à chegada** (§2.13.5). **A coabitação exige que já tenhas um exército teu nesse hexágono:** sem nenhum teu lá, um exército em terreno teu (ou do teu aliado) que **não** seja teu aliado, vassalo ou suserano é combatido — em paz ou não — como abaixo, e é declarada guerra ao seu reino; a nota de movimento da Página do Jogador di-lo. **As muralhas mudam uma coisa:** num hexágono *fortificado* teu ou de um aliado, um exército **em guerra contigo** acampado fora das muralhas é combatido à chegada **quer o teu exército já ocupe as muralhas ou não**. Uma marcha para casa chega sempre **fora** (§5.8.0): o combate é a mesma batalha de campo descrita abaixo (tu atacas, sem postura, sem muralhas), os teus exércitos que já estão fora juntam-se-lhe nos termos do §2.13.5, e uma Guarnição (Garrison) lá dentro nunca se junta. Um acampado em *paz* contigo fora das tuas muralhas continua a ser ultrapassado quando o teu exército está dentro. Se o reforço **vencer**, fica no hexágono **fora** das suas muralhas (ou das do seu aliado), sem postura em vigor; uma ordem de **Garrison** leva-o para dentro a partir do turno seguinte, desde que haja lugar lá dentro (3) e nenhum exército em guerra com ele esteja acampado fora. Um reforço que perca ou empate recua como qualquer atacante em campo aberto — nunca para dentro da cidade. A nota de movimento da Página do Jogador indica o exército que vais combater.

- **Um exército amigo em terreno inimigo ou neutro** → não protege esse terreno de ti: se o hexágono tiver lugar para o teu exército — e para todo o seu grupo de ligação — **entras como se o amigo não estivesse lá**: o hexágono é disputado ou tomado ao seu dono, e o teu amigo é um espectador que fica ao teu lado (dá lugar se o hexágono ficasse sobrelotado). Nunca combates um aliado. Só um hexágono sem lugar para o teu **grupo inteiro** bloqueia a marcha — um exército aliado já lá presente faz recuar um grupo de 3 exércitos — com aviso do limite. Num hexágono estrangeiro com muralhas, um amigo teu **lá dentro** não é escudo: marchar para assaltar as muralhas declara guerra a todos os reinos lá dentro, incluindo o teu amigo, e a aliança quebra-se (§5.6). **Num hexágono estrangeiro com muralhas, qualquer exército acampado fora das muralhas que não seja teu aliado mútuo, vassalo ou suserano é combatido — em guerra ou em paz — e um amigo acampado ao lado dele não o protege: a tua marcha só é repelida por esse terreno quando todos os exércitos de fora são amigos teus.** Qual de vários acampamentos exteriores encontras não depende da ordem em que as ordens do turno foram lidas: primeiro um exército em guerra contigo, depois qualquer outro exército que não seja amigo, depois um amigo, e os reinos desempatam pelo seu lugar na lista. Um exército sem soldados não é ninguém — nem protege o terreno nem é combatido por ele.

- **Qualquer outro exército** (inimigo declarado ou terceiro neutro) → **batalha de campo** (field battle) (após uma **vitória clara** — o defensor destruído ou expulso — **a marcha continua os saltos restantes**; um empate ou uma derrota termina-a, e o atacante recua, §5.5), e **é declarada guerra ao reino do ocupante** — além da do dono do hexágono, quando entras em terras de alguém. Combater o exército de um reino neutro é, em si, um ato de guerra. Se vários exércitos ocupam o hexágono, defendem-se em conjunto como estabelece o §5.11. *Porque é que terra e mar diferem aqui:* a terra tem território e o mar não — no mar uma frota neutra apenas ocupa um ancoradouro (§2.14.2), mas em terra caminhar sobre um exército neutro, ou sobre terreno neutro, é sempre um ato de guerra — muralhas sem dono contam aqui como terreno aberto; muralhas com dono são assaltadas (§5.6). Se tomares um hexágono que o exército de um terceiro reino guardava para o seu dono, o **dono** recebe o aviso da perda, com o nome do exército que o guardava — ou, quando não foi preciso batalha, do amigo teu que ficou a assistir; o exército desse amigo fica (ou dá lugar) e também recebe aviso. Um hexágono sem dono não tem a quem avisar: ninguém é informado de que foi perdido — nem o exército que o guardava — e o aviso do conquistador diz *"No banner flew here; up goes yours…"*.

Em hexágono **teu** ou **de um aliado** a intervenção nunca muda a propriedade — estás a recuperar terreno próprio ou a libertar terra aliada.

**Vês o que acontece na tua terra.** Os movimentos aliados pelo teu território são-te comunicados por inteiro: um exército aliado que **termina o turno** no teu hexágono produz um aviso com o nome do seu comandante, a composição completa, o número de efetivos e o poder de guerra (os aliados não escondem nada uns dos outros — o ESTADO (readiness) não é partilhado); um que apenas **passa** produz um único aviso com a lista dos hexágonos atravessados, com o mesmo detalhe. Se se travar uma batalha **no teu hexágono** em que não participaste — o teu aliado contra um intruso, ou dois exércitos a combater às tuas muralhas ou por um cerco a um teu povoado — recebes o relatório completo da batalha — vitória, derrota ou empate — desenhado *Atacante \| Defensor* com o vencedor nomeado, já que não combateste em nenhuma das colunas — exceto um assalto às tuas muralhas detidas ou tomadas pela guarnição de um aliado, que continua a ser desenhado do teu lado (uma libertação perdida significa que o inimigo ainda acampa na tua terra, o que queres muito saber). Uma marcha aliada para o teu hexágono ocupado **junta-se** ao teu exército aí (coabitação, §5.11) em vez de ser bloqueada — só um hexágono cheio (3 exércitos) faz recuar o visitante, e esse aviso vai para o visitante detido. O mesmo vale no mar, e no teu próprio porto vai-se mais longe: ver *What the port's owner sees* (§2.14.2). Os exércitos inimigos não te concedem nada disto — apenas avistamentos pelo nevoeiro de guerra.

**2.13.4 Tomada de Hexágonos Indefesos (Seizing Undefended Hexes)**

Quando um exército entra num hexágono estrangeiro sem exército defensor, a **população local resiste como milícia (militia)** — uma força defensora no valor de floor(população × 5%) × 20 WP (≈ a própria população; a mesma milícia que defende um povoado cercado, §5.6). Tomar o hexágono é uma **disputa de WP ao estilo de campo aberto** contra essa milícia:

- **Não se aplica nenhuma fortaleza nem bónus de terreno/casa** (é terreno aberto, não um assalto a muralhas), e o atacante não sofre penalização de muralhas. O atacante mantém os multiplicadores de **iniciativa** (1.05–1.10), de **comandante** (1 + Militar/1000) e de **ESTADO**; a milícia apenas rola a variância de ±10%.

- Vence **decisivamente** (o teu lançamento de batalha \> 1.2× o da milícia) → **reclamas o hexágono**, sofrendo **baixas proporcionais ao combate** (uma vitória esmagadora custa pouco; um combate renhido custa mais).

- Um **empate ou uma derrota** → és **repelido**; o hexágono não é tomado. A disputa com a população usa a **mesma curva suave de uma batalha de campo**, incluindo a rampa de probabilidades extremas e a dissolução da armadura (§5.5.3): abaixo da rampa, uma força muito inferior perde até **60%** (o limite aplica-se a partir de 5:1 e mantém-se constante até 13:1) e recua graças à sua armadura; além de 13:1 o limite e a armadura cedem em conjunto, e uma força que marche sobre uma população **25 vezes o seu peso é destruída até ao último homem**. Não existe rácio em que uma companhia bem equipada saia ilesa de um assalto desesperado a uma cidade.

- **Hexágonos neutros/não reclamados** defendem-se com a população que a sua construção contiver. Um hexágono neutro **sem** construção não tem população, não recruta **qualquer milícia**, e é tomado sem oposição — terreno vazio está genuinamente vazio (§3.7); só um mapa antigo, anterior às construções, recorre à população base do terreno.

Como a defesa é **WP, não número de efetivos**, precisas de um exército cujo poder de guerra exceda aproximadamente a população, e a **qualidade conta** — uma pequena força de elite toma terreno que uma horda de fracos não consegue, e uma unidade isolada é simplesmente rechaçada.

A **milícia é recrutada à população, e os seus caídos são removidos permanentemente da população do hexágono** — proporcionalmente à batalha (a mesma divisão de baixas de um combate em campo): uma repulsa esmagadora custa à população apenas um punhado, enquanto ser subjugada (o hexágono cai) mata a maior parte do recrutamento. Assim, um hexágono defendido *desgasta-se* sob ataques repetidos, e um conquistador herda um hexágono **depauperado pela milícia que acabou de destruir** — a população não é uma defesa inesgotável e gratuita. O local de produção (site) e o povoado perdem cada um um nível na tomada (§5.6.3). (Isto aplica-se igualmente a desembarques em praia e a **assaltos** (assaults), §5.6 — um povoado assaltado ou que repele o ataque perde a milícia que levantou. Um hexágono sem construção não tem população a recrutar nem a deduzir à partida.)

**O povoado vai com o hexágono.** Uma construção num hexágono que tomas fica nele e passa a ser tua, com o seu povo. Um **povoado aberto** — um nível cuja muralha é 0 (§3.7.1a: um acampamento Nómada de Nível 1, os primeiros níveis Genérico e Orc) — não tem muralhas para segurar: a sua milícia combate como a de qualquer hexágono indefeso e, quando cai, o povoado cai com ela; um **muralhado** só é tomado por assalto ou cerco (siege) (§5.8.0). Em ambos os casos o povoado e o seu local de produção perdem cada um um nível na captura (§5.6.3). Ambos os relatórios nomeiam o povoado que mudou de mãos.

> ***▶ Exemplo.** Um velite isolado (43 WP) marcha sobre um hexágono de planície com 1,000 de população: a população apresenta floor(1,000 × 0.05) × 20 = 1,000 WP de milícia. A ~23:1 contra, a rampa está em vigor: a perda lê-se ~93% com a armadura quase dissolvida — um homem sozinho arredonda para a morte mais vezes do que não, e além de 25:1 morre com certeza. Abaixo da rampa uma repulsa custa no máximo **60%**; uma força repelida fica no hexágono de onde veio e é **destruída apenas se a disputa não lhe deixar soldados** — a disputa com a milícia nunca procura um hexágono de retirada; também não concede experiência, não rola morte de comandante e não aplica escala de terreno de cavalaria. Um hexágono **sem população nenhuma** é simplesmente tomado — não há ninguém para combater. Uma planície base (200 pop → 200 WP de milícia) precisa de cerca de **240+ WP** em bruto (um pouco menos com uma iniciativa média e um comandante) para ser tomada — cerca de 6 velites ou 2 Praetorians; uma planície desenvolvida (2,000 pop → 2,000 WP) precisa de ~2,400 WP. Terra povoada só cai perante um exército a sério, e a tua força sangra (proporcionalmente) por cada hexágono que conquista.*

**O que cada lado é informado.**

- **O atacante** recebe um aviso de tomada (com baixas) ou um aviso de **"Army Repelled"** em cada repulsa — diz "no survivors" apenas quando a força foi aniquilada na disputa.

- **O dono do hexágono** recebe um aviso de **hexágono perdido** ou, quando a sua população resiste, um aviso de **"Invasion Repelled"**. Sempre que a milícia combate — tomada, desembarque em praia ou assalto — o aviso **comunica as perdas da própria milícia** ("your militia lost N"). Um aviso de hexágono perdido credita a milícia (os seus WP defensivos, as suas perdas, os invasores que matou) e indica o **tamanho da força invasora** — as tropas que marcharam ou desembarcaram.

- **O aviso reflete fielmente como o hexágono caiu:** uma **entrada sem sangue** ("strolled in while nobody was guarding it" — ou "took this hex while X's army — a friend of Y's, camped there — stood by"), um combate com a **milícia** ("trampled past your militia") ou um **assalto** ("stormed the walls by force of arms"; a linha de efeito diz *Taken by force of arms — N troops lost (see the battle card)*).

- **A conquista vem depois da sua batalha.** Quando as muralhas mudam de mãos num assalto ganho ou num desembarque vitorioso, os avisos *Conquered* e *Lost* seguem os avisos dessa batalha no relatório — nunca antes deles.

**O quanto sabes sobre o invasor** depende do que se lhe opôs:

- **Um exército real** combateu-o → o relatório completo da batalha, todos os tipos de unidade da composição do inimigo.

- **Apenas a milícia**, ou muralhas perdidas num **cerco** (§2.7) → o seu tamanho **e o seu equilíbrio entre cavalaria e infantaria**.

- **Nada de nada** → apenas o número de efetivos.

Os três chegam **depois** de o hexágono estar perdido. Um espião (§8.8) é a única informação sobre um exército que *ainda não* combateste — uma estimativa, mas a única que chega a tempo de agir.

**2.13.5 Gatilho de Batalha de Campo (Field Battle Trigger)**

Dois exércitos em guerra no mesmo hexágono resolvem uma batalha de campo. O exército que se move é o atacante; o exército estacionário é o defensor.

**Um exército ou frota já presente no hexágono que atacas junta-se a esse ataque**: quando o teu exército ataca um inimigo num hexágono — marchando sobre ele, chegando ao lado dele ou desembarcando nele — todos os teus exércitos já presentes na mesma zona combatem do teu lado, e também um exército do teu aliado, vassalo ou suserano que esteja **já em guerra com todos os reinos do lado defensor**; os membros de um líder de ligação (link leader) entre eles também vêm. Partilham o resultado: cada um sofre as suas próprias baixas e ganha a sua própria experiência, e numa derrota ou empate cada um recua — ou o seu grupo dispersa-se — exatamente como o teu exército atacante. **Juntar-se nunca inicia uma guerra**: um exército aliado em paz com qualquer reino do lado defensor fica de fora, e o mesmo vale para um exército que já tenha combatido no mesmo passo. Dentro contra fora uma muralha nunca se junta. As frotas fazem o mesmo no mar (§2.14.7).

**Uma Guarnição (Garrison) nunca se junta.** Um exército em Garrison dentro de muralhas nunca é chamado ao ataque de um amigo — as muralhas são o seu posto; só um exército cercado que ordene Sally (Surtida) sai (§5.8.0, §2.13.7). O aviso de batalha do exército que se junta abre com o motivo por que combateu: *"Your Army II was on the hex and joined Army I's attack."* — ou, para um aliado, *"Your Army I was on the hex and joined Aldoria's attack."*

Em **terreno estrangeiro ou sem dono** a tua marcha ataca qualquer exército nessa zona que não seja teu aliado, vassalo ou suserano — também um em paz contigo, ao qual declara guerra — e os teus exércitos aí juntam-se a esse ataque. **Em terreno teu ou aliado, um exército pacífico ao lado do teu exército não é atacado**: a tua marcha simplesmente junta-se ao teu exército aí. A pré-visualização de movimento da Página do Jogador indica quando os teus exércitos se juntarão, contando os exércitos que lá estão agora; um com uma marcha própria em fila para fora só se junta se ainda lá estiver quando o ataque chegar (os exércitos movem-se por ordem de prontidão). Um desembarque em praia a que se juntam exércitos já em terra é uma só batalha: os exércitos que se juntaram a partir da costa recuam por terra se falhar, nunca de volta a bordo, e o aviso do desembarque diz para onde foi cada um — *"Your Army II, which had joined from the shore, fell back overland to (3,2)."* — enquanto o defensor da praia lê cada reino atacante pelo nome, cada exército sob o seu próprio reino.

**Exércitos já em guerra que começam a Fase 5 acampados na mesma zona de um hexágono combatem antes de alguém marchar — o varrimento de acampamento (camp sweep)** (o gémeo terrestre do varrimento de coabitação naval, §2.14.2): uma guerra declarada no turno anterior entre exércitos acampados juntos, uma iniciada neste turno na Fase 1 (uma ligação de bloqueio, uma vassalagem terminada em guerra), ou um exército encurralado que não pôde retirar-se. O dono do terreno — ou um amigo seu — defende; em terreno de qualquer outro, defende o id de reino mais baixo. O lado atacante é todo o exército aí em guerra com o defensor que seja do próprio atacante ou amigo dele, mais os membros de qualquer líder de ligação entre eles; a defesa reúne-se como em qualquer batalha (§5.11). **Nenhum hexágono muda de mãos**, a **Emboscada (Ambush) não dá bónus** (ninguém marchou para ela) — **exceto em terreno fortificado a que és amigo** (o teu, o de um aliado mútuo, de um vassalo ou de um suserano), onde o emboscador já está fora das muralhas de propósito e mantém o seu ×1.40 (§5.4, §5.8.0), a Defensiva (Defensive) e a Guarnição contam como de costume; o perdedor retira-se — exceto um exército **cercado**, que permanece dentro das suas muralhas numa derrota ou empate (§2.13.7), e um exército do dono ou de um amigo derrotado fora das suas próprias muralhas, que vai para dentro em Garrison enquanto houver lugar (§5.8.0); um exército que combateu não descansa nesse turno. Dentro contra fora uma muralha é um cerco, não um choque de acampamento. Os avisos abrem com *"Nobody marched: your armies were already camped on the same ground when the fighting began."*

**Um exército que chega ao lado de um inimigo ataca à chegada.** Quando um passo de marcha termina com um exército — o líder, ou um membro da ligação levado atrás dele ou colocado no hexágono por uma tempestade — na mesma zona de um exército já presente com o qual está em guerra, combatem de imediato, antes de a marcha prosseguir; uma derrota ou empate dispersa todo o grupo de ligação. A regra completa é o choque de chegada (arrival clash) (§5.11); no mar, uma frota levada para o hexágono final da sua nau capitânia faz o mesmo (§2.14.7). Ver a Secção 5.5 para as fórmulas.

**2.13.6 Ordens de Cerco e Assalto (Siege and Assault Orders)**

**Cerco (Siege)**: Um exército com a postura de Siege **parado em** cima de uma construção estrangeira com muralhas (acampado às portas) incrementa em 1 por turno o Progresso de Cerco desse hexágono, desde que cumpra a força mínima de cerco (§5.8.1) — o cerco de um exército sem força suficiente falha sem progresso. O cerco é guardado (§5.4); dar qualquer postura que não Siege nem Assault, ou marchar para longe, termina o cerco no início do processamento (§5.8.5). O Assalto tem de ser ordenado em cada turno.

**Assalto (Assault)**: Um exército com a postura de Assault, acampado SOBRE um hexágono com uma construção estrangeira com muralhas, assalta-a na Pré-Fase 3, depois de primeiro derrotar qualquer exército que esteja fora das muralhas (§5.8.0, Secção 5.6).

**Cada exército numa coligação combate com os seus próprios bónus.** O Poder de Guerra de um lado é a **soma** dos seus exércitos, cada um multiplicado pelo *seu próprio* terreno de casa, escala de cavalaria, postura, estado e comandante — nunca os do grupo (§5.11). Um Elfo e um aliado não Elfo a defenderem juntos numa floresta combatem a ×1.30 e ×1.00, e o resumo do aviso de batalha imprime **"mixed — see below"** sempre que os exércitos de um lado divergem, com a cadeia real de cada exército na discriminação abaixo.

As posturas modificam apenas o lado que está a **DEFENDER** (valores e validade, §5.4): o atacante, incluindo quem faz uma surtida, combate a ×1.00 fosse qual fosse a postura em que estava. Um desembarque em muralhas combate primeiro os exércitos de fora e depois, se vencer, assalta a Guarnição de dentro (§5.8.0, §5.6).

**2.13.6b Dois exércitos, uma construção: o mesmo turno (Two armies, one construction: the same turn)**

Mais do que um exército pode atacar a mesma construção num único turno, e chegam por **ordem de prontidão** (§2.13.1) — uma coluna descansada pode planear chegar primeiro.

- **Ambos são repelidos** → quando o segundo é do mesmo reino do primeiro ou amigo dele, ambos assaltam as muralhas, ambos sofrem baixas, ambos recebem aviso. As muralhas são contabilizadas

para dano de engenhos no máximo uma vez por turno, por muitos sitiadores que levem engenhos (§5.8.6).

- **O primeiro a entrar toma-a** → a construção muda de mãos. Um recém-chegado posterior **não** é afastado:

chega e enfrenta o NOVO detentor, que é agora uma fortaleza hostil como outra qualquer. Uma construção pode, portanto, ser **tomada mais do que uma vez num turno**. O que continua a acontecer só uma vez por turno é o *dano* que uma conquista inflige (§5.6.3) — a segunda captura não degrada a construção outra vez.

- **O primeiro é repelido mas sobrevive** → fica **acampado às portas** (§5.8.0). Um recém-chegado posterior

encontra primeiro esse acampamento, **a céu aberto** — sem muralhas, sem bónus de fortaleza — mesmo quando está apenas em **paz** com o acampado; a guerra começa aí (§2.13.3). Se vencer, e não restar nenhum acampamento hostil fora, **assalta as muralhas no mesmo turno** (§5.8.0); se perder ou empatar, recua para onde começou.

Duas consequências a ter em conta no planeamento:

1\. **Chegar em segundo é muitas vezes melhor.** Se o primeiro atacante for repelido e acampar, o segundo combate um exército ensanguentado a céu aberto, e depois assalta muralhas cujos defensores o primeiro assalto já fez rarear.

2\. **Dois inimigos a sitiar uma fortaleza ajudam sobretudo o defensor.** Desgastam-se mutuamente às portas enquanto as muralhas se mantêm. Em testes, uma guarnição que repeliu dois assaltos distintos de 30 efetivos cada perdeu uma ou duas milícias a fazê-lo.

Isto aplica-se a um exército já acampado às portas em postura de **Siege ou Assault** (§2.13.6) exatamente como a uma marcha de entrada: uma construção que mudou de mãos mais cedo no mesmo turno é simplesmente uma fortaleza hostil sob nova gerência, e o sitiador prossegue.

Há um caso em que uma ordem de postura de facto se desfaz: se a construção passou a ser **tua ou de um aliado** — porque então já não estás parado numa fortaleza estrangeira. Essa desistência recebe aviso, e é a única razão por que uma ordem de cerco ou assalto caduca para um hexágono que mudou de mãos.

**2.13.7 Exércitos Cercados (Besieged) e a Surtida (Sally)**

**Quem está cercado.** Quando a Pré-Fase 3 (Pre-Phase 3) abre, um exército (army) está **cercado** se se encontrar **dentro** de muralhas (walls) — em Guarnição (Garrison), a única postura (stance) possível atrás delas (§5.8.0) — que um reino **em guerra** com ele esteja a cercar — o hexágono tem o cerco (siege) desse reino e um dos seus exércitos com soldados ainda está às portas **e pressiona-o neste turno** (Cerco ou Assalto, ou o seu reino falhou o turno); a tua Página do Jogador não consegue ver as ordens do sitiante e assume que sim. Todos os reinos lá dentro contam (o dono, um aliado, um vassalo — cercar as muralhas torna-os todos inimigos do sitiante, §5.6). **Quando começa.** O anel (o cerco do hexágono) é lançado ou por uma **Marcha de Cerco** (Siege March) que passa o teste de força do §5.8.1 à chegada (§5.8.0), ou pelo primeiro **tique de cerco** do sitiante, que corre na Pré-Fase 3 *depois* desta verificação. Seja como for, os exércitos lá dentro ficam cercados a partir do turno **seguinte** àquele em que o anel é lançado: uma Marcha de Cerco que o fecha à chegada no turno T, ou um exército já acampado às portas que ordena Cerco no turno T, cerca a partir de T+1; uma Marcha de Cerco demasiado pequena para o fechar à chegada cerca a partir do turno seguinte ao seu primeiro tique bem-sucedido. Um exército em guerra com o sitiante não pode simplesmente entrar — tem primeiro de vencer o acampamento às portas (§2.13.3). Um **amigo tanto do sitiante como do dono** chega às portas e fica **fora**, como qualquer chegada; se depois ordenar Guarnição entra, o tique de cerco desse turno declara-lhe guerra, e fica cercado a partir do turno seguinte. Qualquer outro exército é enfrentado pelo acampamento à chegada (§2.13.3). Um exército **recrutado** dentro de uma cidade cercada fica cercado de imediato.

**Onde, e durante quanto tempo.** A zona é lida tal como estava no **início** do turno: um exército que o começou fora das muralhas — qualquer exército que não esteja em Guarnição — não está cercado nesse turno, e ordenar Emboscada (Ambush) neste turno não faz um exército cercado passar para fora. Um exército a bordo de uma frota nunca está cercado. **Uma vez cercado, permanece cercado enquanto esse anel se mantiver**: terminar a aliança com o dono das muralhas não o põe fora, e a paz com o sitiante não o liberta — de qualquer modo, o tique de cerco seguinte declara de novo guerra a todos os reinos lá dentro (§5.6). Só o fim do anel o liberta: uma Surtida vitoriosa, uma força de socorro que bata o sitiante, o sitiante ter partido ou deixado de pressionar, a paz entre o sitiante e o dono, ou a queda.

**O que um exército cercado pode fazer:**

- **Guarnição ou Surtida — nada mais.** Qualquer outra postura que mantenha ou ordene (Em Movimento, Defensiva, Marcha de Cerco, Emboscada) é lida como **Guarnição** enquanto o cerco se mantiver, e guardada como Guarnição.

- **Sem marcha.** Uma ordem de marcha é recusada, e o relatório di-lo (*Army N besieged — march refused*). As únicas formas de sair são **quebrar o cerco** — vencer uma Surtida, ou um exército de socorro vindo de fora bater o sitiante — e marchar no turno seguinte, ou **embarcar** — um embarque em porto só num porto que possuas, ou uma recolha em praia a partir da tua própria frota na água ao lado (§2.14.5); o mar permanece aberto. Uma frota que o tenha recebido a bordo no porto pode até desembarcá-lo no turno seguinte num hexágono de terra **junto ao** porto sem sair para o mar — o porto é uma porta, sejam quais forem os bloqueios na água.

- **A sua ligação a um líder exterior quebra-se.** Um membro cercado de um grupo cujo líder não está cercado abandona o grupo (com cartão) — caso contrário, a marcha do líder levá-lo-ia para fora. **Nem uma ligação leva alguém para dentro:** um exército acampado fora que um líder cercado liga é retirado do grupo (*did not join the besieged group*).

- **Sem transferências através da linha de cerco.** As tropas só passam entre dois dos teus exércitos no hexágono se ambos estiverem cercados ou nenhum estiver: um exército cercado não pode entregar os seus homens a um exército acampado fora para os levar dali, e um acampado fora não pode reforçar a guarnição através do anel (*troops do not cross a siege line*).

- **Uma batalha perdida no seu próprio hexágono deixa-o dentro.** Um exército cercado que perde ou empata uma batalha onde está — contra um inimigo dentro das mesmas muralhas no varrimento de acampamento (§2.13.5), ou numa chegada — recua para trás das suas muralhas em Guarnição, nunca para fora do hexágono — enquanto o anel se mantiver (uma Surtida que venceu neste turno levantou-o, e nesse caso o perdedor retira-se como habitualmente). Não numa Surtida (os seus sobreviventes voltam para dentro de qualquer maneira), e não numa resistência final em muralhas que acabaram de cair.

- **Nunca combate fora das suas muralhas sem ordem** — nem sequer ao lado da marcha de socorro do seu próprio reino para o hexágono (uma Guarnição nunca entra num combate, §2.13.5): só sai ao ordenar Surtida.

> ***▶ Exemplo — a única porta é o mar.** O Exército II da Hyperborea está cercado no seu próprio porto (24,34) e ordena uma marcha para (25,34): recusada — Army II besieged — march refused. A Frota I da Hyperborea está nesse porto, por isso no turno seguinte a Hyperborea ordena a II que **embarque**. O embarque é reaplicado na Pré-Fase 2, antes de alguém ser marcado como cercado, pelo que II fica a bordo, deixa de estar cercado, e a Frota I pode largar nesse mesmo turno. O VI da Nemedia, um aliado lá dentro, não pode embarcar no porto da Hyperborea (um embarque em porto exige um porto teu); a sua porta é uma **recolha em praia** a partir de uma frota nemedia na água ao lado — a frota fica retida nesse turno e larga no seguinte (§2.14.5).*

**A Surtida.** Um exército cercado que ordena **Surtida** sai e combate na **Pré-Fase 3**, antes de o cerco avançar e antes de qualquer Assalto nesse hexágono:

- **Um só lado, quem quer que sejas.** Todos os exércitos cercados no hexágono que ordenam Surtida fazem a surtida **em conjunto**, de qualquer reino, ligados ou não; um líder de ligação que faz a surtida leva consigo os seus membros cercados. Um reino em guerra com um reino que já esteja na surtida é **retido** (com cartão) — um reino nunca combate ao lado do seu inimigo. Quem entra primeiro está fixado, nunca é a ordem em que os ficheiros foram lidos: o **dono** das muralhas, depois os outros reinos por id de reino — a ordem em que entraram na campanha. A ordem de Surtida de um **membro** ligado é ignorada — só sai com o seu líder. Uma Surtida sem ninguém em guerra acampado fora recebe o cartão *no one to sally against* e o exército permanece em Guarnição.

- **Contra todos os que estão fora e em guerra com o reino líder** (o dono, se fizer a surtida): primeiro o sitiante, depois todos os outros exércitos acampados às portas em guerra com ele. Um reino que não esteja em guerra com todos eles é retido — uma surtida nunca inicia uma guerra para os exércitos que a ela se juntam.

- **A céu aberto, como atacante.** Sem bónus de postura, sem bónus de fortaleza, sem milícia — mas um dono Imperial de um povoado FI/POP mantém a sua **Legião** ×1.10 na surtida (§4.2). O sitiante defende a **×1.00** — o ×0.85 do §5.8 aplica-se apenas contra um exército de socorro.

- **Vitória:** os sitiantes derrotados recuam como qualquer exército de campo derrotado — e não pressionam nada onde aterram — **o cerco é levantado** (progresso a 0, ambos os lados com cartão), e os exércitos da surtida ficam dentro em **Guarnição** — livres para marchar no turno seguinte, uma vez desaparecido o anel. Se um exército do reino sitiante ainda estiver às portas (um que a surtida não combateu, ou que manteve a posição), o anel mantém-se e ficam cercados de novo no turno seguinte.

- **Empate:** de volta ao interior em Guarnição. Os sitiantes às portas **não fazem progresso** neste turno e o seu Assalto não toma as muralhas (cada um recebe o cartão *Siege held* / *Assault held*); uma postura de Cerco permanece guardada. Uma nova marcha sobre as muralhas na Fase 5 ainda as toma de assalto.

- **Derrota:** os sobreviventes escapam **de volta para dentro** em Guarnição — as muralhas são o seu refúgio, mesmo quando não há nenhum hexágono exterior livre para onde recuar — e, quando havia um hexágono exterior livre para recuar, lêem *"pulled back inside the walls"* no seu Relatório de Prontidão (sem ele, estão simplesmente de volta ao interior, sem custo de movimento) (§5.10.2). O cerco avança no mesmo turno, e um Assalto ordenado pelo sitiante toma as muralhas de imediato — contra eles, agora em **Guarnição ×1.30**.

- **Apenas um turno.** A Surtida não fica guardada; no turno seguinte o exército mantém Guarnição de novo, a menos que ordene outra.

- O **dono** do povoado é informado de todas as surtidas combatidas às suas portas: se combateu, no seu próprio cartão de batalha; se não tinha nenhum exército no combate, como observador — *Battle on your territory at (c,r)* com o painel de combate completo.

**Surtida e socorro nunca combatem como um só.** Os cercados no interior e um exército de socorro vindo de fora não podem atacar o sitiante em conjunto numa só batalha. A Surtida é combatida na **Pré-Fase 3**; a batalha do socorro vem depois, na **Fase 5** — uma marcha sobre o hexágono, ou o varrimento de acampamento de um exército já acampado às portas (§2.13.5) — ou na **Fase 6** para um desembarque vindo do mar. São duas batalhas, uma após a outra, e o poder de guerra de nenhum dos lados é somado ao do outro. Nem um exército amigo acampado fora das muralhas pode sair com a Surtida — só os exércitos cercados fazem surtidas — e uma Guarnição no interior nunca entra na batalha do socorro. O que a Surtida faz ao sitiante transita: os seus mortos continuam mortos e o seu estado pagou o custo dessa batalha (§5.10.4), pelo que um socorro que chegue no mesmo turno encontra um sitiante mais fraco — e encontra-o a **Cerco ×0.85**, onde a Surtida o encontrou a ×1.00 (§5.8). O que o socorro encontra depende de como correu a Surtida:

- **A Surtida vence** — o anel é quebrado na Pré-Fase 3; o socorro chega a muralhas sem sitiante às portas, a menos que outro exército do reino sitiante ainda lá esteja, e nesse caso combate esse.

- **A Surtida empata** — sem progresso de cerco neste turno e sem assalto dos sitiantes que combateu; o socorro combate-os depois.

- **A Surtida perde** — o cerco avança na Pré-Fase 3, e se esse tique levar o progresso além do limiar **as muralhas caem na Pré-Fase 4 (§5.8.4), antes de o socorro chegar**: a sua marcha aterra então nas muralhas recém-tomadas do seu inimigo, e marchar sobre muralhas é um assalto (§5.8.0). Caso contrário, o socorro combate o sitiante, e um socorro que vença levanta o cerco no turno seguinte, com o progresso de volta a 0.

Daqui decorrem duas coisas. **No turno em que as muralhas cairiam, um socorro chega a tempo apenas se a Surtida pelo menos empatar** — uma Surtida empatada impede o tique desse turno. E **uma Surtida ordenada no turno em que o socorro chega obriga o sitiante a combater duas vezes num só turno**, a segunda vez mais fraco e a ×0.85: os dois golpes não se somam numa só batalha, mas caem no mesmo turno.

> ***▶ Exemplo — depois do cerco.** II venceu a sua Surtida no turno 12. No turno 13, a sua linha de Ordens em vigor diz Army II (18,9) inside the walls · 74% · Garrison (kept from last turn) — order: none. O cerco guardou **Guarnição**, e ela permanece em vigor — ×1.30 contra um assalto, ×1.20 em campo. A Defensiva que mantinha antes do cerco não volta por si: ordena Defensiva, ou uma marcha (que limpa a postura).*

**Se o cerco seguir o seu curso**, as muralhas caem (§2.7) e **todos os exércitos cercados do dono das muralhas rendem-se** — é uma Guarnição. Um exército de um terceiro reino lá dentro — de um aliado — não é a guarnição do dono: é expulso, ou chacinado se não tiver para onde fugir, como diz o §2.7.

**Ninguém faz surtida sem ordem.** Uma Guarnição que **não** esteja cercada — no turno em que chega um inimigo, antes de qualquer cerco — defende as muralhas contra uma marcha, um Assalto ou um desembarque, depois de os exércitos de fora terem sido batidos (§5.8.0). Não há surtida automática em nenhuma via.

> ***▶ Exemplo prático — Nemedia e Hyperborea (turnos 31–35).** A Hyperborea é dona do hexágono amuralhado (24,34); lá dentro estão o Exército II da Hyperborea e o Exército VI da Nemedia, aliados. O Exército VII da Aquilonia, acampado às portas, ordena **Cerco** no turno 31 — o seu primeiro tique lança o anel (progresso 1), e o cerco põe a Aquilonia em guerra com ambos os reinos lá dentro (§5.6).*
>
> *- **Turno 32, Pré-Fase 3.** Ambos os exércitos estão cercados. Qualquer postura que a Nemedia ordene é lida como Guarnição, e a marcha que VI ordenou para fora de (24,34) é recusada (Army VI besieged — march refused) — a mesma marcha que o motor da altura deixou passar no turno 32 real. Se ninguém ordenar Surtida, o cerco avança para 2.*
>
> *- **Turno 33 — a Surtida.** Ambos ordenam **Surtida**. Não estão ligados, e isso não importa: II (o dono, primeiro) e VI saem juntos como um só lado contra VII, a céu aberto, como atacantes. Vitória → VII recua, o anel é quebrado, II e VI ficam dentro em Guarnição e podem marchar no turno 34. Empate → VII não faz progresso neste turno. Derrota → II e VI correm de volta para dentro em Guarnição e o cerco avança.*
>
> *- **Se só a Nemedia ordenar Surtida**, VI sai sozinho; o II da Hyperborea fica dentro em Guarnição.*
>
> *- **Se nunca fizerem surtida**, o progresso chega a 5 no turno 35 e as muralhas caem nessa mesma pré-fase: o II da Hyperborea rende-se com elas, e o VI da Nemedia — um aliado, não a guarnição do dono — é expulso, ou chacinado se encurralado (§2.7). Antes disso, a Nemedia ainda pode retirar VI por uma **recolha em praia** a partir da sua própria frota na água ao lado (§2.14.5) — um embarque em porto no porto da Hyperborea não lhe está aberto.*
>
> ***▶ Exemplo — uma Surtida que vence.** O hexágono amuralhado da Aquilonia (18,9). O Exército III da Cimeria, acampado às portas, ordena Cerco no turno 10 — o primeiro tique lança o anel. A partir do turno 11, o II da Aquilonia lá dentro está cercado. No turno 12, II ordena **Surtida** e, na Pré-Fase 3, ataca III a céu aberto a ×1.00 (sem postura, sem muralhas, sem milícia); III defende a ×1.00. II vence: III recua para um hexágono vizinho e não pressiona nada aí, o cerco é levantado (progresso de volta a 0; a Aquilonia lê Siege at (18,9) broken — the sally won, a Cimeria Siege of (18,9) broken — the garrison sallied and won), e II fica dentro em Guarnição. Uma marcha que II ordene nesse mesmo turno ainda é recusada — estava cercado quando o turno começou — e no turno 13 pode marchar.*
>
> ***▶ Exemplo — uma Surtida empatada.** O mesmo hexágono, mas III é tão forte como II e a batalha é empatada. II está de volta dentro em Guarnição. III recebe o cartão Siege held at (18,9) — a surtida empatou: sem tique neste turno (o progresso fica onde estava), e o seu Cerco permanece guardado para o turno seguinte. Se um segundo exército cimério tivesse marchado sobre as muralhas na Fase 5, ainda as teria tomado de assalto — o empate só retém os sitiantes que já estão às portas.*
>
> ***▶ Exemplo — uma Surtida derrotada, depois assalto.** No turno 12, II ordena Surtida enquanto III ordena **Assalto**. A Surtida é combatida primeiro e perdida: os sobreviventes de II escapam de volta para dentro (pulled back inside the walls) em Guarnição. Depois III ataca — contra II a **Guarnição ×1.30**, com o bónus de fortaleza e a milícia ao lado. Se III tivesse mantido Cerco, o cerco teria avançado no mesmo turno.*
>
> ***▶ Exemplo — três reinos, uma Surtida.** O hexágono amuralhado (24,34) da Hyperborea contém o II da Hyperborea, o VI da Nemedia e o I da Zingara, todos cercados pela Aquilonia (o cerco pôs os três em guerra com ela, §5.6). A Nemedia e a Zingara entraram em guerra uma com a outra no turno passado. Os três ordenam Surtida. A Hyperborea, a dona, entra primeiro; dos outros dois, o que está antes na lista junta-se e o outro — em guerra com ele — é **retido** (held back from the sally) e fica dentro em Guarnição — e na Fase 5 o varrimento de acampamento põe a Nemedia e a Zingara a combater uma contra a outra dentro das muralhas (§2.13.5). Quem perder **fica dentro** enquanto o anel se mantiver: um exército cercado que perde ou empata uma batalha no seu hexágono cercado nunca recua para fora do cerco. Se a Surtida tivesse vencido e quebrado o anel nesse mesmo turno, o cerco teria acabado, e o perdedor recuaria como qualquer exército batido. Os dois que saem combatem a Aquilonia como um só lado, sem ligação entre eles.*
>
> ***▶ Exemplo — uma surtida nunca inicia uma guerra.** O hexágono amuralhado (18,9) da Aquilonia está cercado pelo III da Cimeria; lá dentro estão o II da Aquilonia e o I da Zingara (ambos em guerra com a Cimeria, §5.6), e ambos ordenam Surtida. Acampado fora, ao lado de III, está o IV da Nemedia, em guerra com a Aquilonia mas em paz com a Zingara. A surtida combate todos os exércitos de fora em guerra com o reino líder — a Aquilonia, a dona — portanto IV também é um adversário; a Zingara não está em guerra com a Nemedia, por isso o I da Zingara é **retido** (held back from the sally … a sally never starts a war) e fica dentro em Guarnição. II sai sozinho contra III e IV.*
>
> ***▶ Exemplo — a aliança quebra-se a meio do cerco.** A cidade amuralhada (14,9) de Gruk-Mor, cercada por Aldoria desde o turno 2; lá dentro estão o I de Gruk-Mor e o II de Sylvane. No turno 5, Sylvane termina a sua aliança com Gruk-Mor. No turno 6, II ordena uma marcha para fora: recusada — Army II besieged — march refused. Já não é amigo de Gruk-Mor, mas começou o cerco dentro e **permanece** dentro. Se Sylvane declarar então guerra a Gruk-Mor, o varrimento de acampamento da Fase 5 seguinte põe I e II a combater um contra o outro **dentro** das muralhas — e quem perder também fica dentro, em Guarnição. Na queda, II não é a guarnição de Gruk-Mor: é expulso (§2.7).*
>
> ***▶ Exemplo — paz com o sitiante.** A mesma cidade. No turno 5, Sylvane faz antes a paz com Aldoria. II continua cercado no turno 6: a sua marcha é recusada, e o tique de cerco dessa mesma pré-fase declara de novo guerra a todos os reinos lá dentro (§5.6), Sylvane incluída. Assinar a paz não abre as portas — só o fim do anel o faz.*
>
> ***▶ Exemplo — a porta do porto.** O II da Hyperborea está cercado no seu próprio porto amuralhado (24,34), e galés aquilónias dominam os hexágonos de mar junto ao porto. Turno 33: II **embarca** na Frota I no porto — o embarque vem antes da verificação de cerco, por isso II está a bordo, e deixa de estar cercado. Turno 34: a Frota I desembarca II em (25,34), um hexágono de terra **junto ao** porto, sem sair para o mar. II está fora do anel, livre para marchar no turno 35.*
>
> ***▶ Exemplo — desembarcar no teu próprio porto cercado.** A Aquilonia cerca o porto amuralhado (24,34) da Hyperborea com o Exército VII em Cerco. A Frota II da Hyperborea traz o Exército IV de casa e desembarca-o em (24,34). Isto é um **combate de praia contra o sitiante**, a céu aberto: IV desembarca a ×0.50, VII defende a Cerco ×0.85 (×1.00 se tivesse ordenado Assalto) — sem muralhas, sem milícia, e o II cercado da Hyperborea lá dentro **não** se junta (um exército cercado só sai por Surtida). **Vitória:** VII retira-se, IV fica **fora** das suas próprias muralhas sem postura (−20 de estado de desembarque) — uma ordem de Guarnição leva-o para dentro no turno seguinte — e o anel levanta-se no turno seguinte — o teu relatório ainda pode trazer o cartão Under siege nesse turno; limpa-se no seguinte. **Derrota ou empate:** IV volta a embarcar na Frota II, e o cerco continua.*
>
> ***▶ Exemplo — um grupo ligado faz surtida.** Dentro de (24,34), o II da Hyperborea lidera uma ligação com o VI da Nemedia; ambos estão cercados. Só II ordena Surtida, e VI sai com ele — um membro segue o seu líder, e a ordem de Surtida do próprio VI seria ignorada. Se o líder de VI fosse um exército fora das muralhas, VI abandonaria esse grupo (Army VI besieged — left its link group) e ordenaria a sua própria Guarnição ou Surtida.*
>
> ***▶ Exemplo — socorro vindo de fora.** O III da Cimeria cerca (18,9) da Aquilonia; o II da Aquilonia lá dentro está cercado. No turno 12, o cerco de III avança na Pré-Fase 3; na Fase 5, o Exército IV da Aquilonia marcha para casa sobre (18,9) e enfrenta III às portas, onde III defende a **Cerco ×0.85**. II, cercado, **não** se junta ao ataque de IV — um exército cercado nunca combate fora das suas muralhas a menos que ordene Surtida; se II tivesse ordenado Surtida nesse turno, teria combatido III primeiro, na Pré-Fase 3, e IV teria enfrentado o que restasse. IV vence e III recua: no turno 13 nenhum sitiante pressiona o anel, por isso II não está cercado e pode marchar, e o cerco levanta-se nesse turno. Se IV tivesse perdido ou empatado, IV recua para fora do hexágono e o anel mantém-se; II, que nunca saiu das muralhas, continua cercado.*
>
> ***O que a tua Página do Jogador mostra num exército cercado:** uma nota vermelha Besieged by X at (c,r) — only Garrison or Sally; todas as posturas exceto 🏰 Garrison e 🚪 Sally esbatidas com o motivo; nenhuma marcha pode ser colocada em fila (diz porquê); um membro que abandona a sua ligação é avisado. O cartão de Ordens em vigor lê inside the walls · besieged by X — Garrison or Sally only, no march. Um reino que falha o turno mantém Guarnição, nunca faz surtida, e rende-se com as muralhas se elas caírem.*
>
> ***▶ Exemplo prático — uma Surtida e um socorro no mesmo turno.** A cidade amuralhada (18,9) da Aquilonia, um povoado comum (cai quando o progresso excede 4). O Exército III da Cimeria cerca-a desde o turno 10 e está com estado de 90%; após o turno 11 o progresso é 2. Lá dentro, o Exército II da Aquilonia (estado 80%) está cercado. O Exército IV da Aquilonia, a um hexágono de distância em (17,9), marcha para casa no turno 12, e II ordena **Surtida** no mesmo turno.*
>
> *\| Turno 12 \| O que acontece \| Regra \|*
>
> *\|---\|---\|---\|*
>
> *\| **Pré-Fase 3 — a Surtida** \| II sai e ataca III a céu aberto: sem postura, sem muralhas, sem milícia para II; III defende a **×1.00**. III vence com um rácio de 2.0: III paga −12 de estado (90% → 78%), II paga −18 (80% → 62%) e os seus sobreviventes escapam de volta para dentro em Guarnição. III também perdeu homens. \| §2.13.7, §5.10.4 \|*
>
> *\| **Pré-Fase 3 — o tique** \| A Surtida perdeu, por isso o cerco avança: progresso 3. Não ultrapassa 4, logo as muralhas resistem. \| §5.8.2 \|*
>
> *\| **Fase 5 — o socorro** \| IV marcha sobre (18,9) e enfrenta III às portas. III defende a **Cerco ×0.85**, com o seu novo 78% e sem os homens que a Surtida matou. II fica dentro — uma Guarnição nunca entra na batalha do socorro. \| §5.8, §2.13.5 \|*
>
> *\| **IV vence** \| III recua. No turno 13 ninguém pressiona o anel: II não está cercado e pode marchar, e o cerco levanta-se, com o progresso de volta a 0. \| §5.8.5 \|*
>
> *\| **IV perde ou empata** \| IV recua para fora do hexágono. O anel mantém-se, II continua cercado, e o tique do turno 13 leva o progresso a 4 — Collapse imminent — com a queda no turno 14 a menos que o anel seja quebrado antes. \| §5.8.3 \|*
>
> *- **Se a Surtida tivesse vencido**, III teria recuado na Pré-Fase 3 e o cerco teria sido levantado; IV marcha para casa na Fase 5 para muralhas sem ninguém às portas e fica fora delas — uma ordem de Guarnição leva-o para dentro no turno seguinte.*
>
> *- **Se a Surtida tivesse empatado**, ambos pagam −15, III não faz progresso neste turno (fica em 2) e IV combate-o na Fase 5 a ×0.85, agora com 75%.*
>
> *- **Se o progresso estivesse em 4 após o turno 11**, o tique da Surtida perdida leva-o a 5 e a cidade cai na Pré-Fase 4: III fica dentro das suas novas muralhas, e a marcha de IV na Fase 5 é um assalto a muralhas cimérias. Uma Surtida empatada teria impedido esse tique e mantido a batalha às portas para IV.*
>
> *- **O que nunca acontece** é II e IV combaterem III lado a lado numa só batalha, com o seu poder de guerra somado: a Surtida e o socorro são sempre duas batalhas, por essa ordem.*
>
> ***▶ Exemplo — o sitiante recuou.** No turno 14, III ordena Defensiva em vez de Cerco. O anel não é pressionado, por isso ninguém em (18,9) está cercado nesse turno: uma Surtida que II tenha ordenado é lida como Guarnição (a tua Surtida não se aplica aqui), e ambos os lados lêem Siege … lapsed. A tua página não podia saber de antemão as ordens de III, por isso não te deixou colocar uma marcha em fila — marcha no turno 15, antes de III ordenar Cerco de novo (o contador recomeça de 0).*

**2.13.8 Declaração de Guerra por Movimento (War Declaration from Movement)**

Se um exército se move para um hexágono (hex) pertencente a um reino — ou se move para combater um exército de um reino — que não esteja atualmente em guerra (war) com quem se move, a guerra é declarada automaticamente antes de o combate ser resolvido. Isto aplica-se quer o hexágono de destino esteja **sem defesa** (uma tomada de território) quer **defendido** (uma batalha campal), e aplica-se mesmo quando o alvo é um terceiro neutro cujo exército atacas em terreno disputado ou no teu próprio terreno. Cada declaração deste tipo custa ao agressor **−3 a −8** de opinião (opinion), reforça o defensor em **+2 a +5**, e gera cartões para ambos os reinos; um atacante que arrasta vários reinos para o mesmo combate paga a penalização de agressor apenas uma vez por passo de uma marcha ou viagem, ou uma vez por batalha (§8.5.3).

Uma guerra iniciada neste turno bloqueia também todas as ordens de postura (stance) que não sejam de guerra dirigidas a esse inimigo na Fase 8 do mesmo turno (§2.16.2).

> *Uma guerra iniciada ao atacar um exército acarreta exatamente a mesma penalização de opinião e a mesma notificação que uma iniciada ao entrar em terra sem defesa — não existe forma "discreta" de começar uma guerra através de movimento.*

**2.13.9 Verificação de Eliminação de Reino (Kingdom Elimination Check)**

Depois de a Fase 5 estar totalmente resolvida, o TP verifica todos os reinos ativos. Se um reino não possuir **nenhum território** (todos os hexágonos capturados ou nunca possuídos), é assinalado como **eliminado**:

- A marca de eliminado persiste no estado do GM em todos os turnos seguintes.

- Os exércitos existentes não são destruídos pela marca — continuam a consumir manutenção (upkeep) e passarão fome na Fase 2 se não houver comida.

- É emitida uma entrada de registo do GM **uma única vez**, no turno em que o reino é assinalado (os reinos já eliminados são ignorados), para que o GM seja notificado. A verificação corre novamente no **fim da Fase 6**, pelo que um reino cujo último hexágono cai perante um desembarque anfíbio é assinalado no mesmo turno.

- O GM pode terminar a participação do reino eliminado a seu critério.

**2.13.10 Sucessão da Capital — A Sede de Recrutamento (Muster Seat)**

Cada reino tem uma **sede de recrutamento**: o único hexágono onde são levantados novos exércitos (Pré-Fase 2, §2.6; uma ordem de recrutamento que não encontre nenhum exército levanta um aqui na Pré-Fase 2b) e onde qualquer exército "na capital" se considera estar. Normalmente esta é a tua **capital**. A sede só importa quando a tua capital te é tomada — perder a capital **não** termina o teu reino nem te impede de levantar tropas; a sede limita-se a *suceder* a outra possessão.

**Como é escolhida a sede.** Resolvida no início de cada turno, por prioridade estrita:

1\. **A tua capital inicial original, se ainda a possuíres.** Enquanto fores dono da capital com que começaste o jogo, ela é sempre a tua sede. (Retomá-la após uma perda restaura-a.)

2\. **Caso contrário, a tua sede atual — sem alterações.** Depois de a sede ter saído de uma capital perdida, **fica onde está**. **Não** salta para outra cidade só porque essa cidade cresceu, ou porque recrutaste população dali. As alterações de população nunca movem a sede.

3\. **Só quando a própria sede é conquistada** é que ela volta a mudar — para a tua **maior construção sobrevivente**, classificada pelo **teto de população** do seu nível (não pelo número atual de habitantes), com a população atual a desempatar. Só se escolhe um hexágono vazio se não possuíres qualquer construção — classificado em último lugar e **não** eliminado: um reino assim não pode cobrar impostos, recrutar soldados nem erguer construções (§3.7), embora um exército permanente com soldados ainda possa construir máquinas de cerco a partir das reservas (§2.12.1), e o estado é recuperável se o GM colocar uma construção. Um reino que não possua nem uma coisa nem outra está acabado (§2.13.9).

> ***A regra a recordar: a tua sede só muda por conquista** — ou, para um **Nómada**, ao viajar com um acampamento que moves (§2.11.10). Muda no turno seguinte à captura do hexágono da tua sede — nunca por crescimento da população, recrutamento ou qualquer outra coisa. A classificação abaixo só é consultada no momento em que uma sede se perde, para escolher a seguinte; a mudança de acampamento de um Nómada leva consigo a sede existente e nunca reclassifica nada.*

**Duas capitais capturadas.** Se conquistares uma sede inimiga enquanto ainda possuis a tua, **a tua capital original continua a ser a sede** — a capturada não a substitui. Só se *perdeste* a original e possuis duas ou mais sedes capturadas é que a classificação acima escolhe entre elas.

**A sede é mais do que um ponto de recrutamento.** O hexágono que contém a tua sede de recrutamento recebe:

- **+0.10 de bónus de fortaleza** além do que a muralha da sua construção já proporciona — somado antes do escalonamento por integridade, pelo que se esvai com a muralha e desaparece numa brecha (§5.6.1)

- **Limiar de cerco 5** em vez de 4 — mais um turno de cerco antes de cair (§5.8.3)

Não recebe qualquer bónus de rendimento ou de população: esses vêm da construção que ali se encontra, exatamente como em qualquer outro hexágono. Move a sede e ambas as vantagens defensivas movem-se com ela.

**A sede precisa de espaço de pilha para levantar.** A coabitação de exércitos aplica-se ao recrutamento: novos exércitos podem ser levantados **ao lado** de exércitos já presentes na sede, até ao limite de **3 exércitos por hexágono**. Na tua própria sede **com muralhas** o limite conta o **interior** das muralhas, onde um novo exército nasce em Guarnição (Garrison) (§5.8.0) — os inimigos acampados no exterior não ocupam espaço, pelo que podes levantar um exército sob cerco; numa sede sem muralhas contam todos os exércitos ali presentes. Numa sede cheia o levantamento é cancelado pelo Processador de Turnos (e as ordens de recrutamento dirigidas a esse exército nunca levantado são canceladas com ele, com um cartão no teu relatório). Um exército liberta o seu lugar ao marchar para fora, ao embarcar ou — dentro das muralhas — ao adotar uma postura diferente de Guarnição; um exército cercado só pode embarcar. **Um exército que embarca a partir da sede liberta espaço no mesmo turno** quando estava onde o novo exército é levantado (dentro das muralhas, na tua própria sede com muralhas): o levantamento conta-o como tendo partido. Se esse embarque falhar, o exército fica e continua a contar — os recrutas do novo exército encontram o hexágono cheio e não são aceites (nada é cobrado, com cartão), e o exército, sem soldados, é atingido no fim do turno. A Página do Jogador avisa quando um levantamento só cabe por causa de um embarque em fila.

**Sem sede = eliminado.** Um reino que **não possui qualquer território** não tem sede e não pode levantar exércitos — esse é o estado de eliminado (§2.13.9).

> ***▶ Exemplo — um reino decapitado continua a lutar.** A tua capital cai no turno 5. No turno 6, a tua sede passa para a tua maior construção sobrevivente, **Oakhaven** (pop 1,200) — a tua outra possessão, Riverford, tem apenas 800. Levantas ali um exército novo e contra-atacas. Nos turnos seguintes Riverford cresce até 2,000, ofuscando Oakhaven — mas a tua sede **permanece em Oakhaven**, porque as sedes só mudam por conquista. No turno 10 o inimigo toma Oakhaven de assalto; no turno 11 a tua sede recua para Riverford (agora a tua maior). No turno 14 retomas a tua **capital original** — e a tua sede regressa a ela de imediato.*

**2.13.11 Despojos de Guerra (Spoils of War)**

Vence uma batalha terrestre **decisivamente** e o teu exército vitorioso despoja o campo — recuperando uma parte do material de guerra transportado por **cada soldado que tombou, de ambos os lados** (incluindo os teus próprios mortos). Isto aplica-se igualmente a **batalhas campais, assaltos (assaults) e desembarques em praia**. Um exército derrotado que **não consegue retirar** (cercado, sem para onde fugir) é destruído onde está — e esses caídos são despojados na totalidade juntamente com os mortos da batalha. Um **empate não rende nada**, e o mesmo acontece com um combate decidido **apenas por milícia** (ver abaixo).

**O que reclamas.** De cada unidade abatida — tua e do inimigo — o vencedor recupera uma percentagem do **ferro e dos cavalos** que foram gastos a levantá-la (o custo de construção de uma unidade *é* o material que ela transportava: o ferro das armas e armaduras, o cavalo que montava). As unidades construídas apenas com ouro e comida — escaramuçadores, infantaria ligeira — não rendem metal nem montadas.

**As coligações repartem o saque** entre os reinos vencedores em proporção ao seu poder de guerra, sendo cada quinhão arredondado em baixo separadamente. Isto inclui um desembarque em praia ao qual se juntou o exército de um aliado já em terra: o reino que desembarca e o aliado repartem o saque por poder de guerra. **Quanto — a grandeza da vitória.** O quinhão escala com o quão desequilibrada foi a vitória, medida pela tua jogada de batalha contra a do inimigo:

|             |                         |            |
|-------------|-------------------------|------------|
| **Vitória** | **A tua jogada vs a deles** | **Despojos** |
| Estreita    | pouco acima de 1.2×     | **20%**    |
| Renhida     | ~1.5×                   | **30%**    |
| Sólida      | ~2×                     | **40%**    |
| Forte       | ~3×                     | **50%**    |
| Decisiva    | 5×+                     | **60%**    |

**Os Orcs comem os caídos.** Um vencedor **Orc** leva também **comida** — não só as rações recuperadas das unidades mortas, mas os **próprios cadáveres**. Todos os corpos deixados no campo, de amigos ou inimigos, são arrastados para os caldeirões: o despojo de comida Orc é a mesma percentagem de vitória aplicada a (o custo em comida das unidades mortas **mais um por cada soldado caído**). Para uma horda, um campo de mortos arduamente conquistado é um banquete — vencer batalhas torna-se uma forma de alimentar a guerra, e nenhuma outra raça faz isto.

**Faz uma povoação morrer à fome e o arsenal é teu.** Quando uma povoação cercada (besieged) cai por **queda automática do cerco** (sem assalto, §2.7), a guarnição rende-se intacta — e entrega mais do que qualquer campo de batalha: o sitiante apreende **60–80%** (aleatório) do ferro e dos cavalos que equipavam a guarnição, seja qual for a raça do vencedor, e um sitiante **Orc** leva ainda **60–80%** das reservas de comida da guarnição. A rendição paga melhor do que a chacina (20–60%) — a paciência compensa. O saque aparece no teu cartão de relatório *"Enemy garrison surrendered"* como *⚔ Spoils of war (Surrender, N%)*. Um exército **desbaratado em debandada** na queda (§2.7) — expulso sem para onde retirar — é despojado aos mesmos 60–80% (e 60–80% da sua comida por um sitiante Orc).

**A milícia não rende despojos — exceto a um Orc.** Quando um hexágono é defendido **apenas pela milícia da população** — sem exército de guarnição permanente — o vencedor **não reclama ferro nem cavalos**: os habitantes empunham forquilhas, e as suas mortes contam como perda de população (§5.6). Mas um **Orc** não deixa carne num campo que detém: a milícia caída é arrastada para os caldeirões a **1 de comida por cabeça**, escalada por uma tabela de níveis de vitória situada 10 pontos abaixo da do material — Estreita **10%** · Renhida **20%** · Sólida **30%** · Forte **40%** · Decisiva **50%**. Isto aplica-se onde quer que caia milícia e um Orc fique a deter o terreno: **assaltar uma construção com muralhas** (o atacante come a leva caída dos defensores), **tomar um hexágono povoado ou uma praia** e — sinistramente — **um dono de povoação Orc cujas muralhas repelem um assalto come os seus próprios habitantes caídos** (uma guarnição de terceiros que defenda a povoação de outrem não recebe nada: os mortos não são o seu povo). Os empates não alimentam ninguém. Se um exército de guarnição lutar ao lado da milícia, os caídos da guarnição são recuperados aos níveis normais de batalha e os mortos da milícia aos níveis da milícia, fundidos num só cartão. **As batalhas navais não rendem material — os navios inimigos afundados são tomados como presas (§2.13.12).**

O teu relatório de turno indica o nível e o saque — por exemplo: *"⚔ Spoils of war (Decisive, 60%): +240 iron · +12 horses"* (com *· +N food* acrescentado para um vencedor Orc).

**2.13.12 Despojos Navais — Navios-Presa (Prize Ships)**

Vence uma batalha no mar e os teus marinheiros fazem mais do que ver o inimigo arder — as equipas de abordagem tomam alguns dos **navios que o perdedor perdeu no combate** como **presas**, repostos a flutuar e levados para casa sob as tuas cores. **Cada casco (hull) que o perdedor perdeu no combate lança um dado (d6): com 1 a 4 é capturado, com 5 ou 6 afunda-se.** A margem de vitória não altera as probabilidades — uma vitória estreita toma presas tão certamente como uma debandada. Os teus próprios navios mortos ficam mortos. Os cascos perdidos **depois** do combate não lançam nada: uma frota derrotada **encurralada contra a costa** sem para onde fugir afunda-se onde combateu (§5.9.5), e esses cascos vão ao fundo. Um **empate não rende nada**.

**Uma presa mantém a sua verdadeira natureza.** Um *Wolfship* Bárbaro capturado continua a ser um Wolfship na tua frota — com o seu próprio ataque, defesa, capacidade, manutenção e **velocidade**. As tripulações das presas saem dos teus sobreviventes (sem custo de população), chegam **verdes** (experiência base — nunca a veterania do inimigo, e integrar presas novas num esquadrão veterano do mesmo casco dilui a sua vantagem), e o casco paga a sua **manutenção em ouro** normal a partir do turno seguinte.

**Atenção à velocidade.** Uma frota navega à velocidade do seu **casco mais lento** (§2.14). Uma presa de 60 mp numa frota toda de 90 mp reduz-te de 3 hexágonos de mar para 2 — para uma marinha rápida, uma presa pode custar mais em ritmo do que vale. Uma presa tomada a meio da viagem abranda a frota de imediato: o resto dessa viagem é navegado ao novo ritmo. Nunca és obrigado a ficar com uma: transfere-a para uma frota mais lenta, ou deixa-a afundar-se no combate seguinte.

**Vencer até ao último navio.** Se uma batalha for tão sangrenta que a **frota do próprio vencedor é aniquilada na vitória**, as presas são tomadas na mesma: os sobreviventes regressam a casa a bordo dos navios capturados, e um exército transportado a bordo passa com eles. Se não foram tomadas presas, a frota perde-se como qualquer outra — exército incluído.

**Como as presas são repartidas.** Quando dois ou mais reinos venceram em conjunto, os cascos capturados são repartidos por **quota de pontos de guerra** (maior resto, empates para o parceiro mais forte) e distribuídos **do melhor para o pior** a quem tiver mais presas ainda em dívida. Um parceiro de 40% num saque de cinco cascos fica com dois.

O teu relatório indica o saque e de onde veio: *"⚓ Prizes taken: 3 of the 4 hulls the enemy lost — 2× Wolfship, 1× Reaver"*; quando os reinos venceram em conjunto, cada cartão indica as suas próprias presas de entre todos os cascos que o inimigo perdeu. O cartão do perdedor permanece em silêncio — ele descobre para onde foram os seus navios quando estes voltarem a disparar. (Orcs e Anões não têm frotas, e não podem nem tomar presas nem perdê-las.)

**2.14 Fase 6 — Movimento da Marinha (Phase 6 — Navy Movement)**

**2.14.1 Iniciativa e Terreno Válido (Initiative and Valid Terrain)**

**Ordens em vigor no mar.** A Fase 6 abre com o mesmo cartão para as tuas frotas (fleets): onde está cada uma (em porto ou no mar, e qualquer exército que transporte), o seu ESTADO, a sua postura em vigor — Raid, Blockade, Hunt ou nenhuma, *mantida do turno anterior* ou *ordenada neste turno* — e a sua ordem (*sail* com a rota, *stays*, *none*, ou a nau capitânia que uma frota ligada segue).

As frotas movem-se em **rondas** (rounds) pela mesma regra de prontidão primeiro que os exércitos (§2.13.1): um hexágono por ronda, ESTADO atual da frota mais alto primeiro, e **uma frota bloqueada pára durante o turno**. A fadiga das frotas está plenamente ativa — navegar custa ESTADO por hexágono (costeiro 3 / alto mar 6; Aesir 2 / 4 — §5.10.6) — pelo que uma frota acabada de sair do porto supera e vence uma que esteja no fim de uma travessia de águas profundas. As frotas só se movem por hexágonos de mar e de porto.

**A tua própria rota e os avistamentos de rota** funcionam no mar exatamente como em terra (§2.13.2). A rota inclui um salto em que a frota combateu e, vencendo claramente, seguiu viagem — *Fleet III sailed to (26,27) · route (27,26) → (26,26) → (26,27) · 3 hop(s) · At sea*, ou no cartão que terminou a viagem, *Naval victory (Fleet I) … · Fleet I route (3,0) → (4,0)*; uma fuga forçada após uma derrota não faz parte dela. Uma frota encontra uma frota estrangeira no hexágono para onde avança — no mar ou atracada no porto — e os exércitos estrangeiros parados nesse porto; um grupo de frotas ligadas em movimento é reportado uma só vez, pela sua nau capitânia. Os cartões dizem *Fleet N crossed paths on its route* / *Foreign forces passed Fleet N at (c,r)*.

**2.14.2 Entrada em Porto e Combate (Port Entry and Combat)**

As frotas (fleets) podem navegar para qualquer hexágono (hex) de porto (port), independentemente da postura diplomática face ao proprietário — portos próprios, aliados, neutros e inimigos são todos destinos válidos. Um porto livre é acedido livremente e a frota atraca nele; a atracagem, por si só, não implica qualquer tomada. Um hexágono — mar alto ou porto — comporta até 3 frotas de qualquer combinação de relações, exceto em guerra. As frotas neutras nem bloqueiam nem são bloqueadas: a tua frota pode passar por elas, partilhar o hexágono ou atracar ao lado delas, se houver espaço. Um hexágono cheio (3 frotas) interrompe o movimento; uma frota em guerra no hexágono significa uma batalha (battle) naval à chegada, como sempre. A coabitação aplica-se **em qualquer lugar** — o mar não tem dono, pelo que, ao contrário dos exércitos, não existe barreira terrestre; um encontro no mar é precisamente o objetivo de uma frota. A propriedade de um porto só muda através da **conquista terrestre** do hexágono — uma tomada por marcha ou assalto (assault) (§2.13) ou um desembarque anfíbio (§2.14.6); as frotas nunca mudam a posse de um hexágono. Capturar um porto fortificado — por assalto, por queda automática do cerco (siege) ou por qualquer outra mudança de posse — **não** expulsa uma frota de terceiros ali atracada, a menos que esteja **em guerra** com o captor; uma frota aliada ou neutra aguenta a mudança de proprietário e continua atracada.

**O que o proprietário do porto vê.** Uma frota estrangeira que **termina o seu movimento** no teu porto — a viagem acabou ali, ou foi interrompida ali — é-te comunicada uma vez, se **ainda lá estiver quando o movimento das frotas e as batalhas navais do turno terminarem**; uma frota que apenas navega **através** do teu porto a caminho de outro lugar não é comunicada, nem uma que tenha sido afundada ou expulsa do teu porto mais tarde nesse mesmo turno. Os cascos (hulls) são contados nesse momento, depois de quaisquer baixas. Uma frota derrotada que **se refugia** no teu porto depois de perder uma batalha naval nas proximidades é comunicada da mesma forma, e o seu cartão diz que fugiu para lá e onde perdeu. O título segue a tua relação no fim do turno: *"Allied fleet entered your port"* (aliado mútuo, vassalo ou suserano, pelo que uma aliança assinada nesse mesmo turno aparece como aliada), *"Foreign fleet entered your port"* (não está em guerra) ou *"Enemy fleet entered your port"* (em guerra). Todos os cartões indicam o comandante da frota, os cascos por tipo e o poder de guerra, e, no caso de uma **frota** aliada que atraque no teu porto, também o exército que transporta (os aliados nada escondem); **o que uma frota não aliada transporta permanece oculto** — a carga é assunto de espiões. Assim, uma frota **estrangeira** com a qual não estás em guerra pode atracar no teu porto e ficarás a conhecer os seus cascos; pode já ter-te pilhado ao entrar, e pode pilhar de novo a partir do seu cais no turno seguinte — cada pilhagem é uma declaração de guerra (§2.14.3) — a não ser que navegue num grupo ligado, que só pilha através da sua nau-capitânia (§2.14.7), e o seu cartão di-lo. **O teu próprio porto é a única exceção** a "os inimigos só concedem avistamentos": uma frota inimiga no teu porto é comunicada com o mesmo detalhe, porque qualquer pessoa nas tuas docas consegue contar-lhe os cascos. Uma frota que comissiones nesse porto enquanto o inimigo lá está tem de o combater antes de poder zarpar — dá-lhe cascos no mesmo turno, ou é afundada no estaleiro (o cartão di-lo apenas a um reino que construa frotas) — e pode Pilhar (Raid) ou Bloquear (Blockade) o porto no turno seguinte. O cartão diz se entrou sem oposição quando já estavas em guerra, ou se atracou antes de a guerra rebentar nesse turno.

**Batalhas no teu porto.** Uma frota que tem de abrir caminho à força não é uma convidada: se **tu** fores um dos lados, o teu próprio cartão de batalha di-lo; se dois **outros** reinos lutarem no teu porto, recebes *"Battle in your harbour"* com os dois lados e o resultado, **cada frota que combateu tal como entrou no combate** (cascos por tipo, poder de guerra, comandante; carga apenas para aliados), o que cada uma perdeu nesse combate e onde ficou no fim do turno — ainda no porto, em (c,r), ou afundada — dito uma vez por frota, **o relatório completo da batalha**, o mesmo painel que um combatente recebe, desenhado *Atacante \| Defensor* com o vencedor nomeado (o gémeo naval de uma batalha na tua terra), e todas as frotas estrangeiras ali atracadas depois de terminado o combate. Se alguma frota no combate **não for tua amiga**, vês esse painel *a partir das tuas docas*: sem linha de conveses cheios e sem derivação completa, porque a carga é assunto de espiões (o painel di-lo). Não tomaste parte, pelo que não sofres baixas, e só os navios nunca tomam o porto.

**Uma frota inimiga dentro do teu porto** — um bloqueador ou um intruso — pode ser combatida de duas maneiras: comissionar ali uma nova frota, que defende o porto contra ela antes do movimento, ou enviar uma frota tua ou de um aliado para a expulsar. Em ambos os casos, o recém-chegado combate a ×1.00: o bónus de porto pertence apenas a uma frota que começou o turno no porto, atacante ou defensora (§5.9.2) — pelo que uma frota mantida ali atracada é a que a combate a ×1.25. Vários combates no mesmo porto nesse turno surgem num **único** cartão que nomeia cada um, com um painel de batalha por combate. Um combate entre frotas que **já partilhavam o porto** quando o turno começou — uma frota erguida sob os canhões de um inimigo, ou uma guerra que rebenta entre frotas atracadas juntas — é descrito exatamente assim em todos os lados (a tua nova frota, a nova frota do teu aliado, a nova frota do inimigo, ou a guerra a encontrar as frotas atracadas juntas), nunca como um lado a entrar para atacar. Os cartões do choque dizem de quem era a frota nova, para cada leitor: *"Your newly raised fleet met X's ships already lying in …"*, *"Your ally X raised a new fleet in …, and yours fought beside it against Y's ships"* ou *"X raised a fleet in … while yours lay there"*; se o proprietário do porto vencer, o título do seu cartão continua a ser *"port held, X driven off"*.

**Quem combate num tal choque**: do lado atacante, todas as frotas no hexágono cujo reino esteja **em guerra com o defensor** e seja do próprio atacante ou de um aliado mútuo, suserano ou vassalo — um aliado em guerra junta-se mesmo que não esteja ligado — mais os membros de qualquer grupo ligado cuja **nau-capitânia** esteja entre eles: os membros seguem a nau-capitânia para o seu combate (e são declarados em guerra por ela — mesmo um membro aliado do defensor, cuja aliança então termina, ou jurado a ele, cuja vassalagem então termina), liderados por essa nau-capitânia. A guerra própria de um membro nunca arrasta o reino da sua nau-capitânia — se apenas o reino de um membro estiver em guerra, esse membro combate e a nau-capitânia fica de fora, em paz ou aliada como antes. O lado defensor reúne todas as frotas no hexágono em guerra com o atacante — exceto uma que esteja em guerra com a frota defensora ou com outra frota já a defender — os membros ligados da nau-capitânia defensora contam desde o início — que fica à parte (a mesma regra de qualquer batalha naval).

**Quem defende** (como em terra): num porto, defende o proprietário do porto — ou um aliado mútuo, vassalo ou suserano dele; caso contrário, uma frota criada neste turno é a atacante. Nem o lado, nem quem ataca no mar ou num porto sem dono, depende da ordem em que as ordens do turno foram lidas. Todos os cartões de batalha naval travada num porto indicam de quem é o porto do teu lado do mesmo: uma frota derrotada enquanto estava no porto de outrem é informada de que era o porto desse reino, e um proprietário que ataca um inimigo intruso no seu próprio porto lê "your own port".

**O porto muda de mãos** mais tarde nesse turno (cedido a um aliado, ou tomado)? Os cartões vão para quem o possuir quando o turno terminar, redigidos como uma frota atracada em "a port that became yours this turn"; o reino que perdeu o porto não ouve mais nada sobre ele. Os cartões chegam uma vez, mas a vista permanece: passar o rato sobre um dos teus portos no mapa lista todas as frotas estrangeiras ali atracadas com o seu numeral, cascos por tipo, poder de guerra e comandante (e carga, apenas para aliados), enquanto lá permanecerem.

**Uma vitória clara não termina a viagem (como em terra).** Uma frota que encontra um inimigo num salto e o vence **claramente** — nenhuma frota em guerra com ela resta nesse hexágono, e ela própria continua à tona ali — **segue viagem pelos saltos que lhe restam**; um empate ou uma derrota termina a viagem onde o combate ocorreu (uma frota derrotada já recuou de qualquer forma). O mesmo vale para um Pirata (Pirate) em Caça (Hunt), como caçador ou como presa. Uma frota que abre caminho **para dentro de um porto** e vence fica atracada nele.

**2.14.3 Pilhagem de Porto (Port Raid)**

Uma frota atracada num porto estrangeiro não aliado, ou a navegar para um, pode definir a postura (stance) **Raid**. Uma pilhagem resolve-se em dois tipos de momento: **no início da Fase 6** para uma frota já atracada no porto estrangeiro quando o turno começou — dispara mesmo que a frota também zarpe nesse mesmo turno — e **à vela, em cada porto estrangeiro não aliado em que a viagem entra**, no momento em que a frota o penetra. Define Raid na frota e traça a rota: ela saqueia cada porto estrangeiro pelo caminho, sem aviso ao proprietário, e **segue viagem** — uma pilhagem a meio do caminho não termina a viagem (a viagem termina no último salto, ou onde um combate a pare, §2.14.2). Em cada porto a ordem é fixa: a pilhagem **declara guerra** ao proprietário do porto e a qualquer amigo do proprietário ali atracado (abaixo); se alguma frota agora em guerra com o pilhador estiver no porto, a **batalha no porto é travada primeiro**; o ouro só é levado **numa vitória clara** — o pilhador ainda à tona ali e nenhuma frota inimiga restante no porto. Um pilhador derrotado nessa batalha nada leva, e um **empate** também nada leva e termina a viagem no porto. **Vários portos, várias pilhagens**: uma frota que saqueou o seu cais no início da fase e depois navegou por mais dois portos estrangeiros saqueia os três — cada pilhagem com o valor normal dos fundos do respetivo porto, com o limite da tesouraria (treasury) do proprietário (abaixo) a reduzir os valores posteriores. O **mesmo** porto nunca é saqueado duas vezes num turno pela mesma frota: sair e voltar ao teu cais não rende uma segunda pilhagem. E **um porto entrega o seu espólio uma vez por turno, a quem lá chegar primeiro**: uma segunda pilhagem nesse turno, por qualquer frota de qualquer reino — incluindo a tua segunda frota — continua a declarar guerra e continua a combater o que estiver atracado, mas leva **0g**, e ambos os lados são informados de que o porto já tinha sido saqueado. Um pilhador derrotado ou levado a empate no porto nunca o saqueou, pelo que o porto continua aberto ao próximo pilhador.

**Valor da pilhagem**: floor(portIncome × raidPct / 100) — portIncome é o ouro da Fase 1 desse porto neste turno, depois de qualquer redução por escalão (§2.9.4) — apenas ouro, comida excluída. O valor levado é adicionalmente **limitado pela tesouraria do proprietário** no momento da pilhagem: só roubas o que eles realmente possuem, e uma tesouraria vazia rende 0g (a guerra é declarada na mesma).

**A eficiência da pilhagem** escala com o poder de guerra total da frota pilhadora relativamente à frota viva mais forte neste turno: raidPct = clamp(20, 80, round(20 + (thisPower / maxFleetPower) × 60))

A frota mais fraca possível pilha a 20%; a mais forte a 80%. O ouro é transferido diretamente da tesouraria do defensor. A propriedade e a população não mudam, mas **uma pilhagem declara guerra** ao proprietário do porto (ver abaixo).

**Uma pilhagem que não pode disparar é comunicada.** Uma frota que navega com Raid definido saqueia todos os portos estrangeiros em que entra; uma cuja viagem não entra em nenhum — mar até ao fim, ou apenas portos próprios, de um aliado ou sem dono — nada leva e é informada do motivo, uma vez, no fim da fase. A Página do Jogador (Player Page) oferece Raid sempre que o cais ou qualquer salto da rota seja um porto estrangeiro, e retira a postura, dizendo-o, no momento em que a rota deixa de entrar em algum. Define Raid numa frota que está atracada no teu próprio porto ou no de um aliado, ou cuja viagem não entra em nenhum porto estrangeiro, e o teu relatório (report) traz um cartão ⚡ *"Raid not possible this turn"* a nomear o motivo; nada é levado. Um pilhador **derrotado** num porto não recebe tal cartão — o seu cartão de batalha é a resposta. **Raid é uma ordem por turno — nunca transita** (só o Bloqueio — enquanto surte efeito, §2.9.3 — e a Caça de um pirata, §2.14.9, são guardados). Para saquear, mantém a posição no porto estrangeiro e **define Raid de novo no turno seguinte**; uma frota deixada sem ordem de postura não faz nada.

**Pilhar declara guerra**: Uma pilhagem é um ato de guerra. Pilhar um porto não aliado **declara guerra** automaticamente ao seu proprietário (a menos que já estejas em guerra), aplicando a penalidade padrão de opinião (opinion) por declaração de guerra (−3 a −8) e enviando um aviso de guerra a ambos os reinos. Como estás então em guerra, uma frota defensora no porto **empenha a tua em combate naval** — ancorada, a batalha de coabitação no porto que se segue à pilhagem; à vela, a batalha no porto travada **antes** de qualquer saque — pelo que uma pilhagem nunca fica sem oposição, e um defensor suficientemente forte pode afundar o pilhador. **Os amigos do proprietário também defendem o porto**: uma frota atracada no porto pilhado cujo reino seja aliado mútuo, vassalo ou suserano do proprietário do porto é igualmente declarada em guerra pela pilhagem e combate ao lado do proprietário — mesmo quando o proprietário não tem ali qualquer frota, e mesmo que esse reino fosse teu aliado até então (a guerra termina a aliança, como qualquer guerra). Uma frota de um reino que seja meramente neutro para o proprietário continua espectadora, como em qualquer combate num porto. A pilhagem e esse choque no porto são **um só confronto**: quando o choque também arrasta um membro ligado do proprietário para a guerra, a penalidade de opinião de agressor é paga apenas uma vez. Se já estás em guerra, a pilhagem prossegue simplesmente. Não podes, portanto, pilhar um reino e continuar em paz com ele — a Página do Jogador avisa-te (⚠) antes de definires a postura Raid.

**O primeiro a chegar, o único servido**: quando várias frotas pilham o mesmo porto num turno, a primeira pilhagem a chegar ao passo do saque — as pilhagens ancoradas resolvem-se primeiro, por ordem de carregamento dos ficheiros, depois as pilhagens à vela à medida que as frotas entram — leva a sua parte; todas as pilhagens posteriores nesse porto nada levam (acima). (Um **grupo ligado** pilha como um só — ver §2.14.7: a nau-capitânia pilha **uma vez** com o poder somado do grupo, não uma vez por casco.)

**O limite da tesouraria também é por ordem de chegada**: as pilhagens a portos *diferentes* da mesma vítima são pagas pela mesma ordem de processamento, cada uma limitada pelo que a tesouraria ainda contém — sem proporcionalidade — pelo que um alvo que parece rico pode já ter sido depenado por um pilhador anterior nesse turno.

Um porto bloqueado (Secção 2.9.3) não gera rendimento, pelo que uma pilhagem contra ele rende 0g.

**Pilhar cansa as tripulações.** Um turno em que a frota pilha custa-lhe estado (status) uma vez, além da navegação e de qualquer combate no porto — ver a linha **Raid** de §5.10.6.

> ***▶ Exemplo — a armadilha do porto vazio.** Um jogador pode raciocinar: "não precisas de frotas para defender portos — um pilhador tem de atracar no turno anterior, leio os seus cascos no meu relatório, e compro apenas os navios suficientes para o vencer." Duas regras tornam isso errado:*
>
> *- **Pilhagem à vela.** Um pilhador saqueia no turno N, no momento em que navega para dentro do porto — e nem sequer precisa de parar lá. Não há turno de aviso. A única coisa que o detém é uma frota atracada no porto, tua ou de um aliado: o pilhador tem de a vencer ao entrar, e nada leva se não o fizer.*
>
> *- **Bónus de guarnição.** Uma frota reativa comprada no turno N+1 é uma frota **criada neste turno**: não estava no porto quando o turno começou, pelo que combate a **×1.00**. Se tivesses mantido ali atracada mesmo uma pequena frota e comprado cascos para ela, essa frota combateria com o ×1.25 completo — o bónus segue a frota que começou o turno no porto, não os cascos. Uma frota que navega desde o porto seguinte para ajudar também combate a ×1.00.*
>
> *Efeito líquido: uma frota permanente no porto é o que defende um porto. Comprar navios depois de o inimigo aparecer continua a funcionar — para dentro de uma frota que já lá estava, ou como nova frota sem bónus — e só depois de a primeira pilhagem já ter acontecido.*
>
> ***▶ Exemplo — uma pilhagem ao longo da costa.** A Frota II da Nemedia (8 Drommunds, 90 mp: três saltos) define Raid e traça (12,8) → (13,8) → (14,8), onde (12,8) e (14,8) são portos da Aquilónia e (13,8) é mar alto. Salto 1: a frota entra em (12,8); ninguém está atracado ali. A pilhagem declara guerra à Aquilónia, leva 60% do rendimento desse porto neste turno — digamos 1,200g de 2,000g — e a frota segue viagem. Salto 2: mar alto. Salto 3: a frota entra em (14,8), onde a Frota I da Aquilónia (2 Busse) e a Frota III da sua aliada Hiperbórea (1 Busse) estão ancoradas. A Aquilónia já está em guerra; a pilhagem agora declara guerra também à Hiperbórea, e a batalha no porto é travada de imediato — a Nemedia a atacar, a frota da Aquilónia a liderar a defesa a ×1.25 (começou o turno no seu porto, §5.9.2) com a da Hiperbórea a seu lado. A Nemedia vence claramente: ambos os defensores são expulsos, o porto rende 60% do seu rendimento, limitado pelo que a tesouraria da Aquilónia ainda contiver depois da primeira pilhagem, e a Frota II termina o turno atracada em (14,8), inimiga de dois reinos. Se os defensores tivessem resistido (empate) ou vencido, (14,8) não teria pago nada e a viagem teria terminado ali — as 1,200g do primeiro porto ficam levadas em qualquer dos casos. A Frota II paga o −3 de estado da pilhagem uma vez, embora tenha saqueado dois portos, além dos seus três saltos e da batalha (§5.10.6).*

**2.14.5 Exércitos Transportados (Transported Armies)**

**Só as tuas próprias frotas transportam os teus exércitos — e as tuas frotas só transportam os teus exércitos.** O transporte nunca atravessa uma bandeira, seja qual for a relação: a frota de um aliado, de um suserano ou de um vassalo nunca pode receber o teu exército a bordo, e a tua frota nunca pode receber o deles. Tanto o exército como a frota indicados numa ordem de embarque têm de ser teus; a Página do Jogador (Player Page) só oferece as tuas próprias frotas, e o Processador de Turnos (Turn Processor) procura ambos apenas entre as tuas próprias forças. Para mover por mar o exército de um aliado, o aliado precisa de uma frota própria.

**Um embarque em porto só se faz num porto que seja teu.** O teu exército e a tua própria frota estarem juntos num porto não basta: o porto tem de ser **teu**. O porto de um aliado permite que a tua frota atraque e **desembarque** tropas aí, mas nunca que as embarque — e um porto neutro ou inimigo também não. A Página do Jogador só oferece um embarque em porto nos teus próprios portos, e o Processador de Turnos recusa qualquer outro com um cartão **"Port embark failed"** que diz que o porto não é teu e como embarcar em alternativa. A propriedade é verificada no início do turno, quando o embarque acontece (Pré-Fase 2). Para embarcar em qualquer outro lado, usa um **embarque em praia (beach embark)**: a tua própria frota fica fundeada num hexágono de mar junto ao exército, e o exército embarca a partir de terra — qualquer terra exceto montanha, seja de quem for (§2.14.6).

**Onde o teu exército pode embarcar:**

|                                                          |                                   |                                               |                                     |
|----------------------------------------------------------|-----------------------------------|-----------------------------------------------|-------------------------------------|
| **O teu exército está em…**                              | **A tua própria frota está…**     | **Embarque em porto**                         | **Embarque em praia**               |
| Um porto teu                                             | atracada nesse porto              | ✅                                            | —                                   |
| Um porto de um aliado                                    | atracada nesse porto              | ❌ recusado (*não é teu*)                     | —                                   |
| Um porto neutro ou inimigo                               | atracada nesse porto              | ❌ recusado (*não é teu*)                     | —                                   |
| Qualquer hexágono de terra exceto montanha — teu, de um aliado, de qualquer um | fundeada num hexágono de mar junto a ele | —                              | ✅                                  |
| Uma montanha                                             | fundeada junto a ela              | — (os jogadores não podem construir um porto numa montanha) | ❌ **nunca** — uma falésia, não uma costa |

**Um exército numa montanha não pode embarcar de todo.** Não há praia sob uma falésia, e os jogadores não podem construir um porto numa montanha. Faz-lo descer primeiro para um hexágono costeiro mais baixo — o teu próprio porto para um embarque em porto, ou qualquer outra terra costeira para um embarque em praia.

Em qualquer dos casos, a frota tem de estar já onde a tabela indica **no início do turno**: o embarque acontece na Pré-Fase 2, antes de qualquer frota zarpar (Fase 6). Uma frota que zarpe para a posição neste turno só pode receber o exército a bordo a partir do **próximo** turno. Depois de um embarque em **porto**, a frota pode zarpar no mesmo turno; uma recolha em **praia** mantém-na fundeada nesse turno (§2.14.6).

> ***▶ Exemplo — de quem são os navios e de quem é o porto.** O teu Army II está no porto do teu aliado em (24,34), e queres levá-lo para casa.*
>
> *• A **Fleet I** do teu aliado está atracada mesmo ali, com espaço de sobra. O **Army II não pode embarcar nela**, e o teu aliado não o pode ordenar — o transporte nunca atravessa uma bandeira.*
>
> *• A tua própria **Fleet III** está atracada no mesmo porto. Um embarque em porto é **recusado** — "Army II and Fleet III are in a port that is not yours" — o exército fica em terra e nada se perde.*
>
> *• **Turno 1:** a Fleet III zarpa para o hexágono de mar ao lado, (24,35). **Turno 2:** o Army II embarca nela por **embarque em praia** no início do turno — uma recolha em praia mantém a frota fundeada nesse turno (§2.14.6, linha 6). **Turno 3:** a Fleet III zarpa com o Army II a bordo.*
>
> *• Se o Army II e a Fleet III estivessem juntos num porto **teu** em (27,31), um embarque em porto teria bastado num único turno — e um embarque em porto não retém a frota, que zarpa nesse mesmo turno.*
>
> *• O caminho inverso está aberto: a Fleet III pode zarpar para o porto do teu aliado com o Army II a bordo e **desembarcá-lo** aí.*

Uma frota que transporta um exército move-se com a frota na Fase 6. Os exércitos não se movem na Fase 5 enquanto estão embarcados.

**Cascos perdidos com um exército a bordo.** Uma frota só pode transportar o que os seus cascos comportam — cada soldado ocupa 1 de tonelagem, um soldado montado 2 — e isso é verificado quando o exército embarca. Se uma batalha naval afundar então **alguns** dos navios da frota, os soldados que os navios sobreviventes não conseguem transportar afogam-se com os cascos afundados. As baixas são repartidas proporcionalmente pelas unidades do exército, o exército é reduzido exatamente ao que os navios restantes comportam, e um cartão diz-te quantos se perderam. Aplica-se por igual ao vencedor, ao vencido e ao empate, depois de quaisquer presas capturadas se terem juntado à frota. O comandante do exército não sofre danos. (Se todos os navios afundarem, o exército inteiro vai ao fundo com a frota.)

> ***▶ Exemplo.** A Fleet I transporta 400 soldados de infantaria e 50 cavaleiros — 500 de tonelagem — em 5 Drommunds (capacidade de 100 cada). Uma batalha afunda 2 deles: restam 300 de capacidade, pelo que 200 de tonelagem têm de se perder. Proporcionalmente, são 40% de cada unidade: afogam-se 160 de infantaria e 20 cavaleiros, e o Army I segue viagem com 240 de infantaria e 30 cavaleiros — exatamente 300 de tonelagem.*

**2.14.6 Desembarque (Disembarkation)**

Quando uma frota com um exército transportado se move para uma posição adjacente a (ou sobre) um hexágono (hex) de terra, o exército pode desembarcar — mas apenas através de uma **ordem explícita \`disembark_army\`** (navegar junto a uma costa não descarrega o exército por si só). **Desembarque no nevoeiro.** O hexágono de desembarque é escolhido junto ao local onde a viagem **termina**, e qualquer um dos hexágonos pode estar por revelar (❔): a Página do Jogador (Player Page) oferece um vizinho em nevoeiro como *Desconhecido (nevoeiro)*, e o terreno real decide no fim da Fase 6. Se um hexágono em nevoeiro na rota se revelar terra sem porto, a frota pára no hexágono anterior (§2.14.1), e um hexágono de desembarque que deixe de ser vizinho da frota falha. Se se revelar um porto, a frota entra no porto, e só pode desembarcar a partir daí se o porto for teu ou de um aliado mútuo. Um hexágono de desembarque em nevoeiro que se revele mar ou costa de montanha é recusado; um que se revele terra é desembarcado segundo as linhas abaixo. Um desembarque recusado deixa o exército a bordo, com um cartão de aviso. **Momento:** o desembarque resolve-se **no fim da Fase 6**, numa passagem separada **depois de todas as frotas — a tua e as inimigas — terem acabado de se mover**, e sempre a partir da posição **final** da frota. Nunca acontece no início do movimento nem a meio do percurso: a frota navega primeiro toda a sua rota, *e só depois* o exército desembarca. **De onde a frota pode desembarcar**: a partir de um **hexágono de mar** (qualquer hexágono de terra adjacente é um alvo válido), ou de um porto pertencente ao **teu próprio reino ou a um aliado mútuo** (o próprio hexágono do porto ou qualquer vizinho). Uma frota atracada num porto **neutro ou inimigo** não pode desembarcar em lado nenhum — navega primeiro para o mar. O embarque tem as suas próprias condições (§2.14.5). O que acontece depende do hexágono-alvo:

|  |  |
|---|---|
| **Hexágono-alvo (Target hex)** | **Resultado** |
| Território próprio ou aliado, livre | O exército desembarca livremente. |
| Território próprio ou aliado, **exército amigo presente** (próprio ou aliado, incl. um exército estacionado na tua capital) | O exército **desembarca ao lado dele** — coabitação, até **3 exércitos por hexágono** (§5.11). Só um hexágono **cheio** (já com 3) bloqueia o desembarque; o exército fica então a bordo. |
| Território próprio ou aliado, **qualquer exército presente que não seja teu nem de um aliado mútuo / suserano / vassalo** — mesmo um em paz contigo, e mesmo com um exército amigo ao lado dele: o desembarque **declara guerra** a esse exército | **Combate de praia** — uma Batalha Anfíbia (Amphibious Battle) (§5.7, penalização de praia ×0.50) contra o intruso. O hexágono **nunca muda de mãos** (estás a recuperar o teu próprio território, ou a libertar o de um aliado); uma força de desembarque repelida volta a embarcar na frota. |
| **Construção com muralhas inimiga** | O **assalto** resolve-se de imediato (§5.6) — sem Batalha Anfíbia quando ninguém está do lado de fora; o exército toma as muralhas de assalto diretamente a partir da praia. Todos os reinos lá dentro, incluindo o teu próprio aliado, são alvo de declaração de guerra (§5.6); os exércitos no exterior enfrentam primeiro o desembarque, na praia, e, se este vencer, as Guarnições atrás das muralhas defendem o assalto que se segue (§5.8.0). **Num hexágono estrangeiro com muralhas, qualquer exército acampado fora das muralhas que não seja teu aliado mútuo, vassalo ou suserano é combatido — em guerra ou em paz — e um amigo acampado ao lado dele não o protege: o teu desembarque só passa por esse terreno até às muralhas quando todos os exércitos no exterior são amigos teus.** O desembarque classifica o acampamento exterior exatamente como uma marcha (§2.13.3), pelo que a rota marítima e a rota terrestre nunca discordam. As muralhas contam como estrangeiras quando pertencem a outro reino que não é teu aliado mútuo, vassalo ou suserano — incluindo as de um neutro: um desembarque que perca ou empate na praia, ou que seja repelido das muralhas, não volta a embarcar mas entrincheira-se do lado de fora (−20, §5.7.2). Muralhas sem dono, e as tuas, as de um aliado, de um vassalo ou de um suserano, seguem as outras linhas. |
| **Terra aberta inimiga ou sem dono com um exército nela** | Resolve-se uma **Batalha Anfíbia** (§5.7) — o atacante sofre uma penalização de desembarque em praia de ×0.50. O exército contra o qual desembarcas defende-se, seja quem for o seu dono — é-lhe declarada guerra — e todos os outros exércitos ali em guerra contigo, ou ligados a ele, defendem ao lado dele; um em paz contigo e sem ligação é um espectador (§5.7). **Um amigo teu nunca é combatido**: desembarcas ao lado dele se o hexágono tiver espaço e tomas o hexágono como se estivesse vazio, ou ficas a bordo se não tiver, com o cartão *"Sem espaço ao lado do exército de X, um amigo teu"*. Vitória → desembarca e toma (um hexágono sem dono também é reivindicado); repelido → volta a embarcar. |
| Terra aberta inimiga, sem defesa | A população luta como **milícia** — uma disputa de WP com a penalização de praia de ×0.50 (mesma resolução que uma tomada de terra, §2.13.4); um hexágono **sem população nenhuma** é simplesmente tomado. Vitória → desembarca e toma; repelido → volta a embarcar na frota (destruída apenas se nenhuma unidade sobreviver ao combate). |
| **Construção com muralhas inimiga, zona exterior já cheia** | Desembarque **bloqueado** — o terreno diante das muralhas já tem 3 exércitos; o exército fica a bordo. |
| **Postura de Marcha de Cerco (Siege March)** sobre um hexágono inimigo com muralhas sem ninguém acampado do lado de fora | Sem combate: o exército desembarca e **acampa às portas** (paga os −20), declarando guerra e **iniciando o cerco** (cerco guardado; o anel fecha-se de imediato se a força for suficiente, progresso a partir do turno seguinte — §5.8.0) — o gémeo marítimo da Marcha de Cerco terrestre (§5.4). |
| Terra aberta sem dono, livre (ou ocupada apenas por um amigo teu com espaço) | A população luta como **milícia**, exatamente como em terra inimiga sem defesa (penalização de praia ×0.50); um hexágono **sem população nenhuma** é simplesmente tomado. Vitória → desembarca e **reivindica-o** — ninguém era dono, pelo que não começa nenhuma guerra e nenhuma bandeira é arriada; repelido → volta a embarcar na frota. |
| **Construção com muralhas sem dono**, livre | O exército desembarca livremente e **não reivindica nada** — muralhas sem dono só se tomam pelo lado de terra, marchando sobre elas (§2.13.3, §5.6). |
| **Hexágono de montanha**, qualquer dono | **Recusado** — penhasco, não costa: nenhum lugar onde encalhar um barco, o gémeo da regra de recolha na praia. O exército fica a bordo e recebe um cartão; a Página do Jogador nunca oferece uma costa de montanha que consiga ver — um hexágono de desembarque **por revelar** (❔) que se revele montanha é recusado da mesma forma. Desembarca num hexágono costeiro mais baixo e marcha para cima. |

**O embarque consome o turno do exército.** Um exército que embarca **não pode também desembarcar nesse mesmo turno** — o Processador de Turnos (Turn Processor) recusa o desembarque com um cartão e as tropas ficam simplesmente a bordo, prontas para desembarcar a partir do turno seguinte. Esta regra não é específica dos portos: abrange **ambas as formas de ir a bordo** descritas abaixo — um exército recolhido na praia fica tão impedido de desembarcar neste turno como um embarcado num porto. O **movimento da própria frota não é afetado pela regra do lado do exército**: num embarque em porto, embarca e navega o que quiseres num só turno; só o desembarque espera (uma recolha na praia retém adicionalmente a própria frota — ver abaixo). Isto é o espelho do reembarque, que sempre teve efeito apenas no início do turno seguinte — cada transição entre terra e navio custa uma fronteira de turno, nos dois sentidos. **Consequência para os defensores**: uma frota de invasão tem de passar pelo menos um turno visivelmente no mar (ou ao largo da tua costa) antes de as suas tropas poderem atingir a praia — o ataque de embarcar-navegar-desembarcar num único turno não existe.

> ***⚠ Ordem — porque é que um hexágono "seguro" pode ainda cair neste turno.** O combate terrestre (Fase 5) resolve-se **antes** da marinha (Fase 6). Um hexágono costeiro sobre o qual nenhum exército marchou na Fase 5 não está seguro durante o turno: uma frota inimiga que tenha levado um exército para junto dele pode desembarcar e tomá-lo na Fase 6, depois de a tua fase terrestre já ter acabado. Defender um hexágono costeiro contra isto significa uma de duas coisas — **negar o mar** (uma frota de bloqueio ou de escolta para afundar ou deter a deles antes de chegarem à costa), ou **manter o hexágono com um exército verdadeiro** (então o desembarque resolve-se como uma Batalha Anfíbia contra o teu exército, §5.7, e não como uma disputa unilateral de milícia). A milícia sozinha, com a penalização de praia de ×0.50, muitas vezes não chega.*
>
> ***Voltar a pôr no mar um exército desembarcado — duas formas de ir a bordo.** Depois de um exército ter desembarcado, é um **exército terrestre normal**, e há duas formas de o reembarcar:*
>
> *- **Só as tuas próprias frotas transportam os teus exércitos** (ambas as portas abaixo): nunca a frota de um aliado, embora a tua própria frota possa desembarcar o teu exército num porto de um aliado (§2.14.5).*
>
> *- **Escolher a frota.** Quando mais de uma frota pode levar o exército — duas atracadas no porto, ou uma atracada e outra ao largo, ancorada num hexágono de mar vizinho — o cartão do exército pergunta **qual**, e indica o preço de cada porta: um embarque atracado custa ao exército −5 de prontidão (readiness) e nada à frota; uma recolha a uma frota ancorada ao largo custa também −15 a essa frota.*
>
> *- **Embarque em porto**: o exército tem de estar **num dos teus próprios portos, com uma das tuas próprias frotas atracada lá** (§2.14.5) — e emites uma **ordem `embark_army`**, que se aplica de novo no **início do turno seguinte** (Pré-Fase 2, §2.6). A frota embarcada ainda pode navegar nesse mesmo turno.*
>
> *- **Novas frotas não transportam nada no primeiro turno.** O embarque volta a aplicar-se no **início** do turno (Pré-Fase 2), mas os navios só são encomendados na **Fase 4** — por isso uma frota criada neste turno, ou uma cujos navios foram todos ordenados neste turno, **não tem cascos quando o embarque se resolve**, e o embarque é recusado (cartão "encomendado neste turno"). A Página do Jogador bloqueia a ordem à partida pelo mesmo motivo. O processo que funciona leva dois turnos: **turno N** criar a frota e construir os seus navios; **turno N+1** embarcar — e a frota ainda pode navegar nesse mesmo turno. A capacidade segue o mesmo relógio: só os navios que existiam no início do turno contam para o que um exército pode embarcar neste turno.*
>
> *- **Embarque na praia**: o exército embarca numa das tuas próprias frotas **ancorada ao largo num hexágono de mar adjacente** — não é preciso porto. Emite **`embark_army` com `beach:true`**; aplica-se na **mesma passagem da Pré-Fase 2** que o embarque em porto, antes de o combate da Fase 5 correr (ambos os caminhos partilham um só tipo de ordem e uma só condição de ARMY LINK — um exército ligado não pode embarcar de nenhuma das formas; faz UNLINK primeiro, §5.11). O lado da **frota** também tem condições: uma frota num grupo **FLEET LINK** (líder ou membro) também não pode aguardar uma recolha na praia — faz UNLINK da frota primeiro, §2.14.7. **Não há condição de propriedade, cerco ou postura diplomática no hexágono de origem** — a recolha funciona a partir do teu próprio território, do de um aliado, do de um neutro, ou diretamente de território hostil que estejas a ocupar, em paz ou em guerra, cercado ou não. Há exatamente **um terreno que a recusa: `mountain`**. Uma costa de montanha é penhasco, não costa de praia — não há lugar onde encalhar um barco — por isso um exército parado num hexágono de montanha não pode ser recolhido por mais perto que a frota esteja ancorada. Marcha-o primeiro para um hexágono costeiro mais baixo. (Isto afeta apenas o caminho da praia: não se pode construir um porto numa montanha, pelo que o embarque em porto não é afetado.) Uma recolha recusada **não custa estado** a nenhum dos lados. **Atenção à assimetria — a estrada marítima para uma montanha tem sentido único.** Nada te impede de desembarcar um exército numa costa de montanha; só a recolha é recusada. Um exército posto em terra aí **não pode ser retirado outra vez por mar**: tem de marchar primeiro para um hexágono mais baixo, e numa costa de montanha isolada, sem terra amiga para onde marchar, fica encalhado para sempre. Não uses uma montanha como cabeça de praia. A contrapartida é o turno inteiro da frota: **carregar em mar aberto consome o movimento da frota** — a sua ordem de navegação da Fase 6 é recusada (cartão "retida para uma recolha na praia") e só volta a navegar no turno seguinte — além da regra partilhada de não desembarcar no mesmo turno acima. Toda a recusa tem cartão, nunca é silenciosa: a frota não está ancorada vazia num hexágono de mar, os dois não são vizinhos, outro exército já tem a retenção, a tonelagem do exército excede a capacidade da frota, o exército já está a bordo de outra frota, a frota está num grupo de ligação, ou o exército está numa montanha. Estado: exército **−5**, frota **−15** (§5.10.2, §5.10.6).*
>
> ***⚠ A porta que usaste é decidida por onde está a FROTA, não por onde está o EXÉRCITO.** Estar no teu hexágono de porto não faz dele um embarque em porto. Se o casco a que embarcas está ancorado num **hexágono de mar** em vez de atracado no porto, é uma **recolha na praia** em todos os aspetos — incluindo os dois que surpreendem as pessoas: **essa frota perde o seu turno** (a sua ordem de navegação é recusada) e paga o **−15 de estado da frota** adicional pela carga em mar aberto. A tua Página do Jogador di-lo no painel de embarque antes de clicares, nomeando a frota, **o hexágono de mar em que está ancorada** e o custo em estado. Lê essa coordenada, não o porto de origem da frota: o porto de origem de uma frota é apenas o **último porto em que atracou** (de qualquer dono; limpo se for forçada a fugir de um porto), pelo que "porto de origem: a tua capital" não diz nada sobre onde o navio está hoje. Se queres embarcar e navegar no mesmo turno, a frota tem de estar realmente **atracada no porto** com o teu exército nesse mesmo hexágono.*
>
> ***Consequência:** um exército desembarcado bem dentro de território hostil não fica automaticamente encalhado — uma frota de escolta ancorada ao alcance da cabeça de praia pode retirar o exército no turno seguinte, independentemente de quem detém o terreno. O que continua a encalhá-lo é a ausência dessa frota: sem casco teu ancorado adjacente (ou atracado num porto alcançável) e sem terra amiga para onde recuar, uma batalha perdida ainda **destrói o exército onde está**. Planeia a frota de extração antes de planeares o desembarque. Um exército derrotado nunca se retira para um navio a meio da batalha (a retirada é só terrestre, §5.5) — embarcar é sempre uma ordem deliberada, nunca uma fuga automática.*
>
> ***⚠ O que isto significa — embarcar é tudo ou nada.** Enquanto um exército está a bordo de uma frota, não pode mover-se por si, recrutar, cercar, dissolver, despedir unidades (§2.6), nem dividir-se (§2.12b), e partilha por completo o destino da frota. Se essa frota for afundada em combate naval — ou afundada de propósito quando morre o seu último navio — **o exército embarcado é destruído de imediato**: sem sobreviventes, sem nadar até à costa, sem encalhar na costa mais próxima. Uma batalha naval perdida pode apagar toda a tua força de invasão. Nunca navegues o teu exército principal por águas que uma frota inimiga possa alcançar sem uma escolta combatente, e lembra-te de que uma costa defendida acrescenta a penalização de desembarque em praia por cima (§5.7).*

**▶ Exemplo (Example) — um turno, o que cabe.** A sequência que decide tudo é fixa: **embarque na Pré-Fase 2 → exércitos movem-se na Fase 5 → frotas movem-se na Fase 6 → desembarques no fim da Fase 6.** Nada permite que um exército mude de posição em terra e mude de navio no mesmo turno; toda a combinação que o tente é um ❌ abaixo.

|  |  |  |  |
|---|---|---|---|
| **\#** | **Combinação num SÓ turno** | **Possível?** | **O que realmente acontece** |
| 1 | Embarque em porto **+ a frota navega** | ✅ | O exército embarca no início do turno, a frota leva-o por toda a rota. |
| 2 | Embarque em porto **+ a frota navega + desembarque** no destino | ❌ desembarque | O exército embarca, a frota navega, o desembarque é **recusado** ("tropas ainda a arrumar a bordo") — fica a bordo no hexágono final da frota e desembarca no turno seguinte. |
| 3 | Embarque em porto **+ ordem de movimento do exército** | ❌ | O exército está a bordo desde a Pré-Fase 2; a sua própria marcha nunca corre (a Página do Jogador bloqueia a ordem à partida). |
| 4 | **O exército marcha até ao porto + embarca** | ❌ | O embarque lê o hexágono do exército no **início do turno**. Turno N marcha, turno N+1 embarca (e navega). |
| 5 | **A frota navega para o porto + o exército embarca** | ❌ | O espelho: a frota tem de estar já atracada ou ancorada no início do turno. Turno N navega para dentro, turno N+1 embarca (e navega para fora). |
| 6 | Recolha na praia **+ a frota navega** | ❌ frota | O exército embarca a partir da costa adjacente; a ordem de navegação da frota é **recusada** — fica ancorada neste turno e paga −15 de estado. |
| 7 | Recolha na praia **+ desembarque** | ❌ ambos | Frota retida **e** desembarque recusado. Nada de útil acontece. |
| 8 | **A frota navega + desembarque** (exército embarcado num turno anterior) | ✅ | O movimento de invasão: a frota completa a sua rota e depois descarrega a partir da sua posição **final** para qualquer hexágono de terra adjacente — ou, se terminar atracada num porto **próprio ou aliado**, para esse hexágono de porto ou qualquer vizinho. A partir de um porto neutro ou inimigo: sem desembarque. |
| 9 | Desembarque **+ movimento do exército** | ❌ | O desembarque é a última coisa na Fase 6; a Fase 5 já acabou. O exército fica onde desembarcou e marcha no turno **seguinte**. |
| 10 | Desembarque **a meio da rota**, a frota continua | ❌ | Os desembarques só acontecem a partir do hexágono final. Termina a rota onde queres a praia. |
| 11 | Desembarque **+ reembarque** (praia ou porto) | ❌ | O embarque é, no mínimo, a Pré-Fase 2 do turno seguinte. Desembarca, espera um turno, depois embarca. |
| 12 | Exército a bordo, **a frota navega, sem desembarque** | ✅ | O exército viaja a bordo, todos os turnos se quiseres — o seu estado fica congelado enquanto está a bordo (§5.10.2). |
| 13 | Exército a bordo, a frota **combate no mar** antes do desembarque | — | Se a frota sobreviver, o desembarque ainda se resolve a partir do seu hexágono final; se for afundada ou afundada de propósito, o exército é **destruído de imediato**. |
| 14 | Desembarque em terreno próprio/aliado **que já tem um exército amigo** | ✅ | Desembarca ao lado — até **3 exércitos por hexágono** (§5.11); só um hexágono cheio o bloqueia. |
| 15 | Desembarque num hexágono inimigo com muralhas — defensor em **qualquer** postura | — | Todos os reinos dentro das muralhas são alvo de declaração de guerra (§5.6); lá dentro só há uma Guarnição (§5.8.0). Qualquer exército acampado **no exterior** que não seja teu nem de um aliado mútuo / suserano / vassalo — incluindo os exércitos do dono que não estão em Guarnição e um **neutro** — é combatido primeiro, a céu aberto (combate de praia normal, sem bónus de fortaleza; é declarada guerra); se o **venceres**, o desembarque assalta as muralhas na mesma fase; um acampado **aliado** é deixado em paz. Com a praia livre, o desembarque assalta a Guarnição lá dentro (§5.8); um sobrevivente repelido **não** volta a embarcar — descarrega numa **cabeça de praia fora das muralhas** (−20 de estado), e o mesmo acontece com um desembarque que perca ou empate o combate de praia no exterior. |
| 16 | Embarque por um exército **ligado**, ou recolha por uma frota **ligada** | ❌ | Recusado — faz UNLINK primeiro (§5.11, §2.14.7). |
| 17 | Embarque numa frota **criada ou totalmente construída neste turno** | ❌ | Recusado — os navios são encomendados na Fase 4, o embarque é na Pré-Fase 2. Turno N criar + construir, turno N+1 embarcar + navegar. |
| 18 | O exército move-se para terra **e** a sua própria frota navega, sem relação | ✅ | Ordens independentes. |

Os circuitos legais mais rápidos: **invasão a partir de casa** — T1 criar frota + construir navios → T2 embarcar + navegar → T3 navegar + desembarcar → T4 o exército marcha; **extração de uma praia hostil** — T1 a frota ancora adjacente → T2 recolha na praia (frota retida, exército embarca) → T3 navegar (e desembarcar noutro lado).

**2.14.7 Grupos de Ligação de Frotas (Fleet Link Groups)**

As frotas amigas que partilham um hexágono (hex) podem **ligar-se** num único grupo que navega, combate, faz incursões e bloqueia como um só — o gémeo naval dos grupos de ligação de exércitos (§5.11). Uma frota é a **nau-capitânia** (flagship); as outras navegam sob o seu comando.

- **Formar uma ligação.** Termina um turno no mesmo hexágono de outra frota tua, ou de um aliado mútuo, e usa o painel ⛓ Fleet Link no cartão da frota. Ligar as tuas frotas **próprias** forma o grupo de imediato. Propor a um **aliado** envia uma oferta — o grupo forma-se quando o aliado submete um LINK ACCEPT (um aperto de mão no mesmo turno funciona, ou o aliado aceita a oferta pendente num turno posterior). Um grupo tem no máximo **3 frotas** (o limite de coabitação).

- **Navegar como um só.** Só a ordem de movimento da **nau-capitânia** conduz o grupo; a ordem de movimento própria de uma frota ligada é ignorada — por isso a página nunca deixa uma rota em fila e uma ligação **coexistir**: não podes ligar uma frota que tenha uma rota planeada, e não podes retirar um UNLINK em fila — ou uma *libertação* em fila de um membro — enquanto a frota libertada ainda tiver uma rota; limpa primeiro a rota. Também uma nau-capitânia com uma rota planeada não pode levar para o grupo uma frota **mais lenta** — encurta primeiro a rota para o novo ritmo. Um grupo de frotas formado partilha igualmente os cascos, a prontidão e o comandante de cada membro com todos os seus membros. O grupo navega ao ritmo do **casco mais lento da frota mais lenta** — e a caixa de Movimento da nau-capitânia orça nesse mesmo ritmo de grupo (assinalado como *⛓ group pace*), pelo que a rota que podes planear é a rota que o comboio vai realmente navegar — e os seus membros seguem para o hexágono da nau-capitânia. A prontidão (estado) **nivela pelo mais baixo do grupo** em cada turno — um grupo atracado descansa primeiro e depois sincroniza para baixo, até ao mais fraco.

- **Ofensiva combinada.** Quando a nau-capitânia navega para um hexágono ocupado pelo inimigo, **todo o grupo combate** como uma só força, somando cada frota o seu próprio poder de guerra. **Juntar-se a uma ligação é um compromisso**: a nau-capitânia aponta o grupo para onde quiser, e todos os membros combatem aí — **mesmo contra um reino com o qual esse membro esteja em paz ou aliado.** Combater significa guerra, pelo que um membro assim comprometido é **declarado em guerra** com o alvo da nau-capitânia, e uma aliança existente com esse alvo é **quebrada**. O mesmo vale quando o grupo já se encontra num porto ou no mar junto a uma frota inimiga no início do turno: se o reino da nau-capitânia está em guerra com essa frota, todo o grupo combate o choque pré-movimento; se apenas o reino de um membro o está, esse membro combate e a nau-capitânia fica de fora. Se o ataque falhar ou terminar em empate, o grupo dispersa-se; um membro que nunca navegou até ao hexágono da batalha mantém-se onde está, e o seu cartão di-lo. **Um membro transportado para o hexágono final da nau-capitânia que esteja em guerra com uma frota já lá presente ataca-a à chegada**: a frota já presente defende, só combatem as frotas transportadas que estejam em guerra com ela — a nau-capitânia fica de fora — não há Emboscada (Ambush) no mar, e um membro derrotado dispersa todo o grupo e **recua para o hexágono de onde a sua nau-capitânia veio no último passo** — ou, se esse hexágono estiver fechado para ele, o refúgio mais próximo a partir daí — nunca para onde a viagem começou; o cartão da nau-capitânia nomeia a frota do seu grupo que foi derrotada. Uma frota membro de outro reino também recebe cartão quando a sua nau-capitânia é detida por falta de espaço. Não te ligues sob uma nau-capitânia cujos combates não estejas disposto a partilhar — onde quer que ataque, defenda ou bloqueie, o teu reino entra em guerra com esse inimigo (ligar-se sob uma nau-capitânia que está apenas em guerra não declara nada); desliga-te primeiro se te opuseres ao alvo.

- **A defesa arrasta o grupo, a qualquer preço** (paridade com o exército — §5.11). **As frotas já presentes no hexágono juntam-se também a um ataque**, nos termos terrestres (§2.13.5) — incluindo o ataque à chegada de uma frota transportada. Quando a *nau-capitânia* é atacada, todas as frotas ligadas sob ela combatem a seu lado — mesmo uma que esteja **em paz** com o atacante, a qual fica assim **declarada em guerra** com ele: a ligação é consentimento. Isto vale também para o aliado, vassalo ou suserano do próprio atacante: combate ao lado da sua nau-capitânia e a aliança quebra-se. Uma frota coabitante *fora* da ligação só se junta se já estiver em guerra com o atacante — e não em guerra com o reino da nau-capitânia nem com outro defensor, incluindo os seus membros de ligação. Se a nau-capitânia perder, o grupo dispersa-se e o cartão de cada membro nomeia a batalha (formulação do §5.11). **Um reino nunca combate em ambos os lados de uma mesma batalha naval**: a tua frota na defesa fica à parte, com o cartão *"held back"* (§5.11.1).

- **Incursão e bloqueio de grupo.** Um grupo faz **uma só** incursão a um porto, com o poder **somado** dos membros (não uma por frota), e **todas** as frotas do grupo pagam o custo de prontidão da incursão (§5.10.6). Um **bloqueio** de grupo suprime o porto uma vez, e **todas** as frotas do grupo pagam a manutenção de prontidão do bloqueio — e são parte dele: um membro cujo reino ainda não está em guerra com o dono do porto é **declarado em guerra** com ele nesse turno, terminando qualquer aliança entre ambos (a ligação é consentimento, exatamente como quando o grupo é atacado), e recebe o cartão *"Fleet N joined a blockade"*; um reino cobrado por essa guerra não é cobrado de novo pelo choque no porto nesse mesmo turno — nem em qualquer outro porto do mesmo dono que as suas frotas bloqueiem nesse turno. A guerra é declarada depois de o rendimento da Fase 1 estar liquidado, pelo que um pacto entre os dois reinos paga a ambos ou a nenhum nesse turno, e conta como uma guerra iniciada neste turno — nenhuma aliança lhe pode responder até ao próximo turno (§8). **Ambas as Páginas do Jogador avisam**: o Bloqueio da nau-capitânia nomeia as frotas ligadas de outros reinos que colocaria em guerra, e uma frota ligada sob uma nau-capitânia em bloqueio diz que o seu reino estará em guerra com o dono do porto, nomeando uma aliança — ou uma vassalagem — que terminaria — desliga-te para ficares à parte. **E antes de te ligares sequer**: uma oferta de ligação de frotas de uma nau-capitânia que terminou o último turno mantendo um Bloqueio num porto inimigo di-lo — no cartão de relatório da oferta e junto a **✓ Accept**: *"Accepting while it holds makes your realm a party to it — declared at war with \<owner\> this turn"*, acrescentando *"ending your alliance with \<owner\>"* quando o teu reino é aliado mútuo do dono do porto — ou *"ending the vassalage between you and \<owner\>"* quando é o suserano ou vassalo do dono, visto que a guerra termina a vassalagem (§2.16.4); uma aliança que apenas propuseste, e que o dono nunca aceitou, não conta (as ofertas são liquidadas antes da Fase 1, pelo que a guerra chega no turno em que aceitas, se o bloqueio ainda se mantiver; um reino já em guerra com o dono do porto é apenas lembrado). Toda a oferta de ligação de frotas traz a nota *"A link is consent: wherever the flagship fights or blockades, your fleet goes with it — and your realm is declared at war with that enemy"*. Esse é todo o compromisso: ligar-se sob uma nau-capitânia que está apenas em guerra com alguém, e que nem combate nem bloqueia essa parte, não declara nada. Uma nau-capitânia em Bloqueio num porto inimigo mostra um aviso no fundo do seu painel Fleet Link — enquanto oferece um Propose a aliados, e mesmo depois de a proposta estar em fila — de que um reino que aceite a sua ligação é declarado em guerra com o dono do porto. O aviso da oferta lê a postura da nau-capitânia no fim do turno em que o teu relatório foi escrito: uma nau-capitânia que ative o Bloqueio no mesmo turno em que aceitas só está coberta pela nota de consentimento. A ordem de incursão/bloqueio própria de um membro é ignorada — a nau-capitânia age pelo grupo.

- **Sair.** Qualquer membro pode fazer **UNLINK** para voltar a agir de forma independente (no mesmo turno). A nau-capitânia pode **libertar** (release) um membro específico ou **dissolver** (dissolve) todo o grupo. O cartão da nau-capitânia mostra apenas o que ainda é possível: depois de uma **dissolução** estar em fila, os botões Release e Dissolve desaparecem e o cartão diz "Queued: DISSOLVE GROUP" com um Cancel; um membro libertado perde o seu botão Release e é listado como "Queued: RELEASE F N"; libertar o **último** membro é registado como uma dissolução (o motor dissolve de qualquer forma um grupo de um); e uma Dissolve ordenada sobre libertações pendentes absorve-as em vez de ser recusada — a menos que um membro libertado já tenha planeado uma rota sob essa libertação, caso em que a página pede que limpes primeiro essa rota (a mesma regra que protege o cancelamento de uma libertação). A lista de membros e o teste do "último membro" leem o grupo tal como o Processador de Turnos o reporta, não as marcas dos hexágonos. O cartão do exército comporta-se da mesma maneira. Uma derrota em batalha **dispersa** o grupo e quebra a ligação; o mesmo acontece ao perder a nau-capitânia. E uma ligação **não pode sobreviver à relação em que foi construída**: guerra, uma aliança terminada ou uma fidelidade renunciada libertam o membro no **fim desse turno**, com cartão para ambos os lados — a regra do exército, nau-capitânia ↔ membro (§5.11 *Command*).

**2.14.8 Mapas circulares (wrapped) (por mapa)**

Um mapa pode declarar que as suas margens opostas se tocam — **este↔oeste**, **norte↔sul**, ou ambas. É uma propriedade do **mapa**, definida pelo GM nas *Map Settings* do Editor de Mapas e levada com a exportação para a campanha; todas as páginas a leem do seu relatório, pelo que um mapa que nada diga sobre circularidade é exatamente o mapa de margens rígidas que conheces. Num eixo circular não há margem nem canto: todo o hexágono tem seis vizinhos, um hexágono de margem pede emprestados os que lhe faltam ao lado oposto, e com ambos os eixos ativos um hexágono de canto fica a um passo do canto oposto.

O que muda num eixo circular, e só aí:

|               |                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | **Eixo circular**                                                                                                                                                |
| **Movimento** | Um salto através da costura (seam) é um hexágono vulgar; a rota que planeias mostra os hexágonos da margem oposta como próximos saltos.                           |
| **Distâncias** | O custo e a probabilidade de perda de espiões, o trânsito de caravanas e qualquer alcance são medidos pelo caminho mais curto (§2.8.2, §2.15). Nada num mapa circular fica mais longe do que metade do mapa. |
| **Classe de mar** | Um hexágono de mar na antiga margem que toque em terra através da costura é **costeiro**, não alto mar (§5.10.6).                                              |
| **Fronteiras** | Reinos em margens opostas são vizinhos para pactos comerciais e guerra.                                                                                          |
| **Defesa**    | Os hexágonos de margem e de canto perdem a vantagem das 4 e 3 abordagens que têm num mapa de margens rígidas — todo o hexágono tem seis abordagens.               |

**Norte↔sul exige um número par de linhas.** As linhas de hexágonos alternam o seu desvio, pelo que dar a volta às linhas só encaixa quando a contagem é par; numa contagem ímpar a costura seria de sentido único (poderias marchar através dela e não voltar). O Editor de Mapas recusa exportá-lo, o Processador de Turnos recusa processá-lo, e o validador de estado assinala-o — o sinal simplesmente não pode chegar a uma campanha nesse estado. Este↔oeste não tem tal limite.

**Campanhas em curso** podem ser convertidas com tools/set_map_wrap.mjs, aplicado entre dois processamentos de turno; a partir do turno seguinte processado o mapa navega circular e os seus relatórios levam a marca a todas as páginas. Espera que as consequências estratégicas acima se façam sentir de imediato em todos. A ferramenta faz uma cópia de segurança do ficheiro de estado antes de escrever, e voltar a executá-la nunca substitui essa cópia — as execuções seguintes usam \_2, \_3…

**2.14.9 Caça Pirata (Pirate Hunt)**

Só a frota de um reino **Pirata** pode adotar a postura de **Caça** (Hunt) — uma frota isolada, ou uma nau-capitânia de ligação cujo grupo inteiro seja seu. A Caça mantém-se ativa turno após turno — também num turno em que não envies ordens, e enquanto a frota navega — até escolheres outra postura. Qualquer outra frota que ordene Caça é recusada, é informada do motivo num cartão, e navega normalmente; uma Caça guardada que se torne impossível (por exemplo quando a frota de um aliado se junta ao grupo) termina, e um cartão diz porquê.

**Quando ataca.** Uma frota caçadora ataca quando **navega para** um hexágono que contém um alvo, quando um alvo **navega para** o seu hexágono, ou quando um alvo **partilha o seu hexágono** quando o movimento termina. Um alvo é uma frota de qualquer reino que não esteja em guerra contigo e não seja o teu aliado mútuo, vassalo ou suserano — um pacto comercial não a protege — a menos que essa frota se encontre **no seu próprio porto**. Quando uma frota navega para o hexágono de um caçador, o caçador julga apenas o reino dessa frota. Uma frota atracada como convidada no porto de um reino Pirata não está no seu próprio porto: pode ser caçada aí, e o caçador combate com o seu bónus de porto de origem — a Página do Jogador avisa quando planeias uma viagem para um deles.

**O teste do Poder de Guerra.** O caçador compara o seu lado (ele próprio e os seus membros de ligação no hexágono) com o lado do reino-alvo (todas as frotas desse reino no hexágono, mais as frotas ligadas a elas que poderiam elas próprias ser caçadas — nunca a tua própria frota, a do teu aliado, vassalo ou suserano, nem a de um reino em guerra contigo: essas ficam fora do combate e nada perdem — mas se o grupo em que navegam for derrotado e se dispersar, a sua ligação a esse grupo quebra-se, como após qualquer batalha naval), cada frota ao seu Poder de Guerra de batalha completo — efetivo, estado, almirante, conveses cheios, marinharia, porto — sem sorte nem iniciativa. Só ataca quando o seu Poder de Guerra é **estritamente superior**. Com vários reinos-alvo no hexágono, ataca o mais forte que ainda supere em poder de fogo. Dois Piratas caçadores num hexágono: só o mais forte ataca; se forem iguais, nenhum o faz.

**A batalha.** Uma batalha naval vulgar — sorte, iniciativa, baixas, retirada, navios-presa e a opinião de vitória/derrota aplicam-se todas — exceto que nenhuma guerra é declarada, ninguém paga penalização de agressor, e só combatem o lado do caçador e o lado do reino-alvo; todas as outras frotas no hexágono assistem. Ambos os reinos mantêm a relação que tinham. Um exército a bordo de uma frota afundada numa caça perde-se no mar da mesma forma — não é preciso guerra para isso. O cartão do caçador nomeia ambos os Poderes de Guerra; o cartão da vítima diz que continua em paz e pode declarar guerra.

**Limites.** Um ataque de caça por frota por turno, qualquer que seja o resultado. Uma caça travada num hexágono só termina o movimento do caçador aí se a vitória não tiver sido clara (§2.14.2): um caçador que afunda ou repele a presa com cascos de sobra segue pelos saltos restantes, qualquer que tenha sido aquele em que navegou para dentro; uma presa que bate claramente o seu caçador também segue. Uma frota que travou qualquer batalha de guerra neste turno — a atacar, a defender ou num choque — não caça; mas uma frota que travou uma pode ainda ser caçada no mesmo turno (uma frota maltratada é exatamente o que um pirata espera). Um caçador só navega para um hexágono em que tenha espaço para entrar (§2.14.2).

**Estado.** Uma frota caçadora está em posição: perde FLEET_STATUS_HUNT_UPKEEP de estado em cada turno e nunca descansa — atracada ou fundeada, a navegar ou não — e os seus membros de ligação partilham-no. Uma caça longa desgasta a frota, e uma frota desgastada julga menos alvos como mais fracos.

**2.15 Fase 7 — Espionagem (Espionage)**

Os jogadores submetem ordens hire_spy especificando um hexágono-alvo. O TP lê a estatística de Política do Mestre de Espiões (Spymaster) atribuído a partir do estado do servidor — a estatística embutida na ordem é ignorada — e gera um relatório de informações para esse hexágono usando as posições finais dos exércitos após a Fase 5.

**Custo**: aumenta com a distância — min(200, 15 + 15 × dist) ouro, onde dist é a distância em hexágonos do teu **hexágono próprio mais próximo** até ao alvo. O reconhecimento de fronteira é barato (próprio/adjacente ≈ 15–30g); o reconhecimento profundo em território inimigo é caro (até ao limite de 200g). \**Limite: 3 missões de espionagem por turno — e só as missões* despachadas *(pagas) contam para ele:*\* uma missão recusada por falta de ouro não é despachada, não cobra nada, e liberta a sua vaga para a missão seguinte nas tuas ordens. Tanto o custo como o limite são autoritativos do servidor — o Processador de Turnos recalcula-os e ignora qualquer valor embutido na ordem.

**Risco — o agente pode não voltar.** Toda a missão terrestre traz uma probabilidade de perda na mesma curva do custo: min(20%, 5% + 1.5% × dist). À tua porta isso dá 5%; o reconhecimento profundo atinge o teto de 20%. Um agente perdido custa-te o ouro e não traz nada de volta. A Página do Jogador mostra a percentagem exata junto ao preço antes de te comprometeres.

**Água.** Os espiões trabalham em terra. Uma missão para um hexágono de mar é cobrada por inteiro e devolve o mesmo cartão de "agente perdido" que qualquer outra falha — deliberadamente. Sob nevoeiro não consegues distinguir água de terra antes de te comprometeres, e se um alvo marítimo produzisse uma resposta distintiva, um jogador poderia mapear todas as ilhas e linhas costeiras simplesmente variando as coordenadas dos espiões. Pela mesma razão o cartão de perda nunca nomeia quem apanhou o teu agente: quer se tenha afogado, quer tenha sido apanhado por um Mestre de Espiões (§8.8.5), quer tenha desaparecido na estrada, o relatório lê-se igual — *"Agent lost at (c,r) — no report recovered."* Nomear o captor confirmaria quem é dono do hexágono e que executa contraespionagem. O **defensor** continua a saber exatamente de quem era o agente que apanhou, e o registo do GM guarda todas as causas por inteiro. **O silêncio não é prova.**

**Povoações — muralhas, nunca nomes.** Num hexágono com uma construção, o relatório traz uma linha 🧱 **Fortifications**: os **pontos atuais** da muralha (esbatidos como qualquer outra estimativa, e ainda mais corrompidos pela contraespionagem) contra o seu **máximo exato** — ou *"None — an open settlement"* quando a povoação não constrói muralhas (revelador em si mesmo: as povoações Orc de nível baixo e as aldeias Genéricas combatem sem muralhas). O relatório **deliberadamente nunca nomeia a família nem o nível da povoação** — nada de "FNO5". Um mestre de espiões traz-te números; a dedução é tua: a estimativa de população, o máximo da muralha e a raça do dono estreitam o nível da povoação face às escadas completas no §3.7.1a, e o valor da muralha alimenta diretamente a aritmética das máquinas de cerco (§5.8.6).

> ***▶ Exemplo — ler um relatório sobre uma metrópole Imperial.** Um mestre de espiões de nível médio (Política 60, ±15%) explora uma FI20 com guarnição cuja muralha foi bombardeada até uns reais 21,300 de 25,000:*
>
> *\| \| \| \|*
>
> *\|---\|---\|---\|*
>
> *\| 👥 \| **Population** \| ~46,700 people \|*
>
> *\| 🧱 \| **Fortifications** \| ~19,900 / 25,000 wall points \|*
>
> *\| ⚓ \| **Port** \| Level 2 (estimated) \|*
>
> *\| ⚔ \| **Enemy Forces** \| Empire of Dellinca Army II — ~3,150 troops \|*
>
> *\| 🎖 \| **Commander** \| Marcus Aurelius Drusus \|*
>
> *\| 🔍 \| **Assessment** \| A formidable defensive force \|*
>
> *\| 🏴 \| **Controlled by** \| Empire of Dellinca \|*
>
> *O nível nunca é indicado, mas é dedutível: os máximos de muralha Imperial no topo da escada são 5,000 / 10,000 / 15,000 / 20,000 / **25,000** (FI16–FI20), pelo que o máximo exato mais a raça do dono fixam isto como uma **FI20** sem margem para dúvida — e ~46,700 pessoas corrobora-o, pois só a FI20 comporta 50,000. O valor atual é a parte acionável: "cerca de 20,000 de pé" diz a um sitiador com um comboio completo de dez máquinas (2,500 de dano de muralha por turno, §5.8.6) que uma brecha está a cerca de oito turnos de bombardeamento — e diz a quem pretende assaltar que bónus de fortaleza as muralhas ainda pagam. Um mestre de espiões de elite (Política \> 75) aperta as estimativas para ±5%; com ≤ 50 esborratam-se para ±30%. O máximo mantém-se exato em todos os casos.*

**A exatidão do relatório** depende da estatística de Política do mestre de espiões:

|              |              |                                      |                                                                     |
|--------------|--------------|--------------------------------------|---------------------------------------------------------------------|
| **Política** | **Variação** | **Exatidão do Nível do Local**       | **Detalhes das Tropas**                                             |
| \> 75        | ±5%          | Nível exato                          | ~±5%; comandante mostrado (linha explícita "none" se não atribuído) |
| \> 50        | ±15%         | ±1 nível (estimado)                  | ~±15%; **nome** do comandante mostrado                              |
| ≤ 50         | ±30%         | 40% de probabilidade de falhar o local por completo | ~±30%; 25% de probabilidade de um **avistamento fantasma falso** num hexágono *vazio* |

Fórmula de variação: vary(v) = max(1, round(v × (1 − variance + rand×variance×2))) — por exemplo, uma contagem verdadeira de 100 com ±15% reporta algo entre **85–115**; com ±30%, **70–130**.

> ***Duas coisas que esta tabela facilmente se leem mal:** **(1)** o nome do comandante é visível a partir do **nível médio (Política \> 50)**. **(2)** Um mau mestre de espiões nunca esconde um exército real — só a contraespionagem (§8.8.5) ou uma Emboscada válida (§5.4) o faz; a sua falha é o oposto, uma probabilidade de 25% de **falso alarme** em terreno realmente vazio ("possible troop movement, unconfirmed"). Por isso desconfia de um avistamento de Política baixa em terreno aberto; nunca desconfies de um silêncio de Política baixa.*

**Quem o relatório nomeia, e como.** Todo o exército estrangeiro no hexágono tem a sua própria linha com a sua relação real contigo: 🤝 **Allied Forces** (aliado mútuo, vassalo ou suserano), 🏳 **Neutral Forces** (nem aliado nem em guerra — um parceiro comercial ou um estranho) ou ⚔ **Enemy Forces** (em guerra contigo); um hexágono vazio lê *"No foreign forces observed"*. A contraespionagem esbate e elimina **todas** estas linhas por igual — o exército de um aliado não é mais fácil de ler num hexágono vigiado. Espiar o **teu próprio** hexágono não encontra contraespionagem nem penalização de território Elfo: o teu Mestre de Espiões nunca trabalha contra o teu próprio agente. Um exército em **Emboscada** válida é invisível aos espiões (tabela de posturas, §5.4).

O TP ignora state.spies dos ficheiros de jogador submetidos. Os registos de espiões são relatórios históricos, não unidades ativas no mapa. Toda a ordem hire_spy é um pedido de informações pontual, sem presença persistente nem manutenção.

**2.16 Fase 8 — Diplomacia (Diplomacy)**

**2.16.1 Posturas Diplomáticas (Diplomatic Stances)**

|            |                                                                                                                                                                                      |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stance** | **Descrição**                                                                                                                                                                        |
| peace      | Predefinição. Sem combate, sem bónus.                                                                                                                                                |
| war        | Combate ativado. Declarada automaticamente por ação militar — contacto entre exércitos, uma batalha de frotas, uma incursão a um porto, o ataque ou defesa de um grupo ligado, e uma frota ligada num bloqueio efetivo (§2.14.7). |
| alliance   | Ambos os reinos combatem como parceiros; sem combate mútuo. **Apenas mútua** — exige ordens independentes de ambos os lados; unilateral é inerte.                                    |
| trade      | Ouro bónus mútuo. Exige ordens independentes de ambos os lados.                                                                                                                      |

**2.16.2 Transições e Resolução de Conflitos (Transitions and Conflict Resolution)**

Todas as ordens diplomáticas são avaliadas contra o instantâneo da postura no **início do turno** — tirado antes de quaisquer declarações de guerra do próprio turno (um cerco ou assalto em curso, uma ligação de bloqueio, o contacto da Fase 5, uma incursão da Fase 6), pelo que nenhuma delas pode passar por uma guerra antiga na Fase 8.

**A guerra vence tudo**: Se dois reinos submeterem ordens conflituantes (uma de guerra, outra de paz/aliança/comércio), a guerra prevalece.

**Reconciliação bloqueada após uma guerra recente**: Se entraste em guerra com um reino *neste turno* — através de qualquer guerra iniciada antes neste turno: um cerco ou assalto em curso, uma ligação de bloqueio (Fase 1), um combate da Fase 5, ou uma incursão ou combate naval da Fase 6 — não podes alterar a tua postura em relação a ele (paz, aliança ou comércio) na Fase 8 desse mesmo turno. A guerra mantém-se até ao turno seguinte. Isto evita uma postura unilateral em que declaras paz/aliança enquanto o outro continua em guerra. As guerras já existentes podem continuar a ser terminadas normalmente. Uma alteração de postura bloqueada (por esta regra, ou um pacto comercial recusado por falta de fronteira comum) produz um cartão ⚠ **"Diplomacy blocked"** no teu relatório — a ordem não é aplicada e o teu relatório nunca afirma que foi.

**Posturas baseadas em consentimento**: A **guerra** (War) é espelhada automaticamente para o alvo (a guerra é sempre forçada a ser simétrica). **O comércio e a aliança nunca são espelhados** — cada um exige que ambos os reinos definam a postura de forma independente. **A paz depende do ponto de partida**: passar de uma aliança ou pacto comercial **mútuo** para paz continua a ser unilateral e arrasta consigo a postura do outro lado, mas **terminar uma guerra exige consentimento mútuo** — uma ordem de paz em guerra é uma *proposta*, não um decreto (ver *Ending a war* abaixo). Um pacto comercial ou uma aliança unilateral não concede quaisquer benefícios, e **em qualquer dos casos recebes um aviso de "one-sided pact" no teu relatório em cada turno em que continue sem reciprocidade** (um cartão 🤝 one-sided-alliance, ou um cartão 📦 one-sided-trade). **O alvo também é notificado**: em cada turno em que uma proposta continue aberta, o reino a quem foi feita recebe um cartão 🤝 *"proposes an alliance"* (ou 📦 *"seeks a trade pact"*) que lhe diz para retribuir em Diplomacia — incluindo os reinos passivos. Quando a proposta é finalmente retribuída, o proponente original recebe um cartão de confirmação *"accepted your alliance"* / *"opened trade with you"*. O cartão do teu relatório para a ordem diz **"proposed to"** (*"ALLIANCE proposed to"*) até o pacto ser mútuo — só então diz *forged*/*established* — e o separador Diplomacia mostra a aliança como *"Alliance — proposed (awaiting reply)"*, com **⇢ SENT** ao lado do botão de retirar (um pacto comercial unilateral também mostra ⇢ SENT). O outro lado também a vê em Diplomacia: o cartão do proponente traz **⇠ OFFERS ALLIANCE** (ou **⇠ OFFERS TRADE**) ao lado do botão que lhe responde — premir esse botão forma o pacto, e até o turno ser processado o cartão mostra **✓ ACCEPTING**. Uma oferta comercial de um reino com o qual não partilhas fronteira é etiquetada *(no border)*: um pacto comercial exige-a, uma aliança não. Até lá não concede quaisquer benefícios (nem movimento através do território, nem recrutamento aliado, nem bónus do pacto), e a Página do Jogador (Player Page) só trata um reino como aliado verdadeiro quando a aliança é mútua. **Retirar uma proposta sem resposta é silencioso**: é gratuito, deixa totalmente intacta a postura do outro reino e não lhe envia qualquer cartão — nunca se formou nada, por isso nada termina. Os reinos passivos (que não submetem ordens) nunca retribuem, pelo que não podem ser arrastados para uma aliança ou pacto comercial.

**Terminar uma guerra — Propor Paz (consentimento mútuo) (Ending a war — Propose Peace)**: em guerra, o separador Diplomacia oferece 🕊 **Propose Peace** (uma aliança ou pacto comercial termina-se com os botões ✕ **End Alliance** e ✕ **End Trade Pact**). Uma ordem de paz em guerra altera apenas a **tua** postura para paz, como **oferta permanente**: o inimigo mantém a sua postura de guerra e, como um par está em guerra enquanto *qualquer* dos lados mantiver a guerra, **os combates continuam sem alteração** até ele aceitar. Ambos os lados recebem cartões em cada turno em que a oferta permaneça aberta (🕊 *"peace offered — war continues"* para ti, 🕊 *"proposes peace"* para ele), e o teu cartão de Diplomacia ostenta o distintivo *"⚔ War — 🕊 peace offered"*. A paz **forma-se** quando o outro lado também ordena paz (o seu botão diz 🕊 **Accept Peace** enquanto a tua oferta se mantém) — só então a guerra termina e o **dividendo da paz** (+1 a +3 de opinião, para ambos os lados) é pago. **Retirar**: voltar a declarar guerra enquanto a tua oferta se mantém limita-se a retirar a oferta da mesa — a guerra nunca terminou, por isso **não** é uma nova declaração e **não** custa opinião (o botão diz ✕ *Withdraw Peace Offer*). **Os reinos passivos aceitam automaticamente**: um reino que não submeteu ordens nesse turno aceita automaticamente uma oferta de paz permanente, pelo que uma guerra contra um reino ausente ou controlado pelo GM pode sempre ser terminada.

**2.16.3 Efeitos de Opinião da Diplomacia (Opinion Effects of Diplomacy)**

Cada transição diplomática move a opinião conforme a tabela no §8.5.3 — declarar guerra, quebrar ou rebaixar uma aliança **mútua**, formar a paz. Uma oferta de paz permanente não paga nada até a paz se formar, e retirá-la (voltar a declarar guerra perante uma oferta não aceite) não custa nada.

**2.16.4 Vassalagem (Vassalage) (Fase 8c)**

**Tornar-se vassalo — o suserano tem de aceitar (Becoming a vassal)**: uma ordem become_vassal é uma **oferta de fidelidade**, nunca um vínculo por si só. No turno em que a envias, ambos os reinos recebem cartões (🏳 *"Oath of fealty offered"* para ti, 🏳 *"X offers fealty"* para o futuro suserano) e mais nada muda — sem suserano, sem aliança, sem tributo (Tribute). O suserano responde **com as suas ordens seguintes**: o separador Diplomacia mostra o juramento no teu cartão para esse reino, com a respetiva taxa de tributo, e ✓ **Accept** / ✕ **Decline** (uma ordem vassal_offer_reply; clicar de novo na resposta escolhida retira-a). **Aceite** → ficas juramentado nesse turno (abaixo). **Recusada, ou sem resposta** → a oferta caduca, ambos os lados recebem cartões e nada muda; podes oferecer de novo. Um reino que não submete ordens nunca responde, pelo que um reino passivo não pode ser feito suserano. Uma oferta à espera de resposta é mostrada no teu próprio cartão de Diplomacia para esse reino. Se enviares um novo juramento enquanto outro aguarda resposta, o que aguarda continua a ser respondido nesse turno; o teu novo juramento só sai se o que aguarda não for aceite.

**Requisitos** — verificados quando ofereces **e de novo quando o suserano aceita** (Fase 8c, depois de todas as guerras do turno): não estar em guerra com o futuro suserano, pelo que uma ordem de guerra, batalha, incursão, cerco ou ligação de bloqueio entre vós anula o juramento (pôr a guerra em fila contra ele na Página do Jogador cancela de imediato um juramento em fila e avisa-te); não estar já juramentado a qualquer reino, incluindo o futuro suserano; **não possuir vassalos próprios** (um vassalo caído não conta) — um reino com vassalos não pode jurar fidelidade, pelo que nunca há cadeias de vassalos (a Página do Jogador não oferece o juramento enquanto possuíres algum, e desativa Accept num juramento vindo de um reino que os possua); o suserano não ser vassalo teu; o suserano não ser ele próprio vassalo de outro reino (o seu botão Accept está desativado); nenhum dos reinos ter caído; e não ser o teu próprio reino. Um juramento que falhe um requisito é recusado com um cartão para quem for afetado — na aceitação, ambos os reinos. **Várias aceitações no mesmo turno** são resolvidas uma a uma numa ordem fixa (a mesma em todos os turnos, independentemente de quem enviou ordens primeiro), cada uma verificada contra o que as anteriores alteraram — por isso, quando dois reinos oferecem fidelidade um ao outro, ou se formaria uma cadeia, exatamente um juramento é prestado e o outro é recusado com um cartão. **No turno em que um juramento é aceite**, um novo juramento que tenhas enviado não é enviado e uma renúncia que tenhas enviado não é executada — ambos recebem cartão; envia-os de novo com as tuas ordens seguintes. **Aceitar um juramento faz de ti suserano**, pelo que um juramento teu nesse mesmo turno é recusado: a Página do Jogador retira o teu juramento em fila quando aceitas, e avisa-te.

Na aceitação: ambos os lados definem automaticamente a postura de Aliança (dura até uma guerra entre eles terminar o vínculo, abaixo); taxa de tributo definida (1–5%, por omissão 3%); tributo pago a partir do rendimento (Income) em ouro da Fase 1 do vassalo em cada turno — p. ex. 1,000 de ouro a 3% paga floor(1,000 × 3 / 100) = 30 de ouro; um vassalo que não consiga cobri-lo paga apenas o que tem, e o suserano é creditado exatamente com isso.

**Abandonar a vassalagem (Leaving vassalage)**: ordem leave_vassalage. Resolve-se antes dos novos juramentos do turno, pelo que podes renunciar ao teu suserano e oferecer fidelidade a outro nas mesmas ordens. Pagas o tributo **uma última vez** no turno em que renuncias — o tributo é cobrado na Fase 1 enquanto ainda és vassalo, e a renúncia só se resolve na Fase 8 — depois o tributo cessa a partir do turno seguinte. A postura de Aliança mantém-se, salvo alteração explícita. Até submeteres, o separador Diplomacia mostra a renúncia como pendente sob o nome do teu suserano, com ↺ **Undo Renounce**; anulá-la também retira um juramento a um novo suserano posto em fila depois dela.

**A guerra termina a vassalagem**. Uma guerra entre um suserano e o seu vassalo — declarada por **qualquer** dos lados, por **qualquer** via: uma ordem de guerra, uma batalha, uma incursão, um cerco ou uma ligação de bloqueio — termina a vassalagem **no momento em que a guerra começa**, em qualquer fase: a partir daí os dois deixam de ser amigos — sem bónus de porto nos portos um do outro, sem abrigo dentro das muralhas um do outro, sem participar na defesa um do outro — a lista do suserano deixa cair o vassalo, e qualquer ligação de exército ou frota entre eles é libertada no fim do turno — embora os exércitos dos dois acampados na mesma zona de um hexágono lutem primeiro um contra o outro, na Fase 5 desse turno se a guerra começou na Fase 1 (o varrimento de acampamento, §2.13; as frotas no varrimento de coabitação da Fase 6). O tributo desse turno só é pago se a guerra começou depois do rendimento da Fase 1 (uma ordem de guerra, uma batalha da Fase 5 ou 6, uma incursão, uma ligação de bloqueio); uma guerra começada antes dele — por um cerco ou assalto em curso (o seu ciclo declara guerra a todos os reinos lá dentro, §5.6) — também suspende o tributo desse turno, e ambos os cartões dizem o que aconteceu. Ambos os lados recebem cartões — *"Vassalage to X ended — at war"* e *"X is no longer your vassal — at war"* — e a Página do Jogador avisa-te quando pões essa guerra em fila. Nenhum reino permanece juramentado a um suserano com quem está em guerra.

**O vínculo de um reino caído termina**. Quando um reino cai, todas as vassalagens de que faz parte terminam com ele, nos dois sentidos: um vassalo caído é libertado do seu suserano, e os vassalos de um suserano caído são libertados. Ambos os lados recebem cartões (🏳 *"X has fallen"* / *"Your liege X has fallen"*); a partir daí não se paga tributo e os dois reinos deixam de estar ligados por aliança — a sua diplomacia mantém-se como está até um deles a alterar.

**Taxa de tributo (Tribute rate)**: O suserano pode ajustá-la com set_vassal_tribute (limitada a 1–5%). A nova taxa aplica-se a partir da Fase 1 seguinte. Uma taxa definida no mesmo turno em que uma guerra termina o vínculo não faz nada — na Fase 8c o reino já não é teu vassalo (o registo do GM regista a recusa; o teu relatório traz em vez disso o cartão "no longer your vassal").

**2.16.5 Mensagens e Cessar-fogo (Messaging and Ceasefire) (Fase 8 — depois da vassalagem)**

Até 3 mensagens por turno para quaisquer reinos. Mensagens até 1000 caracteres. Entregues no relatório do destinatário.

**A tua cópia**: o teu relatório seguinte guarda uma cópia de cada mensagem que enviaste — na íntegra em **Sent** no separador Mensagens, e como cartão de evento — com o que lhe aconteceu: *delivered*, uma difusão com o número de reinos que alcançou, ou *not delivered* quando o reino a que te dirigiste não está no turno.

**Difusão para todos os reinos (Broadcast to all kingdoms)**: em vez de escolheres um destinatário, podes dirigir uma mensagem a **All Kingdoms**. É entregue a todos os outros reinos — incluindo os que estão em paz, em guerra, ou controlados pelo GM/ausentes (passivos) — e **conta como uma das tuas 3 mensagens**. Os destinatários veem-na claramente identificada como difusão (📢), para saberem que foi enviada a todos e não em privado só para eles. Os comandos especiais (\[CEASEFIRE\], \[TRIBUTE\]) **não** funcionam dentro de uma difusão — é apenas um anúncio simples; para propores um cessar-fogo ou enviares tributo tens de enviar a mensagem diretamente a esse reino.

**Mecanismo de cessar-fogo (Ceasefire mechanic)**: Se ambos os reinos em guerra incluírem, de forma independente, o símbolo \[CEASEFIRE\] numa mensagem dirigida um ao outro no mesmo turno, a paz é estabelecida automaticamente — desde que a guerra não tenha sido declarada primeiro nesta mesma Fase 8 (um cessar-fogo não pode anular uma guerra declarada neste turno). Ganho de opinião para ambos: +(2 + floor(rand×4)) = +2 a +5.

**2.17 Eventos Aleatórios (Random Events)**

Não existem eventos aleatórios: nenhum reino tira um evento em qualquer ponto do turno. O que um reino ganha ou perde provém apenas das suas próprias ordens, do mapa e dos outros reinos.

**2.18 Geração de Relatórios (Report Generation)**

Depois de todas as fases, o Processador de Turnos (Turn Processor) gera um relatório por reino e um registo do GM.

**Os relatórios dos jogadores incluem**: estado do mapa com nevoeiro (hexágonos próprios = completo, adjacentes/posições de exércitos/hexágonos comunicados por espiões = fronteira, hexágonos vistos anteriormente = recordados — terreno mais o local de produção/construção como visto pela última vez, §2.19 — o resto = oculto), recursos atuais, exércitos, frotas, personagens, todos os eventos de batalha, discriminação do rendimento, alterações diplomáticas, mensagens recebidas, relatórios de espiões. As posições das unidades inimigas são mostradas nos hexágonos de visibilidade completa e de fronteira; os marcadores de exércitos e frotas estrangeiros são coloridos consoante a tua postura diplomática perante o dono — aliado, neutro (paz) ou hostil (guerra). Aplicam-se duas ocultações: um exército em **Emboscada (Ambush)** válida nunca é mostrado a outros reinos, nem aos seus espiões (§5.4), e **um exército embarcado numa frota também nunca é mostrado — vês o marcador da frota, não a sua carga** (só um aliado em cujo porto a frota está acostada é informado do que ela transporta, §2.14.2). **Os teus próprios portos mostram mais do que um marcador:** passar o cursor sobre um porto teu lista todas as frotas estrangeiras acostadas aí, com o seu numeral, cascos por tipo, poder de guerra e comandante, seja qual for a tua relação com o respetivo dono (§2.14.2). Uma frota ao largo da tua costa pode ser um assaltante vazio ou uma força de invasão completa; o mapa não te dirá qual.

O rendimento dos pactos comerciais/de aliança é **discriminado por parceiro** no registo de Eventos — um cartão 📦 lista cada parceiro do pacto com a percentagem sorteada (0–2%) e o ouro ganho nesse turno — além da linha de total único mostrada no resumo do rendimento. (A pré-visualização "Expected Income" anterior ao turno mostra apenas um total estimado; os valores por parceiro surgem depois de o turno ser processado.)

**Ordem das fases no registo do turno.** Os cartões do teu relatório do turno são ordenados pela fase do motor que os produziu — Recrutamento (Pré-Fase 2b) → Cercos e Assaltos (Pré-Fase 3) → Rendimento → Manutenção → Mercado/Construção → Navios e Contratação → Transferências → Combate Terrestre → Marinha → Espiões → Diplomacia → Mensagens — e cada cartão traz um pequeno distintivo de fase no canto direito (p. ex. 🍖 PHASE 2 · Upkeep, 🏇 PHASE 5 · Combat). Isto permite-te ler o turno de cima para baixo, pela ordem exata em que os eventos foram resolvidos.

**Registo de Guerra (War Record)**: cada reino mantém um balanço corrente de vitórias–derrotas, mostrado como ⚔ **War Record (W–L)** na faixa de território sob o teu livro de Perfil — registos separados de exército e frota (p. ex. 4–1 exército · 1–0 frota). Uma vitória ou derrota só é registada numa **batalha real exército contra exército ou frota contra frota** — batalhas campais, surtidas, assaltos a povoações com guarnição, desembarques anfíbios contra um exército defensor, e batalhas navais. Os combates **apenas contra milícia** (assaltar uma povoação sem guarnição) e os **empates** **não** contam. O balanço acumula-se ao longo de todo o jogo (começa em 0–0 e nunca é reposto). O separador **Rankings** inclui uma tabela **🏆 Total Wins** que ordena todos os reinos por vitórias de exército + vitórias de frota; como todas as tabelas, mostra classificações (a tua posição relativa aos rivais), não os números exatos dos adversários — as tuas próprias contagens estão no teu Perfil.

**2.19 Memória do Mapa (Map Memory)**

**Memória do mapa.** O teu reino recorda permanentemente todos os hexágonos que alguma vez viu — território, alcance de exploração, relatórios de espiões, e todos os hexágonos por onde os teus exércitos e frotas passam na marcha (cada hexágono percorrido e os seus arredores). Os hexágonos recordados permanecem no teu mapa nos turnos futuros, desenhados esbatidos e tracejados: conheces o **terreno** e, abaixo, o local de produção e a povoação como os viste pela última vez — nada em tempo real. Não são mostrados donos nem tropas aí — um hexágono recordado vazio NÃO está confirmado como vazio; um exército inteiro pode estar nele. Só a visão atual (a tua terra, os arredores das tuas unidades, os relatórios de espiões deste turno) mostra informação em direto. **As tuas cartas também recordam o que lá estava**: o local de produção e a povoação/fortificação *como as viste pela última vez* — desenhados esbatidos nos hexágonos recordados em todos os mapas e nomeados na dica do hexágono ("last seen: ⚓ Port Lv.II · 🏰 G3"). A memória só é atualizada enquanto um hexágono está à vista: um porto construído depois de teres partido não aparece, um arrasado continua a aparecer até voltares a olhar, e nada sobre o seu dono, população ou força das muralhas é guardado. Um local recordado é uma memória, não informação — o motor nunca o trata como atual (podes planear um desembarque num porto recordado, e o Processador de Turnos resolve-o contra o mapa real).

**PARTE III — MUNDO E TERRENO (PART III — WORLD & TERRAIN)**

**3.1 Tipos de Terreno (Terrain Types)**

|             |                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Terreno** | **Notas**                                                                                                                                                           |
| Planície    | Terra comum. Aloja quintas, portos (se adjacente ao mar), pedreiras e minas (7% de prospeção, limite Lv1). +1 de comida plana se não houver local de produção.        |
| Colinas     | Acidentado. Aloja pedreiras (taxa de pedra reduzida, §3.6.6) e minas (15%). Terreno natal dos Bárbaros.                                                              |
| Montanha    | Rochosa. Aloja minas — os melhores filões (25% de probabilidade de achado, o único terreno capaz de Lv3) — e pedreiras (taxa de pedra reduzida, igual à das colinas). Terreno natal dos Anões. |
| Floresta    | Densa. Aloja serrações, minas (5%, apenas Lv1) e — **só para um reino Elfo, sob uma construção élfica** — portos, se adjacente ao mar (§3.6). Terreno natal dos Elfos. |
| Deserto     | Árido. Aloja minas (7%). Terreno natal dos Nómadas.                                                                                                                 |
| Pântano     | Alagadiço. Não aloja quaisquer locais de produção. Terreno natal dos Orcs.                                                                                          |
| Mar         | Água. Intransponível para exércitos. Apenas frotas.                                                                                                                 |

**Cidade e Capital não são terrenos.** A povoação é uma **construção** que o GM coloca num dos terrenos acima (§3.7); o terreno decide de que é *feito* um hexágono, a construção decide quem *vive* nele. O terreno não tem população própria, e o Imperial não tem terreno natal (§3.5).

**3.2 População Base (Base Population)**

**O terreno não tem população.** A população de um hexágono provém inteiramente da **construção** que nele se encontra, definida pela sua família e nível (§3.7.1); um hexágono sem construção tem **zero**, permanentemente. Cada construção começa a campanha no teto máximo do seu nível e cresce a partir daí (§3.8).

**3.3 Regras de Rendimento do Terreno (Terrain Income Rules)**

|                    |               |               |
|--------------------|---------------|---------------|
| **Terreno**        | **Ouro/Turno** | **Comida/Turno** |
| Planície (sem local de produção) | —             | +1 de comida  |
| Todos os outros terrenos | —             | —             |

**3.4 Terreno em Combate (Terrain in Combat)**

**Os multiplicadores de terreno** aplicam-se em batalha campal e assalto quando uma raça luta no seu terreno natal (ver 3.5). Os multiplicadores não se aplicam em combate naval nem em batalha anfíbia.

**Resistência à tomada (Seizure resistance)**: o terreno não dá bónus a nenhum dos lados — tomar um hexágono é uma disputa de estilo campal contra a milícia da construção (§2.13.4).

**3.5 Bónus de Terreno das Raças (Race Terrain Bonuses)**

|           |                     |                                                                       |
|-----------|---------------------|-----------------------------------------------------------------------|
| **Raça**  | **Terreno(s) Natal(ais)** | **Multiplicador de Combate**                                    |
| Anão      | Montanha            | ×1.30                                                                 |
| Elfo      | Floresta            | ×1.30                                                                 |
| Nómada    | Deserto             | ×1.25                                                                 |
| Orc       | Pântano             | ×1.20                                                                 |
| Bárbaro   | Colinas             | ×1.15                                                                 |
| Imperial  | —                   | nenhum                                                                |
| Aesir     | —                   | nenhum (o seu bónus é naval: ×1.05 em cada lançamento de batalha de frota, §5.9.2) |

Aplicado tanto ao atacante como ao defensor quando lutam no terreno correspondente — e apenas à raça correspondente: qualquer outro reino que lute nesse tipo de terreno não recebe bónus, seja quem for o dono do hexágono.

> ***▶ Exemplo — porque é que o terreno natal importa (Example).** Um atacante que não é da floresta traz 200 WP contra um defensor **Elfo** (floresta natal, ×1.30) que mantém um hexágono de floresta em postura Defensiva (×1.20). O lançamento do defensor constrói-se a partir de 200 × 1.30 × 1.20 = 312 antes da variância; o atacante constrói-se a partir de 200. Para superar a margem decisiva de +20% (§5.5.2), o atacante precisa de aproximadamente 312 × 1.2 ≈ 375 WP efetivos — quase o **dobro** da força bruta. Assaltar um Elfo nos bosques, ou um Anão nas montanhas (também ×1.30), é uma proposta perdedora sem números esmagadores, uma vantagem de comandante, ou o teu próprio terreno correspondente para anular o deles. (Se o atacante também fosse um Elfo, ambos os lados receberiam ×1.30 e anular-se-ia.)*

**3.5.1 Cavalaria e Terreno (Cavalry and Terrain)**

As unidades montadas sentem o chão sob os cascos. Em batalhas campais e assaltos (assaults), a **parcela montada** dos WP de um exército é ajustada pelo terreno do hexágono da batalha:

|             |                                                                                                                                       |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Terreno** | **Multiplicador de Cavalaria**                                                                                                        |
| Planície    | **×1.20** — corredores abertos para a carga; o terreno decisivo da cavalaria                                                          |
| Colinas     | ×0.90 — as cargas perdem ímpeto em subida                                                                                             |
| Floresta    | ×0.70 — sem formações entre as árvores (**Warg Riders isentos** — os wargs são predadores da floresta, não cavalos)                  |
| Pântano     | **×0.60** — os cavalos atolam-se e entram em pânico; o cemitério da cavalaria                                                         |
| Montanha    | ×0.70 — desfiladeiros e cascalho favorecem absolutamente a infantaria                                                                 |
| Deserto     | ×0.85 — o calor e a sede castigam os cavalos dos forasteiros (**toda a cavalaria Nómada isenta** — criada no deserto; acumula com o bónus de raça Nómada ×1.25) |

Regras de âmbito:

- Aplica-se **apenas ao lado do lançamento**, tal como o bónus de terreno da raça (§3.5): os WP do exército mostrados nas classificações, a capacidade de cerco e as estimativas dos espiões mantêm-se em bruto.

- Ajusta apenas a fração montada de cada exército — um exército misto de 70% de infantaria / 30% de cavalaria num pântano perde apenas 40% da contribuição *montada*, não do exército inteiro.

- Tanto o atacante como o defensor são afetados; as tropas a pé e a **milícia nunca são ajustadas**.

- **Sem modificador** em desembarques anfíbios (aí vigora o regime da praia ×0.50, §5.7), nem em disputas de milícia por tomada (sem terreno por conceção, §3.4).

> ***▶ Exemplo — a carga e o lodaçal.** 100 Equites (WP 19,200, todos montados) atacam 200 Swordmasters (WP 20,000, todos a pé). Na **planície** os Equites combatem com 23,040 efetivos e vencem de forma decisiva — a carga compensa. As mesmas duas forças num **pântano** deixam os Equites com 11,520 efetivos, e os Swordmasters abatem-nos. Os mesmos exércitos, resultados opostos; o terreno é uma arma.*

**Cavalaria contra muralhas.** Tomar de assalto um povoado fortificado substitui a regra de terreno para o atacante: todas as unidades montadas do exército assaltante combatem com **65%** dos seus pontos de guerra — os cavalos (e os wargs) de nada servem numa escada. Isto aplica-se quer as muralhas sejam defendidas por uma guarnição, quer apenas pela milícia da cidade, e substitui qualquer bónus de terreno (não há carga de planície contra uma porta fortificada). A cavalaria dos defensores, as surtidas e as batalhas em campo aberto não são afetadas, e as máquinas de cerco não são cavalaria.

**3.6 Locais de Produção: Quintas, Minas, Portos, Forjas, Serrações, Pedreiras (Sites: Farms, Mines, Ports, Forges, Lumbermills, Quarries)**

Cada hexágono pode ter no máximo um local de produção. As quintas, minas, portos, serrações e pedreiras escalam o rendimento nos níveis 1–3. As forjas são fixas no nível 1 e concedem experiência ao exército em vez de rendimento.

**3.6.1 Quintas (Farms)**

- **Terreno**: apenas planície

- **Custo de construção**: 1000g — garantido. **A quinta não faz lançamento para ser construída**: paga-se a taxa, obtém-se a quinta.

- **Rendimento**: floor(pop × rate) comida/turno, onde rate é **sorteado de novo em cada turno, para cada quinta em separado** — Nv1 **5–25%**, Nv2 **20–50%**, Nv3 **40–80%** da população do hexágono. O mínimo é sempre superior a zero, pelo que uma quinta nunca rende nada enquanto tiver gente: o que está garantido é o limite inferior do seu intervalo, e tudo o que passe disso é a estação. A Página do Jogador conta apenas esse mínimo nos seus valores de rendimento; o separador Produção mostra o intervalo completo de cada quinta (🎲 mín–máx).

- **Melhoria Nv2**: 2000g, 100% de probabilidade — garantido

- **Melhoria Nv3**: 3000g, 100% de probabilidade — garantido

> ***▶ A troca que a quinta faz.** Uma quinta é uma certeza na construção e uma aposta na colheita. O ouro que gastas nunca é desperdiçado — 1000g compram sempre uma quinta e 5000g levam-na sempre ao Nv3 — mas o que ela rende varia de turno para turno. Cada melhoria continua a ser um ganho claro em ambos os extremos do seu intervalo (5–25% → 20–50% → 40–80%), pelo que não há nível que valha a pena saltar. Planeia a tua comida pelo **mínimo** de cada quinta; os valores de rendimento da Página do Jogador contam apenas isso, deliberadamente (o seu separador Produção mostra o intervalo completo), e o teu relatório diz-te o que cada turno realmente sorteou.*

**3.6.2 Minas (Mines)**

- **Terreno e probabilidade de descoberta**: Montanha 25% · Colinas 15% · Deserto 7% · Planície 7% · Floresta 5% (os hexágonos de pântano não podem ser prospetados)

- **Custo de construção**: 1000g por tentativa — ouro gasto independentemente do resultado

- **Rendimento**: base\[level\] + floor(pop × siteLevel / 20) ferro/turno — base Nv1: 10, Nv2: 20, Nv3: 50 (um mínimo fixo por nível, visto que as montanhas têm pouca população); 0 se o hexágono não tiver população. Ex.: uma mina Nv3 numa montanha com 300 de pop = 50 + floor(900/20) = **95 ferro/turno**; no Nv1 = 10 + 15 = **25**

- **Nível máximo por terreno**: Montanha 3 · Colinas/Deserto 2 · Planície/Floresta 1

- **Melhoria Nv2**: 2000g, 30% de probabilidade

- **Melhoria Nv3**: 3000g, 50% de probabilidade — **apenas reinos Anões**; como qualquer construção ou melhoria de local de produção, o hexágono tem de ter uma construção (§2.11.1); a conquista degrada os locais de produção um nível (§5.6.3), pelo que um Nv3 capturado chega como Nv2 e só um conquistador Anão o pode restaurar

As montanhas continuam a ser a coroa da mineração em todos os eixos: a melhor probabilidade de achado, os únicos filões Nv3 e a defesa de terreno nativo dos Anões por cima. Em qualquer outro lado, a prospeção é uma aposta cada vez pior — as colinas são respeitáveis, o deserto e a planície são saídas dispendiosas para reinos pobres em montanhas, a floresta é o último recurso.

> ***⚠ O que isto significa —** Construir uma mina é uma aposta: pagas as 1000g completas por tentativa, sem reembolso em caso de falha — espera cerca de 4,000g em tentativas numa montanha (25%), mas até ~20,000g na floresta (5%) antes de aparecer um filão. Depois de a mina existir, aprofundá-la é muito mais fácil (Nv1→Nv2 a 30%, Nv2→Nv3 a 50%) — a parte cara é encontrar o filão, não alargá-lo. Na planície, atenção ao custo de oportunidade: o mesmo hexágono podia ter uma quinta.*

**3.6.3 Portos (Ports)**

> ***Um porto precisa de gente, não apenas de um ancoradouro.** Um porto rende a partir da população do seu próprio hexágono, e só pode tripular um navio a partir dessa mesma população (§2.12.3). Se o povoado do hexágono desapareceu — um acampamento Nómada que se mudou (§2.11.10), ou um hexágono em que o GM pintou um porto sem povoado — o ancoradouro continua a abrigar e a lançar frotas, mas não rende nada e não pode construir nada.*

- **Terreno**: Planície — **ou floresta, apenas para um reino Elfo** (a exceção Élfica, §2.11.1) — o hexágono tem de ser adjacente a pelo menos um hexágono de mar

- **Custo de construção**: 5000g — garantido

- **Rendimento/turno**: ouro floor(pop × goldMult) — Nv1 ×0.20, Nv2 ×0.40, Nv3 ×0.60, nunca aleatório — mais comida sorteada de novo em cada turno por porto (0–5% / 0–10% / 0–15% da população); os portos pagam em escalões de 5, ordenados do maior para o menor. Regras completas, mínimos e o que a Página do Jogador mostra: §2.9.4.

- **Melhoria Nv2**: 10000g — determinística (a taxa é paga na tentativa, e a tentativa tem sempre êxito)

- **Melhoria Nv3**: 15000g — determinística

- **Restrição de raça**: os reinos Orc e Anão não podem construir portos — a ordem é recusada e as 5000g reembolsadas. Os reinos Elfos também podem construir em floresta costeira sob uma construção Élfica (§2.11.1).

- Um porto bloqueado não produz nada.

- Os hexágonos de porto permitem a construção de navios.

**3.6.4 Forja (Forge)**

- **Restrição de raça**: apenas reinos Anões. Não pode ser colocada por nem transferida para nenhuma outra raça.

- **Colocação**: num hexágono com uma **construção Anã (FDW)**. Não pode coexistir com uma Mina.

- **Nível**: Sempre nível 1. Sem melhorias.

- **Não construível**: as forjas são colocadas pelo GM no Editor de Mapa no início da campanha — não podem ser construídas por ordens dos jogadores durante uma campanha.

- **Efeito**: Ver §5.3.2 — os exércitos Anões estacionários num hexágono de forja ganham um +2% fixo de xp_wp no fim do turno.

- **Apresentação**: o ícone da forja (⚒) aparece no canto superior direito do hexágono no minimapa da Página do Jogador, idêntico à apresentação de porto/mina/quinta. No separador Produção, o cartão da forja diz "Stationary armies gain +2% XP per turn" em vez de uma linha de rendimento.

- **Nota para o GM**: se alterares a raça de um reino Anão para outra raça no painel de reinos do Editor de Mapa, todos os locais de forja nos hexágonos desse reino são removidos automaticamente quando guardares.

**3.6.5 Serrações (Lumbermills)**

- **Terreno**: apenas floresta

- **Custo de construção**: 1000g — **100%** de conclusão (sem aposta)

- **Rendimento**: pop \> 0 ? max(1, floor(pop × mult)) : 0 **madeira**/turno — mult Nv1: 0.15, Nv2: 0.45, Nv3: 0.75

- **Melhoria Nv2**: 2000g, **100%** · **Melhoria Nv3**: 3000g, **100%** — nível máximo 3 em todo o lado

- Barato, fiável e determinístico — a economia da floresta é o oposto da prospeção de minas. Num hexágono de floresta a decisão real é entre a serração e a mina de ferro com 5% de probabilidade e limitada ao Nv1 (um local de produção por hexágono); para madeira, não há comparação.

**3.6.6 Pedreiras (Quarries)**

- **Terreno**: Planície, Colinas ou Montanha

- **Custo de construção**: 1000g — **100%** de conclusão

- **Rendimento**: pop \> 0 ? max(1, floor(pop × mult)) : 0 **pedra**/turno — o mult é **definido pelo terreno**: Planície **0.15 / 0.45 / 0.75** · Colinas e Montanha 0.10 / 0.40 / 0.70 *(a planície é o terreno mais rico em pedra)*; uma pedreira em qualquer outro terreno obtém a taxa da planície

- **Melhoria Nv2**: 2000g, **100%** · **Melhoria Nv3**: 3000g, **100%** — nível máximo 3 em todo o lado

- Na planície, uma pedreira compete com quintas, portos e prospeções de minas pela única vaga de local de produção do hexágono; em colinas e montanhas compete com minas — pedra garantida mas mais escassa contra ferro apostado é o dilema central.

A madeira e a pedra são mercadorias de pleno direito: aparecem na tua barra de recursos, podem ser compradas e vendidas no mercado (base 5g / 7g), enviadas para outros reinos e exigidas como tributo. **A madeira é consumida no recrutamento de unidades** — cada arco, besta, coronha de arma de fogo, feixe de dardos, escudo e cabo de machado do jogo custa madeira (vê a tabela de cada raça; as tropas de projéteis são as mais esfomeadas com 8–12w, as muralhas de escudos 4–8w, os cabos simples 2–3w; só as elites Élficas de lâmina pura não custam nada). **Cada casco de navio também custa madeira** — cerca de metade da sua capacidade de tropas em madeira (40–130w; vê as tabelas de navios) — pelo que um programa de frota exige uma economia de madeira constante, o mercado ou presas capturadas (os navios-presa chegam de graça). **A pedra e a madeira também constroem muralhas**: fundar, melhorar e reparar uma construção gasta o material de muralha da família (o tecido da família de construção — madeira para Aesir, Nómadas e Orcs, pedra para as restantes; as muralhas da família Anã custam metade, §2.11.7) — vê §3.7.2 e §6.11. As máquinas de cerco também custam madeira (50w cada).

**3.7 Construções (Constructions)**

**Cidade e Capital não são tipos de terreno.** Ter população, cunhar milícia, ter muralhas, ser cercado e sediar uma capital faz-se através de uma **construção**: um objeto de povoamento que o GM coloca num hexágono, pertencente a uma de oito famílias raciais e situado num nível da escada dessa família.

Um hexágono ou tem uma construção ou não tem. **Um hexágono sem construção não tem população nenhuma** — sem imposto, sem milícia, sem recrutamento, e qualquer local de produção aí construído não rende nada (§3.6). O terreno nu está genuinamente vazio; toda a vida povoada do mundo reside dentro de uma construção.

**3.7.1 As Oito Famílias (The Eight Families)**

Cada raça constrói no seu próprio idioma. Uma família fixa três coisas em cada nível: o **limite de população** para que o povoado cresce, a **muralha** atrás da qual se abriga e o **custo em ouro** para atingir esse nível a partir do inferior.

|            |          |            |            |                      |                |                                                                                                                        |
|------------|----------|------------|------------|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------|
| **Família** | **Código** | **Material** | **Níveis** | **Intervalo de população** | **Intervalo de muralhas** | **Carácter**                                                                                                          |
| Imperial   | FI       | pedra      | 20         | 100 – 50,000         | 500 – 25,000   | O caminho longo: degraus iniciais baratos, depois as maiores muralhas e populações do mundo a um custo ruinoso         |
| Bárbaro    | FBA      | pedra      | 20         | 100 – 20,000         | 500 – 6,000    | Largo e pouco profundo — muitos degraus, muralhas modestas, acessível quase todo o caminho                             |
| Elfo       | FLF      | pedra      | 10         | 100 – 10,000         | 200 – 8,000    | Poucos degraus refinados; muralhas que sobem a pique quando o povoado amadurece                                         |
| Anão       | FDW      | pedra      | 10         | 100 – 10,000         | 1,000 – 18,000 | As muralhas mais densas por habitante do jogo, e o escalão superior mais barato — um burgo Anão é primeiro uma fortaleza e depois uma vila |
| Aesir      | FAS      | madeira    | 10         | 100 – 10,000         | 500 – 10,000   | Muralhas de madeira de 500 até ao Nv.3, depois igualando o limite de população um para um                              |
| Nómada     | FNO      | madeira    | 10         | 100 – 15,000         | 0 – 1,000      | Um povo nómada: vastos povoados de tendas atrás de quase nenhuma muralha — dez degraus baratos e rápidos que nunca se tornam fortaleza |
| Orc        | FOR      | madeira    | 10         | 1,000 – 50,000       | 0 – 12,000     | Vasto, fervilhante e **sem muralhas até ao Nv.4** — a horda é a defesa                                                 |
| Genérico   | POP      | pedra      | 20         | 100 – 50,000         | 0 – 12,000     | Aldeias não alinhadas que o GM espalha como terreno neutro; **sem muralhas até ao Nv.5**                               |

**O Orc começa abaixo do seu próprio primeiro degrau.** Um povoado Orc fundado abre num escalão **Nível 0** sem muralhas, abaixo do Nv.1; todas as outras famílias, incluindo os Nómadas, fundam diretamente no Nv.1 (§3.7.4).

**3.7.1a As Escadas Completas — todas as famílias, todos os níveis (The Full Ladders)**

Os números completos por nível, diretamente da CONSTR_TABLE do Processador de Turnos (que continua a ser a autoridade se esta página e o código alguma vez divergirem). O **Custo** é o ouro pago por esse degrau — na altura da melhoria pagas adicionalmente o **incremento de muralha** no material de construção da família (madeira ou pedra; uma muralha da família Anã custa metade dos seus pontos em pedra, §2.11.7). Uma muralha de — significa um povoado aberto, sem muralhas. Estas escadas são também o teu livro de códigos para a espionagem: um relatório de espião nunca nomeia o escalão de um povoado (§2.15), mas o seu máximo exato de muralha mais a raça do dono lê-se diretamente nestas tabelas.

**Imperial (FI — pedra)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Nv** | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1      | 100                    | 500          | 0               |
| 2      | 200                    | 500          | 500             |
| 3      | 300                    | 500          | 500             |
| 4      | 400                    | 500          | 500             |
| 5      | 500                    | 500          | 500             |
| 6      | 600                    | 500          | 500             |
| 7      | 700                    | 500          | 500             |
| 8      | 800                    | 500          | 500             |
| 9      | 900                    | 500          | 500             |
| 10     | 1,000                  | 500          | 500             |
| 11     | 2,000                  | 1,000        | 4,000           |
| 12     | 3,000                  | 1,500        | 14,000          |
| 13     | 4,000                  | 2,000        | 14,500          |
| 14     | 6,000                  | 3,000        | 15,000          |
| 15     | 8,000                  | 4,000        | 16,000          |
| 16     | 10,000                 | 5,000        | 25,000          |
| 17     | 20,000                 | 10,000       | 45,000          |
| 18     | 30,000                 | 15,000       | 160,000         |
| 19     | 40,000                 | 20,000       | 180,000         |
| 20     | 50,000                 | 25,000       | 200,000         |

**Bárbaro (FBA — pedra)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Nv** | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1      | 100                    | 500          | 0               |
| 2      | 200                    | 500          | 500             |
| 3      | 300                    | 500          | 500             |
| 4      | 400                    | 500          | 500             |
| 5      | 500                    | 500          | 500             |
| 6      | 600                    | 500          | 500             |
| 7      | 700                    | 500          | 500             |
| 8      | 800                    | 500          | 500             |
| 9      | 900                    | 500          | 500             |
| 10     | 1,000                  | 500          | 500             |
| 11     | 2,000                  | 600          | 2,000           |
| 12     | 3,000                  | 900          | 12,000          |
| 13     | 4,000                  | 1,200        | 12,500          |
| 14     | 5,000                  | 1,500        | 13,000          |
| 15     | 7,000                  | 2,000        | 13,500          |
| 16     | 10,000                 | 3,000        | 22,000          |
| 17     | 13,000                 | 4,000        | 34,000          |
| 18     | 16,000                 | 4,750        | 35,000          |
| 19     | 18,000                 | 5,500        | 36,000          |
| 20     | 20,000                 | 6,000        | 38,000          |

**Elfo (FLF — pedra)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Nv** | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1      | 100                    | 200          | 0               |
| 2      | 200                    | 200          | 250             |
| 3      | 500                    | 400          | 500             |
| 4      | 1,000                  | 800          | 1,750           |
| 5      | 1,500                  | 1,200        | 4,500           |
| 6      | 2,000                  | 1,600        | 5,000           |
| 7      | 3,000                  | 2,500        | 5,500           |
| 8      | 5,000                  | 4,000        | 6,000           |
| 9      | 8,000                  | 6,500        | 11,000          |
| 10     | 10,000                 | 8,000        | 28,000          |

**Anão (FDW — pedra)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Nv** | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1      | 100                    | 1,000        | 0               |
| 2      | 200                    | 1,000        | 250             |
| 3      | 500                    | 1,000        | 500             |
| 4      | 1,000                  | 1,800        | 1,000           |
| 5      | 1,500                  | 2,750        | 1,500           |
| 6      | 2,000                  | 3,500        | 2,000           |
| 7      | 3,000                  | 5,500        | 3,000           |
| 8      | 5,000                  | 9,000        | 4,000           |
| 9      | 8,000                  | 14,500       | 5,000           |
| 10     | 10,000                 | 18,000       | 6,000           |

**Aesir (FAS — madeira)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Nv** | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1      | 100                    | 500          | 0               |
| 2      | 200                    | 500          | 250             |
| 3      | 500                    | 500          | 250             |
| 4      | 1,000                  | 1,000        | 1,250           |
| 5      | 1,500                  | 1,500        | 3,500           |
| 6      | 2,000                  | 2,000        | 4,000           |
| 7      | 3,000                  | 3,000        | 4,500           |
| 8      | 5,000                  | 5,000        | 5,000           |
| 9      | 8,000                  | 8,000        | 8,000           |
| 10     | 10,000                 | 10,000       | 22,000          |

**Nómada (FNO — madeira)** *(dez degraus, paliçadas de madeira, sem escalão de fundação — o Nv.1 é o acampamento de colonos.)*

|                                           |                        |              |                 |
|-------------------------------------------|------------------------|--------------|-----------------|
| **Nv**                                    | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1 *(acampamento de colonos — o que a fundação planta)* | 100                    | 0            | 0               |
| 2                                         | 500                    | 100          | 500             |
| 3                                         | 1,000                  | 200          | 750             |
| 4                                         | 1,500                  | 300          | 1,500           |
| 5                                         | 2,000                  | 400          | 2,000           |
| 6                                         | 3,000                  | 500          | 4,000           |
| 7                                         | 4,000                  | 600          | 7,000           |
| 8                                         | 6,000                  | 700          | 12,000          |
| 9                                         | 10,000                 | 800          | 20,000          |
| 10                                        | 15,000                 | 1,000        | 30,000          |

Uma muralha Nómada nunca excede 1,000 pontos, pelo que o bónus de fortaleza (§5.6.1) fica perto de ×1.6; um único golpe de máquina de cerco (250 pontos) arrasa uma paliçada Nv.2 ou Nv.3, e dois golpes arrasam qualquer muralha até ao Nv.6. É essa a intenção: os Nómadas seguram terreno com gente e cavaleiros, não com muralhas. O material é a madeira, não a pedra — e os hexágonos de deserto não têm pedreiras nem serrações, pelo que a madeira vem de um hexágono de floresta ou do mercado (base 5g).

**Orc (FOR — madeira)**

|                                                                          |                        |              |                 |
|--------------------------------------------------------------------------|------------------------|--------------|-----------------|
| **Nv**                                                                   | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 0 *(escalão de fundação, §3.7.4 — só se atinge por fundação, nunca por melhoria)* | 100                    | —            | —               |
| 1                                                                        | 1,000                  | —            | 250             |
| 2                                                                        | 2,000                  | —            | 10,000          |
| 3                                                                        | 3,000                  | —            | 15,000          |
| 4                                                                        | 4,000                  | 1,000        | 16,000          |
| 5                                                                        | 6,000                  | 1,400        | 18,000          |
| 6                                                                        | 8,000                  | 1,900        | 22,000          |
| 7                                                                        | 10,000                 | 2,500        | 24,000          |
| 8                                                                        | 20,000                 | 4,750        | 26,000          |
| 9                                                                        | 30,000                 | 7,250        | 100,000         |
| 10                                                                       | 50,000                 | 12,000       | 120,000         |

**Genérico (POP — pedra)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Nv** | **Limite de população** | **Muralha máx.** | **Custo (ouro)** |
| 1      | 100                    | —            | 0               |
| 2      | 200                    | —            | 1,250           |
| 3      | 300                    | —            | 2,000           |
| 4      | 400                    | —            | 2,000           |
| 5      | 500                    | 100          | 2,000           |
| 6      | 600                    | 100          | 2,000           |
| 7      | 700                    | 200          | 2,000           |
| 8      | 800                    | 200          | 2,000           |
| 9      | 900                    | 200          | 2,000           |
| 10     | 1,000                  | 200          | 2,000           |
| 11     | 2,000                  | 500          | 3,000           |
| 12     | 3,000                  | 700          | 14,000          |
| 13     | 4,000                  | 1,000        | 15,000          |
| 14     | 6,000                  | 1,400        | 16,000          |
| 15     | 8,000                  | 1,900        | 26,000          |
| 16     | 10,000                 | 2,500        | 28,000          |
| 17     | 20,000                 | 4,750        | 30,000          |
| 18     | 30,000                 | 7,250        | 130,000         |
| 19     | 40,000                 | 9,500        | 140,000         |
| 20     | 50,000                 | 12,000       | 150,000         |

A Página do Jogador mostra o degrau atual e o seguinte de cada construção que possuis.

**O Genérico (POP) é a escada universal.** Não pertence a nenhuma raça e — caso único — **qualquer dono a pode melhorar** (§2.11.7). Todas as outras famílias respondem apenas ao seu próprio povo.

**3.7.2 A Muralha (The Wall)**

A muralha de uma construção tem um **máximo** (definido pela sua família e nível) e um valor **atual**, a *integridade* da muralha. Uma construção nova está com integridade total. As máquinas de cerco derrubam-na (§5.8.6); a ordem repair_wall reconstrói-a (§2.11.8).

A integridade não é cosmética — ajusta continuamente o bónus de fortaleza do defensor (§5.6.1). Um povoado cuja muralha foi reduzida a zero está **em brecha**, e combate como se não tivesse muralhas de todo.

As famílias cujos níveis baixos indicam uma muralha de **0** (Orc Nível 0–3, Genérico Nv.1–4, Nómada Nv.1) não têm muralha para danificar, nem bónus de fortaleza, nem nada para reparar. São povoados abertos.

**3.7.3 A Capital (Capital)**

A capital não é um tipo de terreno nem "o maior povoado" — é um **hexágono específico que o GM designa** ao construir o mapa. Essa designação passa a ser a **sede de recrutamento (muster seat)** do reino: onde um exército baseado na capital é recrutado, e o hexágono a que o banner do perfil chama a tua Capital.

Uma sede **Nómada (Nomad)** também se desloca quando o acampamento onde se encontra se move (§2.11.10). Se a sede designada se perder, é sucedida pela escada pegajosa de **§2.13.10**, que define também as vantagens defensivas da sede (+0.10 de bónus de fortaleza, 6 turnos de cerco mantido em vez de 5). Na Página do Jogador (Player Page), a sede é marcada com uma **★ dourada** (com contorno preto) nos três mapas — o mapa do reino, o mapa de Exércitos e o mapa da Marinha — para **todas as sedes que consigas ver**, a tua com força total e as estrangeiras esbatidas com a tonalidade da visão de fronteira (as localizações das sedes são públicas para a visão de fronteira). A estrela ignora os interruptores das camadas do mapa: tal como o nevoeiro, o marcador da capital desenha-se sempre.

**3.7.4 Fundar uma Nova Construção (Founding a New Construction)**

O GM não é o único que pode pôr um povoado no mapa. Assim que exista pelo menos uma construção em qualquer lugar, qualquer reino pode fundar novas construções próprias em terreno livre que detenha — a ordem completa é §2.11.9. Esta secção cobre o que a fundação significa para as escadas de famílias acima.

**Uma escolha permanente.** Fundar planta um povoado de uma família — a da tua própria raça, ou a escada neutra **Generic** — e essa família nunca mais muda. A conquista pode degradar o nível de uma construção (§5.6.3) ou bloqueá-la contra as tuas próprias melhorias se não a construíste tu (§2.11.7), mas nada a move alguma vez para a escada de outra família.

**De onde vêm os colonos, e para onde não podem ir.** Fundar retira 100 pessoas da tua sede de recrutamento — nunca para a própria sede — e nunca reduz um hexágono (§2.11.9). Para colocar uma construção num hexágono de sede livre tens primeiro de perder a sede ou movê-la — na prática, melhora outra posse até a sucessão mover a sede, ou captura terreno que valha a pena povoar.

**Uma família começa abaixo do Nível 1.** Os povoados Orc têm 1,000 de população no seu primeiro degrau da tabela — iniciar aí uma fundação nova abriria com um décimo da capacidade. Em vez disso, fundam num escalão de **Nível 0** mantido fora da escada de família acima (§3.7.1a): 100 de população, sem muralha, alcançado apenas por fundação — nunca por melhoria, e nunca pintado pelo GM. Todas as outras famílias fundam diretamente no Nível 1.

Subir do Nível 0 para o Nível 1 é uma melhoria vulgar (§2.11.7) com preços vulgares, lidos na escada da própria família: a população tem primeiro de atingir o teto do Nível 0 de **100**, e depois custa o **preço em ouro do Lv.1 listado — 250g para Orc** — mais a muralha que o novo nível introduz. *(Os Nómadas não têm Nível 0: FNO1 é o degrau de colonos e FNO1 → FNO2 é uma melhoria vulgar de 500g + 100 wood.)* Como o Nível 0 não tem muralha, esse incremento é a muralha toda do Lv.1: **absolutamente nada para Orc** (FOR1 também não tem muralha). Repara no que a melhoria dá a um Orc: o teto de população salta de 100 diretamente para 1,000.

**O turno de fundação é um feriado de fortificação.** Uma construção fundada neste turno combate como terreno aberto até ao turno seguinte, embora a sua muralha seja real desde o início (§2.11.9).

**3.8 Mecânica da População (Population Mechanics)**

A população vive **apenas dentro de construções**. A cada turno, uma construção abaixo do teto do seu nível cresce em:

growth = max(1, round(rate × ceiling)) rate = 1–3%, rolled per hex per turn

population = min(ceiling, population + growth)

rate é 0.01 + rand×0.02, pelo que o crescimento é 1–3% do teto, nunca inferior a 1. O **teto de população (population ceiling)** é definido pelo **nível de construção** do hexágono, não pelo terreno (§3.7.1), e vai de 100 (uma posse Imperial, Bárbara, Élfica, Anã, Aesir ou Generic de primeiro degrau, ou um acampamento Orc de Nível 0 ou um acampamento Nómada Lv.1) até 50,000 (uma Imperial, Orc ou Generic no máximo). No início da campanha o GM pinta todas as construções no Editor de Mapas e cada uma começa no **teto completo** do seu nível. Um hexágono de construção drenado a 0 volta a crescer a partir de 0 pela mesma regra — nunca é reposto de imediato no teto.

Duas consequências que vale a pena interiorizar:

- O crescimento mede-se face ao **teto do nível que pagaste**, não face à população atual, pelo que um povoado cresce a um ritmo absoluto constante até saturar (uma cidade com teto de 50,000 pode acrescentar até +1,500 por turno). Um povoado grande um degrau acima na escada cresce em passos absolutos maiores do que um pequeno — subir de nível acelera-te, e ficar parado estagna-te no teto.

- O crescimento **satura e pára** no teto; nunca o ultrapassa por si só. A população *acima* do teto (que a degradação por conquista pode deixar para trás, §5.6.3) fica exatamente onde está — nunca é reduzida, nunca cresce.

- Um **acampamento Nómada movido** leva consigo as suas gentes e o seu teto, e deixa o hexágono antigo a zero (§2.11.10).

> ***⚠ A consequência que mais dói.** Como o crescimento pára de vez no teto, uma sede de recrutamento cujo nível comporte menos de 300 pessoas **nunca** poderá enviar colonos até que a própria sede seja melhorada (§2.11.9).*

**Os hexágonos livres nunca crescem, porque nunca tiveram população.** (Um mapa antigo sem qualquer construção continua a usar o antigo caminho do terreno: a população base do terreno só é semeada quando um hexágono **não** tem campo de população; um hexágono **drenado a 0** nunca é ressemeado e cresce por max(1, floor(pop × rate)) → 1, depois 1–3%.)

A população determina:

- Rendimento de imposto: floor(totalPop × taxRate / 100) ouro (§2.9.5)

- Produção dos locais de produção — comida da quinta, ouro e comida do porto, ferro da mina, madeira da serração, pedra da pedreira (§3.6.1–§3.6.6; portos §2.9.4)

- Força da milícia: floor(pop × 0.05) unidades de milícia (5% da população) a 20 WP cada

- Estimativas dos relatórios de espiões

- O **portão de melhoria**: uma construção só pode subir de nível quando a sua população tiver atingido o teto atual (§2.11.7)

Todo o local de produção rende **0 se a população do hexágono for 0** — o que, nesta era, significa que todos os locais de produção num hexágono livre não produzem absolutamente nada. Num hexágono *povoado*, um local rende **pelo menos 1**, exceto a comida sorteada de um porto, que pode sair 0% e não pagar nada (§2.9.4).

A população também é gasta em recrutas (Pré-Fase 2b, antes do crescimento) e em tripulações de navios (Fase 4, depois do crescimento) — nunca em máquinas de cerco (§2.12.1, §2.12.3).

> ***▶ Exemplo — quando o teto corta o crescimento.** A capital de um reino tem 6,866 pessoas sob um teto de 7,000; todos os outros povoados já estão cheios. Neste turno a capital cresce 1–3% do seu **teto** — 70 a 210 pessoas — mas só cabem mais 134, pelo que o ganho é de 70 a 134. O Perfil diz exatamente isso: 18,866 (+70–134 /turn) · only (60,65) has room to grow — 134 more people · 9 settlements are full: upgrade them to grow. No turno seguinte a capital também está cheia, e o reino pára de crescer até que um povoado seja melhorado para um nível com teto mais alto.*

**PARTE IV — RAÇAS (RACES)**

**4.1 Visão Geral das Raças e Assimetria (Race Overview and Asymmetry)**

|           |                  |                   |                                                                |
|-----------|------------------|-------------------|----------------------------------------------------------------|
| **Raça**  | **Terreno Natal** | **Bónus de Terreno** | **Mecânica Especial**                                       |
| Imperial  | — (nenhum)       | —                 | Nenhuma                                                        |
| Bárbaro   | Colinas          | ×1.15             | Nenhuma                                                        |
| Elfo      | Floresta         | ×1.30             | Nenhuma                                                        |
| Orc       | Pântano          | ×1.20             | Reprodução de infantaria (só em pântano); fome severa          |
| Anão      | Montanha         | ×1.30             | Dependência de ferro em todas as unidades                      |
| Aesir     | — (nenhum)       | —                 | Bónus de ×1.05 em batalhas de frota (§5.9.2); o único casco de 120 MP do jogo |
| Nómada    | Deserto          | ×1.25             | Deserto atravessado a 30 MP quando todos os outros pagam 60 (§2.13.2) |

**4.2 Imperial**

**Sem bónus de terreno — a Legião mantém antes as suas muralhas.** O bónus assenta em **construções, posse e papel**, não no terreno. Um reino Imperial **a defender um hexágono que possui** cuja construção seja da família Imperial (FI) ou da linhagem POP rola a **×1.10** — guarnição (garrison) sob assalto, surtida (sally), batalha de campo nesse hexágono e defesa de praia por igual, e a milícia do hexágono usa o mesmo multiplicador. Nunca se aplica como atacante — exceto numa surtida ordenada a partir das suas próprias muralhas (§2.13.7) — nunca num hexágono que o Imperial não possua no momento da batalha, nunca no povoado de outra família (um acampamento Orc capturado não rende nada), e nunca para um aliado que defenda a seu lado (o bónus é por exército). Acumula multiplicativamente com a postura, o terreno e o bónus de fortaleza, e como todos os bónus de terreno aplica-se só ao lado da rolagem: classificações, estimativas de espiões e o portão de capacidade de cerco nunca o veem. Em terreno aberto o Imperial continua a combater sem bónus, como os Aesir. O registo do cartão de batalha mostra-o como a linha da legião.

**Lista de Unidades:**

|                       |         |         |        |                        |            |        |             |
|-----------------------|---------|---------|--------|------------------------|------------|--------|-------------|
| **Unidade**           | **ATK** | **DEF** | **HP** | **Custo**              | **Manutenção** | **WP** | **Montada** |
| Velites               | 5       | 5       | 8      | 50g, 8f, 6w            | —          | 43     | Não         |
| Legionnaire           | 7       | 9       | 11     | 60g, 1i, 8f, 5w        | —          | 67     | Não         |
| Sagitarii             | 9       | 5       | 9      | 150g, 20i, 5f, 1h, 10w | 4g         | 121    | Sim         |
| Equites               | 11      | 7       | 13     | 200g, 40i, 1h, 3w      | 8g         | 192    | Sim         |
| Praetorians           | 10      | 10      | 16     | 300g, 100i, 10f, 5w    | 12g        | 356    | Não         |
| Onager (máquina de cerco) | 1       | 1       | 8      | 250g, 10i, 50w         | 3g         | 10     | Não         |

**Lista de Navios:**

|          |         |         |              |                 |            |        |        |
|----------|---------|---------|--------------|-----------------|------------|--------|--------|
| **Navio** | **ATK** | **DEF** | **Capacidade** | **Custo**     | **Manutenção** | **WP** | **MP** |
| Drommund | 6       | 5       | 100          | 155g, 9i, 50w   | 4g         | 66     | 90     |
| Cog      | 10      | 8       | 200          | 310g, 24i, 90w  | 8g         | 108    | 60     |
| Galley   | 12      | 11      | 300          | 550g, 36i, 130w | 15g        | 138    | 60     |

**4.3 Bárbaro (Barbarian)**

A infantaria recrutável mais barata de todas as raças. Raiders e Berserkers custam 40–50g sem manutenção de ouro nem de ferro — mas continuam a comer comida por cabeça (§2.10.4). Teto de ATK elevado; DEF moderada. Storm Horses custa 120g (mais 1 cavalo, como todas as unidades montadas exceto o Warg Rider Orc) — mais barato do que toda a outra cavalaria exceto o Bedouin Nómada (90g) e o Warg Rider Orc (100g).

**Lista de Unidades:**

|                              |         |         |        |                     |            |        |             |
|------------------------------|---------|---------|--------|---------------------|------------|--------|-------------|
| **Unidade**                  | **ATK** | **DEF** | **HP** | **Custo**           | **Manutenção** | **WP** | **Montada** |
| Raiders                      | 7       | 4       | 10     | 50g, 15f, 4w        | —          | 48     | Não         |
| Berserker                    | 8       | 5       | 12     | 40g, 10f, 2w        | —          | 55     | Não         |
| Wild Archer                  | 10      | 8       | 13     | 220g, 12i, 20f, 12w | 5g         | 120    | Não         |
| Storm Horses                 | 13      | 7       | 13     | 120g, 8f, 1h, 3w    | 4g         | 85     | Sim         |
| Warchief                     | 15      | 10      | 18     | 350g, 20i, 30f, 4w  | —          | 179    | Não         |
| Stone-Thrower (máquina de cerco) | 1       | 1       | 8      | 250g, 10i, 50w      | 3g         | 10     | Não         |

**Lista de Navios:**

|          |         |         |              |                      |            |        |        |
|----------|---------|---------|--------------|----------------------|------------|--------|--------|
| **Navio** | **ATK** | **DEF** | **Capacidade** | **Custo**          | **Manutenção** | **WP** | **MP** |
| Wolfship | 8       | 4       | 80           | 135g, 8i, 10f, 45w   | 3g         | 72     | 90     |
| Reaver   | 11      | 5       | 120          | 245g, 13i, 15f, 65w  | 5g         | 96     | 90     |
| Tigress  | 14      | 7       | 200          | 435g, 22i, 25f, 100w | 14g        | 126    | 60     |

*(O casco Bárbaro é o Wolfship; "Longship" é um casco Aesir, §4.7.)*

**4.3.1 Pirata — subconjunto Bárbaro (Pirate — Barbarian subset)**

**Pirata não é uma raça completa** — é um *subconjunto* de sabor da raça Bárbara, definido por reino no Editor de Mapas (seletor de raça → Pirate; guardado como race:'Barbarian' mais uma flag pirate:true). Um reino Pirata joga exatamente como um reino Bárbaro — mesmas listas de unidades e navios, custos, comida, bónus de terreno, e a mesma exclusão de emboscada (ambush) — com apenas estas diferenças (e uma postura de frota exclusiva dos Piratas, Caça (Hunt)):

- **Bónus de batalha naval ×1.10** — as frotas piratas multiplicam o seu WP de batalha de frota por 1.10. Apenas batalhas de frota: sem efeito em desembarques anfíbios, bloqueios, ataques de saque, movimento ou combate terrestre.

- **Heráldica e aspeto próprios** — escudos piratas (shield-pirate-N, com a sua própria numeração), logótipo e arte de batalha (a arte pirata em falta recorre à arte Bárbara); uma paleta de UI pirata (carta náutica desgastada no tema claro, caveira e ossos negro-alcatrão no escuro); e nomes de forças piratas — os exércitos são recrutados como **CREW**, as frotas como **FLOTILLA**.

- **Títulos próprios** — Haven of / Brotherhood of / Cove of / Crew of (independente / suserano / vassalo / vassalo-de-um-vassalo).

- **Etiqueta** — a UI mostra a raça como **Pirata** sempre que diria Bárbaro.

- **Postura de Caça** — só as frotas Piratas podem adotar a Caça: uma frota em caça ataca uma frota que encontre e julgue mais fraca, e não é declarada nenhuma guerra (§2.14.9).

**4.4 Elfo (Elf)**

Elite, cara, dependente de ferro. **O Swordmaster não tem manutenção de ouro** — paridade de manutenção: todas as raças têm uma unidade de linha sem manutenção. Só os Swordmasters/Bladedancers custam comida a recrutar, mas os exércitos Elfos continuam a comer comida por cabeça e passam fome sem ela (§2.10.4). Todos os navios Elfos têm manutenção apenas em ouro.

**Lista de Unidades:**

|                               |         |         |        |                   |            |        |             |
|-------------------------------|---------|---------|--------|-------------------|------------|--------|-------------|
| **Unidade**                   | **ATK** | **DEF** | **HP** | **Custo**         | **Manutenção** | **WP** | **Montada** |
| Swordmaster                   | 11      | 6       | 9      | 100g, 14i, 5f     | —          | 100    | Não         |
| Bladedancer                   | 12      | 7       | 11     | 160g, 25i, 5f     | 6g         | 139    | Não         |
| Ranger                        | 9       | 11      | 12     | 220g, 37i, 12w    | 8g         | 174    | Não         |
| Elven Cavalry                 | 12      | 13      | 22     | 300g, 55i, 1h, 3w | 10g        | 247    | Sim         |
| High Guard                    | 15      | 12      | 18     | 400g, 104i, 3w    | 14g        | 362    | Não         |
| Great Ballista (máquina de cerco) | 1       | 1       | 8      | 250g, 10i, 50w    | 3g         | 10     | Não         |

**Lista de Navios:**

|            |         |         |              |                |            |        |        |
|------------|---------|---------|--------------|----------------|------------|--------|--------|
| **Navio**  | **ATK** | **DEF** | **Capacidade** | **Custo**    | **Manutenção** | **WP** | **MP** |
| Moonskiff  | 7       | 6       | 60           | 170g, 4i, 40w  | 5g         | 78     | 90     |
| White Ship | 10      | 9       | 100          | 295g, 7i, 60w  | 8g         | 114    | 90     |
| Swan Ship  | 16      | 8       | 150          | 545g, 13i, 85w | 16g        | 144    | 60     |

**Portos entre as árvores.** Só os Elfos podem construir um **porto num hexágono de floresta costeira**, além de em planícies costeiras — mas apenas onde a construção do hexágono seja Élfica (§2.11.1). **O hexágono continua floresta**, pelo que o teu bónus de terreno natal de ×1.30 defende esse porto em terra — um porto Élfico é o porto mais bem defendido do mundo, e o único cujo solo luta por ele.

**4.5 Orc**

A infantaria reproduz-se passivamente (5–7% por exército por turno se a infantaria for ≥ 10 **e o exército estiver num hexágono de pântano**, §2.9.10), e a reprodução que leve a tua infantaria total para além de 300 / 500 / 1000 é anunciada a todos os rivais. A fome é desproporcionadamente severa (10–20% vs 3–10%). As unidades Orc têm pouca ou nenhuma manutenção de ouro, mas comem comida por cabeça (§2.10.4), e o recrutamento e a reprodução, pesados em comida, fazem da comida a restrição central.

> ***⚠ O que isto significa — alimenta a horda ou vê-la apodrecer.** Um Orc pode fazer crescer em campo um exército que nunca precisou de recrutamento pago completo, mas uma horda em crescimento come mais a cada turno — constrói quintas e acumula comida antes da curva de crescimento, ou a fome apagará os soldados que a reprodução acabou de te dar.*

**Lista de Unidades:**

|                             |         |         |        |                |            |        |             |
|-----------------------------|---------|---------|--------|----------------|------------|--------|-------------|
| **Unidade**                 | **ATK** | **DEF** | **HP** | **Custo**      | **Manutenção** | **WP** | **Montada** |
| Goblin                      | 8       | 5       | 9      | 30g, 12f, 2w   | —          | 51     | Não         |
| Orc                         | 13      | 6       | 15     | 150g, 20f, 3w  | 3g         | 88     | Não         |
| Orc Archer                  | 11      | 10      | 20     | 200g, 25f, 10w | —          | 104    | Não         |
| Warg Rider                  | 7       | 4       | 8      | 100g, 10f, 2w  | 4g         | 51     | Sim         |
| Uruk-Hai                    | 12      | 5       | 11     | 180g, 18f, 4w  | —          | 80     | Não         |
| War Catapult (máquina de cerco) | 1       | 1       | 8      | 250g, 10i, 50w | 3g         | 10     | Não         |

**Capacidade de frota**: os reinos Orc não podem construir nem encomendar frotas.

**4.6 Anão (Dwarf)**

Ferro primeiro. Todas as unidades requerem ferro para produção; várias requerem manutenção de ferro. Os Anões continuam a comer comida por cabeça e passam fome como qualquer raça sem ela (§2.10.4). Os Thunderers têm o ATK mais alto de qualquer unidade do jogo (16). Os Anões em terreno de montanha são uma fortaleza defensiva. Só os engenheiros Anões conseguem abrir um poço de mina de Nível 3 (§3.6.2) — todos os filões mais profundos do mundo foram escavados por Anões, e as minas Anãs capturadas são conquistas preciosas.

**O Ironclad não tem manutenção de ouro** — paridade de manutenção: todas as raças têm uma unidade de linha sem manutenção.

**Lista de Unidades:**

|                          |         |         |        |                |            |        |             |
|--------------------------|---------|---------|--------|----------------|------------|--------|-------------|
| **Unidade**              | **ATK** | **DEF** | **HP** | **Custo**      | **Manutenção** | **WP** | **Montada** |
| Warrior                  | 7       | 12      | 14     | 100g, 15i, 3w  | 3g, 1i     | 118    | Não         |
| Ironclad                 | 11      | 6       | 8      | 90g, 10i, 2w   | —          | 93     | Não         |
| Crossbowman              | 6       | 8       | 10     | 150g, 20i, 10w | 5g         | 117    | Não         |
| Thunderers               | 16      | 5       | 8      | 320g, 70i, 8w  | 10g, 3i    | 278    | Não         |
| Heartguard               | 12      | 12      | 16     | 240g, 50i, 3w  | 6g, 2i     | 237    | Não         |
| Trebuchet (máquina de cerco) | 1       | 1       | 8      | 250g, 10i, 50w | 3g         | 10     | Não         |

**Capacidade de frota**: os reinos Anões não podem construir nem encomendar frotas.

**Forja (Forge)**: colocada pelo GM no início da campanha numa construção Anã (FDW); um exército estacionário aí ganha +2% xp_wp por turno (§3.6.4, §5.3.2).

**4.7 Aesir**

Saqueadores marítimos dos fiordes gelados. Os Aesir põem em campo um exército **inteiramente de infantaria** — sem unidades montadas e **sem dependência de cavalos em toda a raça** — com uma lista de custo médio cujo topo (Jarl's Guard, WP 240) fica entre o Bárbaro e o Anão. Em terra são deliberadamente simples: **sem bónus de terreno natal e com custos de movimento normais**. Toda a sua vantagem está no mar: um **bónus de ×1.05 em batalhas de frota** em cada rolagem naval (§5.9.2), o **único casco de 120 MP** do jogo (uma frota inteira de Snekkja navega **4 hexágonos de mar** por turno — a coisa mais rápida a flutuar), e o porão de capacidade 220 do Busse para desembarcar um bando de guerra completo. Joga-os como saqueadores: ataca a partir da água, e lembra-te de que a penalização universal de ×0.50 na praia (§5.7) continua a aplicar-se quando desembarcas.

**Lista de Unidades:**

|                           |         |         |        |                    |            |        |             |
|---------------------------|---------|---------|--------|--------------------|------------|--------|-------------|
| **Unidade**               | **ATK** | **DEF** | **HP** | **Custo**          | **Manutenção** | **WP** | **Montada** |
| Shore Raider              | 7       | 4       | 10     | 42g, 15f, 5w       | —          | 48     | Não         |
| Axe Thane                 | 9       | 6       | 12     | 76g, 3i, 15f, 3w   | 2g         | 75     | Não         |
| Shield-Karl               | 7       | 10      | 13     | 119g, 16i, 8w      | 4g         | 110    | Não         |
| Huscarl                   | 12      | 9       | 15     | 204g, 20i, 20f, 6w | 6g         | 170    | Não         |
| Jarl's Guard              | 14      | 11      | 17     | 289g, 32i, 30f, 6w | 10g        | 240    | Não         |
| Valslöngva (máquina de cerco) | 1       | 1       | 8      | 250g, 10i, 50w     | 3g         | 10     | Não         |

**Lista de Navios:**

|          |         |         |              |                      |            |        |         |
|----------|---------|---------|--------------|----------------------|------------|--------|---------|
| **Navio** | **ATK** | **DEF** | **Capacidade** | **Custo**          | **Manutenção** | **WP** | **MP**  |
| Snekkja  | 8       | 4       | 80           | 120g, 9i, 10f, 45w   | 3g         | 72     | **120** |
| Longship | 12      | 6       | 140          | 300g, 20i, 20f, 75w  | 8g         | 112    | 90      |
| Busse    | 14      | 9       | 220          | 490g, 31i, 30f, 105w | 14g        | 136    | 60      |

**Bónus naval**: cada frota Aesir multiplica a sua rolagem de batalha por **×1.05** — atacante ou defensor, mar ou porto (§5.9.2). Aplica-se apenas à rolagem: o WP de frota apresentado, a manutenção e as classificações não são afetados.

**4.8 Nómada (Nomad)**

> ***Os cavaleiros do deserto comem como peões.** Uma unidade **montada** Nómada consome **1 comida por cabeça**, e não as 2 que a cavalaria de todas as outras raças paga. Duas das seis unidades Nómadas são cavaleiros — o Bedouin e o Askari — e têm os mais baixos pontos de guerra por cabeça de toda a cavalaria do jogo, pelo que o suplemento padrão para unidades montadas cobrava-lhes rações a dobrar precisamente às tropas que já precisavam de mais corpos. Cavaleiros que vivem da terra obedecem à mesma lógica que concede o bónus de 1.25 no deserto.*
>
> ***Os acampamentos movem-se.** Um acampamento FNO por turno pode levantar as tendas e voltar a montá-las até 2 hexágonos de distância, em terras tuas, por 1,000g, descansando 6 turnos entre deslocações — o povo e a paliçada viajam, os locais de produção (sites) ficam para trás e ficam inativos. Nenhum outro povo o pode fazer. Regras completas em §2.11.10.*

O Sultanato do deserto — cavaleiros velozes e comerciantes pacientes ao modelo dos Aiúbidas. O exército mais barato do jogo: o Rajjala custa 20g (mais 2 de madeira para a lança) e é concebido **deliberadamente um pouco acima da milícia** (WP 26 contra os 20 por cabeça da milícia), e o teto do elenco (Askari, WP 143) é o mais baixo de qualquer raça. Os Nómadas vencem pela economia de atrito e por dominarem a areia: **deserto ×1.25 em batalha** e **deserto atravessado a 30 MP** onde todas as outras raças pagam 60 — um exército Nómada de infantaria faz 2 hexágonos de deserto por turno, uma força toda montada de Bedouin/Askari faz 3, enquanto os invasores se arrastam a 1. A areia também esconde minério: os hexágonos de deserto podem ser prospetados em busca de minas (7% de probabilidade, limite Lv2 — §3.6.2), transformando dunas de resto mortas num modesto rendimento de ferro que nenhum rival se dará ao trabalho de atravessar o deserto para tomar. A sua marinha é uma frota utilitária modesta: o Dhow transporta tropas a baixo custo, e o brulote Harraqa ferroa muito acima da sua tonelagem, mas não aguenta um golpe.

**Elenco de Unidades (Unit Roster):**

|                         |         |         |        |                   |            |        |             |
|-------------------------|---------|---------|--------|-------------------|------------|--------|-------------|
| **Unidade**             | **ATK** | **DEF** | **HP** | **Custo**         | **Manutenção** | **WP** | **Montada** |
| Rajjala                 | 4       | 3       | 6      | 20g, 8f, 2w       | —          | 26     | Não         |
| Naffatun                | 7       | 4       | 8      | 40g, 10f, 5w      | —          | 50     | Não         |
| Rumat                   | 9       | 5       | 9      | 90g, 5i, 15f, 10w | 2g         | 86     | Não         |
| Bedouin                 | 10      | 5       | 10     | 90g, 8f, 1h, 6w   | 3g         | 88     | Sim         |
| Askari                  | 11      | 8       | 12     | 180g, 10f, 1h, 4w | 5g         | 143    | Sim         |
| Mangonel (engenho de cerco) | 1   | 1       | 8      | 250g, 10i, 50w    | 3g         | 10     | Não         |

**Elenco de Navios (Ship Roster):**

|          |         |         |              |                   |            |        |        |
|----------|---------|---------|--------------|-------------------|------------|--------|--------|
| **Navio** | **ATK** | **DEF** | **Capacidade** | **Custo**       | **Manutenção** | **WP** | **MP** |
| Dhow     | 6       | 4       | 100          | 145g, 2i, 5f, 50w | 3g         | 56     | 90     |
| Shini    | 10      | 6       | 140          | 300g, 10i, 70w    | 6g         | 98     | 60     |
| Harraqa  | 13      | 5       | 60           | 360g, 5i, 45w     | 10g        | 116    | 60     |

> ***▶ Nota do GM sobre o desenho do mapa (ambas as novas raças).** Um reino Aesir **tem** de receber hexágonos de porto costeiros na criação do mapa, ou toda a sua identidade racial (marinha, pilhagem, o casco de 120 MP) fica inalcançável — o inverso da regra de "sem portos para Orc/Anão". (Um reino Elfo exige menos cuidado: uma costa de floresta basta, desde que os seus hexágonos de floresta costeira tenham construções Élficas — pinta-os com a família Elfo, §2.11.1.) Convém também um hexágono ou dois de **floresta**: cada casco custa madeira, e uma frota Aesir sem florestas vive do mercado, do tributo e da pilhagem (temático, mas uma dificuldade deliberada). Um reino Nómada deve possuir ou confinar com hexágonos de **deserto** pela mesma razão.*

**PART V — UNIDADES E COMBATE (UNITS & COMBAT)**

**5.1 Ler a Ficha de uma Unidade (Reading a Unit Stat Block)**

|           |                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------|
| **Campo** | **Significado**                                                                                            |
| ATK       | Poder de ataque — valor de referência; o WP é o valor de combate                                           |
| DEF       | Poder de defesa — valor de referência                                                                      |
| HP        | Pontos de vida (Hit Points) — valor de referência                                                          |
| Custo     | Recursos para recrutar uma unidade (g=ouro, f=comida, i=ferro, h=cavalos, w=madeira)                       |
| Manutenção | Recursos por unidade por turno (Fase 2)                                                                   |
| WP        | Pontos de Guerra base — o valor de combate real usado em todas as rolagens                                 |
| Montada   | Sim/Não — as unidades montadas consomem 2 comida/turno (a pé 1); as unidades montadas **Nómadas** comem 1, como a pé (§4.8) |

**5.2 Pontos de Guerra: a Moeda de Combate (War Points: The Combat Currency)**

Os **Pontos de Guerra (War Points, WP)** são o único valor de combate em todas as rolagens. ATK, DEF, HP são valores de referência.

WP total do exército: armyWP = sum of (unit.xp_wp × unit.count) across all stacks

unit.xp_wp começa no WP base e aumenta com a experiência de combate.

> ***▶ Exemplo — ler a força de um exército.** Um exército de 40 Legionnaires (WP base 67) e 10 Equites (WP base 192), ainda sem experiência, totaliza armyWP = 40×67 + 10×192 = 2,680 + 1,920 = 4,600 WP. Depois de várias batalhas elevarem os Legionnaires para xp_wp 74, as mesmas pilhas totalizam 40×74 + 10×192 = 4,880 WP — sem novos recrutas. Os Pontos de Guerra, e não o número de cabeças, decidem a matemática: uma força veterana menor pode superar em rolagem uma maior e inexperiente.*

**5.3 Experiência (Experience, xp_wp)**

**5.3.1 Ganho de XP em Batalha (XP Gain from Battle)**

Após qualquer batalha (campal, anfíbia, assalto ou naval), todas as unidades sobreviventes ganham experiência:

- Rolagem: 1 + (0.03 + rand×0.02) × oppFactor — até ×1.03 a ×1.05

- **\`oppFactor = min(1, opponent WP / your WP)\`** — a experiência escala com o quão perigoso o inimigo realmente era. Combater uma força igual ou mais forte concede a rolagem completa; **esmagar uma força simbólica não ensina nada** (contra um inimigo que seja uma fração da tua força, o ganho arredonda a zero). Num assalto, o "oponente" do atacante é a defesa completa — guarnição, milícia e fortaleza em conjunto — pelo que tomar de assalto uma cidade a sério instrui sempre. **A guarnição defensora é medida contra essa mesma defesa completa como o seu próprio "your WP"** — as muralhas atrás das quais se abriga e a milícia que combate a seu lado contam como a sua força, e não apenas as suas próprias tropas. Os dois lados de um assalto leem, portanto, as mesmas duas quantidades, invertidas, tal como já faziam numa batalha campal. Quanto mais fortes as muralhas e maior a população, menos experiência a guarnição obtém.

- new_xp_wp = min(cap, round(xp_wp × roll))

- Ambos os lados ganham experiência independentemente do resultado — o lado em inferioridade, ao combater contra um adversário mais forte, ganha sempre a sua rolagem completa

**As frotas ganham-na da mesma forma (§5.9).** Após cada batalha naval — ganha, perdida ou empatada — cada **pilha de cascos** sobrevivente de cada frota que combateu faz a mesma rolagem 1 + (0.03 + rand×0.02) × oppFactor, uma rolagem por frota aplicada a todas as suas pilhas, limitada a 3 × WP base. Cinco coisas são específicas do mar:

- **\`oppFactor\` é de lado inteiro.** Num combate de coligação, a tua frota mede o lado oposto *inteiro* contra o *teu inteiro* (as somas que decidiram a rolagem), pelo que duas frotas a combater como um só esquadrão ganham a mesma rolagem — nenhuma é "a pequena".

- **Os cascos capturados chegam inexperientes e depois aprendem.** Um navio capturado junta-se a ti com o seu WP base, seja o que for que a sua antiga tripulação soubesse (§2.13.12), e a partir da sua batalha seguinte faz rolagem de XP como qualquer casco teu — o limite é 3× a sua **própria base verdadeira**, pelo que um casco estrangeiro nunca vale mais do que o mesmo casco construído em casa.

- **A veterania é armadura tanto como poder.** O XP de um casco aumenta o seu poder de guerra *e* o seu equivalente em preço na fórmula de baixas (§5.9.3: price × (1 + xp_wp/base − 1)), pelo que os navios veteranos tanto batem mais forte como afundam menos vezes — o mesmo duplo efeito que a infantaria obtém em terra.

- **O ESTADO não é afetado.** A experiência nunca restaura a prontidão; uma frota a 40% após uma luta dura é uma frota veterana a 40% (§5.10.6).

- **O cartão di-lo.** O teu relatório traz uma linha *"Battle XP — Fleet N sailors hardened at sea"* que nomeia o WP antigo e o novo de cada tipo de casco, e o Relatório de Prontidão (Readiness Report) é separado.

Os almirantes ganham experiência de **personagem** nas mesmas batalhas segundo a regra terrestre — um ponto Militar por cada três batalhas comandadas, empates incluídos (§7.10).

> ***▶ Porque existe a escala por oponente.** Sem ela, dois reinos em conluio poderiam cultivar veterania: um alimentaria o anfitrião do outro com exércitos descartáveis de uma só unidade, cada "batalha" concedendo o pleno +3–5%. Com a escala, um sacrifício simbólico vale exatamente nada — a experiência só flui de lutas que foram reais.*

**5.3.2 Ganho de XP na Forja (apenas Anões) (XP Gain from Forge, Dwarf only)**

No fim de cada turno, antes da Experiência de Personagem (e depois da geração de relatórios), o Processador de Turnos (Turn Processor) aplica um bónus de forja aos exércitos Anões elegíveis:

- **Elegível**: reino Anão, exército não destruído, exército com pelo menos uma unidade viva, exército não embarcado numa frota, **nenhuma ordem \`move_army\` submetida neste turno**, o hexágono atual do exército tem um local de produção (site) de Forja **e uma construção da família Anã (FDW)**, e esse hexágono pertence ao mesmo reino.

- Taxa: **+2%** (fixa) aplicada multiplicativamente a todas as pilhas de unidades vivas

- new_xp_wp = min(cap, round(xp_wp × roll))

- Uma rolagem por exército, o mesmo multiplicador aplicado a todos os tipos de unidade desse exército

- Limite: igual ao XP de batalha — baseWP × 3

O requisito de imobilidade baseia-se nas **ordens submetidas**, não no resultado. Um exército com uma ordem de movimento que é bloqueada a meio do percurso não recebe XP de forja, porque o jogador pretendia movê-lo.

**5.3.3 Limite de XP (XP Cap)**

cap = baseWP × 3. Uma unidade não pode exceder o triplo dos seus Pontos de Guerra base.

**5.3.4 Mistura de XP no Recrutamento (XP Blending on Recruitment)**

xp_wp_new = round( (oldWP × existingCount + baseWP × newCount) / totalCount )

Os recrutas por treinar diluem proporcionalmente as pilhas veteranas.

**5.4 Posturas do Exército (Army Stances)**

|             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Postura** | **Efeito**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Moving (Em Movimento) | Executa o percurso de movimento. Sem modificador defensivo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Defensive (Defensiva) | ×1.20 a defRoll. Nas muralhas fica **fora** delas — sem bónus de fortaleza, sem milícia (só a Guarnição está atrás das muralhas, §5.8.0)                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ambush (Emboscada) | ×1.40 a defRoll (batalha campal) **enquanto DEFENDE** — válida apenas para um **Elfo em floresta** ou um **Anão em montanha** (caso contrário, Defensiva). Uma Emboscada válida fica **fora** das muralhas, oculta dos mapas e dos espiões, e fica gasta assim que combate — ver *Emboscada em pormenor* abaixo                                                                                                                                                                                                                                       |
| Garrison (Guarnição) | ×1.20 a defRoll (batalha campal); ×1.30 a defRoll (assalto); rende-se na queda automática do cerco em vez de se retirar, se o seu reino for dono das muralhas (a Guarnição de um aliado lá dentro é, em vez disso, expulsa, §2.7). **A única postura atrás das muralhas** (§5.8.0) — e nunca sai para se juntar a um combate. Um exército **cercado** mantém a Guarnição seja o que for que tenha ordenado (§2.13.7). Válida apenas numa **construção fortificada** (máximo de muralha \> 0) — em qualquer outro hexágono, ou num povoado fundado neste mesmo turno (sem fortificação até ao turno seguinte), a postura é despromovida a Defensiva. |
| Siege March (Marcha de Cerco) | Avança **um hexágono por turno** e **acampa** num hexágono fortificado estrangeiro em vez de o tomar de assalto, e depois cerca-o por si só — o anel fecha-se logo se a força for suficiente (§5.8.0). Defende a ×0.85 se for atacado (§5.8.0).                                                                                                                                                                                                                                                                                                  |
| Siege (Cerco) | Cerca a construção com muralhas em que o exército SE ENCONTRA (marcha primeiro — um assalto precipitado; sobrevive para acampar); Progresso do Cerco +1/turno                                                                                                                                                                                                                                                                                                                                                                                  |
| Assault (Assalto) | Ordenado por um exército já acampado NUM hexágono estrangeiro com muralhas: toma as muralhas de assalto na Pré-Fase 3 (§5.6). Uma marcha sobre muralhas é um assalto precipitado por si só (§2.13.6b). Um exército que submete uma marcha juntamente com esta postura **marcha** — a postura é ignorada nesse turno e um cartão *Stance Ignored* di-lo                                                                                                                                                                                      |
| Sally (Surtida) | Apenas para um exército **cercado**: na Pré-Fase 3 sai com todos os outros exércitos cercados que o ordenem e combate os sitiadores a céu aberto, como atacante. Apenas um turno, nunca armazenada (§2.13.7).                                                                                                                                                                                                                                                                                                                                  |

**Só conta a postura do defensor.** O lado atacante de qualquer batalha terrestre não tem qualquer modificador de postura: um **surtidor** (§2.13.7), atacante da sua própria batalha, combate a ×1.00 seja qual for a postura em que estava.

**Emboscada em pormenor.**

**Quem a pode manter.** Apenas um **exército Elfo em floresta** ou um **exército Anão em montanha**; qualquer outra raça ou terreno despromove a Defensiva. Uma Emboscada **inválida** nunca o foi — decorre como uma postura Defensiva normal, fora das muralhas, a ×1.20.

**Fora das muralhas.** Uma Emboscada válida num hexágono fortificado fica FORA das muralhas. A única exceção é um **membro de ligação**, que fica onde o seu LÍDER fica e não tem postura própria (§5.8.0 Casos E e F). Como todas as posturas exceto a Guarnição, fica fora (§5.8.0) — no teu hexágono, no de um aliado mútuo, no de um vassalo ou no de um suserano (§5.6, §9.10). Lá fora está oculta, mantém o seu terreno e o ×1.40, mas não tem bónus de fortaleza nem milícia; um atacante que venha pelas muralhas tem de a combater primeiro a céu aberto: uma marcha ou um Assalto que a derrote toma as muralhas de assalto no mesmo turno, enquanto uma Marcha de Cerco ou um Cerco perde o progresso desse turno.

**Gasta — mas o terreno mantém-se.** **Qualquer emboscada que combata — ganhe, perca ou empate — fica gasta:** volta à Defensiva para o turno seguinte (uma armadilha que foi acionada já não é armadilha). O exército continua, no entanto, a manter esse hexágono fora das muralhas, turno após turno, até definires **🏰 Garrison** para o fazer voltar para dentro ou o marchares para longe — voltar a submeter Defensiva não altera nada, porque já está Defensiva. Uma Emboscada armazenada continua a funcionar num turno em que o seu reino não submeta ordens — incluindo a zona exterior e o gasto.

**Oculta.** Um emboscador válido está oculto dos mapas de todos os outros reinos, aliados incluídos, **e é invisível para os espiões, incluindo os espiões aliados** — uma missão de espionagem no seu hexágono não o reporta (§2.15); só marchar para o hexágono o descobre. Uma emboscada acionada aparece em todos os mapas estrangeiros desde esse mesmo turno. Um aliado a seu lado que não possa manter Emboscada fica à vista, pelo que o hexágono continua a mostrar um ocupante.

**Uma armadilha, mesmo fora das tuas terras.** A Emboscada não se limita às tuas terras: um exército em paz contigo que marche para o hexágono encontra-a como qualquer outro exército — uma batalha, e guerra entre os vossos reinos — embora não te pudesse ver.

**Numa ligação.** Um líder em Emboscada mantém-na, mas os seus membros **aliados** ficam visíveis e combatem sem o bónus, e a oferta de um aliado a um exército em Emboscada fica sem resposta (§5.11).

> ***▶ As posturas mantêm-se em vigor.** Cerco, Defensiva, Guarnição e Emboscada ficam **armazenadas no exército**: ordena uma vez e vale em todos os turnos até submeteres outra postura ou uma marcha — não é preciso repeti-la, e esquecê-la não custa nada. **O inverso é a armadilha: um exército sem postura em vigor defende a ×1.00** — um exército acabado de levantar (exceto um levantado na tua própria sede com muralhas, que nasce em Guarnição, §5.8.0), um que acabou de marchar (a marcha apaga a postura armazenada) ou um que recuou após uma derrota não tem nenhuma até definires uma. **Qualquer movimento forçado para fora do hexágono apaga-a** — uma retirada, um recuo ou uma expulsão, incluindo um forçado antes da fase de marcha por um assalto às muralhas ou pelo choque de um sitiador com um acampamento no exterior. As exceções mantêm ou ganham uma postura porque nunca saem do hexágono: os sobreviventes de uma Surtida derrotada, um exército **cercado** derrotado no seu próprio hexágono e um exército derrotado fora das suas próprias muralhas — cada um termina dentro, em Guarnição (§2.13.7, §5.8.0). A postura armazenada de um exército cercado é **Guarnição**, e continua a ser Guarnição depois de o cerco ser levantado, até submeteres outra postura ou uma marcha. A Página do Jogador avisa no cartão do exército (No stance in force — defends at ×1.00), e numa marcha em fila de espera, que o exército chegará sem postura. O valor armazenado é a postura tal como resolvida (uma Guarnição ou Emboscada inválida é armazenada como Defensiva, e um Cerco só enquanto o seu anel se mantiver). Mover-se é a predefinição; **o Assalto nunca é armazenado** — é uma ordem por turno. A bordo de uma frota um exército não tem postura. A Página do Jogador pré-seleciona uma postura armazenada e assinala o seu botão (in force); escolher outra postura ou planear uma marcha substitui-a.*

**5.5 Batalha Campal (Field Battle)**

Desencadeada quando um exército em movimento entra num hexágono ocupado por um exército inimigo.

**5.5.1 Fórmula de Rolagem (Roll Formula)**

initiative = 1.05 + rand×0.05 (attacker only — attRoll; defRoll has no initiative term)

variance = 0.90 + rand×0.20 (BATTLE_VARIANCE = 0.10 → ±10 %, independent per roll)

cmdMult = 1 + military/1000 (0 if no commander)

attRoll = attWP × status × attTerrainMult × cavTerrainScale × initiative × attCmdMult × variance

defRoll = defWP × status × defTerrainMult × cavTerrainScale × defStanceMod × defCmdMult × legion × variance

legion = 1.10 se o defensor é Imperial, é dono do hexágono e a sua construção é FI ou POP (§4.2); caso contrário 1.0 — milícia incluída. A rolagem do atacante inclui-o em UM só caso: uma SURTIDA, em que o dono do forte é o lado que carrega para fora (attRoll × legion)

attTerrainMult / defTerrainMult: bónus de terreno da raça se combater em terreno natal, caso contrário 1.0 cavTerrainScale: por lado — a parcela de WP **montado** do exército escalada pelo terreno da batalha (§3.5.1); exércitos todos a pé ×1.0 defStanceMod: Emboscada ×1.40, Defensiva ×1.20, Guarnição ×1.20, Marcha de Cerco ×0.85 (SIEGE_MARCH_DEF_MULT, §5.4), **Cerco ×0.85 quando atacado por qualquer coisa que não a surtida que enfrenta** (SIEGE_RELIEF_DEF_MULT — um exército de socorro que chega de fora por terra **ou que desembarca do mar**, ou um já acampado a seu lado; contra a surtida o sitiador mantém ×1.00), caso contrário ×1.0 status: a **prontidão** de cada exército, 0.10–1.00 (10–100%; §5.10) — um exército fatigado rola proporcionalmente mais fraco, pelo que uma força desgastada pode perder um combate que os seus Pontos de Guerra em bruto ganhariam. Este mesmo fator × status aplica-se em todas as rolagens de combate (assalto, anfíbio, naval); as levas de milícia não têm status e nunca são escaladas.

**5.5.2 Resultado (Outcome)**

|                          |               |
|--------------------------|---------------|
| **Condição**             | **Resultado** |
| attRoll \> defRoll × 1.2 | O atacante vence |
| defRoll \> attRoll × 1.2 | O defensor vence |
| Caso contrário           | Empate        |

> ***▶ Exemplo — a vantagem do defensor, quantificada.** O Exército A (300 WP) ataca o Exército B (280 WP) em postura **Defensiva** em planície neutra. Pondo de parte as rolagens aleatórias (que se aplicam de forma semelhante a ambos): o ×1.20 defensivo de B eleva a sua rolagem para cerca de 280 × 1.20 = 336; A rola a partir de 300.*
>
> *• A só vence se attRoll \> defRoll × 1.2 → precisaria de \> 403. Tem 300. Não.*
>
> *• B só vence se defRoll \> attRoll × 1.2 → precisaria de \> 360. Tem 336. Não.*
>
> *• Nenhuma das margens é atingida → **Empate**, e num empate o atacante retira-se e sofre 6–12% de baixas por nada.*
>
> *Atacar com mais WP em bruto do que o defensor falhou na mesma, puramente por causa da postura defensiva mais a margem decisiva de ±20%. **Regra prática: para vencer de forma fiável um ataque a um inimigo Defensivo entrincheirado em terreno igual, leva cerca de 1.5× o seu WP em bruto** — o ×1.20 da postura e a margem de ×1.2 compõem-se em ≈1.44×. Acrescenta terreno ou um comandante e esse número sobe.*

**5.5.3 Fórmulas de Baixas (Casualty Formulas)**

ratio = winnerRoll / loserRoll

As perdas do **vencedor** descem na mesma proporção do rácio (ratio) — **não existe um mínimo de baixas**, pelo que uma derrota esmagadora custa quase nada ao vitorioso, enquanto um combate equilibrado (rácio ligeiramente acima de 1.2) ainda faz sangrar ambos os lados.

**O atacante vence:**

attLoss = 0.10 / ratio (sem mínimo — uma vitória esmagadora custa quase nada ao vencedor)

defLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) abaixo de 10:1 (pelo menos 12% dos WP do VENCEDOR, limitado a 60% da própria força)

\> \*\*▶ O mínimo de dano.\*\* O perdedor sangra sempre pelo menos \*\*12% dos pontos de guerra (war points) do \*vencedor\*\*\* — pelo que um exército grande inflige \*pelo menos tantas\* baixas absolutas a um inimigo pequeno como a um grande. Em termos da própria força, o mínimo é \`12% × ratio\`; ultrapassa a curva logarítmica a partir de cerca de \*\*2.1:1\*\*, e o seu \*\*limite de 60%\*\* aplica-se a partir de \*\*5:1\*\* — um exército pequeno derrotado é massacrado, mas nunca aniquilado só pelas probabilidades abaixo da rampa de 25:1. Ser \*\*cercado\*\* continua a ser a única verdadeira aniquilação, tal como nos cercos da história. As perdas do próprio vencedor não têm mínimo (10%/ratio — o que equivale sempre a 10% dos WP do perdedor em termos absolutos).

max(o valor com mínimo, 0.50 + 0.50 × (ratio − 10) / 15) acima de 10:1 (o limite de 60% mantém-se até 13:1, depois a rampa linear até à aniquilação total a 25:1)

**Empate:**

attLoss = defLoss = 0.06 + rand×0.06 (6–12% cada, mesmo valor)

**O defensor vence:**

defLoss = 0.10 / ratio (sem mínimo — as perdas do vencedor crescem com o combate)

attLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) abaixo de 10:1 (pelo menos 12% dos WP do VENCEDOR, limitado a 60% da própria força)

max(o valor com mínimo, 0.50 + 0.50 × (ratio − 10) / 15) acima de 10:1 (o limite de 60% mantém-se até 13:1, depois a rampa linear até à aniquilação total a 25:1)

Perda do perdedor por rácio: 1.2 → 15% · 1.5 → 19% · 2 → 24.5% · **a partir de ≈2.1:1 o mínimo domina** — 3 → 36% · 4 → 48% · **5:1 → o limite de 60%, que se mantém constante até 13:1** (6:1, 8:1, 10:1, 12:1 todos → 60%). **Além de 13:1 a rampa domina:** 15:1 → 67% · 20:1 → 83% · **25:1 e acima → nenhum sobrevivente**, armadura incluída. No mar a rampa é mais curta — uma frota é aniquilada a 10:1 (§5.9.3).

> ***▶ A armadura dissolve-se com as probabilidades.** O que perdes de facto é a percentagem da batalha **multiplicada pela tua armadura** — e a armadura é aquilo que o preço de um soldado compra (§ fator de morte). Abaixo de 10:1 isto não muda: uma unidade bem equipada continua a sangrar muito menos do que levas de recrutas. Acima de 10:1 a armadura é retirada segundo o **mesmo calendário da perda**, chegando a nada aos 25:1. Uma unidade de elite de vinte homens perde **4 · 7 · 13 · 20** em 10:1 → 15:1 → 20:1 → 25:1. Os números não te salvam de probabilidades tão grandes; apenas decidem quanto tempo demora.*
>
> ***▶ Porque existe uma rampa e não um interruptor.** As probabilidades esmagadoras devem acabar com um exército, mas a fronteira não pode decidir a batalha por si só. Um interruptor brusco aos 10:1 significaria que 10.0 te custava metade da força e 10.1 a custava toda — uma diferença mínima em pontos de guerra a transformar uma derrota numa extinção. A rampa mantém os dois extremos honestos: **abaixo da rampa nenhum rácio aniquila** — um exército gravemente derrotado sai com pelo menos 40% da sua força e reconstrói-se; acima de 13:1 cada novo degrau de superioridade compra destruição real, até que aos 25:1 já não resta nada para salvar. Os assaltos mantêm a sua própria curva, mais dura.*
>
> ***Porque é que a curva é suave.** A curva de perdas está calibrada para que uma **derrota de 2:1–3:1 seja recuperável em 4–5 turnos de recrutamento a partir de uma cidade** — de uma sede com ≥500 de população (o recrutamento está limitado a 5% da população do hexágono por turno: uma construção de Nv5+ Imperial/Bárbaro, Nv3+ Elfo/Anão/Aesir; uma sede de Nv1 com 100 precisa de ~26 turnos para a mesma perda). É côncava: a superioridade continua a compensar — a perda do próprio vencedor continua a cair como 0.10/ratio e a do perdedor continua a subir — mas com retornos decrescentes — limitada a 60% abaixo de 10:1 pelo mínimo de dano (§5.5.3), depois em rampa até à aniquilação a 25:1. A destruição decisiva vem da **posição, não da aritmética**: corta a retirada e os sobreviventes morrem onde estão. Os assaltos a muralhas (§5.6.2) mantêm deliberadamente a sua própria curva, mais dura.*

**5.5.4 Baixas Ponderadas (Weighted Casualties)**

As baixas dentro de um exército não se distribuem uniformemente. A sobrevivência depende do **preço total** de uma unidade — cada moeda e mercadoria gasta no soldado protege-o, e a veterania (veterancy) multiplica essa proteção. A composição não importa: cada pilha de unidades responde apenas pelo seu próprio valor, quer marche sozinha, quer ao lado de elites:

price (g-eq) = gold + iron×12 + horses×20 + wood×5 (equipamento — as rações não compram nada)

deathFactor = clamp( 0.3 … 1.0 , 1.0 − price × (1 + veterancy) / 1100 )

losses = battle loss % × unit count × deathFactor (arredondado por pilha)

**Mínimo de um.** As baixas arredondam-se para o soldado mais próximo, pelo que uma pilha minúscula ou de elite pode arredondar para zero perdas. **Cada exército** do lado perdedor de um combate em campo, anfíbio ou contra a população perde sempre **pelo menos um soldado** (o mínimo é por exército, pelo que uma coligação derrotada enterra pelo menos um homem por membro) (retirado da unidade mais próxima de uma baixa); vencedores e empates não são afetados.

Os soldados mais caros do jogo situam-se no **mínimo de 0.3** e quase ignoram por completo as percentagens normais de batalha; as levas baratas andam perto do **teto de 1.0** e morrem, no máximo, um por um com as perdas nominais da batalha — o fator só *protege*, nunca amplifica (a milícia levantada fica exatamente em 1.0). As baixas TOTAIS de um exército dependem, portanto, daquilo de que é feito — uma horda de recrutas sangra à taxa de destaque, enquanto um exército profissional sai ileso.

> ***▶ Exemplo — porque é que o equipamento e os veteranos sobrevivem.** Os Velites (50g + 8 food + 6 wood×5 = 80 g-eq) têm deathFactor = 1.0 − 80/1100 ≈ 0.93; os Pretorianos novos (300g + 100 iron×12 + 5 wood×5 = 1,525 g-eq) caem para o mínimo de 0.3 (1.0 − 1,525/1100 \< 0.3). Com uma perda de 20% em toda a batalha, os Velites perdem 20% × 0.93 ≈ 18.5% enquanto os Pretorianos perdem 20% × 0.3 = 6% — e o arredondamento por pilha costuma transformar as perdas fracionárias de uma pequena pilha de elite em **zero**. Um veterano a 1.5× os WP base conta como um soldado uma vez e meia mais caro, pelo que a experiência (experience) acumula sobrevivência até ao limite de 3× XP.*

**5.5.5 Morte do Comandante (Commander Death)**

Depois do combate, verifica-se a morte dos comandantes:

deathChance = min(0.4, lossPct × 0.5)

**Batalha em campo**: ambos os comandantes são verificados incondicionalmente após a batalha. **Assalto — o atacante vence**: ambos os comandantes são verificados incondicionalmente. **Assalto — repelido**: o comandante do atacante é verificado incondicionalmente; o comandante da guarnição (garrison) também faz o teste com qualquer perda positiva (ver §7.7).

A morte do comandante é permanente. A personagem é marcada como morta e deixa de afetar os resultados.

**O inimigo também é informado.** Quando um comandante cai, o reino que o perdeu recebe o seu cartão de luto — e o mesmo acontece com **todos os reinos que combateram do lado oposto desse confronto**, num cartão que nomeia o comandante morto e o seu reino, e diz se liderava um exército ou uma frota — **nunca qual deles**: um corpo no campo é identificável, mas o número de uma força inimiga é informação secreta e nenhum cartão a revela. Como as batalhas aqui são travadas por **coligações** (§5.11) e nenhum motor regista a lâmina de quem desferiu o golpe, todos os reinos adversários são informados, e cada um é informado **uma vez por morte**, por mais exércitos que tenha trazido. O cartão não atribui mérito a nenhum soldado em particular — dá conta de um corpo encontrado, não de um duelo ganho.

**A cidade que combateu apenas com o seu povo conta.** Num assalto, "o outro lado" é exatamente o conjunto que o motor já usa para decidir contra quem foste à guerra: a **coligação da guarnição mais o dono do hexágono**. Assim, um reino cujo povoado foi tomado de assalto **sem qualquer exército lá** é na mesma informado do que a sua milícia levou consigo — os seus habitantes foram toda a defesa, e um defensor só com milícia merece o cartão tanto como uma guarnição. Se o dono também guarnece o hexágono, é informado na mesma **uma só vez**, não duas.

**No mar, a regra é o vencedor.** Um comandante que se afoga com um transporte é comunicado a quem **ganhou** o combate que o afundou: a frota vencedora numa batalha naval, ou o reino cujo cerco ou assalto fez cair o porto sob uma frota presa ao cais. As coligações vencedoras são tratadas exatamente como em terra — todos os reinos do lado vencedor são informados, uma vez cada.

**Onde ninguém é informado.** Apenas uma classe de mortes é silenciosa, e a razão é que **não há vencedor a quem atribuir mérito**: um **empate** naval, em que os atacantes recuaram (os defensores mantêm a posição num empate) e o transporte afundou-se na mesma (e o seu parente próximo, um casco esvaziado por baixas de batalha em qualquer dos lados — essa varredura pode atingir o próprio navio do vencedor). O Witch King (§7.8) não pode ser morto de todo, pelo que também não há nada a comunicar em nenhum dos casos.

**5.5.6 Retirada (Retreat)**

Os exércitos em retirada procuram até **3 saltos** para o exterior um hexágono válido:

- Destino válido: terreno que não seja mar, território que não pertença ao inimigo, e **ou vazio de exércitos ou ocupado apenas por exércitos AMIGOS com espaço** — próprios / aliados mútuos / vassalos / suserano, pilha **abaixo do limite de 3 exércitos** — num hexágono com muralhas conta-se na zona exterior, onde uma retirada chega sempre (§5.8.0). Como os exércitos amigos podem **partilhar um hexágono** (até 3), um exército derrotado pode **reagrupar-se junto dos amigos**; mas uma **pilha cheia (3 exércitos)** ou **qualquer exército não amigo** no hexágono bloqueia-o, exatamente como um exército inimigo. **Uma convocação sem soldados já não é um exército para nada disto**: não impede um hexágono nem enche uma pilha amiga, pelo que nunca pode empurrar um exército derrotado para um hexágono pior — ou, com as alternativas fechadas, fazê-lo morrer onde está. A mesma regra vale em todo o lado onde o motor pergunta se há um exército presente: quem defende um hexágono, quem se junta a uma parede de escudos, e o que bloqueia um caminho.

- **A procura nunca atravessa o mar** (nem sai do mapa): a cascata de vários saltos existe para contornar *terra* ocupada por amigos ou hostil, não para vadear águas abertas. Um exército não tem navios — não pode fugir para a margem oposta de um estreito.

- Se nenhum hexágono válido for alcançável em 3 saltos **por terra**: o exército é **destruído** onde está (e os seus caídos são despojados por inteiro por um vencedor decisivo, §2.13.11). Um exército encurralado contra a costa, ou a defender uma ilha sem um hexágono amigo, não tem para onde fugir.

Entre os hexágonos que *são* válidos, a procura toma primeiro o **mais próximo**; entre hexágonos à mesma distância, prefere a **origem** do exército (de onde veio), depois a tua própria terra, depois a de um aliado mútuo, depois a neutra (a terra de um suserano ou de um vassalo conta aqui como neutra). A distância é o critério principal: um hexágono neutro livre a um salto vence a tua própria terra a dois saltos. **Não existe nenhuma regra especial de "recuar para a capital"** — a capital é apenas mais um hexágono de território próprio.

> ***⚠ Podes mesmo assim fechar a fuga do teu próprio defensor.** Reagrupar junto de amigos só funciona **enquanto a pilha tiver espaço**. O recrutamento (recruitment) e a colocação de exércitos (Pré-Fase 2 / 2b) resolvem-se **antes** do combate — tanto o da pré-fase como o da Fase 5 — pelo que encher o hexágono de recuo até ao seu **limite de 3 exércitos** — ou deixar lá um exército **não amigo** — torna-o uma retirada **inválida**. A **capital** não é um recuo especial: uma pilha cheia ali (um exército de capital pode ser o que a leva ao limite) bloqueia-a como qualquer outro hexágono. Entope a tua retaguarda até ao limite e um exército derrotado sem para onde ir é **destruído**.*

Resultados:

- O atacante vence: o defensor retira; o atacante reclama o hexágono — exceto um exército do dono ou de um amigo derrotado fora das suas muralhas, que entra em Guarnição (Garrison) (§5.8.0)

- Empate: o atacante retira; o defensor mantém a posição

- O defensor vence: o atacante retira

> ***Deslocação a meio da marcha.** O movimento resolve-se como um escalonador por rondas (§2.13.1): um exército ou frota — incluindo um membro de um grupo ARMY LINK ou FLEET LINK — pode ser expulso do seu hexágono pela batalha de um **outro** movente travada antes na mesma fase — um espectador apanhado no combate de outrem, não no seu. Quando isso acontece, o movente deslocado **perde o resto do seu caminho em fila**; não retoma a marcha para o destino original a partir de onde a batalha o deixou. Um cartão honesto de "deslocado a meio do movimento" explica a paragem, em vez de levar silenciosamente o movente de volta ao seu plano.*

**5.5.7 Atribuição de Experiência (Experience Grant)**

Ambos os exércitos sobreviventes ganham experiência após cada batalha, independentemente do resultado, escalada pelo fator de força do oponente (§5.3.1) — uma vitória fácil não ensina nada.

**5.6 Assalto (Assault)**

Desencadeia-se na Pré-Fase 3 para um exército com a postura (stance) de Assalto ATIVA num hexágono com uma **construção amuralhada** estrangeira (§3.7.2). Uma construção sem muralha não é assaltada — é simplesmente disputada como terreno aberto.

**Quem defende — e como.** Um assalto — uma marcha sobre as muralhas, uma postura de Assalto, um desembarque — começa por vencer os exércitos de fora, depois **toma as muralhas de assalto**; cada Guarnição lá dentro defende atrás delas a ×1.30, com o bónus de fortaleza e a milícia (§5.8.0), e ninguém faz surtidas sem ordem (§2.13.7). Sem nenhum exército lá dentro, a milícia defende sozinha as muralhas. **Todos os reinos lá dentro são defensores.** Um exército que toma muralhas de assalto ou que lança ou mantém um cerco sobre elas declara guerra a **todos os reinos com um exército lá dentro**: o dono, um reino em paz com ele, e o seu próprio aliado mútuo, vassalo ou suserano, cuja aliança ou vassalagem se quebra no ato (o atacante lê *A sworn alliance lies in ruins*, o reino lá dentro *…lies shattered*), ligado à defesa ou não. É declarada de novo a **cada turno de cerco**, pelo que um reino que entra numa cidade cercada está em guerra com o sitiante desde o seu primeiro turno lá dentro. Só o reino do exército atacante declara — um membro do seu grupo de ligação mantém as regras normais (§5.11.1). Os exércitos acampados **fora** das muralhas não estão lá dentro e não são afetados — e todo o exército que não está em Guarnição fica fora (§5.8.0): qualquer atacante que venha pelas muralhas tem de os combater primeiro ali. Uma exceção lá dentro: um exército em guerra com **outro defensor** afasta-se da defesa. Um reino que não entrega ordens vê os seus exércitos sem postura, nas suas muralhas ou nas de um amigo, colocados em Guarnição enquanto houver espaço e nenhum exército em guerra com ele estiver acampado fora (§5.8.0). Muralhas que **ninguém possui** não têm interior — não há dono sob quem abrigar-se — pelo que um exército de um reino em paz contigo que lá esteja é recebido como em terreno aberto: declara-se guerra e combate-se nos portões. **Quando as muralhas caem, só o dono do hexágono recebe o cartão da perda** — um aliado cujo exército as defendia mantém o seu cartão de derrota, e o conquistador baixa o estandarte do dono. Um **assalto anfíbio** (um desembarque na praia sobre uma construção costeira, §5.7) toma as muralhas de assalto da mesma forma: uma investida **repelida** deixa os sobreviventes acampados em terra junto aos portões, após o custo fixo de desembarque (−20 de ESTADO), como faria quem marchou (§5.8.0); reembarcar após um combate de praia perdido acontece em todo o lado exceto em muralhas estrangeiras (§5.7.2).

> ***▶ Exemplo prático — guerra a todos os reinos lá dentro.** Gruk-Mor possui uma cidade amuralhada em (14,9). Lá dentro estão o Exército I de Gruk-Mor (Guarnição) e o Exército II de Sylvane (Guarnição). Sylvane é aliada de **ambos**, Gruk-Mor e Aldoria; Aldoria está em guerra com Gruk-Mor e envia o Exército III em **Siege March**.*
>
> *- **Turno 1 — chegada.** O III chega aos portões e lança o cerco por si só (§5.8); sendo forte o bastante, fecha o anel de imediato. Lançá-lo declara guerra a todos os reinos lá dentro: a Gruk-Mor (já em guerra) e a **Sylvane**. A aliança Aldoria–Sylvane quebra-se: Aldoria lê A sworn alliance lies in ruins, Sylvane …lies shattered.*
>
> *- **Turno 1, Fase 5 — um convidado tardio.** Zingara, aliada de Gruk-Mor, de Aldoria **e** de Sylvane, marcha com o Exército I até à cidade — para as muralhas de um aliado, passando o acampamento de um aliado, pelo que não há batalha. Uma marcha nunca leva Guarnição: o I de Zingara fica **fora**, e ninguém lhe declara guerra.*
>
> *- **Turno 2 — o turno de cerco.** Zingara ordena **Garrison** e entra. O ciclo de cerco do III declara guerra de novo a todos os reinos lá dentro, pelo que Aldoria e Zingara estão agora em guerra — e a sua aliança também se desfaz em ruínas. Este é o primeiro ciclo (progresso 1, §5.8.0). Gruk-Mor e Sylvane estão cercados desde este turno (o anel fechou à chegada), pelo que as suas ordens já só podiam ser Garrison ou Sally; Zingara, fora quando o turno começou, fica cercada a partir do turno 3. Se Zingara tivesse ficado fora, nenhuma guerra teria seguido, e nunca ficaria cercada.*
>
> *- **A queda.** O Exército I de Gruk-Mor rende-se e os exércitos de Sylvane e de Zingara são expulsos ou chacinados, exatamente como no exemplo de queda das muralhas do §2.7.*
>
> *- **O que a página mostra.** A tua Página do Jogador avisa-te antes de te comprometeres. As notas de entrada em marcha, Siege March, desembarque e Siege/Assault nomeiam todos os reinos que consegues ver lá dentro com os quais ainda não estás em guerra, e assinalam um aliado com "the alliance breaks".*

**5.6.1 Fórmula de Resultado (Roll Formula)**

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (±10 %)

militiaCount = floor(pop × 0.05) // 5% of population

militiaWP = militiaCount × 20 // ≈ population

wallMax = the construction level's listed wall

integrity = wall_hp / wallMax // 1.0 = whole, 0.0 = breached

fortressBase = max(1.5 + 1.5×r , 1 + 6×r) where r = min(1, wallMax / 15000) (+0.10 if muster seat)

fortressBonus = 1 + (fortressBase − 1) × integrity

attPenalty = 1 − 0.15 × integrity

attRoll = attWP × status × attTerrainMult × cavAssaultScale × attPenalty × initiative × attCmdMult × variance

defRoll = (garrisonWP × status × defStanceMod × cavTerrainScale + militiaWP) × fortressBonus × defTerrainMult × defCmdMult × legion × variance

defStanceMod aplica-se **apenas aos WP da guarnição** (não à milícia): Garrison ×1.30 — só uma Guarnição está lá dentro (§5.8.0). Aplica-se o bónus de terreno do defensor. cavAssaultScale: a parte de WP **montados** do atacante é penalizada em ×0.65 ao tomar muralhas de assalto (substitui o regime de terreno para o atacante); cavTerrainScale: a parte montada da guarnição é escalada pelo terreno como em campo (§3.5.1). Exércitos todos a pé ×1.0 em ambos.

**As muralhas valem o que são grandes o suficiente para valer.** O bónus de fortaleza deriva do **tamanho** da muralha. Uma paliçada de madeira e uma cidadela anã não defendem da mesma forma:

|                  |                                      |                                                                                                            |
|------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Máximo da muralha** | **Bónus de fortaleza com integridade total** | **Aproximadamente o que o atacante precisa (WP brutos, após a sua penalização de assalto ×0.85 e um resultado médio de iniciativa)** |
| 500 (paliçada)   | ×1.55                                | ~2.0 : 1                                                                                                   |
| 2,500            | ×2.00                                | ~2.6 : 1                                                                                                   |
| 5,000            | ×3.00                                | ~3.9 : 1                                                                                                   |
| 10,000           | ×5.00                                | ~6.6 : 1                                                                                                   |
| 15,000 e acima   | ×7.00                                | ~9.2 : 1 — uma grande fortaleza não se toma de assalto, esfomeia-se                                        |

A sede de recrutamento acrescenta **+0.10** por cima. Muralhas acima de 15,000 não dão mais nada — a curva termina aí.

**Porque é que a curva tem duas metades.** O bónus é o maior de dois declives: um íngreme, 1 + 6×r, que define os números de destaque acima, e um mais suave, 1.5 + 1.5×r, que funciona como **mínimo**. Cruzam-se numa muralha de cerca de **1,667**. Abaixo desse cruzamento manda o mínimo — cada paliçada de 500 pontos, cada FDW1–3 anã. Acima dele manda o declive íngreme, até ×7.00 para uma muralha de 15,000.

**A integridade escala os dois lados do combate, de forma contínua.** Uma muralha batida até metade da força dá metade do bónus *acima de 1.0* — uma cidadela FDW10 a ×7.00 inteira fica a ×4.00 a meia integridade e a ×1.00 uma vez aberta uma brecha. E a penalização do atacante relaxa ao mesmo ritmo: uma muralha inteira custa ao atacante o conhecido **×0.85**, uma muralha meio batida ×0.925, e uma **muralha com brecha não custa nada (×1.00)**. Deitar abaixo a muralha antes de a tomar de assalto vale, portanto, duas coisas ao mesmo tempo, e é exatamente para isso que servem as máquinas de cerco (§5.8.6).

Uma construção **sem muralha** — Orc Nível 0–3, Genérica Nv.1–4, Nómada Nv.1 — dá ×1.00 em ambos os sentidos. É um povoado aberto, defendido apenas pela sua milícia.

> ***▶ Exemplo — tomar de assalto um povoado é caro, e abrir brecha é o desconto.** Alvo: uma **FI12** Imperial (máximo da muralha 1,500 ⇒ fortressBase = max(1.5 + 1.5×0.1, 1 + 6×0.1) = max(1.65, 1.60) = 1.65 — muralhas pequenas assentam no mínimo), população 4,000, defendida por uma guarnição de 200 WP em postura de **Garrison** (×1.30); ambos os exércitos todos a pé, pelo que os fatores de cavalaria são ×1.0. A população gera milícia: floor(4,000 × 0.05) = 200 milicianos × 20 WP = 4,000 militiaWP (os WP da milícia ≈ a própria população).*
>
> *• **Muralhas inteiras (integridade 1.0):** fortaleza ×1.65, atacante ×0.85. Resultado do defensor (200 × 1.30 + 4,000) × 1.65 = 4,260 × 1.65 = 7,029. Para atingir a margem decisiva o atacante precisa de attWP × 0.85 \> 7,029 × 1.2, ou seja **\`attWP \> ~9,920\`**.*
>
> *• **Muralhas com brecha (integridade 0.0):** fortaleza ×1.00, atacante ×1.00. Resultado do defensor 4,260. Agora o atacante só precisa de attWP \> 4,260 × 1.2 = **\`~5,110\`** — pouco mais de metade.*
>
> *• Deitar abaixo essa muralha de 1,500 pontos exige 1,500 ÷ 250 = **seis golpes de máquina** — seis máquinas a bombardear durante um turno, ou três máquinas durante dois turnos (§5.8.6). Saber se isso sai mais barato do que quase duplicar o teu exército é toda a questão da guerra de cerco.*
>
> *A **milícia sozinha (≈ a população) domina** a defesa — a guarnição e as muralhas somam-se por cima. A própria população é a arma (mais população → proporcionalmente mais milícia). O reverso: essa milícia é **retirada da população, e os seus caídos são removidos dela** depois (proporcionalmente ao combate, §2.13.4) — um assalto repelido custa ao povoado uma fatia pequena, uma tomada bem-sucedida estripa a leva, e um povoado pode ser desgastado por assaltos repetidos. Se puderes dispensar os turnos, um **Cerco** (§5.8) toma-o sem baixas de batalha para ti; reserva o assalto para quando não podes esperar ou não consegues formar o anel (§5.8.1).*

**5.6.2 Resultado e Baixas (Outcome and Casualties)**

Mesmo limiar da batalha em campo aberto (rácio \> 1.2 para resultado decisivo).

**O atacante vence:**

attLoss = 0.15 / ratio (no floor)

defLoss = ratio ≥ 5 ? 1.0 : min(0.95, 0.25 × ratio)

**Empate (Draw):**

attLoss = defLoss = 0.10 + rand×0.08 (10–18%)

**O defensor vence (assalto repelido):**

defLoss = 0.12 / ratio (no floor)

attLoss = ratio ≥ 5 ? 1.0 : min(0.95, 0.30 × ratio)

Nota: **os assaltos mantêm de propósito uma curva mais severa** — a curva suave (§5.5.3) aplica-se apenas às batalhas em campo aberto e anfíbias. Nas muralhas, o perdedor sofre 0.25 × ratio (atacante repelido: 0.30 × ratio) e é **aniquilado com ratio ≥ 5**. Assaltar muralhas deve ser o único combate capaz de acabar com um exército numa tarde. O **teto do fator de morte de 1.0** (§5.5.4; milícia 1.0) aplica-se também às baixas de assalto — corpos baratos nunca morrem mais depressa do que a percentagem de perdas principal, pelo que uma guarnição barata de 100 homens assaltada a 3:1 perde 75 (por desenho).

**5.6.3 Degradação na Captura (Degradation on Capture)**

**Toda** a mudança de posse de um hexágono — assalto, queda automática por cerco, apreensão terrestre, desembarque em praia, assalto anfíbio — danifica o que se encontra no hexágono. Duas coisas distintas degradam-se, cada uma pela mesma regra, no máximo uma vez por turno.

**O local de produção (production site)**, se existir:

- Nível do local **−1**, até um **mínimo de nível 1**. Um local nunca é arrasado por conquista.

- O conquistador é notificado com um cartão **Captured Works Damaged**; capturar um local de nível 1 não altera nada e passa em silêncio.

- Aplica-se igualmente a quintas, minas e portos. As forjas são apenas de nível 1 e não são afetadas.

- Consequência para as minas: uma mina anã de nível 3 capturada chega como **nível 2**, e só um proprietário anão a poderá voltar a escavar até ao nível 3 (§3.6.2).

**A construção (construction)**, se existir:

- Nível da construção **−1**, até um **mínimo de nível 1**. Um povoado também nunca é arrasado por conquista — herdas sempre alguma coisa.

- O máximo da muralha desce com o nível, e a integridade atual é **reduzida** ao novo máximo. Uma muralha que já esteja abaixo dele fica onde está: a conquista nunca *repara*.

- **A população não é afetada.** Mantém o que tinha, o que, após uma degradação, está muitas vezes *acima* do teto do novo nível — legitimamente. Esse povoado simplesmente deixa de crescer (§3.8) até o voltares a subir, e entretanto paga imposto integral e cunha milícia integral.

- O conquistador recebe um cartão **🏚 Fortifications Degraded** com o nível de origem e de destino.

> ***▶ Porque dói mais do que parece.** Assaltar um FI12 (muralha 1,500, teto 3,000) deixa-te um FI11 — máximo da muralha 1,000, teto 2,000 — com 3,000 pessoas lá dentro. E se era uma construção de uma família estrangeira, nunca a poderás melhorar de volta (§2.11.7): esse nível perdido é permanente sob a tua bandeira. A conquista do coração de um rival rende muita gente a viver atrás de muralhas permanentemente diminuídas.*

**5.6.4 Estado Pós-Assalto (Post-Assault State)**

**Vitória**: o atacante ocupa o hexágono; o progresso do cerco é limpo.

**Repelido**: se não houver outro sitiador nesse hexágono, o progresso do cerco volta a 0. Se outro reino estiver a sitiar ativamente, o seu progresso continua. Qualquer resultado decisivo faz oscilar a opinião como qualquer batalha (§8.5.3). (Um assalto **empatado** não faz oscilar a opinião de ninguém — o cartão do atacante continua a dizer *repelido*, pois foi rechaçado, mas ninguém ganha nem perde prestígio.)

**5.7 Batalha Anfíbia (Amphibious Battle)**

Desencadeada quando uma frota com um exército transportado desembarca num hexágono terrestre defendido.

**Todos os exércitos no hexágono da praia em guerra com o invasor defendem em conjunto**, e os membros da ligação do defensor juntam-se, cada um com a sua postura e comandante — a regra da coligação terrestre (§5.11); Emboscada ×1.40 e Marcha de Cerco ×0.85 aplicam-se a um defensor na praia exatamente como em campo aberto.

**5.7.1 Fórmula de Rolagem (Roll Formula)**

BEACH_PENALTY = 0.50

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (±10 %)

attRoll = attWP × status × 0.50 × initiative × attCmdMult × variance

defRoll = defWP × status × defStanceMod × defCmdMult × legion × variance

Sem multiplicador de terreno para nenhum dos lados. Sem bónus de fortaleza para o defensor.

**5.7.2 Resultados (Outcomes)**

|                      |                          |           |                  |              |
|----------------------|--------------------------|-----------|------------------|--------------|
| **Resultado**        | **Condição**             | **Hexágono** | **Atacante**  | **Defensor** |
| **O atacante vence** | attRoll \> defRoll × 1.2 | Tomado    | Desembarca, mantém o hexágono | Retira-se |
| **Empate / Impasse** | rolagens a menos de 20%  | Sem alteração | Reembarca na frota† | Mantém o hexágono |
| **O defensor vence** | defRoll \> attRoll × 1.2 | Sem alteração | Reembarca na frota† | Mantém o hexágono |

†Se o atacante for destruído (todas as unidades perdidas no combate — uma força de desembarque nunca procura um hexágono de retirada), o exército desaparece de vez — sem reembarque. O reembarque aplica-se em todo o lado exceto em muralhas **estrangeiras**: num povoado ou capital amuralhados pertencentes a outro reino que não seja o teu aliado, vassalo ou suserano mútuo, a força de desembarque sobrevivente descarrega, paga o custo fixo de desembarque (−20 de ESTADO) e mantém uma cabeça de praia fora das muralhas, quer tenha sido derrotada na praia, quer repelida das muralhas (§5.6, §5.8.0). Quando a praia cai, o **proprietário** do hexágono recebe um cartão com a perda — e, quando o exército de outro reino a mantinha em nome do proprietário, o cartão nomeia esse exército: *"(X's army holding it was driven off the beach)"*. Uma costa **sem dono** não tem proprietário a quem enviar cartão: ninguém é informado de que foi perdida, e o cartão do conquistador diz *"No banner flew here; up goes yours…"*. Nas muralhas, um exército do proprietário ou de um amigo acampado no exterior que o desembarque derrote entra para dentro em Guarnição e defende o assalto (§5.8.0); qualquer outro acampado que o desembarque derrote retira-se como em qualquer derrota em campo aberto, ou é abatido se não tiver para onde ir.

Declara-se guerra nos três resultados. Um empate é um **impasse**: o desembarque falha, o atacante reembarca sob fogo (em muralhas estrangeiras entrincheira-se, †), e o defensor conserva o hexágono. Ao contrário das batalhas terrestres (onde um empate também não favorece ninguém), os empates anfíbios acarretam baixas mais pesadas para o atacante (atacante 8–14% contra defensor 5–10%, §10.2) devido à retirada pela praia.

> ***⚠ O que isto significa — nunca desembarques levianamente numa praia defendida.** A penalização de praia de ×0.50 reduz a metade os WP do teu atacante antes de tudo o resto. Contra um defensor com WP brutos iguais em Defensiva (×1.20), a tua rolagem efetiva é 0.50 da base contra 1.20 deles — ficas a perder por mais de dois para um, e para vencer realmente precisas de cerca de **2–3× os WP do defensor** (attWP × 0.50 \> defWP × 1.20 × 1.2 ⇒ attWP \> ~2.9 × defWP). Prefere desembarcar em hexágonos abertos não defendidos (continua a ser uma disputa de WP contra a milícia da população local com a mesma penalização de ×0.50 — não há exército inimigo a enfrentar, mas uma costa populosa resiste e pode repelir um desembarque fraco) ou navegar até um porto não defendido e desembarcar no povoado; reserva os assaltos anfíbios contestados para depois de já teres quebrado os defensores locais — e lembra-te de que perder o combate naval anterior afoga o exército inteiro (§2.14.6).*

**5.7.3 Baixas (Casualties)**

**O atacante vence:**

attLoss = 0.10 / ratio (no floor)

defLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) (a mesma curva suave com piso do campo aberto, §5.5.3)

**Empate (impasse — o atacante reembarca, ou entrincheira-se em muralhas estrangeiras †):**

attLoss = 0.08 + rand×0.06 (8–14%)

defLoss = 0.05 + rand×0.05 (5–10%)

**O defensor vence:**

defLoss = 0.10 / ratio (no floor)

attLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) (a mesma curva suave com piso do campo aberto, §5.5.3)

A praia usa a curva do campo aberto sem alterações — a penalização de praia de ×0.50 já desloca o rácio contra quem desembarca, pelo que não é necessário nenhum multiplicador de perdas adicional. Só o empate mantém a sua assimetria do lado do desembarque. Uma força de desembarque repelida nunca é aniquilada por um rácio abaixo da rampa de 25:1; perde no máximo **60%** (o teto do piso de dano, §5.5.3) e reembarca — ou, em muralhas estrangeiras, entrincheira-se no exterior (†); sem frota onde reembarcar, é destruída.

**5.8 Guerra de Cerco (Siege Warfare)**

**5.8.0 As Muralhas (Walls) — Dentro e Fora (Cerco no Hexágono)**

**Os cercos são montados a partir do próprio hexágono da fortificação.** Um hexágono com uma construção amuralhada tem duas zonas: **DENTRO das muralhas** e **FORA** (o terreno aberto do hexágono). **Só um exército em Guarnição (Garrison) fica dentro.** Um exército do proprietário — ou de um aliado mútuo, vassalo ou suserano do proprietário — cuja postura (stance) seja **Garrison** fica atrás das muralhas: o bónus de fortaleza, a milícia e ×1.30 contra um assalto. **Todas as outras posturas ficam FORA**, no terreno aberto, e combatem aí com a sua própria postura (Defensiva ×1.20, nenhuma ×1.00, uma Emboscada válida ×1.40 — §5.4). Inimigos, estranhos e neutros ficam sempre fora. Mais três regras decidem uma zona: um **membro de ligação** fica onde fica o seu líder (Casos E e F abaixo); um exército **cercado** é uma Guarnição e fica dentro enquanto o anel se mantiver, aconteça o que acontecer à sua aliança (§2.13.7); e um reino que submete **nenhuma ordem** mantém as suas muralhas — os seus exércitos aí sem postura são colocados em Guarnição enquanto houver espaço e nenhum exército em guerra com ele estiver acampado fora (uma postura que tenha escolhido é mantida). Cada zona comporta no máximo **3 exércitos**. **Para defender uma cidade**, coloca até 3 exércitos em Guarnição; um exército deixado fora em Defensiva é uma barreira — o atacante tem de o vencer primeiro e, se for vencido, junta-se à Guarnição para o assalto. A Página do Jogador desenha as zonas que o motor decidiu (o leque é dividido por zona — §5.11), e isto é informação deliberada: em qualquer hexágono amuralhado que consigas ver, o emblema das muralhas (§5.11) diz-te quem está **dentro** — e, portanto, quem o proprietário conta como amigo, aliado, vassalo ou suserano — exatamente como um batedor leria as muralhas. Um grupo ligado que marche sobre muralhas chega **fora** com o seu líder; um membro amigo do proprietário do forte deixa o grupo em vez de combater esse proprietário ou os seus amigos (§5.11.1 regra 3), e, se a zona exterior transbordasse, todo o grupo pára no portão; a carta indica qual a zona que está cheia.

**Entrar — a Guarnição é a única porta.** Ordena Garrison e o exército fica dentro a partir da pré-fase desse turno — **mas nunca passando por um inimigo**: um exército que começou o turno fora das suas muralhas, com um exército **em guerra** com ele acampado aí, não pode ordenar a sua entrada (a ordem é lida como Defensiva, ×1.20, e uma carta explica porquê); tem de vencer esse exército primeiro. **Uma marcha nunca leva Garrison**: um exército que marche para casa chega fora e ordena Garrison no turno seguinte. Um exército **recrutado** numa sede de recrutamento amuralhada nasce em Guarnição, e um exército **dividido** de uma Guarnição fica dentro. O interior enche-se como qualquer zona: com 3 já em Guarnição, uma quarta ordem de Garrison fica fora, com carta. Um **grupo ligado** entra inteiro ou não entra — vencido fora ou ordenado para dentro (se vencido, entra inteiro, mas a ligação quebra-se como após qualquer batalha de campo perdida, §5.11) — e, perante um acampamento, fica barrado se **qualquer** dos seus reinos estiver em guerra com o acampamento. Todas as outras portas fecham-se da mesma maneira: uma ligação cujo líder está dentro não se pode formar perante um exército em guerra com o exército que se junta acampado fora, nem para um interior cheio (Caso F); e as tropas não podem ser **transferidas** de um exército fora para um exército dentro perante tal acampamento (*as tropas não passam para dentro das muralhas*). Um exército que deixa o seu grupo neste turno — por UNLINK, pela dispensa do seu líder ou pela regra 3 da §5.11.1 — e submeteu Garrison passa pela mesma porta. Uma Surtida (Sally) submetida por um exército que não está cercado é uma ordem de Garrison e passa pela mesma porta. **Uma Guarnição é um lugar nestas muralhas:** um exército expulso do seu hexágono durante o turno (uma retirada, um recuo) para outras muralhas fica fora delas sem postura, o que quer que tenha submetido. Um líder que dissolve o seu grupo neste turno e submete Garrison é julgado sozinho. **Um exército do proprietário ou de um amigo que esteja nas suas muralhas em qualquer postura que não Garrison é avisado uma vez disso** — *O exército N está fora das muralhas em (c,r)* — para que ninguém descubra a meio de um assalto. **Vencido fora, entra:** um exército do proprietário ou de um amigo atacado no terreno aberto das suas próprias muralhas que **perca** entra em Guarnição (se houver espaço) e defende o assalto que se segue no mesmo turno; um **empate** não muda nada para ele — o atacante recua. **Isto aplica-se apenas ao exército que já está no hexágono.** Um que venha de fora — um socorro que marche sobre o sitiante — e perca ou empate é o atacante: recua como qualquer atacante, nunca para dentro da cidade; e uma cidade cercada nunca é destino de retirada, pois o acampamento às suas portas bloqueia-o. Um exército apanhado **a sair ou a atravessar** as suas muralhas é lido como Moving, fica fora e combate aí: se vencer ou empatar, prossegue a marcha; se vencido, entra em Guarnição. **O conquistador** de muralhas — por assalto ou pela queda de um cerco — fica dentro delas em Guarnição.

> ***▶ Exemplos — a porta.***
>
> *- **Perante um acampamento.** O II da Hyperborea está em Defensiva fora das suas próprias muralhas em (24,34), e o VII da Aquilonia, em guerra com ela, está acampado ao lado. O II ordena Garrison: é lido como **Defensiva** (×1.20), com a carta O exército II não pode entrar nas muralhas em (24,34), e o varrimento de acampamento (camp sweep) da Fase 5 combate os dois. Se o II vencer, o VII recua e o II pode ordenar Garrison no turno seguinte; se o II perder, entra em Garrison.*
>
> *- **Um interior cheio.** Três exércitos da Hyperborea ocupam (24,34) em Guarnição. Um quarto, o IV, ordena Garrison: fica fora em **Defensiva** (×1.20), com a carta O exército IV não pode entrar nas muralhas (sem espaço dentro); a Página do Jogador desativa o botão por falta de espaço dentro. Se um dos três marchar, ordena Garrison outra vez: a ordem recusada foi mantida como Defensiva. Um grupo ligado conta-se inteiro — um líder e o seu membro precisam de dois lugares.*
>
> *- **Um grupo misto.** O II da Hyperborea lidera o VI da Nemedia fora em (24,34), e o VII da Aquilonia, em guerra apenas com a Nemedia, está acampado aí. O II ordena Garrison: todo o grupo fica fora em Defensiva, porque um dos seus reinos está em guerra com o acampamento. Uma transferência de um exército nemédio fora para um exército nemédio dentro é recusada da mesma maneira (as tropas não passam para dentro das muralhas).*
>
> *- **Um reino que falhou o turno.** A Nemedia não submete ordens. O seu VI, sem postura, está nas suas próprias muralhas com espaço dentro: o VI é colocado em Garrison e mantém as muralhas. Se o VI estivesse em Defensiva, ficaria fora em Defensiva; se um exército em guerra com a Nemedia estivesse acampado fora, o VI ficaria fora sem postura.*

Para sitiar ou assaltar, **marcha sobre o forte — e marchar para dentro é um ASSALTO PRECIPITADO (HASTY ASSAULT)** (assalto à chegada). A marcha enfrenta primeiro **todos os exércitos hostis fora** — os exércitos do proprietário e dos seus amigos que não estejam em Guarnição, um sitiante rival, uma força de socorro — numa **batalha às portas**, em campo aberto. **Vence-a**, sem nenhum acampamento hostil restante fora, e **assaltas as muralhas no mesmo turno**: contra a Guarnição dentro (×1.30), o bónus de fortaleza da curva de tamanho das muralhas (×1.55–×7.00 escalado pela integridade; atacante ×0.85 apenas com integridade total — §5.6.1) e a milícia — os exércitos que venceste fora entraram e defendem com elas. **Perde ou empata** a batalha das portas e a marcha termina e o atacante recua (§5.5.6). Um desembarque (landing) é a exceção: os seus sobreviventes entrincheiram-se fora das muralhas (§5.7.2). Com o terreno aberto limpo, assaltas de imediato. **Vence o assalto e tomas o forte. Se fores repelido mas sobreviveres, ficas acampado às portas** (a zona exterior) — esse acampamento é a rampa de acesso a um cerco de vários turnos. Uma **Marcha de Cerco (Siege March)** que vença as portas monta o cerco em vez de assaltar (§5.8). Um Assalto ordenado a partir de um acampamento às portas (§2.13.6) e um desembarque (§2.14.6) seguem a mesma ordem: primeiro o terreno aberto, depois as muralhas. **Uma Guarnição nunca sai** para participar num combate às suas portas — só um exército cercado que ordene **Sally** sai (§2.13.7). Os inimigos não partilham uma zona por muito tempo: o varrimento de acampamento seguinte combate-os (§2.13.5) — dentro de uma cidade **cercada** em cada varrimento, pois o seu perdedor fica dentro (§2.13.7); os inimigos **do outro lado da linha da muralha** partilham o hexágono em paz, à distância de uma lâmina.

> ***▶ Exemplo prático — duas marchas sobre um forte num turno.** **X**, um grupo ligado de três exércitos (60 MP, estado 97), e **Y** (60 MP, estado 90) ordenam ambos um passo de planície sobre **Z**, um pequeno porto amuralhado do próprio reino de Y — muralhas 50 HP, população 21, **nenhum exército dentro**. X está em (29,26) e Y em (27,27); Z é (28,26). (Três exércitos não ligados de X tomariam Z com o primeiro e chegariam fora com os outros dois, que Y enfrentaria primeiro em campo aberto.)*
>
> *\| Ronda 1 da Fase 5 \| O que o motor faz \| Porquê \|*
>
> *\|---\|---\|---\|*
>
> *\| **X move-se primeiro** (estado 97 vence 90 — §2.13.1) \| Z é um forte estrangeiro sem ninguém dentro: **assalto precipitado** só contra a milícia. 1,361 vs 21 — Z cai. Os três exércitos de X estão agora **dentro** de Z, em Guarnição \| §5.8.0: marchar para dentro é um assalto precipitado; o conquistador fica dentro em Guarnição \|*
>
> *\| **Y move-se em segundo**, 30 MP gastos, 30 restantes \| Z é agora um forte estrangeiro com três exércitos inimigos dentro: Y **assalta as muralhas de imediato** (ninguém está fora). Os exércitos de X defendem atrás delas em Guarnição (×1.30), com a milícia de 21 ao lado, muralhas 50 HP. Vencer → Z volta a ser de Y e os sobreviventes de X retiram-se; repelido → Y entrincheira-se às portas \| §5.8.0: o conquistador é uma Guarnição; §5.6 \|*
>
> ***Os MP nunca decidem uma batalha:** os 30 MP restantes de Y não compraram nada — uma batalha não custa MP, e chegar às muralhas termina uma marcha, sobre o que restar (§2.13.2).*

**Marcha de Cerco (Siege March) — chegar às portas sem as assaltar.** Marchar sobre uma construção amuralhada inimiga significa normalmente um **assalto precipitado** nesse mesmo turno. Um exército na postura **Siege March**, em vez disso, avança e **acampa** na zona exterior: as muralhas não são assaltadas, ninguém dentro combate, e mesmo um forte indefeso não é capturado — tomas-o com o Assalto do turno seguinte. A postura atua apenas onde a marcha **termina**: uma Siege March cuja marcha termine em qualquer lugar que não sejam muralhas inimigas — ou sem marcha nenhuma — não faz nada, e a carta do exército di-lo. Um exército já acampado às portas ataca com **Assault**, não com uma marcha. Um **povoado aberto** (um nível cuja muralha é 0, §3.7.1a) não tem portas onde acampar: uma Siege March sobre ele é uma marcha vulgar, e é tomado à sua milícia como qualquer hexágono indefeso (§2.13.4). O preço paga-se em tempo e exposição: a marcha cobre **um hexágono por turno**, e se um exército inimigo atacar a coluna esta defende a **×0.85** (um sitiante já entrincheirado às portas defende a ×1.00 contra a surtida que enfrenta, e a ×0.85 contra um exército de socorro que o ataque de fora). **Chegar às portas monta o cerco** — mesmo quando primeiro teve de vencer um inimigo acampado aí. Montá-lo declara guerra a todos os reinos dentro, incluindo um amigo teu (§5.6). A postura guardada do exército torna-se Siege à chegada e, se a coluna passar aí e então o teste de força da §5.8.1, **o anel fecha-se de imediato** — a menos que outro reino já mantenha o anel aí, caso em que o tick seguinte decide entre os dois sitiantes (§5.8.2). Um grupo ligado conta em conjunto, mas um membro que seja amigo do proprietário das muralhas deixa o grupo nessas muralhas e não conta. Os reinos dentro ficam cercados a partir do turno seguinte (§2.13.7); o proprietário das muralhas e todos os reinos dentro são avisados nesse turno, e o cerco faz o seu primeiro progresso no tick do turno seguinte. Uma coluna demasiado pequena para o teste de força apenas acampa: o seu Siege fica guardado e fecha o anel no primeiro tick que passar, uma falha registada em carta como de costume. Ordena Assault ou outra postura para fazer diferente. Investir uma fortaleza estrangeira declara guerra, tal como um assalto. Um exército inimigo já acampado fora dessas muralhas é combatido como uma batalha de campo vulgar (um sitiante, como uma marcha, combate o acampado **em guerra** com ele antes de um pacífico) — a Siege March isenta-te das *muralhas*, não dos *exércitos*. **Acampar também custa descanso**: um exército acampado num hexágono fortificado estrangeiro não recupera ESTADO, seja qual for a sua postura (§5.10.5).

**A postura nunca assalta muralhas, nem à chegada nem à partida.** Ao marchar para fora de um hexágono fortificado contra o qual está acampada, uma Siege March desengaja-se e avança um hexágono — como toda a postura a partir de uma origem fortificada; o terreno aberto continua a ser reclamado à partida (§2.13.2b).

Depois, a partir do hexágono do forte, ordena **Siege** ou **Assault** nos turnos seguintes (não se pode sitiar a partir de um hexágono adjacente). A partir do turno seguinte ao da montagem do anel — na chegada de uma Siege March ou no teu primeiro tick de cerco (§2.13.7) — os exércitos dentro ficam **cercados**: mantêm a Guarnição, não podem marchar para fora, e podem ordenar uma **Sally**, combatida antes do teu tick de cerco ou assalto (§2.13.7). **O lado perdedor de qualquer combate de campo enterra pelo menos um soldado** — um piquete de um só homem não pode fazer surtidas para sempre. **Um assalto repelido não abandona o cerco**: os seus atacantes sobreviventes ficam acampados às portas e podem prosseguir no turno seguinte — só a aniquilação, ou perder o terreno aberto numa batalha às portas, os remove. Reforçar um forte cercado significa combater através do acampamento fora; retirar *para dentro* de um forte cercado através das linhas de cerco não é possível, e uma **ligação** também não atravessa a linha de cerco em nenhum sentido (§2.13.7).

> ***▶ Exemplo prático — a cidade amuralhada de A, o exército de B ao lado, C a vir buscar ambos.** A possui um hexágono amuralhado; o exército de A e o exército de B (B é aliado mútuo de A) estão nele; C está em guerra com ambos. Cada linha abaixo é o que o motor realmente faz.*
>
> ***Turno 1 — C marcha para dentro (postura Moving); A mantém Garrison, B mantém Defensiva.***
>
> *\| O que acontece \| Porquê \|*
>
> *\|---\|---\|*
>
> *\| **A está dentro, B está fora.** Só uma Guarnição fica atrás das muralhas: A mantém-nas; B, em Defensiva, está no terreno aberto \| §5.8.0 \|*
>
> *\| **C enfrenta B primeiro, em campo aberto** — B a ×1.20, sem muralhas, sem milícia. **B vence** → C recua, as muralhas nunca são alcançadas. **B perde** → B entra em Guarnição, e C assalta as muralhas no mesmo turno contra A e B (Guarnição ×1.30 cada), o bónus de fortaleza e a milícia. **Empate** → C recua; B fica fora \| §5.8.0 \|*
>
> *\| **C toma as muralhas — o forte é de C**, e os sobreviventes de A e B são expulsos. **C é repelido pelas muralhas — entrincheira-se às portas** como sitiante, e no turno seguinte pode ordenar Siege \| §5.6, §5.8.0 \|*
>
> ***Turno 2 — C adota a postura Siege; A e B estão dentro, em Garrison.***
>
> *\| O que acontece \| Porquê \|*
>
> *\|---\|---\|*
>
> *\| **Nenhuma batalha.** Um sitiante não assalta, e ninguém dentro está ainda cercado — o primeiro tick de C monta o anel após a verificação (§2.13.7), pelo que A e B ainda podem marchar para fora neste turno; só podem fazer Sally a partir do Turno 3 \| §5.8.2 \|*
>
> *\| **O contador de cerco sobe 1 por turno**, até um limiar de **4** — ou **5** se o hexágono for a tua sede de recrutamento. Passado o limiar a guarnição rende-se, sem uma única batalha \| §5.8.2–3 \|*
>
> *\| **A partir do Turno 3, A e B estão cercados** — Garrison ou Sally, sem marcha. Para quebrar o anel ordenam **Sally**: A e B saem **juntos**, ligados ou não, e combatem C em campo aberto como atacante. Vencer → C recua e o cerco é levantado; empate → sem progresso nesse turno; perder → regressam a Guarnição, e o cerco avança \| §2.13.7 \|*
>
> *\| **Se nunca fizerem Sally**, as muralhas caem no limiar: o exército de A rende-se com elas (um exército cercado é uma Guarnição); o de B, um aliado, é expulso — ou abatido se encurralado \| §2.7 \|*
>
> ***Caso D — acrescenta um quarto exército: D, de A, um Elfo na floresta do hexágono em Ambush.***
>
> *\| O que acontece \| Porquê \|*
>
> *\|---\|---\|*
>
> *\| **D está FORA das muralhas — Turno 1, Turno 2, façam A e B o que fizerem.** Só uma Guarnição está dentro; uma Emboscada não é uma Guarnição. (D não está ligado aqui. Uma ligação altera isto — vê os Casos E e F abaixo: um membro fica onde fica o seu líder.) \| §5.4, §5.8.0 \|*
>
> *\| **Turno 1 (C marcha para dentro): C tem de combater D em campo aberto PRIMEIRO** — com B também, se B ainda estiver fora em Defensiva. D defende em Ambush ×1.40, oculto até ser atingido. **C vence** → os vencidos entram em Guarnição, e C assalta as muralhas no mesmo turno; **C perde ou empata** → a marcha termina aí, com as muralhas intocadas \| §5.4, §5.8.0 \|*
>
> *\| **Vença, perca ou empate, a armadilha de D está agora acionada.** Qualquer Emboscada que combate fica gasta — e **a partir desse mesmo turno D é desenhado em todos os mapas estrangeiros**, de aliado e de inimigo por igual (uma emboscada acionada não oculta nada, mesmo que a página volte a submeter a ordem Ambush) \| §5.4 \|*
>
> *\| **D vence ou empata → C recua; D fica fora**, agora em Defensiva — já não oculto, já sem bónus, até ser reordenado para Ambush e o seu terreno voltar a validar \| §5.4, §5.8.0 \|*
>
> *\| **D perde → D entra em Guarnição** (se houver espaço) — vencido fora das suas próprias muralhas, as muralhas são o seu refúgio — e defende o assalto que C lança no mesmo turno. Sem espaço dentro, retira como um exército de campo (§5.5.6), destruído se cercado, e não mantém postura nenhuma (§5.4) \| §5.8.0 \|*
>
> *\| **D nunca é cercado enquanto está fora.** O cerco cerca os exércitos DENTRO. Se D voltar a sair mais tarde enquanto C acampa às portas, os dois partilham a zona **EXTERIOR** e o **varrimento de acampamento da Fase 5** combate-os em cada turno até um morrer ou marchar — D em Defensiva ×1.20 (ou uma nova Emboscada válida), em campo aberto, sem muralhas e sem milícia. **Uma emboscada fora das tuas portas compra-te uma boa batalha, não um quebra-cercos permanente** \| §2.13.5, §5.4, §2.13.7 \|*
>
> ***Caso E — a ligação arrasta a guarnição para fora. A liga o seu exército B ao emboscador D.***
>
> *A regra que o faz é a mais simples da §5.11: **um grupo ligado fica junto.** D está fora das muralhas, D é o líder, por isso todos os membros do grupo de D estão também fora das muralhas — incluindo B, cuja Guarnição o teria de outro modo mantido atrás delas. **Ligar um exército a um emboscador tira-o do castelo.** Não é um erro e não é reversível a meio do turno: desliga-o, ou não o ligues.*
>
> *\| Quem \| Onde acaba \| Com que combate \|*
>
> *\|---\|---\|---\|*
>
> *\| **D — o líder, Elfo do próprio A em Ambush** \| Fora. Oculto até ser atingido \| Terreno × **Ambush ×1.40**. Sem bónus de fortaleza, sem milícia \|*
>
> *\| **B — exército PRÓPRIO de A, ligado sob D** \| **Fora, arrastado pela ligação** \| **Herda o Ambush ×1.40 de D** (um membro não tem postura própria — obedece à do líder, §5.11) e fica **oculto com ele**. Mas as muralhas desapareceram: sem bónus de fortaleza, sem milícia \|*
>
> *\| **B' — exército de um ALIADO, ligado sob D em vez disso** \| **Fora, arrastado da mesma maneira** \| **Nada.** O membro de um aliado sob um líder em Ambush é lido como em movimento (§5.4): **nenhum bónus de postura**, e fica **visível** no mapa do inimigo. Deixou as muralhas e nada recebeu em troca \|*
>
> ***Lê a terceira linha duas vezes antes de aceitares um aliado num grupo de emboscada.** O exército do teu aliado dentro da tua cidade, em Garrison, tem ×1.30, o bónus de fortaleza e a milícia. Ligado ao teu emboscador tem ×1.00, sem muralhas e sem milícia, e é a única marca no hexágono que o inimigo consegue ver. A emboscada ganha um corpo; o teu aliado paga por ele. É uma tática real — um membro visível é também **isco**, e o inimigo não consegue ver o que está ao lado dele — mas é o exército dele que estás a gastar, por isso pergunta-lhe primeiro.*
>
> *O mesmo vale para o teu próprio exército na linha dois, sem a penalização: B mantém o ×1.40 e a ocultação, e abdica das muralhas. Essa é toda a troca — **estás a converter uma guarnição num segundo emboscador.** Contra um inimigo que teria assaltado as muralhas, isso é normalmente bom; contra um que teria cercado e feito passar fome, acabaste de abdicar da coisa que te mantinha vivo.*
>
> *Uma consequência que surpreende as pessoas: como o grupo está fora, **B está agora na zona do sitiante**, pelo que o varrimento de acampamento da Fase 5 o combaterá em cada turno em que os dois lados permaneçam em guerra nesse hexágono (linha quatro do Caso D), e o Ambush de B — tal como o de D — fica gasto da primeira vez que combate.*
>
> ***Não sob cerco.** Se B já está **cercado**, não pode seguir D para fora: deixa em vez disso o grupo de D (besieged — left its link group) e fica dentro (§2.13.7).*
>
> ***Caso F — inverte a ligação: B mantém as muralhas e é o LÍDER, D o emboscador é o MEMBRO.** (O espelho do Caso E, com as portas livres — C ainda não chegou.)*
>
> *Mesma regra, resultado oposto. O grupo fica onde fica o **líder**, e o líder está dentro — por isso **a ligação puxa o emboscador PARA DENTRO**. E um membro não tem postura própria: o Ambush de D não é enfraquecido, **desaparece**. D combate com a postura de B.*
>
> *\| Quem \| Onde acaba \| Com que combate \|*
>
> *\|---\|---\|---\|*
>
> *\| **B — o líder, a manter as muralhas em Garrison** \| Dentro, como antes \| Garrison **×1.30**, bónus de fortaleza, milícia \|*
>
> *\| **D — o emboscador Elfo, agora um membro** \| **Dentro, puxado pela ligação** \| **Garrison de B ×1.30**, bónus de fortaleza, milícia. **Nenhum Ambush** — nem ×1.40, nem ocultação, nem a armadilha \|*
>
> ***Esta é normalmente uma boa troca, e a do Caso E normalmente não é.** ×1.30 atrás de muralhas com a milícia ao lado vence ×1.40 nu em campo aberto. Assim, a ligação é uma forma de chamar o teu emboscador para dentro — e a ligação inversa é uma forma de tirar uma guarnição para fora. Escolhe o líder deliberadamente: **a zona do líder é a zona do grupo, nos dois sentidos.***
>
> *Pormenores que apanham as pessoas:*
>
> *- **Não perante um acampamento inimigo, nem para um interior cheio.** Uma ligação para dentro é uma porta como uma ordem de Garrison: com um exército em guerra com D acampado fora — C às portas — ou com 3 exércitos já dentro, a ligação é recusada (Link refused, a carta indica qual) e D fica fora. Uma ligação entre exércitos em lados opostos das muralhas só se forma quando ambos são amigos do proprietário das muralhas.*
>
> *- **Um emboscador gasto também entra** — um membro fica onde fica o seu líder.*
>
> *- **O exército de um aliado em Ambush não pode ser puxado para o teu grupo de todo** — a tua oferta fica simplesmente sem resposta, e nunca te dizem porquê (§5.11). Com um aliado, a única alavanca que tens é pedir-lhe.*
>
> *- **Não sob cerco.** Se B está **cercado**, uma ligação nunca leva um exército através da linha de cerco: D é retirado do grupo (did not join the besieged group) e fica fora (§2.13.7).*
>
> ***Entretanto, o que pode A fazer quanto a C acampado fora das suas próprias portas?** Enquanto C apenas acampa — ainda sem Siege — A **não está cercado**, pelo que não há Sally a ordenar (§2.13.7), e dentro contra fora uma muralha nunca é um choque de acampamento. Uma Guarnição nunca sai para participar num combate (§5.8.0), e uma partida nunca disputa o terreno. A tem três maneiras de atacar C:*
>
> *- **Sair.** Ordena qualquer postura exceto Garrison: o exército fica fora a partir da pré-fase desse turno, ao lado de C, e o varrimento de acampamento da Fase 5 combate-os (A defende — o terreno é de A). Se vencido, volta a entrar, em Garrison. Não pode simplesmente ordenar a sua volta enquanto C acampa aí (a porta está fechada perante um acampamento, acima): tem de vencer, perder, ou esperar que C se vá embora.*
>
> *- **Marchar outro exército para dentro.** Um exército que chega ao seu próprio hexágono onde está um exército não amigo combate-o — "Reclaiming home ground — no hex changes hands" — e a zona não protege C.*
>
> *- **Marchar para fora e voltar.** Sair não custa nada enquanto A não está cercado (uma partida nunca assalta nem disputa, §2.13.2b); a marcha de regresso é o ataque.*
>
> *Seja qual for o modo, o exército que marcha é o **atacante**, sem muralhas e sem bónus de postura. **Quando o anel se mantém**, os exércitos de A dentro já não podem marchar para fora nem juntar-se a esse ataque — resta apenas a sua própria Sally, ou um socorro a combater sozinho.*
>
> ***O espelho para C, acampado fora das muralhas de A.** Uma ordem de movimento de zero passos (um caminho que começa e termina no hexágono em que estás) é rejeitada — uma ordem tem de dar um passo até um vizinho — por isso C não pode "reentrar" no hexágono em que já está. Marchar **para fora** nunca provoca um combate (§2.13.2b); marchar **de volta para dentro** no mesmo turno é uma chegada vulgar a um hexágono fortificado estrangeiro, isto é, um **assalto precipitado** exatamente como a primeira marcha de C: os exércitos fora são combatidos primeiro, depois a Guarnição dentro é assaltada. É o mesmo resultado que ordenar **Assault** a partir do acampamento, ao preço de dois hexágonos de marcha. Só um exército que regresse ao seu próprio forte ou a um forte aliado não encontra senão o que está fora: chega fora e nunca assalta. **Essa é a verdadeira assimetria de um cerco: o sitiante decide quando vem o assalto; os cercados decidem apenas se, e quando, fazem Sally.***

**5.8.1 Força Mínima de Cerco (Minimum Siege Force)**

Antes de um cerco (siege) poder começar, o exército (army) sitiante tem de ser suficientemente grande para cercar o alvo. **Ambas** as condições seguintes têm de se verificar face à população (pop) do hexágono (hex) alvo:

- **Força (corpos):** soldados ≥ floor(pop × 0.3) — pelo menos 30% da população em **soldados**, para cercar as muralhas (walls). **Um cavaleiro conta como dois:** os cavaleiros patrulham e cortam as estradas em terreno que um soldado de infantaria não consegue cobrir, pelo que fecham um arco maior do anel. Repara no espelho deliberado: o mesmo cavaleiro vale **o dobro** para fechar um anel e apenas **65%** para escalar uma muralha (§3.5.1) — a cavalaria sela um cerco, a infantaria toma-o de assalto. Os recrutas (recruits) levantados neste turno (§2.6a) já contam para o requisito de corpos quando se avalia um tick estacionário. **Os engenhos não são corpos:** as máquinas não conseguem guarnecer uma linha de cerco, pelo que um exército de 10 soldados a transportar 40 engenhos conta 10 sitiantes, não 50. (Os seus pontos de guerra continuam a contar abaixo — os engenhos combatem.) Todo o **grupo ligado (link group)** conta em conjunto, líder e membros por igual.

- **Poder de guerra:** armyWP × status \> floor(pop × 0.05) × 20 — forte o suficiente, **ao ESTADO atual do exército**, para dominar a milícia do povoado (a mesma imposição de floor(pop × 5%) × 20 WP que defende um assalto, §5.6). Os WP nominais são escalados pelo ESTADO (o ESTADO do turno que acabou de terminar — a verificação corre antes de qualquer recuperação); um grupo ligado soma os WP escalados de cada exército. Os corpos **não** são escalados: um soldado exausto continua a fazer parte do anel.

- **Um grupo ligado é testado como um só, a partir do seu líder:** os corpos e os WP escalados de todos os membros — os teus próprios exércitos e os exércitos aliados ligados ao líder — são somados. O cartão de exército de um membro mostra o mesmo grupo.

Se **qualquer uma** falhar, o cerco **não** avança: sem Progresso de Cerco, não se lança um primeiro anel (um anel lançado num turno anterior mantém-se, e os exércitos no seu interior continuam cercados — a falha só pára o contador), e o exército recebe um cartão de relatório *"Siege of (c,r) failed — force too small"* que indica a insuficiência; o seu cartão de exército mostra o cerco como *stalled* (sem contagem decrescente) até a força bastar. A postura de Cerco é **mantida** numa falha apenas de força: o anel é apertado sem nova ordem no turno em que a força bastar — reforça, e o cartão di-lo. É mantida também quando um exército com ordem de Cerco teve primeiro de limpar um acampamento inimigo às portas e venceu (o seu anel é lançado no turno seguinte; uma Marcha de Cerco fecha-o à chegada, §5.8.0), e enquanto um anel **amigo** se mantiver no hexágono. Uma paz assinada, ou um Cerco ordenado num turno que não lança anel, limpa antes a postura (§5.8.5). O exército limita-se a manter o seu hexágono — pode receber nova ordem de Assalto, ou esperar por reforços.

Como a fasquia escala com a dimensão do *alvo*, os grandes povoados tornam-se efetivamente só de assalto: uma pequena posse (pop 500) precisa de ~150 tropas e \>500 WP, mas uma sede crescida (pop 10,000) precisa de ~3,000 tropas. A verificação é feita face à população que o sitiante consegue ver — um exército acampado no hexágono de um povoado estrangeiro vê a população no seu relatório, pelo que o requisito é conhecido antes de te comprometeres com a ordem.

Esta exigência de força aplica-se **apenas ao Cerco**. Podes sempre *tentar* um Assalto (§5.6) com um exército de qualquer dimensão (uma força minúscula perde simplesmente contra a milícia e as muralhas). Ninguém no interior combate num Cerco a menos que esteja **cercado** e ordene **Surtida** (Sally) (§2.13.7) — essa batalha acontece *antes* de se chegar sequer à barreira do cerco.

> ***▶ Exemplo.** Um exército de 1 unidade junto de um povoado de 500 pop: 1 \< floor(500 × 0.3) = 150 → **Cerco Falhado**, nada acontece. Um exército de 200 velites (8,600 WP) com ESTADO 60 passa ambas as barreiras (200 ≥ 150, 8,600 × 0.60 = 5,160 \> 500) e o cerco prossegue normalmente.*
>
> ***▶ Exemplo prático — um cerco da marcha à queda.** Aldoria (**A**) está em guerra com Gruk-Mor (**G**), cuja cidade amuralhada **Z** tem 1,000 habitantes: a fasquia do §5.8.1 é de **300 soldados** (os cavaleiros contam a dobrar) e **mais de 1,000 WP ao ESTADO** (floor(1000 × 0.05) × 20). Sylvane (**S**) é aliada de A, também em guerra com G.*
>
> *\| Turno \| O que acontece \| Regra \|*
>
> *\|---\|---\|---\|*
>
> *\| **1** \| O Exército I de A (200 legionários, ESTADO 100) chega ao hexágono de Z em **Marcha de Cerco (Siege March)**. Ninguém está acampado no exterior, pelo que faz acampamento e **lança o cerco por si só**: o Cerco fica armazenado, o cartão indica a fasquia (300 soldados, \>1,000 WP). Com 200 corpos fica abaixo dessa fasquia, pelo que o anel **ainda não** é fechado. Se um inimigo estivesse acampado às portas, A teria combatido primeiro — e, vencendo, lançaria o cerco na mesma. \| §5.8.0 \|*
>
> *\| **2** \| Pré-fase: o anel é testado. 200 corpos \< 300 → "Siege of (c,r) failed — force too small" (efeito: a postura de Cerco MANTÉM-SE EM VIGOR). Sem tick, sem anel, **a postura é mantida**. No mesmo turno A transfere 150 homens do seu Exército II, acampado ao lado de I — as transferências resolvem-se na Fase 4.5, depois desta verificação. \| §5.8.1 \|*
>
> *\| **3** \| Os 150 homens transferidos no turno anterior contam agora: 350 ≥ 300 e 350 × 67 × ESTADO 0.95 ≈ 22,000 WP \> 1,000 → o anel fecha sem ordem submetida: "Siege tightens at (c,r) — 1/4". A paga 3 de ESTADO de manutenção de cerco e não recupera nenhum enquanto estiver junto de muralhas estrangeiras. \| §5.8.1 ao ESTADO, §5.10 \|*
>
> *\| **4** \| O exército de socorro de G marcha para o hexágono vindo do exterior. A é o **defensor** dessa batalha em campo aberto com **Cerco ×0.85** (um socorro por desembarque vindo do mar encontraria o mesmo ×0.85; uma surtida da própria guarnição de Z não — A mantém ×1.00 contra ela). A vence: "2/4". \| §5.5.1 \|*
>
> *\| **5** \| O Exército I de S chega em marcha de cerco e lança cerco ao lado de A. Pré-fase do turno 6: ambos pressionam; o WP × ESTADO de A é superior, pelo que **as linhas de S cedem** — "Siege lines yielded at Z — Aldoria holds the ring … you remain a besieger". S mantém o seu Cerco, paga os mesmos 3 de manutenção, e um socorro encontraria **ambos** a ×0.85. A: "3/4" no turno 5, "4/4" no turno 6. \| §5.8.2 \|*
>
> *\| **7** \| O progresso 5 **excede** o limiar de 4 — Z cai para A na pré-fase do turno 7 (uma sede teria precisado de mais um: limiar 5). Seis turnos de pressão desde a chegada, contando o falhado. \| §5.8.3 \|*
>
> *\| (alternativa 6) \| A e G assinam a paz. O anel de A levanta-se e o Cerco armazenado de A é **limpo** — "Siege ended by peace" — pelo que nada volta a declarar a guerra no turno seguinte. A continua acampado; dá-lhe uma postura. **Z não está livre:** S, ainda em guerra com G, continua a pressionar o seu próprio Cerco às portas, e o cerco prossegue sob S. \| §5.8.1 \|*
>
> *Um cartão que não verás neste fio: "Siege stance dropped" (apenas quando um Cerco que ordenaste não lançou anel — muralhas sem dono, por exemplo — ou quando um anel que existia no início do turno desapareceu por outro motivo).*

**5.8.2 Progresso do Cerco (Siege Progress)**

Exército com postura de Cerco parado SOBRE uma construção amuralhada estrangeira (acampado às portas, e cumprindo a força mínima do §5.8.1): siege_progress += 1 por turno, limitado ao limiar + 1. **Um reino sitiante por povoado.** Se dois reinos pressionam as mesmas muralhas no mesmo turno, aquele com maior poder de guerra **ao seu ESTADO atual** (o mesmo WP × ESTADO que a barreira do §5.8.1 lê) mantém o cerco e as linhas de cerco do outro cedem — mas quem cede **continua sitiante**: a sua postura de Cerco é mantida enquanto um anel amigo se mantiver, paga a manutenção do cerco, e um exército de socorro encontra **ambos** os sitiantes aliados a defender a ×0.85 — não faz progresso nesse turno e é informado num cartão *Siege Yielded*. Se o reino que cede agiu primeiro, já pagou o seu −3 de manutenção e disparou os seus engenhos — só o seu tick de progresso é desfeito. Um povoado **fundado neste mesmo turno** ainda não tem muralhas e não pode ser cercado nem assaltado nas muralhas. Qualquer exército que partilhe o terreno fora das muralhas e que não seja amigo teu — um sitiante rival, uma força de socorro, um acampado **neutral** — tem de ser combatido primeiro (declara-se-lhe guerra) — essa batalha custa o progresso do turno. Apenas o reino de um sitiante é registado por hexágono (campo besieged_by). Uma **Surtida** vinda do interior é combatida antes do tick: uma Surtida ganha levanta o cerco, uma empatada custa aos sitiantes que a combateram o progresso e o Assalto deste turno, e uma perdida nada altera — o cerco avança no mesmo turno (§2.13.7).

**5.8.3 Limiares (Thresholds)**

Uma construção amuralhada comum cai quando siege_progress \> 4 (após 5 turnos consecutivos de cerco bem-sucedido; uma sede após 6). A tua **sede de recrutamento (muster seat)** (§3.7.3) cai quando siege_progress \> 5 (após 6 turnos consecutivos).

O contador tem de **exceder estritamente** o limiar. O turno em que o sitiante chega nunca conta: o primeiro tick é o processamento seguinte.

**Só uma construção amuralhada pode ser cercada.** Um hexágono sem construção, ou cujo nível de família indique uma muralha de 0 (Orc Nível 0–3, Genérico Nv.1–4, Nómada Nv.1), não pode sustentar um cerco: qualquer progresso contra ele é limpo e o marcador de cercado é removido. Esses locais tomam-se simplesmente marchando para dentro e derrotando quem lá estiver.

> ***▶ Exemplo — quanto dura um cerco?** Em cada turno em que um exército mantém a postura de Cerco acampado no hexágono do povoado, o progresso sobe +1. Uma **construção amuralhada comum** cai quando o progresso excede 4: os turnos de cerco 1-2-3-4 levam-no a 4 (o cartão do defensor: Collapse imminent — cai no turno seguinte a menos que uma Surtida quebre o anel), o 5.º turno de cerco leva-o a 5 e **o povoado cai nesse mesmo processamento** — a verificação de queda automática corre logo após o tick de cerco, pelo que cinco turnos de cerco consecutivos tomam uma construção amuralhada comum (seis tomam uma sede de recrutamento). Uma **sede de recrutamento** precisa de progresso acima de 5 — seis turnos de cerco. **O progresso não sobrevive a uma interrupção:** no momento em que o reino sitiante deixa de manter o cerco — o seu último exército com postura de Cerco/Assalto sai do hexágono do próprio forte — a **verificação de Levantamento de Cerco (Siege Lift)** (executada na pré-fase de cada turno) repõe o contador diretamente a 0 (§5.8.5).*

**5.8.4 Queda Automática (Auto-Fall) (Pré-Fase 4)**

A queda resolve-se exatamente como o §2.7 estabelece: o hexágono transfere-se para o sitiante sem batalha, e o seu exército, parado no novo hexágono, está agora dentro das suas muralhas. Os exércitos do dono no interior rendem-se, todos os outros exércitos são expulsos ou postos em debandada, as frotas defensoras fazem-se ao mar, o local de produção desce um nível (§5.6.3), e a opinião oscila como numa batalha decisiva (§8.5.3).

**5.8.5 Levantamento do Cerco (Siege Lift)**

Um cerco é levantado — progresso de volta a 0, ambos os lados notificados por cartão — quando:

- uma **Surtida** vence e nenhum exército do reino sitiante fica às portas (§2.13.7);

- um exército de **socorro** derrota os sitiantes (o levantamento aparece no turno seguinte);

- o reino sitiante deixa de pressionar — submete uma postura que não seja Cerco ou Assalto, marcha para longe, ou já não tem soldados às portas. Os cartões dizem *lapsed* quando o exército ficou sem ordem de Cerco, *Siege of … abandoned* / *Siege broken … withdraws* quando marchou para longe. **Os engenhos não são soldados**: um exército reduzido apenas ao seu comboio de cerco não tem quem guarneça as linhas *nem* as máquinas, pelo que o seu cerco é levantado e a sua salva é zero, embora o próprio comboio sobreviva como exército até os soldados se lhe voltarem a juntar;

- o sitiante faz **paz com o dono das muralhas** — o anel levanta-se e o Cerco armazenado é limpo (*Siege ended by peace* — a guerra não recomeça por si só);

- as muralhas mudam de mãos.

Uma paz, ou uma aliança rompida, que envolva qualquer *outro* reino no interior não liberta ninguém (§2.13.7). Um sitiante demasiado fraco para o §5.8.1 apenas pára o contador; o seu anel continua firme — o dono das muralhas e todos os reinos com um exército no interior são informados em cada um desses turnos (*Still besieged … the siege counter stopped*): continua a ser só Guarnição ou Surtida, e um exército de socorro ainda o pode levantar. Um Cerco ordenado num turno que não lança anel — muralhas sem dono, por exemplo — é limpo e notificado: *Siege stance dropped … no ring was laid this turn; order Siege again*.

**O progresso não sobrevive a uma interrupção.** Um atacante posterior **nunca herda um cerco abandonado** — começa sempre de 0, pelo que um antigo cerco de dois turnos de que te afastaste não dá nada ao exército seguinte.

**Um assalto repelido** repõe o contador apenas quando não há sitiante presente: a contagem de cerco **própria** do assaltante sobrevive ao seu assalto falhado, pelo que um sitiante que assalta cedo e é repelido nada perdeu a não ser o sangue, e um reino que detenha besieged_by mantém o seu cerco seja o que for que o assalto falhado de um terceiro faça.

> ***⚠ O que isto significa — cerco vs. assalto.** Um cerco concluído captura o povoado **sem batalha e sem baixas para ti** — e o teu exército sitiante, já no hexágono, fica dentro das novas muralhas — mas tem de ficar exposto durante 5 turnos (6 contra uma sede de recrutamento). Um **assalto** (§5.6) é imediato e ocupa de facto o povoado em caso de vitória, mas é sangrento e as muralhas favorecem fortemente o defensor. O progresso do cerco apenas conta decrescentemente até à queda: não reduz a guarnição nem enfraquece as muralhas — só os engenhos de cerco as batem (§5.8.6) — pelo que um assalto a 4/4 encontra a mesma defesa que no primeiro dia. Jogo típico: cercar para imobilizar o defensor, depois a 4/4 (Falls next turn if the ring holds) assaltar se precisares do local já, ou simplesmente deixá-lo cair.*
>
> ***▶ Exemplo — um cerco completo, das portas à queda.** Cimeria e Aquilonia estão em guerra. O **III ARMY** de Cimeria, 300 Raiders, está a dois hexágonos do povoado amuralhado **FI8** de Aquilonia, no hexágono (31,17) — uma posse comum (não uma sede de recrutamento), população 800.*
>
> *- **Turnos 1–2 — aproximação.** Cimeria ordena **Marcha de Cerco**: o exército percorre um hexágono por turno, pelo que leva dois turnos a fechar a distância. Uma marcha comum para esse hexágono teria sido, em vez disso, um assalto precipitado às muralhas no momento da chegada; a Marcha de Cerco compra a aproximação sem combate.*
>
> *- **Turno 2, chegada — acampado às portas.** O III ARMY está na **zona exterior** do povoado: nenhuma muralha é assaltada. Investir uma fortaleza estrangeira declararia guerra por si só — irrelevante aqui, os dois reinos já estão em guerra. A chegada armazena o Cerco por si só (§5.4) e, passando a coluna o teste de força (abaixo), fecha logo o anel (§5.8.0) — o que bloqueia repair_wall a partir do turno 3.*
>
> *- **Turno 3 — o primeiro tick, sem ordem submetida.** O anel fechou à chegada porque a coluna passou aí a barreira de força: face à população 800, os corpos precisam de floor(800 × 0.3) = 240 soldados, o poder de guerra precisa de \> floor(800 × 0.05) × 20 = 800. Os 300 Raiders do III ARMY passam ambos por larga margem (300 ≥ 240; a 48 WP cada, 14,400 WP × ESTADO ≫ 800). Agora siege_progress começa a avançar, e começa a sangria de −3 de ESTADO. Acampado num hexágono fortificado estrangeiro, o III ARMY também **não recupera ESTADO** de turno para turno — o preço de nunca largar o anel.*
>
> *- **Opções de Aquilonia, a partir do turno 3.** Qualquer exército no interior está cercado — mantém Guarnição (×1.30 contra um eventual assalto) e não pode marchar para fora; pode ordenar uma **Surtida** para combater o III ARMY em campo aberto e quebrar o anel (§2.13.7); uma força de socorro pode marchar para o hexágono vinda do exterior e combater o III ARMY a ×0.85; ou Aquilonia pode absorver o −3/turno e as reparações bloqueadas e simplesmente esperar — até as muralhas caírem e todos os exércitos aquilonianos no interior se renderem.*
>
> *- **Turnos 3–6 — o relógio.** Quatro turnos de cerco tranquilos levam o progresso a 4: o cartão de Aquilonia diz Collapse imminent!. Nada antes do turno 7 força a questão — Aquilonia ainda poderia ordenar uma Surtida do interior, ou socorrer do exterior.*
>
> *- **Turno 7 — o progresso excede o limiar.** Um quinto turno de cerco leva o progresso a 5, acima da fasquia de \> 4 da construção comum.*
>
> *- **Turno 7, pré-fase — Queda Automática.** O hexágono transfere-se para Cimeria; todos os exércitos aquilonianos no interior se rendem; qualquer exército aquiloniano fora das muralhas retira ou é destruído; as frotas de Aquilonia fogem para mar aberto; o povoado desce um nível, de FI8 para FI7. O hexágono é de Cimeria, e o **III ARMY**, parado no seu novo hexágono amuralhado, está agora dentro das suas muralhas.*
>
> *- **A armadilha.** Se Cimeria tivesse retirado o III ARMY do hexágono por um só turno entre o 3 e o 6, a verificação de Levantamento de Cerco teria reposto o progresso diretamente a 0 — e um segundo exército cimério que chegasse mais tarde começaria também de 0, não de onde o primeiro ficou.*
>
> ***⚠ O que isto significa —** o cerco custa cinco turnos expostos, uma sangria contínua de ESTADO e zero sangue; um assalto à chegada teria sido imediato mas teria combatido as muralhas e a guarnição com plena integridade. A Marcha de Cerco é o que torna aqui possível o caminho lento — transformou o que teria sido um assalto precipitado às portas numa aproximação gratuita.*

**5.8.6 Máquinas de Cerco (Siege Engines)**

A fome (Starvation) não é a única forma de passar uma muralha. As **máquinas de cerco** (siege engines) derrubam-na diretamente, e uma muralha rompida vale mais do que um cerco encurtado — retira ao defensor o bónus de fortaleza *e* ao atacante a sua própria penalização (§5.6.1).

**Só funcionam sob uma ordem de cerco.** As máquinas batem a muralha num **cerco** (siege) — a ordem permanente, que a máquina nem sequer aceitará se a tua força não for suficientemente grande para cercar o local — e na **postura de Assalto** (Assault) ordenada a partir das portas **apenas se essa mesma prova de força for superada** (um exército demasiado pequeno para cercar que ordene Assalto todos os turnos ataca de mãos nuas; o seu relatório traz um cartão *Engines Idle* a indicar a insuficiência) (§5.8.1). **Não** batem a muralha quando um exército simplesmente marcha para um hexágono fortificado e combate o assalto improvisado que se segue, nem numa reivindicação de origem, nem num desembarque em praia. Se queres a muralha no chão, compromete-te com o cerco.

**A coluna é lenta e arde numa debandada.** Um exército que transporta máquinas marcha **um hexágono por turno, seja qual for o terreno** — e um membro que leve máquinas, mesmo aliado, abranda todo o seu grupo LINK para o mesmo passo de caracol (§5.11). Se planeares mais longe, o Processador de Turnos (Turn Processor) elimina os hexágonos a mais com um cartão 🏗; a Página do Jogador (Player Page) não te deixa planear além de um hexágono. As retiradas estão isentas do limite. E se uma batalha correr mal, **as máquinas são abandonadas em qualquer retirada**: um exército em debandada não consegue arrastar a sua coluna de um campo perdido — as máquinas são destruídas no local (uma Surtida (Sally) que perca ou empate perde também as suas máquinas na confusão do regresso ao interior, a não ser que nenhum hexágono exterior estivesse livre) (o cartão 🏗 indica o número), além do que a própria batalha lhes tenha custado. Duas isenções deliberadas: um espectador **deslocado** de um hexágono conquistado na batalha de *outrem* nunca combateu — retira-se em ordem e **conserva a sua coluna**; e **no mar são os navios que fazem o transporte** — uma coluna embarcada navega à velocidade plena da frota (o passo de caracol retoma-se no instante em que desembarca). Um exército reduzido a *nada mais* do que a sua coluna pela batalha perde tudo na debandada e é destruído. Entre o passo de caracol e a regra da debandada, uma coluna de cerco é um compromisso: chega devagar e não volta para casa de uma derrota.

Cada raça constrói as suas, todas com estatísticas idênticas:

|           |                |                                                                                                                                                                                                            |
|-----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Raça**  | **Máquina**    | **A máquina real por detrás do nome**                                                                                                                                                                      |
| Imperial  | Onager         | A catapulta de torção imperial (tendão ou cabelo torcido), cujo braço único "dava um coice" ao disparar — daí o nome: *onager*, o burro selvagem.                                                          |
| Bárbaro   | Stone-Thrower  | O trabuco de tração (de origem chinesa, adotado em todo o mundo antigo): uma viga pivotante puxada por dezenas de homens com cordas — artilharia coletiva de força bruta, sem contrapeso.                  |
| Elfo      | Great Ballista | A balista imperial: uma besta gigante de torção de notável precisão, que arremessa virotes pesados ou esferas de pedra — a mais cirúrgica das máquinas antigas.                                            |
| Anão      | Trebuchet      | O trabuco medieval de contrapeso (a partir do século XII): engenharia pura — toneladas de lastro a converter a gravidade em projéteis de 100 kg; a máquina que verdadeiramente demoliu muralhas antes da pólvora. |
| Orc       | War Catapult   | O termo genérico — qualquer engenho de arremesso por braço, do grego *katapeltēs*, "perfurador de escudos"; aqui na sua leitura mais tosca: pedra grande, arco largo, pouca pontaria.                      |
| Aesir     | Valslöngva     | Um nome real do nórdico antigo (≈ "funda assassina"): o engenho de arremesso que as fontes escandinavas atestam nos cercos vikings — essencialmente o trabuco de tração na sua encarnação nórdica.            |
| Nómada    | Mangonel       | O termo genérico medieval para a catapulta de torção/tração mais leve das campanhas — mais portátil do que um trabuco, a favorita dos exércitos em movimento (o *manjaniq* das hostes das estepes e islâmicas). |

**Estatísticas:** ataque 1, defesa 1, HP 8, **10 WP**, a pé. **Custo 250g + 50 madeira + 10 ferro**, manutenção **3g/turno**. Dano à muralha **250 por máquina por turno**.

Não existe **nenhuma máquina Generic** — Generic é uma família de construção, não um povo, e não tem lista própria.

**Como se resolve o bombardeamento:**

- **Só disparam as máquinas com tripulação.** Cada exército opera no máximo floor(os seus próprios soldados ÷ 5) das suas máquinas — a mesma tripulação de 5 por máquina que condiciona a construção condiciona também a salva. A tripulação é **por exército**: os soldados de um aliado ligado nunca manobram as *tuas* máquinas, e as máquinas nunca tripulam máquinas. As máquinas sem tripulação são peso morto — seguem na coluna, abrandam a marcha, combatem (mal) e ardem nas debandadas, mas nada acrescentam à muralha; transferir máquinas para um exército com tripulação insuficiente é logística legal, mas não compra poder de fogo. **As baixas em batalha reduzem, portanto, a salva**: mata os soldados do sitiante e os seus engenhos calam-se um a um — um exército reduzido apenas a máquinas não dispara coisa nenhuma.

- Contam-se até **10 máquinas com tripulação** por hexágono por turno, pelo que o teto é de **2,500 pontos de muralha por turno** por mais que traga — e atingi-lo exige **50 soldados de pé** ao lado das 10 máquinas. Uma décima primeira máquina nada acrescenta.

- **Uma vez por hexágono por turno, ponto final.** Dois sitiantes distintos, cada um com máquinas, derrubam a muralha uma só vez, não duas.

- Sob a **postura de Cerco** (Siege), as máquinas de todos os exércitos de um grupo LINK (§5.11) juntam-se numa única salva — é isso que torna os grupos de cerco ligados dignos de formação.

- **Quando o cerco amadurece num assalto**, as máquinas de toda a coligação atacante juntam-se e **a salva cai antes de as muralhas serem medidas**: bombardeia e assalta no mesmo turno, de modo que esse assalto é travado contra a muralha que acabaste *de* derrubar. Este é o assalto em que um cerco termina — o exército já cumpriu a prova de força de cerco, por isso já ganhou direito às suas máquinas. Um assalto **improvisado** (uma marcha que entra num hexágono fortificado), uma reivindicação de origem e um desembarque em praia não trazem salva nenhuma: as máquinas estão com o exército, mas ninguém as monta para um combate que não foi planeado.

- **Um assalto repelido deixa o dano de pé.** Perdes o assalto; a muralha continua partida. Volta no turno seguinte contra um lugar mais fraco.

- O dano tem piso em **0** — uma muralha não pode ficar negativa, e a 0 o povoado fica **rompido** (breached) (fortaleza ×1.00, penalização do atacante ×1.00) até alguém o reparar (§2.11.8).

As máquinas são quase inúteis num combate — 10 WP, ataque 1 — pelo que uma coluna de cerco precisa de tropas a sério à sua volta, cinco soldados por máquina. São construídas, não recrutadas (§2.12.1): em qualquer lugar em terra, **sem retirar população**, pelo que um sitiante pode erguer a sua coluna *no próprio acampamento de cerco* — e as máquinas construídas neste turno já bombardeiam no tique de cerco estacionário ou no assalto deste turno, uma vez que são construídas na Pré-Fase 2b.

> ***▶ Exemplo — quanto tempo para abrir brecha?** Uma cidadela Anã **FDW10** (muralha 18,000) contra a coluna máxima de 10 máquinas demora 18,000 ÷ 2,500 = **8 turnos** de bombardeamento. Contra uma **FI12** Imperial (muralha 1,500), a mesma coluna rompe-a **num único turno**, com folga. Esta é toda a razão por que a curva das fortalezas tem teto em 15,000: abaixo dele, as máquinas respondem rapidamente às muralhas; no escalão máximo são uma verdadeira campanha, e a fome (5–6 turnos) é muitas vezes o caminho mais rápido.*

**5.9 Combate Naval (Naval Combat)**

Uma vitória naval toma navios e afasta o inimigo — nunca o porto. Os portos mudam de mãos apenas por assalto terrestre ou desembarque anfíbio.

**5.9.1 Poder da Frota (Fleet Power)**

fleetWP = sum of (ship.xp_wp × ship.count) across all ship stacks

**5.9.2 Fórmula de Lançamento (Roll Formula)**

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (±10 %)

portMod = 1.25 PER FLEET, attacker or defender, whose kingdom owns the port or is a mutual ally, liege or vassal of its owner — else 1.0.

O bónus só é obtido por uma frota que \*\*começou o turno nesse porto\*\* — atacante ou defensor, sem distinção. Os cascos que construiu ou recebeu neste turno seguem com o ×1.25 pleno; uma frota que entrou a navegar neste turno, ou que foi criada neste turno, combate a ×1.00.

Uma frota que esteja num porto inimigo ou neutro — um bloqueador ou um intruso — não obtém nada; uma frota que navegue para o seu próprio porto ou o de um aliado para expulsar um intruso mantém-no.

Os lados mistos somam por frota, pelo que o fator do lado no registo pode situar-se entre 1.0 e 1.25.

cargoMod = 0.85 if fleet is transporting an army, else 1.0

cmdMult = 1 + fleetCommander.military / 1000

raceMod = 1.05 if the fleet's kingdom is Aesir; ×1.10 if it is a Pirate kingdom (§4.3.1); else 1.0 (either side)

attRoll = attWP × status × portMod × initiative × attCmdMult × attCargoMod × attRaceMod × variance

defRoll = defWP × status × portMod × defCmdMult × defCargoMod × defRaceMod × variance

huntWP(side) = Σ per fleet: fleetWP × status × cmdMult × cargoMod × raceMod × portMod (no initiative, no variance)

Pirate Hunt attacks iff huntWP(hunter side) \> huntWP(target kingdom side) (§2.14.9)

**5.9.3 Baixas (Casualties)**

O mesmo limiar de resultado (rácio \> 1.2). Ambos os lados usam a fórmula de perdas idêntica:

**O atacante vence (Attacker wins):** attLoss = 0.10/ratio, defLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) até 5:1, depois 0.60 + 0.40 × (ratio − 5) / 5 — uma perda total a 10:1 **Empate (Draw):** ambos 0.06 + rand×0.06 (6–12%), o mesmo valor para ambos **O defensor vence (Defender wins):** defLoss = 0.10/ratio, attLoss como o defLoss de atacante-vence acima

**O mar usa a curva da batalha de campo até 5:1** (§5.5.3) — a curva logarítmica, o piso de dano e o seu teto de **60%** — **e depois uma rampa mais curta de probabilidades extremas**: a partir de 5:1 a perda sobe em linha reta até uma **perda total a 10:1** (6:1 → 68% · 7:1 → 76% · 8:1 → 84% · 9:1 → 92% · **10:1 e além → nenhum casco sobrevive**). A dissolução da armadura segue o mesmo calendário de 5:1 → 10:1: até 5:1 o custo de construção de um casco protege-o, para lá de 5:1 essa proteção é retirada ao ritmo da perda crescente. Um esquadrão de seis cascos dos navios de guerra mais pesados (Galés Imperiais) perde 2 a 5:1, 3 a 7:1, 5 a 9:1 e todos os seis a 10:1. Até 5:1 uma frota derrotada de vários cascos regressa a casa como um remanescente combativo (um casco isolado paga sempre o seu mínimo de um); para lá disso, só as probabilidades podem afundá-la.

**Uma frota é aniquilada (annihilated) pelas probabilidades a 10:1.** Abaixo de 10:1 a perda corre pela distribuição da armadura, e uma frota derrotada é destruída de vez quando o arredondamento lhe leva os últimos cascos — um esquadrão de dois ou três cascos baratos pode afundar-se por inteiro a partir de cerca de 8:1, um casco isolado paga sempre o seu mínimo de um — ou quando **não tem para onde se retirar** (nenhuma água livre ao alcance, ou encurralada num porto de que não pode sair), a versão marítima da regra terrestre de que só um exército cercado é destruído. **A 10:1 ou pior a rampa atinge a perda total e a frota afunda-se, tivesse ou não para onde fugir**. O estado da frota conta para o rácio, pelo que tripulações desgastadas chegam a 10:1 muito antes de o número de cascos o fazer.

**Mas o perdedor paga sempre pelo menos um casco — por frota.** Se a distribuição da armadura arredondar a zero a perda de todas as pilhas, a pilha mais próxima de perder cede, ainda assim, um navio.

Os vencedores navais sangram exatamente como os vencedores em campo: a perda base do vencedor é 0.10/ratio (contra 0.15/ratio nas muralhas). Não há **nenhum mínimo fixo** — com rácios de vitória elevados, a perda do vencedor tende simplesmente para zero.

> *Os navios que morrem são decididos pelo que custam, não pela sua DEF. A proteção de cada casco é o seu*
>
> *preço em ouro equivalente — ouro ao valor facial, ferro a ×12, madeira a ×5 — pelo que um navio de guerra caro*
>
> *perde uma fração menor do seu número do que um barato na mesma batalha. A comida não compra proteção:*
>
> *as rações não são armadura. Os cascos veteranos contam como proporcionalmente mais caros e por isso sobrevivem melhor.*
>
> *Um casco é medido contra uma escala fixa, não contra o resto da sua própria frota — um esquadrão de*
>
> *um só tipo de casco não é uniformemente protegido.*
>
> ***▶ Exemplo — luta em casa, nunca carregado.** Duas frotas de 500 WP chocam. Se o defensor estiver no seu próprio **porto** (×1.25, §5.9.2) lança a partir de 625 enquanto o atacante lança a partir de 500 — o atacante precisa agora de \> 750 efetivos para vencer um recontro que de outro modo seria equilibrado. Pior, uma frota que **transporta um exército** sofre ×0.85 (cargoMod): uma frota carregada de 500 WP lança apenas 425 e, se perder, o exército embarcado afoga-se com ela (§2.14.6). Escolta os teus transportes com frotas de guerra vazias e procura forçar as frotas inimigas a lutar contigo nos teus portos e não nos delas. O bónus segue o porto, não o papel — atacante ou defensor — mas apenas para uma frota que começou o turno nesse porto: uma enviada para expulsar um intruso combate a ×1.00, tal como o intruso (§5.9.2).*

**5.9.4 Destino do Exército Transportado (Transported Army Fate)**

Se a frota transportadora for afundada, o exército a bordo é destruído com ela — sem sobreviventes (§2.14.6).

**5.9.5 Derrota e Retirada (Defeat and Retreat)**

Uma frota derrotada que ainda tenha navios a flutuar recua para o **refúgio mais próximo a menos de 3 hexágonos**. Um refúgio que seja um **porto** atraca lá a frota — conta como estando em porto para incursões, embarque e regras do porto a partir desse momento. Numa luta de coligação, **cada frota derrotada retira-se individualmente** — cada uma encontra o seu próprio refúgio, exatamente como os exércitos terrestres (§5.5.6). **Num empate os atacantes retiram-se da mesma forma e os defensores mantêm o hexágono** — um atacante empatado que não encontre refúgio afunda-se exatamente como se tivesse sido batido, e um empate não rende presas a ninguém. **Quem combate do lado defensor é automático**, pela regra terrestre (§5.11): toda a frota no hexágono em guerra com o atacante junta-se à defesa, a menos que esteja em guerra com um defensor, e as frotas ligadas sob a nau capitânia defensora juntam-se sempre, contando como defensoras desde o início; uma frota em paz com o atacante é espectadora e não sofre baixas nem toma parte. **Um cartão por batalha.** O teu relatório mostra um **único** cartão de batalha por recontro naval, intitulado com todas as tuas frotas que combateram — *"Naval victory (Fleets I + II)"* — e lista os navios de cada frota abaixo dos totais dos lados (as perdas são o total do reino nesse combate). Se uma das tuas frotas se afundou enquanto outra recuou, o cartão diz qual. Duas frotas tuas no mesmo combate são um esquadrão, não uma coligação; a palavra *coalition* só aparece quando a frota de um **aliado** esteve ao lado da tua.

A busca decorre como a de um exército batido. Primeiro vem o hexágono de onde a frota **veio** neste salto (apenas a frota principal — os cobeligerantes partem do seu próprio hexágono). Caso contrário, a frota toma o hexágono utilizável **mais próximo** até **3 hexágonos** de distância, movendo-se apenas por **mar aberto que não contenha nenhuma frota em guerra contigo** — um anel de frotas inimigas ainda a prende, pelo que um bloqueio ou um porto encurralado mantém os dentes, ao passo que as tuas próprias pilhas cheias não. Entre hexágonos à mesma distância, prefere:

1\. um **porto teu**;

2\. um **porto aliado** (aliança mútua, o teu suserano ou um dos teus vassalos);

3\. **mar aberto**;

4\. um **porto neutro**.

Um candidato só é utilizável se **nenhuma frota em guerra contigo** estiver lá, **não pertencer a um reino em guerra contigo** (um porto inimigo — a regra que mantém um exército batido fora de solo inimigo) **e a pilha amiga tiver lugar** — o limite de 3 frotas aplica-se também às retiradas, pelo que uma debandada nunca pode sobrecarregar um hexágono. Os camaradas, e as frotas meramente **neutras**, são refúgio e não parede: uma frota batida pode juntar-se a um hexágono partilhado enquanto houver um lugar livre (§2.14.2).

Se **nenhum candidato se qualificar, a frota afunda-se onde combateu**: todos os cascos se perdem, um exército embarcado **vai ao fundo com ela** — sem sobreviventes (§5.9.4) — e o seu comandante faz o teste de morte com 100% de perdas; o **comandante da própria frota** já lançou os dados sobre as perdas de cascos da batalha como qualquer comandante de exército. Os cascos perdidos desta forma não são presas: só os cascos perdidos no próprio combate são sorteados para captura (§2.13.12).

Uma fuga forçada continua a ser navegação: a retirada **cobra estado à frota** pelo hexágono em que entra como qualquer movimento (a linha *"Retreat, or flee a fallen port"* da tabela de fadiga, §5.10.6). Uma frota cujo **porto cai** num assalto ou num cerco não usa esta busca: corre para o hexágono de águas abertas livre mais próximo que consiga alcançar pela água — nunca um porto, amigo ou não — e é **destruída nas suas amarras** se nenhum estiver ao alcance (§2.7).

**5.10 Estado do Exército (Prontidão) (Army Status (Readiness))**

Todo o exército tem um valor de **ESTADO** (STATUS) de **10% a 100%** — a sua prontidão para marchar e combater. Um exército descansado está a 100%. A Página do Jogador (Player Page) mostra-o em cada cartão de exército (STATUS: 77%) e antevê a perda projetada de qualquer rota planeada (Arrive at ~N%).

O estado é o relógio de exaustão do jogo. Nada na lista de um exército muda quando se cansa — os mesmos regimentos, os mesmos Pontos de Guerra (WP) no papel — mas uma coluna esgotada chega mais devagar, bate mais fraco e move-se em último. Cada ponto é gasto *a fazer* e só se compra de volta *a descansar*, pelo que o estado é a etiqueta de preço do ritmo: cada hexágono que marchas, cada luta que escolhes e cada turno em que manténs um anel de cerco fechado é pago em prontidão.

**5.10.1 O Que o Estado Faz (What Status Does)**

O estado tem exatamente dois efeitos mecânicos, e ambos pesam muito:

- **Multiplica o poder de batalha.** Em cada batalha — de campo, surtida, assalto, anfíbia e a disputa de milícia de uma tomada — os Pontos de Guerra de cada exército são multiplicados pelo seu estado antes do lançamento. Um exército de 10,000 WP a 50% luta como um de 5,000 WP. Os rankings e as estimativas dos espiões usam WP **brutos**; as batalhas e o limiar de capacidade de cerco (§5.8.1) usam WP **ao estado**.

- **Compra iniciativa.** O movimento, os cercos/assaltos e os movimentos de frotas resolvem-se todos em **ordem de estado, do mais alto para o mais baixo**, valores exatos (§2.13.1): um exército a 99% marcha antes de um a 98%.

Duas coisas que *não* são efeitos: o estado nunca altera o que custa alimentar um exército, e **nunca é visível aos teus inimigos** — nem no mapa, nem nos relatórios de espiões. Adivinhas a exaustão deles exatamente como eles adivinham a tua.

**O teu relatório diz-te porquê.** Todos os turnos o teu relatório traz um **Relatório de Prontidão** (Readiness Report) — apenas no teu relatório, nunca mostrando unidades de outro reino — em dois cartões: os **exércitos** fecham a Fase 5 e as **frotas** fecham a Fase 6, cada um onde terminou o seu próprio combate. Juntos listam cada exército e frota cujo estado mudou neste turno, discriminando cada causa pela ordem em que aconteceu, ao lado do multiplicador de poder de batalha resultante. As causas, tal como o cartão as redige:

- **Movimento:** *marched N hexes (terrain)*, *fell back N hexes (terrain)* após uma batalha perdida ou uma retirada, *pulled back inside the walls* para os sobreviventes de uma surtida perdida ou empatada, *sailed N hexes (coastal / high sea)*.

- **Embarque e desembarque:** *embarked*, *landed*, *beach pickup* (o custo da frota por levantar tropas de uma praia).

- **Combate:** *battle won / battle lost / battle drawn at (col,row)*. Uma tomada que a populaça repele — empate ou derrota — lê-se *battle lost*, em conformidade com o cartão *Army Repelled*.

- **Serviço permanente:** *siege upkeep*, *blockade*, *hunting* (uma frota pirata em Caça), *raiding* (uma frota que fez incursões neste turno).

- **Recuperação:** *rested* (um exército, ou uma frota atracada em qualquer porto cujo dono não esteja em guerra contigo — incluindo o porto de um neutro), *rode at anchor* (uma frota a descansar longe de qualquer porto). Uma frota atracada num porto inimigo não recupera nada.

- **Reorganização:** *levelled to the group's weakest* (os membros de um grupo LINK são nivelados pelo mais fraco — ao juntar-se e de novo no fim de qualquer turno em que os seus estados se afastem), *reinforced by fresh recruits*, *reinforced by new hulls*, *absorbed transferred troops*.

As linhas de batalha nomeiam o hexágono onde o combate se deu — *battle lost at (20,28) −22* — e cada batalha é a sua própria linha: duas batalhas em dois hexágonos são duas linhas, e também o são duas batalhas no **mesmo** hexágono — um assalto a 92% seguido de um contra-ataque a 84% lê-se *battle won at (24,34) −8 · battle won at (24,34) −3*, nunca um único −11 somado.

**O piso também é reportado.** O estado nunca desce abaixo de 10%, mas uma unidade no piso continua a pagar pelo que faz — simplesmente não tem mais nada a perder. O cartão di-lo em vez de se calar: uma frota que navega três hexágonos a 10% lê-se *Fleet V 10 → 10 · sailed 3 hexes (coastal) −0 (at the 10% floor)*, e uma marcha que bate no piso conta cada hexágono e nomeia-o — *Army II 12 → 10 · marched 2 hexes (plains) −2 (at the 10% floor)*.

Uma unidade cujo estado termina abaixo de metade (50%) recebe também uma sugestão de "ficar parada um turno para recuperar". Um turno calmo — nada pago, nada recuperado — não traz cartão nenhum.

**5.10.2 Todas as Ações que Alteram o Estado (Status)**

Todas as regras que alteram o estado (status) de um exército, num só lugar. Os custos são em **pontos** de estado (o estado é uma escala de 10–100, pelo que um ponto é um ponto percentual).

|                                                                                                    |                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ação**                                                                                           | **Alteração de estado**         | **Notas**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Marchar para um hexágono**                                                                       | **−5 a −18** por hexágono       | Por raça × terreno — ver §5.10.3. Cobrado por hexágono *em que se entra*, pelo que recuar sobre um hexágono paga-o duas vezes. Infantaria e montados pagam o mesmo valor.                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Retirada ou expulsão**                                                                           | **−(terreno) × hexágonos fugidos** | Uma marcha forçada continua a ser uma marcha. Cobrada ao terreno do hexágono de destino, multiplicada pela distância fugida. O Relatório de Prontidão (Readiness Report) diz *"fell back N hex"* — ou *"pulled back inside the walls"* para os sobreviventes de uma Surtida (Sally) perdida ou empatada. Um exército derrotado fora das suas próprias muralhas entra sem se mover, pelo que não tem essa linha.                                                                                                                                                              |
| **Embarcar** (subir a bordo de uma frota)                                                          | **−5**                          | Um custo fixo, pago uma só vez ao embarcar — igual quer se embarque num porto quer se seja recolhido numa praia (§2.14.6). O estado fica então congelado durante a viagem.                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Desembarcar** (*qualquer* desembarque)                                                           | **−20**                         | Um custo fixo que **substitui** o custo do terreno — todas as praias custam o mesmo (uma costa de **montanha** não permite desembarque algum — é falésia, não margem). Um desembarque **disputado** paga o seu custo de batalha por cima (§5.10.4); um desembarque **bloqueado** por uma pilha completa não paga nada; um desembarque que combate e é **repelido** (ou empata) reembarca sem pagar o −20 mas **paga** o custo próprio da batalha (§5.10.4) — em muralhas estrangeiras não reembarca: os sobreviventes entrincheiram-se no exterior e pagam também o −20 (§5.7.2); o combate foi real, mesmo que a praia não tenha sido tomada. |
| **A bordo de uma frota (no mar)**                                                                  | **congelado**                   | Um exército transportado nem se cansa nem descansa. O seu estado é exatamente o que era quando embarcou.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Vencer uma batalha**                                                                             | **−3 a −15**                    | Escalado pela dureza do combate — ver §5.10.4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Perder uma batalha**                                                                             | **−15 a −30**                   | Também escalado pelo rácio; um perdedor esmagado paga os −30 completos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Empatar uma batalha**                                                                            | **−15** para ambos os lados     | Um impasse é o resultado mais caro por ponto de ganho.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Disputa de apreensão pela milícia**                                              | igual a uma batalha             | A população não é um exército: **a milícia não paga nada**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Manter a postura de Cerco (Siege)**                                                              | **−3 por turno**                | Pago apenas enquanto o anel de cerco está realmente a ser apertado (um exército demasiado pequeno para investir o povoado não paga nada — nunca chega a tanto). Cada membro de um grupo ligado em serviço de cerco paga-o.                                                                                                                                                                                                                                                                                                                                                     |
| \**Manter a postura de Cerco* ou de Assalto *(stance)*\*                                           | **sem recuperação**             | Nenhuma das duas descansa alguma vez: um sitiante ou um assaltante só recupera depois de cessar a postura. **O Assalto não paga os −3** — custa a batalha, não a sangria. Um assalto que **toma** as muralhas paga também a entrada no terreno do hexágono, como uma marcha — o exército moveu-se para dentro.                                                                                                                                                                                                                                                                |
| **Combater neste turno** (qualquer batalha, qualquer fase, atacante ou defensor — incluindo um desembarque no teu hexágono) | sem recuperação neste turno | O descanso é concedido após a última batalha do turno, apenas a uma unidade que ninguém tocou. O combate em si cobra o seu próprio custo como habitual.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Acampar num hexágono fortificado estrangeiro** (qualquer postura)                                | **sem recuperação**             | Estende o princípio "um sitiante só recupera depois de cessar a postura" a quem quer que esteja acampado em muralhas estrangeiras — um exército em Marcha de Cerco ou um assaltante repelido entrincheirado às portas não descansa nada enquanto mantiver esse terreno. Um exército no seu próprio hexágono fortificado, ou num aliado, continua a descansar normalmente.                                                                                                                                                                                                    |
| **Descansar** (sem ordem de movimento)                                                             | **+33**                         | Limitado a 100. Ver §5.10.5 para o que desqualifica um exército.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Recrutar novas unidades**                                                                        | **aproxima-se de 100**          | Ponderado pelo número de efetivos — ver §5.10.5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Receber uma transferência de unidades**                                                          | **o destino mistura-se**        | As tropas que chegam arrastam o estado do exército recetor para o seu (ponderado pelos efetivos); o estado do exército de *origem* não se altera (§5.10.5).                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Reunir um novo exército**                                                                        | **começa em 100**               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Pertencer a um grupo LINK**                                                                      | **nivela pelo mínimo do grupo** | Aplicado todos os turnos, *depois* do descanso (§5.11).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Piso**                                                                                           | **nunca abaixo de 10**          | Mesmo um exército exausto combate com um décimo da força — nunca zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**▶ Exemplo — o que custa um desembarque, situação a situação.** Os −20 são fixos e pagos apenas quando o exército efetivamente desembarca; uma batalha travada na praia acrescenta o seu custo de §5.10.4 por cima; um desembarque que não chega a acontecer não paga nada.

|                                                                                                                 |                                                                                              |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Situação de desembarque (§2.14.6)**                                                                           | **Estado pago pelo exército**                                                                |
| Terreno próprio/aliado, livre — ou junto de amigos (co-localização)                                             | **−20**                                                                                      |
| Terreno próprio/aliado, hexágono já **cheio** (3 exércitos)                                                     | **0** — fica a bordo                                                                         |
| Terreno próprio/aliado, **exército inimigo** presente — combate na praia vencido                                | **−20** + custo de batalha do vencedor (max(3, min(15, 15 − 3(r−1))))                       |
| — combate na praia perdido ou empatado (reembarca)                                                              | **0** de custo de desembarque + custo de batalha do perdedor / do empate (§5.10.4)           |
| Hexágono inimigo com **muralhas** — assalto a partir da praia vencido                                           | **−20** + custo de batalha do vencedor (o custo fixo de desembarque substitui o custo do terreno mesmo aqui) |
| — combate na praia às portas perdido ou empatado, ou assalto repelido: o sobrevivente mantém uma **cabeça de praia** fora das muralhas | **−20** + custo de batalha do perdedor ou do empate (§5.10.4)                                |
| Terreno aberto inimigo/sem dono, exército ou milícia — vencido                                                  | **−20** + custo de batalha do vencedor                                                       |
| — repelido (reembarca)                                                                                          | **0** de custo de desembarque + custo de batalha do perdedor (§5.10.4)                       |
| Desembarque recusado porque o exército **embarcou neste turno**                                                 | **0**                                                                                        |
| Embarque (porto ou praia)                                                                                       | **−5** uma vez; depois **congelado** a bordo                                                 |
| Frota a fazer uma **recolha na praia**                                                                          | frota **−15**, e o seu movimento fica gasto                                                  |

**5.10.3 Custo de Marcha por Raça e Terreno (Marching Cost by Race and Terrain)**

O custo de entrar num hexágono, segundo a raça do exército em marcha e o terreno de destino. A pátria de cada raça é a sua pechincha, e o seu oposto é a sua ruína: um Anão atravessa uma montanha por 10 quando todos os outros pagam 18, mas arrasta-se pela floresta a 12; um Orc vadeia um pântano a 9 que custa 15 a todos os outros; os Aesir compram colinas e floresta a baixo preço e pagam 16 por um deserto para onde ninguém os mandou.

|             |              |           |         |               |         |           |           |
|-------------|--------------|-----------|---------|---------------|---------|-----------|-----------|
| **Terreno** | **Imperial** | **Nómada** | **Elfo** | **Bárbaro** | **Orc** | **Anão** | **Aesir** |
| Planície    | 5            | 5         | 5       | 5             | 5       | 6         | 5         |
| Colinas     | 10           | 9         | 10      | 8             | 10      | 8         | 9         |
| Floresta    | 8            | 8         | 6       | 8             | 10      | 12        | 7         |
| Deserto     | 14           | 10        | 14      | 14            | 14      | 14        | 16        |
| Pântano     | 15           | 15        | 15      | 15            | 9       | 15        | 15        |
| Montanha    | 18           | 18        | 18      | 16            | 18      | 10        | 17        |

Montados e infantaria pagam o mesmo **por hexágono** — mas os exércitos montados têm 90 MP contra os 60 da infantaria, pelo que cobrem mais hexágonos por turno e, portanto, cansam-se *mais depressa por turno*. A velocidade compra-se com prontidão, não é dada de graça.

Esta tabela custeia **apenas a marcha**. Um **desembarque** ignora por completo o terreno e paga os −20 fixos de §5.10.2 — um exército anfíbio paga pelos barcos e pela rebentação, não pelo terreno onde pisa.

**5.10.4 Custo da Batalha por Rácio (Battle Cost by Ratio)**

O custo de uma batalha é determinado pela desigualdade do combate. O **rácio** é a jogada de combate do vencedor ÷ a jogada do perdedor (o mesmo número que define os escalões de despojos, §2.13.11):

- O **vencedor** paga 15 − 3 × (rácio − 1), limitado a **3–15**.

- O **perdedor** paga **30 − o custo do vencedor** — uma luta dura exaure ambos os lados de forma mais ou menos igual. Um perdedor **esmagado** (rácio ≥ 5) paga os **30** completos, independentemente.

- Os **empates** custam a ambos os lados **15** fixos.

|                            |                 |                |
|----------------------------|-----------------|----------------|
| **Rácio (vencedor ÷ perdedor)** | **O vencedor paga** | **O perdedor paga** |
| ~1.0 — vitória por um fio  | −15             | −15            |
| 2.0 — vitória clara        | −12             | −18            |
| 3.0 — decisiva             | −9              | −21            |
| 4.0 — unilateral           | −6              | −24            |
| 4.9 — quase debandada      | −3              | −27            |
| **≥ 5.0 — esmagado**       | **−3**          | **−30**        |
| Empate (qualquer rácio)    | −15             | −15            |

A forma é deliberada: **uma vitória fácil é quase gratuita, uma luta renhida custa ao vencedor quase tanto como ao perdedor.** Vencer a custo contra um adversário a sério deixa-te com cerca de metade da prontidão e em último lugar na iniciativa do turno seguinte — que é muitas vezes o momento em que o aliado dele marcha.

**5.10.5 Recuperar e Reforçar (Recovering and Reinforcing)**

**Descansar.** Um exército que **não submete ordem de movimento** "recupera em vez de se mover": **+33 pontos** (limitado a 100) no **fim do combate do turno** (após a Fase 6), e **apenas se ninguém o atacou** — um exército parado atacado nesse turno defende com o seu estado real, sem descanso, e não descansa nada. As desqualificações estão listadas na tabela de §5.10.2: uma ordem de movimento (própria ou do seu líder de ligação — um desembarque, embarque ou retirada contam), postura de Cerco ou de Assalto, qualquer combate neste turno, ou estar num hexágono fortificado estrangeiro, qualquer que seja a postura. Um exército **embarcado** não descansa nada — o seu estado fica congelado até desembarcar: a *frota transportadora* recupera ao ancorar, as tropas no seu porão não.

Em termos gerais: **dois turnos de marcha em terreno fácil por cada turno de descanso.** Em colinas ou montanhas o rácio inverte-se, e uma travessia de montanha pode custar mais do que um turno completo de descanso consegue restaurar.

**Sangue fresco restaura o ânimo.** O reforço revigora genuinamente um exército, porque o estado se mistura por peso em vez de ser carregado pelos veteranos:

- Os **novos exércitos** são reunidos em **100**.

- Os **recrutas** chegam a **100** e misturam-se **ponderados pelo número de efetivos** — 50 tropas frescas a juntarem-se a 50 exaustas a 40% resultam em (40×50 + 100×50) ÷ 100 = **70%**. A mistura ocorre na Pré-Fase 2b — antes dos cercos, surtidas e assaltos em curso da Pré-Fase 3 e antes do descanso da Fase 5 — pelo que uma guarnição reforçada neste turno é assaltada, ou faz surtidas, com o valor misturado.

- As **transferências de unidades** levam o estado do **exército de origem** para o destino e misturam-se da mesma forma; o exército de origem mantém o seu.

Este é o estado de prontidão mais barato do jogo: um pequeno núcleo veterano reforçado com recrutas na sede de recrutamento regressa à frente muito mais fresco do que o mesmo exército a descansar no local.

**5.10.6 Fadiga da Frota no Mar (Fleet Fatigue at Sea)**

As frotas seguem o mesmo quadro, com o mar a fornecer o terreno. Navegar custa estado por cada hexágono em que **se entra**, classificado pelo hexágono em que entras:

|                                                 |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ação da frota**                               | **Alteração de estado**       | **Notas**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Navegar um hexágono costeiro**                | **−3** (Aesir **−2**)         | O hexágono é um porto, ou toca pelo menos um hexágono de terra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Navegar um hexágono de alto mar**             | **−6** (Aesir **−4**)         | Água aberta de todos os lados — o limite do mapa conta como oceano.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Recolha na praia** (carregar um exército em águas abertas) | **−15**          | Pago uma só vez, quando a frota leva um exército a bordo via embark_army com beach:true (§2.14.6) — além dos −5 de custo de embarque do próprio exército. Consome o movimento da frota no turno: sem navegar até ao turno seguinte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Batalha naval**                               | igual à terrestre (§5.10.4)   | O poder de cada frota é multiplicado pelo seu próprio estado; o bónus de batalha de ×1.05 dos Aesir acumula por cima.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Retirada, ou fugir de um porto caído**        | **−(classe do hexágono em que entra)** | O movimento forçado cobra como a retirada de um exército.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Descansar atracado num porto**                | **+33**                       | Porto próprio, aliado ou neutro, e apenas sem ordem de movimento. Uma frota que **travou um choque de porto** neste turno não descansa (o gémeo naval da regra dos exércitos acima) — uma frota inimiga que partilha o teu porto é combatida *antes* de as tripulações largarem o serviço.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Ancorada no mar**                             | **+16**                       | Uma frota que simplesmente fica parada em qualquer lugar que não seja uma doca amiga fica ao ancora e recupera **metade de uma licença em terra**, incluindo em pleno oceano. Concedido no **fim do combate do turno**, apenas se a frota nem navegou nem combateu — uma frota atacada ao ancora combate com o seu estado real e não descansa nada nesse turno. Desqualificada por tudo o que gasta o turno da frota, o que **não** é o mesmo que emitir uma ordem: um movimento que **efetivamente navegou** (o seu ou o da sua nau capitânia — uma ordem que o motor recusa, numa pilha cheia por exemplo, deixa a frota onde estava e ela descansa como qualquer frota inativa, paga no fim da fase), um choque de porto travado neste turno, postura de bloqueio, **uma retirada forçada** (ser expulso de um hexágono não é estar parado — paga o custo de navegação e não ganha descanso por isso), ou **uma recolha na praia** (§2.14.6 — a recolha consome o turno). |
| \**Atracada num porto* inimigo*\*               | **0**                         | Um porto inimigo vazio é um destino legal (§2.14.2) — mas as tripulações não têm licença em terra num porto hostil, e **também não há descanso ao ancora**: acampar num porto inimigo é deliberadamente pior do que estar em águas abertas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Postura de Bloqueio (Blockade)**              | **−2 por turno**              | E sem recuperação enquanto estiver em posição.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Pilhagem (Raid)**                             | **−3 num turno em que pilha** | Pago **uma vez** em qualquer turno em que a frota pilha um porto (§2.14.3) — seja o que for que leve, 0g incluído, e por muitos portos que a viagem pilhe. Cada frota de um grupo ligado em pilhagem paga-o. Uma pilhagem recusada não custa nada, nem uma pilhagem **à vela** derrotada ou empatada no porto: nunca chega a pilhar. Uma pilhagem **ao ancora** pilha antes da sua luta no porto, pelo que paga sempre. A luta cobra o seu próprio custo de batalha e a navegação é cobrada por cima; o porto pilhado não dá descanso (*Atracada num porto inimigo*, acima).                                                                                                                                                                                                                                                                                                    |
| **Postura de Caça (Hunt)** (apenas piratas)     | **−2 por turno**              | E sem recuperação enquanto caça (§2.14.9).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Construir navios**                            | **aproxima-se de 100**        | Os novos cascos são lançados a 100 e misturam-se **por número de navios**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Transferência de navios**                     | **o destino mistura-se**      | O estado da frota recetora mistura-se com o dos navios que chegam (ponderado pelo número de navios); a frota de origem não se altera.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Navios-presa capturados**                     | **adotam o estado do captor** | As presas juntam-se à frota que as tomou; não alteram nada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Piso**                                        | **nunca abaixo de 10**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

A caixa *Planned Route* da Página do Jogador (Player Page) pré-visualiza estes custos salto a salto. Um hexágono que não consegues ver (nevoeiro) é custeado como **águas abertas** — o pior caso — e rotulado *assumed open water*. O motor classifica o hexágono real quando a frota navega, pelo que um hexágono desconhecido que se revele costeiro custa menos do que o previsto, nunca mais.

**Cada cartão de batalha naval nomeia ambos os lados.** O título traz o(s) número(s) da(s) frota(s) inimiga(s) — *"Vanaheim (F III) driven from the sea"* — e quando mais de uma frota combateu do teu lado o cartão termina com uma lista **Your side:** que enumera cada uma delas, aliadas incluídas, com os seus cascos sobreviventes: partilhaste uma linha de batalha, vês os navios. O cartão de uma frota isolada não mostra lista — não há nada a partilhar.

Um exército transportado nem altera o ritmo da frota nem descansa a bordo — o seu estado fica congelado até desembarcar (§5.10.2).

> ***⚠ O que isto significa —** As ofensivas têm um tempo: cerca de dois turnos de marcha por um de descanso em terreno fácil, pior em colinas e montanhas. Um atacante que faça uma marcha forçada por um desfiladeiro de montanha chega com dois terços da força ou menos contra um defensor descansado que pode ainda deter um bónus de batalha de terreno natal — o terreno defendido está agora duas vezes defendido. Vigia a linha Arrive at ~N% no planeador de rotas, e descansa os teus exércitos antes da fronteira, não nela.*

**5.11 Co-localização de Exércitos e Grupos LINK (Army Co-location & LINK Groups)**

**Recrutar e ligar funciona num só turno.** As ligações são formadas *depois* do recrutamento (muster) do turno, pelo que um exército (army) levantado neste turno pode ser ligado — e marchar em grupo — no mesmo ficheiro de ordens. **Toda a ligação recusada é registada em carta com o respetivo motivo** ("ainda não existe", "não está no mesmo hexágono", "já ligado", "a bordo de uma frota", "grupo cheio", "não é um aliado mútuo"); uma ligação que não apareça no teu relatório foi recusada, nunca perdida. Uma nota sobre a ordem: um exército que embarca e é ligado no mesmo turno embarca primeiro e a ligação é recusada (os exércitos ligados não podem embarcar — §2.14.6).

**Amigos podem partilhar um hexágono.** Até **3 exércitos** podem estar num só hexágono (hex), em qualquer mistura amigável: os teus próprios exércitos e os de **aliados mútuos** (ou vassalo/suserano). A co-localização é automática em **terreno teu ou aliado**. Em terreno inimigo ou neutro, um amigo não protege o hexágono de ti (§2.13.3): se todo o teu grupo couber, entras como se ele não estivesse lá e ele fica a teu lado como espetador. Inimigos num hexágono significam sempre batalha, nunca um acampamento duradouro: os exércitos que entram em guerra enquanto acampam juntos combatem no início da Fase 5 seguinte (o varrimento de acampamento — camp sweep, §2.13). O único acampamento duradouro de inimigos é dentro de uma cidade cercada, onde o derrotado não pode sair (§2.13.7). O limite de 3 vale em **todos** os caminhos para um hexágono *aberto*: marchar, desembarcar, retirar, até recrutar um novo exército — um hexágono cheio rejeita-os a todos. **Todos os exércitos no hexágono contam para o limite, seja qual for a sua bandeira**: um exército em paz contigo ocupa um lugar tal como um amigo, pelo que um grupo que não cabe inteiro é recusado inteiro com a habitual carta de *hexágono cheio*, em vez de entrar e deixar um membro para trás; os avisos da Página do Jogador também contam todos os exércitos que ela consegue ver ali. **Um exército que marcha para um hexágono cuja zona tem um exército em guerra com ele combate esse exército — os inimigos não ocupam lugar perante um ataque**: a marcha nunca é recusada como *hexágono cheio* por causa deles e o aviso de movimento da página fica em silêncio; recrutamentos e divisões continuam a contar todos os exércitos. Diante das muralhas de uma cidade estrangeira, **um exército em guerra contigo acampado no exterior é combatido às portas, nunca contado como espaço**, seja quem for que lá esteja acampado. Um grupo ligado **que avança atrás do seu líder depois de uma batalha** também lhe obedece: um membro que encheria demasiado o hexágono (um exército aliado pode já lá estar acampado) fica onde estava e deixa o grupo. Se o grupo for travado diante de um hexágono sem espaço, um membro de outro reino também recebe carta: *"O teu exército está ligado sob X, e o grupo parou: …"*. **Num hexágono com uma construção (construction) com muralhas (walls), o limite é por zona**, não por hexágono: até **3 dentro das muralhas e 3 fora** (até 6 exércitos presentes no total), porque um acampamento de cerco e uma guarnição ocupam terreno diferente — ver §5.8.0. Um exército batido pode também retirar para um hexágono ocupado por amigos com espaço (§5.5.6). Uma deslocação ordenada para um hexágono atualmente cheio continua legal: se os ocupantes saírem primeiro (a ordem de iniciativa decide), entras; se não, a tua coluna pára à frente dele. Isto resolve-se **em direto, ronda a ronda, não por reserva** (§2.13.1): um lugar de acampamento — fora das muralhas ou em terreno aberto — vai para o movimento cujo salto chega primeiro e nunca é mantido livre para um movimento ainda em fila para uma ronda posterior.

**Exércitos co-localizados defendem-se em conjunto — automaticamente.** Quando um inimigo ataca o hexágono, todos os exércitos que estão na zona atacada do hexágono (nas muralhas, uma Guarnição (Garrison) defende apenas o assalto, §5.8.0) que estejam **em guerra com o atacante** — os do defensor, os dos seus aliados e os de completos estranhos por igual (como no mar) — juntam-se à defesa como uma só força, **exceto um exército em guerra com o defensor ou com outro exército que já defende, que se mantém à parte em vez de combater ao lado do seu próprio inimigo** (um membro do grupo LINK do defensor junta-se mesmo em paz com o atacante, que então lhe declara guerra, e conta como defensor desde o início — **incluindo o aliado, vassalo ou suserano do próprio atacante, cuja aliança se quebra** — §5.11; só o grupo do defensor **principal** é arrastado desta forma, e os membros ligados de um co-defensor só se juntam se estiverem eles próprios em guerra com o atacante): cada um contribui com os seus próprios pontos de guerra (war points), bónus de terreno, postura (stance) e comandante; as baixas recaem sobre cada participante em proporção ao seu tamanho; cada participante regista a sua própria carta de batalha, variação de opinião e vitória/derrota. Os despojos de uma vitória defensiva **repartem-se entre os reinos defensores em proporção à sua quota de pontos de guerra**. Um exército aliado **em paz** com o atacante e **fora do grupo de ligação do defensor** fica à parte em terreno aberto — ninguém é arrastado para uma guerra pela geografia (ninguém dentro de muralhas é espetador, §5.6); uma ligação é outra questão (acima). **Um reino nunca combate dos dois lados da mesma batalha**: se um dos teus exércitos **combate do lado atacante** — como membro do grupo de ligação do atacante, por exemplo — o teu exército que está na defesa fica à parte, não defende, e recebe a carta *"retido"*. O teu exército atacante continua a combater e os seus golpes são do teu reino: entras em guerra contra o defensor (a ligação é consentimento) — regras completas e um exemplo trabalhado em §5.11.1. Nas muralhas de um amigo, um membro deixa o grupo que se vira contra esse amigo ou os seus aliados ali (§5.11.1 regra 3). **Exércitos co-localizados também atacam em conjunto** — os teus exércitos na zona atacada, e um aliado já em guerra com todo o lado defensor, juntam-se ao ataque; nunca um exército cercado (§2.13.5).

**Uma batalha, uma carta — e todos os exércitos nomeados, os teus e os deles.** Quando dois (ou três) dos teus exércitos combatem a mesma batalha — ligados, ou defensores co-localizados que se juntam automaticamente — recebes **uma** carta de batalha, não uma por exército. As cartas terrestres seguem a mesma convenção das cartas de frota: o título traz o nome do teu exército — *"(Army II)"*, ou *"(Armies II + III)"* para um grupo — **e** o(s) número(s) do inimigo: *"Victory on forest at (14,22) against Vanaheim (A III)! (Armies II + III)"* — o hexágono está no título, pelo que exército e lugar se leem juntos. A linha de perdas é o total do grupo, a composição agrupa **todos** os exércitos do teu lado, e quando mais de um exército esteve do teu lado a carta acrescenta uma lista *"Your side:"* — cada exército, aliados incluídos, com as suas unidades sobreviventes. O contador de cada lado na carta de batalha nomeia os exércitos que se encontraram (§5.12), tal como a carta naval nomeia as frotas.

**LINK — marchar e combater como um só, por escolha.** Uma ordem permanente solda até 3 exércitos co-localizados num **grupo de ligação (link group)**:

- **Formação.** O **LÍDER DA LIGAÇÃO (LINK LEADER)** emite a ordem a partir da carta do seu exército, escolhendo exércitos co-localizados. Os teus próprios exércitos juntam-se **no mesmo turno**, sem necessidade de consentimento. Um exército **aliado** precisa da aceitação do seu dono: a proposta torna-se uma oferta pendente (registada em carta, mostrada na carta do exército do aliado) aceite num turno posterior — ou, se coordenarem e ambos submeterem no mesmo turno (proposta + LINK ACCEPT), o grupo forma-se logo. Uma oferta caduca (com carta) se os exércitos se separarem antes da aceitação. Num **hexágono fortificado o grupo tem de ficar junto**, e o teste é se ainda ficariam separados **depois de ligados**. Um membro adota a zona do seu líder, pelo que dois exércitos em lados opostos das muralhas podem ligar-se quando **ambos são amigos do dono do forte**: o grupo fica então do lado do líder (§5.8.0 Casos E e F). Uma ligação **para dentro** (líder no interior) é recusada enquanto um exército em guerra com o exército que se junta estiver acampado no exterior, ou quando o interior está cheio — é uma porta, tal como uma ordem de Guarnição. Qualquer outro cruzamento é recusado, tanto na proposta como na aceitação (*Link refused — … stand on opposite sides of the walls*). Uma ligação nas muralhas de um amigo sob um líder hostil a ele é também recusada (§5.11.1 regra 3). Se a diplomacia voltar a deslocar um membro para o outro lado das muralhas, este é libertado automaticamente do grupo (com carta). Um exército em Emboscada (Ambush) nunca é arrastado para o grupo de um aliado (*Ligações e Emboscada*, abaixo). **Um grupo formado cresce da mesma maneira** — a partir da carta do líder, qualquer exército no seu hexágono pode ser acrescentado até o grupo ter 3 (líder incluído; uma ligação já em fila neste turno conta); a carta de um exército não ligado que partilha o hexágono de um líder remete-te para a carta desse líder. As frotas são idênticas, a partir da carta da nau capitânia (§2.14.7).

- **Propostas mútuas não ligam.** O motor associa um ACCEPT a uma proposta específica: se ambos os jogadores se propuserem um ao outro em vez de um propor e o outro aceitar, são duas ofertas pendentes, e cada lado espera acreditando que está feito. Combinem de antemão quem lidera — o proponente é o líder.

- **Ligações e Emboscada**. **Um exército em Emboscada pode liderar uma ligação, mas a Emboscada cobre apenas os exércitos do seu próprio reino.** Um exército Elfo em floresta ou um exército Anão em montanha com Emboscada pode acrescentar os seus próprios exércitos ou propor uma ligação ao exército de um aliado (aceite no mesmo turno ou depois), e mantém a Emboscada. Os teus próprios membros ficam escondidos com ele e combatem a ×1.40. Um membro **aliado** é **visível** no mapa de todos os outros reinos e combate **sem bónus de postura** — nem sequer Defensiva — e o seu marcador nada mostra que aponte para o líder escondido; a página avisa-te quando acrescentas ou propões um aliado a partir de um exército em Emboscada. **Um aliado não pode arrastar um exército em Emboscada para o seu grupo:** a sua proposta fica como uma oferta pendente normal que não pode ser aceite enquanto a Emboscada durar — o proponente **não é informado do motivo**, ao passo que tu és. Se esse aliado já tinha uma oferta pendente sobre o teu exército, ela não é tocada e a tua carta di-lo. **Uma oferta feita antes da Emboscada espera:** ✓ Accept fica a cinzento enquanto o exército está em Emboscada, uma aceitação submetida mesmo assim é recusada e a oferta mantida, e pode ser aceite no turno em que a Emboscada termina (ordena outra postura ao lado da aceitação). "Em Emboscada" significa a postura que o exército mantém neste turno: uma postura submetida neste turno conta, e outra postura ou uma marcha termina-a. **Mantém-se num turno em que não submetes ordens**: a Emboscada guardada continua a funcionar, os teus próprios membros ficam escondidos com ela e um membro aliado continua visível — um turno falhado nada te custa aqui.

- **Comando.** A ligação é **persistente** até ser quebrada. As ordens de movimento e postura do líder comandam todo o grupo; as ordens de movimento e postura próprias de um subordinado são nulas — a sua única prerrogativa é **UNLINK** (efeito no mesmo turno: podes desligar e mover na mesma folha de ordens). O líder pode libertar membros individuais ou dissolver o grupo; a morte ou dissolução do líder dissolve-o. **Nem uma ligação sobrevive à aliança em que foi construída**: se o reino do membro e o do líder entrarem em guerra, terminarem a sua aliança mútua, ou o juramento de fidelidade do vassalo for renunciado, o membro é libertado no **fim desse turno** — depois de a diplomacia ser resolvida — e ambos os lados recebem carta com o motivo. Um **vínculo de vassalagem** vivo mantém a ligação, diga o campo de postura o que disser nesse turno (um vassalo que defina paz para com o seu suserano não dispersa o grupo). O teste é só **líder ↔ membro**: dois membros do mesmo grupo que se desentendam entre si continuam ligados e combatem lado a lado sob as ordens do líder até um desligar. Os subordinados continuam a **recrutar e a receber/enviar transferências de unidades** normalmente. **Uma marcha em fila e uma ligação nunca coexistem na página**: não podes ligar um exército que tenha um caminho planeado, e não podes retirar um UNLINK em fila — nem uma *libertação* de um membro em fila a partir da carta do líder — enquanto o exército libertado ainda tiver um caminho. Limpa primeiro o caminho; o motor descartaria essa marcha de qualquer forma, e a caixa recolhida escondê-la-ia de ti. **Um grupo formado partilha os seus membros com todos os que o integram:** o teu relatório lista as unidades, prontidão, postura e comandante de cada membro — aliados incluídos, nos dois sentidos — pelo que o ritmo do grupo na tua carta é o real, não um palpite cauteloso. Uma *proposta* não partilha nada até ser aceite, e no turno em que um membro sai deixa de constar da lista. O mesmo vale do lado do líder: um exército cuja marcha planeada seja mais longa do que o ritmo que um novo membro mais lento imporia tem de encurtar a rota antes de ligar.

- **Tão rápido, e tão fresco, como o seu homem mais fraco.** O ESTADO nivela pelo **mínimo** do grupo — na formação e outra vez a cada turno (um grupo em descanso ainda recupera, cada exército pelas suas regras, *depois* nivela ao mínimo). O ritmo de movimento é o **MP mais baixo** do grupo: um regimento de infantaria abranda toda a coluna para 60mp.

- **Uma força na batalha — nos dois sentidos.** O grupo ataca como uma única força combinada sob as ordens do líder e defende-se como uma só quando atingido. A ligação **é** consentimento: um aliado ligado em paz com o atacante combate na mesma — e assim **entra na guerra** — a não ser que o seu próprio reino também combata do lado atacante, caso em que é retido (defesa co-localizada, acima). A ligação é consentimento **nos dois lados**: um membro do grupo atacante segue o seu líder para um combate contra o seu próprio aliado (o exemplo trabalhado abaixo, Zingara), e um membro do grupo defensor que seja aliado, vassalo ou suserano do próprio atacante combate ao lado do seu líder da mesma forma (Ophir) — em qualquer dos casos essa aliança quebra-se — exceto nas muralhas do próprio aliado, onde o membro deixa o grupo (§5.11.1 regra 3). Os despojos do lado atacante repartem-se por quota de pontos de guerra, exatamente como a repartição defensiva.

- **Cercos e assaltos combinam-se.** Um grupo ligado em postura de cerco enfrenta o portão do cerco em conjunto (§5.8.1) e junta a salva dos seus engenhos — dois exércitos, cada um demasiado pequeno para investir um povoado, podem manter o anel em conjunto. Um assalto ligado toma as muralhas como um só; em caso de vitória o grupo entra no povoado, ainda ligado (um membro amigo do dono já o deixou, §5.11.1 regra 3). Todo o membro em serviço de cerco paga a sangria de −3 de ESTADO.

- **Chegar junto a um inimigo — o choque de chegada (arrival clash)**. Os membros pisam o hexágono do líder atrás dele, a cada passo. Se um membro — ou o líder — ficar então na mesma zona que um exército **já lá presente** com o qual **está em guerra**, **ataca à chegada**, antes de a marcha prosseguir: o exército já presente defende — mesmo quando ambos são amigos do dono do terreno — e só os exércitos chegados em guerra com ele combatem — um líder em paz com esse exército fica de fora e nada declara. Um exército que chega combate **uma batalha por passo**: qualquer outro inimigo nessa zona que não tenha defendido nela é combatido no varrimento de acampamento seguinte, se ainda estiverem acampados juntos. Os exércitos já presentes nessa zona juntam-se aos atacantes que chegam — os do reino atacante, e os de um aliado só quando já em guerra com todos os reinos do lado defensor (§2.13.5). Emboscada, Defensiva e Guarnição contam como em qualquer batalha de campo; nenhum hexágono muda de mãos. Se vencer, o defensor retira e o grupo prossegue em conjunto; se perder ou empatar, **todo** o grupo dispersa-se — um líder que não combateu mantém o seu caminho restante e percorre-o sozinho. Dentro contra fora de uma muralha é um cerco, nunca um choque de chegada; exércitos já acampados juntos em guerra aguardam o varrimento de acampamento (§2.13.5). **Os membros da ligação colocados no hexágono por um assalto chegam da mesma forma**: os membros que um assalto já pôs no hexágono do salto atacam um exército em guerra com eles na sua zona, e esse exército não se retira de graça. A carta de batalha do exército que chega diz porque combateu: *"Carried in Nemedia AII's group onto (5,5), your Army IV attacked Cimeria on arrival — your kingdoms are at war."*

- **A derrota dispersa o grupo.** Um grupo ligado que perde uma batalha de campo, um combate de praia ou as suas muralhas para um assalto retira exército a exército (se for batido fora das suas muralhas, entra antes inteiro, §5.8.0) — exceto um membro que nunca entrou no hexágono da batalha, que se mantém onde está (também no mar), com a carta *"Your army had not marched in with its leader — bruised, it held its position at (c,r)"* (uma frota: *"The survivors held their position at (c,r) — your fleet had not sailed in with its flagship"*) — e a **ligação quebra-se** (com carta). **Uma batalha de campo empatada também dispersa o grupo atacante** — os atacantes recuam exército a exército e os defensores mantêm-se — e as suas cartas dizem *"Stalemate at (c,r) against X — the group fell back and scattered"*. Uma **Surtida (Sally)** perdida ou empatada não dispersa: o seu grupo regressa junto para dentro das muralhas (§2.13.7). Um grupo **atacante** cujo assalto não toma as muralhas **não** é disperso: os seus sobreviventes ficam acampados às portas como sitiadores, ainda ligados (§5.8.0). A carta nomeia a batalha: um exército que combateu lê *"Defeat at (c,r) against X — the group scattered"*; um exército que **não** esteve nessa batalha lê que o seu líder foi batido ali e que é libertado — não lhe é dito que perdeu. Sempre que o próprio líder não combateu (por exemplo, um membro atacou à chegada), a carta nomeia os exércitos do teu grupo que foram batidos: *"Nemedia AII (in your group) was beaten at (5,5) by Cimeria — your army was not in that battle and is released; the group scattered"*. Um membro que não sobreviveu a essa batalha é nomeado como destruído: *"Nemedia AII (in your group) was destroyed at (5,5) by Cimeria — your army was not in that battle and is released; the group scattered"*. Reforma-o quando te reagrupares.

- **Sem embarque em grupo.** Os exércitos ligados não podem embarcar em frotas — faz UNLINK primeiro; cada exército embarca sozinho.

> ***▶ Exemplo — uma ligação aliada entre reinos.** O **II ARMY** de Cimeria e o **III ARMY** de Aquilonia são aliados mútuos, ambos no hexágono (24,18); Cimeria quer que marchem como um só, sob o seu comando.*
>
> *- **Turno 5 — Cimeria propõe.** Na carta do II ARMY, Cimeria escolhe o III ARMY de Aquilonia e submete. O relatório de Cimeria diz Link Offered — Cimeria A II offers a link to Aquilonia A III · awaiting the ally's LINK ACCEPT; o relatório de Aquilonia traz a oferta correspondente. **Ainda nada está ligado** — se Cimeria ordenar ao II ARMY que marche neste turno, marcha sozinho.*
>
> *- **Turno 6 — Aquilonia aceita.** A oferta aparece agora na carta do III ARMY de Aquilonia com um controlo LINK ACCEPT. Aquilonia aceita; ambos os relatórios dizem Link Formed — Cimeria A II links Aquilonia A III (allied — accepted). O ESTADO nivela de imediato pelo do mais fraco dos dois exércitos.*
>
> *- **Turno 7 em diante.** O II ARMY de Cimeria é o líder: as suas ordens de movimento e postura comandam ambos os exércitos. O III ARMY de Aquilonia tem as suas próprias ordens de movimento e postura ignoradas (com carta); a sua única prerrogativa é UNLINK, que tem efeito no mesmo turno.*
>
> *A oferta **persiste ao longo dos turnos** até ser aceite — mas caduca (com carta) se os exércitos se separarem, ou se a aliança terminar, for declarada guerra, ou o juramento de fidelidade de um vassalo for renunciado.*
>
> ***⚠ O que isto significa —** a aceitação custa um turno inteiro, pelo que uma ligação entre reinos tem de ser combinada **antes** do turno em que precisas da força combinada, não durante ele.*
>
> ***▶ Exemplo — uma ligação arrasta reinos que nunca se desentenderam.** Seis reinos, dois grupos de ligação de três exércitos cada, um turno. Só os dois **líderes** estão em guerra à partida — todos os outros pares estão em paz ou aliados, e dois dos seis são aliados do líder do outro lado. Esta é a armadilha: a diplomacia própria de um membro nunca tem voto depois de o seu exército estar no grupo.*
>
> *\| Grupo atacante (líder **Cimeria**) \| Relação com o lado de Nemedia \|*
>
> *\|---\|---\|*
>
> *\| **Cimeria** — I ARMY, 30 Legionnaire + 10 Equites, Gen. Strabo (military 40) \| **Em guerra** com Nemedia \|*
>
> *\| **Aquilonia** — I ARMY, 40 Velites \| Em paz com Nemedia, Vanaheim e Ophir \|*
>
> *\| **Zingara** — I ARMY, 40 Velites \| **Aliada de Nemedia** \|*
>
> *\| Grupo defensor (líder **Nemedia**, postura Defensiva) \| Relação com o lado de Cimeria \|*
>
> *\|---\|---\|*
>
> *\| **Nemedia** — I ARMY, 80 Legionnaire, Gen. Numa (military 30) \| **Em guerra** com Cimeria \|*
>
> *\| **Vanaheim** — I ARMY, 40 Legionnaire \| Em paz com Cimeria, Aquilonia e Zingara \|*
>
> *\| **Ophir** — I ARMY, 40 Legionnaire \| **Aliada de Cimeria** \|*
>
> *Cada membro é um **aliado mútuo do seu próprio líder** (o único requisito rígido da ligação) — Aquilonia e Zingara com Cimeria, Vanaheim e Ophir com Nemedia. As relações com o outro lado não são afetadas por isso, e ninguém as verificou antes de se alistar.*
>
> *- **Turno 1 — ambos os grupos ligam-se e Cimeria marcha, tudo num só turno.** Os exércitos de Cimeria já partilham o seu hexágono; os de Nemedia também. Cimeria emite LINK sobre Aquilonia e Zingara; Nemedia emite LINK sobre Vanaheim e Ophir; os quatro aliados submetem LINK ACCEPT no mesmo turno — todos os grupos se formam de imediato (o aperto de mão no mesmo turno do §5.11). Cimeria ordena então ao **I ARMY que marche para o hexágono de Nemedia**. Essa única ordem comanda toda a coluna: as ordens de movimento próprias de Aquilonia e Zingara são irrelevantes — de facto o ficheiro de Aquilonia ainda tem uma em fila (uma marcha-isco para outro lado), e o seu relatório explica porque nunca foi executada: "Army I follows its leader — Your Army I is linked under an allied Army I and marched with the group — its own move order was superseded. Only the leader moves the group; UNLINK to march independently." (o registo do GM mantém a linha concisa "Aquilonia — Army I is linked and follows its leader") Nemedia nunca chega a escolher se combate; o seu hexágono é simplesmente onde a coluna acaba.*
>
> *- **Quem combate realmente.** Os três atacantes chegam como uma só coligação — Cimeria, Aquilonia, Zingara, **120 tropas no total**, Aquilonia e Zingara incluídas apesar de nenhuma ter qualquer disputa com Nemedia. No hexágono defensor, gather-defenders arrasta todos os exércitos co-localizados que estão **em guerra com o atacante (e não em guerra com um defensor) OU ligados ao defensor principal** — Vanaheim e Ophir não estão em guerra com Cimeria à partida, mas ambos estão ligados a Nemedia, pelo que ambos são arrastados sem voto algum. **160 tropas** aguardam a carga, as três herdando a postura Defensiva de Nemedia através da ligação (a postura de um subordinado é a do líder — §5.11).*
>
> *- **A aritmética — saída real do motor, dos dois lados** (reexecutada contra o motor atual, ambos os grupos já ligados: todos os valores abaixo reproduzidos). Terreno da batalha: planície aberta (sem bónus de raça para nenhum dos lados, Imperial contra Imperial — attTerrainMult = defTerrainMult = 1.00). A pilha mista de infantaria e cavalaria de Cimeria dá a **toda a coligação atacante** uma escala de cavalaria combinada de **×1.10** (a planície favorece tropas montadas, e só o seu próprio contingente cavalga); os Velites de infantaria pura de Aquilonia e Zingara não trazem bónus de cavalaria próprio. A postura Defensiva de Nemedia aplica **×1.20** a todo o seu lado ligado. O bónus de comandante aplica-se **por exército, apenas ao seu próprio contingente** (cmdMult = 1 + military/1000, §5.5.1): o military 40 de Strabo dá às tropas de Cimeria ×1.04; o military 30 de Numa dá às tropas de Nemedia ×1.03 — Aquilonia, Zingara, Vanaheim e Ophir combatem sem comando. O ESTADO à entrada do combate já tinha custado 5 pontos à coluna em marcha pelo salto. Combinando o WP bruto, o terreno, a cavalaria, o ESTADO e o multiplicador de comandante de cada exército na força efetiva de cada lado, e depois lançando uma vez por lado (iniciativa = 1.075, sorte fixada exatamente em 1.00 para este exemplo trabalhado, de modo a que a aritmética seja verificável):*
>
> *- **Atacante:** WP 7174 → lançamento **8280***
>
> *- **Defensor:** WP 10720 × Defensiva ×1.20 → lançamento **13057***
>
> *- defRoll (13057) \> attRoll (8280) × 1.2 (9936) → **o lado de Nemedia vence.** Rácio 13057 ÷ 8280 = **1.58**.*
>
> *- Fórmula de baixas (§5.5.3) ao rácio 1.58: perdedor ≈ 0.12 + 0.18 × ln(1.58) ≈ **20%**, vencedor 0.10 ÷ 1.58 ≈ **6%** — e isso coincide exatamente com os números do próprio motor.*
>
> *- **Baixas, exército a exército.** Coligação atacante (120 → 99, **−21 tropas**, ≈20% cada): Cimeria 30 Legionnaire + 10 Equites → 24 + 9 (**−7**); Aquilonia 40 Velites → 33 (**−7**); Zingara 40 Velites → 33 (**−7**). Coligação defensora (160 → 151, **−9 tropas**, ≈6% cada): Nemedia 80 Legionnaire → 75 (**−5**); Vanaheim 40 Legionnaire → 38 (**−2**); Ophir 40 Legionnaire → 38 (**−2**).*
>
> *- **COMBATER SIGNIFICA GUERRA — o atacante paga pelo combate que forçou.** Todo o reino atacante que trocou golpes está agora em guerra com todos os reinos defensores que enfrentou — oito novas guerras numa só batalha (Cimeria–Nemedia já estava em guerra e não dispara de novo). **A penalização de opinião do próprio agressor está limitada a uma por passo de uma marcha ou viagem, e a uma por batalha para qualquer outro confronto** — este combate é um passo da marcha de Cimeria, e uma guerra declarada ao dono do hexágono ou aos seus defensores como salto de marcha, desembarque ou início de assalto conta para essa única penalização: por mais reinos com que um atacante entre em guerra neste MESMO passo, cada uma dessas guerras é declarada na mesma e cada reino recebe a sua própria carta — só o primeiro par processado custa opinião ao agressor; todos os seguintes nesse passo ficam limitados, com carta, sem mais perdas:*
>
> *- Aquilonia declara guerra a Nemedia, Vanaheim **e** Ophir (os três antes em paz) — as três guerras disparam, mas só a carta de Nemedia traz a penalização: "War declared against Nemedia! … Opinion -6 (aggressor penalty) … Previous stance: peace." As cartas de Vanaheim e Ophir trazem a mesma prosa de "peace is over" mas a linha de efeito limitada: "No further opinion penalty — already charged once this step."*
>
> *- Zingara declara guerra a Nemedia, Vanaheim **e** Ophir — e a carta de Nemedia lê-se de modo diferente das outras duas: "War declared against Nemedia! … A sworn alliance lies in ruins … Previous stance: alliance." Zingara seguiu Cimeria num combate contra a sua própria aliada e pôs ela própria fim a essa aliança — e esse é o ÚNICO par, dos três de Zingara, que come a penalização de opinião de agressor de −6; as cartas de Vanaheim e Ophir ficam limitadas como as de Aquilonia.*
>
> *- **Cimeria** — o líder que ordenou a marcha — também declara guerra a **Vanaheim e Ophir**, os dois reinos arrastados para a defesa de Nemedia apenas pela sua ligação, nenhum dos quais tinha qualquer disputa com ela à partida: "War declared against Vanaheim! … The peace is over … Previous stance: peace … Opinion -6 (aggressor penalty)." Vanaheim é o par que é cobrado — a carta de Ophir traz a MESMA prosa de aliança quebrada ("A sworn alliance lies in ruins … Previous stance: alliance") mas uma linha de efeito limitada: "No further opinion penalty — already charged once this step." Ophir era aliada de Cimeria — marchar sobre o hexágono de Nemedia é o que quebrou essa aliança — mas Cimeria paga os −6 só uma vez por todo o passo, não uma vez por reino que arrasta para a guerra.*
>
> *- Vanaheim e Ophir, arrastadas para a defesa sem disputa própria, nunca trazem uma carta de agressor por este combate — recebem a carta de **defensor** por cada atacante que lhes acaba de declarar guerra (Cimeria, Aquilonia, Zingara), e o limite aplica-se apenas ao lado agressor, pelo que cada uma dessas cartas de defensor traz o seu próprio +4 completo, sem limite: "Cimeria is now at WAR with you! … Your opinion +4 (defender's rally) … Previous stance: peace" para Vanaheim, "… A sworn alliance lies shattered … Previous stance: alliance" para Ophir. O reino que marchou e forçou o combate paga o custo de opinião — uma vez por passo, por muitos reinos com que entre em guerra de novo; o reino que ficou em terreno próprio e foi arrastado pela sua ligação nunca paga, e recebe o seu próprio apoio por inteiro de cada vez.*
>
> *- **As consequências da derrota.** O grupo de Cimeria perdeu o campo: Cimeria recua para (1,2), o hexágono de onde a coluna marchou — e Aquilonia e Zingara, que nunca o deixaram (os membros só seguem o líder para dentro depois de uma vitória), **mantêm-se onde estão** — e no momento em que o último aterra, a ligação quebra-se para os três. O registo do GM regista-o numa linha, por nome de reino: "Cimeria AI + Aquilonia AI + Zingara AI — group dissolved · Defeat — the group scattered." Cada um dos três JOGADORES vê algo diferente no seu relatório — o seu próprio exército, não a lista de nomes: "Army I — link broken · The link group is no more — Defeat at (1,3) against Nemedia, Vanaheim, Ophir — the group scattered. The army acts independently again. · Independent command restored." Reformá-lo custa uma nova proposta e (para os aliados) uma nova aceitação. O grupo de Nemedia **manteve o terreno e continua ligado** — só o lado perdedor se dispersa. A opinião moveu-se em todos os reinos que combateram (vencedores +2, perdedores −3, independente das variações das declarações de guerra acima), e a coligação de Nemedia dividiu 30% dos despojos do campo por quota de pontos de guerra.*
>
> *- **O que cada um dos seis vê.** Cimeria, Aquilonia e Zingara recebem cada uma uma carta de combate de Derrota completa (a mesma carga attWP/defWP/lançamentos/rácio transcrita acima), a sua própria linha de baixas e a carta de Link Broken do seu grupo. Nemedia, Vanaheim e Ophir recebem cada uma uma carta de Vitória, a sua própria quota de despojos, e nenhuma carta de Link Broken. Todas as seis recebem as cartas de nova guerra dos pares que combateram pessoalmente — as cartas de Vanaheim e Ophir nomeiam corretamente **Cimeria**, e não elas próprias, como quem a começou.*
>
> ***⚠ O que isto significa —** aderir a uma ligação é assinar um cheque em branco sobre a tua própria diplomacia — a ligação **é** consentimento, pelo que as guerras do teu líder se tornam as tuas guerras no instante em que uma batalha encontra o teu hexágono, o que quer que a diplomacia do teu reino dissesse no turno anterior. Verifica a lista de guerras do líder antes de aceitar, não depois. O único controlo que manténs é UNLINK, efetivo no mesmo turno em que o ordenas — a única forma de recusar um combate que o teu líder escolheu — exceto nas muralhas de um amigo, onde o teu exército deixa um grupo que se vira contra esse amigo (§5.11.1 regra 3).*

**Espetadores — quando o chão cede debaixo dos pés.** Um exército que ficou de fora da batalha pelo seu hexágono (estava em paz com o atacante) resolve-se pela sua postura para com o **conquistador** no momento em que o hexágono muda de mãos: **aliado** do conquistador → **fica** — o terreno pertence agora ao seu próprio aliado; em **paz ou neutro** → **retira em boa ordem** para um hexágono vizinho válido — sem guerra, sem baixas, uma retirada e não uma debandada; **encurralado** (sem linha de retirada) → homens encurralados não se rendem: o exército **declara guerra** e trava uma **última resistência** contra a força enfraquecida pela batalha do conquistador — se perder morre onde está, mas se **vencer retoma o hexágono**, ganho a sangue. (Ninguém **dentro** de muralhas é espetador: quem as assalta ou cerca está em guerra com todos os reinos lá dentro (§5.6), pelo que este parágrafo trata de terreno aberto e de exércitos acampados no exterior. Um povoado que cai por fome de cerco trata da mesma forma o exército de um terceiro reino acampado no exterior, exceto que um em guerra com o sitiador sem para onde fugir é desbaratado e despojado, §2.7.) **Um aliado só fica enquanto houver espaço**: após um assalto bem-sucedido todos os exércitos do conquistador ficam dentro das suas novas muralhas, em Guarnição, e um aliado conta o espaço na sua própria zona — um espetador aliado que seria o quarto na sua zona retira para dar lugar, com a carta *"made room"*. **Se não tiver para onde ir, é o conquistador que cede**: um dos exércitos do conquistador nessa zona que não seja nem o exército líder do ataque nem um líder de ligação retira — o próprio reino do conquistador cede antes dos seus aliados, depois por reino, o último exército primeiro (nunca pela ordem em que as ordens do turno foram lidas) — em boa ordem para um hexágono vizinho — sem baixas — deixa o seu grupo de ligação (o seu líder, cujo grupo sobrevive, lê *"Army N — X AN left the group"*), e recebe a carta *"withdrew … to make room"* com o motivo (o teu aliado ali estava encurralado); a carta do aliado diz quem cedeu. Só quando nenhum desses exércitos tem rota de saída (ou todos eles são líderes) é que a zona mantém um quarto exército — ambos os lados recebem carta, o hexágono é marcado para o validador do GM (apenas essa zona), e a marca desaparece quando um exército sai. **E quando a defesa se mantém**, um exército que ficou de fora mas está agora em guerra com um exército que ainda detém a sua zona retira em vez de acampar ao lado de um inimigo (§5.11.1) — nunca um exército **cercado**, que fica dentro (§2.13.7). **A última resistência de um exército encurralado é travada pelos próprios exércitos do conquistador no hexágono** — e pelo exército de um amigo apenas quando esse amigo já está em guerra com o reino do exército encurralado: um aliado que se juntou ao ataque, ou um membro de ligação de outro reino, não inicia uma nova guerra ali. Se nenhum dos exércitos do conquistador restar no hexágono, um amigo já em guerra com o exército encurralado combate-o sozinho; se o exército encurralado vencer, mantém ali o seu terreno — nenhum hexágono muda de mãos e nenhuma guerra começa com o conquistador, cujos exércitos não estiveram nesse combate; o seu relatório diz que mantém o terreno **ainda encurralado**, com todas as saídas fechadas. **Ordem:** os exércitos que *não* são aliados do conquistador resolvem-se primeiro — retiram ou fazem a sua última resistência — e só depois os seus aliados, que assim contam o espaço como ele realmente é. **Quando uma última resistência retoma o hexágono, o resto do acampamento resolve-se de novo contra o seu novo detentor** — um aliado do reino que retomou fica, um estranho retira ou, encurralado, faz a sua própria última resistência. *Já em guerra* conta uma guerra declarada por **qualquer** dos lados: um amigo que ainda detenha uma oferta de paz ao reino encurralado combate a última resistência com a sua própria postura inalterada — a sua oferta mantém-se, nenhuma guerra é declarada por ele e não paga penalização de agressor.

**Ler o mapa.** Os exércitos co-localizados abrem-se em leque no espaço de exército do hexágono — os escudos espalham-se ligeiramente para que a profundidade da pilha fique visível, com uma contagem **⚔×N** no leque. No mapa do reino o exército mais forte fica por cima; no minimapa de um exército, é esse exército. Os teus escudos ocupam a esquerda do leque, por ordem de espaço, e os escudos estrangeiros seguem-se à direita. Num hexágono com muralhas o leque divide-se por zona: os exércitos **dentro** das muralhas abrem-se no espaço superior, cada um com o **emblema de muralhas (walls badge)** — a imagem da construção do hexágono (o ícone do seu povo, ou a aldeia para um povoado POP; a cidadela quando nenhuma construção é conhecida) num disco escuro no canto superior direito do escudo — e os acampados no exterior no espaço inferior — só um exército em Guarnição, teu ou de um amigo, está dentro (§5.8.0), e a contagem **⚔×N** é por zona. Um movimento de grupo planeado pré-visualiza o **leque inteiro** no destino — membros aliados incluídos, grupos de frotas também. Um membro que acabaste de libertar, ou um grupo que estás a dissolver, fica onde está; as dicas do rato do mapa listam o leque da mesma forma. A própria ligação é **privada**: os inimigos veem apenas N exércitos a partilhar um hexágono, nunca quem comanda quem.

> ***⚠ O que isto significa —** LINK transforma três exércitos de tamanho médio numa coluna esmagadora — ao preço do ritmo (passo e ESTADO do mais fraco) e da fragilidade (uma batalha perdida dispersa o grupo). A defesa co-localizada automática é a ferramenta mais barata: estaciona dois exércitos num hexágono de fronteira e qualquer atacante enfrenta ambos, sem ordens. E atenção ao nivelamento: ligar um exército fresco a um exausto gasta de imediato a prontidão do exército fresco.*

**5.11.1 Batalhas entre os teus Aliados (Battles Between Your Allies — Um Reino, Ambos os Lados)**

Um reino aliado de dois reinos que entram em guerra um com o outro pode ver os seus exércitos (armies) em **ambos os lados do mesmo combate**: um acampado no hexágono do defensor — talvez ligado ao grupo do defensor — e outro a marchar no grupo de ligação do atacante. Estas regras decidem quem combate, que guerras começam e onde fica cada exército quando a poeira assenta. Aplicam-se a batalhas campais e assaltos em terra e a batalhas navais no mar.

**1. Um reino nunca combate em ambos os lados de uma batalha.** Se um dos teus exércitos combater do lado atacante, o teu exército que se encontra na defesa **põe-se de parte**: não defende, não sofre perdas, e o teu relatório (report) traz um cartão *"held back"* (retido). O teu exército atacante continua a combater, e os seus golpes são os do teu reino: entras em **guerra (war) com o defensor** e pagas a penalização de opinião (opinion) do agressor (a ligação é consentimento). Como estás agora em guerra com o defensor, o teu exército retido sai do grupo de ligação do defensor no fim do turno. O reino do próprio defensor nunca é retido.

**2. Quem mais se junta à defesa** é a regra do §5.11 acima; a regra 1 é a única exceção à atração do grupo de ligação.

**3. Junto às muralhas de um amigo, um membro sai do grupo.** Um exército ligado nunca combate um **amigo** (aliado mútuo, vassalo ou suserano do seu reino) junto às muralhas desse mesmo amigo.

- **Quando sai.** O seu grupo, junto a essas muralhas, marcha sobre elas, toma-as de assalto, cerca-as ou pressiona um assalto (Assault) ali; ou é atacado ali pelo dono ou pelos amigos do dono (um socorro, uma Surtida (Sally)); ou acampa ali enquanto hostil a eles — o reino do líder em guerra com o dono, mantendo o cerco (siege) ali, ou o líder em Cerco ou Assalto. Recebe o cartão *Army N left X's group at (c,r)*, e o reino do líder também é informado.

- **Quando fica.** Um grupo acampado ali em paz, sem pressionar nada e atacado por ninguém, mantém o seu membro, que combate com ele contra qualquer outro ali presente (um sitiante rival). Um grupo que marche para longe neste turno mantém o seu membro, que marcha com ele.

- **O que significa sair.** Fica onde estava, por conta própria e em paz com o seu amigo: não acrescenta nada ao anel, nunca é levado para dentro, e não é declarada guerra ao seu amigo. A regra 1 não se aplica. Mantém as suas próprias guerras — um reino com o qual já está em guerra continua a encontrá-lo ali.

- **Em guerra com o exército às portas.** Um membro em guerra com o exército que enfrentaria às portas continua a combater essa batalha — ao lado do seu grupo, ou sozinho se já tiver saído de um grupo acampado — mas sai do grupo antes de qualquer assalto às muralhas do seu amigo.

- **Entrar.** Ao dar ordem de Guarnição (Garrison), passa a porta do §5.8.0 (não passa um acampamento inimigo, nem entra num interior cheio). Uma vez lá dentro, o próximo ciclo de cerco do sitiante declara-lhe guerra como a todos os reinos lá dentro (§5.6), mesmo que o sitiante seja o seu próprio aliado.

- **Nenhuma nova ligação** se forma ali sob um líder hostil a essas muralhas: a oferta ou a ordem é recusada, com o cartão *Link refused*, com a causa.

> ***▶ Exemplo.** O VII da Aquilónia cerca as muralhas da Hiperbórea com o VI da Nemédia ligado; a Nemédia é aliada da Hiperbórea. Na pré-fase o VI sai do grupo e fica às portas, em paz — o anel conta apenas o VII. Se o VII tivesse marchado para longe nesse turno, o VI teria ido com ele. Se o VI tivesse dado ordem de Guarnição, teria entrado (havendo lugar), e o ciclo de cerco da Aquilónia poria então a Aquilónia e a Nemédia em guerra.*

O teu exército lá dentro, em Guarnição, é alvo de declaração de guerra como todos os reinos lá dentro (§5.6) e defende atrás das muralhas; uma vez cercado pode ordenar uma Surtida (§2.13.7). Se o grupo do atacante transbordar a zona exterior, o **grupo inteiro pára à porta**, e o cartão nomeia a zona que está cheia.

**4. Depois da batalha — onde fica cada um.**

- **O atacante toma o terreno.** Os exércitos que não combateram resolvem-se pela sua relação com o conquistador (o parágrafo *Bystanders* acima): um aliado do conquistador fica enquanto houver lugar — após um assalto os exércitos do conquistador ficam dentro das suas novas muralhas, em Guarnição, e um aliado conta lugar na sua própria zona (dentro apenas se estiver em Guarnição), pelo que um aliado que fosse o quarto ali retira-se, com o cartão *"made room"* — ou, se estiver encurralado, um dos exércitos não líderes do conquistador retira-se em seu lugar, com o cartão a indicar porquê (um quarto só fica se nenhum deles se puder mover); qualquer outro retira-se, e um inimigo encurralado faz uma última resistência.

- **A defesa mantém-se.** Um exército que ficou de parte mas está agora em **guerra** com um exército que ainda ocupa a sua zona do hexágono **retira-se em vez de acampar ao lado de um inimigo** — com o cartão *"withdrew"*, sem perdas: conserva as suas máquinas de cerco e paga apenas o habitual custo de prontidão da retirada (§5.10). Um que não tenha para onde ir fica, e é informado disso — e combate até ao fim no início da próxima Fase 5 (o varrimento de acampamento (camp sweep), §2.13). É exatamente isto que acontece ao teu exército retido quando a defesa se mantém, porque o teu exército atacante acabou de te pôr em guerra com o defensor. Um exército do reino atacante que esteja na zona do atacante nunca fica de parte: juntou-se ao ataque e partilha o seu resultado (§2.13.5).

- **O grupo do atacante avança.** Os membros seguem o líder para o hexágono apenas enquanto houver lugar; um membro que não caiba fica onde estava e sai do grupo. Um membro cujo reino está agora em guerra com o líder também não é levado, e sai do grupo no fim do turno. Um membro levado para dentro que esteja em guerra com um exército ainda no hexágono ataca-o à chegada (§5.11).

- **Uma batalha campal empatada ou perdida dispersa o grupo atacante**, e os seus cartões dizem *"Stalemate at (c,r) against X — the group fell back and scattered"* ou *"Defeat at …"*. **Uma Surtida não dispersa:** os seus sobreviventes regressam ao interior em Guarnição (§2.13.7). **Um assalto falhado também não:** os atacantes ficam acampados às portas como sitiantes, ainda ligados (§5.8.0).

**5. No mar.** As regras 1 e 2 valem para as frotas (fleets): se uma das tuas frotas atacar com o grupo do atacante, a tua frota na defesa põe-se de parte, com o cartão *"held back"*, e a tua frota atacante leva-te para a guerra. O mar não tem zonas nem passo de retirada: uma frota que fique a partilhar um hexágono com um inimigo combate-o no varrimento de coabitação do turno seguinte, antes do movimento (§2.14) — o equivalente em terra é o varrimento de acampamento da Fase 5 (§2.13).

> ***▶ Exemplo prático — a Aldória (A) e a Sylvane (C) estão em guerra, e ambas são aliadas de Gruk-Mor (B).** O grupo da Aldória, com A I, A II e o B I de Gruk-Mor, ocupa um hexágono; o grupo da Sylvane, com C I, C II e o B II de Gruk-Mor, avança sobre ele. Resultados reais do motor:*
>
> *\| O combate \| Exército de Gruk-Mor com a Aldória \| Exército de Gruk-Mor com a Sylvane \| Guerras de Gruk-Mor no fim \| Ligações \|*
>
> *\|---\|---\|---\|---\|---\|*
>
> *\| Campo aberto, a Sylvane vence \| Retido; fica como aliado da Sylvane \| Ataca a Aldória \| Em guerra com a Aldória, ainda aliado da Sylvane \| B I sai do grupo da Aldória; um membro da Sylvane que seria o quarto fica para trás \|*
>
> *\| Campo aberto, a Aldória resiste \| Retido, depois retira-se \| Ataca de onde estava; nunca entrou no hexágono, pelo que mantém a posição enquanto o grupo se dispersa \| Em guerra com a Aldória, ainda aliado da Sylvane \| O grupo da Sylvane dispersa-se; B I sai do grupo da Aldória \|*
>
> *\| Hexágono com muralhas, Aldória em Guarnição \| Defende ao lado da Aldória — a Sylvane declara guerra a todos os reinos dentro das muralhas, incluindo Gruk-Mor (§5.6); quando as muralhas caem recua com a Aldória \| Sai do grupo da Sylvane e fica onde estava — não dá assalto \| Em guerra com a Sylvane, ainda aliado da Aldória \| O grupo de B I dissolve-se; B II sai do grupo da Sylvane \|*
>
> *\| Hexágono com muralhas, exército da Aldória fora em Defensiva \| Defende ao lado da Aldória na batalha às portas \| Sai do grupo da Sylvane antes da batalha às portas — não combate nem essa batalha nem o assalto (regra 3) \| Em guerra com a Sylvane, ainda aliado da Aldória \| B II sai do grupo da Sylvane; se a Sylvane vencer, o grupo da Aldória dispersa-se \|*
>
> *\| Hexágono com muralhas, zona exterior já cheia \| — \| — \| Sem alteração \| O grupo inteiro da Sylvane pára à porta \|*
>
> ***A linha "exército da Aldória fora em Defensiva" por palavras.** A coluna da Sylvane encontra A I, A II e B I fora, em Defensiva, a céu aberto. B II marchou com a Sylvane mas é amigo da Aldória: sai do grupo da Sylvane, com o cartão Army II left Sylvane's group at (c,r) uma só vez, fica onde estava, e não é declarada guerra à Aldória. Se a Sylvane vencer, os vencidos entram em Guarnição e C I e C II dão assalto sem B II; se a Sylvane perder, recua sozinha.*
>
> *Ninguém lá dentro faz uma surtida contra o assalto da Sylvane: os exércitos da Aldória e de Gruk-Mor em Guarnição defendem atrás das muralhas a ×1.30; os que estiverem fora são combatidos primeiro. Só a partir do turno seguinte ao primeiro ciclo de cerco da Sylvane podem ordenar uma **Surtida** (§2.13.7) — e então os exércitos da Aldória e de Gruk-Mor podem sair juntos, ligados ou não.*

**5.12 Derivação do Cartão de Batalha (Battle Card Derivation — Registo de Fatores)**

Cada cartão de batalha terrestre e naval traz um **registo de fatores (factor ledger)** a par dos números-resumo descritos nos §5.5–§5.9: uma lista ordenada de todos os multiplicadores aplicados à rolagem, registados no momento em que o resolvedor os aplica e não reconstruídos depois, de modo que a Rolagem Final impressa possa sempre ser reconciliada com ele — Poder de Guerra base × Π(multiplicadores da cadeia) ≈ Rolagem Final, até ao arredondamento de apresentação. A cadeia é mantida **por participante**: uma batalha de coligação lista separadamente os multiplicadores de cada exército ou frota, mais uma curta **cauda** (tail) de todo o lado (iniciativa, fortuna e termos exclusivos de um lado, como a penalização de muralha do atacante num assalto) aplicada uma só vez ao total combinado do lado. O bónus de porto naval não é um termo da cauda: é uma linha da cadeia por frota, em qualquer dos lados em que uma frota combata num porto amigo (tabela abaixo). Na esmagadora maioria das batalhas — um exército ou frota por lado — a cadeia reduz-se exatamente a uma linha e lê-se exatamente como as fórmulas já dadas acima.

Ambos os cartões de batalha — terrestre e naval — estão dispostos como uma folha de resultados de combate nas cores do tema escolhido: os dois lados como peças (tropas ou navios, poder de guerra, perdas), a **régua de probabilidades (odds ruler)** — o rácio das rolagens finais numa escala de 0.5–4+, com a linha de vitória no limiar de vitória (§5.5.2) — e depois a **Derivação completa (Full derivation)** ao lado do registo de baixas, com cada modificador na sua própria linha com o produto acumulado (arredondado apenas para apresentação; um lado sem esse modificador mostra —). Quando um dos lados apresenta vários exércitos ou frotas, as linhas emparelham o **Contingente 1** com o Contingente 1 e assim sucessivamente, cada célula nomeando a sua própria unidade, antes dos totais dos dois lados e das linhas de toda a batalha (iniciativa, fortuna, muralhas, praia). A milícia de uma cidade é a sua própria peça e a sua própria linha de baixas. A folha termina com o carimbo de resultado e, onde os houver, os despojos de guerra ou as presas tomadas (§2.13.12). Um relatório anterior ao registo mostra o Poder de Guerra e os modificadores-resumo que trazia em vez disso — num assalto, assinalados como já incluídos nesse poder de guerra. Ambos os lados trazem a cadeia completa, fortuna incluída — e o mesmo acontece com o cartão de um reino que apenas assistiu (uma batalha na sua terra ou no seu porto), desenhado *Atacante \| Defensor* — o seu cabeçalho diz *"\<attacker\> WON"*, *"\<defender\> HELD"* ou DRAW, as linhas de porto dizem *Port bonus (defender)* / *Port bonus (attacker)*, e a nota de veteranos de cada lado traz o seu reino — exceto um combate no porto que envolva uma frota que não é sua amiga, visto das suas docas sem a derivação; um reino cujo próprio exército combateu na batalha recebe o seu próprio cartão de batalha, nunca o de um observador — o total é de qualquer modo visível no cartão, pelo que esconder as razões por trás dele apenas obrigaria o jogador a subtrair à mão. Um fator igual a ×1.00 é omitido da cadeia, com uma exceção: **o ESTADO do Exército / Frota é sempre impresso**, mesmo a ×1.00, por ser o único fator que um jogador acompanha turno a turno. A **Iniciativa** aparece apenas do lado do atacante — um defensor nunca a rola. A tabela-resumo no topo do cartão lista-a nos cartões de **ambos** os jogadores, na coluna do atacante.

Chaves de fatores, por tipo de batalha:

|                     |                                                                                                                                                                                                                                                                                                              |                                                                       |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Tipo de batalha (Battle kind)**     | **Fatores por participante (Per-participant factors)**                                                                                                                                                                                                                                                                                  | **Todo o lado (cauda) (Side-wide, tail)**                                                  |
| Assalto (Assault) (§5.6) | status, terrain, cav (a parte montada cavAssaultScale/cavTerrainScale do §5.6.1), cmd; a postura da guarnição e o bónus de fortaleza são por participante, e legion também o é (§4.2 — guarnição de um dono Imperial, ×1.10); a milícia aparece como participante nomeado à parte (militia, fortress, terrain, cmd, legion) | Atacante: wall (o attPenalty do §5.6.1), init, luck. Defensor: luck |
| Batalha campal (Field battle) (§5.5) | status, terrain, cav, stance (apenas defensor), cmd, legion (um dono Imperial a defender o seu próprio hexágono FI/POP — ou a fazer uma **surtida** a partir dele, o único caso em que a linha fica no atacante; §4.2)                                                                                                                  | Atacante: init, luck. Defensor: luck                                  |
| Anfíbia (Amphibious) (§5.7)   | Atacante: status, cmd. Defensor: status, stance, cmd, legion (um dono Imperial que detém a sua própria costa FI/POP; §4.2)                                                                                                                                                                                          | Atacante: beach (BEACH_PENALTY), init, luck. Defensor: luck           |
| Naval (§5.9)        | status, cmd, cargo (cargoMod), navrace (raceMod), port (portMod ×1.25 — qualquer frota que combata num porto amigo, atacante ou defensora, desde que tenha começado o turno nesse porto; uma linha por frota, pelo que um lado misto a mostra apenas em algumas frotas)                                                                 | Atacante: init, luck. Defensor: luck                                  |

Um segundo registo, independente, explica a linha de baixas: para cada pilha de unidades — e para a milícia, num assalto — nomeia a pilha, a sua contagem, o seu **fator de morte (death factor)** (o deathFactor do §5.5.4, o valor realmente usado após a mistura de dissolução da armadura do §5.5.3), a perda fracionária bruta e o número de efetivos realmente removido, arredondado. Um cartão sem perdas realizadas diz **"none"** — nunca uma percentagem solta ao lado de nada.

> ***▶ Exemplo — uma linha de baixas, nomeada.** Oito Elven Cavalry (xp_wp 251) perdem um assalto. O seu equivalente em preço (§5.5.4) é gold + iron×12 + horses×20 + wood×5 = 300 + 660 + 20 + 15 = 995; veterania vet = 251/247 − 1 ≈ 0.0162. landDeathFactor = max(0.3, 1 − 995 × 1.0162 / LAND_DEATH_BASELINE), onde LAND_DEATH_BASELINE = 1,100 — o termo interior dá cerca de 0.08, abaixo do piso, pelo que o **piso de 0.3** se aplica. A uma taxa de perda de batalha de 6.67%: rawLoss = 8 × 0.0667 × 0.30 ≈ 0.16 homens, arredondando para **0**. O registo de baixas declara a linha diretamente — unidade "Elven Cavalry", contagem 8, df 0.30, raw 0.16, lost 0 — e a linha de efeito reporta a perda realizada, nunca o valor bruto de entrada da curva. (Uma linha de milícia, quando aparece num assalto, usa MILITIA_DEATH_FACTOR = **1.0**.)*

**PARTE VI — ECONOMIA E PRODUÇÃO (PART VI — ECONOMY & PRODUCTION)**

**6.1 Os Seis Recursos (The Six Resources)**

|              |                      |                                                                                                                                                                                                                                  |
|--------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Recurso (Resource)** | **Fonte Principal (Primary Source)**   | **Principal Escoamento (Primary Drain)**                                                                                                                                                                                                                |
| Ouro (Gold)         | Imposto, portos, comércio    | Manutenção de unidades/navios, construção, contratação                                                                                                                                                                                |
| Comida (Food)        | Quintas, planícies, portos | Consumo dos exércitos, alguns custos de unidades                                                                                                                                                                                       |
| Ferro (Iron)         | Minas                | Produção de unidades/navios, alguma manutenção                                                                                                                                                                                                          |
| Cavalos (Horses)       | Criação               | Produção de unidades montadas                                                                                                                                                                                                          |
| Madeira (Wood)        | Serrações         | Recrutamento de unidades (40 de 42 unidades — só o Swordmaster e o Bladedancer não custam nada; todas as máquinas de cerco custam 50w), **todos os cascos de navios** (40–130w consoante a tonelagem), e **níveis de muralha das famílias Aesir/Nómada/Orc** (fundação, melhoria e reparação) |
| Pedra (Stone)        | Pedreiras             | **Níveis de muralha** de todas as outras famílias de construção (fundação, melhoria e reparação; as muralhas da família Anã custam metade)                                                                                                                  |

**6.2 Resumo das Fontes de Rendimento (Income Sources Summary)**

|                           |           |                                   |
|---------------------------|-----------|-----------------------------------|
| **Fonte (Source)**                | **Fase (Phase)** | **Recurso (Resource)**                      |
| Planícies (sem local de produção)          | Fase 1   | Comida                              |
| Imposto sobre a população | Fase 1   | Ouro                              |
| Locais de Quinta        | Fase 1   | Comida                              |
| Locais de Mina        | Fase 1   | Ferro                              |
| Locais de Porto        | Fase 1   | Ouro + Comida                       |
| Locais de Serração          | Fase 1   | Madeira                              |
| Locais de Pedreira        | Fase 1   | Pedra                              |
| Bónus de personagens         | Fase 1   | Ouro / Comida / Ferro / Madeira / Pedra |
| Pactos Comerciais               | Fase 1   | Ouro                              |
| Criação de cavalos            | Fase 1   | Cavalos                           |
| Reprodução Orc | Fase 1   | Tropas (não recursos)            |
| Tributo de vassalos (recebido) | Fase 1   | Ouro                              |
| Compras no mercado               | Fase 3   | Mercadorias                       |

**6.3 Imposto sobre a População (Population Tax)**

rawTax = floor(totalPop × taxRate / 100)

Taxa de 1–10 (definida pelo jogador, por omissão 5), cobrada na totalidade (ver Secção 2.9.5). A opinião (opinion) modifica o rendimento efetivo (ver Secção 2.9.6), e a taxa que mantiveres move a opinião todos os turnos (ver Secção 2.9.13). As alterações têm efeito no turno seguinte.

**6.4 Rendimento do Terreno por Hexágono (Hex Terrain Income)**

Planície (sem local de produção): 1 comida/turno. Não há ouro de terreno.

**6.5 Produção dos Locais (Site Production)**

|                     |           |                                                                                                |                                                |
|---------------------|-----------|------------------------------------------------------------------------------------------------|------------------------------------------------|
| **Local (Site)**            | **Nível (Level)** | **Fórmula (Formula)**                                                                                    | **Recurso (Resource)**                                   |
| Quinta (Farm)                | 1 / 2 / 3 | max(1, floor(pop × **roll 5–25% / 20–50% / 40–80%**))                                          | Comida (rolada por quinta por turno)                |
| Mina (Mine)                | 1 / 2 / 3 | 10 / 20 / 50 + floor(pop × level/20)                                                           | Ferro                                           |
| Porto (Port)                | 1 / 2 / 3 | max(1, floor(pop × 0.20 / 0.40 / 0.60)) gold + floor(pop × **roll 0–5% / 0–10% / 0–15%**) food | Ouro + Comida (comida rolada por turno, 0 possível) |
| Serração (Lumbermill) (floresta) | 1 / 2 / 3 | max(1, floor(pop × 0.15 / 0.45 / 0.75))                                                        | Madeira                                          |
| Pedreira (Quarry) — planície     | 1 / 2 / 3 | max(1, floor(pop × 0.15 / 0.45 / 0.75))                                                        | Pedra                                          |
| Pedreira — colinas/montanha  | 1 / 2 / 3 | max(1, floor(pop × 0.10 / 0.40 / 0.70))                                                        | Pedra                                          |

*Cada local produz pelo menos 1 do seu recurso num hexágono povoado (exceto a comida rolada de um porto), mas 0 se a população do hexágono for 0. As linhas de Porto são por porto antes do fator de escalão (§2.9.4 / §10.3). Regras e exceções: §3.6.*

**6.6 Pactos Comerciais (Trade Pacts)**

Um **pacto mútuo** — ambos os reinos em comércio ou melhor — paga 0–2% do imposto + ouro de portos por parceiro por turno (floor(rand×3) → 0/1/2%), **no máximo 5 parceiros num turno** (os restantes: *market saturated*). Qualquer par aquém de uma aliança mútua plena precisa de uma fronteira partilhada, verificada de novo todos os turnos; os benefícios da aliança plena (passagem, recrutamento aliado) exigem aliança em **ambos** os lados. Regras completas: §2.9.8.

**6.7 Tributo de Vassalo (Vassal Tribute)**

Taxa de 1–5%, por omissão 3%, do imposto da Fase 1 + ouro de portos (sem bónus de Mestre). Pagamento parcial se os fundos forem insuficientes. Vassalo e suserano ficam automaticamente em postura de Aliança — até que uma guerra entre eles ponha fim ao vínculo (§2.16.4).

**6.8 Referência de Manutenção (Upkeep Reference)**

Toda a manutenção é deduzida na Fase 2. A comida é consumida em separado através do consumo de comida dos exércitos.

**6.8.1 Manutenção de Unidades (Unit Upkeep — Ouro e Ferro por unidade por turno)**

|           |               |          |          |
|-----------|---------------|----------|----------|
| **Raça (Race)**  | **Unidade (Unit)**      | **Ouro (Gold)** | **Ferro (Iron)** |
| Imperial  | Velites       | —        | —        |
| Imperial  | Legionnaire   | —        | —        |
| Imperial  | Sagitarii     | 4        | —        |
| Imperial  | Equites       | 8        | —        |
| Imperial  | Praetorians   | 12       | —        |
| Bárbaro | Raiders       | —        | —        |
| Bárbaro | Berserker     | —        | —        |
| Bárbaro | Wild Archer   | 5        | —        |
| Bárbaro | Storm Horses  | 4        | —        |
| Bárbaro | Warchief      | —        | —        |
| Elfo       | Swordmaster   | —        | —        |
| Elfo       | Bladedancer   | 6        | —        |
| Elfo       | Ranger        | 8        | —        |
| Elfo       | Elven Cavalry | 10       | —        |
| Elfo       | High Guard    | 14       | —        |
| Orc       | Goblin        | —        | —        |
| Orc       | Orc           | 3        | —        |
| Orc       | Orc Archer    | —        | —        |
| Orc       | Warg Rider    | 4        | —        |
| Orc       | Uruk-Hai      | —        | —        |
| Anão     | Warrior       | 3        | 1        |
| Anão     | Ironclad      | —        | —        |
| Anão     | Crossbowman   | 5        | —        |
| Anão     | Thunderers    | 10       | 3        |
| Anão     | Heartguard    | 6        | 2        |
| Aesir     | Shore Raider  | —        | —        |
| Aesir     | Axe Thane     | 2        | —        |
| Aesir     | Shield-Karl   | 4        | —        |
| Aesir     | Huscarl       | 6        | —        |
| Aesir     | Jarl's Guard  | 10       | —        |
| Nómada     | Rajjala       | —        | —        |
| Nómada     | Naffatun      | —        | —        |
| Nómada     | Rumat         | 2        | —        |
| Nómada     | Bedouin       | 3        | —        |
| Nómada     | Askari        | 5        | —        |

> ***A comida não é um custo de manutenção.** Nenhuma unidade tem manutenção de comida; todos os exércitos comem por **número de efetivos** (§2.10.4), pelo que uma unidade mostrada com — em ambas as colunas continua a comer.*

**6.8.2 Manutenção de Navios (Ship Upkeep — por navio por turno)**

|           |            |          |          |
|-----------|------------|----------|----------|
| **Raça (Race)**  | **Navio (Ship)**   | **Ouro (Gold)** | **Ferro (Iron)** |
| Imperial  | Drommund   | 4        | —        |
| Imperial  | Cog        | 8        | —        |
| Imperial  | Galley     | 15       | —        |
| Bárbaro | Wolfship   | 3        | —        |
| Bárbaro | Reaver     | 5        | —        |
| Bárbaro | Tigress    | 14       | —        |
| Elfo       | Moonskiff  | 5        | —        |
| Elfo       | White Ship | 8        | —        |
| Elfo       | Swan Ship  | 16       | —        |
| Aesir     | Snekkja    | 3        | —        |
| Aesir     | Longship   | 8        | —        |
| Aesir     | Busse      | 14       | —        |
| Nómada     | Dhow       | 3        | —        |
| Nómada     | Shini      | 6        | —        |
| Nómada     | Harraqa    | 10       | —        |

**6.8.3 Consequências do défice (Deficit Consequences)**

|   |   |
|---|---|
| **Défice (Deficit)** | **Consequência** |
| Falta de ouro (Gold shortfall) | 5–15% de deserção de tropas em todos os exércitos (arredondado para baixo por pilha, sem mínimo — nunca o último soldado de um exército, §2.10.2); opinião −5 a −12 |
| Falta de ferro (Iron shortfall) | As reservas vão a 0; sem efeito em tropas nem em opinião |
| Falta de comida (Food shortfall) | Fome (Starvation): Orc 10–20% de perda de tropas; os restantes 3–10% |

> ***⚠ O que isto significa — duas espirais de morte separadas.** Exércitos maiores custam mais ouro em cada turno, pelo que um aparelho militar sobredimensionado pode desertar por si próprio mesmo em tempo de paz; a comida é uma verificação à parte (os Orcs são os piores), e um reino mal abastecido pode sofrer os dois golpes na mesma Fase 2. Mantém a manutenção (upkeep) total confortavelmente abaixo do rendimento — é paga antes de chegar o ouro de pilhagem ou os despojos de batalha (§2.13.11).*

**6.9 Transferências de recursos (Resource Transfers)**

Através de ordens send_resource (separador Shipments) ou do token de mensagem \[TRIBUTE\] — **um sistema unificado**, apenas de excedentes, ao **fim do turno** e **despachado como caravana (caravan)**: trânsito de 1 + floor(distância ÷ 5) turnos entre sedes de recrutamento (muster seats), uma **verificação de bandidos de 3% tudo-ou-nada** em cada turno de trânsito, e um regresso à origem se o destinatário não tiver sede ou já não existir. Diretamente apenas a um parceiro comercial/aliado mútuo, suserano ou vassalo; a um neutro é uma **oferta**; nunca a um reino em guerra. **O tributo de vassalagem e a compra/venda no mercado continuam instantâneos.** Regras completas: §2.8.2, §2.8.3, §8.7.

**6.10 O mercado (The Market)**

Os preços, o preço de venda de 60%, os limites das ordens e a dinâmica de preços estão todos em §2.11.4–§2.11.5. Na prática:

- **Compras caro e vendes barato.** Uma venda rende cerca de 60% do preço, pelo que uma revenda perde sempre dinheiro — o ferro a 12g volta a vender-se por round(12 × 0.6) = 7g, uma perda de 5g por unidade (comida a 8g → round(4.8) = 5g).

- **Resumo:** compra quando algo estiver barato (perto da base, ou logo depois de outros reinos o terem despejado) e vende quando estiver caro (após um pico de procura). Não faças entrar e sair a mesma mercadoria — a diferença entre compra e venda come-te o ouro em silêncio.

**6.11 Construção e melhorias (Construction and Upgrades)**

|   |   |   |
|---|---|---|
| **Ação** | **Custo** | **Probabilidade** |
| Construir Quinta (Farm) | 1000g | 100% |
| Construir Mina (Mine) | 1000g | 25% montanha / 15% colinas / 7% deserto e planície / 5% floresta |
| Construir Porto (Port) | 5000g | 100% |
| Construir Serração (Lumbermill) | 1000g | 100% |
| Construir Pedreira (Quarry) | 1000g | 100% |
| Serração Nv1→2 | 2000g | 100% |
| Serração Nv2→3 | 3000g | 100% |
| Pedreira Nv1→2 | 2000g | 100% |
| Pedreira Nv2→3 | 3000g | 100% |
| Quinta Nv1→2 | 2000g | 100% |
| Quinta Nv2→3 | 3000g | 100% |
| Mina Nv1→2 | 2000g | 30% — o terreno tem de ser montanha, colinas ou deserto (as minas de planície/floresta ficam no Nv1; recusado e reembolsado) |
| Mina Nv2→3 | 3000g | 50% — apenas reinos anões; o terreno tem de ser montanha |
| Porto Nv1→2 | 10000g | 100% |
| Porto Nv2→3 | 15000g | 100% |

**As construções (Constructions) são a outra metade do edificar, e funcionam de forma diferente.** Os locais de produção (Sites) têm um limite de nível 3 e preços indicados na tabela acima (§3.6), e só as minas fazem teste — para prospetar e para aprofundar; as construções são caras, **determinísticas** (sem dados — verifica-se cada condição e depois simplesmente acontece) e vão de 5 a 20 níveis consoante a família. Custam também **dois** recursos: ouro *mais* a pedra ou madeira do incremento de muralha.

|   |   |   |
|---|---|---|
| **Ação** | **Custo** | **Probabilidade** |
| Fundar construção (§2.11.9) | 500g de planta (blueprint) + 100 colonos (a sede tem de ter 300) + a **muralha completa** do escalão de fundação em pedra/madeira (família Anã: ceil(pontos/2); escalões sem muralha — Orc Nível 0, Nómada Nv.1, Genérico Nv.1 — sem qualquer material) | 100% se todas as condições forem cumpridas; caso contrário, recusado sem custo |
| Melhorar construção (§2.11.7) | Custo em ouro do nível seguinte **+ incremento de muralha** em pedra/madeira (família Anã: ceil(pontos/2)) | 100% se todas as condições forem cumpridas; caso contrário, recusado sem custo |
| Reparar muralha (§2.11.8) | 1 pedra/madeira por ponto, até floor(wallMax × 0.10) por turno | 100%, as reparações parciais têm êxito |
| Engenho de cerco (§5.8.6) | 250g + 50 madeira + 10 ferro cada, 3g/turno de manutenção | 100% (um recrutamento comum) |

Os valores de ouro e de muralha por nível variam consoante a família e estão listados no **separador 🏰 Constructions** da Página do Jogador para cada povoação que possuas. **Os seis tipos de ordem de construção partilham uma única ranhura por hexágono por turno** (§2.11.1).

**6.12 Criação de cavalos (Horse Breeding)**

Uma manada de 2+ cavalos cria 1–3% por turno (mais os pontos de um Mestre dos Cavalos, §2.9.7), arredondado para cima, sobre o que sobra depois de a cavalaria deste turno ser paga (§2.9.9).

**PARTE VII — PERSONAGENS (CHARACTERS)**

**7.1 O que fazem as personagens (What Characters Do)**

As personagens são indivíduos com nome e quatro atributos. Cada uma ocupa uma ranhura de atribuição. As personagens podem morrer após o combate — comandantes de exército após uma batalha terrestre, comandantes de frota após uma naval, com a mesma rolagem (§7.7). A morte é permanente.

O **líder do reino** mostrado na faixa da Página do Jogador é **derivado, nunca guardado**: é simplesmente a primeira personagem viva na ordem da corte. Não existe qualquer campo de líder no estado do reino e o Processador de Turnos nunca lê nenhum — todos os efeitos de personagem dependem de uma atribuição, pelo que a coroa em si não confere nada: nem bónus de atributo, nem mecânica. Quando um líder cai, a personagem viva seguinte na ordem da lista sucede-lhe de imediato (decide a antiguidade, não os atributos, para que o herdeiro não possa mudar em silêncio quando a corte muda); uma personagem contratada mais tarde nunca passa à frente na fila. Se toda a corte estiver morta ou vazia, a faixa mostra um cartão de **trono vago** até contratares de novo (§7.3).

**7.2 Atributos das personagens (Character Stats)**

Cada atributo é gerado aleatoriamente na criação; depois disso só pode subir através da experiência (§7.10), até ao máximo de min(150, base + 20%).

- **Personagens contratadas** (ordem hire_character da Fase 4): cada atributo é rolado entre 1–100.

- **Governantes iniciais** atribuídos pelo GM no Editor de Mapas na criação da campanha: cada atributo é rolado entre 20–100 (evitando o intervalo patológico 1–19). Os atributos do Rei Feiticeiro (Witch King) são ainda duplicados e limitados a 150 — ver §7.8.

|   |   |   |
|---|---|---|
| **Atributo** | **Usado por** | **Efeito** |
| Militar (Military) | Comandantes de exército / frota | cmdMult = 1 + military/1000 acrescentado à rolagem de combate |
| Economia (Economics) | Tesoureiro (Treasurer) | Rendimento de ouro de bónus: atributo × 0.2% do ouro de imposto |
| Gestão (Management) | Mestres das Quintas/Minas/Portos/Serrações/Pedreiras/Cavalos | Rendimento de recursos de bónus: atributo × 0.2% da base relevante (comida de quintas+portos, ferro das minas, ouro dos portos, madeira das serrações, pedra das pedreiras); o Mestre dos Cavalos acrescenta atributo × 0.02 pontos percentuais ao crescimento da manada (§2.9.9) |
| Política (Politics) | Mestre de Espiões (Spymaster) | Escalão de precisão dos espiões (\>75 / \>50 / ≤50); o preço de um rumor (§8.8.7) |

**7.3 Contratação (Hiring)**

Custo por omissão: **1000g** (CHAR_HIRE_COST_DEFAULT). Deduzido no momento da contratação. A ordem indica um candidate_id do **conjunto de candidatos (candidate pool) da tua corte — três candidatos rolados pelo TP** (reposto a três em cada turno); quaisquer atributos escritos na ordem são ignorados, o que obténs são os atributos rolados pelo TP para o candidato.

**Os nomes são únicos em todo o mundo.** Duas personagens — vivas **ou caídas** — não podem partilhar um nome, em nenhum reino, sem distinção de maiúsculas. Uma contratação com um nome já usado é recusada antes de se gastar ouro (*"Choose another name — this name was already taken."*); o candidato permanece no teu conjunto para uma tentativa com outro nome no turno seguinte. A recusa nunca diz **onde** o nome é usado — isso seria informação grátis. O Editor de Mapas aplica a mesma regra aos senhores iniciais na exportação, e a tua própria página deteta duplicados dentro da tua corte à medida que escreves.

**Um nome é texto simples até 28 caracteres.** A caixa de contratação aceita no máximo 28 caracteres, e o Processador de Turnos impõe o mesmo limite: um nome mais longo, que não seja texto, ou que contenha um carácter de controlo — incluindo os invisíveis que invertem a direção do texto ou acrescentam espaços de largura zero — é recusado antes de se gastar ouro (*"Choose another name — up to 28 characters of plain text"*), e o candidato permanece no teu conjunto. Os espaços nas pontas são removidos. Tudo o resto — acentos, apóstrofos (*Bor'aqh*), qualquer alfabeto — é aceite: o teu nome chega aos relatórios de outros reinos como o comandante dos teus exércitos e frotas, e todas as páginas o mostram como texto, nunca como código.

**Limite de tamanho da corte: máximo de 10 personagens vivas.** As personagens mortas (caídas em batalha, à espera de dispensa) não contam para o limite — perder um comandante em batalha liberta de imediato uma ranhura. O Rei Feiticeiro conta como uma personagem viva, pelo que os reinos orcs podem contratar no máximo 9 senhores adicionais. Quando a corte está cheia:

- O botão de contratação no painel de Personagens fica desativado e mostra **⛔ Court Full (10/10)**.

- Surge uma faixa vermelha acima da tua lista de personagens.

- Qualquer ordem hire_character submetida ao TP é rejeitada e não devolve alterações (sem dedução de ouro).

- Dispensa uma personagem morta ou indesejada para abrir uma ranhura.

**7.4 Atribuições (Assignments)**

|   |   |   |   |
|---|---|---|---|
| **Chave** | **Função** | **Atributo usado** | |
| army_N | Comandante do Exército N | Militar | |
| fleet_N | Comandante da Frota N *(Orc, Anão: indisponível — sem frotas)* | Militar | |
| treasury | Tesoureiro | Economia | |
| farms | Mestre das Quintas | Gestão | |
| mines | Mestre das Minas | Gestão | |
| ports | Mestre dos Portos | Gestão | *(Orc, Anão: indisponível — sem portos)* |
| lumbermills | Mestre das Serrações | Gestão | |
| quarries | Mestre das Pedreiras | Gestão | |
| horses | Mestre dos Cavalos | Gestão | |
| spy | Mestre de Espiões | Política | |
| none | Sem atribuição | — | |

Estas chaves são as **únicas** cadeias de atribuição que o Processador de Turnos aceita, e apenas em assign_character. Qualquer outra é recusada com um cartão ⚠ *"Assignment failed"* e a função atual fica intocada. As duas restrições de raça da tabela acima são aplicadas **no servidor**: Mestre dos Portos e comando de frota. Uma **contratação junta-se sempre à corte sem atribuição** — qualquer atribuição escrita numa ordem hire_character, válida ou não, é ignorada e assinalada com um cartão; as funções só são dadas através de assign_character, que é onde residem as verificações de raça e de um-comandante-por-exército.

A precisão dos espiões usa o atributo Política da personagem atribuída como **Mestre de Espiões** (a atribuição spy), lido do estado do servidor no momento do processamento. O valor de Política embutido no objeto da ordem é ignorado. Um reino sem Mestre de Espiões atribuído opera no escalão de precisão mais baixo.

> ***⚠ O que isto significa — uma pessoa, um cargo.** Cada personagem ocupa exatamente uma ranhura de atribuição, e a tua corte está limitada a 10 personagens vivas (§7.3). Um senhor que comanda um exército não pode ao mesmo tempo gerir a tesouraria; pôr a tua personagem com mais Política em funções de Mestre de Espiões significa que ela não está a reforçar o rendimento noutro lado. Faz corresponder o atributo mais forte de cada personagem à sua função — Militar → comandante, Economia → tesouraria, Gestão → um Mestre das Quintas/Minas/Portos, Política → Mestre de Espiões — e decide deliberadamente a que bónus escolhes renunciar. Com apenas 10 ranhuras, um reino não pode fazer tudo ao mesmo tempo.*

**As atribuições produzem efeito no mesmo turno.** Uma ordem assign_character é resolvida na Fase 4, pelo que a personagem comanda — e pode morrer — nas batalhas das Fases 5/6 desse mesmo turno; não há tempo de viagem nem atraso, onde quer que o exército ou a frota se encontre. Atribuir a um army_N/fleet_N ocupado desloca de imediato o comandante anterior para none (por desenho). **Contratar e atribuir no mesmo turno funciona:** a Página do Jogador envia a contratação e uma assign_character separada em conjunto, e a nova personagem assume o cargo nesse turno. O que o cargo faz primeiro depende de quando corre a sua fase: um **comandante** lidera nas batalhas desse turno (Fases 5/6) e um **Mestre de Espiões** executa as missões desse turno (Fase 7); um **cargo de rendimento** — Tesoureiro, os Mestres das Quintas, Minas, Portos, Serrações, Pedreiras e Cavalos — paga a partir do turno **seguinte**, porque a Fase 1 calcula o rendimento e a criação antes de a Fase 4 atribuir.

**7.5 Fórmula do bónus de comandante (Commander Bonus Formula)**

cmdMult = 1 + military / 1000

Militar 100 → ×1.10. Militar 50 → ×1.05. Sem comandante → ×1.0.

Aplica-se às rolagens de combate do atacante e do defensor, de forma independente.

**7.6 Fórmula do bónus económico (Economic Bonus Formula)**

bonus = atributo × 0.2% do rendimento base relevante.

Gestão 80 nas Quintas = 16% de bónus de comida na base de comida da quinta **e do porto** (§2.9.7). Máximo com atributo 100: 20% de bónus.

**7.7 Morte do comandante (Commander Death)**

deathChance = min(0.4, lossPct × 0.5)

80% de baixas → 40% de probabilidade de morte (máximo) — as perdas em campo, anfíbias **e navais** seguem a curva suave (uma disputa de tomada não rola morte de comandante): **30%** de probabilidade de morte no teto de 60% do piso de dano (cerca de 5:1 a 13:1), subindo com a rampa de aniquilação até aos **40%** completos a partir de aproximadamente 20:1 (no mar, numa rampa mais curta, a partir de 7.5:1); nas muralhas, os 40% chegam com 80% de baixas. A personagem passa a dead: true e fica permanentemente inativa. **Os comandantes de exército e de frota rolam ambos** — um comandante de frota sobre a percentagem de perda de casco após um combate naval; um comandante de exército a bordo de uma frota que afunda testa a morte com 100% de perdas — o máximo de 40% — enquanto o próprio exército se perde (§5.9.4). Um comandante que sobreviva à perda do seu exército ou frota — em batalha, no mar, com um porto caído, por dissolução ou por fusão — é libertado do comando no fim do turno, com um cartão a dizê-lo, e pode receber um novo. Um comandante que colocaste numa ranhura que ainda não tem exército nem frota mantém essa ranhura. Todos os comandantes numa batalha rolam sobre as perdas do seu próprio lado — ganhem, percam ou empatem, em campo, nas muralhas ou no mar; não há limiar abaixo do qual um comandante esteja seguro.

Uma morte é **comunicada aos autores** — o lado oposto, uma vez cada, sem nunca dizer que exército ou frota o comandante liderava; quem conta como lado oposto nas muralhas e no mar está definido em §5.5.5.

**7.8 O Rei Feiticeiro (The Witch King)**

Os reinos orcs podem ser liderados por um **Rei Feiticeiro (Witch King)** — um governante morto-vivo designado pelo GM no Editor de Mapas na criação da campanha. Esta designação é permanente e não pode ser alterada durante o jogo.

**Propriedades:**

|   |   |
|---|---|
| **Propriedade** | **Valor** |
| Atributos | Cada atributo rolado entre 20–100, duplicado, limitado a 150 (ou seja, 40–150 efetivos) |
| Morte | Imune — a verificação de morte em combate é totalmente suprimida |
| Dispensa | Não pode ser dispensado; serve durante toda a campanha |
| Bónus de comandante | Militar 150 → cmdMult = ×1.15 (máximo possível) |

O Rei Feiticeiro aparece no painel de Personagens com um retrato ☠️ e o título **Undying Ruler of the Horde**. Não é mostrado nenhum botão de dispensa.

**Nota do GM:** A opção do Rei Feiticeiro está disponível apenas para reinos orcs no Editor de Mapas. Ativá-la para um reino é uma decisão de desenho ao nível da campanha — não pode ser revertida depois de a campanha começar.

**7.9 Dispensar uma personagem (Dismissing a Character)**

As personagens (exceto o Rei Feiticeiro) podem ser dispensadas permanentemente a partir do painel de Personagens.

- **Personagem viva** — prime o botão **✕**. A personagem deixa o reino no fim do turno e não aparecerá no relatório seguinte.

- **Personagem morta** — prime o botão **🗑**. O registo da personagem caída é removido do estado do GM e não aparecerá em relatórios futuros.

A dispensa é processada na Fase 4 e não é reversível. Sem uma ordem de dispensa, os registos de personagens mortas persistem indefinidamente no estado do GM (não têm efeito no jogo, mas ocupam o painel de Personagens).

O Rei Feiticeiro não pode ser dispensado. Tentar dispensá-lo mostra uma notificação de erro.

**7.10 Experiência das personagens (Character Experience)**

Senhores e senhoras crescem com o serviço. Cada atributo pode subir no máximo **20% acima do seu valor original** (arredondado para baixo, mínimo +1), nunca além de 150.

- **Militar** — +1 por cada **3 batalhas** travadas pelo exército ou frota que a personagem

comanda. Vitórias, derrotas e empates contam todos; contam as batalhas de exército e as navais. Combater a milícia da população não conta — apenas as batalhas contra um verdadeiro exército ou frota inimigos. Um comando inativo não rende nada.

- **Economia / Gestão / Política** — +1 por cada **10 turnos** servidos num

cargo dessa competência: Tesoureiro (Economia); Mestre das Quintas, Minas, Portos, Serrações, Pedreiras ou Cavalos (Gestão); Mestre de Espiões (Política). Os turnos em cargos diferentes da mesma competência acumulam-se — o progresso sobrevive à reatribuição, apenas fica em pausa enquanto a personagem não tiver nenhum cargo desse tipo.

O cartão da personagem mostra o valor atual de cada atributo face ao seu teto e o progresso rumo ao ponto seguinte. Um aumento de atributo é anunciado no teu relatório do turno. O Rei Feiticeiro cresce segundo as mesmas regras (o mesmo teto min(150, original + 20%) — 150 é o limite absoluto, não o seu teto especial). As personagens mortas não ganham nada.

O cartão de cada comandante guarda também um **registo de batalhas** — vitórias, empates e derrotas — contado para as mesmas batalhas que concedem a experiência militar acima. O registo aparece no cartão da personagem como **W · D · L** e mantém-se visível mesmo para um comandante caído. O total de um senhor conta apenas as batalhas travadas desde que os registos de batalha começaram na campanha — o registo de um veterano mais antigo pode ser curto.

**PARTE VIII — DIPLOMACIA E ESPIONAGEM (DIPLOMACY & ESPIONAGE)**

**8.1 Posturas diplomáticas (Diplomatic Stances)**

Cinco posturas: paz (por omissão), guerra, aliança, comércio, e vassalo/suserano (estrutural).

**8.2 Declarar guerra (Declaring War)**

Por ordem de diplomacia (Fase 8) ou por contacto entre exércitos (auto-declaração na Fase 5, §2.13.8). Uma guerra iniciada neste turno bloqueia, na Fase 8 do mesmo turno, qualquer ordem de paz, aliança ou comércio para esse reino; a guerra mantém-se até ao turno seguinte (§2.16.2).

**8.3 Fazer a paz e alianças (Making Peace and Alliances)**

**As muralhas prevalecem sobre os tratados.** Assaltar ou cercar muralhas declara guerra a todos os reinos com um exército lá dentro, incluindo um aliado (§5.6), e um exército já **cercado** continua cercado enquanto o anel se mantiver, qualquer que seja a paz ou aliança que o seu reino assine (§2.13.7).

Através de ordem de diplomacia da Fase 8; a guerra prevalece sobre todas as ordens conflituantes. Terminar uma aliança ou pacto comercial **mútuo** (✕ *End Alliance*, ✕ *End Trade Pact*) é unilateral e leva ambos os lados à paz — quebrar uma aliança mútua custa opinião (§8.5.3). Terminar uma guerra exige o consentimento do inimigo (🕊 *Propose Peace*), e uma aliança exige as ordens de ambos os reinos; os reinos passivos nunca correspondem, pelo que não podem ser aliados. Cartões, avisos e retiradas: §2.16.2.

**8.4 Postura comercial (Trade Stance)**

Exige ordens independentes de ambos os reinos **e uma fronteira partilhada**, e paga o bónus de ouro do pacto de 0–2%/turno por cada parceiro mútuo — que um par comércio↔aliança continua a pagar enquanto a oferta de melhoria se mantiver (§2.9.8). Ofertas, avisos e o cartão *"Diplomacy blocked"* para uma recusa por fronteira: §2.16.2.

**8.5 Opinião (Opinion)**

**8.5.1 Escala (Scale)**

0–100. Por omissão 90. Representa o apoio popular interno. Não representa as relações entre reinos.

**8.5.2 Opinião e rendimento de impostos (Opinion and Tax Income)**

Com opinião 50 ou inferior perde-se uma parte do imposto bruto (PENALTYTAX): 2% em 41–50, subindo 2 pontos por cada escalão de dez até 10% em 0–10 (§2.9.6).

**8.5.3 Como muda a opinião (How Opinion Changes)**

|   |   |
|---|---|
| **Causa** | **Efeito** |
| Taxa de imposto mantida, **todos os turnos** (a taxa que cobrou) | +2 por ponto abaixo de 5%, −2 por ponto acima: +8 a 1% até −10 a 10% (§2.9.13) · mudar a taxa não custa nada por si só |
| Défice de ouro | −5 a −12 |
| **Qualquer batalha ganha** — em campo, surtida/libertação, praia, assalto (tomado ou repelido), naval, queda automática de cerco | vencedor **+1 a +3** |
| **Qualquer batalha perdida** — mesma lista | perdedor **−2 a −4** |
| Povoação tomada / assalto repelido — **proprietário terceiro** (a guarnição de outrem lutou pela tua povoação) | o proprietário sofre a mesma oscilação que a guarnição: −2 a −4 numa queda, +1 a +3 numa defesa bem-sucedida |
| Guerra declarada por ordem de diplomacia (Fase 8), a partir da paz | agressor −3 a −6; alvo +2 a +5 |
| Guerra declarada por movimento ou combate (Fases 5–6) | agressor −3 a −8 — **uma vez por passo de uma marcha ou viagem** (a batalha ao entrar no hexágono e qualquer choque de chegada a que esse passo conduza partilham uma só cobrança) e **uma vez por batalha** para qualquer outro confronto, por muitos reinos que o combate arraste; as guerras declaradas ao dono do hexágono e ao seu ocupante quando começa um passo de marcha, desembarque, movimento de frota, assalto ou choque de acampamento/porto contam para essa cobrança, uma incursão ou uma ligação de guerra por bloqueio conta como um só confronto com o choque de porto nesse porto, e uma reivindicação de origem e o primeiro passo da marcha contam como dois (§2.13.8); cada guerra adicional continua a ser declarada e assinalada com cartão, com a linha de efeito a dizer *"No further opinion penalty — already charged once this step"* dentro de um passo de marcha ou viagem e *"… once this battle"* em qualquer outro lado; alvo +2 a +5 em cada declaração |
| Guerra declarada, unilateral, a partir de aliança — **apenas alianças MÚTUAS** | agressor −8 a −15; alvo +5 a +10; traição difundida a todos os reinos · declarar guerra após uma *proposta* unilateral a que o alvo nunca correspondeu é uma declaração normal (−3 a −6, sem difusão) |
| Guerra mútua (ambos declaram no mesmo turno) | ambos −1 a −3 |
| Quebrar aliança (paz a partir de aliança) — **apenas alianças MÚTUAS** | quem declara −2 a −4; alvo −1 a −3 · ambos os lados recebem cartão; retirar uma *proposta* de aliança unilateral a que o alvo nunca correspondeu é gratuito para ambos |
| Descer aliança a comércio — **apenas alianças MÚTUAS** | quem declara −1 a −2; alvo −1 a −2 · ambos os lados recebem cartão; retirar uma proposta sem correspondência é gratuito |
| Paz formada (mútua — a guerra só termina quando ambos os lados mantêm ou ordenam paz ou melhor; ordens de guerra→aliança/comércio, por si sós, não dão nada) | ambos +1 a +3 |
| Cessar-fogo aceite | ambos +2 a +5 |

Limitada inferiormente a 0, e superiormente a 100. Cada oscilação resultante de uma batalha é indicada no seu próprio cartão do relatório (a linha de efeito traz · Opinion +N / · Opinion −N), pelo que a opinião nunca se move sem uma causa visível.

> ***▶ Exemplo — a opinião é um imposto discreto sobre a agressão.** A opinião começa em 90 e só morde a 50 ou menos, onde corta 2–10% do teu rendimento de impostos, tanto mais quanto mais baixa for (a linha PENALTYTAX no teu cartão de rendimento). O verdadeiro perigo é o ciclo de retroalimentação: declarar guerras, manter uma taxa de imposto acima de 5% (cobrada todos os turnos), **e cada batalha perdida (−2 a −4 cada)** arrastam a opinião para baixo, e uma série delas pode fazer-te cair abaixo de 50 exatamente quando uma guerra exige o máximo de rendimento. As derrotas custam mais do que as vitórias rendem (+1 a +3), pelo que uma guerra longa de desgaste corrói até a reputação de um vencedor. O golpe mais duro é a **traição** — declarar guerra a um aliado custa −8 a −15 de uma só vez, mais uma difusão a todos os outros reinos. Uma única facada numa aliança pode fazer-te passar de confortável a sobretaxado e desconfiado. Trata a opinião como um orçamento que gastas em agressão, e mantém a taxa de imposto abaixo de 5% (+2 por ponto, todos os turnos) para recuperar entre guerras.*

**8.6 Vassalagem (Vassalage)**

**8.6.1 Tornar-se Vassalo (Becoming a Vassal)**

Ordem become_vassal — uma oferta que o suserano aceita ou recusa com as suas ordens seguintes; os requisitos, incluindo a regra contra cadeias de vassalos e as aceitações no mesmo turno, estão em §2.16.4.

**8.6.2 Tributo (Tribute)**

Taxa de 1–5% do rendimento (income) em ouro da Fase 1 (imposto + ouro dos portos, sem os bónus dos Mestres — não a tesouraria), por defeito 3%, ajustada pelo suserano com set_vassal_tribute (§2.16.4). O suserano troca proteção e uma fronteira pacífica garantida por uma parte modesta, proporcional ao rendimento — o vassalo fica com 95–99% dos seus ganhos.

**8.6.3 Abandonar (Leaving)**

leave_vassalage termina o tributo a partir do turno seguinte, após um último pagamento; uma guerra entre suserano e vassalo termina o vínculo no momento em que começa (§2.16.4).

**8.7 Mensagens e Cessar-fogo (Messaging and Ceasefire)**

Os limites de mensagens, a difusão 📢 e o símbolo mútuo \[CEASEFIRE\] estão definidos em §2.16.5.

\[TRIBUTE: amount resource\] numa mensagem envia recursos (resources) ao reino destinatário através do **mesmo sistema de caravanas (caravan)** do painel **Shipments → Send Resources**, incluindo as regras permanentes (§2.8.2, §2.8.3). O formato é uma quantidade inteira seguida de um de gold, food, iron, horses, wood ou stone — p. ex. \[TRIBUTE: 500 gold\] ou \[TRIBUTE: 200 wood\]. Um tributo por mensagem (só o primeiro símbolo \[TRIBUTE:…\] é executado); usa mensagens separadas para vários destinatários ou mercadorias. Não é executado dentro de uma difusão, e a sua caravana tem uma etiqueta **🏛 tribute** nas listas de Shipments.

**8.8 Espionagem (Espionage)**

**8.8.1 Custo e Requisitos (Cost and Requirements)**

Custo min(200, 15 + 15 × dist) de ouro (gold) consoante a distância ao teu hexágono (hex) próprio mais próximo, um risco de perda na mesma curva, e **máximo de 3 missões de espiões por turno (turn)** — regras completas em §2.15. A precisão vem da personagem atribuída como Mestre de Espiões (Spymaster) (lida pelo servidor no momento do processamento). Podes escolher qualquer hexágono por coordenada.

**8.8.2 Conteúdo do Relatório (Report Contents)**

Após o movimento da Fase 5: estimativa da população (population), tipo/nível do local, uma linha 🧱 Fortifications em qualquer hexágono com construção, e todos os exércitos (army) estrangeiros presentes, exceto um em Emboscada (Ambush) válida, identificados pela sua relação contigo, com contagem aproximada de tropas e o proprietário — conteúdo completo em §2.15.

**8.8.3 Níveis de Precisão (Accuracy Tiers)**

A variância, a precisão do local, as estimativas de tropas e a fórmula vary() por nível estão na tabela de precisão de §2.15. Os níveis decidem também a avaliação da composição: completa a \> 75, grosseira a \> 50, nenhuma a ≤ 50.

**Avaliação da composição (Composition assessment)** (dois eixos): a proporção de montados é verificada primeiro — mais de ⅔ montados lê-se *"Cavalry host — predominantly mounted"*, mais de ⅓ *"Mixed force — foot and horse"* — depois o equipamento de ferro pelo ferro do **custo de construção**: mais de 40% de unidades feitas com ferro lê-se *"Heavy armoured infantry — iron-equipped"*, caso contrário *"Mixed foot soldiers — standard equipment"*. O nível intermédio (\>50) vê as versões mais vagas *"Mounted troops sighted"* / *"Heavily armoured troops"* / *"Standard troops"*.

**8.8.4 Penalização do Território Elfo (Elf Territory Penalty)**

Escolher um hexágono pertencente a um reino **Elfo** degrada a precisão em um nível, independentemente da Política do Mestre de Espiões. A sociedade élfica é singularmente resistente à recolha de informações estrangeira.

|                        |                     |                            |
|------------------------|---------------------|----------------------------|
| **Spymaster Politics** | **Normal Tier**     | **Tier vs. Elf Territory** |
| \> 75                  | High confidence     | Moderate confidence        |
| \> 50                  | Moderate confidence | Low confidence             |
| ≤ 50                   | Low confidence      | Low confidence (unchanged) |

A nota de qualidade, tanto na pré-visualização da ordem de espionagem como no relatório final, reflete o nível degradado. Isto acumula-se com a interferência de contraespionagem.

> ***▶ Exemplo — o aspeto de um relatório de espionagem real.** O teu Mestre de Espiões tem Política 60 (o nível "moderado" \>50: ±15% nos números, nível do local ±1, nome do comandante visível). Fazes o reconhecimento de um hexágono inimigo que tem realmente 1,000 de população, uma mina de Nível 3 e uma guarnição (garrison) de 200 soldados.*
>
> *• **População** devolve um valor dentro de ±15% — cerca de 850 a 1,150.*
>
> *• **Mina** lê-se como "about Level 3" (pode mostrar Nível 2, 3 ou 4).*
>
> *• **Tropas** são comunicadas em cerca de 170–230, e o nome do comandante do inimigo é legível (visível a partir do nível \>50 — só é preciso um mestre de espiões de elite para ler os números com precisão, não para saber quem lidera).*
>
> *Agora torna o hexágono **propriedade de Elfos**: a penalização élfica (§8.8.4) faz-te descer um nível para "baixo" (±30%, 40% de probabilidade de falhar o local por completo e — num hexágono realmente vazio — 25% de probabilidade de um falso avistamento fantasma; uma guarnição real continua a nunca ficar escondida de ti só por Política baixa). E se o defensor tiver construído **Counter-Espionage ≥ 20%**, linhas militares inteiras podem desaparecer do relatório para além disso — a **≥ 40%** o teu agente corre o risco de ser queimado de vez. A Política, a raça do alvo e a contrainformação inimiga compõem-se: contra um Elfo fortificado com forte contraespionagem, até um excelente Mestre de Espiões traz pouco mais do que palpites. Faz espionagem antes de empenhares um exército, e nunca apostes uma campanha num único relatório de nível baixo.*

**8.8.5 Interferência de Contraespionagem (Counter-Espionage Interference)**

Os reinos defensores acumulam **força de Contraespionagem (Counter-Espionage, CE)** ao atribuir uma personagem ao papel de espião (mestre de espiões) — a interferência de CE é floor(Política do mestre de espiões defensor × 0.5), pelo que um mestre de espiões com Política elevada na defesa é o que cega os agentes que chegam. Quando um relatório de espionagem recebido é processado, o TP mede a percentagem de interferência de CE e aplica uma degradação cumulativa:

|                     |                                                         |
|---------------------|---------------------------------------------------------|
| **CE Interference** | **Effect**                                              |
| \> 0%               | Population estimates are noisier than usual             |
| ≥ 15%               | Site levels and troop counts may be inaccurate          |
| ≥ 20%               | Some military intelligence rows may be missing entirely |
| ≥ 40%               | **Spy burn risk** — the agent may have been neutralised |

> ***Nunca te dizem quem apanhou o teu agente.** Um espião queimado, uma missão perdida na estrada e um alvo que afinal era mar aberto produzem todos o **mesmo** cartão de agente perdido (§2.15); trata o silêncio como informação sobre nada.*

Os efeitos são cumulativos: um relatório a 40% degrada os quatro níveis em simultâneo. O cartão do relatório de espionagem na Página do Jogador (Player Page) mostra a percentagem exata de interferência e os avisos de nível ativos. A penalização do território élfico (§8.8.4) e a interferência de CE acumulam-se de forma independente.

**8.8.6 Ciclo de Vida do Espião (Spy Lifecycle)**

Cada ordem hire_spy é um pedido de informação único, resolvido na Fase 7 — sem unidade persistente no mapa, sem manutenção (upkeep) (§2.15). Cada missão terrestre começa por lançar uma perda de base de min(0.20, 0.05 + 0.015 × dist); um alvo em hexágono de mar perde-se sempre (cobrado, sem relatório); além disso, a interferência de CE no nível de risco de queima (§8.8.5) pode queimar o agente. Os três casos produzem o mesmo cartão genérico de agente perdido.

**8.8.7 Mexericos e Rumores (Gossip & Rumours) (Fase 10)**

Um reino com um **Mestre de Espiões** (o gabinete de espionagem, §7) pode espalhar **um rumor por turno**: um texto livre até 1,000 carateres que chega a **todos os reinos** — o teu, em guerra (war), em paz (peace) e ausentes — como um cartão 🗣 *Rumours spread through the courts*, o último cartão do relatório do turno (Fase 10). **Não tem remetente**: nenhum reino pode saber quem o espalhou, e nada no jogo o rastreia. Só o registo de processamento do GM nomeia o autor.

- **Preço:** round(500 × (1 − Politics / 200)) de ouro, pago quando o rumor se espalha — Política 50 paga 375g, 90 paga 275g, 100 paga 250g, 150 paga 125g. Um reino que não consiga pagar quando chega a Fase 10 não espalha nada e é informado disso.

- **Um Mestre de Espiões atribuído neste turno já serve**: a Fase 10 corre depois das atribuições da Fase 4. Sem Mestre de Espiões, nada se espalha (com cartão).

- **Apenas palavras.** Um rumor não move nenhuma opinião, postura ou recurso; \[CEASEFIRE\] e \[TRIBUTE\] não fazem nada dentro dele. Acreditar ou não nele fica ao critério de quem lê.

- O separador **Spies** da Página do Jogador contém a caixa do rumor, o seu preço e o motivo por que está a cinzento (sem Mestre de Espiões, ouro insuficiente).

> ***▶ Exemplo — um rumor, do princípio ao fim.** O Mestre de Espiões do reino B tem Política 90, por isso um rumor custa round(500 × (1 − 90/200)) = **275g**. B escreve "They say the queen of Belmora keeps a dragon in the cellars" no separador Spies; as 275g saem de imediato (cancela, e voltam). Na Fase 10 todos os reinos — B também — encontram o cartão 🗣 Rumours spread through the courts — "They say the queen…" · Source unknown, em último no seu relatório; só B recebe também Your rumour spread … −275g. Se a tesouraria (treasury) de B tivesse caído abaixo de 275g na Fase 10 (uma fatura de manutenção, uma compra), o rumor não se espalharia e B leria Rumour not spread — Spreading it costs 275g … and the treasury holds …g, sem nada cobrado.*

**PARTE IX — GUIA DE ESTRATÉGIA**

**9.1 Princípios Gerais (General Principles)**

**A economia acumula-se; os exércitos depreciam-se.** Os locais de produção (sites) geram rendimento todos os turnos. Um exército custa manutenção (upkeep) todos os turnos. O jogador que construir mais depressa infraestruturas no início gastará mais do que os adversários a meio do jogo, sem precisar de ganhar todas as batalhas.

**A opinião (opinion) é um multiplicador de imposto.** Um reino com opinião 20 perde 8% do seu imposto (tax) para a agitação, e um com 10 ou menos perde 10%. Um défice de ouro provoca deserção e perda de opinião em simultâneo, criando uma cascata: falta de dinheiro → menos soldados → mais falta de dinheiro. Evita esta espiral.

**As baixas (casualties) seguem o preço.** A fórmula deathFactor = clamp(0.3–1.0, 1.0 − price×(1+veterancy)/1100) (preço = o custo total de recrutamento da unidade em equivalente de ouro) significa que as tropas baratas morrem à percentagem total da batalha, enquanto as unidades mais caras mal sangram — independentemente do que marcha ao lado delas. O poder de ataque não compra sobrevivência; ouro, ferro (×16), cavalos, madeira e experiência compram — a comida nunca.

**O mercado (market) é um estado coletivo.** Os preços movem-se com o volume transacionado por todos os reinos em conjunto — um comerciante isolado mal mexe num mercado grande (§2.11.5). Se conseguires antecipar quando a comida será escassa (depois de eventos de fome atingirem vários reinos), podes lucrar com um posicionamento prévio.

**9.2 Prioridades Económicas por Fase do Turno (Economy Priorities by Turn Phase)**

**Início**: Assegura planície com um povoado (settlement) para quintas (1000g, garantido; uma quinta precisa de uma construção no hexágono e começa a render no turno seguinte ao da sua construção, e a sua colheita é sorteada em cada turno — §3.6.1). A comida da quinta escala com a população do povoado, pelo que as quintas que contam são as das tuas maiores cidades.

**Meio**: Melhorias de Porto (Port). Um Porto Nv3 numa construção de grande população gera um rendimento duplo substancial (ouro + comida). As melhorias são determinísticas mas caras — 10000g (Nv1→2) e 15000g (Nv2→3), além das 5000g do porto — pelo que só se pagam a si próprias quando o povoado tem população real por trás.

**Fim**: As melhorias de Mina (Mine) tornam-se significativas quando a mina assenta numa construção populosa (os mapas de era não fazem crescer um hexágono de montanha vazio — a população é a do povoado, §3.2). Mina Nv3 com 600 de população = 50 + floor(600 × 3 / 20) = 140 ferro/turno. Com várias minas em território Anão, o excedente de ferro permite produção militar direta ou influência no mercado.

**9.3 Estratégia de Facção: Imperial (Faction Strategy: Imperial)**

A vantagem dos Imperiais é o **alcance, não um bónus de dados**. Três coisas são verdade para o Império e para mais ninguém:

- **Recruta em todo o lado.** A tabela de compatibilidade (§2.12) é mútua e o Império é compatível com **todas** as famílias, pelo que um exército Imperial em qualquer construção estrangeira de um amigo pode recrutar o par de duas unidades dessa família — Elfo, Anão, Orc, Bárbaro, Aesir ou Nómada. Um Elfo ou um Nómada consegue-o em três famílias, um Orc em quatro. A expansão Imperial nunca fica sem terreno de recrutamento, seja quem for que construiu a cidade onde se encontra.

- **A Legião defende as suas muralhas.** Os teus exércitos e a milícia rolam **×1.10** a defender os teus próprios povoados FI/POP, além das muralhas (walls) (§4.2). Nada mais no jogo recompensa uma raça por lutar de dentro da sua própria pedra.

- **A escada mais alta.** Vinte degraus, os maiores tetos de população (50,000) e as muralhas mais altas (25,000) do jogo, com os preços mais íngremes no topo (FI17–FI20; os degraus do meio situam-se na faixa Bárbara). Uma sede Imperial crescida é a coisa mais difícil de tomar no mapa — e, com 30% do seu povo em sitiantes, efetivamente só por assalto (§5.8.1).

Não há **bónus de terreno** nem unidade barata: os Pretorianos (Praetorians) (WP 356, 300g+100i+10f+5w) são a segunda infantaria de WP mais alto do jogo, e o ferro torna-os dependentes de minas. A fórmula ponderada de baixas favorece-os — um exército com muitos Pretorianos sobrevive com taxas de perda mais baixas contra defensores de WP elevado. Joga com o Império como a potência que constrói, mantém e guarnece, e que transforma a cidade de cada aliado num terreno de recrutamento.

**9.4 Estratégia de Facção: Bárbaro (Faction Strategy: Barbarian)**

Expansão rápida através de infantaria barata. Raiders (48 WP, 50g) e Berserkers (55 WP, 40g) não têm manutenção em ouro — só drenam comida. Uma estratégia Bárbara inicial pode inundar território rapidamente antes de as outras raças conseguirem massificar unidades de elite.

O risco é o abastecimento de comida — a comida por efetivos (§2.10.4) e o recrutamento rico em comida (Warchief 30f, Wild Archer 20f). Forças grandes precisam de um rendimento agrícola profundo. O bónus de terreno de colinas (×1.15) recompensa os jogadores Bárbaros que posicionam exércitos em colinas para defesa.

Storm Horses (WP 85, 120g + 1 cavalo, 4g de manutenção) é uma unidade montada barata (só os Bedouin a 90g e os Warg Rider a 100g custam menos) — útil para flanquear e para apreensão antes de os adversários construírem contramedidas de cavalaria. Mantém uma reserva de cavalos (mercado ou criação) para os pôr em campo em escala.

**9.5 Estratégia de Facção: Elfo (Faction Strategy: Elf)**

Os exércitos Elfos pagam manutenção apenas em ouro, mas ainda comem comida por efetivos e passam fome sem ela (§2.10.4) — pouca dependência de comida, não imunidade.

O terreno de floresta (×1.30) é o bónus de terreno mais alto do jogo, a par das montanhas Anãs. Defender hexágonos de floresta com pilhas de Ranger (WP 174, sem comida no custo de recrutamento) é extremamente rentável.

A dependência de ferro é o ponto de pressão estratégico. Os jogadores Elfos sem infraestrutura de minas não conseguem construir High Guard (104 de ferro cada) nem Elven Cavalry (55 de ferro cada) em escala. A prospeção em floresta existe, mas é a pior aposta do jogo (5% de probabilidade, limite de Nv1) — o mercado ou a conquista são normalmente o caminho mais barato para o ferro.

**Resistência à informação:** Todos os hexágonos pertencentes a reinos Elfos impõem uma penalização de precisão de um nível aos espiões inimigos (ver §8.8.4). Os mestres de espiões inimigos de alta confiança são degradados para moderada; os de moderada para baixa. Isto torna o território Elfo significativamente mais difícil de reconhecer — uma vantagem em campanhas defensivas em que os adversários dependem de informação para cronometrar os ataques.

**Pondera as tuas presas (prizes).** A marinha Elfa está entre as mais rápidas a flutuar — Moonskiffs e White Ships fazem 3 hexágonos de mar — um ritmo que o casco de 90 mp de qualquer raça consegue igualar, mas só uma frota livre de cascos de 60 mp (só um bando puro de Snekkja Aesir os ultrapassa, com 4, §4.7). Essa velocidade faz dos Elfos uma raça com muito a *perder* com os despojos navais (§2.13.12): um casco de 60 mp capturado (um Cog, uma Galley, uma Tigress) arrasta a frota inteira para 2 hexágonos. Fica com a presa, mas estaciona-a — transfere os cascos lentos para uma frota de segunda linha e mantém os esquadrões de ataque puros.

**9.6 Estratégia de Facção: Orc (Faction Strategy: Orc)**

Os exércitos Orcs crescem sem recrutamento se lhes for dado tempo em terreno de pântano. Um exército que começa com 50 soldados de infantaria e nunca é empenhado em batalha pode chegar a 100+ soldados após muitos turnos por reprodução passiva. Esta mecânica é mais poderosa combinada com unidades de baixo custo (Goblins: 30g, 12f) que se reproduzem livremente.

A comida é a preocupação central dos Orcs. A comida por efetivos (§2.10.4), o recrutamento rico em comida, o crescimento por reprodução e a penalização de fome (starvation) acentuada de 10–20% significam que uma horda Orc que ultrapassa o seu abastecimento de comida colapsa mais depressa do que qualquer outra raça. A infraestrutura agrícola é existencial.

**Alimenta o Waaagh vencendo.** Um vencedor Orc **come os caídos**, e a comida escala com os *efetivos* dos mortos (§2.13.11) — uma batalha grande, sangrenta e decisivamente ganha pode devolver mais comida do que uma quinta rende num turno, pelo que um Orc que continue a ganhar batalhas terrestres consegue sustentar uma horda que só a agricultura não sustentaria. O senão: tens de **ganhar, e ganhar decisivamente** — um empate ou uma derrota não alimenta ninguém, e uma vitória por pouco rende apenas 20% contra 60% de uma decisiva. Por isso escolhe combates que vais esmagar, e festeja entre eles. E não poupes as aldeias: a **milícia** caída também é comida — uma conquista Orc de terra povoada alimenta-se enquanto arde, e até a tua própria gente, caída a defender as tuas muralhas, regressa à despensa.

O evento Waaagh Frenzy (+2 xp_wp a todos os tipos de unidade) é um reforço fixo por tipo de unidade — mais forte em unidades baratas de WP baixo (o ×1.03 de Barbarian Fury Unchained supera-o em qualquer unidade acima de 67 WP).

**Campanhas do Witch King:** Se o GM atribuir um governante Witch King, o reino Orc ganha um comandante permanente com atributos duplicados (Militar até 150, cmdMult ×1.15) que não pode morrer nem ser dispensado. É o maior bónus de comandante possível no jogo. O Witch King não pode liderar uma frota — os reinos Orcs não podem construir nem tripular frotas, aconteça o que acontecer.

**9.7 Estratégia de Facção: Anão (Faction Strategy: Dwarf)**

A economia centrada no ferro é ao mesmo tempo a força e a restrição. Os Anões em montanhas (×1.30) com pilhas de Warrior (WP 118, DEF 12) são excecionalmente difíceis de desalojar. Heartguard (WP 237) e Thunderers (WP 278, ATK 16) são as opções de ataque mais fortes.

O evento Ale Festival (+ouro) e Vein Strike (+ferro) beneficiam ambos de populações grandes — dá prioridade a hexágonos que fazem crescer a população.

**Exploração da forja (Forge exploitation)**: Um exército Anão estacionado num hexágono de forja e sem ordem de movimento ganha +2% xp_wp por cada turno que ali permanece. Isto acumula-se: um exército parado numa forja durante 10 turnos enquanto outros exércitos combatem noutro lado entrará em campo com um WP significativamente mais alto do que um acabado de levantar. Roda os exércitos pelos hexágonos de forja em tempo de paz para construir uma força-núcleo permanentemente superior. O bónus da forja acumula-se com o XP de batalha — um exército que combate, sobrevive e depois descansa numa forja atinge o limite rígido de 3× mais depressa do que qualquer outra raça consegue — e pára aí.

**9.8 Estratégia de Facção: Aesir (Faction Strategy: Aesir)**

Os Aesir são uma raça de infantaria simples em terra e a melhor marinha a flutuar — joga na água ou estarás a jogar com um Bárbaro pior. **Não há bónus de terreno natal nem desconto de movimento** (cada hexágono terrestre custa a base Imperial), e o catálogo é **todo a pé**: sem cavalos para criar ou comprar, sem escala de terreno para cavalaria, sem a taxa de cavalaria de ×0.65 ao tomar muralhas de assalto. A vantagem racial está inteiramente no mar: **×1.05 em cada lançamento de batalha de frota** (atacante ou defensor, mar ou porto — só no lançamento, nunca mostrado em WP), o **único casco de 120 MP** do jogo (uma frota toda de Snekkja faz **4 hexágonos de mar** por turno onde os rivais mais rápidos fazem 3), e o porão de **220 de capacidade** do Busse.

**Mantém os bandos puros.** Uma frota navega à velocidade do seu casco mais lento, pelo que um Longship (90 MP) faz descer um bando de Snekkja para 3 hexágonos e um Busse (60 MP) para 2. Constrói dois tipos de frota e nunca os mistures: bandos de Snekkja (80 homens por casco, 3g de manutenção) para ataque, bloqueio (blockade) e extração na praia; comboios de Busse/Longship para o bando de guerra. A mesma regra governa as presas (§2.13.12) — estaciona um casco de 60 MP capturado na frota lenta. A incursão (Raid) paga ouro mas **declara guerra** (§2.14.3). O desembarque (landing) em si continua a ser **×0.50** na praia e custa **−20 de estado** — ganha primeiro o combate no mar, desembarca sem oposição sempre que possível.

**A madeira é a economia Aesir.** Cada casco custa madeira (Snekkja 45w, Longship 75w, Busse 105w), e a família de construção **FAS** constrói **muralhas de madeira** que acompanham a população um para um (FAS4 muralha de 1,000 por 1,250g; FAS10 muralha de 10,000 por 22,000g) — o incremento de muralha de cada degrau e cada repair_wall são pagos em madeira. As serrações (Lumbermills) só se instalam em **floresta**; um reino Aesir sem floresta vive do mercado (base 5g), de tributo ou de ouro de incursões. Assegura floresta antes de tudo o resto.

**A infantaria é honesta, não barata.** Os Shore Raiders (WP 48, 42g, sem manutenção em ouro) inundam uma costa; os Shield-Karls (WP 110, DEF 10, 16i) mantêm-na; a Jarl's Guard (WP 240, 289g + 32i, 10g de manutenção) ganha-a. A fatura de ferro sobe a pique, e a fórmula de baixas recompensa-o: o preço de ~703 de equivalente de ouro de uma Jarl's Guard dá um deathFactor de cerca de 0.36 onde um Shore Raider sangra a ~0.94. Fica longe de deserto e montanha — os Aesir pagam **16 e 17 de estado por hexágono** ali, a pior taxa de deserto do jogo. Far Raid Returns (+10% de ouro de rendimento, +1.5% de comida da população) e Whale-Road Bounty (+3% de comida da população) escalam com a população, não com o tamanho do exército.

**9.9 Estratégia de Fação: Nómada (Nomad)**

Os Nómadas possuem a areia e mais nada. **Deserto ×1.25** em batalha, **deserto a 30 MP** onde todas as outras raças pagam 60 (um exército Nómada a pé faz 2 hexágonos de deserto por turno, um totalmente montado 3, um invasor 1), **cavalaria Nómada isenta da penalização de ×0.85 da cavalaria no deserto**, e apenas **10 de ESTADO (status) por hexágono de deserto** contra os 14–16 de todos os outros. Uma força composta só por Bedouin/Askari atravessa três hexágonos de deserto por 30 de prontidão e volta à força total (+33/turno de descanso) antes de uma coluna inimiga ter saído de uma única duna. Fora da areia, és o plantel de WP mais baixo do jogo (teto Askari 143) sem qualquer ajuda do terreno — luta onde o mapa diz que se luta.

**A doutrina é a cavalaria pesada, não uma opção.** Um cavaleiro Nómada come **1 de comida por cabeça**, e não os 2 que toda a outra cavalaria paga — cem Askari custam 100 de comida/turno, onde cem Elven Cavalry custam 200. Bedouin (WP 88, 90g + 1 cavalo, 3g de manutenção) e Askari (WP 143, 180g + 1 cavalo, 5g de manutenção) são a cavalaria sustentada mais barata do jogo, desde que o abastecimento de cavalos aguente: cria (§2.9.9) ou compra, porque cada cavaleiro custa um cavalo. Em planície continuam a receber o bónus de terreno aberto de **×1.20**; em floresta, pântano e montanha são penalizados com 0.70/0.60/0.70 como qualquer outro — nunca cavales para dentro de árvores.

**É nas muralhas que o Askari morre.** A regra de assalto da cavalaria aplica **×0.65** a todos os pontos de guerra montados ao tomar de assalto muralhas, criados no deserto ou não. Cerca com Mangonels (250 de dano às muralhas), esfomeia, ou manda Rumat (WP 86, 5i) e Naffatun (WP 50, sem manutenção em ouro) para a brecha, e guarda os cavaleiros para o campo aberto — ou para uma Surtida (Sally) ordenada (§2.13.7). O Rajjala (WP 26, 20g, sem manutenção, deathFactor ~0.97) é milícia com uma lança: um número de corpos para tomadas, nunca uma linha de batalha.

**Os acampamentos Nómadas movem-se** (§2.11.10) — o povo e a paliçada viajam; os locais de produção não. É essa a troca: a mobilidade é a compensação pelas muralhas mais fracas do jogo, e o preço é a mina ou o porto que deixas para trás. Usa-a para perseguir uma fronteira, para tirar um acampamento baixo de uma campanha de conquista lenta, ou para pôr a tua sede onde o inimigo não planeou — nunca para fugir a uma batalha já travada, porque o movimento resolve-se depois do combate.

**Os povoados Nómadas são acampamentos, não castelos.** A família **FNO** tem **dez** degraus de madeira e funda diretamente em **FNO1** — o acampamento de colonos (100 pop, sem muralha, gratuito). Os degraus são baratos e rápidos (FNO2 500 pop por 500g + 100 de madeira; FNO5 2,000 pop por 2,000g; FNO10 15,000 pop por 30,000g — 77,750g e 1,000 de madeira pela escada toda) mas as muralhas nunca passam dos 1,000 pontos, pelo que uma sede Nómada nunca é uma fortaleza: o bónus fica-se perto de ×1.6 e um só golpe de engenho derruba qualquer degrau abaixo do Lv.6. Segura o terreno com cavaleiros e mantém a população da sede elevada — é isso, e não a paliçada, que um assalto tem de desfazer. A madeira vem de uma serração em floresta ou do mercado (base 5g); os hexágonos de deserto não oferecem nenhuma das duas. A população é a verdadeira riqueza do Nómada: as Caravan Tolls (+12% do rendimento) e a Oasis Bloom (+3% de comida da pop) pagam sobre ela, e os hexágonos de deserto permitem prospeção de minas (7%, limite Lv2) que ninguém atravessará a areia para tomar. O recrutamento no estrangeiro é escasso — os Nómadas só recrutam em construções **Imperiais e Bárbaras** (§2.12).

**9.10 Jogo Defensivo (Defensive Play)**

**Prioridade de postura para defesa pura**: em campo aberto Emboscada (Ambush) (×1.40) \> Defensiva (Defensive) = Guarnição (Garrison) (×1.20 — uma Guarnição conta como Defensiva fora de um assalto); atrás das muralhas só a Guarnição (×1.30) se mantém de todo — qualquer outra postura fica fora delas (§5.8.0).

**Uma Emboscada válida mantém-se afastada das muralhas.** Usa-a para obrigar qualquer atacante a vencer um exército oculto em campo aberto antes de chegar às tuas portas — e uma ligação (link) pode levar um emboscador para dentro ou uma guarnição para fora (§5.8.0 Casos E e F). É de uso único: depois de combater fica gasta, pelo que um segundo atacante encontra um exército de campo vulgar (§5.4).

**Só uma Guarnição se mantém atrás das muralhas** (×1.30, fortaleza, milícia — §5.8.0); um exército deixado fora em Defensiva combate primeiro o atacante e, se derrotado, vai para dentro defender o assalto. Uma vez **cercado (besieged)** (§2.13.7) a tua única forma de lutar é uma **Surtida** — em campo aberto, sem bónus de postura e sem muralhas: ordena-a quando o sitiante for fraco o bastante para ser vencido aí; caso contrário, fica atrás das muralhas, e lembra-te de que um cerco que siga o seu curso termina com todos os exércitos do dono lá dentro a render-se.

As posturas são **guardadas** (§5.4), pelo que uma Emboscada registada há turnos continua a manter a zona exterior. Um exército **cercado** só tem à escolha Guarnição e 🚪 Surtida, e não pode pôr uma marcha em fila (§2.13.7).

**O bónus de fortaleza acumula com a postura**. Guarnição atrás de uma muralha de 15,000+ na sede de recrutamento: garrisonWP × 1.30 × 7.10 = garrisonWP × 9.23 antes da milícia (7.10 = a curva r=1 mais a sede de +0.10, com integridade total) — e só enquanto a muralha estiver inteira (§5.6.1). Mantê-la reparada é o ato defensivo de maior alavancagem do jogo.

**Defesa de cerco**: só expulsar o sitiante — uma Surtida vitoriosa, um exército de socorro vindo de fora, ou o ataque de um terceiro — ou o sitiante deixar de pressionar impede a queda automática (§5.8.5); uma Surtida empatada só ganha um turno, e um sitiante demasiado fraco para o limiar de §5.8.1 continua a manter os teus exércitos lá dentro. Os povoados cercados continuam a produzir rendimento enquanto não tiverem caído, por isso esperar só compensa enquanto a ajuda estiver a caminho: o sitiante tem de manter a postura de cerco no hexágono durante todos os 5 turnos (6 contra uma sede de recrutamento).

**9.11 Estratégia Naval (Naval Strategy)**

**Modificador de porto ×1.25**: combate no teu próprio porto ou no de um amigo com uma frota que **começou o turno aí** (§5.9.2), quer a defender quer a atacar um intruso; uma frota que entra a navegar não ganha nada, nem ninguém num porto inimigo ou neutro, pelo que um bloqueador ou ocupante combate sem ele. Mantém uma frota ancorada em casa antes de te comprometeres com operações navais ofensivas.

**Penalização de carga ×0.85**: Uma frota que transporta um exército combate com força reduzida. Ganha o controlo do mar antes de carregar exércitos.

**Bloqueio (Blockade)**: exige guerra e um ancoradouro dentro do porto inimigo (§2.9.3) — um porto indefendido não custa mais do que a navegação até lá, um defendido tem de ser vencido primeiro contra o bónus de porto. Manter um porto inimigo de nível elevado retira uma grande fonte de rendimento sem tomar as suas muralhas de assalto.

**Pilhagem (Raid)**: uma pilhagem leva uma parte do ouro da Fase 1 de um porto estrangeiro, limitada ao que o dono possui, e é sempre um ato de guerra — contra o dono e contra os seus amigos ali atracados (§2.14.3). Uma pilhagem à vela tem de vencer um porto defendido antes de qualquer ouro mudar de mãos, pelo que as pilhagens fáceis são a portos vazios; uma pilhagem de âncora saqueia primeiro e combate depois, e ainda deixa a frota partir no mesmo turno. Cada turno de pilhagem custa à frota 3 de ESTADO e o porto pilhado não dá descanso (§5.10.6), pelo que uma frota que pilha turno após turno se desgasta. Escolhe o momento das pilhagens para guerras que realmente queres, ou guerras já em curso.

**Transporte e desembarque**: A batalha anfíbia é de alto risco — só uma vitória absoluta do atacante toma o hexágono. Um empate é um impasse: o teu exército reembarca com baixas (em muralhas estrangeiras entrincheira-se às portas, §5.7.2) e o defensor mantém-se. Só te comprometas com um desembarque em praia quando tiveres uma vantagem clara de WP; um impasse dispendioso deixa o teu exército reduzido e ainda no mar. Usa os desembarques em praia como segunda frente quando puderes garantir os números, não como uma sondagem de baixo custo.

**Extração em praia — o controlo do mar compra a extração**: uma cabeça de praia não está casada com um porto — uma frota de escolta ancorada junto ao desembarque pode recolher o exército logo no turno seguinte, seja quem for o dono desse terreno (§2.14.6). Isto corta nos dois sentidos: **um cerco costeiro tem fugas a menos que o sitiante traga também poder marítimo** — uma guarnição cercada com um casco seu ancorado ao largo pode embarcar nele e partir no turno seguinte. Nega a extração, não apenas o porto: patrulha ou bloqueia os hexágonos de mar adjacentes, ou o cerco que julgas estar a ganhar esvazia-se debaixo de ti. Orça também a prontidão: cada recolha custa à frota **−15 de ESTADO** e o seu turno (§5.10.6), pelo que uma frota de extração usada repetidamente chegará cansada e lenta à tarefa seguinte.

**9.12 Manipulação Diplomática (Diplomatic Manipulation)**

**Alavancagem de opinião**: trair um aliado mútuo é o maior golpe de opinião individual do jogo (§8.5.3). Se estás prestes a ser eliminado, romper uma aliança para ir para a guerra custa-te mais do que a própria guerra.

**Momento do cessar-fogo**: um \[CEASEFIRE\] mútuo (§2.16.5) faz a paz no mesmo turno, sem qualquer ordem diplomática a aguardar — acorda-o com a outra parte e envia as duas mensagens em conjunto quando precisares de mudar depressa.

**Acumulação de pactos**: Cada pacto mútuo — comercial **ou** de aliança — contribui com um bónus de ouro de 0–2% de forma independente por turno. Três parceiros mútuos dão em média ~3% de ouro de bónus (intervalo de 0–6%). Escala com o rendimento, pelo que os jogadores mais ricos obtêm mais valor absoluto. No máximo 5 parceiros pagam num turno, pelo que o rendimento de pactos tem teto em 10% do imposto + portos — até cinco aliados são um motor económico; para lá de cinco, os aliados servem para a guerra, não para o ouro.

**Difusão da traição de aliança**: Todos os outros reinos recebem uma notificação quando uma aliança é rompida para ir para a guerra. Isto pode ser explorado diplomaticamente — se o teu alvo for universalmente impopular, a difusão da traição será ignorada. Se tens muitos aliados, a difusão pode custar-te mais do que a guerra.

**PARTE X — GLOSSÁRIO E REFERÊNCIA (PART X — GLOSSARY & REFERENCE)**

**10.1 Glossário (Glossary)**

**Aliança (Alliance)** — Postura diplomática, **apenas mútua**: ambos os reinos têm de a declarar, ou fica inerte. Impede o combate mútuo, permite operações conjuntas e paga o bónus de ouro de pacto de 0–2% sem necessidade de fronteira. §2.16.1, §2.9.8.

**Emboscada (Ambush)** — Postura de exército: ×1.40 a defRoll ao defender, válida apenas para um exército Elfo em floresta ou um exército Anão em montanha. Mantém-se fora das suas muralhas, oculta a mapas e espiões, e fica gasta depois de combater. §5.4.

**Varrimento de acampamento (Camp sweep)** — Início da Fase 5: os exércitos já em guerra acampados na mesma zona de um hexágono combatem antes de alguém marchar; nenhum hexágono muda de mãos, um perdedor cercado fica dentro das suas muralhas, e o perdedor do dono ou de um amigo que esteja fora das muralhas vai para dentro em Guarnição. §2.13.5.

**Choque de chegada (Arrival clash)** — Um exército, ou um membro de ligação levado atrás dele, que termine um passo de marcha na zona de um exército com o qual está em guerra ataca de imediato. Idem para as frotas. §5.11, §2.14.7.

**Varrimento de coabitação (Cohabitation sweep)** — Início da Fase 6: as frotas em guerra que partilham um hexágono ou porto combatem antes do movimento; o dono do porto ou um amigo seu defende. Gémeo terrestre: o *varrimento de acampamento*. §2.14.2.

**Pirata (Pirate)** — Não é uma raça: uma marca de subconjunto Bárbaro por reino (§4.3.1). Mecânicas idênticas às dos Bárbaros; ×1.10 de WP em batalha de frotas, a postura de frota Caça (Hunt) (§2.14.9), escudos/arte/títulos próprios, e a etiqueta de raça na UI diz Pirata.

**Exército (Army)** — Uma coleção de pilhas de unidades pertencentes a um reino, que ocupa um único hexágono.

**Assalto (Assault)** — Ordem de combate dirigida a um hexágono com uma construção amuralhada.

**ATK** — Atributo de ataque. Valor de referência; os Pontos de Guerra (War Points) são o verdadeiro valor de combate.

**WP base (Base WP)** — O valor de Pontos de Guerra do plantel de unidades, antes da modificação por experiência.

**Cercado (Besieged) (exército)** — Dentro de muralhas sob um anel de cerco inimigo, a partir do turno seguinte àquele em que o anel é lançado (§2.13.7) e enquanto se mantiver, seja que paz ou aliança for assinada: só Guarnição ou Surtida, sem marcha, embarque livre (§2.13.7).

**Cercado Por (Besieged By)** — O ID do reino registado num hexágono ativamente sob cerco.

**Bloqueio (Blockade)** — Postura de frota: uma frota ancorada dentro de um porto inimigo, em guerra, suprime o seu ouro e comida; guardado enquanto morde, −2 de ESTADO por turno, as frotas ligadas participam. §2.9.3, §2.14.7.

**Planta (Blueprint)** — A taxa fixa de **500 de ouro** que toda a ordem de fundação paga, seja qual for a família ou o nível, além dos colonos e do material da muralha. §2.11.9.

**Espectador (Bystander)** — Um exército num hexágono de batalha que não toma parte — em paz com o atacante e fora da ligação do defensor, ou *retido*; nunca um que esteja dentro de muralhas. Então fica, retira-se ou faz uma última resistência. §5.11, §5.6.

**Capital** — O hexágono que o GM designa como **sede de recrutamento (muster seat)** de um reino (§3.7.3); não é um terreno. Bónus de fortaleza +0.10 e limiar de cerco 5; se for perdida, a sede é sucedida como em §2.13.10.

**Penalização de carga (Cargo Penalty)** — Modificador de combate naval de ×0.85 para uma frota que transporta um exército.

**Construção (Construction)** — Um povoado colocado num hexágono, de uma de oito famílias raciais, num nível da escada dessa família. Transporta **toda** a população do hexágono, a sua muralha e a sua milícia. Um hexágono sem uma é terreno vazio. §3.7.

**Morte de Comandante (Commander Death)** — Perda permanente de uma personagem após o combate (probabilidade = min(0.4, lossPct×0.5)).

**DEF** — Atributo de defesa. Valor de referência.

**Defensiva (Defensive)** — Postura de exército. ×1.20 a defRoll. Nas muralhas fica de fora, em campo aberto (§5.8.0).

**Desembarcar (Disembark)** — Pôr em terra um exército transportado de uma frota para um hexágono de terra.

**Embarcar (Embark)** — Pôr o teu próprio exército a bordo da tua própria frota: um embarque em **porto** só num porto que possuis, um embarque em **praia** a partir de qualquer terra exceto montanha, com a frota ancorada junto a ela. §2.14.5, §2.14.6.

**Frota (Fleet)** — Uma coleção de pilhas de navios pertencentes a um reino num hexágono de mar ou de porto.

**Forja (Forge)** — Local de produção exclusivo dos Anões que o GM coloca no início da campanha numa construção Anã (FDW); os exércitos Anões estacionários aí ganham +2% de xp_wp por turno. Nunca junto a uma mina. §3.6.4, §5.3.2.

**Nevoeiro de Guerra (Fog of War)** — Visibilidade: Total nos hexágonos próprios, Fronteira nos adjacentes, espiados e nos de exércitos/frotas, Recordada nos hexágonos já vistos, Oculta no resto; as forças encontradas numa rota são comunicadas nesse turno. §2.18, §2.19, §2.13.2.

**Legião (Legion)** — A identidade de batalha Imperial: ×1.10 para um exército Imperial e para a milícia que defende, ou faz surtida de, um povoado FI ou POP próprio; nunca como atacante noutro lado, nunca para um aliado. §4.2.

**Bónus de Fortaleza (Fortress Bonus)** — Multiplicador de assalto do defensor pelo **tamanho** da muralha, escalado pela **integridade** da muralha: de ×1.55 (paliçada) a ×7.10 (uma muralha de 15,000+ na sede de recrutamento); uma muralha violada dá ×1.00. §5.6.1.

**Nível de Fundação (Founding Tier)** — O nível em que uma ordem de fundação planta um povoado: Nível 1 para todas as famílias exceto a Orc, que funda num **Nível 0** sem muralha (100 de população) alcançado só por fundação. §2.11.9, §3.7.4.

**Turno de Fundação (Founding Turn) (inércia de combate)** — Uma construção fundada neste turno combate como terreno aberto **sem fortificação** durante o resto desse turno, embora a sua muralha já exista com integridade total. §2.11.9.

**Sede de Recrutamento (Muster Seat)** — O hexágono onde os novos exércitos são recrutados: a capital designada pelo GM ou, se esta for perdida, a maior construção sobrevivente pelo teto de população do seu nível (a contagem de cabeças desempata). §2.13.10, §3.7.3.

**Engenho de Cerco (Siege Engine)** — Unidade por raça (Onager, Trebuchet, War Catapult …) que deita abaixo **250 pontos de muralha** por turno sob uma ordem de cerco; 5 tripulantes cada, só os engenhos tripulados disparam. §5.8.6, §2.12.1.

**Integridade da Muralha (Wall Integrity)** — A muralha atual de uma construção como fração do máximo do seu nível. Escala continuamente o bónus de fortaleza e a penalização do atacante; a 0 o povoado fica **violado** e combate como se não tivesse muralhas. §3.7.2.

**Movimento de acampamento (Camp move)** — Um reino Nómada a reinstalar um acampamento FNO até 2 hexágonos em terra própria, por 1,000g, no fim do turno; o acampamento descansa depois 6 turnos. §2.11.10.

**Material da Muralha (Wall Material)** — A pedra ou madeira de que as muralhas de uma construção são feitas, fixada pela sua **família** (madeira para Aesir, Orc e Nómada, pedra para as restantes) — não pela raça do dono. §2.11.7.

**Guarnição (Garrison)** — A única postura de exército atrás de muralhas: ×1.30 a defRoll contra um assalto (×1.20 em campo aberto), com a fortaleza e a milícia; qualquer outra postura fica de fora. §5.8.0, §5.4.

**Estado do GM (GM State)** — O estado de jogo autoritativo mantido e distribuído pelo Processador de Turnos.

**HP** — Pontos de vida (Hit Points). Valor de referência.

**Retido (Held back)** — Cartão para um exército que se põe de lado, sem perder nada, porque o seu reino também ataca nessa batalha (§5.11.1); *retido da surtida* assinala um exército cercado impedido de fazer surtida (§2.13.7); *Army N left X's group* assinala um membro de ligação que saiu em vez de combater um amigo às suas muralhas (§5.11.1).

**Caça (Hunt)** — Postura de frota exclusiva de Piratas: ataca uma frota mais fraca não aliada que encontre sem declarar guerra; a frota perde ESTADO enquanto caça (§2.14.9).

**Iniciativa (Initiative)** — Multiplicador por lançamento para o atacante: 1.05–1.10. Representa a vantagem do primeiro movimento.

**Ferro (Iron)** — Recurso. Usado na produção de unidades/navios e em alguma manutenção.

**Ligação (Link)** — Uma ordem permanente que une até 3 exércitos no mesmo local sob um líder: os membros movem-se, adotam a sua postura e mantêm-se na sua zona. §5.11.

**Suserano (Liege)** — Um reino que detém um ou mais vassalos (§2.16.4).

**Milícia (Militia)** — Defensores automáticos levantados da população de uma construção. floor(pop × 0.05) unidades (5% da população) valendo cada uma 20 WP, pelo que o WP da milícia ≈ a população.

**Montado (Mounted)** — Tipo de unidade. Consome 2 de comida/turno (unidades a pé 1); os montados Nómadas comem 1.

**ODD-R** — O sistema de coordenadas da grelha de hexágonos usado pelo TREVASXXI.

**Opinião (Opinion)** — Métrica interna de popularidade (0–100, por omissão 90). Afeta o rendimento do imposto; a taxa de imposto que mantiveres move-a todos os turnos (§2.9.13).

**Opção A (Option A)** — A arquitetura de reposição de estado: o TP descarta todo o estado submetido pelos jogadores antes de processar; um reino sem estado guardado é verificado e reconstruído (§2.5).

**Paz (Peace)** — Postura diplomática por omissão. Sem combate, sem bónus.

**Fase (Phase)** — Um passo nomeado na sequência do turno.

**População (Population)** — Contagem de habitantes por hexágono. Cresce 1–3%/turno. Determina o imposto, o rendimento dos locais de produção e a milícia.

**Modificador de Porto (Port Modifier)** — Bónus naval de ×1.25, atacante ou defensor, para uma frota num porto **amigo** (próprio, aliado mútuo, suserano ou vassalo) que começou o turno aí; ×1.00 caso contrário. §5.9.2.

**Pilhagem (Raid)** — Postura de frota, por turno: saqueia o porto estrangeiro em que se encontra e todos os portos estrangeiros em que a sua viagem entra; sempre um ato de guerra; −3 de ESTADO num turno em que saqueia. §2.14.3, §5.10.6. **Avistamentos de rota (Route sightings)** — Quando o teu exército ou frota entra num hexágono onde está uma força estrangeira, ambos os lados são informados, mesmo que terminem o turno fora de vista. Avistamentos de rota, §2.13.2 e §2.14.1.

**Surtida (Sally)** — Postura por turno de um exército **cercado**: com todos os outros exércitos cercados que a ordenem, combate os sitiantes em campo aberto na Pré-Fase 3 (§2.13.7). Ninguém faz surtida sem ordem.

**Colonos (Settlers)** — As **100 pessoas** que uma ordem de fundação faz marchar da sede de recrutamento. A sede tem de ter **300** no momento do processamento; uma sede cujo teto seja inferior a 300 nunca pode fundar até ser melhorada. §2.11.9.

**Progresso de Cerco (Siege Progress)** — Contador num hexágono cercado. Aumenta 1 por cada turno em que o anel é pressionado — um reino sitiante por hexágono (§5.8.2).

**Limiar de Cerco (Siege Threshold)** — 4 para uma construção amuralhada vulgar, 5 para a sede de recrutamento. O hexágono cai quando o progresso excede estritamente este valor. Uma construção sem muralha não pode ser cercada de todo.

**Despojos de Guerra (Spoils of War)** — Ferro e cavalos (e comida Orc) recuperados dos caídos após uma batalha terrestre vencida: 20–60% do custo de construção conforme a margem, 60–80% de uma guarnição que se rendeu; nenhuns no mar. §2.13.11.

**Navios Presa (Prize Ships)** — Cascos tirados dos navios que o perdedor perdeu numa batalha naval vencida: cada um é capturado com um lançamento de d6 de 1–4, afundado com 5–6; mantêm os seus atributos e juntam-se com tripulações verdes. §2.13.12.

**Postura (Stance)** — Estatuto diplomático (paz/guerra/aliança/comércio) ou postura de exército.

**Comércio (Trade)** — Postura diplomática, apenas mútua, que **exige uma fronteira comum**: paga o bónus de ouro de pacto de 0–2% por parceiro por turno só enquanto os dois reinos ainda confinarem. §2.16.1, §2.9.8.

**Processador de Turnos (Turn Processor)** — A aplicação autoritativa do GM que resolve todas as ordens.

**Manutenção (Upkeep)** — Custo de recursos por unidade/navio pago na Fase 2.

**Variância (Variance)** — O multiplicador de sorte 0.90 + rand×0.20 aplicado a todos os lançamentos de combate, a ambos os lados, de forma independente (intervalo 0.90–1.10; BATTLE_VARIANCE = 0.10, ±10 %).

**Vassalo (Vassal)** — Um reino que paga tributo a um suserano, em aliança com ele enquanto o vínculo durar: uma guerra entre os dois termina-o (§2.16.4).

**Pontos de Guerra (War Points) (WP)** — O único valor de combate usado em todos os lançamentos.

**Baixas Ponderadas (Weighted Casualties)** — Fórmula pela qual as unidades mais fortes dentro de um exército morrem proporcionalmente menos.

**xp_wp** — Os Pontos de Guerra com experiência atuais de uma pilha de unidades. Começa no WP base; cresce com o combate.

**10.2 Referência Completa das Fórmulas de Combate (Full Combat Formula Reference)**

**Batalha de Campo (Field Battle):**

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (BATTLE_VARIANCE = 0.10 → ±10 %, independente por lançamento)

cmdMult = 1 + military/1000

attRoll = attWP × status × attTerrainMult × attCavTerrainScale × initiative × attCmdMult × variance

defRoll = defWP × status × defTerrainMult × defCavTerrainScale × defStanceMod × defCmdMult × legion × variance

(cavTerrainScale: a parte de WP montados de cada lado, escalada pelo terreno, §5.5; a postura de guarnição conta aqui como defensiva ×1.20)

Resultado: attRoll \> defRoll×1.2 → att vence; defRoll \> attRoll×1.2 → def vence; caso contrário, empate

Att vence: attLoss=0.10/ratio; defLoss=softLossPct(ratio)

Empate: attLoss=defLoss=0.06+rand×0.06

Def vence: defLoss=0.10/ratio; attLoss=softLossPct(ratio)

softLossPct(r): base=min(0.50, 0.12+0.18×ln r); floored=max(base, min(0.60, 0.12×r)) (piso de dano)

r≤10 → floored; r\>10 → max(floored, min(1.0, 0.50+0.50×(r−10)/15)) (rampa de aniquilação; 1.0 a 25:1)

(destruído apenas quando não há hexágono de retirada — §5.5.6)

**Assalto (Assault):**

militiaWP = floor(pop × 0.05) × 20

integrity = wall_hp / wallMax

fortressBase = max(1.5 + 1.5×r, 1 + 6×r), r = min(1, wallMax/15000) (+0.10 sede de recrutamento)

fortressBonus = 1 + (fortressBase − 1) × integrity // 1.00 quando em brecha ou sem muralhas

attPenalty = 1 − 0.15 × integrity // 0.85 intacta … 1.00 em brecha

attRoll = attWP × status × attTerrainMult × attCavAssaultScale × attPenalty × initiative × attCmdMult × variance

defRoll = (garrisonWP × status × defStanceMod × defCavTerrainScale + militiaWP) × fortressBonus × defTerrainMult × defCmdMult × legion × variance

(legion = 1.10 para um proprietário Imperial de um povoado FI/POP, §4.2 — sobre o defensor em todos os resolvedores, e sobre o ATACANTE apenas quando o atacante é o proprietário a fazer uma surtida)

(attCavAssaultScale: parte de WP montados do atacante ×0.65; defCavTerrainScale como em campo, §5.5)

Att vence: attLoss=0.15/ratio; defLoss=ratio≥5?1.0:min(0.95,0.25×ratio)

Empate: attLoss=defLoss=0.10+rand×0.08

Def vence: defLoss=0.12/ratio; attLoss=ratio≥5?1.0:min(0.95,0.30×ratio)

**Batalha Anfíbia (Amphibious Battle):**

attRoll = attWP × status × 0.50 × initiative × attCmdMult × variance

defRoll = defWP × status × defStanceMod × defCmdMult × legion × variance

(sem multiplicador de terreno; empate = impasse, o atacante volta a embarcar — entrincheira-se em muralhas estrangeiras)

Att vence: attLoss=0.10/ratio; defLoss=softLossPct(ratio) (a mesma curva suave que em campo, piso e rampa incluídos)

Empate: attLoss=0.08+rand×0.06; defLoss=0.05+rand×0.05

Def vence: defLoss=0.10/ratio; attLoss=softLossPct(ratio)

**Batalha Naval (Naval Battle):**

portMod = 1.25 por frota, atacante ou defensor, num porto AMIGO (próprio / aliado / suserano / vassalo) onde começou o turno, caso contrário 1.0

cargoMod = 0.85 se transportar um exército, caso contrário 1.0

attWP = fleetPower × fleetStatus (o ESTADO de cada lado, §5.10 — aplicado aqui, uma só vez)

attRoll = attWP × portMod × initiative × attCmdMult × attCargoMod × attRaceMod × variance

defRoll = defWP × portMod × defCmdMult × defCargoMod × defRaceMod × variance

Att vence: attLoss=0.10/ratio; defLoss=softLossPct(ratio, sea ramp) (a curva de campo até 5:1, depois a rampa própria do mar)

Empate: attLoss=defLoss=0.06+rand×0.06

Def vence: defLoss=0.10/ratio; attLoss=softLossPct(ratio, sea ramp)

softLossPct(r, sea ramp): r≤5 → floored (como em campo); r\>5 → max(floored, min(1.0, 0.60+0.40×(r−5)/5)) (1.0 a 10:1)

(a armadura do perdedor dissolve-se no mesmo calendário de 5:1 → 10:1; mínimo de um casco; uma aniquilação total a 10:1 passa pelo desvio ≥1.0 — ver §5.9.3)

**Baixas Ponderadas (Weighted Casualties):**

price (g-eq) = gold + iron×12 + horses×20 + wood×5 (equipamento; as rações não compram nada)

deathFactor = clamp(0.3 … 1.0, 1.0 − price × (1 + max(0, xp_wp/baseWP − 1)) / 1100)

rawLoss = count × lossPct × deathFactor

loss = round(rawLoss)

(se lossPct≥1.0: o exército inteiro é aniquilado, distribuição ignorada — rácios de assalto ≥ 5 chegam lá diretamente; campo, anfíbia e apreensão de milícia chegam lá a 25:1 através da rampa de aniquilação e ficam no limite do piso de dano de 0.60 abaixo de 10:1)

**Baixas Ponderadas Navais (Naval Weighted Casualties):**

price (g-eq) = gold + iron×12 + horses×20 + wood×5 (equipamento; as rações não compram nada)

deathFactor = clamp(0.20 … 1.5, 0.9 − price × (1 + max(0, xp_wp/baseWP − 1)) / 4900)

rawLoss = count × lossPct × deathFactor

loss = round(rawLoss)

(o desvio de aniquilação ≥1.0 é atingido no mar a 10:1, através da rampa de 5:1 → 10:1 do mar; acima de 5:1 deathFactor → df + (1 − df) × (r − 5)/5)

**Morte do Comandante (Commander Death):**

deathChance = min(0.4, lossPct × 0.5)

**Ganho de XP (XP Gain):**

roll = 1 + (0.03 + rand×0.02) × clamp(0, 1, oppFactor) (×1.03 a ×1.05 com oposição total)

cap = baseWP × 3

new = min(cap, round(xp_wp × roll))

**10.3 Referência Completa das Fórmulas de Rendimento (Full Income Formula Reference)**

terrainGold = 0

terrainFood = plainsWithoutSiteCount × 1

farmFood = Σ max(1, floor(pop × rate)) por quinta povoada; rate: SORTEADO por quinta por turno — Lv1 \[0.05,0.25\], Lv2 \[0.20,0.50\], Lv3 \[0.40,0.80\] (§2.9.4)

mineIron = Σ base\[level\] + floor(pop × siteLevel / 20); base: Lv1=10, Lv2=20, Lv3=50

portGold = Σ floor(pop × goldMult); goldMult: Lv1=0.20, Lv2=0.40, Lv3=0.60

portFood = Σ floor(pop × foodRate); foodRate: SORTEADO por porto por turno a QUALQUER nível — Lv1 \[0,0.05\], Lv2 \[0,0.10\], Lv3 \[0,0.15\]; um 0 paga 0

× bracketFactor por porto: ordenar os portos por ouro DESC; factor = max(0, 1 − floor((rank−1)/5) × 0.10)

(os portos bloqueados contribuem com 0 mas mantêm o seu lugar na classificação)

forgeXP = +2% (fixo) para xp_wp da unidade (exércitos Anões, estacionários, no hexágono da forja, no fim do turno)

rawTax = floor(totalPop × taxRate / 100)

penaltyPct = opinion\<=10?10 : opinion\<=20?8 : opinion\<=30?6 : opinion\<=40?4 : opinion\<=50?2 : 0 (TP_TAX_PENALTY_BANDS, opinião no início do turno)

netTax = max(0, rawTax − floor(rawTax × penaltyPct / 100))

opinion += (TP_TAX_OPINION_NEUTRAL − taxRate) × TP_TAX_OPINION_PER_POINT (logo após o imposto, mantida entre 0–100; uma tax_change aplica-se depois disto)

baseGold = netTax + portGold

treasGold = floor(netTax × economics × 0.2 / 100)

farmBonus = floor((farmFood+portFood) × management × 0.2 / 100)

mineBonus = floor(mineIron × management × 0.2 / 100)

portBonus = floor(portGold × management × 0.2 / 100)

tradeBonus = Σ por parceiro de pacto pagante: floor(baseGold × pct / 100)

o pacto paga se: aliança mútua (não é preciso fronteira), ou comércio mútuo / comércio+aliança misto com fronteira partilhada

onde pct = floor(rand×3) (0, 1 ou 2% — em alguns turnos um pacto não paga nada)

totalGold = baseGold + treasGold + portBonus + tradeBonus

totalFood = terrainFood + farmFood + portFood + farmBonus

totalIron = mineIron + mineBonus

totalWood = lumberWood + lumberBonus (serrações em hexágonos de floresta)

totalStone = quarryStone + quarryBonus (pedreiras em planície/colinas/montanha)

O tributo de vassalo é deduzido de totalGold após o cálculo: floor(tributeBase × tributeRate / 100).

**10.4 Referência de Eventos Aleatórios (Random Events Reference)**

Não existem eventos aleatórios (§2.17).

**10.5 Referência Rápida de Terreno (Terrain Quick Reference)**

**Cidade e Capital não são terrenos** — o povoado é uma construção colocada *sobre* um terreno (§3.7), e o terreno não tem população própria.

|             |                          |               |                  |                                                                         |
|-------------|--------------------------|---------------|------------------|-------------------------------------------------------------------------|
| **Terreno** | **População**            | **Comida/Turno** | **Bónus de Combate** | **Locais permitidos**                                               |
| Planície    | Apenas de uma construção | +1f (sem local) | —               | Quinta, Mina (7%), Porto, Pedreira                                      |
| Colinas     | Apenas de uma construção | —             | Bárbaro ×1.15    | Mina (15%), Pedreira                                                    |
| Floresta    | Apenas de uma construção | —             | Elfo ×1.30       | Mina (5%), Serração, **Porto (apenas Elfo, costeiro, construção Élfica)** |
| Montanha    | Apenas de uma construção | —             | Anão ×1.30       | Mina (25%), Pedreira                                                    |
| Pântano     | Apenas de uma construção | —             | Orc ×1.20        | —                                                                       |
| Deserto     | Apenas de uma construção | —             | Nómada ×1.25     | Mina (7%)                                                               |
| Mar         | Nenhuma                  | —             | —                | —                                                                       |

**Imperial e Aesir não têm bónus de terreno terrestre** (o bónus Aesir é naval — §5.9; o bónus Imperial depende da construção — a Legião, §4.2). As unidades montadas escalam ainda com o terreno — ver §3.5.1.

A força da milícia e da apreensão provém da **população da construção**, não do terreno (§3.8). Um hexágono vazio não cria qualquer milícia, seja qual for o seu terreno.

**10.6 Referência Rápida da Sequência de Turno (Turn Sequence Quick Reference)**

Pré-Fase 1 Opção A Reposição de Estado — o TP descarta o estado do jogador, usa gmState

Pré-Fase 2 Criar/Dissolver/Embarcar reaplicados

Pré-Fase 2b Recrutamento (§2.6a) — pago antes do rendimento; pop da população ANTERIOR ao crescimento (limite de 5% próprios / 1% aliados); engenhos construídos. Os recrutas combatem em todas as batalhas abaixo.

Pré-Fase 3 Cerco e Assalto — exércitos cercados fixos (marcha recusada, apenas Guarnição/Surtida); primeiro combatem-se as surtidas ordenadas (depois de os membros da ligação amigos do proprietário abandonarem um grupo hostil, §5.11.1 regra 3); depois os sitiadores ESTACIONÁRIOS avançam — um com um exército não amigo seu (um neutro incluído) acampado no exterior combate-o em vez disso e não faz progresso nesse turno; as posturas de Assalto combatem os exércitos no exterior e depois tomam de assalto (tudo antes do rendimento)

Pré-Fase 4 Queda Automática do Cerco — hexágonos com progresso \> limiar são transferidos

Fase 1 Crescimento da População (1–3% por hexágono)

\+ Rendimento de terreno (planície +1f; sem ouro de terreno)

\+ Verificação de supressão por bloqueio

\+ Rendimento de locais (quintas→comida, minas→ferro, portos→ouro+comida, serrações→madeira, pedreiras→pedra)

\+ Imposto sobre a população (taxRate%, penalização de opinião aplicada), depois a opinião move-se pela taxa cobrada (§2.9.13)

\+ Bónus de personagens (tesoureiro, mestres, portos)

\+ Bónus de pactos comerciais/de aliança (0–2% por parceiro mútuo)

\+ Criação de cavalos (1–3%, + os pontos de um Mestre dos Cavalos)

\+ Reprodução Orc (5–7% de infantaria por exército se infantaria≥10 e em pântano)

\+ Tributo de vassalo deduzido/pago

\+ Alteração da taxa de imposto (nova taxa no turno seguinte; a alteração em si não move a opinião)

\+ Guerras de ligação por bloqueio — declaradas após a Fase 1 de todos os reinos (§2.14.7)

Fase 2 Manutenção em ouro deduzida → défice: 5–15% de deserção (arredondado para baixo por pilha — nunca o último soldado), opinião −5 a −12

\+ Manutenção em ferro deduzida (sem consequência em caso de falta)

\+ Consumo de comida (infantaria 1, montados 2; montados Nómadas 1)

→ Fome se houver escassez: Orc 10–20%, os outros 3–10%

Fase 3 Ordens de compra/venda de mercado executadas PRIMEIRO, reino a reino (uma venda paga as construções deste turno)

\+ Ordens de construir/melhorar/fundar/mover acampamento processadas

\+ Ajuste do preço de mercado (volume líquido transacionado vs profundidade, ±15% por turno)

Fase 4 Navios e Contratação — construir navios (frota atracada num porto PRÓPRIO; tripulação da pop do porto)

\+ Contratar (1000g por defeito) / atribuir / dispensar personagens

Fase 5 Varrimento de acampamento: exércitos em guerra acampados numa zona de um hexágono combatem primeiro (§2.13.5)

Fase 5 Ordens de movimento de exércitos classificadas por ESTADO (o mais alto primeiro; aleatório entre empates exatos)

\+ Movimento hexágono a hexágono: apreensão (disputa de WP da milícia da população) / batalha de campo / assalto / acampamento de Marcha de Cerco (inicia o cerco; o anel fecha-se de imediato se for suficientemente forte, progresso a partir do turno seguinte)

\+ Declaração automática de guerra ao entrar num hexágono inimigo

\+ Os vencedores de uma batalha terrestre decisiva reclamam os espólios — ferro/cavalos (Orc: +comida dos caídos), §2.13.11

Fase 6 Ataques de âncora: frotas em postura de Pilhagem atracadas num porto estrangeiro pilham-no (§2.14.3)

\+ Varrimento de coabitação — frotas em guerra que partilham um hexágono combatem antes do movimento (§2.14.2); o proprietário do porto ou o seu amigo defende, ×1.25 apenas se começou o turno lá; uma frota nova sem cascos é afundada

\+ Ordens de movimento de frotas classificadas por ESTADO (o mais alto primeiro; aleatório entre empates exatos)

\+ Movimento hexágono a hexágono: entrada em porto (qualquer porto) / combate naval — uma vitória CLARA prossegue a navegação, um empate ou derrota termina a viagem

\+ Pilhagem à vela, em cada porto estrangeiro em que entra: guerra, combate no porto, pilhagem apenas numa vitória CLARA, prosseguir a navegação (§2.14.3)

\+ Desembarque (DEPOIS de todo o movimento de frotas): os desembarques com a penalização de praia de ×0.50

podem tomar um hexágono costeiro — a conquista terrestre também acontece aqui (§2.14.6)

\+ Os vencedores de uma batalha naval capturam navios-presa — cada casco que o perdedor perdeu no combate é capturado com um 1–4 num d6, §2.13.12

Fase 7 Relatórios de informações de espiões gerados (posições pós-Fase 5)

Fase 8 Ordens de diplomacia (a guerra vence tudo; sem paz/aliança/comércio para com um reino com que foste à guerra neste turno, por qualquer via)

Fase 8 ·V Vassalagem — os juramentos do turno anterior respondidos (vassal_offer_reply), depois leave_vassalage, depois become_vassal (uma oferta), depois set_vassal_tribute; uma guerra suserano–vassalo já terminou o vínculo (corre ANTES das mensagens)

Fase 8 ·M Mensagens (até 3; \[CEASEFIRE\] paz automática se mútua; \[TRIBUTE: n res\], §2.8.3)

Fim do turno Transferências de Recursos — send_resource + \[TRIBUTE\] (apenas excedente, aplicado após todas as despesas)

Aleatório 40% por reino; 1 evento no máximo; pool de guerra ou paz + pool de raça

Varrimentos Varrimentos de forças vazias e de integridade de ligações

Forja Exércitos Anões estacionados num local de Forja ganham XP

XP Pers. Experiência de Personagens (§7.10)

Relatórios Gerados com nevoeiro aplicado por reino

**10.7 Referência de Ordens (Order Reference)**

Cada ordem que uma Página do Jogador (Player Page) exporta é um objeto no array orders\[\] do ficheiro de ordens, indexado por tipo. Dois tipos de tráfego **não** viajam como tipos de ordem: as transações de mercado seguem em market_orders\[\] (action: buy / sell, com commodity e qty — §2.11.4) e as mensagens seguem em message_orders\[\] (até 3 por turno — §2.16.5). Tudo o resto está na tabela abaixo. Este é um índice de consulta — a mecânica reside nas secções citadas; a coluna da fase usa os nomes do §2.4.

|                      |                                                                                                                                                                           |                                                                                                       |                               |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------|
| **Tipo de ordem**    | **Fase**                                                                                                                                                                  | **Campos principais**                                                                                 | **Ver §**                     |
| create_army          | Pré-Fase 2 (reaplicação de Criar / Dissolver)                                                                                                                             | army_num, label                                                                                       | §2.6, §2.12.1                 |
| disband_army         | Pré-Fase 2                                                                                                                                                                | army_num                                                                                              | §2.6                          |
| disband_units        | Pré-Fase 2                                                                                                                                                                | army_num, unit_id, qty (limitada à pilha; recusada a bordo de uma frota ou abaixo da tripulação de engenhos; sem reembolso) | §2.6                          |
| create_fleet         | Pré-Fase 2                                                                                                                                                                | fleet_num, port                                                                                       | §2.6, §2.14.2                 |
| disband_fleet        | Pré-Fase 2                                                                                                                                                                | fleet_num                                                                                             | §2.6                          |
| disband_ships        | Pré-Fase 2                                                                                                                                                                | fleet_num, ship_id, qty (limitada à pilha; recusada enquanto transporta um exército; sem reembolso)   | §2.6                          |
| link_armies          | Pré-Fase 2 (reaplicação de ligação)                                                                                                                                       | army_num (líder), targets\[\]                                                                         | §5.11                         |
| link_accept          | Pré-Fase 2                                                                                                                                                                | army_num, leader_kingdom_id, leader_army_num                                                          | §5.11                         |
| unlink               | Pré-Fase 2                                                                                                                                                                | army_num                                                                                              | §5.11                         |
| link_fleets          | Pré-Fase 2                                                                                                                                                                | fleet_num (nau-capitânia), targets\[\]                                                                | §2.14.7                       |
| fleet_link_accept    | Pré-Fase 2                                                                                                                                                                | fleet_num, leader_kingdom_id, leader_fleet_num                                                        | §2.14.7                       |
| fleet_unlink         | Pré-Fase 2                                                                                                                                                                | fleet_num                                                                                             | §2.14.7                       |
| embark_army          | Pré-Fase 2 (reaplicação de embarque)                                                                                                                                      | army_num, fleet_num, beach (true = recolha na praia)                                                  | §2.6, §2.14.5, §9.11          |
| set_army_stance      | Lida na Pré-Fase 3 (cerco / assalto / surtida) e no combate da Fase 5                                                                                                     | army_num, stance, siege_target {col,row}                                                              | §5.4, §2.6b, §2.13.6, §2.13.7 |
| set_fleet_stance     | Lida na Fase 1 (bloqueio) e na pré-passagem de pilhagem da Fase 6; um bloqueio efetivo (a frota está dentro de um porto inimigo em guerra) fica guardado na frota até caducar ou ser alterado | fleet_num, stance (sailing / blockade / raid / hunt; hunt é exclusivo de Piratas e guardado como um bloqueio) | §2.9.3, §2.14.3, §2.14.9      |
| tax_change           | Fase 1 (aplicada à taxa do turno seguinte)                                                                                                                                | to (1–10, ±1 por turno)                                                                               | §2.9.13                       |
| build_site           | Fase 3                                                                                                                                                                    | col, row, site_type                                                                                   | §2.11.1                       |
| upgrade_site         | Fase 3                                                                                                                                                                    | col, row, site_type                                                                                   | §2.11.2                       |
| raze_site            | Fase 3                                                                                                                                                                    | col, row                                                                                              | §2.11.6                       |
| upgrade_construction | Fase 3                                                                                                                                                                    | col, row                                                                                              | §2.11.7, §3.7                 |
| repair_wall          | Fase 3                                                                                                                                                                    | col, row                                                                                              | §2.11.8, §3.7.2               |
| found_construction   | Fase 3                                                                                                                                                                    | col, row, family                                                                                      | §2.11.9, §3.7.4               |
| recruit_unit         | Pré-Fase 2b (Recrutamento)                                                                                                                                                | army_num, unit_id, qty                                                                                | §2.6a, §2.12.1                |
| build_ship           | Fase 4                                                                                                                                                                    | fleet_num, ship_id, qty                                                                               | §2.12.3                       |
| hire_character       | Fase 4                                                                                                                                                                    | candidate_id (custo e atributos são da autoridade do TP)                                              | §2.12.4, §7.3                 |
| assign_character     | Fase 4 (após contratações)                                                                                                                                                | char_id, assignment                                                                                   | §7.4                          |
| dismiss_character    | Fase 4                                                                                                                                                                    | char_id                                                                                               | §7.9                          |
| transfer_units       | Fase 4.5                                                                                                                                                                  | from_army_num, to_army_num, units\[\] (ou all: true)                                                  | §2.12b                        |
| split_army           | Fase 4.5 (antes das transferências)                                                                                                                                       | from_army_num, new_army_num (ranhura vazia), units\[\] — novo exército no mesmo hexágono, retido neste turno | §2.12b                        |
| transfer_ships       | Fase 4.6                                                                                                                                                                  | from_fleet_num, to_fleet_num, ships\[\]                                                               | §2.12b                        |
| split_fleet          | Fase 4.6 (antes das transferências)                                                                                                                                       | from_fleet_num, new_fleet_num (ranhura vazia), ships\[\] — nova frota no mesmo hexágono, retida neste turno | §2.12b                        |
| move_army            | Fase 5 (recusada para um exército cercado)                                                                                                                                | army_num, path\[\] of {col,row}                                                                       | §2.13.2, §2.13.7              |
| move_fleet           | Fase 6                                                                                                                                                                    | fleet_num, path\[\] of {col,row}                                                                      | §2.14.1                       |
| disembark_army       | Fase 6 (após todo o movimento de frotas)                                                                                                                                  | army_num, fleet_num, col, row                                                                         | §2.14.6                       |
| hire_spy             | Fase 7                                                                                                                                                                    | col, row (máx. 3 por turno; custo da autoridade do TP)                                                | §2.15, §8.8                   |
| diplomacy            | Fase 8                                                                                                                                                                    | target_id, new_status                                                                                 | §2.16, §8.1–8.3               |
| become_vassal        | Fase 8c (Vassalagem)                                                                                                                                                      | liege_id, tax_rate opcional (1–5, por defeito 3) — uma oferta a que o suserano responde no turno seguinte | §2.16.4, §8.6.1               |
| vassal_offer_reply   | Fase 8c (Vassalagem)                                                                                                                                                      | offer_id, accept (true/false) — a resposta do suserano a um juramento                                 | §2.16.4                       |
| set_vassal_tribute   | Fase 8c                                                                                                                                                                   | vassal_id, rate (1–5)                                                                                 | §8.6.2                        |
| leave_vassalage      | Fase 8c                                                                                                                                                                   | —                                                                                                     | §8.6.3                        |
| send_resource        | Fim do turno (Transferências de Recursos)                                                                                                                                 | to_kingdom_id, commodity, amount                                                                      | §2.8, §6.9                    |
| transfer_hex         | Fim do turno (Transferências de Recursos)                                                                                                                                 | col, row, to_kingdom_id                                                                               | §2.8.1                        |

Qualquer campo não listado aqui que uma página escreva numa ordem (custos, atributos, política do mestre de espiões, chaves com prefixo \_) é ignorado ou removido pelo Processador de Turnos (Turn Processor) — as ordens são autoassinadas, pelo que o servidor recalcula tudo o que pode.

*Toda a mecânica foi obtida diretamente de `turn_processor_V\<N\>.html` e `player_page_V\<N\>.html` atuais (N mais alto). Os valores nos comentários do código não são fiáveis — todos os valores deste manual provêm de atribuições de constantes e lógica de execução reais.*

*Os ícones do mapa "Qaitbay Citadel", "Village", "Greek Temple", "Viking Longhouse", "Goblin Camp" e "Miner" de Delapouite, e "Elven Castle" de Pepijn Poolman, de game-icons.net (https://game-icons.net), licenciados sob CC BY 3.0 (https://creativecommons.org/licenses/by/3.0/) — recoloridos e contornados, e mostrados no mapa e nos cartões do separador Constructions (o mineiro num sinal redondo). A iúrte e a fortaleza anã foram desenhadas para o TREVAS no mesmo estilo.*
