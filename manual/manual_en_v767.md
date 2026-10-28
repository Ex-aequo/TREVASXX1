**PART I — INTRODUCTION**

**1.1 What Is TREVASXXI?**

TREVASXXI is a browser-based asynchronous turn-based strategy game for 2–N players and a Game Master (GM). Players command one of seven asymmetric races competing for territory, resources, and dominance on a hex-grid map. The game has no built-in win condition — victory conditions are defined by the GM for each campaign.

Each turn, players submit orders files to the GM. The GM runs the Turn Processor to resolve all orders simultaneously and distribute one report per kingdom.

**1.2 The Three Applications**

TREVASXXI runs across three separate HTML applications. All run locally in a browser. No server is required for play — but report **signing and encryption** need a secure context (localhost or HTTPS, e.g. python3 -m http.server); opened via file:// the Turn Processor runs with signing unavailable. Files are exchanged as JSON.

|                                                                                                |                 |                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Application**                                                                                | **Who Uses It** | **Purpose**                                                                                                                                                                                                                                                          |
| Map Editor (map_editor_V\<N\>.html, highest N)                                                 | GM only         | Create and edit the campaign map; define hex terrain, sites, starting resources                                                                                                                                                                                      |
| Turn Processor (turn_processor_V\<N\>.html, highest N)                                         | GM only         | Load all submitted player order files; process the full turn; generate reports; the 🗺 **WORLD MAP** shows the whole world as the GM sees it — every kingdom's armies and fleets, nothing hidden — flat or, with **🧊 3D VIEW**, in the same 3D view the players have |
| Player Page (player_page_V\<N\>.html, highest N — the one the GM sent with your latest report) | Each player     | Load personal report; issue orders; export the orders file for submission                                                                                                                                                                                            |

**Always use the Player Page the GM distributed with your latest report.** The page carries a version number. The Turn Processor keeps a **floor** — the oldest page whose orders it takes without a warning (EXPECTED_PP_VERSION) — and raises it whenever an older page would preview a price, yield or rule the engine no longer honours, or offer an order the engine now refuses. A page at or above the floor draws no warning even when a newer one exists, so the rule stays simple: use the latest page the GM sent. A page below the floor still submits — the server is authoritative and the turn processes — but it previews prices, yields and affordability the engine no longer honours. The GM's log flags every orders file that comes from an outdated page, and your own report carries an **"Outdated Player Page"** card naming the version you used and the floor (fetch the latest page, which may be newer than the floor), with the reminder that every order was billed at the engine's rates, not the page's; your report also shows a banner when the page's unit roster is out of date — reload the page the GM sent when either happens. Two copies can share a version number if the GM edited the page in place, so "same number" is not proof; use the file the GM sent last.

The Player Page **Kingdom** tab also has a **🖨 Print Map (PDF)** button: it prints the current map view (whatever you have panned and zoomed to) as a landscape page — choose *Save as PDF* in the browser's print dialog. It is a convenience for record-keeping and sharing and has no effect on gameplay.

**The Army and Navy tabs.** Each tab opens with a **summary table**, one row per army or fleet: what it does this turn (the march and its destination, the stance in force, recruits, an embark, a transfer; for fleets the route, Blockade, Raid or Hunt, ships being built, the landing target), its status, troops (or ships) and power, upkeep per turn, hex and where it stands — fleets also show their **cargo**. A row marked **⚠** needs you, and the header counts them (*⚠ 2 need you*). Click a row to open that card. Under the army table your race's terrain movement costs are listed once.

- **Every card starts folded** to one line: name, place, power, status, upkeep and this turn's order. A folded card that needs you says so on that line — *⚠ no order — stands at ×1.00* (an army that would stand still with no stance), *⚠ no troops — struck at end of turn unless you recruit*, or *⚠ needs you · …* for anything else that asks for a decision: a siege of your walls, a siege of yours that has stalled, lapses or stands at breaking point, an ally's link offer, a Siege March with nowhere to besiege, an army aboard a fleet, status under 34%, a fleet that is not your friend in the same hex, a linked fleet about to be drawn into a war by a blockade. The table row and the card line always agree.

- **▸ Open** and **▾ Fold** on each card. A card you open stays open while you give it orders; ▾ Fold closes it. An army or fleet you raise this turn opens with its roster ready.

- **Inside a card.** The roster opens on **＋ Recruit / build** (fleets: **＋ Build ships** — a fleet at sea shows only *Return to port to build*) as one row per unit; hover a unit's name for its description, and the roster opens by itself while recruits are queued for that army. **Reorganise** (split and transfer) opens on **▸ Split / transfer** and stays open while one is queued. The header shows the army's or fleet's whole upkeep per turn, and the Enlisted Units box shows its share of troops of other peoples (§2.12.1). When Blockade, Raid or Hunt cannot be used, the reasons share one line: *Unavailable here: …*.

> ***▶ Example — reading the Army and Navy tabs.** Hyperborea opens its Army tab at turn 41. The table reads I HOST — ⚠ no order — stands at ×1.00, II HOST and V HOST — Ambush (in force), IV HOST — Garrison (in force), and the header ⚠ 1 needs you; all four cards are folded. A click on I HOST's row opens its card; choosing 🛡 Defensive clears the warning, and the card stays open while the rest of its orders are planned. On the Navy tab, III ARMADA — at 26% status — reads ⚠ needs you · holds at sea: opened, it is sailed home to rest.*

**1.3 How a Campaign Works**

1\. GM creates the map in the Map Editor and exports the initial game state.

2\. GM runs Turn 0 in the Turn Processor to generate initial player reports.

3\. Each player receives their Turn 0 report file and loads it in the Player Page.

4\. Players issue orders and export their orders file. *(A half-made turn can be parked: 💾 TEMP SAVE in the top bar writes a \`draft\_\<Kingdom\>\_turn\<N\>.json\` holding every order queued so far — the first save asks where to put it (pick the folder you keep the Player Page in; Chrome and Edge remember it for every later save and load, other browsers use the Downloads folder); later, load the same turn's report again and 📂 TEMP LOAD that draft to resume exactly where you left off. The draft is not an orders file — SUBMIT TURN still has to go to the GM — and it only fits the kingdom and turn it was saved from. It also restores what your orders had already spent off the map: the population a recruit levied, the crew a ship took and the settlers a founding sent, together with the counters that hold recruitment to one turn's share. On TEMP LOAD the page re-checks the never-coexist rule: a saved march or route belonging to a unit that is a link member is dropped with a notice — a member follows its leader, and a draft from an older page could otherwise plant an uncancellable ghost path on the map. A draft also remembers which processing of the turn its report came from: if the GM processed that turn again and you load the draft on the new report, the page asks first —* This draft was made on ANOTHER processing of Turn N… *— because the draft brings back the old processing's army positions and stocks. Cancel keeps the report you loaded (plan from it); OK loads the draft anyway, and your orders then tell the GM which processing they were planned on)* *(On a phone — held upright or sideways — the page is laid out for a finger: the menu is a strip across the top that stays on screen while you scroll, each tab opens at its top, and text and buttons are finger-sized. The file pickers show every file, so a report your mail app saved under another name (\`report\_….json.txt\`) can still be picked; the page checks the contents and says so when a file is not a report. A computer keeps the usual layout; in a window too narrow for the whole top bar, the bar wraps to a second row, kept to the right, so SUBMIT TURN stays in the top-right corner.)* *(On a phone or tablet the export — and 💾 TEMP SAVE — opens the system share sheet instead of a download. For the orders file (SUBMIT TURN), send it straight to the GM by mail or chat. For a TEMP SAVE draft, pick Save to Files and keep it yourself — it is not for the GM, and 📂 TEMP LOAD opens it from Files. Cancelling the share sends or saves nothing; press the button again. On a touchscreen, tap a greyed-out button (or long-press any button) to read why it is disabled or what it does — the explanations a mouse shows on hover.)*

5\. GM collects all orders files and loads them into the Turn Processor alongside the current game state. *(Every rumour in the loaded orders appears in full in the 🗣 RUMOURS TO REVIEW box above the log, exactly as players will read it, with its author: ✓ PASS or ✕ STRIKE each before processing — a rumour carrying many line breaks or invisible characters is flagged ⚠. ⚙ PROCESS TURN asks first while any rumour is unreviewed; a file the turn will refuse anyway is marked as refused and needs no review (§8.8.7).)* *(Two files from the same kingdom — a player who re-exported — are flagged in the slot list as soon as they are loaded, the one submitted latest marked to keep; the turn will not process until one of them is removed.)* *(Each processing run stamps an id into its \`gm_state\` and every report, and the orders file carries back the id of the report it was planned on. If you process a turn twice, send the reports of the run whose \`gm_state\` you keep: an orders file planned on the other run is flagged in the slot list and in the log — its armies may not be where its orders expect. The turn still processes.)*

6\. GM runs the turn. The TP processes all phases, generates one report per player plus a GM log.

7\. Players load their new report. The cycle repeats from step 4.

> ***▶ Example — a turn processed twice.** The GM processes turn 52 (run 1), notices a late orders file from realm A and processes the turn again with it (run 2). Run 2's reports go out by mistake, but run 1's gm_state_turn52.json is the one kept. A plans turn 53 on run 2's report, where its Army II is still a hex short of the walls; in run 1, the state turn 53 continues from, Army II is already camped at the walls. When the GM loads A's turn-53 orders, A's slot row turns red — ⚠ planned on another processing of last turn (report run T52-…, gm_state run T52-…) — and the log opens with ⚠ Orders From Another Run. The turn can still be processed; the GM decides whether to process it anyway or to send A the right report and ask for new orders. A player who **TEMP LOAD**s a draft made on the other run's report is asked first, because the draft brings back that run's army positions.*

**Option A State Architecture.** The Turn Processor is the sole authority on all game state. When the TP loads player orders files, it immediately replaces all player-submitted state with the GM-authoritative game state before processing any orders. Players cannot gain advantage by manipulating their submitted state file. All order effects are re-applied from scratch against the authoritative state.

**1.3.1 Adding a Kingdom to a Live Campaign (GM)**

A new player can join a campaign that is already running. The Map Editor exports a **GM State Patch** carrying the running state plus the newcomer, and the Turn Processor seeds the newcomer in a *Mid-campaign Starters* phase during the next processing. Do it **between two processings** — after turn N's reports have gone out, before turn N+1 is processed — on the gm_state_turnN.json the TP just wrote (keep an untouched copy).

**Before you start.** Have the player's details (kingdom name, race, colour, player name, email, phone, password) and the lord's name — character names are unique across the whole world, dead ones included. Decide the start: the rolled defaults are gold 2,500–4,000, food 1,500–2,500, iron 100–250, horses 0–20, wood 100–500, stone 100–500, no army and no fleet.

**In the Map Editor**

1\. **Import JSON** → choose gm_state_turnN.json. The editor confirms *"GM State Turn N imported"* and switches to patch mode. Every existing kingdom's capital ★ appears from the campaign's seat marks (the TP never persists capital_hex; the live capital is the hex marked as muster seat) — nothing to re-click. From here on use only the gold **Export GM State Patch** button — the plain *Export JSON* writes a bare map with no armies, resources or diplomacy and would reset the campaign.

2\. On the kingdom panel **add the kingdom**: race, colour, the player fields, and the lord's name. Any kingdom that was not in the imported state is marked a starter automatically at export.

3\. **Paint the realm's hexes.** Every hex you give it needs a **construction** of a family its race can use (§3.7), or it holds no population and yields nothing. Painting over another kingdom's hex transfers it; armies standing there are not moved — check the map first.

4\. **Designate the capital** with the ★ button on the kingdom card, then click the hex. Export refuses a kingdom without one; the patch stamps that hex as the newcomer's muster seat and original capital, so it is the recruiting ground from its first turn. (For existing kingdoms the ★ is display-only — a seat moves only by succession, §2.13.10.)

5\. Optional — **Starter Setup** on the kingdom card: exact starting resources (a blank field keeps the rolled value); starting troops as unitId count lines, seeded as Army I at the capital; starting ships as shipId count lines, seeded as Fleet I at an owned **port** site that must be empty of fleets. The TP validates ids against the race's roster and **drops** unknown ones with a GM-log warning.

6\. **Export GM State Patch.** The editor runs its gates (retired terrains, designated capitals, duplicate lord names, map wrap) and writes gm_state_patch_turnN.json: the whole map with **every per-hex campaign field intact** (population, wall damage, sieges in progress, seat marks, origin claims), every existing kingdom's state untouched, the market prices and campaign flags, and the newcomer flagged as a starter with no state yet. Repainting a hex to a different owner drops the old owner's siege and seat on it but keeps its people. Changing an existing construction's **family or level** gives it a fresh, full wall for the new level — the next GM log shows one *Walls Reseeded* line per such hex, which is expected (an untouched patch shows none). People above the new ceiling stay where they are and simply stop growing (§3.8); **removing** a construction removes its people, and any siege of it, with it — never strip a kingdom's ★ seat hex: the seat stays there regardless (§2.13.10), so its armies would muster on a bare hex with nothing to recruit; the editor warns before exporting. Repainting terrain reshapes everyone's sea lanes and land paths — make sure no fleet or army stands on, or is sailing through, the hexes you change.

**In the Turn Processor**

7\. Load gm_state_patch_turnN.json **in place of** the state file, with the other players' turn N+1 orders as usual. The new kingdom submits nothing this turn.

8\. **Process the turn.** The *Mid-campaign Starters* phase runs first: it seeds the newcomer's state (resources, Army I and Fleet I if defined, its lord plus a three-candidate court pool, opinion 90, tax 5%, at **peace** with everyone — allied to its liege if you set one — and explored memory of its own land) and writes a **starter report**, report\_\<Kingdom\>\_turnN+1_starter.json. The starter flag is consumed: the next processing treats the kingdom as an ordinary one.

9\. Send the newcomer that starter report and the current Player Page. With encrypted reports (§1.2), set the player up first — the starter report is written encrypted like any other.

10\. From turn N+2 the new player submits orders like everyone else.

**Two things that catch GMs.** The patch must be the **current** turn's state — an older one would carry every passive kingdom back in time. And an orders file that names a realm not on the map, or the new kingdom before its starter report has been issued, is refused outright (§2.5), so the new kingdom cannot file orders before its starter report exists.

**1.3.2 Checking a Processed Turn (GM)**

When a player reports something odd, re-run the turn instead of guessing. node tools/replay_turn.mjs \<gm_state_turnN.json\> \<orders-folder\> replays turn **N+1** headlessly with the newest Turn Processor: it loads the state through the Turn Processor's own loader, takes every orders\_\*\_turn\<N+1\>.json in the folder, validates the result and prints each kingdom's cards (--kingdom Name and --grep text narrow the output).

- **Pair the files correctly.** The orders that produced report\_\*\_turnK belong with gm_state_turn\<K-1\>. A mismatch is refused, and the tool lists the turns it does have orders for — never re-label an orders file to make it run: that applies the same orders twice over a state that already holds them.

- **It changes nothing.** --out \<new folder\> writes the replayed reports for study only: they are unencrypted, rolled with fresh dice and carry no player contact details — **never send them to players**.

- **It shows how a turn resolves, not the exact numbers.** Dice are re-rolled and the newest Turn Processor is used, so the numbers your players received will differ.

- **Struck rumours.** The rumours the GM struck in the real run are struck in the replay only when that run's gm_state_turn\<N+1\>.json sits beside the input or is named with --strikes \<file\> — it records which rumour was struck (kingdom and a fingerprint, never the words). Without it every rumour spreads and is charged as filed, and the tool says which case it is.

**1.4 How to Read This Manual**

- floor(x) = round down. ceil(x) = round up. min(a,b) / max(a,b) = minimum/maximum of two values.

- **Capitalized terms** are defined game terms. All terms appear in the Part X Glossary.

- Numeric ranges A–B are inclusive on both ends.

- All values are sourced from the current turn_processor_V\<N\>.html and player_page_V\<N\>.html (highest N in the project folder). Inline code comments in those files are frequently outdated; the actual constant assignments are authoritative.

**1.5 Code of Conduct & Disclaimer**

The text below is the standalone Player Code of Conduct every player receives; it is reproduced here verbatim so the manual is complete on its own. Joining a campaign means accepting it.

Read this before you join. By joining a TREVASXXI campaign you accept everything below.

**1. A hobby project**

TREVASXXI is a free, non-commercial strategy game run by a volunteer Game Master (GM) for a private group of players. Nothing in it has real-world monetary value, and nothing may be bought, sold or traded for money.

**2. Provided "as is"**

The game is under active development. Rules, prices, units and balance may change between campaigns and, when needed, during one. Software bugs, lost or delayed turns, data loss and campaign interruptions can happen. The GM will act in good faith to fix problems but makes no guarantees and accepts no liability for any loss, direct or indirect. The GM may pause, alter or end a campaign at any time.

- When the GM finds that a turn was processed wrongly, the GM may correct the result or process that turn again. That is not a change of ruling; it is putting the game back on its own rules.

**3. Fiction**

All kingdoms, characters, peoples, religions and events are fictional. Some names, titles and cultures draw loosely on history, mythology and fantasy literature. That includes titles such as Sultanate, Emirate or Jarldom, and peoples such as the Aesir or the Imperials. They are used as flavour only and express no view on, or endorsement of, any real culture, faith, nation or person. The game depicts war and conquest as part of its setting; it does not condone violence.

**4. No affiliation**

TREVASXXI is not affiliated with, endorsed by or sponsored by any author, publisher, studio or rights holder whose works may have inspired its setting, names or artwork. All trademarks belong to their owners.

**5. Your data**

- The GM holds your player name, your email address, and the game files you send and receive (orders and turn reports). They are used only to run the campaign.

- Turn reports are sent by email through a third-party delivery service, which processes your address solely to deliver them.

- Other players see your kingdom's name and banner in their own reports, and its position in every ranking — positions only, never your figures.

- Your data is not sold, and it is not shared for any other purpose.

- When a campaign is encrypted, orders and reports are protected with a password. Keep yours private: the GM cannot recover data locked with a lost password.

- You may ask the GM at any time to delete your contact details once you leave a campaign.

**6. Code of Conduct**

Joining a campaign means accepting this Code of Conduct. There is zero tolerance: breaking rule 6.1 or 6.2 means removal from the campaign (6.6). The one exception is a rumour the GM strikes: the GM decides, by how serious it is, what follows (6.6).

\##### 6.1 Respect

- No insults, harassment, threats or discrimination towards any player or the GM, in-game or outside it (chat, email, social media, in person). Rivalry, betrayal and hard diplomacy between kingdoms are part of the game; personal attacks on the person behind a kingdom are not.

- Keep out-of-game disputes out of the game. If something bothers you, tell the GM privately.

- Do not publish another player's messages, reports or screenshots of them without their consent.

- Rumours you spread follow these rules too. The GM sees every rumour before the turn is processed and may strike one that breaks them: a struck rumour does not spread and costs nothing.

\##### 6.2 Fair play

- No cheating or tampering of any kind: editing order files, turn reports, save data or the Player Page; forging or replaying orders; exploiting bugs; using scripts or other tools to write orders or read game files for you; or obtaining another player's reports, messages or password without their consent.

- Found a bug? Report it to the GM — do not use it. Deliberately exploiting a known bug counts as cheating.

- One player, one kingdom. No alternate accounts, and no playing (or giving orders for) someone else's kingdom.

- Do not impersonate another player or the GM, and do not join under someone else's identity. Nicknames are fine.

- Your password is personal. Never share it — not with other players, and not with the GM.

\##### 6.3 Diplomacy

- Diplomacy outside the game (chat, email, calls, in person) is allowed.

- Only the orders the GM receives change the game. A promise made in or outside the game is kept or broken by the players who made it; the GM does not enforce it.

\##### 6.4 Commitment

- Submit orders by the deadline the GM announces. A missed turn is played passively: income, upkeep and your defences still run, but no new orders are carried out.

- Missing turns repeatedly without notice forfeits your kingdom. The GM announces the number of missed turns that forfeits a kingdom before the campaign starts.

- If you need to leave the campaign, tell the GM. A kingdom that is left, forfeited or removed becomes GM-controlled or is removed from the map, at the GM's choice.

\##### 6.5 The GM

- The GM's rulings on rules, results and disputes are final. Ask for clarification, but accept the answer.

- The GM does not play favourites and does not share private information between players.

- The GM may update this document. Players are told of every change, and continuing to play means accepting the updated version.

\##### 6.6 Removal Breaking rule 6.1 or 6.2 means removal from the campaign, at the GM's sole discretion, without warning and without appeal. For a rumour the GM strikes, the GM decides by how serious it is: the strike alone, or removal.

By joining a TREVASXXI campaign you confirm that you have read and agree to this Disclaimer and Code of Conduct.

**PART II — CORE RULES**

**2.1 The Hex Map**

The game is played on an **Odd-R offset hex grid**: a rectangular array of hexagons where odd-numbered rows are shifted half a hex to the right. Hexes are identified by (col, row) coordinates.

Each hex has:

- A **Terrain** type (see Part III)

- An optional **Site** (farm, mine, port, lumbermill, quarry, or forge — see §3.6)

- A **Population** value

- A **Kingdom** owner (or unowned/neutral)

- Optionally: a **Siege Progress** counter and a **Besieged By** kingdom ID

**Moving the map.** Drag the kingdom map with the mouse to move it and turn the wheel to zoom; the **+** / **−** buttons (keys + and -) zoom too, and **Fit to map** (key 0) shows it whole. On a touch screen drag it with one finger and pinch with two to zoom; while your finger is on the map the page does not scroll — scroll from outside it.

**Magnifier lens.** The 🔍 button under **Fit to map** turns on a round lens that follows your cursor across the kingdom map (keyboard: L, and Esc closes it). It does not blow up the picture — it redraws that patch of the map at higher magnification, so terrain, site icons and army numerals stay legible. On a phone it follows your finger. The lens never changes where the map is: switch it off and you are exactly where you were.

**3D view.** The **🧊 3D VIEW** button at the end of the kingdom map's layer row swaps the map for a three-dimensional view of the same ground; press it again to return. On a phone (a screen 700 pixels wide or less) the 3D view fills the whole screen, with the layer row above it. It shows what the flat map shows you — the same fog and remembered hexes, your armies and fleets where your queued orders take them, and the foreign armies and fleets your scouting reveals. A foreign army appears as hooded grey figures under a "?" standard, with a dashed grey rim and a low mist, and a foreign fleet as a ship, each under its realm's shield and name only: their strength stays unknown, as on the flat map. Hover a hex for its details — on a touchscreen, tap it. Drag to rotate, right-drag to pan and scroll to zoom (on a touchscreen: one finger turns the view, two fingers pinch to zoom and pan), or use the on-screen pad (keyboard: WASD or the arrows pan, Q/E rotate, R/F tilt, +/− zoom, H resets the view). The layer buttons filter the 3D view as they filter the flat map: with **Terrain** off the ground keeps its relief and the sea its level but loses its colours, trees and peaks; **Constructions+** shows only the settlements, any siege around them, the kingdoms' borders and the worker signs of your queued settlement orders, each settlement tagged with its construction code. An army is drawn as a company of figures that grows with its soldiers — one figure for one soldier, two for two, and from three soldiers about one figure for every ten (never fewer than three), up to 12 (6 on **Detail: low**) — so it shows size and make-up, not a head count: every kind of troop it holds appears while there is room (siege engines first, as their machines; past the cap the smallest kinds are left out), and an army with no soldiers yet shows only its standard. Every army stands on a plate in its realm's colour, and the plate's rim shows how you stand with that realm: gold for your own armies, green for an ally, vassal or liege, red for a realm at war with you, grey for the rest — foreign name tags also say "ally", "enemy" or "neutral". Your armies show their strength with gold pips on the front of the plate (one under 100 soldiers, two under 500, three under 1,500, four from 1,500) and a taller standard as they grow, and take a formation for their stance this turn: a column along a queued march, a shield line in Defensive, a tight square in Garrison, facing the walls with tents in Siege, a wedge with ladders in Assault; in Ambush they crouch in cover with the standard lowered and no plate, only a dashed gold rim, and only you see it. A queued march is drawn on the ground as a red trail, like the flat map's: from the hex the army leaves, a dot on each hex it passes, an arrowhead into the hex where it is shown. Each people builds and sails in its own style, and a pirate realm's own settlements appear as pirate havens; every fleet sails in its realm's style whatever hulls it holds, and a pirate realm's fleets fly the skull and crossbones. A settlement is drawn with a wall only if it has one. A hex you only remember is drawn dimmed in sepia, as last seen — whatever the **Terrain** button says — and its tooltip says so; a remembered settlement is drawn walled if its level has a wall, and its owner is not remembered. **Labels** hides the name tags, never the worker signs; **Detail: low** turns off shadows and thins forests and companies for slower computers, and a phone or tablet starts on it unless you chose otherwise. A device whose browser cannot run 3D graphics is told so and keeps the flat map; if a phone takes back its graphics memory (switching apps, running low), the view pauses with a message and returns on its own — or close and reopen it. If the view ever stops with an error message, reload the page; the flat map is unaffected. The view is for looking only: orders are given on the flat map and in the other views. Realm shields come from the page's images folder, like the flat map's.

**Fullscreen.** The **⛶ FULLSCREEN** button beside **🧊 3D VIEW** fills the screen with the kingdom map — the layer row and the map, flat or 3D — and you can switch between the two while in fullscreen. Press **✕ EXIT FULLSCREEN** or Esc to return; the flat map keeps its place and zoom. Browsers that cannot show a page element fullscreen, such as Safari on iPhone, do not show the button.

**Construction orders on the map.** A hex holding one of your queued construction orders (§2.11.1: build, upgrade or raze a site, found or upgrade a settlement, repair its wall; one per hex) shows a worker sign — a triangular warning sign with rounded corners: a black worker with a pickaxe on white, inside a red border — in the hex's upper-right corner, where production icons sit, or as a small badge on the lower-left of the production icon already there. A raze shows the sign inverted: a white worker on red, inside a white border. The sign follows the layer of what it builds — **Productions** for a site, **Constructions** or **Constructions+** for a settlement — and appears in the 3D view too. A Nomad camp move shows its route arrow instead. Hover the hex and its tooltip names the order, on the flat map and in the 3D view. The sign stays until you cancel the order or load the next turn's report.

**Settlements on the map.** The **Constructions** layer marks each settlement with its construction code on a small label; **Constructions+** shows only the settlements, each as its people's picture (§2.11.9) with its code beneath.

**2.2 Adjacency**

Each hex has up to six neighbors, computed using ODD-R direction tables that account for row parity. The same adjacency function drives movement path validation, siege adjacency and fog-of-war scouting (a blockade does not use it — it acts on the port the fleet lies in, §2.9.3). Hexes at the map boundary have fewer than six neighbors.

**2.3 Ownership**

A hex belongs to the kingdom whose ID is recorded in its kingdom field. Ownership changes when:

- An army seizes an undefended foreign hex during Phase 5

- An army wins a field battle or assault and the defender is destroyed or retreated (Phase 5)

- A fleet disembarks an army that wins the resulting amphibious battle (Phase 6)

- A siege auto-falls (Pre-Phase, before Phase 1)

Capturing a hex clears any Siege Progress on that hex.

**2.4 The Turn Sequence**

The table below lists every step **in the exact order the Turn Processor runs them** — read it top to bottom and that is the sequence your orders resolve in.

|                     |                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Step**            | **Name**                                                                                                                                                                                                                                                                                                                                                                                      |
| Pre-Phase 1         | Option A State Reset                                                                                                                                                                                                                                                                                                                                                                          |
| Pre-Phase 2         | Create / Disband / Embark Re-apply                                                                                                                                                                                                                                                                                                                                                            |
| Pre-Phase 2b        | Recruitment (soldiers and engines join their armies — before every battle of the turn)                                                                                                                                                                                                                                                                                                        |
| Pre-Phase 3         | Siege & Assault Stance Resolution (besieged armies fixed, ordered sallies fought, then stationary besiegers tick and Assaults storm). **In your report these carry their own ⚙ PRE-PHASE 3 — Sieges & Assaults heading, ahead of PHASE 1 — Income** — they really did happen first, before the turn's money is counted and long before any march, and a city taken here fell before all of it |
| Pre-Phase 4         | Siege Auto-Fall                                                                                                                                                                                                                                                                                                                                                                               |
| Phase 1             | Population Growth & Income                                                                                                                                                                                                                                                                                                                                                                    |
| Phase 2             | Upkeep & Starvation                                                                                                                                                                                                                                                                                                                                                                           |
| Phase 3             | Markets & Construction                                                                                                                                                                                                                                                                                                                                                                        |
| Phase 4             | Ships & Hire (recruitment runs in Pre-Phase 2b)                                                                                                                                                                                                                                                                                                                                               |
| Phase 4.5           | Army Transfers                                                                                                                                                                                                                                                                                                                                                                                |
| Phase 4.6           | Fleet Transfers                                                                                                                                                                                                                                                                                                                                                                               |
| Phase 5             | Army Movement & Land Combat (the camp sweep first: armies at war camped together fight)                                                                                                                                                                                                                                                                                                       |
| Phase 6             | Navy Movement                                                                                                                                                                                                                                                                                                                                                                                 |
| Phase 7             | Spies                                                                                                                                                                                                                                                                                                                                                                                         |
| Phase 8             | Diplomacy (stance changes)                                                                                                                                                                                                                                                                                                                                                                    |
| Phase 8 · Vassalage | last turn's oaths answered (accepted ones sworn), renouncing, then this turn's oaths offered; a war between liege and vassal ends the bond the moment it begins, in any phase (resolves **before** messaging)                                                                                                                                                                                 |
| Phase 8 · Messaging | messages, \[CEASEFIRE\]; each \[TRIBUTE\] leaves here, as it is read (direct / offer / refused by standing, §2.8.3)                                                                                                                                                                                                                                                                           |
| End of turn         | Resource Transfers — last turn's accepted caravan offers are served, then this turn's send_resource (direct / offer / refused by standing, §2.8.3). This turn's \[TRIBUTE\] caravans have already left (Phase 8 · Messaging)                                                                                                                                                                  |
| End of turn         | Empty-force & link-integrity sweeps (whatever empties a force, no soldier-less army or hull-less fleet, and no link across a broken relationship, survives the turn)                                                                                                                                                                                                                          |
| End of turn         | Forge Experience (Dwarf armies)                                                                                                                                                                                                                                                                                                                                                               |
| Phase 10            | Gossip & Rumours — one anonymous rumour per realm with a Spymaster, to every kingdom (§8.8.7)                                                                                                                                                                                                                                                                                                 |
| End of turn         | Character Experience (job-skill turn credit, §7.10)                                                                                                                                                                                                                                                                                                                                           |
| End of turn         | Report Generation                                                                                                                                                                                                                                                                                                                                                                             |

No phase can affect the outcome of a preceding phase in the same turn. Three ordering points routinely surprise players:

- **Recruits are paid before you are paid.** Recruitment (Pre-Phase 2b) is charged from last turn's closing treasury, before this turn's income, tribute and market fills (§2.6a).

- \**Sieges advance in* two different places*. A stationary besieger ticks in Pre-Phase 3*\*, before income, and a tick over the threshold makes the hex fall in Pre-Phase 4 (§2.6b). A march onto a foreign fort storms it in Phase 5 instead (§5.8.0), and a Siege March camps — closing the ring at once if strong enough — and ticks from the next turn.

- **Vassalage resolves before messaging.** Despite the internal "8b/8c" labels, the Turn Processor runs the **vassalage** block *before* the **messaging** block — so a vassal bond (and its forced alliance) is already in effect when a same-turn \[TRIBUTE\] or \[CEASEFIRE\] message is read.

**2.5 Pre-Phase 1: Option A State Reset**

Before any orders are processed, the Turn Processor discards all state data from each player's submitted orders file and replaces it with the corresponding GM-authoritative state. This neutralises any state the player might have manipulated — resources, army unit counts, diplomatic records. Only order lists are read from submitted files.

**A realm with no saved state.** Turn 0 and a mid-campaign start both write each realm's state into the GM's records, so the overwrite above always has something to restore. If a realm reaches a turn without one, the Turn Processor checks the submitted resources against the ranges every realm's starting stores are rolled in — food 1,500–2,500, gold 2,500–4,000, iron 100–250, horses 0–20, wood 100–500, stone 100–500 — moved only by that same file's market orders, the last one per commodity as the market runs them: starting from the top of every range, its sales (no more than that stock) and then its purchases (no more than that gold buys), each order counted only as far as the market's per-order cap (§2.11.4) and only in whole units, give the most an honest file can report. Any figure above that, or below zero, refuses the whole file; a figure below the range is fine, since the Player Page deducts queued spending from the stores it reports. Those market orders are not run again — the stores the file reports already include them — so they make no market card and move no prices. Everything else — armies, fleets, court, applicants, diplomacy, vassalage, spies, offers and caravans — is rebuilt as a realm starts the campaign, and the file's other orders are applied to that — their costs are charged against the reported stores, which the Player Page had already reduced for them, so the GM log flags every realm that takes this path for the GM to give it a saved state. An orders file for a newly added kingdom whose starter report has not been issued yet is refused outright.

**Malformed orders.** An order the Player Page could not have written — a diplomatic stance other than war, peace, alliance or trade, or one aimed at your own realm — is discarded and named in the GM log; the rest of the file stands. Coordinates in any order are read as whole numbers — one that is not a number points at no hex, so its order is refused as "hex not found"; a route or a list of link targets that is not a list counts as empty.

> ***⚠ What this means —** Anything you change in your Player Page that is not expressed as an order is discarded when the GM processes the turn. Hand-editing your resources, troop counts, or diplomacy in the file accomplishes nothing — the TP overwrites all of it with its own records and then re-applies only your order list on top. The upside: you also cannot lose progress to a UI glitch or a bad save, because the GM's copy is the single source of truth. Treat your file as a way to send orders, never as a way to set state.*

**2.6 Pre-Phase 2: Create / Disband / Embark Re-apply**

After Option A resets all state, create-army, disband-army, **dismiss-units** (disband_units, below), disband-fleet, **scuttle-hulls** (disband_ships, below), embark-army, create-fleet and all link/unlink orders (link_armies, link_accept, unlink, link_fleets, fleet_link_accept, fleet_unlink — §5.11) are re-applied to the authoritative state before any other processing. Option A wiped the army/fleet objects that other orders reference; this re-apply step restores them before Phase 1 runs. These order types are not processed again in Phase 4, Phase 5, or Phase 6.

> ***▶ Dismiss units — part of an army, not the whole.** On the Army tab every unit row of an army ashore carries a **✂** button: pick how many of that kind to dismiss (any number up to the whole stack) and they leave the army when the turn is processed, in this same Pre-Phase 2 — so their upkeep and food stop this turn. **Nothing comes back:** no gold, no material, and nobody rejoins a town's population — dismissed soldiers are simply gone, exactly as with a full Disband. Engines may be dismissed too. Two limits, enforced by the Turn Processor and mirrored on the page: **not aboard a fleet** (land first — an embarked army can neither disband nor dismiss, §2.14.6), and **soldiers may not be dismissed below the crew the army's engines need** (5 soldiers per engine, the same ratio the walls volley uses — dismiss engines first). A third: **dismissing your own troops may not leave the army over 20% troops of other peoples** (§2.12.1). The page pre-deducts the units and shows **−N ✂** on the row with an **↩** undo until the orders are sent; the report carries one card per dismissal naming the count, the remainder and the no-refund rule. Only units already on the roster can go: this turn's recruits arrive in Pre-Phase 2b, after dismissals resolve, so the page clamps the count to the standing stock (undo the recruit instead), and while a unit transfer touches the army in the same turn the ✂ is refused — cancel the transfer first (the transfer's own undo restores the army as it was). Dismissing an army's last soldiers empties it, and an empty army does not survive the turn (§2.12): it is struck from the rolls at the end of the turn and its slot freed.*
>
> ***▶ Scuttle hulls — part of a fleet, not the whole.** The naval twin: on the Navy tab every ship row carries a **✂** button — pick how many of that hull to scuttle and they are broken up when the turn is processed, in Pre-Phase 2, so their upkeep stops this turn. **Nothing comes back** (no gold, iron or wood), any hull type may go — prize hulls included — and it works **anywhere**, at sea or in port. The one limit, enforced by the Turn Processor and mirrored on the page, is **cargo room**: a fleet carrying an army may scuttle the hulls it can **spare**, but not the ones its army still needs. The hulls it would keep must still hold that army's tonnage — foot counts 1, mounted counts 2 — and a carrier can never scuttle its way down to no hull at all. It is the same test a **ship transfer** from a loaded fleet uses (§2.14.6). A refusal is **outright, never a silent partial**, and the card names the arithmetic — "Fleet I carries Army I (tonnage 150); the hulls it would keep hold 100." Scuttle fewer, or disembark first. The **whole-fleet Disband** is different and still absolute: it is refused while any army is aboard, by the page **and** by the engine. The page pre-deducts the hulls and shows **−N ✂** with an **↩** undo; the report carries one card per scuttling naming the count, the remainder and the no-refund rule. A linked fleet may scuttle freely (only a whole Disband breaks the link). The same two same-turn limits apply: hulls laid down this turn cannot be scuttled yet (undo the build instead), and a ship transfer touching the fleet blocks the ✂ until it is cancelled. Scuttling the last hull empties the fleet, and an empty fleet does not survive the turn (§2.12).*

**Fleet creation rejection**: a create_fleet order is rejected at this step if the kingdom is **Orc or Dwarf** (race gate, below), if the target is **not a port the kingdom owns** at the start of the turn, if the kingdom already fields **5 fleets** (the kingdom-wide cap, §2.14.2), or the port already holds **3 fleets in any non-warring mix** — the co-location cap (§2.14.2), which is a PER-HEX limit and stays at 3 even though a kingdom may own five. **A fleet raised this turn holds its berth from the moment it is commissioned, hulls or not** — you cannot raise a fourth at the same port in the same turn, exactly as a fourth army cannot be raised on a full muster hex. A **neutral** or **allied** fleet docked at your port does **not** block you — it merely occupies a room slot on the same cap your own fleets stack against. **Neither does an enemy one**: the new fleet is commissioned and fights it as the port's defender in the Phase 6 cohabitation sweep, before any fleet moves, with whatever hulls were built into it that turn — at ×1.00, since the port bonus belongs only to a fleet that began the turn there (§5.9.2); with no hulls it is scuttled on the slipway (§2.14.2). When rejected, the fleet is not commissioned, no resources are spent, and the player receives a blocked notification naming which case applied. The Player Page offers only ports you own, refuses a port whose stack is full, and marks a port holding an **enemy** fleet as a fight rather than a block (*"your new fleet fights it this turn"*); it works from last-turn fog data and cannot see a fleet that arrives the same turn — the Turn Processor's stack check catches those.

**Race restriction**: Orc and Dwarf kingdoms cannot field fleets. create_fleet and build_ship orders from those races are rejected by the Turn Processor, and the Navy section of the Player Page is replaced with a "not available" notice.

**2.6a Pre-Phase 2b: Recruitment**

**Unit recruitment resolves here**, right after the re-apply step and **before every battle of the turn** — the standing sieges and assaults of Pre-Phase 3 as well as the marches of Phase 5. One rule, both sides: **troops recruited this turn fight this turn, whatever their army does.** The price of that position:

- **Paid from the treasury as the report shows it** — before income, tribute and this turn's market orders, so "buy iron, then recruit" is a two-turn pipeline (the page's check: §2.12.1). A refusal for materials says so on its card ("paid in Pre-Phase 2b, from the treasury as your report showed it"), and the recruit cards themselves carry a **PRE-PHASE 2b · Recruitment** badge and sit first in the report.

- **Billed the turn they arrive.** Phase 2 upkeep and food include the new men (the page reserves that bill, §2.12.1).

- **Cap on the population the report shows** (pre-growth, §2.12.1).

- **Fresh recruits muster at status 100** and dilute the army's status by headcount *before* it fights.

- **A hex you take this turn musters for you from next turn.** Recruitment runs before the pre-phase storm, the auto-fall and the marches that capture hexes, so an army camped on an enemy fortress cannot recruit there yet (own/allied hex rule); engines are the exception (built anywhere, §5.8.6).

- **Phase 1 counts the recruits too.** Orc reproduction breeds on the foot count *including* this turn's recruits (§2.9.10), and the horse herd breeds on what is left after this turn's mounted recruits were paid (§2.9.9). Both by design.

- **Recruiting into a garrison at breaking point buys men who surrender an hour later.** A recruit aimed at a garrison whose hex auto-falls this turn (Pre-Phase 4) is paid and the units are lost with the garrison.

Hires and ship builds did not move — they stay in Phase 4 (§2.12).

**2.6b Pre-Phase 3: Siege & Assault Stance Resolution**

Between the re-apply step and Siege Auto-Fall, the Turn Processor resolves the stances of every army that is **holding position** — an army that submitted no move order this turn:

- The **ordered sally** is fought here first, before any siege tick or Assault on that hex (§2.13.7). Nobody sallies unordered.

- A **stationary besieger** (a siege-stance army already sitting at an enemy walled construction) **advances its Siege Progress by 1 here, before Phase 1** — unless an army not friendly to it — a neutral included — is camped outside: it fights that army instead, and the battle costs the turn's progress (§5.8.2). This is the quiet reason a patient siege resolves a full segment earlier than a marching one: its counter ticks *now*, and if that tick pushes it over the threshold the hex falls in the very next step (§2.7), all before income.

- On-the-spot stance orders (siege, assault, ambush, defensive, garrison) for stationary armies are read at this point, together with each army's **stored** stance (Siege, Defensive, Garrison and Ambush stay in force until changed; Assault is a per-turn order — §5.4). Only siege, assault and sally *act* here (the Sally first, §2.13.7); a Siege or an Assault first fights any hostile army camped outside the walls (§5.8.0). garrison also matters here: a Garrison order given this turn already gives its ×1.30 to a storm resolved in this block. A **besieged** army holds Garrison or orders Sally (§2.13.7). defensive otherwise takes effect when someone attacks the army in Phase 5/6. On walls, **every stance but Garrison stands OUTSIDE** from this point (§5.8.0). An **invalid** Ambush is stored and behaves as Defensive throughout. An army with no stance order **and none stored** counts as moving (a besieged one counts as Garrison); a kingdom that submitted no orders keeps its stored stances, and its armies with **no** stance on its own or a friend's walls are put in Garrison while there is room and no army at war with it is camped outside (§5.8.0).

- **Recruits are already there.** Recruitment runs in Pre-Phase 2b (§2.6a), so a stationary siege or assault storms with this turn's recruits, and a garrison that is stormed, or an army that sallies, fights with them too.

A *moving* army carries its stance into its Phase-5 combat instead — and a march onto a foreign fort is a Phase-5 **assault-on-arrival** (§5.8.0), not a pre-phase event. So the combat resolved here is the stationary besieger's siege tick, the ordered sally of a besieged army, and a full walled assault by any stationary assault-stance army already sitting at an enemy fortification (a repelled assaulter stays on the hex). This step spends no resources and marches no army; only battles move armies here — besiegers beaten by a Sally fall back, and a stormer that takes the walls moves in.

**2.7 Pre-Phase 4: Siege Auto-Fall**

If any hex has a Siege Progress counter that **exceeds** its Siege Threshold, the hex falls to the besieger before Phase 1. This runs before income and before any army movement (resource transfers happen at end of turn, so they are unaffected).

**Thresholds** (§5.8.3): an ordinary walled construction falls when progress exceeds 4 — **five** pressed turns; the muster seat when it exceeds 5 — **six**.

**On auto-fall:**

- The hex transfers to the besieger. Siege Progress resets to 0. No battle is fought: the besieger's army, standing on its new hex, is now inside its walls.

- Every army of the walls' **owner** inside **surrenders**: all units destroyed. Every one of them is a besieged Garrison, whatever it ordered (§2.13.7). Another realm's army inside — even one holding Garrison — is not the owner's garrison: it is expelled (below). The besieger seizes the surrendered arsenal (60–80% of its iron and horses, §2.13.11).

- Other defending armies at that hex — in practice only an owner army standing outside its own walls (any owner army not in Garrison), as every owner army inside is a besieged Garrison — retreat (up to 3 hops over land — never across sea, §5.5.6), abandoning their engines (§5.8.6). **If no retreat hex is found they are cut down in the rout, exactly as a third party's army at war with the besieger is** (the bullet below): the besieger strips the wreckage as it would a surrendered arsenal (§2.13.11), and you take a **−2 to −4 opinion** hit for the lost army, on top of the hit for the settlement itself (both count toward the −8 defeat cap, §8.5.3). Either way the army's fate is reported: a card for the rout, or a card for the withdrawal.

- **Nobody inside the walls is a bystander when they fall** (§5.6): every realm inside is at war with the besieger, so its army withdraws by the retreat rules above or is cut down if cornered — never *"holds its camp"*, never a peace last stand.

- A **third kingdom's** army camped **outside** the walls of the fallen hex that is a **mutual ally, vassal or liege of the besieger stays** — the ground now belongs to its own friend, and it is carded *"holds its camp"* (the same rule as for a stormed hex, §5.11). Any other third kingdom's army is **expelled** — it withdraws by the same retreat rules and its owner is notified. If it has nowhere to run, its relation to the besieger decides: a kingdom **at war** with the besieger is **cut down in the rout** — the besieger strips its wreckage (§2.13.11), and its owner takes the standard loser opinion hit (−2 to −4, within its −8 defeat cap, §8.5.3); a kingdom **at peace** with it makes a **last stand** instead, exactly as when walls are stormed — it declares war, fights the besieger's army there, and retakes the ground if it wins.

> ***▶ Example — the walls fall.** Aldoria's walled town (12,7) holds Aldoria's Army I and its ally Sylvane's Army II. Gruk-Mor's III, camped at the gates, orders Siege on turn 5; that first tick lays the ring (progress 1) and declares war on Sylvane too. From turn 6 both armies inside are besieged; neither orders Sally. Progress climbs 2, 3, 4 (the defender's card reads Collapse imminent!), then 5 on turn 9 — and in Pre-Phase 4 of turn 9 the town falls. Aldoria's I **surrenders** (a besieged army is a Garrison; Gruk-Mor salvages 60–80% of its iron and horses). Sylvane's II, an ally and not the owner's garrison, is **expelled** up to 3 hexes over land — or cut down and stripped if it has nowhere to go. Gruk-Mor's III, now on its own walled hex, stands inside them.*

- Any defender fleet docked at the fallen hex **puts to sea** — it runs for the nearest free **open-water** hex, and it can only travel *through* water to get there. A fleet cannot escape overland, and it cannot duck into the friendly port next door (a port is a land hex): the sea is its only road. It may sail **past** a hex another fleet already occupies, but it must finish on a free one — empty, or a friendly stack with room under the 3-fleet cap. **If no free water is within reach, the fleet is destroyed at its moorings** — the crews fire the hulls rather than hand the enemy a squadron, and any army aboard is lost with it. Both losses are reported.

- **Degradation** (§5.6.3): the production site and the settlement each drop one level, never below level 1.

- **What you are told**: the fallen hex's owner receives a card naming the **size and shape of the force that took it** — Besieging force: 88 troops (16 mounted, 72 foot). You watched them sit outside your walls for turns, so this is the best-observed force in the game and the report says so plainly. It counts every army of the besieging kingdom that was actually pressing the siege, and it reaches you whether or not you submitted orders that turn. It does **not** name their unit types — that stays a spy's work (§8.8; see the intel ladder in §2.13.4).

- No combat rolls. Siege fall is administrative — but it swings opinion like a won and a lost battle (§8.5.3).

**2.8 Resource Transfers (end of turn)**

Two ways to send resources — **the same underlying system**: the **🐪 Shipments → 📦 Send Resources** panel (send_resource orders, one per commodity) **and** the \[TRIBUTE: amount resource\] token inside a diplomatic message (§8.7). Either can send **gold, food, iron, horses, wood, or stone**, deducted at the **end of the turn**, *after* all your own spending (upkeep, construction, recruitment, and a rumour's price, set aside before any caravan leaves — §8.8.7) — surplus only, and partial if you run short — and carried by caravan (§2.8.2) to whoever your standing allows (§2.8.3). The page allows **one send per commodity per turn**; should an orders file nonetheless carry several sends of the same commodity to the same kingdom, the Turn Processor **merges them into a single caravan** carrying the sum (one dispatch card each side, one bandit roll). Offers accepted from last turn are not part of that merge: each leaves as its own caravan (§2.8.3).

**Tributes are not merged.** Each \[TRIBUTE: …\] message raises its own caravan with its own bandit roll — one tribute per message, up to 3 messages a turn (§8.7). So in one turn a kingdom can make up to **four** new sends of the same commodity to the same kingdom: once from the Send Resources panel and once in each of three messages. Offers that kingdom accepted from last turn leave on top of these, each as its own caravan — up to **eight** caravans of one commodity to one kingdom in a turn.

> ***▶ Example — eight caravans.** Last turn you were neutral with a neighbour and sent it 100 stone from the panel and three \[TRIBUTE: 100 stone\] messages — four offers. This turn it accepts all four, the two of you complete a trade pact, and you send the same four again, now directly. Eight caravans of stone leave for that kingdom this turn, each rolling for bandits on its own.*
>
> ***▶ Example.** You send 400 stone to an ally from the panel and write three messages to the same ally, each carrying \[TRIBUTE: 200 stone\]. Four caravans leave at the end of the turn — 400, 200, 200 and 200 stone, 1,000 in all — each rolling for bandits on its own. The tributes leave first — messages are read before the panel's sends — so with only 700 stone of surplus the three tributes take 600 and the panel's caravan carries the 100 left.*

**2.8.1 Returning captured land (hex transfer)**

A kingdom may return a hex to its **original owner** — the kingdom that held it at campaign start — if the two are in a **mutual alliance** (both sides holding Alliance stance; one-sided is inert, as everywhere else). Order it from the **🏰 Constructions** tab ("🤝 Return Captured Land", at the foot of the tab, listed automatically when you hold eligible hexes); the hex, its population and any production site change sovereign at the **end of the turn**, undamaged — this is a peaceful handover, not a conquest, so no conquest degradation applies. Maximum **one hex per kingdom per turn**.

Restrictions: only the hex's original kingdom may ever receive it (each hex remembers its founder forever — it can never be gifted onward to anyone else, and land that was neutral at campaign start can never be "returned" at all); capitals, muster seats and besieged hexes cannot be ceded.

**GM note — origin backfill for running campaigns:** on the first processing after this update, every hex is stamped with its CURRENT owner as its permanent origin (neutral hexes are stamped as no-one's). Hexes conquered BEFORE the update therefore read as the conqueror's original land. To make such a hex returnable, edit the current gm_state_turnN.json once: find the hex ("col":C,"row":R) and set its "origin_kingdom" to the true original kingdom's id. New campaigns need no backfill.

**2.8.2 Caravan Mechanics**

**Transit time:** 1 turn, plus 1 more per full 5 hexes of distance between capitals' muster seats (1 + ⌊distance/5⌋, minimum 1) — even direct neighbours send the caravan out *this* turn, and it \**arrives at the end of the* next *turn. Example: a distance of 20 hexes → \`1 + floor(20/5)\` = 5 transit turns*\*; dispatched at the end of turn 5, it arrives at the end of turn 10.

**Bandit risk** — Each turn the caravan spends on the road — including the arrival turn and any return leg — it rolls a **3% all-or-nothing bandit attack**. Caravans are lost entirely if the roll hits; there is no partial loss. Both the sender and receiver are notified at dispatch ("expect arrival at the end of turn N"), at arrival or loss, and **both** are told if the caravan turns back (below) — the receiver once, *"The caravan of N \<commodity\> from \<sender\> turned back"*, so a promised shipment never just vanishes from its Inbound list. The GM log records every dispatch, arrival, and loss with full detail.

**Realm destruction turnback** — The receiving kingdom's status is checked every turn the caravan spends on the road, not only when it arrives. The moment the destination realm holds no muster seat or no longer exists, the caravan turns back and heads home, taking as long to return as it had already travelled when the check caught it. The cargo is re-credited to the sender's treasury when the caravan arrives home. If the sender's kingdom also holds no muster seat when the return arrives, the caravan is lost to the roads — the cargo disperses, never recovered.

**No guarantee of delivery** — Caravans are fragile. The 3% per-turn roll means a 5-turn journey has a cumulative 1 - (0.97^5) ≈ **14% chance of loss** to bandits alone; a turn-back adds one roll per return turn. Frontier kingdoms or those besieged deep in hostile territory should expect a significant fraction of their caravans to never arrive. Plan accordingly.

**Vassalage tribute** (the automatic vassal→liege payment) remains **instant** — it is paid directly each turn, no travel delay. Market buy/sell orders also resolve instantly (Phase 3) — only diplomatic resource transfers (Send Resources panel + \[TRIBUTE\] message token) travel by caravan.

**The Shipments tab** gathers everything on the road in one place: the 📦 Send Resources panel (with this turn's queued sends and their ✕ Cancel chips), an **📤 Outbound** list — every caravan you have in transit, with destination, commodity, amount, dispatch turn, arrival turn and turns left (a turned-back caravan reads **↩ returning home from \<kingdom\> · back turn N** instead — its arrival turn now means *home*, so no arrow and no "arrives") — and a **🤝 Caravan Offers** list (offers from realms without a pact, with ✓ Accept / ✕ Decline, and your own offers awaiting an answer — §2.8.3), an **📥 Inbound** list of every caravan other kingdoms currently have on the road *to you* (sender, commodity, amount, arrival turn, turns left). A caravan raised by a \[TRIBUTE\] token carries a **🏛 tribute** tag on either list. The inbound list is **not fogged**: you were already told at dispatch by the *Caravan inbound* card, so the list simply keeps that knowledge visible until the goods land. Both lists are read-only — a dispatched caravan has left the sender's hands and nobody can recall it.

**2.8.3 Who you may send to — caravan offers**

**Why the rule exists.** When a caravan sets out, the sender's *Caravan dispatched* card says how many hexes of road lie between the two muster seats. That is useful to a friend and dangerous in anyone else's hands: sending 1 gold to a stranger would tell you exactly how far away their seat is, and two realms comparing notes could pin it down. So the **receiver** decides whether a stranger may learn that.

**The rule — read at the end of the turn, after that turn's diplomacy:**

|                                                                                                         |                                                                                                            |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Your standing with the receiver**                                                                     | **What happens to your send**                                                                              |
| **Mutual trade pact or alliance** (both of you hold Trade or Alliance), or you are **liege and vassal** | Sent **directly**: deducted and dispatched at the end of this turn (§2.8.2).                               |
| **At war** — either of you holds War                                                                    | **Refused.** Nothing is deducted, you are carded *Shipment/Tribute not sent*, and the enemy hears nothing. |
| **Anything else (neutral)** — including a pact only *you* hold                                          | Becomes an **offer**. Nothing leaves your stores this turn; the receiver decides next turn.                |

Because the standing is read *after* Phase 8 diplomacy, a trade pact that both sides complete this turn already sends directly, and a war declared this turn already blocks the send.

**How an offer runs.**

1\. **Turn N — you send.** The Send Resources panel tags each kingdom *direct*, *offer* or *at war* before you choose. For a neutral receiver your pending order reads *Offering…* and your stock does **not** drop. It is **not reserved** either, so keep the full amount in your stores until the offer is answered. At the end of the turn you are carded *Caravan offered*, and the receiver is carded *Caravan offer*, which names you and the goods and nothing else — no distance, no seat.

2\. **Turn N+1 — they answer.** The offer appears in the receiver's **Shipments → 🤝 Caravan Offers** list with **✓ Accept** and **✕ Decline** (click the chosen answer again to take it back). Your own copy sits in the same list as *awaiting their answer*.

3\. **End of turn N+1 — the result.**

- **Accepted:** the caravan sets out **with the full amount offered, or not at all**. If you no longer hold all of it when it is served at the end of that turn, the offer is **void**: nothing is sent, both sides are carded *Caravan offer void*, no distance is shown, and the receiver is not told how much you held. The receiver agreed to *that* gift, so a sender cannot offer 5,000 and ship 1 just to read the road length. If the full amount leaves, it is an ordinary caravan from here (§2.8.2): both sides get the dispatch/inbound cards, and you now learn the length of the road. That is what the receiver agreed to by accepting.

- **What goes first.** Your \[TRIBUTE\] messages of that turn leave during Messaging, **before** accepted offers are served; your panel sends leave **after** them (§2.3). A tribute can therefore use up the stock an accepted offer needs.

> ***▶ Example.** You hold 700 stone. Mayaris accepted your offer of 500 stone from last turn, and this turn you write three messages to Wyrmskar, each with \[TRIBUTE: 200 stone\]. The three tributes leave first and take 600; when the offer is served you hold 100, so the 500-stone offer is **void** — nothing goes to Mayaris. Send the tributes a turn later, or from the panel, to keep the offer.*

- **Declined:** nothing moves; both sides are carded.

- **No answer** (including a receiver that sent no orders): the offer **lapses** after that one turn and you are carded. Offer again if you still want to.

- **War by then:** if the two realms are at war by the end of turn N+1, an accepted offer is refused on both sides.

The \[TRIBUTE: …\] token follows the same rule as the panel. A tribute to a neutral becomes an offer, and it keeps its 🏛 tag once accepted. A tribute to an enemy is refused. The message itself is still delivered, because only the goods are held back. The Messages tab warns you about both cases when you queue the message. A tribute to a realm you are at war with when the messages are read is **refused even if the two of you make peace with \`\[CEASEFIRE\]\` in that same turn**, whichever message you wrote first — send it the turn after the peace. The panel's sends are read at the end of the turn, after the peace, so they follow the new standing.

> ***▶ Example — one turn, three sends** (invented realms). On turn 12 Valdoria sends 500 gold to each of three realms:*
>
> *• **Ostmark** holds a trade pact with Valdoria, and Ostmark holds one back. The 500 gold leaves at the end of turn 12, Valdoria's card reads "The road is 12 hexes of country; expect arrival at the end of turn 15" (1 + ⌊12/5⌋ = 3 turns), and Ostmark is carded Caravan inbound.*
>
> *• **Kheshet** is at peace with Valdoria; there is no pact. Valdoria's treasury does **not** drop. Valdoria is carded Caravan offered, and Kheshet is carded "Valdoria offers you 500 gold … answer in the Shipments tab next turn", with no distance anywhere.*
>
> *◦ If Kheshet accepts on turn 13, the gold is deducted and leaves at the end of turn 13, as long as Valdoria still holds all 500 then. Only now does Valdoria's dispatch card name the road length. Had Valdoria spent down to 499 gold, the offer would be void: nothing leaves and no distance is shown.*
>
> *◦ If Kheshet declines or ignores it, nothing moves and Valdoria learns nothing but the answer.*
>
> *• **Drakmoor** is at war with Valdoria. The send is refused on the spot; the page will not even queue it. A hand-edited order would be refused at the end of the turn, with Valdoria carded "Shipment to Drakmoor not sent — no caravan crosses a war" and Drakmoor told nothing.*
>
> *The outcome: Valdoria's friend gets the gold and Valdoria learns the road to it. The stranger keeps its location to itself unless it chooses to take the gold. The enemy gets nothing and learns nothing.*

**2.9 Phase 1 — Population Growth & Income**

This phase runs for each kingdom. All income is calculated from the post-Pre-Phase map state and applied to resources.

**2.9.1 Population Growth**

Each owned construction hex grows by 1–3% of its level's **population ceiling** each turn, and stops at the ceiling; bare hexes never grow. Formula, ceilings and the legacy bare-hex path: §3.8. The report's **👥 Population grew** card gives the turn's gain and the new total, and names every settlement already at its level's ceiling: those grow again only after an upgrade.

**Emigration.** If Opinion is **40 or below** at the start of the turn (the same start-of-turn reading as the tax penalty, §2.9.6), **no settlement grows**, and every settlement instead loses a share of the people living in it (TP_EMIGRATION_BANDS):

|                   |                                              |
|-------------------|----------------------------------------------|
| **Opinion Range** | **People leaving each settlement, per turn** |
| 41–100            | none (normal growth)                         |
| 31–40             | 1%                                           |
| 21–30             | 2.5%                                         |
| 11–20             | 5%                                           |
| 0–10              | 10%                                          |

left = max(1, floor(pop × share / 100)) per populated settlement

The people who leave are gone; no other kingdom gains them. They leave before this turn's tax and site output are counted, so the same turn already collects from fewer people. A populated settlement always loses at least 1 person, so a small settlement can empty completely, and its sites then produce nothing. A settlement must reach its ceiling to be upgraded (§2.11.7), so a kingdom in these bands cannot upgrade a settlement that is not already full. The report's **👥 People left your kingdom** card replaces the growth card and gives the count. To stop it, raise opinion above 40: every turn at a tax rate below 5% raises it (§2.9.13).

> ***▶ Example — emigration.** A kingdom with two settlements of 4,000 and 30 people starts the turn at Opinion 25 (the 21–30 band, 2.5%). The large one loses floor(4,000 × 2.5 / 100) = 100 people; the small one would lose floor(30 × 2.5 / 100) = 0, so it loses the minimum of 1. Neither grows. This turn's tax is counted on 3,900 + 29 = 3,929 people, and then the 30% opinion penalty applies (§2.9.6).*

**2.9.2 Terrain Income**

- **Plains hex (no site)**: +1 food per qualifying plains hex owned

- **There is no terrain gold.** All gold comes from population tax, ports and trade.

A plains hex with any site does **not** generate the +1 flat food; its site replaces terrain food production.

**2.9.3 Blockade Suppression**

A fleet in **Blockade** stance suppresses all income from the enemy port it **lies inside**. Sail onto the port hex first — if an enemy fleet is docked there you fight it on arrival, and it defends with the port bonus if it began the turn there (§5.9.2) — then order Blockade next turn. A fleet beside a port, or in its own harbour next to an enemy one, blockades nothing. A blockaded port generates no gold and no food that turn. Blockade requires active war status between the two kingdoms. The station has a price: a blockading fleet loses **2 STATUS per turn** and cannot recover until it stands down (§5.10).

**Who is told.** The blockader's report carries *"Fleet N — Blockade active"* naming the harbour it lies in, and the owner's carries *"N port(s) under naval blockade!"*, which names each blockaded port, every fleet blockading it (its commander, hulls, ships and WP as it lay when the blockade took hold — never its cargo) and every fleet **linked** to a blockader, listed with that blockade (the group blockades as one: every member pays its upkeep, and a member's realm not yet at war with you is declared at war by sailing in it — the card says so); any other foreign fleet moored there is listed as **not** blockading, with why (at peace with you, your ally, or at war but under no Blockade order) and whose link it sails in.

**Stored while it bites** (the naval twin of the stored Siege). Order it once and the fleet holds station turn after turn — suppressing and bleeding — with no need to repeat it, for as long as it stands still inside a port of a kingdom it is at war with. The moment that stops (peace, the port changes hands, the fleet is driven off) the station is dropped and you are carded *"Blockade lapsed"* with the reason; a sail order or another stance ends it silently. A Blockade ordered anywhere else is never stored, and the order is carded *"Blockade not in force"* with the reason. A blockade that held at the start of a turn but cannot continue — the port changed hands during that turn — is carded *"Blockade ends"*. **Raid is never stored** — it is an action, ordered per turn. The Player Page loads a stored blockade pre-selected and marks the chip *(in force)*; planning a sail for that fleet drops it back to Sailing on the page, as the engine will.

**A fleet that sails does not blockade that turn** (the naval twin of the army rule): a Blockade filed beside a sail order is read as Sailing for the whole turn — no suppression, no station bleed — and the page keeps the two exclusive in both directions: a planned sail refuses Blockade's twin ("Set Sailing first"), and clicking Blockade over a planned sail clears the voyage. If the pair still reaches the engine (an outdated page), your report carries *"Blockade not applied"* for that fleet, and if the fleet was already holding a stored blockade the card says that station has ended: sail this turn, order Blockade next turn with no sail, and it bites from where the fleet then stands. Raid is different: an anchor raid fires before movement, so "raid and leave" is legal (§2.14.3).

**2.9.4 Site Income**

**Farm** (food, rolled fresh every turn per farm — §3.6.1) and **Mine** (iron — §3.6.2) pay from their hex's population at this step.

**Port** (plains on any map built today, **and, for an Elf kingdom alone, coastal forest under an Elven construction** (§2.11.1) — a coastal settlement on hills, mountain or swamp cannot host a harbour, so where your realm meets the sea decides whether you can have a navy at all; must be adjacent to at least one sea hex; **Orc and Dwarf kingdoms may never build or upgrade one** — they field no navy, so a harbour would be dead investment. A port they take by conquest keeps producing for them; it simply never grows): gold = floor(pop × goldMult) — Lv1: ×0.20, Lv2: ×0.40, Lv3: ×0.60 — **gold is never random** food = floor(pop × rate) — **no port level has a fixed food rate: every port rolls its own, fresh, every turn** — Lv1 anywhere from **0% to 5%** of population, Lv2 from **0% to 10%**, Lv3 from **0% to 15%**. The roll is per port and per turn, so ten small harbours average out while one big one is a gamble, and **a bad season pays next to nothing** — any roll above 0% still pays at least 1 food, so only a roll of exactly 0% (possible, but practically never seen) pays none. Gold floors at 1 while the hex has any population, and so does a food rate above zero; a rolled 0% pays 0, and a port whose bracket factor reaches 0 earns nothing either way. A blockaded port produces neither.

> ***▶ What the upgrade actually buys you.** Each level raises gold (×0.20 → ×0.40 → ×0.60, guaranteed) and widens the food roll (0–5% → 0–10% → 0–15%), so the harvest averages ~2.5% / ~5% / ~7.5% of population and can fall to next to nothing at any level. The ladder is monotonic: a higher port is never worse on average.*

**Why your port food moves.** The Ports card in your report lists your ports one by one: each port's gold, its food and the % it rolled this turn, a blockaded port marked as blockaded, and a port past your first five marked with its reduced rate. Your Player Page **cannot** predict it — the page counts rolled food as **zero** in every figure it calls guaranteed, deliberately, so it can never promise you a harvest the engine has not granted. The Production tab shows each port's possible harvest as a range instead (e.g. 600g + 🎲 0–149f/turn for a 1,000-pop Lv3 port — the top is the best the roll can actually pay, which at many round populations is one short of the percentage), so a 0 there is the bottom of the roll, never a forecast. A port your report marks as **blockaded** — marked only while a blockade still holds it at the end of the turn, so a blockader you drove off leaves no mark — counts as 0 in the page's income forecast and on its Production card, because a held blockade bites again next turn. Plan around the gold, and treat the food as weather.

**Port brackets.** A kingdom's ports pay in brackets of **5**, ranked **biggest first** by gold yield: ports 1–5 earn the full rate, ports 6–10 earn **90%**, 11–15 **80%**, 16–20 **70%**, and so on down by 10% per bracket (a 51st port would be the first to earn nothing). Gold and food are cut alike, and the cut always lands on your smallest harbours. A blockaded port still occupies its slot. The Player Page warns you the moment you queue a port build that would fall into a reduced bracket (the toast and the order card both name the rank and the rate), the Production tab marks each cut port with its rate (⚓ 90% …), the income breakdown counts how many ports were reduced, and the turn report's Ports card, active or passive, says how many of your ports were paid at the reduced rate.

**Lumbermill** (wood — §3.6.5) and **Quarry** (stone — §3.6.6) pay from their hex's population at this step too.

**2.9.5 Population Tax**

Player-set tax rate: 1–10 (default 5). **Every rate collects in full** — 10% of your people's worth is 10%.

rawTax = floor(totalPop × taxRate / 100)

totalPop = sum of all owned hex populations after this turn's growth or emigration (§2.9.1) — and after this turn's recruits were drawn from it (Pre-Phase 2b, §2.6a): recruiting lowers the same turn's tax base.

**Tax at a glance** — what each rate collects, what that pays from 25,000 people, and what it does to opinion every turn (§2.9.13). Low opinion then takes its PENALTYTAX share of what is collected (§2.9.6). The gold column scales with population; the opinion column is the same for any kingdom.

|              |                             |                        |
|--------------|-----------------------------|------------------------|
| **Tax rate** | **Gold from 25,000 people** | **Opinion every turn** |
| 1%           | 250                         | +8                     |
| 2%           | 500                         | +6                     |
| 3%           | 750                         | +4                     |
| 4%           | 1,000                       | +2                     |
| 5%           | 1,250                       | no change              |
| 6%           | 1,500                       | −2                     |
| 7%           | 1,750                       | −4                     |
| 8%           | 2,000                       | −6                     |
| 9%           | 2,250                       | −10                    |
| 10%          | 2,500                       | −15                    |

In any one turn more tax is more gold; the price is opinion: at 50 or below opinion takes a share of the tax back, and at 20 or below most of it (§2.9.6).

> ***▶ Example — tax, then the opinion penalty.** A kingdom of 26,000 people holds 7% tax with Opinion 35 at the start of the turn.*
>
> *• **Tax:** rawTax = floor(26,000 × 7 / 100) = 1,820 gold.*
>
> *• **Opinion penalty (§2.9.6):** Opinion 35 sits in the 31–40 band, 10% → penaltyAmt = floor(1,820 × 10 / 100) = 182 → netTax = 1,638 gold.*
>
> *• **Opinion (§2.9.13):** holding 7% moves opinion −4 → 31 next turn. The same kingdom at Opinion 55 would have kept all 1,820 gold; at Opinion 15 it would keep only 1,820 − floor(1,820 × 60 / 100) = 728. Holding the rate drives opinion down into those bands. To climb back, the rate must go below 5%.*

**2.9.6 Opinion Penalty on Tax**

If Opinion is **50 or below**, a share of raw tax income is lost (the reports label this deduction **PENALTYTAX**; note that exactly 50 is already penalized). From 31 to 50 the loss is small; at 30 or below it climbs fast, and at 20 or below most of the tax is lost. The share is read from your opinion at the **start** of the turn — before this turn's tax rate moves it, and before any siege, storm or sally fought earlier in the same turn (Pre-Phase 3) moves it (TP_TAX_PENALTY_BANDS):

|                   |                 |
|-------------------|-----------------|
| **Opinion Range** | **Tax Penalty** |
| 51–100            | 0%              |
| 41–50             | 5% of raw tax   |
| 31–40             | 10% of raw tax  |
| 21–30             | 30% of raw tax  |
| 11–20             | 60% of raw tax  |
| 0–10              | 90% of raw tax  |

penaltyAmt = floor(rawTax × penaltyTax / 100)

netTax = max(0, rawTax − penaltyAmt)

> ***▶ Example — holding 10% from Opinion 90.** One settlement of 25,000 people, already at its level's ceiling (so it does not grow), already taxed at 10%. Each turn the penalty band and emigration are read from the opinion the turn **starts** with; then 10% moves opinion −15 (§2.9.13).*
>
> *• **Turns 1–3** — start at 90, 75, 60: no penalty, nobody leaves → 2,500 gold each turn. Opinion ends turn 3 at 45.*
>
> *• **Turn 4** — start 45 (41–50): 2,500 − floor(2,500 × 5 / 100) = 2,375. Ends at 30.*
>
> *• **Turn 5** — start 30 (21–30): 2.5% leave first, floor(25,000 × 2.5 / 100) = 625 → 24,375 people; rawTax = 2,437, penalty floor(2,437 × 30 / 100) = 731 → 1,706. Ends at 15.*
>
> *• **Turn 6** — start 15: 5% leave (1,218 → 23,157); rawTax = 2,315, penalty 60% = 1,389 → 926. Ends at 0.*
>
> *• **Turn 7 and on** — start 0: 10% leave (2,315 → 20,842); rawTax = 2,084, penalty 90% = 1,875 → 209, and a tenth of the people leave again every turn.*
>
> *Seven turns pay 12,716 gold against 8,750 at a steady 5% — but the kingdom has lost a sixth of its people, and from then on earns 209 a turn where 5% would pay 1,250.*

**2.9.7 Character Income Bonuses**

Applied after base income is established:

- **Treasurer** (assignment treasury): bonusGold = floor(netTax × economics × 0.2 / 100) — **tax gold only**; port gold is the Master of Ports' office, and no gold is counted by both (there is no terrain gold — §2.9.2)

- **Master of Farms** (assignment farms): bonusFood = floor((farmFood + portFood) × management × 0.2 / 100) — note that portFood contains the **rolled** harvest of every port level (§2.9.4), so this bonus inherits that swing: a season where your ports roll badly pays your Master of Farms less through no fault of his own.

- **Master of Mines** (assignment mines): bonusIron = floor(mineIron × management × 0.2 / 100)

- **Master of Ports** (assignment ports): bonusGold = floor(portGold × management × 0.2 / 100) — portGold is the bracket-reduced, blockade-reduced total, exactly the figure on the Ports card. Not available to Orc or Dwarf kingdoms (no ports).

- **Master of Lumbermills** (assignment lumbermills): bonusWood = floor(lumberWood × management × 0.2 / 100)

- **Master of Quarries** (assignment quarries): bonusStone = floor(quarryStone × management × 0.2 / 100)

- **Master of Horses** (assignment horses): adds management × 0.02 **percentage points** to the herd's breeding rate — not a share of the yield, which on a herd growing 1–3% a turn would be worth almost nothing (§2.9.9). Available to every race.

> ***▶ Example — the Treasurer next to a Master of Ports.** A realm takes 1,552g in tax and 8,583g from its ports. Its Treasurer has Economics 96 (+19.2%) and its Master of Ports Management 94 (+18.8%). The Treasurer adds floor(1,552 × 19.2 / 100) = **297g** — the ports are not the Treasurer's to count; the Master of Ports adds floor(8,583 × 18.8 / 100) = **1,613g**. No gold piece is counted by both offices, and neither bonus enters the pact base (§2.9.8) or the tribute base (§2.9.11). For a realm that lives on its harbours the Master of Ports is the office that pays; for one that lives on its taxes, the Treasurer.*

Character stats range 1–100 at creation, so the base maximum bonus per character is 20%; experience (§7.10) can lift a stat to min(150, base + 20%), i.e. a bonus of up to 30%. The Master of Horses works in points instead: +2 at management 100, up to +3 at 150. The Player Page's **Profile** ledger shows, on each resource's row, the Master holding the office and what they add this turn (an office assigned this turn pays from the next).

> ***▶ Example — reading one row of the Profile ledger.** A realm's Gold row reads: 💰 Gold 28,070 · +8,988 · 51,744 people at 3% tax · 4 ports (2 Lv3 · 1 Lv2 · 1 Lv1) · −3,057 upkeep · Treasurer ✓ +297 💰 (+19.2%) · Master of Ports ✓ +1,613 💰 (+18.8%). The row adds up: tax 1,552 + ports 8,583 + the Treasurer's 19.2% of the tax (297) + the Master of Ports' 18.8% of the ports (1,613), minus 3,057 upkeep, is the **+8,988** per turn. Every source and drain on the row is a line of the Production Income table below it, so the two never disagree; each site count carries its levels, highest first; a Master assigned this turn reads assigned this turn — pays from next turn.*

**2.9.8 Trade / Alliance Pact Income**

A **mutual pact** grants a gold bonus each turn — both kingdoms at trade **or better** toward each other (trade↔trade, trade↔alliance, or alliance↔alliance; the mixed pair counts as a trade pact and needs the border — see below):

- Each mutual pair grants 0–2% of the kingdom's gold base — **tax + ports**, without the Treasurer's or Master of Ports' bonuses

- Roll per partner: floor(rand×3) → **0, 1, or 2%** (some turns a pact pays nothing)

- Gold only; stacks across your mutual trade or alliance partners — **at most 5 pay in a turn**: with more, 5 are drawn at random each turn and the rest bring nothing (*Market saturated — your merchants cannot find a market for so many trade partners*); both kingdoms roll independently

- **Trade requires a shared border**: you can only form a trade pact with a kingdom directly adjacent to your territory, and it only pays on turns you still border them — the border is re-checked every turn: lose it (territory changes hands) and the pact goes **dormant** — it pays nothing and both reports carry a 📦 *"trade pact dormant — no shared border"* card until you are neighbours again (or upgrade to full mutual alliance, which needs no border). A trade↔alliance pair keeps paying while the upgrade offer stands; the proposer's report shows 🤝 *"alliance proposed — trade pact still active"* and the other side's alliance-offer card notes the pact keeps paying either way

- **Alliances have no border requirement** — ally a distant kingdom to earn a pact bonus across the map; this is how you get an economic pact with a non-neighbour

- Vassal and liege are allied, so they receive this bonus too — on top of tribute, at any distance

- Works with **any** kingdom including AI-controlled or absent (passive) ones (trade still needs the border; alliance does not)

Neither stance is auto-mirrored — both kingdoms must set it independently (§2.16.2); a truly one-sided pact (the other side at peace or worse) pays nothing.

> ***▶ Example — seven allies, five pay.** Realm A holds mutual alliances with seven realms, and its gold base this turn (tax + ports) is 10,000g. Each turn five of the seven are drawn to pay; each of those rolls 0, 1 or 2% — together 0 to 1,000g, about 500g on an average turn. The other two bring nothing, and A's report says so: Market saturated — 5 of 7 trade partners paid … This turn C, F brought nothing. Next turn the draw starts again, so a different pair may sit out. Five allies or seven, A's pact income never passes 5 × 2% = **10%** of its gold base.*

**2.9.9 Horse Breeding**

If a kingdom holds at least 2 horses (a breeding pair), they breed each turn — a lone horse cannot reproduce: gained = ceil(horses × (growthPct + masterPts) / 100) where growthPct = 1 + floor(rand×3) = 1–3% and masterPts = management × 0.02 of a **Master of Horses** (§2.9.7; 0 without one) — **rounded UP** (a breeding pair always gains at least 1). Example: 1,000 horses at a 2% roll with a management-90 Master breed at 2% + 1.8 = 3.8% — 38 foals instead of 20. The Master needs the breeding pair too: below 2 horses nothing breeds.

**The herd breeds on what is left after this turn's cavalry is paid.** Recruitment (Pre-Phase 2b) spends 1 horse per mounted recruit *before* Phase 1 counts the herd. Example at a 2% roll: with 100 horses and 50 cavalry recruited, the herd breeds on 50, gives 1 foal and ends at 51. Spend the herd down to a single horse and it breeds nothing that turn.

**2.9.10 Orc Reproduction**

Each Orc army with **10 or more Orc foot soldiers** that **stands on a swamp hex** gains troops each turn:

- **Swamp only.** The army's position **when Phase 1 runs** — after the pre-phase sieges, assaults and embarkations have resolved, before this turn's marches — must be swamp terrain: any swamp, owned or not. On any other ground, or aboard a fleet, the horde does not breed; the report says so per army ("no swamp underfoot"), never silently.

- Growth rate: 5 + floor(rand×3) = 5–7% of that army's foot count. **The count includes foot recruited this turn:** recruitment (Pre-Phase 2b) runs before Phase 1, so fresh goblins breed the turn they arrive, and a horde below the 10-foot threshold that recruits past it breeds that same turn. Example at a 6% roll: a swamp horde of 20 that recruits 30 breeds on 50, grows 3 and ends at 53.

- gained = ceil(footCount × growthPct / 100) — **rounded UP**, so every eligible army gains at least +1 per turn

- Distributed proportionally across foot unit stacks in the army

- Mounted units do not reproduce. **Only Orc foot soldiers breed and count:** troops of other peoples in an Orc army (§2.12.1) and siege engines do not breed, and are not part of the foot count or the 10-soldier threshold

- When a turn's breeding carries total Orc foot soldiers across all armies over 300, 500, or 1000 for the first time, all other kingdoms receive a warning broadcast. Crossing a line by recruitment or merging alone does not announce — only the breeding does.

- **The Player Page forecast is a forecast.** The submit-time 🧬 card reads each army's hex on the page; the Turn Processor decides at Phase 1. One known one-turn lag (by design): in the turn right after a kingdom **retakes its original capital**, the page still places a freshly raised army at the old fallback seat while the TP already uses the original capital — if exactly one of the two is swamp, the forecast is wrong for that single turn; the report is right.

- **Zero-growth turns.** With the gain rounded up, an eligible horde *on swamp* always grows. Kingdom-wide zero growth is routine: whenever no horde stands on a swamp hex the report carries the neutral 🧬 *"the horde stands on dry ground"* card listing each dry horde. The *"no new boyz this season"* card remains only as a defensive fallback for a swamp horde whose roll floors to 0, which the rounded-up math never produces.

- **The rolls are shown, army by army.** Both reproduction cards (growth and zero-growth, active and passive reports) itemise every eligible army's roll — e.g. Army I: +3 (5% of 41) · Army II: +1 (6% of 12) — followed by every dry-ground horde that did not breed — e.g. Army III: no swamp underfoot (plains) — did not breed — and the GM's turn log carries a matching 🧬 *Orc Reproduction* entry with the same per-army breakdown.

**2.9.11 Vassal Tribute**

Vassals pay tribute to their liege after Phase 1 income is calculated:

- Rate: 1–5% (set by liege, default 3%), clamped in code: max(1, min(5, rate))

- tributeBase = netTax + portGold — the vassal's Treasurer and Master of Ports bonuses are not taxed, the same base as the pacts (§2.9.8)

- tributeAmt = floor(tributeBase × tributeRate / 100)

- Gold deducted from vassal, added to liege. If vassal cannot cover the full amount, only what it has is taken.

- Tribute stops from the turn after the vassalage ends — renounced, or broken by a war between the two (§2.16.4); a war begun before Phase 1's income (a standing siege or assault) stops it that same turn.

> ***▶ Example — a vassal with good Masters.** A vassal at 5% takes 1,552g in tax and 8,583g from its ports; its Treasurer adds 297g and its Master of Ports 1,613g. The tribute is floor((1,552 + 8,583) × 5 / 100) = **506g**. The two Masters' 1,910g stay with the vassal — the liege taxes the realm's income, not the skill of its officers.*

**2.9.12 Income Applied**

totalGold = netTax + portGold + treasurerBonus + masterPortsBonus + tradePactBonus

totalFood = plainsFood + farmFood + portFood + masterFarmsBonus

totalIron = mineIron + masterMinesBonus

totalWood = lumberWood + masterLumbermillsBonus

totalStone = quarryStone + masterQuarriesBonus

plainsFood is the +1 food per site-less plains hex (§2.9.2). There is no terrain gold term: gold comes only from tax, ports, character bonuses and pacts.

Vassal tribute is then deducted from the vassal's accumulated gold.

> ***▶ Example — a small kingdom's Phase 1 income.** A muster-seat construction (pop 10,000) + two lesser constructions (pop 5,000 each) + three plains constructions each holding a Level-2 farm (pop 2,000 each). Tax rate 5, Opinion 75, no characters, no trade pacts.*
>
> *• **Terrain gold:** none (§2.9.2).*
>
> *• **Tax:** total population = 10,000 + 2×5,000 + 3×2,000 = 26,000; rawTax = floor(26,000 × 5 / 100) = 1,300 gold. Opinion 75 is above 50, so there is no tax penalty → netTax = 1,300.*
>
> *• **Farm food:** a Level-2 farm rolls its rate each turn in \[0.20, 0.50\] (§3.6.1), so each of these yields between floor(2,000 × 0.20) = 400 and floor(2,000 × 0.50) = 1,000 food → **1,200 to 3,000 food**, and a different figure every turn. What you are guaranteed is the bottom of that: 1,200. The three plains hexes have a site, so they do **not** also produce the flat +1 terrain food.*
>
> *• **This turn:** 1,300 gold, 1,200–3,000 food (guaranteed 1,200), 0 iron.*
>
> *Now assign a Treasurer with Economics 80: gold rises by floor(1,300 × 80 × 0.2 / 100) = floor(208) = 208 → 1,508 gold. A single well-placed character is worth more than a whole settlement.*

**2.9.13 Tax Rate Changes**

A tax_change order takes effect at the end of Phase 1 (this turn's income is already calculated at the old rate, so the **new rate first applies to next turn's income**).

You may change the rate by at most **1 percentage point per turn** (e.g. 5→6 or 5→4, never 5→7). This is enforced by the **Turn Processor**, not just the Player Page: an orders file hand-edited to request a larger jump is **clamped to ±1** from your actual current rate (and logged to the GM), so there is no way to leap to a high rate in a single turn.

**Changing the rate costs no opinion by itself. The rate you hold moves opinion every turn**, by the rate that collected that turn's tax:

opinionChange = (TP_TAX_OPINION_NEUTRAL − taxRate) × TP_TAX_OPINION_PER_POINT — +2 per point below 5%, −2 per point above up to 8%. The two top rates cost more: **9% costs 10 and 10% costs 15** every turn (every rate in the *Tax at a glance* table, §2.9.5).

No dice are rolled. The change lands in Phase 1, right after tax income, and opinion stays inside 0–100. Because a tax_change applies after income, **the turn you order a new rate still moves opinion at the old rate**; the new rate's figure starts next turn, together with its gold. It applies to every kingdom, including one that sent no orders. Opinion **does not recover on its own**: besides a rate below 5%, it rises only through events — any battle won (at most +3 a turn), or making peace or a ceasefire after at least 3 turns of war (§8.5.3). Your income card states the change that actually landed (· opinion −6 (tax 8%) — less, or nothing, when opinion is already at 0 or 100), and the Player Page shows the figure under Public Opinion and beside a queued tax change.

> ***▶ Example — the top two rates.** Three kingdoms of 25,000 people start at Opinion 70 and hold their rate for three turns.*
>
> *• **8%** — 2,000 gold a turn; opinion 70 → 64 → 58 → 52. Never penalised.*
>
> *• **9%** — opinion 70 → 60 → 50 → 40. 2,250, 2,250, then 2,138 (the third turn starts at 50: 5% of the tax lost). The fourth would start at 40: 10% lost and 1% of the people leave.*
>
> *• **10%** — opinion 70 → 55 → 40 → 25. 2,500, 2,500, then 2,228 (the third turn starts at 40: 250 people leave first, rawTax = 2,475, 10% lost). The fourth would start at 25: 30% lost, 2.5% leave.*
>
> *The 9th point costs 4 more opinion than the 8th, and the 10th costs 5 more than the 9th: the last points of tax are the dearest.*

**2.10 Phase 2 — Upkeep & Starvation**

**2.10.1 Gold Upkeep**

Total gold upkeep = sum of upkeep.gold × count across all armies (all unit stacks) plus all fleets (all ship stacks). Deducted from gold reserves. Recruits raised this turn (Pre-Phase 2b, §2.6a) are already on the rolls and are billed here; the Player Page reserved that first-turn bill when you queued them.

**2.10.2 Gold Deficit Consequences**

If gold upkeep exceeds available gold:

- Desertion: 5 + floor(rand×11) = 5–15% of all troops across all non-destroyed armies — rounded **down** per unit stack with no minimum, so it never takes an army's last soldier (a stack of fewer than 7 loses nobody even at 15%)

- Applied to every unit stack proportionally

- Opinion penalty: −(5 + floor(rand×8)) = −5 to −12

**2.10.3 Iron Upkeep**

Iron upkeep deducted from iron reserves. Iron shortfall has no troop or opinion consequence — reserves go to 0 and stop.

**2.10.4 Food Consumption**

Food is consumed each turn by army headcount — **1 food per foot soldier, 2 per mounted** — the same for every race except **Nomad**, whose mounted units eat only 1 (§4.8).

foodConsumed = footCount + mountedCount × 2 (counts include this turn's recruits — §2.6a)

Embarked armies consume food normally.

**2.10.5 Starvation**

If foodConsumed \> foodAvailable:

- **Orc**: 10 + floor(rand×11) = 10–20% troop loss

- **All other races**: 3 + floor(rand×8) = 3–10% troop loss

- Applied proportionally across all non-destroyed armies

> ***▶ Example — when do my soldiers starve?** Food consumption is footCount + 2×mountedCount. An army of 200 foot + 50 mounted eats 200 + 2×50 = 300 food this turn. If your stores hold only 250, every army in the kingdom starves: a non-Orc force loses 3–10% of its troops, an Orc force loses 10–20%. Note the order of operations — **upkeep (Phase 2) runs before movement (Phase 5)**, so stock enough food before the turn you plan a big march — or a big recruitment: the men you raise this turn eat this turn — not after.*

**2.11 Phase 3 — Markets & Construction**

**Order inside the phase:** each kingdom's **market orders execute first**, then its construction orders — a sale or purchase queued this turn is available to this turn's builds, foundings, upgrades and camp moves. Prices are the turn's fixed prices for everyone; the buy/sell pressure pass that moves next turn's prices runs after every kingdom has traded. (Recruits and engines resolve earlier, in Pre-Phase 2b, and never see this turn's market — §2.6a.)

**2.11.1 Site Construction**

Players submit build orders against specific hexes. Terrain eligibility:

|            |                                             |                                                                                                                |          |                                         |
|------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------|
| **Site**   | **Required Terrain**                        | **Additional Requirement**                                                                                     | **Cost** | **Chance**                              |
| Farm       | Plains                                      | No existing site; **hex must have a construction**                                                             | 1000g    | 100%                                    |
| Mine       | Mountain / Hills / Desert / Plains / Forest | No existing site; **hex must have a construction**                                                             | 1000g    | **25% / 15% / 7% / 7% / 5%** by terrain |
| Port       | Plains *— or Forest, Elf kingdoms only*\*†  | No existing site; hex adjacent to at least one sea hex; **not Orc or Dwarf**; **hex must have a construction** | 5000g    | 100%                                    |
| Lumbermill | Forest                                      | No existing site; **hex must have a construction**                                                             | 1000g    | 100%                                    |
| Quarry     | Plains, Hills, or Mountain                  | No existing site; **hex must have a construction**                                                             | 1000g    | 100%                                    |

Mine construction is a **prospect**. Gold is spent on the attempt regardless of outcome — no refund on failure. Mine depth is terrain-capped — mountain Lv3, hills/desert Lv2, plains/forest Lv1 — and the Lv3 shaft is **Dwarven-only** (conquest degrades a captured site one level — §5.6.3 — so a captured Dwarf Lv3 arrives as Lv2, and only a Dwarven owner can dig it back down). Swamp and sea hexes cannot be prospected at all.

\\ Plains is the only port terrain open to **every** race on a map built today (the Elven exception below is the one addition). The engine also accepts the two **legacy** terrains city and capital, which the Map Editor no longer paints and which no current map contains — they exist so an old save still loads. If you are playing on a map made since the terrains were retired, read this as "plains".\*

† \***The Elven exception.** An **Elf** kingdom — and no other — may also raise a port on a coastal **forest** hex. Elves settle in the forest, and because every site needs a construction beneath it (below), an Elven realm can hold an entire coastline and still own no hex a harbour may legally stand on. The exception is a terrain whitelist, not a licence: an Elf is refused on hills, mountain, swamp and desert coasts exactly like everyone else, and the Orc/Dwarf ban outranks it (a hypothetical Orc forest coast is still closed). Two consequences worth planning around: the hex **stays forest**, so an Elven harbour is defended on land with the full Elven forest bonus (§5.2 — ×1.30) that no other realm enjoys at its ports; and once built, the port upgrades to Lv2 and Lv3 on the normal terms, since only the initial build looks at terrain. **Only under an Elven construction:** the forest hex must carry a construction of the **Elf** family (§3.7) — Elven shipwrights build only where Elves have built. Forest under a Generic or any other family's construction never takes an Elven harbour; the order is refused with the reason and the 5000g refunded. A harbour already standing on such a hex is untouched, and plains ports are not affected.\*

**A site can only be built where a construction stands.** Site output is population-scaled (§3.8) and population lives only inside constructions, so a farm, mine, port, lumbermill or quarry on a **bare hex would produce nothing, forever** — and you could never fix it, because only the GM places constructions. Rather than let you buy that, the game refuses it: **bare hexes are not offered in the build panel and the Turn Processor rejects the order**, refunding the cost. The same applies to **upgrading**: a site that somehow sits on bare ground (GM-placed, or taken by conquest) is pinned at its level and shows "✓ Fully upgraded" — there is nothing to gain by deepening it.

The terrain table above still governs *which* terrain each site needs. The construction governs *whether the hex is buildable at all*.

The Turn Processor accepts **one construction order per hex per turn**, and all six construction order types share that single slot: build site, upgrade site, raze site (§2.11.6), upgrade construction (§2.11.7), repair wall (§2.11.8) and found a new construction (§2.11.9). Issue two against the same hex in one turn and the first is kept, the second refused as a duplicate. A queued order shows on the kingdom map as a worker sign (§2.1).

**Timing — income starts NEXT turn.** Construction resolves in Phase 3, but income (Phase 1) is calculated earlier in the same turn. So a site you build (or upgrade) this turn produces **nothing this turn** — its food / iron / gold begins the **following** turn. A farm built on turn N first yields food on turn N+1 (its yield is rolled each turn — §3.6.1). Farms, ports, lumbermills and quarries complete the turn you order them (100%); a mine may take several turns just to appear (5–25%/turn by terrain), and only then begins producing the turn after it lands. This is the same one-turn lag as a tax change (§2.9.13) — anything you start this turn pays off starting next turn, because income is the first phase.

**2.11.2 Site Upgrades**

|            |                  |          |                                                                                                             |
|------------|------------------|----------|-------------------------------------------------------------------------------------------------------------|
| **Site**   | **Target Level** | **Cost** | **Chance**                                                                                                  |
| Farm       | Lv1 → Lv2        | 2000g    | 100%                                                                                                        |
| Farm       | Lv2 → Lv3        | 3000g    | 100%                                                                                                        |
| Mine       | Lv1 → Lv2        | 2000g    | 30% — mountain, hills or desert only (a plains or forest mine stays Lv1; the order is refused and refunded) |
| Mine       | Lv2 → Lv3        | 3000g    | 50% — Dwarven kingdoms only, mountain only                                                                  |
| Port       | Lv1 → Lv2        | 10000g   | 100%                                                                                                        |
| Port       | Lv2 → Lv3        | 15000g   | 100%                                                                                                        |
| Lumbermill | Lv1 → Lv2        | 2000g    | 100%                                                                                                        |
| Lumbermill | Lv2 → Lv3        | 3000g    | 100%                                                                                                        |
| Quarry     | Lv1 → Lv2        | 2000g    | 100%                                                                                                        |
| Quarry     | Lv2 → Lv3        | 3000g    | 100%                                                                                                        |

On failure, gold is spent and the level does not increase. Maximum level: 3. **Orc and Dwarf kingdoms can never upgrade a port** (§3.6) — a port they take by conquest keeps producing but is frozen at the level they captured it. And **no site can be upgraded on a hex with no construction** (§2.11.1): a settlement is what a site belongs to, so one standing on bare ground is frozen wherever it is.

**2.11.3 Refund Rules**

Every order the Turn Processor **refuses on validation** is refunded — hex captured by an enemy this same turn, wrong terrain, no construction, race gate, duplicate slot, and the like. Only **dice misses** are not refunded: a mine prospect miss and a mine deepening failure spend the gold (the mine is the only build that rolls — §3.6.2).

**2.11.4 The Market**

Five commodities: **Food**, **Iron**, **Horses**, **Wood**, **Stone**.

Base prices: Food 8g, Iron 12g, Horses 20g, Wood 5g, Stone 7g.

- **Buy price**: Current market price per unit

- **Sell price**: max(1, round(currentPrice × 0.6)) — 60% of buy price, rounded to the nearest gold (never below 1g)

- **Tradeable commodities: food, iron, horses, wood, stone.** Gold is the currency, not a commodity — it can never be bought or sold on the market (the server discards any such order), though it **can** be *sent* to another kingdom via the 📦 Send Resources panel (§2.8).

The Turn Processor re-validates all market orders server-side: a buy is **clamped** to what your gold covers and a sell to what your stock holds (partial fill, reported as "of N requested"). Only an order that would fill zero units is discarded. **The Player Page applies the same clamp to a buy as you queue it**: ask for more than your cash on hand covers and it queues what you can afford and tells you both figures — it does not refuse the whole order. Because the page counts cash only (never this turn's income), the engine may fill slightly *more* than the page queued, never less.

The Player Page validates **sell** orders against **cash on hand** (§2.12.1) — only stock you already hold; production arriving this turn is not sellable on the page even though the Turn Processor checks stock in Phase 3, after income and upkeep have landed. **Buy** orders still require the gold in hand. Ask to sell more than you can and the page queues what you can sell and tells you both figures, as it does for a buy.

One order per commodity per kingdom per turn (duplicates deduplicated, keeping last submitted). Each order is capped at **999 units** — the Player Page input stops there and the Turn Processor clamps anything larger to 999.

**The Market tab** has one row per good: what you hold and how much of it you can sell this turn, the buy and sell price with how the price moved last turn, a **Buy \| Sell** switch, the quantity (**100**, **500** or **Max** — the most your sellable stock or your gold covers, up to 999) and the gold the order moves. **Place order** queues it and folds the row to one line with **✕ Cancel**. The foot of the table adds up the gold of every queued trade. Beside each good a small chart shows its price over the **last 5 turns** and how many units all kingdoms together bought (bars above the line) and sold (below) each turn — each good's bars are scaled to its own busiest turn, so compare goods by the figures, not the bar heights; hover over or tap a turn for its figures. A good with no recorded turns yet shows no chart.

**Sales are paid out before purchases.** The page sends your sales ahead of your buys, so the gold from a sale can pay for a buy in the same turn — the page already counts it when it tells you what your gold covers.

**Cancelling a queued order** reverses it exactly — but only while its proceeds are still free. A **buy** cannot be cancelled once the purchased goods are already committed to other pending orders (e.g. a ship build placed after the purchase — recruits can never depend on a queued buy, as they are validated without it); a **sell** cannot be cancelled once its gold is committed. Cancel the dependent orders first.

**2.11.5 Market Price Dynamics**

After all trades execute, prices update for next turn. What moves a price is the **volume traded**, not how many kingdoms traded: buying 1 unit weighs a thousandth of buying 999.

- **Net volume** — every unit **bought** minus every unit **sold** of that commodity this turn, by all kingdoms together, counting what was actually traded (an order your treasury or stock could not fill counts only for what it filled). Buyers and sellers cancel each other.

- **Depth** — **half of everything the market could trade in a turn**: active kingdoms × 999 units × 50%. With 40 active kingdoms the depth is about 20,000 units; with 5 it is about 2,500.

- **The move** — the price changes in proportion to the net volume against the depth, up to **±15% a turn**: a net volume of half the depth moves it 7.5%; the whole depth or more moves it the full 15%, never more.

- **Quiet market** — when the net volume is under **5% of the depth**, the price instead drifts **1g a turn back toward its base price** — but never against the trade: a price above base that is still being bought, or below base that is still being sold, holds where it is.

|                                                     |                                                                   |
|-----------------------------------------------------|-------------------------------------------------------------------|
| **Net volume (40 active kingdoms, depth ≈ 20,000)** | **Move**                                                          |
| +1,000 (one kingdom buys 999 of it)                 | +0.75% (from 41 kingdoms this is a quiet market: the price holds) |
| +10,000                                             | +7.5%                                                             |
| +20,000 or more                                     | +15%                                                              |
| −20,000 or more (a flood of sellers)                | −15%                                                              |

**Trades use whole gold; the price behind them does not.** The market keeps each price with decimals, so small moves add up from turn to turn; every buy, sale, report and card uses that price **rounded to the nearest gold**, floored at **1g**. There is no upper cap.

The depth counts **active (order-submitting) kingdoms only** — passive/AI kingdoms don't trade, so they don't dilute it. In a small game the depth is small: one kingdom trading its full 999 moves the price noticeably; in a large one, only many kingdoms trading the same way do.

**2.11.6 Razing a Site**

You may order demolition of any production site in your own realm (Production tab → the site's card → **🏚 Raze**, confirmed with a second click). Razing is **free, instant and final**: the site — whatever its level — is gone when the turn processes, and nothing is salvaged. The hex can take a new site from the following turn, never the same turn (one construction order per hex per turn, and razing counts).

Two exceptions:

- **Forges cannot be razed** — their craft is beyond any demolition crew.

- **A port with a fleet in harbor** — yours or anyone's — refuses demolition until the harbor is clear. (A port with a pending raze likewise cannot raise a new fleet or take ship-building this turn.)

Razing before an invader arrives is a legitimate scorched-earth defense: demolition resolves in Phase 3, before armies move in Phase 5, so a doomed port or quarry can be denied to its would-be conqueror. The site is still lost to you all the same.

**2.11.7 Upgrading a Construction**

Raising a construction one rung up its family ladder (§3.7.1) is ordered from the **🏰 Constructions tab** — the settlement list under the founding panel (§2.11.9). There is **no dice roll** — every condition is checked first, and nothing is spent unless all of them pass.

The order is refused, at no cost, if any of these hold — checked in this order, so the reason you are shown is the first thing that failed:

|        |                          |                                                                         |
|--------|--------------------------|-------------------------------------------------------------------------|
| **\#** | **Refusal**              | **Meaning**                                                             |
| 1      | Duplicate                | Another construction order already claimed this hex this turn (§2.11.1) |
| 2      | Not yours                | The hex was taken from you this same turn — gold is refunded            |
| 3      | No construction          | There is nothing on the hex to upgrade                                  |
| 4      | **Foreign family**       | The construction is neither your own race's nor Generic                 |
| 5      | Besieged                 | The siege cuts off outside materials                                    |
| 6      | At max level             | Already at the top of its family's ladder                               |
| 7      | Population below ceiling | Population has not yet reached the **current** level's ceiling          |
| 8      | Insufficient gold        | Treasury short of the next level's cost                                 |
| 9      | Insufficient material    | Not enough stone/wood for the wall increment                            |

**You can never upgrade a captured foreign construction.** A Dwarf hold you storm keeps working for you — it houses population, mints militia, mans its walls, and you may repair it (§2.11.8) — but it will never grow another level under your banner. This is unconditional and does **not** consult the racial compatibility matrix; that matrix governs recruiting only (§2.12). The single exception is **Generic (POP)**, which any owner may upgrade.

**What it costs.** Gold equal to the **next** level's listed cost, plus material equal to the **wall increment only** — the difference between the next level's wall and the current one's, not the whole new wall. The material is the **construction's own fabric**, not your kingdom's: wood for the Aesir, Nomad and Orc families, stone for everyone else. So an Imperial kingdom repairing or expanding a captured Orc settlement spends **wood**, and must have wood on hand to do it.

**Dwarf master-builders.** Dwarf-family constructions pay ceil(points / 2) — one stone buys two points of wall. This is a *cost* advantage only; the wall itself is no tougher than its listed value.

**What you get.** Level +1. The wall rises by the increment and then clamps to the new maximum, so a damaged wall is partly healed by expanding — repair covers whatever the increment doesn't. **Population is kept exactly as it was** and simply resumes growing toward the new, higher ceiling next turn (§3.8).

> ***▶ Example.** An Imperial FI10 at population 1,000 (its ceiling) with a 500-point wall, upgrading to FI11: costs **4,000 gold** (FI11's price) and **500 stone** (the 1,000 → 500 wall increment). The wall ends at 1,000/1,000, population stays 1,000, and next turn it starts growing toward FI11's ceiling of 2,000.*

**2.11.8 Repairing a Wall**

Wall integrity does **not** mend on its own. Rebuilding it takes an explicit repair_wall order — one hex, no parameters, repairing as much as the cap and your stores allow.

Refusals, again in check order: duplicate; not yours; no construction; **no wall** (a wall-less family level — Orc Lv.1–3, Generic Lv.1–4, §3.7.2); **besieged**; **wall intact** (nothing to mend); insufficient material.

**How much.** At most **10% of the wall's maximum** per turn — floor(wallMax × 0.10) — and never more than the damage actually present. That figure is then capped again by what you can pay for: **one unit of material per point** mended, or ceil(points / 2) for Dwarf-family constructions. **A partial repair still succeeds** — if you can only afford half, you mend half and spend what you had.

Two rules that decide sieges:

- **Only an active siege blocks repair.** A hostile army merely *camped* on your hex — sitting at the gates without Siege stance — does not stop your masons. This is a deliberate tradeoff: an attacker who camps keeps his options open but lets you rebuild; an attacker who commits to Siege stance stops the repairs but commits.

- **The current owner repairs, whoever built it.** Unlike upgrading, there is no foreign-family gate here. Take a Dwarf hold and you may mend its walls — paying in the Dwarf family's stone, at the Dwarf family's favourable rate.

> ***▶ Example.** An Imperial FI11 (wall max 1,000) beaten down to 800 has 200 points missing, but the turn's cap is floor(1,000 × 0.10) = 100. With 2,000 stone in the treasury it mends exactly **100 points** for **100 stone**, ending at 900/1,000. With only 50 stone on hand it would mend **50** and end at 850 — still a success, just a smaller one.*

**2.11.9 Founding a Construction**

A kingdom is not limited to the settlements the GM placed at campaign start. Any kingdom may charter a brand-new settlement on bare ground it holds: a party of settlers marches out of your muster seat, and where they stop a construction of your own family goes up.

**Where the order lives.** The **🏰 Constructions tab** — its own tab in the Player Page's left-hand nav. The founding panel sits at the top ("🏗 Found a New Settlement"), and below it is the list of every construction you already own, with its upgrade and wall-repair buttons. Each settlement card, and each founding tier, wears the picture of the people whose family it belongs to — a captured Dwarven hold keeps the mountain hold — the same one the map's **Constructions+** layer draws: a yurt for the Nomads, a longhouse for the Aesir, an elven palace for the Elves, a mountain hold for the Dwarves, a war camp for the Orcs, a columned temple for the Imperials, a citadel for the Barbarians, and a village for a common (POP) settlement. **The Production tab covers production sites only** (farms, mines, ports, lumbermills, quarries, forges — §2.11.1–§2.11.6).

**No dice roll, and a refusal is free.** Like upgrading, founding is decided entirely by the gates below. They are checked **in order, before a single coin is spent**, so an order that fails costs you nothing at all — no gold, no material, no settlers. The panel mirrors the same gates and will not offer you a hex the engine is going to refuse.

**Founding needs an era map.** This order does not exist until at least one construction already stands somewhere on the map. A legacy map with none yet has no population economy for founding to plug into — turning it on with a single order would zero every OTHER kingdom's bare-hex population in the same turn, so the game refuses outright until the GM has placed the map's first construction.

**The refusals, in the exact order the game checks them.** If more than one applies you are told about the first — fix that, and the next may still be waiting.

|        |                       |                                                                                                                    |                                                                                                                                                                                                                                                        |
|--------|-----------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\#** | **Refusal**           | **What it means**                                                                                                  | **What to do about it**                                                                                                                                                                                                                                |
| 1      | No charter            | The map carries no constructions at all, so founding does not exist in this campaign                               | Nothing you can do — only the GM can place the map's first settlement                                                                                                                                                                                  |
| 2      | Already founded       | Your court has already chartered a settlement this turn — **one per kingdom per turn**, however many hexes qualify | Cancel the queued founding if you want the other hex instead, or wait a turn                                                                                                                                                                           |
| 3      | Not yours             | The hex is not on the map, or you did not hold it when the turn was processed                                      | Ownership is read at processing time, not planning time — pick a hex you are confident you will still hold                                                                                                                                             |
| 4      | Open water            | Settlers cannot be planted on a sea hex                                                                            | Pick land                                                                                                                                                                                                                                              |
| 5      | Occupied              | A construction already stands there                                                                                | Upgrade it (§2.11.7) instead of founding. Note that a *production site* on a bare hex does **not** block founding — you may settle a hex that already carries an idle farm or mine, and it starts earning the turn after the settlers arrive (§2.11.1) |
| 6      | Besieged              | A siege sits on that ground                                                                                        | Break the siege first (§5.8), then send the settlers                                                                                                                                                                                                   |
| 7      | Hostile army          | A non-friendly foreign army is standing on the target hex (see below)                                              | Drive it off, or settle somewhere else this turn                                                                                                                                                                                                       |
| 8      | Foreign family        | You tried to found in a tradition that is neither your race's nor the common Generic one                           | Choose your own family or Generic in the panel's family picker                                                                                                                                                                                         |
| 9      | No seat               | You hold no muster seat to send settlers from — including the case where your seat was **captured this turn**      | Retake a seat, or wait: your seat relocates by itself the turn after it falls (§2.13.10)                                                                                                                                                               |
| 10     | **Your own seat**     | The hex you picked **is** your muster seat                                                                         | Pick a different hex — settlers are sent *out* of the seat, never back into it (see below)                                                                                                                                                             |
| 11     | Too few settlers      | Your seat's population is below the threshold needed to send a party and still stand                               | See "the settler threshold" and "the trap" below — this one has a nasty version                                                                                                                                                                        |
| 12     | Insufficient gold     | Treasury short of the 500-gold blueprint                                                                           | Raise the gold first; the treasury is read at processing time, after this turn's income                                                                                                                                                                |
| 13     | Insufficient material | Not enough stone or wood on hand for the new settlement's wall                                                     | Buy it on the market (§2.11.4), or found a wall-less tier                                                                                                                                                                                              |

One more card can come back that is not a gate: **duplicate**. All six construction order types share **one slot per hex per turn** (§2.11.1), so if the target hex already carries a queued build, upgrade, raze or repair order, the founding is dropped as a duplicate — first order in wins.

**What it costs.** Every founding pays the same **500-gold blueprint**, whatever the family and whatever the tier, plus **100 settlers** marched out of your muster seat, plus the founding tier's **full wall maximum** in the family's building material — not an increment, the whole wall, because there is no existing wall to increment from. Dwarf-family founding pays the usual master-builders rate of ceil(points / 2) stone (§2.11.7). **A tier with no wall costs no material at all**: that is Orc Level 0 (below), Nomad Lv.1 (the settler camp) and Generic Lv.1, which stand at wall 0 (§3.7.1a).

**The settler threshold — what your seat is left with.** The party that leaves is always exactly **100 people**, and that is exactly what your seat loses: a seat of 1,000 comes out at 900. Recruitment (Pre-Phase 2b) draws from the seat *before* the founding is tested in Phase 3, so with a settler party queued the Player Page refuses any recruit at the seat that would leave fewer than the threshold behind (the message names the count that would remain); queue the founding after the recruits and the same test runs at once. What the threshold controls is whether the party may leave at all — your seat must hold **300** at processing time. Below that the order is refused (gate 11) and nobody moves. So a 300-population seat may just barely found, and ends the turn at 200; a 299-population seat may not found at all. The founding panel prints the resulting figure for your actual seat before you commit, and **the moment you queue the order the page takes the 100 off your seat's population** — the 👥 total and the seat's own figure both drop at once, exactly as they already do for a recruit drawn from that hex, and cancelling the order puts them back.

**You cannot found on your own muster seat.** Gate 10 refuses it outright. Your seat is already a settled place with a role of its own — it is the hex the settlers march *out* of, and sending them out only to plant them back on the same ground is not a move the game recognises. The founding panel does not list the seat as a target either, so on a normal turn you will never see this refusal; it exists because the engine, not the page, is the authority.

**Founding never destroys population.** The new settlement opens with **the larger of the 100 settlers and whatever the hex already held**. On a clean era map a bare hex holds nobody, so the answer is simply 100. On an older or migrated map a bare hex can already carry people — founding there gathers them into the new settlement and adds nothing, rather than replacing them. A founding order can never lower a hex's population, anywhere on the map.

**A settlement founded this turn takes no part in that turn's fighting.** For the rest of the turn it counts as **unfortified**, exactly as the bare hex it was an hour ago:

- it confers **no fortress bonus** to a defender and imposes **no attacker penalty**;

- it has **no inside/outside wall zones** — the hex fights under the ordinary flat stacking rule;

- it **cannot be besieged or assaulted**, and there is no garrison stance to take on it;

- **siege engines do it no damage**, because there is nothing to batter yet.

The wall is nonetheless real from the moment it is built: it is stored at full integrity, it can be repaired and upgraded from the next turn, and a spy who looks at the hex sees it. The reason for the rule is fairness of timing. Founding resolves in Phase 3; marches land in Phase 5 and sea landings in Phase 6. Without this, 500 gold spent *after* an enemy had already written their orders would turn a march onto open ground into an assault against walls that did not exist when either side planned the turn. **A fight already in motion is fought on the ground both sides planned against.** Note the practical asymmetry: for Orc (Level 0), Nomad (FNO1) and Generic (Lv.1), whose founding tier has no wall at all, this rule changes nothing — there was never a wall to switch off.

**⚠ The trap: a small seat can never found, no matter how long you wait.** Population growth **saturates at the ceiling of the tier you have paid for** (§3.8) and stops there. It follows that if your muster seat's current level holds fewer than 300 people, that seat will **never** reach the settler threshold by growing — it will sit at its ceiling forever, one refusal after another. Six of the eight families start at a Lv.1 ceiling of **100**, so a brand-new or freshly degraded seat is very often in exactly this position.

There is only one way out: **upgrade the seat** until its ceiling is 300 or more, then let it grow (§2.11.7). Nothing else works — in particular, **your tax rate has no effect whatsoever on population growth**, and neither does income, food or anything you can spend. The founding panel says so on the spot: when your seat's own tier caps below the threshold it names the ceiling and tells you to upgrade the seat.

**The family is permanent.** The race you found with — your own, or Generic — is that settlement's family for as long as it stands. There is no order to change it afterward; only conquest (§5.6.3) and the foreign-family upgrade lock (§2.11.7) ever touch it again.

**One per turn, sharing the per-hex slot too.** A kingdom may charter at most one new settlement per turn (gate 2), no matter how many eligible hexes it holds. The target hex still competes for the same single construction-order slot every other construction order type uses (§2.11.1).

**A non-friendly foreign army standing on the hex blocks founding outright.** Gate 7 refuses the order before anything is spent: it fires on any army standing on the target hex that is not yours, not a mutual ally's, not your liege's and not one of your vassals'. Those four never trigger it — the settlement goes up around them exactly as before. The rule is one line — an enemy stands on it, you cannot settle it — and it applies to every founding, walled or not.

> ***▶ Example.** An Imperial kingdom with a seat at 1,000 population founds an FI1 settlement on a bare hex: 500g blueprint + 500 stone (FI1's full wall) + 100 settlers. The seat drops to 900; the new hex opens at population 100, wall 500/500 — and for the remainder of that turn it fights as open ground. An Orc kingdom doing the same instead founds FOR0: 500g + 100 settlers only — no wood spent, because Level 0 has no wall.*

**2.11.10 Moving a Camp — Nomad only**

A Nomad people does not build to stay. **One camp per turn** may strike its tents and pitch them again on another hex you hold, **up to 2 hexes away**, for **1,000 gold**. Each camp then **rests 6 turns** before it can move again. The order lives in the **⛺ Move a Camp** panel at the top of the Constructions tab, above "Found a New Settlement".

**Which camps can move.** Any construction of the **FNO (Nomad) family** standing on a hex you hold. A settlement of any *other* family — Generic, or one you took from an Imperial or Elven neighbour — never moves: it was built of stone and mortar and stays where it was laid. A camp you captured from *another Nomad kingdom* is FNO and **can** be moved — with one exception: if it carries that realm's **ancestral capital** (the hex their kingdom was founded on), it is bound to that ground and cannot be carried off it. A conquered camp also arrives carrying whatever remains of its previous owner's rest.

**One order, two steps, one turn.** A camp move is not resolved where you queue it:

1\. **Construction phase (Phase 3).** Every gate below is checked and the **1,000 gold is taken**. Nothing has moved yet. Your report carries a **"Camp packing up"** card naming both hexes and the fee.

2\. **End of the turn**, after all recruitment, marching, fighting and naval landings are finished. The gates that could have changed in the meantime are checked *again*, and only then do the tents actually come down. Your report carries **"Camp moved"** — or **"Camp move cancelled"**, with the 1,000 gold back in your treasury. An order that fails a gate in step 1 instead carries **"Camp move refused"** and costs nothing.

**Why the end of the turn.** It serves the same principle as the founding-turn holiday (§2.11.9), by a different means: *a battle already in motion is fought on the ground both sides planned against.* Founding keeps a brand-new settlement's walls out of that turn's fighting; a camp move simply does not happen until the fighting is over. Your camp stands exactly where your enemy expected it for the whole of the turn they attacked it, and it leaves only once the dust has settled. You can never use a move to dodge a fight that is already coming.

**A camp crosses only its own ground.** A camp is carried, not flown: a move of **2 hexes** passes over a **middle hex**, and at least one middle hex must be **land you hold, clear of foreign armies and fleets, for the whole turn**. In a straight line there is one middle hex, and it must be clear. Off the straight line there are two, and one clear one is enough. A **1-hex** move has no middle hex, so this rule never applies to it — the destination rules below still do.

"Foreign" means anyone except you, a mutual ally, your liege or your vassal. Only land and forces count: a settlement, people or a production site on the middle hex do not block. A middle hex is closed if:

**Checked when you order (a refusal, nothing paid) and again at the end of the turn:**

|                                   |                                            |
|-----------------------------------|--------------------------------------------|
| **What closes it**                | **What the card says about that hex**      |
| It is open water                  | *is open water*                            |
| Nobody holds it                   | *belongs to no one*                        |
| An ally, liege or vassal holds it | *is an ally's land (only your own counts)* |
| Another realm holds it            | *is another realm's land*                  |
| A foreign army stands on it       | *holds a foreign army*                     |
| A foreign fleet lies in its port  | *has a foreign fleet in its port*          |

**Checked only at the end of the turn, once the marching and sailing are over (they cancel an accepted move, and the 1,000g comes back):**

|                                                                                                                          |                                                   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| **What closes it**                                                                                                       | **What the card says about that hex**             |
| It was yours when you ordered, and it was taken during the turn                                                          | *was taken from you this turn*                    |
| A foreign army entered it during the turn — it attacked your army or your walls there, or took the hex and lost it again | *was entered by a foreign army this turn*         |
| A foreign fleet put into its port during the turn, even if it sailed on                                                  | *had a foreign fleet put into its port this turn* |
| There was fighting on it that no army entered — a raid your settlement's militia threw back, or a landing                | *saw fighting this turn*                          |

A foreign army cannot walk through your land in peace: entering your hex is always a fight — with your army, your walls or your militia — so a foreign army that goes near your middle hex always leaves one of those marks behind it. Only one reason is given per hex: the first that applies, in the order of the tables. The card is headed *"No clear way for the tents:"* and names **every** middle hex with its reason, so you always know which way was closed and why. It does not say whose force it was.

> ***▶ Example — the way over.** Your camp stands at (27,31).*
>
> *• **To (29,31), straight east.** There is one middle hex, (28,31). If it is yours and clear, the camp moves. If a neighbour holds (28,31), the order is refused and costs nothing: "No clear way for the tents: (28,31) is another realm's land".*
>
> *• **To (29,32), off the straight line.** There are two middle hexes, (28,31) and (28,32). The neighbour still holds (28,31), but (28,32) is yours and clear: **the camp moves** — one clear way is enough.*
>
> *• **The same order, with a neutral fleet lying in the port on your (28,32).** Both ways are closed, and the refusal names both: "(28,31) is another realm's land, and (28,32) has a foreign fleet in its port".*
>
> *• **The same order, with (28,32) clear when you order it.** Phase 3 accepts it and takes the 1,000g. Then, during the turn, one of these happens:*
>
> *– an enemy army marches onto (28,32) and takes it → cancelled: "(28,32) was taken from you this turn";*
>
> *– (28,32) holds one of your settlements (that alone never blocks), an enemy raid hits it and its militia throws the raid back → cancelled: "(28,32) saw fighting this turn". A bare hex has no people and no militia, so a raid on it takes it instead (the line above);*
>
> *– a neutral fleet sails into the port on (28,32) and out again → cancelled: "(28,32) had a foreign fleet put into its port this turn".*
>
> *Each time the 1,000g comes back and the camp never leaves (27,31).*
>
> *• **To (28,32), next door.** A 1-hex move has no middle hex, so the way over never closes it — whoever holds the land around it. The destination itself must still pass every gate in the table below: your own land, no settlement, no people, no siege, no foreign army.*

**What travels, and what stays:**

|                                                                                   |                                                         |
|-----------------------------------------------------------------------------------|---------------------------------------------------------|
| **Travels with the camp**                                                         | **Stays behind**                                        |
| Every one of its people                                                           | Production sites (farm, mine, quarry, lumbermill, port) |
| The palisade, at its **current** integrity — a wall at 180/300 arrives at 180/300 | Fleets docked at a port on the old hex                  |
| The camp's level, and therefore its population ceiling                            | Armies standing **at the capital** (see below)          |
| Its rest counter, which restarts at the new hex                                   | Ownership of the old hex — it stays yours, simply empty |
| Your **muster seat**, if it stood on this camp                                    | Any memory an enemy has of the camp (see below)         |

**The hex you leave is emptied, not lost.** It stays your territory, but its population drops to **zero** and — because bare hexes are never seeded or grown (§3.8) — it stays at zero until a camp stands there again. That means no tax from it, no militia on it, and nothing for a site to work.

**A site left behind goes dormant, not derelict.** A site earns from the **people** on its hex, and on a constructions map only a hex carrying a settlement has any (§3.6, §3.8) — so a site whose camp has left produces nothing at all. The quarry you walk away from keeps its level and produces **nothing** until a camp stands there again — move back, or found there, and it earns exactly as before, at the level it had. This is the real price of moving, and it is why a camp grown fat beside a good port rarely moves at all. One consequence worth planning around: a **port** whose camp has left still works as a dock for your fleets, but with nobody living on the hex it can no longer crew a hull (§2.12.3).

**Your seat travels with the camp it sits on.** This is the one exception to "your seat changes only by conquest" (§2.13.10). The succession *ranking* is untouched and still runs only when a seat hex is captured — a moving camp simply carries the existing seat with it. Armies sitting **at the capital** do **not** ride along: they become field armies standing on the ground the camp left, including any you recruited that same turn. Your "Camp moved" card names them.

**The rest between moves.** A camp that moves on turn *N* may move again on turn *N + 6*. **Founding starts the rest too**, so a settlement you charter this turn cannot pack up for another six. Three things do **not**: a camp the GM painted at the start of the campaign has never been pitched and is ready on turn 1; **upgrading** a camp does not restart its rest; and a camp you **capture** arrives carrying whatever remains of its previous owner's rest. The Move panel shows each camp's state, and a refusal card names the turn it comes ready.

**Enemy charts do not see it go.** A kingdom that cannot currently see the hex keeps the camp drawn on its map, faded, exactly as it last saw it (§2.19). It learns nothing until it looks again. Nothing on its page announces that a camp moved.

**Ordering it, and taking it back.** Pick the camp and its destination in the **⛺ Move a Camp** panel. The camp list shows every FNO camp you hold with its state — *ready*, or *resting — ready on turn N*, or besieged, or blocked by a foreign army — and the destination list offers the land you hold within range with nothing standing on it and, for a 2-hex move, a way over your own land past every foreign army you can see — armies hidden from you, fleets and anything that happens during the turn are judged by the turn processor, and the card tells you what it found. The panel also names any site that will fall idle and warns you when your seat is about to travel. Queuing takes the 1,000 gold off your displayed treasury straight away, so the rest of your planning stays honest about what you can still afford, and it draws a gold arrow on your kingdom map from the camp to where it is going (with the constructions layer on). **Cancel**, in the same panel, puts the full 1,000 back and frees both hexes. While the move is queued **neither hex will accept another construction order**, because a move claims the slot on both.

**Gates, in the order the engine checks them.** Nothing is spent until every one has passed, and a refusal costs nothing:

|        |                 |                                                                                                                                                               |
|--------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\#** | **Refusal**     | **Meaning**                                                                                                                                                   |
| 1      | not_era         | This campaign has no constructions at all.                                                                                                                    |
| 2      | not_nomad       | Only a Nomad people moves camps.                                                                                                                              |
| 3      | already_moving  | A camp move has already been **accepted** for you this turn — a refused one does not use up your turn.                                                        |
| 4      | no_construction | There is no camp on that hex.                                                                                                                                 |
| 5      | foreign_family  | It is not an FNO camp.                                                                                                                                        |
| 6      | foreign_seat    | The camp carries another realm's ancestral capital.                                                                                                           |
| 7      | dest_missing    | The destination is not on the map.                                                                                                                            |
| 8      | out_of_range    | The destination is the camp's own hex, or further than 2 hexes.                                                                                               |
| 9      | duplicate       | Another of your construction orders already claims the **destination** — a move takes the slot on both hexes.                                                 |
| 10     | dest_not_yours  | The destination is not land you hold.                                                                                                                         |
| 11     | dest_not_land   | The destination is open water.                                                                                                                                |
| 12     | dest_occupied   | The destination already carries a settlement.                                                                                                                 |
| 13     | dest_inhabited  | People already live on the destination — rare on an ordinary map, where a hex with no settlement has no people, but possible on a hand-built or migrated one. |
| 14     | path_blocked    | A 2-hex move has no middle hex of your own land clear of foreign armies and fleets; the card names each middle hex and why (see the table above).             |
| 15     | besieged        | A siege sits on the camp or on the destination.                                                                                                               |
| 16     | hostile_army    | A foreign army stands on the camp or on the destination.                                                                                                      |
| 17     | on_cooldown     | The camp is still resting; the card names the turn it is ready.                                                                                               |
| 18     | no_gold         | The 1,000g is not on hand when the turn is processed.                                                                                                         |

One note on that table. If you file a second construction order on the camp's **own** hex, the check that all six other construction orders share refuses one of the two, and the card it writes is titled **"Camp move from (col,row)"** — the move is the order it drops, so queue the two in the order you care about most.

**The second check, at the end of the turn.** A queued move is cancelled — and the **1,000 gold refunded** — if, once the fighting is over: the camp's hex or the destination changed hands; the camp is gone; something now stands on the destination, or people have settled there; a siege closed around either hex; a foreign army is standing on either hex; the way between closed — no middle hex is still your own and clear, for any reason in the table above (taken, a force standing or passing, fighting); or **the camp was fought over during the turn**. That last test is the plain one: any battle on the camp's hex pins it — a storm it repelled, a capture, a bombardment, a landing. A camp that saw fighting does not strike its tents, whatever the outcome and whether or not the enemy is still standing.

> ***▶ Example.** An FNO4 camp of 1,089 people with a 300-point palisade and a Lv.2 quarry sits at (27,31), and it is your seat. You order it to (29,32), two hexes away — the limit — over (28,31) and (28,32), both yours. In Phase 3 the 1,000g leaves your treasury and you get a "Camp packing up" card. The turn's fighting happens around the camp where it stands. At the end of the turn all 1,089 people arrive at (29,32), the palisade arrives at 300, your gold ★ moves with it, and Army I — which was at the capital — is left standing on (27,31) as a field army. The quarry stays at (27,31) and earns nothing until a camp returns. The camp can move again on turn N+6.*

**2.12 Recruiting (Pre-Phase 2b) and Phase 4 — Ships & Hire**

**2.12.1 Recruiting Units**

Units are recruited to specific armies. Costs are deducted in **Pre-Phase 2b** (§2.6a — before income, upkeep and markets); the recruits are in the army for **every** battle of the turn, standing or marching. Population is deducted from the recruit hex — **except siege engines, which draw no population at all** (they are *built*, not levied — see the engine rules below and §5.8.6).

**The treasury is a hard wall.** The Turn Processor grants only what your stores fully cover, *checked before anything is minted*: an order the treasury cannot pay in full is **trimmed to the affordable quantity** (a card names the trim and the binding resource) and an order it cannot pay at all is **refused outright — nothing minted, nothing charged**. The same applies to shipbuilding (crew is drawn only for the hulls actually built), to **production sites** (a build or upgrade you cannot pay for is refused before the attempt — mine prospects included), and to **spy missions** (an unpaid mission is *not dispatched*: no agent leaves, nothing is charged, and the card says so plainly — never the "agent lost" wording). There is no overdraft and no forgiven shortfall anywhere.

**Affordability is cash on hand minus this turn's outflows.** The Player Page lets you commit only the treasury your report shows **less the upkeep, army food and vassal tribute the Turn Processor will charge in Phase 2** — and, for recruits, their own first-turn upkeep and food — and validates recruits, ship builds, hires, spies, constructions and founding against that figure; this turn's income, although the Turn Processor credits it (Phase 1) before it charges most orders (Phases 3–4), does **not** count on the page. Two ordering rules follow from the server: a **queued market sale counts toward this turn's constructions, foundings, upgrades and camp moves** (markets resolve before construction, inside Phase 3 — §2.11) but **never toward recruits or engines** (Pre-Phase 2b, before any market — §2.6a), and a queued **buy** or **send** is deducted on the page at once even though the server charges it later — so the page can be stricter than the server, never looser. An order the page allows is always one the Turn Processor can pay, and the balance shown never goes negative.

**Recruit locations and per-turn caps:**

|                  |                         |                          |
|------------------|-------------------------|--------------------------|
| **Hex type**     | **Terrain restriction** | **Per-turn cap**         |
| Own territory    | Any with population     | 5% of hex population     |
| Allied territory | Any with population     | **1%** of hex population |

The cap binds to the hex's population **as the report shows it** — recruitment (Pre-Phase 2b) resolves before this turn's Phase-1 growth, so the Player Page's preview and the server's cap are the same number. The cap is floored (24.7 → 24) on both sides.

Cap formula: max(1, floor(hexPop × capPct)), measured against the hex's population at the **start of Pre-Phase 2b** (before this turn's growth, snapshotted when recruitment first touches the hex). This is a per-turn **total**: splitting recruitment across several orders does not raise it — once a hex has given its 5% (own) or 1% (allied) for the turn, further recruitment there is trimmed to zero until next turn. The owner's 5% and an ally's 1% at the same hex are separate allowances. **Ship crews draw from the same allowance**: the people a Phase-4 build_ship takes at a port count against that hex's 5% for the turn, after the turn's recruits — see §2.12.3. If hex population is zero, recruitment fails. An army already at sea (embarked on a previous turn) cannot recruit — disembark first. You *may*, however, recruit at a port and embark the same army the same turn: the army boards first (Pre-Phase 2), the recruits are raised at the port an instant later (Pre-Phase 2b) and are counted aboard before the fleet sails in Phase 6 — queue the recruits *before* the embark order, the Player Page refuses the reverse.

**You recruit from a construction, and it decides what you may raise.** Population lives only inside constructions (§3.8), so an army standing on bare ground raises nothing at all — there is no one there. More than that: *which* units a hex will muster depends on **whose settlement it is**.

|                                    |                                                                                                       |
|------------------------------------|-------------------------------------------------------------------------------------------------------|
| **The construction you stand on**  | **What it will raise for you**                                                                        |
| **Your own race's**                | Your entire roster — anything your kingdom can build                                                  |
| **Generic (POP)**                  | Your entire roster. Generic has no people of its own, so it musters yours                             |
| **A foreign race's**, compatible   | **Only that race's two-unit pair** (below) — never your own troops, never elites, never siege engines |
| **A foreign race's**, incompatible | Nothing                                                                                               |
| **None** (bare hex)                | Nothing                                                                                               |

**Compatibility is mutual** — if Dwarves will muster for Elves, Elves will muster for Dwarves. Who works with whom:

|                        |                                                      |
|------------------------|------------------------------------------------------|
| **Recruiting kingdom** | **Will raise troops at these foreign constructions** |
| Imperial               | Everyone — the Empire deals with all                 |
| Barbarian              | Imperial, Dwarf, Orc, Aesir, Nomad                   |
| Dwarf                  | Imperial, Elf, Barbarian, Aesir                      |
| Elf                    | Imperial, Dwarf                                      |
| Aesir                  | Imperial, Dwarf, Orc, Barbarian                      |
| Orc                    | Imperial, Barbarian, Aesir                           |
| Nomad                  | Imperial, Barbarian                                  |

*(Generic is compatible with everyone and is not listed. A kingdom is always compatible with its own race.)*

**The two-unit pairs** a foreign settlement will offer — its commonest troops, never its finest:

|            |                          |
|------------|--------------------------|
| **Family** | **Offers**               |
| Imperial   | Velites, Legionnaire     |
| Barbarian  | Berserker, Raiders       |
| Elf        | Swordmaster, Bladedancer |
| Dwarf      | Ironclad, Warrior        |
| Orc        | Goblin, Uruk-Hai         |
| Aesir      | Shore Raider, Axe Thane  |
| Nomad      | Rajjala, Naffatun        |

**Troops of other peoples are at most 20% of an army.** "Other peoples" are units of any race but your kingdom's own — in practice the pairs above, raised on a foreign settlement. Every unit of the army counts towards the total, **siege engines included**. The limit is checked whenever an army's mix changes by your order:

- **Recruiting.** The room left is the largest number of foreign troops that keeps them at **20% or less** of the whole army *after* they arrive — a quarter of the army's own (non-foreign) units, rounded down, minus the foreign troops it already has: 20 own → room for **5**; 80 own → **20**; 100 own → **25**; 80 own + 20 foreign → **0**. Order more and the Turn Processor recruits only what fits; the recruit card says *Trimmed: ordered 30, got 20 (foreign troops at most 20% of an army)*, or, when there is no room at all, *Recruitment failed* with the army's count.

- **A new army cannot start foreign.** An army with no troops has no room — recruit your own people into it first. Recruited the **same turn**, they count: own-race recruits and engines are always counted before foreign ones, whatever order you file them in.

- **When it is counted.** Recruitment resolves in Pre-Phase 2b — **after** this turn's dismissals and **before** this turn's transfers and splits (Phase 4.5). So a transfer queued this turn does not yet give or take room for this turn's recruits; the Player Page counts the same way.

- **Transfers, merges and splits** are refused whole if either army would end **over 20% foreign** — or, for an army already over, **more foreign than it was** (compared as a share). Handing your *own* troops out of a mixed army counts too: the troops left behind become more foreign. A split cannot create an army over 20% foreign.

- **Dismissals** follow the same test: dismissing your own troops is refused if it would leave the army over 20% foreign (or more foreign than it was); dismissing foreign troops is always allowed. The Player Page also refuses a dismissal that would leave no room for foreign recruits you already queued this turn — undo some of them first.

- **An army that ends up over 20% keeps every soldier it has.** That happens when it was over before this rule, or through **battle losses** and **attrition**, which are never refused. It simply takes no more foreign troops; your own people may always join it, and a transfer or split may not make it more foreign.

- **What you see.** The Enlisted Units box shows each army's share (*Other peoples: 20 of 100 (20%) · cap 20%*, in red when over). On a foreign settlement each offered unit says *room for N more* and greys out with the reason when there is none; a refused transfer, split or dismissal names the army and its count.

> ***▶ Example — the 20% rule through one turn.** Army I (80 Legionnaires) stands on a captured Dwarf hold; Army II (10 Legionnaires) stands beside it.*
>
> *- **Recruit.** You order 30 Ironclads into I. Room is 80 ÷ 4 = **20**, so 20 arrive (20 of 100 = 20%) and the card says the order was trimmed. Next turn I has no room left: 20 of 100 is already the limit.*
>
> *- **Hand out own troops.** You order I to transfer 50 Legionnaires to II. I would keep 30 Legionnaires + 20 Ironclads — 20 of 50 is 40% — so the transfer is **refused**.*
>
> *- **A mixed transfer.** You send 10 Legionnaires and 5 Ironclads from I to II instead: I keeps 15 of 85 (17.6%), II becomes 5 of 25 (20%) — both within the limit, so it goes through.*
>
> *- **A split.** Peeling the 20 Ironclads off into a new army would make it 20 of 20 foreign — **refused**.*
>
> *- **An army already over.** An army of 10 Ironclads (from before the rule) keeps them. It takes no more foreign troops, but 10 Legionnaires may join it (10 of 20 — less foreign than before).*

**Siege engines are built, not levied.** Engines stand outside the whole construction system above. A **standing army** builds its own race's engines **wherever it stands on land — your own ground, an ally's, a neutral's or the enemy's siege camp alike**, construction or none, drawing **no population** and paying **materials only** (250g + 50w + 10i each, straight from your stores under the hard-wall rule above). Four limits remain: **(1)** only your **own race's** engine — no foreign designs, whatever construction is underfoot; **(2)** the order must name an **existing army** — an engine order can never raise a new one; **(3)** an army **embarked at sea** cannot build (same as any recruit); **(4)** the **crew ratio**: every engine needs a crew of **5 soldiers**, counted as a *standing* ratio — the army's total engines after the build may never exceed floor(soldiers ÷ 5), where **only non-engine units count as crew** (engines cannot crew engines). 25 soldiers support at most 5 engines, this turn or ever, until the army grows. Losses never destroy engines retroactively — a shrunken army simply cannot build more, and only crewed engines fire (§5.8.6). Orders beyond the ratio or the treasury are trimmed with an explanatory card.

All of this applies **identically on an allied hex**; only the cap changes (**1%** instead of 5%). **The pools are independent:** your 1% and the owner's own 5% are separate ceilings on the same town, and two allies levying it in one turn each get their own 1% — a town can lose up to 5% plus 1% per allied recruiter. **Your ally is told:** every levy from an allied town puts an *Allied recruitment at (col,row) — −N population* card in the owner's report naming who recruited what and the town's population before and after. The compatibility test always runs between *your* race and the *construction's* race — your ally's race never enters into it. So standing on an ally's captured Orc settlement, an Elf raises nothing, because Elves and Orcs will not muster for one another, whoever owns the ground.

> ***▶ Example.** An Imperial army holding a captured Dwarf hold may raise **Ironclads and Warriors** there — as many as fit the 20% limit below — and not a single Legionnaire, because a foreign settlement never musters your own people. To raise legions, march to a hex with an Imperial or Generic construction.*

**Force limits.** A kingdom may field at most **10 armies** (slots I–X) and **5 fleets** at once. The per-hex stack (3 armies), the link group (3) and the room at the muster seat still apply: with ten armies you can never raise more than three before moving some out, nor march more than three together. On the Player Page's Army tab the raised armies get their full cards; the unraised slots fold into a single strip at the top — one chip per slot, the next slot carrying the Raise button, a destroyed slot keeping its 💀 until re-raised, and a hint line saying why raising is blocked (Orc and Dwarf field no fleets at all), plus up to **10 living characters**. These caps are enforced by the **Turn Processor**, not merely the Player Page UI — a hand-edited orders file requesting an 11th army or a 6th fleet is rejected server-side. Disbanding (or losing) an army/fleet frees a slot.

> ***▶ An empty army or fleet does not survive the turn.** At the end of every turn any army with **no soldiers** and any fleet with **no ships** is struck from the rolls and its slot is freed. Recruitment and shipbuilding resolve earlier in the turn, so **raising a force and filling it in the same orders file is safe** — but raising one and leaving it empty is not: it will be disbanded before the turn ends, and you will need to raise it again. You cannot hold an empty slot in reserve.*
>
> *An army with no troops cannot be found, fought, or kept. The slots themselves are **I–X** for armies and **I–V** for fleets, and nothing else: the Turn Processor refuses a create_army/create_fleet order carrying any other numeral, naming the legal slots on the refusal card.*

On the Player Page maps (mini-map and Army map) and army cards, your armies are marked with your kingdom's **nation shield** (the same shield shown on the Profile tab — kingdoms of the same race receive distinct shields automatically) with the army's numeral **I to X** on a small badge low on the shield. Allied armies (any confirmed ally — a declared or mutual alliance, your liege, or one of your vassals) also wear that ally's **nation shield** on the mini-map and Army map — without the numeral badge, as their internal army numbers aren't shown to you. Armies of kingdoms you are at **war** with show a distinct enemy emblem, and armies of **neutral** kingdoms (peace or undeclared) show a distinct neutral emblem, on those same two maps; a rival's own nation shield is never shown to you. **Fleets are marked the same way, with an anchor (⚓) added to the shield to mark it as a fleet rather than an army:** your own fleets show your nation shield with the fleet's numeral **I to V** and the anchor; foreign fleets show the owner's stance emblem — an allied nation shield, or a distinct war or neutral naval shield — each with the anchor. These shield markers appear consistently across all three surfaces — the mini-map, the Army map and the Navy map (foreign land armies on the Navy map wear their stance shields too).

If the referenced army does not exist in the GM state, the TP attempts recovery by creating it at your **muster seat** (own hex only).

New armies muster at your **muster seat** — your GM-designated capital (§3.7.3), or its successor if conquered (**§2.13.10 Capital Succession**).

> ***▶ Example — the recruit cap bites fast.** A hex with 2,000 population caps own-territory recruitment at max(1, floor(2,000 × 0.05)) = 100 soldiers this turn; recruiting on an ally's hex the cap is only floor(2,000 × 0.01) = 20. Population is spent as you recruit, so the cap shrinks within the same turn — you cannot drain a hex to zero in one turn. A tiny hamlet still permits at least 1 recruit (the max(1, …) floor), but a hex at zero population permits none. To raise a large army quickly, recruit from several populous hexes in parallel rather than hammering one.*

**2.12.2 Experience Blending on Recruitment**

New recruits join a stack at base WP and dilute its experience proportionally (§5.3.4).

**2.12.3 Building Ships**

Orc and Dwarf kingdoms cannot build ships — build_ship orders from those races are rejected.

**The fleet must be docked at one of your own ports.** A fleet at sea — or docked at an allied, neutral, or enemy port — cannot build; the Turn Processor rejects the order (the Player Page blocks it before you can submit). A fleet's remembered port is simply the **last port it docked at**, whoever owns it — only the build order itself checks ownership — so you may build at **any** owned port you sail into, not only where the fleet was first raised. **A blockade does not stop building**: a fleet of yours docked in a blockaded port may still build there, and a new fleet may be raised there — though, lying beside the blockader, it fights it before any fleet moves (§2.6).

**You build your own race's hulls, whatever port you build in.** A captured port lets you build there from your race's Ship Roster (Part IV). It never gives you the hulls of the race that built the port: an Imperial kingdom building in a conquered Aesir port gets Drommunds, Cogs and Galleys, not Snekkjas. This differs from land recruitment, where a compatible foreign settlement offers its own two-unit pair (§2.12.1). A foreign hull comes only as a prize taken in a naval battle (§2.13.12). An Orc or Dwarf kingdom that takes a port builds nothing there.

Ships are added to the specified fleet. Costs deducted in Phase 4 (affordability is cash on hand, §2.12.1).

Crew deducted from the port hex population: **\`crewPerShip = the hull's wood cost\`**. A hull takes as many people as it takes wood:

|           |            |              |                 |
|-----------|------------|--------------|-----------------|
| **Race**  | **Hull**   | **Capacity** | **Wood = crew** |
| Imperial  | Drommund   | 100          | 50              |
| Imperial  | Cog        | 200          | 90              |
| Imperial  | Galley     | 300          | 130             |
| Barbarian | Wolfship   | 80           | 45              |
| Barbarian | Reaver     | 120          | 65              |
| Barbarian | Tigress    | 200          | 100             |
| Elf       | Moonskiff  | 60           | 40              |
| Elf       | White Ship | 100          | 60              |
| Elf       | Swan Ship  | 150          | 85              |
| Aesir     | Snekkja    | 80           | 45              |
| Aesir     | Longship   | 140          | 75              |
| Aesir     | Busse      | 220          | 105             |
| Nomad     | Dhow       | 100          | 50              |
| Nomad     | Shini      | 140          | 70              |
| Nomad     | Harraqa    | 60           | 45              |

Orcs and Dwarves build no ships and have no row.

**Crews count against the hex's per-turn population ceiling.** A port hex gives at most max(1, floor(hexPop × 5%)) people a turn to **recruits and crews together** — the same snapshot and the same running total as §2.12.1, recruits (Pre-Phase 2b) first, crews (Phase 4) after. An order that needs more is **trimmed** to the hulls that can still be crewed, the trimmed hulls are not charged, and the card says the population ceiling did it (*"PARTIAL: you ordered N, but the port hex gives P people a turn to recruits and crews together — only M could be crewed"*). When nothing is left the order is refused with the same explanation. The Player Page trims the same way before you can queue the order.

> ***▶ Example — 900 Dhows in one order.** Nemedia's capital holds 15,000 people, and one order asks for **900 Dhows**. The hex gives floor(15,000 × 5%) = 750 people a turn to recruits and crews together. A Dhow costs 50 wood, so it takes **50 crew**. With no recruits that turn, floor(750 / 50) = 15 Dhows are commissioned and 885 are trimmed; had 400 soldiers been recruited there first, 350 people remain and only 7 Dhows launch. A fleet is a drain on a settlement, not a line in the treasury.*

**A port that cannot man the hulls builds nothing.** After the ceiling trim above, if the port hex still holds fewer people than the crew the trimmed order needs — it was drained after the turn began — the **whole order is refused** and nothing is charged. Ships need hands, and the hands come from the settlement on that hex. This bites hardest on a port whose camp has moved away (§2.11.10): the harbour still works as a dock, but with nobody living there it can crew nothing.

**2.12.4 Hiring Characters**

Default cost: **1000g**. Each turn your court draws **3 applicants** (the candidate pool), each with fixed stats (Military, Economics, Management, Politics — 1–100) rolled by the Turn Processor and listed in your report. Open **Hire**, pick the applicant you want, and give them a name. Stats are **server-set and fixed**: reloading your report shows the same applicants — you cannot re-roll for better numbers. Applicants stay at court until hired; each hire is replaced by a fresh applicant. A hired lord joins your court the following turn — assign their role then (see Part VII).

**2.12b Phase 4.5 & 4.6 — Army & Fleet Transfers**

After recruitment (Pre-Phase 2b) and before movement you may **redistribute forces within your own kingdom**:

- **\`transfer_units\` (Phase 4.5)** moves units from one of your armies into another; **\`transfer_ships\` (Phase 4.6)** moves ships between two of your fleets.

- The two armies (or fleets) must be standing on the **same hex**. Adjacent is not enough — march or sail them together first. Position is measured from **start-of-turn positions**, never from where a pending move would put you, and a transfer refused for distance carries a card naming both hexes, so it can never fail silently. A source **army** must not be embarked or destroyed.

- **Loaded fleets.** A fleet carrying an army may **receive** hulls freely — capacity only rises and the embarked army stays aboard. It may also **give** hulls, but only the ones its army does not need: the hulls it **keeps** must still hold the army's tonnage (foot ×1, mounted ×2 — the same measure as embarking), and **a carrier is never emptied**. Tonnage is read on the **live count** when transfers resolve (after Phase 1), not on what you saw while planning. A request that breaks either limit is **refused whole** — no partial fill — with a card naming the army, its tonnage and the room that would have been left. *Transfer All (Merge)* is not offered on a carrier.

- **The Navy card tells you what you may give.** On a loaded fleet the Transfer Ships panel shows *"Carrying Army X — cargo T / capacity C: you may release up to S capacity, and never the last hull"*, caps each hull row at what that type alone could release (a row that cannot be spared is greyed), and re-checks a mixed pick when you click. When a fleet with hulls has **no eligible partner**, the panel does not disappear: it names the reason — no fleet on this hex · the fleet here has a route planned (cancel it) · it already sent hulls this way · not one of your own hulls can be spared.

- A source army or fleet may give **one transfer per turn**; a second transfer from the same source is refused with a card.

- You cannot transfer in **both directions** between the same pair in one turn.

- **A receiver may march or sail the same turn.** Transfers resolve before movement (Phase 4.5/4.6), so the army or fleet that receives units or hulls moves with its **merged** force: its movement is set by its slowest unit or hull **after** the merge — foot joining horse marches at foot pace. Nothing moves twice (the units came from the same hex), and a receiver still cannot pass them on (next rule). On the Player Page, plan the merge **first** and the route **after** it — the transfer panel asks you to cancel a route already planned for the receiver, so that the route is re-planned on the merged pace. Two conflicts still refuse the *transfer* instead: an **embarking** receiver — the army boards its fleet at the very start of the turn, long before transfers resolve, so units cannot be handed to a force already filing aboard. **Link clause:** a **linked receiver whose group LEADER has a move order** also refuses the transfer (viaLink card) — the leader's march may belong to an **allied sovereign**, and your transfer never cancels another kingdom's group movement; unlink first, or let the leader hold.

- **An army or fleet that received a transfer this turn cannot give one.** A force that received units or hulls cannot pass them on until next turn — chained same-turn relays (A→B→C) are refused (it may still march or sail with them). Giving first and receiving afterwards in the same turn is fine: nothing moves twice. *(This rule is enforced by the Turn Processor — a violating transfer simply fails, and your report carries a card explaining why.)*

- Transferred troops keep their experience: the destination's experience becomes a count-weighted average of its own and the incoming units (the same blending as recruiting fresh troops).

- **Transfer All moves the live count.** A full-stack send is marked at planning time, and the Turn Processor transfers whatever that stack holds when transfers resolve (Phase 4.5) — including foot soldiers gained to Orc reproduction in Phase 1 of the same turn. The emptied source army always auto-disbands; newborns are never left behind in a one-goblin remnant. For fleets, *Transfer All* likewise empties and disbands the source — which is why it is never offered on a fleet carrying an army.

- **Troops of other peoples stay within 20% of each army** — a transfer, merge or split that would push either army over it (or leave an army already over more foreign than it was) is refused (§2.12.1).

- **A transfer can be undone this turn.** Once submitted, the transfer panel shows a **✕ Cancel transfer** button that reverses it in full — the moved units (or ships) return to their original army or fleet, and a source that a *Transfer All (Merge)* auto-disbanded is restored. (Re-issue any move or stance order the disbanded force had carried; those are not restored.)

This is purely internal reorganisation — consolidate a scattered force into one strong stack, or peel veterans off to seed a new army or fleet. Nothing is transferred to other kingdoms.

> ***▶ Split — peel a new army or fleet off an existing one.** The Army and Navy cards carry a **Split** panel beside Transfer: type how many of each unit (or hull) to peel off, and the **next empty slot** is raised **on the same hex** when the turn is processed — armies in Phase 4.5, fleets in Phase 4.6, exactly where transfers resolve, on start-of-turn positions. So the split needs a free slot (10 armies / 5 fleets per kingdom) and room on the hex (3 armies or 3 fleets), and the new force **holds still this turn**: it cannot march, sail or give a transfer in the turn it is born (a hand-edited move order for it is refused with a card), and takes its own orders from next turn — the page shows it as a dashed pending card with a **✕ Cancel split**. The new force **inherits the source's readiness** and every stack **keeps its experience**; it starts in Moving stance, **outside any link**, with **no commander** (the source keeps its own). Nothing is refunded or lost. Refused, with a card: a source **aboard a fleet** or a fleet **carrying an army** (land or disembark first), a split that would **empty the source** (that is a merge — use Transfer All, or Disband), and soldiers left below the **crew their engines need** on either half. A fleet may split **anywhere**, at sea or in port; a fleet split in port is docked there. A source inside a **link group** or holding **Siege** may split — the new force stands outside the group, and a besieging ring counts fewer bodies from then on. One split per source per turn, and the page refuses a split (or a transfer, dismissal, recruit, shipbuild, recruit undo, disband or embark) that would touch an army or fleet already splitting this turn — cancel the split first. The pending force is offered nowhere (not as a transfer target, a link candidate or a fleet to embark on) until it exists; room on the hex is judged where forces **stand** at the start of the turn, not where they plan to be.*

**2.13 Phase 5 — Army Movement & Land Combat**

> ***Not all land conquest happens in this phase.** Phase 5 covers combat driven by armies **marching on land** — field battles, hex seizures, and assaults reached over land. A hex can also change hands in **Phase 6**, through an **amphibious disembarkation** (§2.14.6), which resolves **after** this phase. So a hex that came through Phase 5 untouched can still fall the same turn to a beach landing — do not read "survived the land phase" as "safe for the turn". See the ordering warning in §2.14.6.*

**2.13.0 The March, Step by Step**

**Orders in force.** Your turn log opens Phase 5 with an **Orders in force** card: one entry per army, showing where it stands (and on which side of the walls), its status, the stance **in force** for this phase and where that stance came from — *kept from last turn* or *ordered this turn* — and the order it carries this turn. The stance shown is the one its battles will use, after every rule has been applied: a march leaves an army with no stance (Moving), and a stance that cannot hold on its hex says so (*your Garrison does not hold here* on open ground, where it fights as Defensive). A linked army shows the leader it follows; an embarked army shows the fleet carrying it. A kingdom that missed the turn gets the card too — that is when its stored stances matter most.

**Inside the walls.** On a hex with standing walls only an army in **Garrison** — the owner's or a friend's — stands **inside**, behind the walls; every other stance stands **outside** on the open ground, and a **besieged** army stays inside while the ring stands (§5.8.0, §2.13.7). A Garrison never comes out to fight; only a besieged army that **orders Sally** goes out. So the card says the zone, and whether a siege holds you:

|                                                                       |                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **The card reads**                                                    | **Meaning**                                                                                                                                                                                                                           |
| *inside the walls*                                                    | This army is in Garrison: an attack must beat the armies outside first, then storm the walls — and this army defends behind them at ×1.30.                                                                                            |
| *inside the walls · besieged by X — Garrison or Sally only, no march* | A realm at war with you besieges these walls (§2.13.7): this army holds **Garrison** (whatever stance it had), cannot march out, and may order **Sally** — or embark (a port embark only in your own port; otherwise a beach pickup). |
| *outside the walls*                                                   | Your army is camped before walls that are not yours (or stands outside your own, in any stance but Garrison, or with its link leader outside).                                                                                        |

Whoever storms or besieges walls is at war with every realm inside them, its own ally included (§5.6).

> ***▶ Example — behind the walls.** Your Army II (Garrison) and Army III (no stance) stand on your walled hex (29,27): II's line reads inside the walls, III's outside the walls. An enemy march meets III first, in the open; beaten, III goes inside in Garrison, and the storm follows against both (the full walk-through is §5.8.0's worked example).*
>
> *Army II (29,27) inside the walls · 92% · Garrison (kept from last turn) — order: none*
>
> *Army II (29,27) inside the walls · besieged by Aquilonia — Garrison or Sally only, no march · 81% · Garrison — after the Sally fought in Pre-Phase 3 — order: stays ← the turn it ordered Sally*

One sequential picture of everything that happens to a marching army in a turn — each step points at the section that owns the detail.

**Before the march ever starts:**

1\. **Pre-phase** — link groups form (leader + members, including links ordered *this* turn), embarks re-apply, and **recruits join (Pre-Phase 2b, §2.6a — they fight everything below)**, then standing siege/assault stances resolve. An army that files a march together with Siege or Assault marches, and the stance is ignored that turn (*Stance Ignored*); ordering a "stationary" army to march reads as the Moving stance; a **besieged** army cannot march at all — its march is refused (§2.13.7).

2\. **Phase 4** — ships and hires only; nothing joins an army here (recruits joined in step 1, Pre-Phase 2b — §2.6a — and count for the march's headcount and crew maths).

3\. **Phase 4.5** — splits first (a new army peeled off an existing one is raised on the same hex and **holds still**, §2.12b), then transfers: an army that received units this turn **may still march** on its merged pace, and so may the giver with what it kept. The Player Page does not let you plan a route for a split-raised army, and it lets an army board a fleet receiving hulls only if the army fits **without** those hulls — armies board before transfers resolve.

**Phase 5 opens with the camp sweep:** armies already at war camped in the same zone of one hex fight before any march (§2.13.5); an army that fought does not rest this turn.

**Order intake (Phase 5 begins):**

4\. Eligibility: the army exists, is not destroyed, is not embarked. **Duplicate move orders** — only the first per army is honoured (one card).

5\. **A link member cannot move itself** — its order is ignored with a card; the leader's order moves the whole group, at the pace of its slowest member.

6\. **Claiming the ground you stand on (§2.13.2b)** — an army starting its march on foreign, non-allied **open** ground fights for *that* hex first: the populace contest, **before hop 1**, war declared as needed (§2.13.8). A **walled** origin is never contested by a departure — the army simply marches off.

7\. The **movement-point budget** prices the path: 60mp on foot / 90mp fully mounted, per-hex terrain and race costs (§2.13.2) — and **an army hauling siege engines is a siege train: one hex per turn**, extra hops dropped with a card (§5.8.6).

**The march itself — in rounds, one hex at a time (§2.13.1):**

8\. Every marching army becomes a cursor and advances **exactly one hex per round**, in STATUS order re-ranked every round (§2.13.1). This is the whole of the "randomness" in movement: it matters only when two armies contest the same hex in the same round.

9\. **Every hop re-checks reality**: is the army still alive (casualties from a battle earlier in the same round count), what does the budget say *now* (it recomputes from the live composition — lose your last horse mid-march and the next hop is priced on foot; the budget can only shrink, never grow mid-march), and what is the terrain *really* (a hop planned into fog resolves against the true map — the army halts where it can no longer pay, or if the hidden hex is sea).

10\. **Entering a hex resolves, immediately**: an enemy field army → **battle** (§2.13.5; win with points and rounds to spare → march on; lose → retreat, or annihilation only if surrounded); a foreign **walled construction** → a battle against the armies **outside** first, then, if won, a **hasty assault on arrival** against the Garrison inside, even a holder that took it earlier this phase (§5.8.0, §2.13.6b; repelled but alive → camped at the gates); a foreign **open hex with population** → the militia seizure contest (§2.13.4); a **full hex** (3 friendly armies, zone-aware before walls) → blocked with a card (§2.13.3).

11\. **A stop is definitive.** Any block, defeat, or exhausted budget closes the cursor — the rest of the path is discarded for the turn, even if the obstacle later moves away.

**After the land phase:** embarked armies move with their fleets in **Phase 6** — including amphibious landings that can take a hex *after* Phase 5 left it untouched (see the warning at the top of this section); armies left at war in one zone meet in the next camp sweep (§2.13.5); an army that neither moved nor pressed a siege **recovers +33 STATUS** — unless it is camped on a **foreign fortified hex** (§5.10.5); and every hex an army stepped on (plus its ring) becomes *remembered* on your map, forever (the terrain-only fog tier, §2.19).

**2.13.1 Initiative — Readiness First**

All move orders enter a single movement pool. Movement resolves in **rounds**: every army in the pool advances **one hex per round**, and the next round begins only after every active army has taken its hop. The order within each round follows **current army STATUS** (highest first, re-evaluated every round — marching wears an army down the queue), with random draw only among equals (§5.10). Readiness buys tempo: the rested strike first, and an exhausted army finds the battlefield already changed when its turn comes. An army leaves the pool when it completes its path, runs out of movement points, is blocked, is halted by battle, or storms a settlement. **A blocked army stops for the turn** — it does not retry in later rounds, even if the blocker moves away. Two armies both moving this turn therefore meet **only if their paths contest the same hex in the same round**: an army that leaves a hex in round 1 is not there when you arrive in round 2 — there is no interception on adjacency and no zone of control, by design. You catch an army by predicting its **destination**, or by attacking what it must defend; never by chasing its last-seen hex, which is always one turn stale in your fog report. The pre-movement siege/assault phase and fleet movement (§2.14.1) use this same STATUS-first ordering rule.

**2.13.2 Movement Rules**

Players submit a path (an ordered list of **adjacent** hex coordinates). The army advances **one hex per movement round** (§2.13.1), spending **movement points (MP)** per hex according to terrain. Movement stops if the army is stopped by combat, is destroyed, runs out of MP, finds a fortified hex's outside approach zone already at its cap (§5.8.0), or completes its path.

An army's MP budget is **60** on foot (any non-mounted unit in the stack) or **90** when every unit is mounted. **A siege train crawls**: an army carrying siege engines — or leading a LINK group in which any member carries them — marches at most **one hex per turn**, and abandons its engines on a retreat (§5.8.6). That budget is **re-checked every hex against the army's current composition and can only decrease as the march continues** — a loss that slows the army (its last mounted unit falling in a battle fought mid-march, say) takes effect immediately, on the very next hop; the budget never rises mid-march either, even when a linked group's slowest member is destroyed and its removal would otherwise raise the group's minimum. Per-hex cost depends on terrain and race (plains are cheapest; mountains, swamp and desert are the costliest; Dwarves cross hills/mountains cheaply, Elves forests, Orcs swamp, Nomad desert). A path may string together **any sequence of adjacent hexes up to the MP budget — including doubling back or revisiting a hex** (for example A→B→A "up and down" between two plains hexes spends 60 MP). The only constraints are adjacency, the MP budget and no sea hexes (embark first). Marching into a foreign walled construction is allowed — it is a **hasty assault** that turn (§5.8.0), declaring war on every realm inside, your own ally included (§5.6), and it storms whoever holds the walls, even one that took them earlier the same phase (§2.13.6b). In the Player Page the outbound route is drawn in gold and any **retraced (return) leg is offset to the side in cyan**, so both legs stay visible. You **may plan a hop into a fogged (unknown-terrain) hex** while you still have movement points: the panel shows it as ❔ Unknown (fog) priced at the optimistic minimum (≥30mp) with a ⚠ warning, because the real cost is hidden. The Turn Processor then resolves the move at the **real** terrain and halts the army where it can no longer proceed — a fog hop may not complete if the hidden hex costs more MP than you have left or is open sea (armies can't enter); if the hidden hex turns out to be a foreign walled construction, the army marches in and presses a **hasty assault** on its walls (§5.8.0). It can never push the army past its true MP budget.

\**A march that* begins *on hostile ground fights for its own campsite first — the origin hex is claimed (contested on open ground — walls are never stormed by a departing army) before the first hop. Full rules and a worked example in §2.13.2b*\*.

**Per-hex MP cost by race and terrain** (the exact table the game uses — racial home-terrain discounts in **bold**; Aesir have deliberately NO land discount — their mobility is the fleet):

|             |                                      |               |         |         |           |           |           |
|-------------|--------------------------------------|---------------|---------|---------|-----------|-----------|-----------|
| **Terrain** | **Imperial**                         | **Barbarian** | **Elf** | **Orc** | **Dwarf** | **Aesir** | **Nomad** |
| Plains      | 30                                   | 30            | 30      | 30      | 30        | 30        | 30        |
| Hills       | 45                                   | 45            | 45      | 45      | **30**    | 45        | 45        |
| Forest      | 45                                   | 45            | **30**  | 45      | 60        | 45        | 45        |
| Mountain    | 60                                   | 60            | 60      | 60      | **30**    | 60        | 60        |
| Swamp       | 60                                   | 60            | 60      | **30**  | 60        | 60        | 60        |
| Desert      | 60                                   | 60            | 60      | 60      | 60        | 60        | **30**    |
| Sea         | — armies cannot enter (embark first) |               |         |         |           |           |           |

On foot (60 MP): two plains hexes per turn, one mountain hex; a Dwarf does two mountain hexes where everyone else does one. Mounted (90 MP): three plains hexes. There is no terrain cheaper than 30 — a race's discount brings its home terrain down to plains price, never below. (Each hex entered also costs readiness by race and terrain, §5.10.3.)

**Fleets** move on **sea** hexes (and into ports — any port, whoever owns it, §2.14.2) at a flat **30 MP per hex**, but a fleet's MP budget is the **mp of its slowest ship** — a convoy is paced by its heaviest vessel: **60 MP → 2 hexes**, **90 MP → 3 hexes**, **120 MP → 4 hexes** (per-hull mp is listed in each race's Ship Roster, Part IV). That budget, too, is **re-checked every hex against the fleet's current hulls and can only decrease mid-voyage** — capturing a slower prize hull mid-battle slows the convoy to the prize's pace from that hex on (an honest card explains the slowdown), but losing a slow hull never speeds a voyage back up once it's underway. A mixed fleet therefore moves at its slowest hull, and carrying an army does not slow it. Fleets may likewise revisit hexes / sail back and forth within that budget, with the same gold-outbound / cyan-return path display. *(Orc and Dwarf field no fleets. The 120-MP tier belongs solely to the Aesir Snekkja, §4.7 — an all-Snekkja fleet is the fastest thing afloat.)*

Embarked armies (transported by fleet) do not move in Phase 5.

**Your own route.** An army that marches through two or more hexes is told every hex it entered, in order. A march that ends unopposed on its own or an ally's ground gets its *marched to* card with the route — *Army I marched to (2,2) · route (3,2) → (2,2) · 2 hop(s) · plains*. A march that ends any other way — a battle, a conquest, a storm of walls, a block — carries the route on the card that ended it: *Conquered (2,2) — plains · No resistance · Army I route (3,2) → (2,2)*. A retreat is not part of the route (the battle card says where the army fell back). A one-hop march carries no route: the card already names the hex.

**Route sightings.** When one of your armies **steps into** a hex where a foreign army already stands — or a fleet lies docked in that hex's port — both sides are told, even if the two forces end the turn out of each other's sight. An army of siege engines alone, with no soldiers, meets nothing and is not met. You learn the realm, the army or fleet number and its size (hulls exactly, soldiers to the nearest 10, never fewer than 10; an ally, liege or vassal also shows its full snapshot). A friend's fleet (ally, liege or vassal) also names the army it carries as its cargo; what a foreign fleet carries stays hidden (§2.14.2). The force you walked in on learns where you came from and, while it is still there, the round you left and the hex you stepped to — it is not told whether you went further (if that was your last step, it is where you stopped). Only the **same hex** counts: marching past a force on a neighbouring hex reports nothing, and forces that fight you there are covered by the battle card instead. On a walled hex, when the two stand on opposite sides of the walls — one inside, one camped outside — that line says so instead (*No contact — … is outside the walls, your Army N inside*): that, not a passage, is why nobody fought. Standing on your starting hex is not a meeting; stepping back into it later in the turn is. A head-on swap — two armies trading hexes in the same round — is one meeting. Each force gets one card — *Army N crossed paths on its march* for the army that moved, *Foreign forces passed Army N at (c,r)* for the army that was entered; when both are still on the hex at the end of the turn the titles say so instead (*Army N marched in beside foreign forces* / *Foreign forces camped beside Army N at (c,r)*) and the card's last line says the visitor *remains on the hex* (when the visitor is an allied army already carded as passing through your lands, the line joins that card) — and the maps mark the meeting hex with a dashed ring in the other realm's colour labelled with the round (**R1**, **R2**…), unless that realm already shows a marker of the same kind (fleet or army) there at the end of the turn. Meetings are reported for that turn only.

**Witnessed battles.** If a battle is fought on a hex where your army stands, no army of yours fights in it, and your realm is a friend (ally, liege or vassal) of either side, you receive the battle card as an observer — *Battle beside your Army N at (c,r)* — with the full combat panel, who won, and whether your army stood inside the walls. Your army loses nothing and no war begins.

> ***▶ Example — the battle you did not fight.** Hyperborea's walled forest at (24,34) holds two armies: Hyperborea's own **Army II** in a valid **Ambush** — so it stands **outside** the walls, hidden — and its ally Nemedia's **Army VI** (**Garrison**, 10 soldiers) **inside** — only a Garrison stands inside (§5.8.0). Aquilonia, at war with both, marches in with 120. The marcher meets the ambusher in the open first (§5.8.0 Case D) and beats it; having won at the gates, it **storms the walls the same turn**.*
>
> *\| Who \| What it does \| What its report says \|*
>
> *\|---\|---\|---\|*
>
> *\| Hyperborea II \| Fights (and loses) at Ambush ×1.40. Beaten outside its own walls, it goes **inside, in Garrison** (§5.8.0), and defends the storm that follows. From this turn every foreign map draws it: a sprung ambush conceals nothing. \| Army II stands outside the walls, its defeat card (Beaten outside your walls, your survivors went inside them, into Garrison), then the storm's card \|*
>
> *\| Nemedia VI \| Takes no part in the gate battle — a Garrison never comes out (§2.13.5). It then defends the storm beside II, in Garrison ×1.30 with the walls and the militia. \| Battle beside your Army VI at (24,34) — Aquilonia vs Hyperborea (observer card with the full panel: "took no part: it stood inside the walls"), then the storm's card \|*
>
> *\| Aquilonia VII \| Wins at the gates, then storms the walls against II and VI. At 120 against the remnant of II and 10 soldiers it takes them: II and VI fall back out of the lost city, and VII stands inside in Garrison as the conqueror. \| Victory card, then Walls breached, then the conquest card — in that order (§2.13.4) \|*
>
> *Had Nemedia's VI stood on **Defensive** instead, it would have stood **outside** beside II and fought the gate battle with it at ×1.20; beaten, both would have gone inside to defend the storm. Had Aquilonia **lost** at the gates, it would have fallen back and never reached the walls.*

**2.13.2b Claiming the Ground You Stand On**

How does an army end up standing on land whose owner is not its friend? Almost always, **diplomacy moved under its feet**: it was camped on a mutual ally's hex (a legal, fully reported visit — §2.13.3) and the alliance then ended, by your hand or theirs; or a vassalage was released. However it happened, the army now begins its turn on ground it has no right to stand on. The ground it stands on is the first thing it must answer for.

**The rule.** A move order whose army **starts** on another kingdom's land, when that owner is **not a friend** (not you, not a mutual ally, not your liege, not your vassal), makes the army fight for its origin hex **before its first hop** — exactly as if it had just marched into it. **Peace is not friendship**: a merely-neutral owner triggers the claim the same as an enemy; the claim then declares the war itself (below). Unowned wilderness never triggers a claim — only owned land can be claimed.

**What it never touches:**

- A **stationary** army claims nothing. No move order, no claim — simply standing on foreign land remains bloodless and legal, exactly as before. The claim is a consequence of *choosing to act*, never an ambient penalty.

- Armies in **Siege or Assault stance** are exempt — their on-hex fight already resolves in the stance step, before movement.

- An army leaving a **fortified** origin (walls standing) **never storms the walls it was camped against**, in any stance: it disengages and simply marches. A walled settlement is taken by Siege or Assault stance, or by marching **in** — never by walking away. No war is declared by the departure, and the march keeps its full budget. The GM log notes a *Fort Departed* line.

- **Embarked** armies never claim (they are cargo — §2.14).

- **Friendly ground** (your own, a mutual ally's, your liege's or vassal's) is never claimed.

- **Other armies camped on the same hex** (up to 3 — §5.11) are **not** part of the claim fight itself — it disputes the populace (walls are never claimed by a departure) — but once the ground is won they resolve as **bystanders** (§5.5): a hostile camper withdraws, or, cornered, makes a last stand that can take the hex back. A hostile co-camper is a separate problem for a separate order.

**On open ground** (no walls — bare terrain or a wall-less construction tier), the claim is the standard seizure contest against the hex's militia (§2.13.4). A **LINK group contests together**: the whole group's WP counts, and group-wide casualties follow (§5.11). Three outcomes:

- **Won** — the hex flips to you with full conquest treatment: seizure and lost-hex cards on both sides, the militia's dead deducted from the hex's population, spoils where they apply (§2.13.11), construction conquest damage as on any flip, and combat-proportional casualties to your force. The march then proceeds **with its entire MP budget intact** — and the claim charges **no terrain entry** either — the battle's own status cost (§5.10.4) is still paid, as in any fight: status prices the hexes you *enter* (§5.10), and the army entered this one long ago.

- **Repelled** — you take casualties, the hex stays the owner's, and the fight **consumed the march**: the army holds position and its planned path is cancelled (an "Army Repelled" card explains it).

- **Wiped out** — as with any seizure, a hopelessly outmatched force can be destroyed outright by the populace.

**On a fortified construction** (walls standing — wall points above zero) there is **no claim at all**. The army marches off, the walls are untouched, and the ordered path runs as planned. Only a Siege or Assault stance, or a march *into* the settlement, ever engages walls.

**War declares itself.** Claiming declares war on the hex's owner exactly as marching into their territory would (§2.13.8), with the same opinion consequences — **and the declaration stands even if the claim is repelled**: the attempt is the act of war, not the outcome. Read the strategic corollary carefully: **after an alliance breaks, there is no quiet way home.** An army camped on ex-allied land cannot slip away — its first step is a fight for its own campsite, and that fight starts the war. If you intend to end an alliance (or suspect your host is about to), march your visiting armies off their land **first**; from the turn the alliance dies, every army you left behind is a claim waiting to happen.

**Timing.** Claims resolve at the very start of Phase 5, before any army anywhere takes its first hop — a claimed origin is settled ground (or a settled defeat) before the readiness-ordered rounds (§2.13.1) begin.

> ***▶ Example — the broken alliance.** Last turn your neighbour ended your alliance. Your army of **10 Praetorians (≈1,200 WP)** is still camped on one of their open plains hexes, population **600**, and you order a two-hex march home. Before its first hop, the claim fires: the populace fields floor(600 × 5%) × 20 = 600 militia WP. At roughly two-to-one you win decisively — the hex is **yours**, war is declared, a proportional sliver of Praetorians falls, and the army still completes **both** hexes of its march (the claim cost no MP and no terrain entry; the battle's own status cost of §5.10.4 is paid, as in any fight). Now rerun it with **3 velites (≈129 WP)**: the mob wins — the army is thrown back onto its own tents, bloodied; the hex stays your ex-ally's; the march is cancelled; and the war is **still** declared, because the attempt itself is the act of war. And had the camp been one of their **walled settlements**, neither contest applies — there would be no claim at all: the army marches off and the walls are untouched (§2.13.2b).*

**2.13.3 Stacking and Blocking**

Each hex holds at most **3 armies** (per zone on a walled hex), and every army counts, whatever its banner — except that **enemies take no room against an attack**: a march onto an army at war with it fights it rather than halt as *hex full* (§5.11). What happens when an army moves into an occupied hex depends on WHO holds it and WHERE it is:

**Who is engaged when several armies share the hex.** On your own or an ally's ground, a march or a landing engages the army you are **at war with**, even when a friendly army stands beside it — a friend on the hex never masks an intruder, and the intruder never takes room against you: you fight it rather than halt as *hex full*. Among several armies of the same standing — two at war with you, say — the one whose realm id is lowest is engaged, never the one whose orders file happened to be read first.

- **Your own or a genuinely friendly army** (mutual ally, vassal, liege) on **your own or allied ground** → you **co-locate**: the army moves in alongside them, up to 3 armies on the hex. A **full** hex (3 already) halts the march with a 🚧 notice — an army at peace with you standing there takes a place like any other, and a link group that does not fit **whole** halts whole, leaving nobody behind. If a member of your group arriving there is at war with an army already on the hex, it **attacks on arrival** (§2.13.5). **Co-location needs one of your own armies already on that hex:** with none of yours there, an army standing on your (or your ally's) ground that is **not** your ally, vassal or liege is engaged — at peace or not — as below, and war is declared on its kingdom; the Player Page's move note says so. **Walls change one thing:** on your own or an ally's *fortified* hex an army **at war with you** camped outside the walls is engaged on arrival **whether or not your own army already holds the walls**. A march home always arrives **outside** (§5.8.0): the fight is the same field battle as below (you attack, no stance, no walls), your armies already outside join it on the §2.13.5 terms, and a Garrison inside never does. A camper at *peace* with you outside your walls is still walked past when your army is inside. If the relief **wins** it stays on the hex **outside** its own walls (or its ally's), with no stance in force; a **Garrison** order takes it inside from the next turn, while the inside has room (3) and no army at war with it is camped outside. A relief that loses or draws falls back as any field attacker — never into the city. The Player Page's move note names the army you will fight.

- **A friendly army on enemy or neutral ground** → it does not shield that ground from you: if the hex has room for your army — and its whole link group — you **go in as if the friend were not there**: the hex is fought for or taken from its owner, and your friend is a bystander that stays beside you (it makes room if the hex would overfill). You never fight an ally. Only a hex without room for your **whole group** blocks the march — one allied army already there turns a 3-army group away — carded with the cap. On a foreign walled hex a friend of yours **inside** is no shield: marching in to storm the walls declares war on every realm inside, your friend included, and the alliance breaks (§5.6). **On a foreign walled hex, any army camped outside the walls that is not your mutual ally, vassal or liege is fought — at war or at peace — and a friend camped beside it does not shield it: your march bounces off that ground only when every army outside is a friend of yours.** Which of several outside camps you meet does not depend on the order the turn's orders were read in: an army at war with you comes first, then any other army that is not a friend, then a friend, and realms tie by their place on the roster. A soldier-less army is nobody — it neither shields the ground nor is fought for it.

- **Any other army** (declared enemy or neutral third party) → **field battle** (after a **clear victory** — the defender destroyed or driven off — **the march continues its remaining hops**; a draw or a defeat ends it, and the attacker falls back, §5.5), and **war is declared on the occupant's kingdom** — in addition to the hex owner's, when you are entering someone's land. Fighting a neutral kingdom's army is itself an act of war. If several armies hold the hex, they defend together as §5.11 sets out. *Why land and sea differ here:* land has territory and the sea has none — at sea a neutral fleet only takes a berth (§2.14.2), but on land walking onto a neutral army, or onto neutral ground, is always an act of war — walls nobody owns count as open ground here; walls with an owner are stormed instead (§5.6). If you take a hex that a third kingdom's army was holding for its owner, the **owner** is carded the loss, naming the army that held it — or, when no battle was needed, the friend of yours that stood by; that friend's army stays (or makes room) and is carded too. A hex nobody owned has no owner to card: nobody is told it was lost — not the army that held it — and the conqueror's card reads *"No banner flew here; up goes yours…"*.

On your **own** or an **ally's** hex the engagement never changes ownership — you are reclaiming home ground or liberating allied land.

**You see what happens on your land.** Allied movements across your territory are fully reported to you: an allied army that **ends its turn** on your hex produces a card naming its commander, its full composition, headcount and war-power (allies hide nothing from each other — readiness is not shared); one that merely **passes through** produces a single card listing the hexes crossed, with the same detail. If a battle is fought **on your hex** that you took no part in — your ally against an intruder, or two armies fighting at your walls or over a siege of your settlement — you receive the full battle report — win, loss or draw — drawn *Attacker \| Defender* with the winner named, since you fought in neither column — except an assault on your walls held or taken by an ally's garrison, which still comes drawn as your side (a lost liberation means the enemy still camps on your land, which you very much want to know). An allied march onto your occupied hex **joins** your army there (co-location, §5.11) rather than being blocked — only a full hex (3 armies) turns the visitor away, and that notice goes to the halted visitor. The same holds at sea, and in your own harbour it goes further: see *What the port's owner sees* (§2.14.2). Enemy armies grant you none of this — only fog-of-war sightings.

**2.13.4 Seizing Undefended Hexes**

When an army moves into a foreign hex with no defending army, the local **populace fights back as militia** — a defending force worth floor(population × 5%) × 20 WP (≈ the population itself; the same militia that defends a besieged settlement, §5.6). Seizing the hex is a **field-style WP contest** against that militia:

- **No fortress and no terrain/home bonus** apply (it's open ground, not a walled assault), and the attacker takes no walls penalty. The attacker does keep its **initiative** (1.05–1.10), **commander** (1 + Military/1000) and **STATUS** multipliers; the militia rolls only the ±10% variance.

- Win **decisively** (your battle roll \> 1.2× the militia's) → you **claim the hex**, taking **combat-proportional casualties** (a lopsided win costs little; a close fight costs more).

- A **draw or a loss** → you're **repelled**; the hex is not taken. The populace contest uses the **same soft curve as a field battle**, including the extreme-odds ramp and the armour dissolve (§5.5.3): below the ramp a badly outmatched force loses up to **60%** (the cap binds from 5:1 and holds flat to 13:1) and falls back on the strength of its armour; beyond 13:1 the cap and the armour give way together, and a force that marches on a populace **25 times its weight is destroyed to a man**. There is no ratio at which a well-equipped company walks away unbloodied from a hopeless assault on a city.

- **Neutral/unclaimed hexes** defend with whatever population their construction holds. A neutral hex with **no** construction has no population, mints **no militia at all**, and is taken unopposed — empty ground is genuinely empty (§3.7); only a legacy map from before constructions falls back to the terrain's base population.

Because the defence is **WP, not headcount**, you need an army whose war-power roughly exceeds the population, and **quality counts** — a small elite force takes ground a horde of weaklings can't, and a lone unit is simply thrown back.

The **militia is levied from the populace, and its fallen are permanently removed from the hex's population** — proportional to the battle (the same casualty split as a field fight): a crushing repel costs the populace only a handful, while being overrun (the hex falls) kills most of the levy. So a defended hex *erodes* under repeated attack, and a conqueror inherits a hex **depleted by the militia it just destroyed** — population is not a bottomless, free defence. The site and the settlement each lose a level in the takeover (§5.6.3). (This applies equally to beach landings and to **assaults**, §5.6 — a stormed or repelled settlement loses the militia it raised. A hex with no construction has no population to levy or deduct in the first place.)

**The settlement goes with the hex.** A construction on a hex you take stays on it and is now yours, with its people. An **open settlement** — a level whose wall is 0 (§3.7.1a: a Level-1 Nomad camp, the first Generic and Orc levels) — has no walls to hold: its militia fights like any undefended hex's and, when it falls, the settlement falls with it; a **walled** one is taken only by storm or siege (§5.8.0). Either way the settlement and its production site each lose a level on capture (§5.6.3). Both reports name the settlement that changed hands.

> ***▶ Example.** A lone velite (43 WP) marches onto a plains hex of 1,000 population: the populace fields floor(1,000 × 0.05) × 20 = 1,000 militia WP. At ~23:1 against, the ramp is in force: the loss reads ~93% with the armour nearly dissolved — a lone man rounds to his death more often than not, and past 25:1 he is gone with certainty. Below the ramp a repulse costs at most **60%**; a repelled force stays on the hex it came from and is **destroyed only if the contest leaves it no soldiers** — the militia contest never searches for a retreat hex; it also grants no experience, rolls no commander death and applies no cavalry terrain scale. A hex with **no population at all** is simply taken — there is nobody to fight. A base plains (200 pop → 200 militia WP) needs roughly **240+ WP** raw (a little less with an average initiative roll and a commander) to take — about 6 velites or 2 Praetorians; a developed plains (2,000 pop → 2,000 WP) needs ~2,400 WP. Populated land falls only to a real army, and your force bleeds (proportionally) for every hex it conquers.*

**What each side is told.**

- **The attacker** gets a seizure card (with casualties) or an **"Army Repelled"** card on every repulse — it reads "no survivors" only when the force was wiped out in the contest.

- **The hex's owner** gets a **lost-hex** card or, when its populace holds, an **"Invasion Repelled"** card. Whenever the militia fights — seizure, beach landing or assault — the card **reports the militia's own losses** ("your militia lost N"). A lost-hex card credits the militia (its defending WP, its own losses, the invaders it killed) and gives the **size of the invading force** — the troops that marched or landed.

- **The card reads true to how the hex fell:** a bloodless **walk-in** ("strolled in while nobody was guarding it" — or "took this hex while X's army — a friend of Y's, camped there — stood by"), a **militia** fight ("trampled past your militia") or an **assault** ("stormed the walls by force of arms"; the effect line reads *Taken by force of arms — N troops lost (see the battle card)*).

- **The conquest comes after its battle.** When walls change hands in a won storm or a winning landing, the *Conquered* and *Lost* cards follow that battle's cards in the report — never before them.

**How much you learn about the invader** depends on what stood in its way:

- **A real army** fought it → the full battle report, every unit type in the enemy's composition.

- **Only the militia**, or walls lost to a **siege** (§2.7) → its size **and its horse-to-foot balance**.

- **Nothing at all** → a headcount only.

All three arrive **after** the hex is gone. A spy (§8.8) is the only intelligence on an army you have *not* yet fought — an estimate, but the only kind that arrives in time to act on.

**2.13.5 Field Battle Trigger**

Two armies at war in the same hex resolve a field battle. The moving army is the attacker; the stationary army is the defender.

**An army or fleet already standing on the hex you attack joins that attack**: when your army attacks an enemy on a hex — marching onto it, arriving beside it or landing on it — every army of yours already standing there in the same zone fights on your side, and so does an army of your ally, vassal or liege that is **already at war with every kingdom on the defending side**; the members of a link leader among them come too. They share the result: each takes its own casualties and gains its own experience, and on a loss or a draw each falls back — or its group scatters — exactly as your attacking army does. **Joining never starts a war**: an allied army at peace with any kingdom on the defending side stays out, and so does an army that already fought in the same step. Inside against outside a wall never joins. Fleets do the same at sea (§2.14.7).

**A Garrison never joins.** An army in Garrison inside walls is never called into a friend's attack — the walls are its post; only a besieged army that orders Sally goes out (§5.8.0, §2.13.7). The joining army's battle card opens with why it fought: *"Your Army II was on the hex and joined Army I's attack."* — or, for an ally, *"Your Army I was on the hex and joined Aldoria's attack."*

On **foreign or unowned ground** your march attacks any army in that zone that is not your ally, vassal or liege — one at peace with you too, which it declares war on — and your armies there join that attack. **On your own or an ally's ground a peaceful army standing beside your army is not attacked**: your march simply joins your army there. The Player Page's move preview says when your armies will join, counting the armies standing there now; one with a march of its own queued away joins only if it is still there when the attack comes (armies move in readiness order). A beach landing that armies already ashore join is one battle: the armies that joined from the shore fall back overland if it fails, never back aboard, and the landing card says where each went — *"Your Army II, which had joined from the shore, fell back overland to (3,2)."* — while the beach's defender reads every attacking kingdom by name, each army under its own realm.

**Armies already at war that begin Phase 5 camped in the same zone of one hex fight before anyone marches — the camp sweep** (the land twin of the naval cohabitation sweep, §2.14.2): a war declared last turn between armies camped together, one begun this turn in Phase 1 (a blockade link, a vassalage ended in war), or a cornered army that could not withdraw. The ground's owner — or a friend of it — defends; on anyone else's ground the lower realm id defends. The attacking side is every army there at war with the defender that is the attacker's own or friendly to it, plus the members of any link leader among them; the defence gathers as in any battle (§5.11). **No hex changes hands**, **Ambush gives no bonus** (nobody marched into it) — **except on fortified ground you are friendly to** (your own, a mutual ally's, a vassal's or a liege's), where the ambusher already stands outside the walls on purpose and keeps its ×1.40 (§5.4, §5.8.0), Defensive and Garrison count as usual; the loser retreats — except a **besieged** army, which stays inside its walls on a loss or a draw (§2.13.7), and an army of the owner or a friend beaten outside its own walls, which goes inside in Garrison while there is room (§5.8.0); an army that fought does not rest that turn. Inside against outside a wall is a siege, not a camp clash. The cards open *"Nobody marched: your armies were already camped on the same ground when the fighting began."*

**An army that arrives beside an enemy attacks on arrival.** When a march step ends with an army — the leader, or a link member carried in behind it or placed on the hex by a storm — in the same zone as an army already there that it is at war with, they fight at once, before the march goes on; a loss or draw scatters the whole link group. The full rule is the arrival clash (§5.11); at sea, a fleet carried onto its flagship's final hex does the same (§2.14.7). See Section 5.5 for formulas.

**2.13.6 Siege and Assault Orders**

**Siege**: An army with Siege stance **standing on** a foreign walled construction (camped at the gates) increments that hex's Siege Progress by 1 each turn, provided it meets the minimum siege force (§5.8.1) — an under-strength army's siege fails with no progress. Siege is stored (§5.4); filing any stance other than Siege or Assault, or marching away, ends the siege at the start of processing (§5.8.5). Assault must be ordered each turn.

**Assault**: An army holding Assault stance while camped ON a hex with a foreign walled construction storms it in Pre-Phase 3, after first beating any army standing outside the walls (§5.8.0, Section 5.6).

**Every army in a coalition fights with its own bonuses.** A side's War Power is the **sum** of its armies, each multiplied by *its own* home terrain, cavalry scaling, stance, status and commander — never the group's (§5.11). An Elf and a non-Elf ally defending together in forest fight at ×1.30 and ×1.00, and the battle card's summary prints **"mixed — see below"** wherever a side's armies disagree, with each army's real chain in the breakdown underneath.

Stances modify only the side that is **DEFENDING** (values and validity, §5.4): the attacker, a sallier included, fights at ×1.00 whatever it stood in. A landing on walls first fights the armies outside, then, if it wins, storms the Garrison inside (§5.8.0, §5.6).

**2.13.6b Two armies, one construction: the same turn**

More than one army may attack the same construction in a single turn, and they arrive in **readiness order** (§2.13.1) — a rested column can plan to arrive first.

- **Both are repelled** → when the second is the first's own realm or a friend of it, both storm the walls, both take losses, both are carded. The walls are ticked

for engine damage at most once per turn no matter how many besiegers bring engines (§5.8.6).

- **The first one in takes it** → the construction changes hands. A later arrival is **not** turned away:

it arrives and engages the NEW holder, who is now a hostile fortress like any other. A construction can therefore be **taken more than once in one turn**. What still happens only once per turn is the *damage* a conquest inflicts (§5.6.3) — the second capture does not degrade the construction again.

- **The first one is repelled but survives** → it stays **camped at the gates** (§5.8.0). A later arrival

meets that camp first, **in the open** — no walls, no fortress bonus — even when it is only at **peace** with the camper; the war begins there (§2.13.3). If it wins, and no hostile camp is left outside, it **storms the walls the same turn** (§5.8.0); if it loses or draws, it falls back to where it started.

Two consequences worth planning around:

1\. **Arriving second is often better.** If the first attacker is repelled and camps, the second fights a bloodied army in the open, then storms walls whose defenders the first storm has already thinned.

2\. **Two enemies besieging one fortress mostly help the defender.** They grind each other at the gates while the walls stand. In testing, a garrison that saw off two separate 30-strong assaults lost one or two militia doing it.

This applies to an army already camped at the gates on **Siege or Assault stance** (§2.13.6) exactly as it does to a march-in: a construction that changed hands earlier in the same turn is simply a hostile fortress under new management, and the besieger presses on.

There is one case where a stance order does stand down instead: if the construction became **yours or an ally's** — because then you are no longer standing on a foreign fortress at all. That stand-down is carded, and it is the only reason a siege or assault order lapses for a hex that changed hands.

**2.13.7 Besieged Armies and the Sally**

**Who is besieged.** When Pre-Phase 3 opens, an army is **besieged** if it stands **inside** walls — in Garrison, the only stance behind them (§5.8.0) — that a realm **at war** with it is besieging — the hex carries that realm's siege and one of its armies with soldiers still stands at the gates **and presses it this turn** (Siege or Assault, or its realm missed the turn); your Player Page cannot see the besieger's orders and assumes it does. Every realm inside counts (the owner, an ally, a vassal — besieging walls makes them all the besieger's enemies, §5.6). **When it starts.** The ring (the hex's siege) is laid either by a **Siege March** that passes the §5.8.1 force test as it arrives (§5.8.0), or by the besieger's first **siege tick**, which runs in Pre-Phase 3 *after* this check. Either way the armies inside are besieged from the turn **after** the ring is laid: a Siege March that closes it on arrival on turn T, or an army already camped at the gates that orders Siege on turn T, besieges from T+1; a Siege March too small to close it on arrival besieges from the turn after its first passing tick. An army at war with the besieger cannot simply walk in — it must beat the camp at the gates first (§2.13.3). A **friend of both the besieger and the owner** walks up to the gates and stands **outside**, like every arrival; if it then orders Garrison it goes inside, that turn's siege tick declares war on it, and it is besieged from the turn after. Any other army is engaged by the camp on arrival (§2.13.3). An army **raised** inside a besieged city is besieged at once.

**Where, and for how long.** The zone is read as the turn **began**: an army that began it outside the walls — any army not in Garrison — is not besieged that turn, and filing Ambush this turn does not step a besieged army outside. An army aboard a fleet never is. **Once besieged, it stays besieged while that ring stands**: ending its alliance with the walls' owner does not put it outside, and peace with the besieger does not free it — the next siege tick declares war on every realm inside again anyway (§5.6). Only the ring's end frees it: a winning Sally, a relief that beats the besieger, the besieger gone or no longer pressing, peace between the besieger and the owner, or the fall.

**What a besieged army can do:**

- **Garrison or Sally — nothing else.** Any other stance it holds or orders (Moving, Defensive, Siege March, Ambush) is read as **Garrison** while the siege holds, and stored as Garrison.

- **No march.** A march order is refused, and the report says so (*Army N besieged — march refused*). The only ways out are to **break the siege** — win a Sally, or a relief army from outside beats the besieger — and march the turn after, or to **embark** — a port embark only in a port you own, or a beach pickup from your own fleet on the water next door (§2.14.5); the sea stays open. A fleet that took it aboard in the port may even land it the next turn on a land hex **next to** the port without sailing out — the harbour is a door, whatever blockades the water.

- **Its link to an outside leader breaks.** A besieged member of a group whose leader is not besieged leaves the group (carded) — otherwise the leader's march would carry it out. **Nor does a link carry anyone in:** a camper outside that a besieged leader links is dropped from the group (*did not join the besieged group*).

- **No transfer across the siege line.** Troops pass between two of your armies on the hex only if both are besieged or neither is: a besieged army cannot hand its men to a camper outside to march them away, and a camper cannot reinforce the garrison through the ring (*troops do not cross a siege line*).

- **A battle lost on its own hex leaves it inside.** A besieged army that loses or draws a battle where it stands — against an enemy inside the same walls in the camp sweep (§2.13.5), or an arrival — falls back behind its walls in Garrison, never off the hex — while the ring still stands (a Sally that won this turn has lifted it, and then the loser retreats as usual). Not on a Sally (its survivors come back in anyway), and not in a last stand on walls that have just fallen.

- **It never fights outside its walls unordered** — not even beside its own realm's relief march onto the hex (a Garrison never joins a fight, §2.13.5): it goes out only by ordering Sally.

> ***▶ Example — the only door is the sea.** Hyperborea's Army II is besieged in its own port (24,34) and files a march to (25,34): refused — Army II besieged — march refused. Hyperborea's Fleet I lies in that port, so next turn Hyperborea orders II to **embark**. Boarding is re-applied in Pre-Phase 2, before anyone is marked besieged, so II is aboard, no longer besieged, and Fleet I may sail that same turn. Nemedia's VI, an ally inside, cannot board in Hyperborea's port (a port embark needs your own port); its door is a **beach pickup** from a Nemedian fleet on the water next door — the fleet is held that turn and sails the next (§2.14.5).*

**The Sally.** A besieged army that orders **Sally** goes out and fights in **Pre-Phase 3**, before the siege ticks and before any Assault on that hex:

- **One side, whoever you are.** Every besieged army on the hex that orders Sally sallies **together**, from any realm, linked or not; a link leader that sallies takes its besieged members with it. A realm at war with a realm already in the sally is **held back** (carded) — a kingdom never fights beside its enemy. Who goes in first is fixed, never the order the files were read in: the walls' **owner**, then the other realms by realm id — the order they joined the campaign. A linked **member's** own Sally order is ignored — it goes out only with its leader. A Sally with nobody at war camped outside is carded *no one to sally against* and the army stays in Garrison.

- **Against everyone outside at war with the leading realm** (the owner, if it sallies): the besieger first, then every other army camped at the gates at war with it. A realm that is not at war with every one of them is held back — a sally never starts a war for the armies that join it.

- **In the open, as the attacker.** No stance bonus, no fortress bonus, no militia — but an Imperial owner of an FI/POP settlement keeps its **Legion** ×1.10 on the sally (§4.2). The besieger defends at **×1.00** — the ×0.85 of §5.8 is only against a relief army.

- **Win:** the beaten besiegers fall back like any beaten field army — and press nothing where they land — **the siege is lifted** (progress to 0, both sides carded), and the sallying armies stand inside in **Garrison** — free to march the next turn once the ring is gone. If an army of the besieging realm still stands at the gates (one the sally did not fight, or one that held its ground), the ring holds and they are besieged again next turn.

- **Draw:** back inside in Garrison. The besiegers at the gates make **no progress** this turn and their Assault does not storm (each is carded *Siege held* / *Assault held*); a Siege stance stays stored. A fresh march onto the walls in Phase 5 still storms them.

- **Loss:** the survivors slip **back inside** in Garrison — their walls are their refuge, even when no outside hex is free to retreat to — and, when an outside hex was free to fall back to, read *"pulled back inside the walls"* on their Readiness Report (with none, they are simply back inside, charged no move) (§5.10.2). The siege ticks the same turn, and an Assault ordered by the besieger storms at once — against them, now at **Garrison ×1.30**.

- **One turn only.** Sally is not stored; next turn the army holds Garrison again unless it orders another.

- The settlement's **owner** is told of every sally fought at its gates: if it fought, on its own battle card; if it had no army in the fight, as an observer — *Battle on your territory at (c,r)* with the full combat panel.

**Sally and relief never fight as one.** The besieged inside and a relief army from outside cannot strike the besieger together in one battle. The Sally is fought in **Pre-Phase 3**; the relief's battle comes later, in **Phase 5** — a march onto the hex, or the camp sweep of an army already camped at the gates (§2.13.5) — or in **Phase 6** for a landing from the sea. They are two battles, one after the other, and neither side's war power is added to the other's. Nor can a friendly army camped outside the walls go out with the Sally — only besieged armies sally — and a Garrison inside never joins the relief's battle. What the Sally does to the besieger carries over: its dead stay dead and its status has paid that battle's cost (§5.10.4), so a relief arriving the same turn meets a weaker besieger — and meets it at **Siege ×0.85**, where the Sally met it at ×1.00 (§5.8). What the relief finds depends on how the Sally went:

- **Sally wins** — the ring is broken in Pre-Phase 3; the relief arrives to walls with no besieger at the gates, unless another army of the besieging realm still stands there, and then it fights that one.

- **Sally draws** — no siege progress this turn and no storm by the besiegers it fought; the relief then fights them.

- **Sally loses** — the siege ticks in Pre-Phase 3, and if that tick takes progress past the threshold **the walls fall in Pre-Phase 4 (§5.8.4), before the relief arrives**: its march then lands on its enemy's newly taken walls, and marching onto walls is an assault (§5.8.0). Otherwise the relief fights the besieger, and a relief that wins lifts the siege the next turn, its progress back to 0.

Two things follow. **On the turn the walls would fall, a relief arrives in time only if the Sally at least draws** — a drawn Sally stops that turn's tick. And **a Sally ordered on the turn the relief arrives makes the besieger fight twice in one turn**, the second time weaker and at ×0.85: the two blows do not add up in one battle, but they land on the same turn.

> ***▶ Example — after the siege.** II won its Sally on turn 12. On turn 13 its Orders-in-force line reads Army II (18,9) inside the walls · 74% · Garrison (kept from last turn) — order: none. The siege stored **Garrison**, and it stays in force — ×1.30 against a storm, ×1.20 in the field. The Defensive it held before the siege does not come back by itself: file Defensive, or a march (which clears the stance).*

**If the siege runs its course**, the walls fall (§2.7) and **every besieged army of the walls' owner surrenders** — it is a Garrison. A third realm's army inside — an ally's — is not the owner's garrison: it is expelled, or cut down if it has nowhere to run, as §2.7 says.

**Nobody sallies unordered.** A Garrison that is **not** besieged — on the turn an enemy arrives, before any siege — defends the walls against a march, an Assault or a landing, once the armies outside have been beaten (§5.8.0). There is no automatic sally on any route.

> ***▶ Worked example — Nemedia and Hyperborea (turns 31–35).** Hyperborea owns the walled hex (24,34); inside stand Hyperborea's Army II and Nemedia's Army VI, allies. Aquilonia's Army VII, camped at the gates, orders **Siege** on turn 31 — its first tick lays the ring (progress 1), and the siege puts Aquilonia at war with both realms inside (§5.6).*
>
> *- **Turn 32, Pre-Phase 3.** Both armies are besieged. Whatever stance Nemedia files reads Garrison, and the march VI filed out of (24,34) is refused (Army VI besieged — march refused) — the very march the engine of that time let through in the real turn 32. If nobody orders Sally, the siege ticks to 2.*
>
> *- **Turn 33 — the Sally.** Both order **Sally**. They are not linked, and it does not matter: II (the owner, first) and VI go out together as one side against VII, in the open, as the attacker. Win → VII falls back, the ring is broken, II and VI stand inside in Garrison and may march on turn 34. Draw → VII makes no progress this turn. Loss → II and VI scramble back inside in Garrison and the siege ticks.*
>
> *- **If only Nemedia orders Sally**, VI goes out alone; Hyperborea's II stays inside in Garrison.*
>
> *- **If they never sally**, progress reaches 5 on turn 35 and the walls fall in that same pre-phase: Hyperborea's II surrenders with them, and Nemedia's VI — an ally, not the owner's garrison — is expelled, or cut down if cornered (§2.7). Before that, Nemedia can still lift VI off by a **beach pickup** from its own fleet on the water next door (§2.14.5) — a port embark in Hyperborea's port is not open to it.*
>
> ***▶ Example — a Sally that wins.** Aquilonia's walled hex (18,9). Cimeria's Army III, camped at the gates, orders Siege on turn 10 — the first tick lays the ring. From turn 11, Aquilonia's Army II inside is besieged. On turn 12 II orders **Sally** and, in Pre-Phase 3, attacks III in the open at ×1.00 (no stance, no walls, no militia); III defends at ×1.00. II wins: III falls back to a neighbouring hex and presses nothing there, the siege is lifted (progress back to 0; Aquilonia reads Siege at (18,9) broken — the sally won, Cimeria Siege of (18,9) broken — the garrison sallied and won), and II stands inside in Garrison. A march II files that same turn is still refused — it was besieged when the turn began — and on turn 13 it may march.*
>
> ***▶ Example — a drawn Sally.** The same hex, but III is as strong as II and the battle is drawn. II is back inside in Garrison. III is carded Siege held at (18,9) — the sally drew: no tick this turn (progress stays where it was), and its Siege stays stored for next turn. Had a second Cimerian army marched onto the walls in Phase 5, it would still have stormed them — the draw holds only the besiegers already at the gates.*
>
> ***▶ Example — a Sally beaten, then stormed.** On turn 12 II orders Sally while III orders **Assault**. The Sally is fought first and lost: II's survivors slip back inside (pulled back inside the walls) in Garrison. Then III storms — against II at **Garrison ×1.30**, with the fortress bonus and the militia beside it. Had III held Siege instead, the siege would have ticked the same turn.*
>
> ***▶ Example — three realms, one Sally.** Hyperborea's walled hex (24,34) holds Hyperborea's II, Nemedia's VI and Zingara's I, all besieged by Aquilonia (the siege put all three at war with it, §5.6). Nemedia and Zingara went to war with each other last turn. All three order Sally. Hyperborea, the owner, goes in first; of the other two, the one earlier on the roster joins and the other — at war with it — is **held back** (held back from the sally) and stays inside in Garrison — and in Phase 5 the camp sweep sets Nemedia and Zingara on each other inside the walls (§2.13.5). Whoever loses **stays inside** while the ring still stands: a besieged army that loses or draws a battle on its besieged hex never falls back out of the siege. Had the Sally won and broken the ring that same turn, the siege would be over, and the loser would fall back like any beaten army. The two that go out fight Aquilonia as one side, with no link between them.*
>
> ***▶ Example — a sally never starts a war.** Aquilonia's walled hex (18,9) is besieged by Cimeria's III; inside stand Aquilonia's II and Zingara's I (both at war with Cimeria, §5.6), and both order Sally. Camped outside beside III stands Nemedia's IV, at war with Aquilonia but at peace with Zingara. The sally fights every army outside at war with the leading realm — Aquilonia, the owner — so IV is a foe too; Zingara is not at war with Nemedia, so Zingara's I is **held back** (held back from the sally … a sally never starts a war) and stays inside in Garrison. II goes out alone against III and IV.*
>
> ***▶ Example — the alliance breaks mid-siege.** Gruk-Mor's walled town (14,9), besieged by Aldoria since turn 2; inside stand Gruk-Mor's I and Sylvane's II. On turn 5 Sylvane ends its alliance with Gruk-Mor. On turn 6 II files a march out: refused — Army II besieged — march refused. It is no longer Gruk-Mor's friend, but it began the siege inside and **stays** inside. If Sylvane then declares war on Gruk-Mor, the camp sweep of the next Phase 5 sets I and II on each other **inside** the walls — and whoever loses stays inside too, in Garrison. At the fall, II is not Gruk-Mor's garrison: it is expelled (§2.7).*
>
> ***▶ Example — peace with the besieger.** Same town. On turn 5 Sylvane makes peace with Aldoria instead. II is still besieged on turn 6: its march is refused, and the siege tick of that same pre-phase declares war on every realm inside again (§5.6), Sylvane included. Signing peace does not open the gates — only the end of the ring does.*
>
> ***▶ Example — the harbour door.** Hyperborea's II is besieged in its own walled port (24,34), and Aquilonian galleys hold the sea hexes off the harbour. Turn 33: II **embarks** on Fleet I in the port — boarding comes before the besieged check, so II is aboard, and no longer besieged. Turn 34: Fleet I lands II on (25,34), a land hex **next to** the port, without sailing out. II is outside the ring, free to march on turn 35.*
>
> ***▶ Example — landing on your own besieged port.** Aquilonia besieges Hyperborea's walled port (24,34) with Army VII at Siege. Hyperborea's Fleet II brings Army IV from home and lands it on (24,34). That is a **beach engagement against the besieger**, in the open: IV lands at ×0.50, VII defends at Siege ×0.85 (×1.00 had it filed Assault) — no walls, no militia, and Hyperborea's besieged II inside does **not** join (a besieged army goes out only by Sally). **Win:** VII retreats, IV stands **outside** its own walls with no stance (−20 landing status) — a Garrison order takes it in next turn — and the ring lifts the next turn — your report may still carry the Under siege card that turn; it clears the next. **Loss or draw:** IV re-boards Fleet II, and the siege goes on.*
>
> ***▶ Example — a link group sallies.** Inside (24,34) Hyperborea's II leads a link with Nemedia's VI; both are besieged. Only II files Sally, and VI goes out with it — a member follows its leader, and VI's own Sally order would be ignored. Had VI's leader been an army standing outside the walls, VI would leave that group (Army VI besieged — left its link group) and order its own Garrison or Sally.*
>
> ***▶ Example — relief from outside.** Cimeria's III besieges Aquilonia's (18,9); Aquilonia's II inside is besieged. On turn 12 III's siege ticks in Pre-Phase 3; in Phase 5 Aquilonia's Army IV marches home onto (18,9) and engages III at the gates, where III defends at **Siege ×0.85**. II, besieged, does **not** join IV's attack — a besieged army never fights outside its walls unless it orders Sally; had II ordered Sally that turn, it would have fought III first, in Pre-Phase 3, and IV would have met whatever was left. IV wins and III falls back: on turn 13 no besieger presses the ring, so II is not besieged and may march, and the siege lifts that turn. Had IV lost or drawn, IV falls back off the hex and the ring holds; II, which never left the walls, is still besieged.*
>
> ***What your Player Page shows a besieged army:** a red note Besieged by X at (c,r) — only Garrison or Sally; every stance but 🏰 Garrison and 🚪 Sally greyed out with the reason; no march can be queued (it says why); a member leaving its link is told so. The Orders-in-force card reads inside the walls · besieged by X — Garrison or Sally only, no march. A realm that misses the turn holds Garrison, never sallies, and surrenders with the walls if they fall.*
>
> ***▶ Worked example — a Sally and a relief on the same turn.** Aquilonia's walled town (18,9), an ordinary settlement (it falls when progress exceeds 4). Cimeria's Army III has besieged it since turn 10 and stands at status 90%; after turn 11 the progress is 2. Inside, Aquilonia's Army II (status 80%) is besieged. Aquilonia's Army IV, one hex away at (17,9), marches home on turn 12, and II orders **Sally** the same turn.*
>
> *\| Turn 12 \| What happens \| Rule \|*
>
> *\|---\|---\|---\|*
>
> *\| **Pre-Phase 3 — the Sally** \| II goes out and attacks III in the open: no stance, no walls, no militia for II; III defends at **×1.00**. III wins at a ratio of 2.0: III pays −12 status (90% → 78%), II pays −18 (80% → 62%) and its survivors slip back inside in Garrison. III has lost men too. \| §2.13.7, §5.10.4 \|*
>
> *\| **Pre-Phase 3 — the tick** \| The Sally lost, so the siege ticks: progress 3. Not past 4, so the walls stand. \| §5.8.2 \|*
>
> *\| **Phase 5 — the relief** \| IV marches onto (18,9) and engages III at the gates. III defends at **Siege ×0.85**, at its new 78% and without the men the Sally killed. II stays inside — a Garrison never joins the relief's battle. \| §5.8, §2.13.5 \|*
>
> *\| **IV wins** \| III falls back. On turn 13 nobody presses the ring: II is not besieged and may march, and the siege lifts, progress back to 0. \| §5.8.5 \|*
>
> *\| **IV loses or draws** \| IV falls back off the hex. The ring holds, II is still besieged, and turn 13's tick brings progress to 4 — Collapse imminent — with the fall on turn 14 unless the ring is broken first. \| §5.8.3 \|*
>
> *- **Had the Sally won**, III would have fallen back in Pre-Phase 3 and the siege been lifted; IV marches home in Phase 5 to walls with nobody at the gates and stands outside them — a Garrison order takes it in next turn.*
>
> *- **Had the Sally drawn**, both pay −15, III makes no progress this turn (it stays at 2) and IV fights it in Phase 5 at ×0.85, now at 75%.*
>
> *- **Had progress stood at 4 after turn 11**, the lost Sally's tick takes it to 5 and the town falls in Pre-Phase 4: III stands inside its new walls, and IV's march in Phase 5 is an assault on Cimerian walls. A drawn Sally would have stopped that tick and kept the battle at the gates for IV.*
>
> *- **What never happens** is II and IV fighting III side by side in one battle, their war power added: the Sally and the relief are always two battles, in that order.*
>
> ***▶ Example — the besieger stood down.** On turn 14 III files Defensive instead of Siege. The ring is not pressed, so nobody at (18,9) is besieged that turn: a Sally II ordered reads Garrison (your Sally does not hold here), and both sides read Siege … lapsed. Your page could not know III's orders in advance, so it did not let you queue a march — march on turn 15, before III files Siege again (the counter restarts from 0).*

**2.13.8 War Declaration from Movement**

If an army moves into a hex belonging to — or moves to engage an army of — a kingdom not currently at war with the mover, war is automatically declared before combat is resolved. This applies whether the destination hex is **undefended** (a territory seizure) or **defended** (a field battle), and it applies even when the target is a neutral third party whose army you attack on contested or your own ground. Every such declaration costs the aggressor **−3 to −8** opinion, leaves the defender's opinion unchanged, and cards both kingdoms; an attacker who drags several kingdoms into one fight pays the aggressor penalty only once per step of a march or voyage, or once per battle (§8.5.3).

A war begun this turn also blocks every non-war stance order toward that enemy in Phase 8 of the same turn (§2.16.2).

> *A war started by attacking an army carries exactly the same opinion penalty and notification as one started by walking onto undefended land — there is no "quiet" way to begin a war through movement.*

**2.13.9 Kingdom Elimination Check**

After Phase 5 is fully resolved, TP checks every active kingdom. If a kingdom holds **zero territory** (all hexes captured or never owned), it is flagged **eliminated**:

- The eliminated flag persists in GM state across all subsequent turns.

- Existing armies are not destroyed by the flag — they continue to consume upkeep and will starve in Phase 2 if food is unavailable.

- A GM log entry is emitted **once**, the turn a kingdom is flagged (already-eliminated kingdoms are skipped), so the GM is notified. The check runs again at the **end of Phase 6**, so a kingdom whose last hex falls to an amphibious landing is flagged the same turn.

- The GM may end the eliminated kingdom's participation at their discretion.

**2.13.10 Capital Succession — The Muster Seat**

Every kingdom has a **muster seat**: the single hex where new armies are raised (Pre-Phase 2, §2.6; a recruit order that finds no army raises one here in Pre-Phase 2b) and where any army "at the capital" is considered to stand. Normally this is your **capital**. The seat matters only when your capital is taken from you — losing your capital does **not** end your kingdom or stop you raising troops; the seat simply *succeeds* to another holding.

**How the seat is chosen.** Resolved at the start of each turn, in strict priority:

1\. **Your original starter capital, if you still hold it.** As long as you own the capital you began the game with, it is always your seat. (Retaking it after a loss restores it.)

2\. **Otherwise, your current seat — unchanged.** Once the seat has moved off a lost capital, it **stays where it is**. It does **not** hop to another city because that city grew larger, or because you recruited population away. Population changes never move the seat.

3\. **Only when your seat itself is conquered** does it move again — to your **greatest surviving construction**, ranked by its level's **population ceiling** (not its current headcount), with current population breaking ties. A bare hex is chosen only if you hold no construction at all — ranked last, and **not** eliminated: such a kingdom cannot tax, recruit soldiers or build constructions (§3.7), though a standing army with soldiers can still build siege engines from stores (§2.12.1), and the state is recoverable if the GM places a construction. A kingdom holding neither is finished (§2.13.9).

> ***The one rule to remember: your seat changes only by conquest** — or, for a **Nomad**, by travelling with a camp you move (§2.11.10). It relocates the turn after your seat hex is captured — never from population growth, recruitment, or anything else. The ranking below is consulted only at the moment a seat is lost, to choose the next one; a Nomad camp move carries the existing seat with it and never re-ranks anything.*

**Two captured capitals.** If you conquer an enemy seat while still holding your own, **your own original capital remains the seat** — the captured one does not take over. Only if you have *lost* your original and hold two or more captured seats does the ranking above pick between them.

**The seat is more than a muster point.** The hex carrying your muster seat gets:

- **+0.10 fortress bonus** on top of whatever its construction's wall already earns — added before the integrity scaling, so it fades with the wall and is gone at a breach (§5.6.1)

- **Siege threshold 5** instead of 4 — an extra turn of siege before it falls (§5.8.3)

What it does *not* get is any income bonus or population bonus: those come from the construction standing there, exactly as on any other hex. Move the seat and both defensive perks move with it.

**The seat needs stack room to raise.** Army co-location applies to mustering: new armies may be raised **alongside** armies already on the seat, up to the **3-armies-per-hex** cap. On your own **walled** seat the cap is the **inside** of the walls, where a new army is born in Garrison (§5.8.0) — enemies camped outside take no room, so you can raise an army under siege; on an unwalled seat every army standing there counts. At a full seat the raise is cancelled by the Turn Processor (and recruit orders aimed at that never-raised army are cancelled with it, with a card in your report). An army frees its place by marching out, embarking, or — inside walls — taking a stance other than Garrison; a besieged army can only embark. **An army that embarks from the seat makes room the same turn** when it stood where the new army is raised (inside the walls, on your own walled seat): the raise counts it as leaving. If that embark fails, the army stays and still counts — the new army's recruits find the hex full and are not taken (nothing is charged, carded), and the army, left with no soldiers, is struck at the end of the turn. The Player Page warns when a raise fits only because of a queued embark.

**No seat = eliminated.** A kingdom that holds **no territory at all** has no seat and cannot raise armies — that is the eliminated state (§2.13.9).

> ***▶ Example — a beheaded kingdom fights on.** Your capital falls on turn 5. Turn 6, your seat moves to your greatest surviving construction, **Oakhaven** (pop 1,200) — your other holding Riverford has only 800. You raise a fresh army there and counter-attack. Over the next turns Riverford swells to 2,000, dwarfing Oakhaven — but your seat **stays at Oakhaven**, because seats move only by conquest. On turn 10 the enemy storms Oakhaven; turn 11 your seat falls back to Riverford (now your biggest). On turn 14 you retake your **original capital** — and your seat returns to it at once.*

**2.13.11 Spoils of War**

Win a land battle **decisively** and your victorious army strips the field — salvaging a share of the war material carried by **every soldier who fell, on both sides** (your own dead included). This applies to **field battles, assaults, and beach landings** alike. A beaten army that **cannot retreat** (surrounded, nowhere to run) is destroyed where it stands — and those fallen are stripped in full along with the battle dead. A **draw yields nothing**, and neither does a fight decided by **militia alone** (see below).

**What you claim.** From every slain unit — yours and the enemy's — the winner recovers a percentage of the **iron and horses** that went into raising it (a unit's build cost *is* the material it carried: the iron in its weapons and armour, the horse it rode). Units built from gold and food alone — skirmishers, light infantry — yield no metal or mounts.

**Coalitions split the haul** between the winning kingdoms in proportion to their war power, each share floored separately. That includes a beach landing that an ally's army already ashore joined: the landing kingdom and the ally share the haul by war power. **How much — the greatness of the victory.** The share scales with how lopsided the win was, measured by your battle roll against the enemy's:

|             |                         |            |
|-------------|-------------------------|------------|
| **Victory** | **Your roll vs theirs** | **Spoils** |
| Narrow      | just over 1.2×          | **20%**    |
| Hard-fought | ~1.5×                   | **30%**    |
| Solid       | ~2×                     | **40%**    |
| Strong      | ~3×                     | **50%**    |
| Decisive    | 5×+                     | **60%**    |

**Orcs eat the fallen.** An **Orc** victor also carries off **food** — not only the rations salvaged from the dead units, but the **corpses themselves**. Every body left on the field, friend or foe, is dragged back to the cook-pots: the Orc food spoil is the same victory percentage applied to (the dead units' food cost **plus one for every fallen soldier**). For a horde, a hard-won field of the dead is a feast — winning battles becomes a way to feed the war, and no other race does this.

**Starve a settlement out and the arsenal is yours.** When a besieged settlement falls by **siege auto-fall** (no assault, §2.7), the garrison surrenders intact — and hands over more than any battlefield: the besieger seizes **60–80%** (random) of the iron and horses that equipped the garrison, whatever the victor's race, and an **Orc** besieger additionally carts off **60–80%** of the garrison's food stores. Surrender pays better than slaughter (20–60%) — patience is profitable. The haul appears on your *"Enemy garrison surrendered"* report card as *⚔ Spoils of war (Surrender, N%)*. An army **cut down in the rout** at the fall (§2.7) — expelled with nowhere to retreat — is stripped at the same 60–80% (and 60–80% of its food by an Orc besieger).

**Militia are not spoils — except to an Orc.** When a hex is defended by its **populace-militia alone** — no standing garrison army — the winner claims **no iron or horses**: townsfolk carry pitchforks, and their deaths count as population loss (§5.6). But an **Orc** does not leave meat on a field it holds: fallen militia are dragged to the cook-pots at **1 food per head**, scaled by a victory-tier table sitting 10 points below the materiel one — Narrow **10%** · Hard-fought **20%** · Solid **30%** · Strong **40%** · Decisive **50%**. This applies wherever militia fall and an Orc holds the ground afterwards: **storming a walled construction** (attacker eats the defenders' fallen levy), **seizing a populated hex or beach**, and — grimly — an **Orc settlement owner whose walls repel an assault eats its own fallen townsfolk** (a third-party garrison defending someone else's settlement gets nothing: the dead are not its people). Draws feed no one. If a garrison army fights alongside militia, the garrison's fallen are salvaged at the normal battle tiers and the militia dead at the militia tiers, merged onto one card. **Naval battles yield no materiel — sunk enemy ships are taken as prizes instead (§2.13.12).**

Your turn report names the tier and the haul — for example: *"⚔ Spoils of war (Decisive, 60%): +240 iron · +12 horses"* (with *· +N food* appended for an Orc victor).

**2.13.12 Naval Spoils — Prize Ships**

Win a sea battle and your sailors do more than watch the enemy burn — boarding parties take some of the **ships the loser lost in the fight** as **prizes**, refloated and sailed home under your colours. **Every hull the loser lost in the fight rolls a die (d6): on 1 to 4 it is captured, on 5 or 6 it sinks.** The margin of victory does not change the odds — a narrow win takes prizes as surely as a rout. Your own dead ships stay dead. Hulls lost **after** the fight roll nothing: a beaten fleet **pinned against the coast** with nowhere to run sinks where it fought (§5.9.5), and those hulls go down. A **draw yields nothing**.

**A prize keeps its true nature.** A captured Barbarian *Wolfship* stays a Wolfship in your fleet — its own attack, defence, capacity, upkeep and **speed**. Prize crews are found from your survivors (no population cost), arrive **green** (base experience — never the enemy's veterancy, and folding fresh prizes into a veteran squadron of the same hull dilutes its edge), and the hull pays its normal **gold upkeep** from the next turn.

**Mind the speed.** A fleet sails at its **slowest hull** (§2.14). A 60-mp prize in an all-90-mp fleet drops you from 3 sea hexes to 2 — for a fast navy, a prize can cost more in tempo than it is worth. A prize taken mid-voyage slows the fleet at once: the rest of that voyage is sailed at the new pace. You are never obliged to keep one: transfer it to a slower fleet, or let it go down with the next fight.

**Won to the last ship.** If a battle is so bloody that the **winner's own fleet is wiped out in the winning**, the prizes are still taken: the survivors sail home aboard the captured ships, and an army carried aboard steps across with them. If no prizes were taken, the fleet is lost like any other — army and all.

**How prizes are shared.** When two or more kingdoms won together, the captured hulls are split by **war-point share** (largest remainder, ties to the stronger partner) and dealt **best first** to whoever has the most prizes still owed. A 40% partner in a five-hull haul takes two.

Your report names the haul and what it came from: *"⚓ Prizes taken: 3 of the 4 hulls the enemy lost — 2× Wolfship, 1× Reaver"*; when kingdoms won together, each card names its own prizes out of every hull the enemy lost. The loser's card stays silent — they learn where their ships went when the ships come back shooting. (Orcs and Dwarves field no fleets, and can neither take prizes nor lose them.)

**2.14 Phase 6 — Navy Movement**

**2.14.1 Initiative and Valid Terrain**

**Orders in force at sea.** Phase 6 opens with the same card for your fleets: where each one lies (in port or at sea, and any army it carries), its status, its stance in force — Raid, Blockade, Hunt or none, *kept from last turn* or *ordered this turn* — and its order (*sail* with the route, *stays*, *none*, or the flagship a linked fleet follows).

Fleets move in **rounds** by the same readiness-first rule as armies (§2.13.1): one hex per round, highest current fleet STATUS first, and **a blocked fleet stops for the turn**. Fleet fatigue is fully live — sailing costs status per hex (coastal 3 / high seas 6; Aesir 2 / 4 — §5.10.6) — so a fleet fresh out of port outraces and outfights one at the end of a blue-water crossing. Fleets move only through sea and port hexes.

**Your own route and route sightings** work at sea exactly as on land (§2.13.2). The route includes a hop where the fleet fought and, winning clearly, sailed on — *Fleet III sailed to (26,27) · route (27,26) → (26,26) → (26,27) · 3 hop(s) · At sea*, or on the card that ended the voyage, *Naval victory (Fleet I) … · Fleet I route (3,0) → (4,0)*; a forced flight after a defeat is not part of it. A fleet meets a foreign fleet on the hex it steps into — at sea or docked in the port — and foreign armies standing in that port; a linked fleet group on the move is reported once, by its flagship. The cards read *Fleet N crossed paths on its route* / *Foreign forces passed Fleet N at (c,r)*.

**2.14.2 Port Entry and Combat**

Fleets may sail to any port hex regardless of diplomatic stance toward the owner — own, allied, neutral, and enemy ports are all valid destinations. A free port is entered freely and the fleet docks there; no seizure occurs on docking alone. A hex — open sea or port — holds up to 3 fleets of any mix of relations except at-war. Neutral fleets neither block nor are blocked: your fleet may sail past them, share the hex, or dock beside them if there is room. A full hex (3 fleets) halts the move; an at-war fleet on the hex means a naval battle on arrival, as ever. Co-location applies **anywhere** — the sea has no owner, so unlike armies there is no ground gate; a rendezvous at sea is the whole point of a fleet. Port ownership changes only through **land conquest** of the hex — a march-in seizure or assault (§2.13) or an amphibious disembarkation (§2.14.6); fleets never flip a hex. Capturing a fortified port — by assault storm, siege auto-fall, or any other flip — does **not** evict a third-party fleet docked there unless it is **at war** with the captor; an allied or neutral fleet rides out the ownership change and stays docked.

**What the port's owner sees.** A foreign fleet that **ends its move** in your port — its voyage finished there, or was halted there — is carded to you once, if it is **still there when the turn's fleet movement and sea battles are over**; a fleet that only sails **through** your port on its way elsewhere is not, and neither is one that was sunk or driven out of your port later that same turn. Its hulls are counted at that moment, after any losses. A beaten fleet that **takes refuge** in your port after losing a sea battle nearby is carded the same way, and its card says it fled there and where it lost. The title follows your relation at the end of the turn: *"Allied fleet entered your port"* (mutual ally, vassal or liege, so an alliance signed that same turn reads as allied), *"Foreign fleet entered your port"* (not at war) or *"Enemy fleet entered your port"* (at war). Every card names the fleet's commander, hulls by type and war-power, and for an allied **fleet** that ties up in your port also the army it carries (allies hide nothing); **what a non-allied fleet carries stays hidden** — cargo is spy business. So a **foreign** fleet you are not at war with may tie up in your harbour and you will know its hulls; it may already have raided you as it sailed in, and can raid again from its berth next turn — each raid a declaration of war (§2.14.3) — unless it sails in a linked group, which raids only through its flagship (§2.14.7), and its card says so. **Your own harbour is the one exception** to "enemies grant only sightings": an enemy fleet in your port is carded with the same detail, because anyone on your docks can count its hulls. A fleet you commission at that port while it lies there must fight it before it can sail — give it hulls the same turn, or it is scuttled on the slipway (the card says so only to a kingdom that builds fleets at all) — and it can Raid or Blockade the port next turn. The card says whether it sailed in unopposed while you were already at war, or tied up before war broke out that turn.

**Battles in your harbour.** A fleet that has to fight its way in is not a guest: if **you** were one of the sides, your own battle card reports it; if two **other** kingdoms fight in your port, you receive *"Battle in your harbour"* naming both sides and the result, **every fleet that fought as it came into the fight** (hulls by type, war-power, commander; cargo only for allies), what each lost in that fight and where it stood at the end of the turn — still in the port, at (c,r), or sunk — said once per fleet, **the full battle report**, the same panel a combatant gets, drawn *Attacker \| Defender* with the winner named (the naval twin of a battle on your land), and every foreign fleet moored there once the fighting is over. If any fleet in the fight is **not your friend**, you see that panel *from your docks*: no crowded-decks row and no full derivation, because cargo is spy business (the panel says so). You took no part, so you suffer no losses, and ships alone never take the port.

**An enemy fleet inside your port** — a blockader or a squatter — can be fought two ways: commission a new fleet there, which defends the harbour against it before movement, or sail a fleet of yours or an ally's in to drive it out. Either way the newcomer fights at ×1.00: the port bonus belongs only to a fleet that began the turn in the harbour, attacker or defender (§5.9.2) — so a fleet kept docked there is the one that fights it at ×1.25. Several fights in the same port that turn come as **one** card naming each, with one battle panel per fight. A fight between fleets that **already shared the harbour** when the turn began — a fleet raised under an enemy's guns, or war breaking out between fleets moored together — is reported as exactly that on every side (your new fleet, your ally's new fleet, the enemy's new fleet, or war finding the fleets moored together), never as one side sailing in to attack. The clash cards say whose fleet was new, for each reader: *"Your newly raised fleet met X's ships already lying in …"*, *"Your ally X raised a new fleet in …, and yours fought beside it against Y's ships"*, or *"X raised a fleet in … while yours lay there"*; if the port's owner wins, its card title still reads *"port held, X driven off"*.

**Who fights such a clash**: on the attacking side, every fleet on the hex whose realm is **at war with the defender** and is the attacker's own or a mutual ally's, liege's or vassal's — an ally at war joins even if it is not linked — plus the members of any link group whose **flagship** is among them: members follow their flagship into its fight (and are declared at war by it — even a member allied with the defender, whose alliance then ends, or sworn to it, whose vassalage then ends), led by that flagship. A member's own war never drags its flagship's realm in — if only a member's realm is at war, that member fights and the flagship stays out, at peace or allied as before. The defending side gathers every fleet on the hex at war with the attacker — except one at war with the defending fleet or with another fleet already defending — the defending flagship's own link members count from the start — which stands aside (the same rule as any naval battle).

**Who defends** (as on land): in a port, the port's owner — or a mutual ally, vassal or liege of it — defends; otherwise a fleet raised this turn is the attacker. Neither side, nor who attacks at sea or in an unowned port, depends on the order the turn's orders were read in. Every naval battle card fought in a port names whose port it is from your side of it: a fleet beaten while lying in someone else's harbour is told it was that kingdom's harbour, and an owner that attacks an enemy squatting in its own port reads "your own port".

**The port changes hands** later that turn (ceded to an ally, or taken)? The cards go to whoever owns it when the turn ends, worded as a fleet moored in "a port that became yours this turn"; the kingdom that lost the port hears nothing more about it. The cards come once, but the view stays: hovering one of your ports on the map lists every foreign fleet moored there with its numeral, hulls by type, war-power and commander (and cargo, for allies only), for as long as it stays.

**A clear victory does not end the voyage (as on land).** A fleet that meets an enemy on a hop and beats it **clearly** — no fleet at war with it left on that hex, itself still afloat there — **sails on through its remaining hops**; a draw or a defeat ends the voyage where the fight was (a beaten fleet has retreated anyway). The same holds for a Pirate on the hunt, as hunter or as prey. A fleet that fights its way **into a port** and wins is docked there.

**2.14.3 Port Raid**

A fleet docked at a foreign non-allied port, or sailing into one, may set **Raid** stance. A raid resolves at two kinds of moment: **at the start of Phase 6** for a fleet already docked in the foreign port when the turn began — it fires even if the fleet also sails away that same turn — and **under sail, at every foreign non-allied port the voyage sails into**, the moment the fleet enters it. Set Raid on the fleet and plot the route: it plunders each foreign harbour on the way, with no warning to the owner, and **sails on** — a raid on the way through does not end the voyage (the voyage still ends at its last hop, or wherever a fight stops it, §2.14.2). At each port the order is fixed: the raid **declares war** on the port's owner and on any friend of the owner moored there (below); if any fleet now at war with the raider lies in the harbour, the **harbour battle is fought first**; the gold is taken **only on a clear win** — the raider still afloat there and no enemy fleet left in the port. A raider beaten in that battle takes nothing, and a **draw** takes nothing either and ends the voyage in the harbour. **Several ports, several raids**: a fleet that plundered its berth at the start of the phase and then sailed through two more foreign ports plunders all three — each raid at the normal take from its own port's funds, the owner's treasury cap (below) shrinking the later takes. The **same** port is never plundered twice in a turn by the same fleet: sailing out and back to your berth earns no second raid. And **a port gives up its takings once a turn, to whoever gets there first**: a second raid on it that turn, by any fleet of any kingdom — your own second fleet included — still declares war and still fights whatever is moored there, but takes **0g**, and both sides are told the port had already been plundered. A raider beaten or held to a draw in the harbour never plundered it, so the port stays open to the next raider.

**Raid amount**: floor(portIncome × raidPct / 100) — portIncome is that port's Phase-1 gold this turn, after any bracket reduction (§2.9.4) — gold only, food excluded. The take is additionally **capped by the owner's treasury** at raid time: you steal only what they actually hold, and an empty treasury yields 0g (the war is declared regardless).

**Raid efficiency** scales with the raiding fleet's total war power relative to the strongest living fleet this turn: raidPct = clamp(20, 80, round(20 + (thisPower / maxFleetPower) × 60))

The weakest possible fleet raids at 20%; the strongest at 80%. Gold is transferred directly from the defender's treasury. Ownership and population are unchanged, but **a raid declares war** on the port's owner (see below).

**A raid that cannot fire is told so.** A fleet that sails with Raid set plunders every foreign harbour it enters; one whose voyage enters none — sea all the way, or only your own, an ally's or unclaimed ports — takes nothing and is told why, once, at the end of the phase. The Player Page offers Raid whenever the berth or any hop of the route is a foreign port, and drops the stance, saying so, the moment the route no longer enters one. Set Raid on a fleet that is docked in your own port or in an ally's, or whose voyage enters no foreign port, and your report carries a ⚡ *"Raid not possible this turn"* card naming the reason; nothing is taken. A raider **beaten** in a harbour gets no such card — its battle card is the answer. **Raid is a per-turn order — it never carries over** (only Blockade — while it bites, §2.9.3 — and a pirate's Hunt, §2.14.9, are stored). To plunder, hold position in the foreign harbour and **set Raid again next turn**; a fleet left without a stance order does nothing.

**Raiding declares war**: A raid is an act of war. Raiding a non-allied port automatically **declares war** on its owner (unless you are already at war), applying the standard war-declaration opinion penalty (−3 to −8) and pushing a war notice to both kingdoms. Because you are then at war, a defending fleet at the port **engages yours in naval combat** — at anchor, the port-cohabitation battle that follows the plunder; under sail, the harbour battle fought **before** any plunder — so a raid never goes unopposed, and a strong enough defender can sink the raider. **The owner's friends defend the harbour too**: a fleet moored in the raided port whose kingdom is a mutual ally, vassal or liege of the port's owner is declared at war by the raid as well and fights beside the owner — even when the owner has no fleet there at all, and even if that kingdom was your ally until then (the war ends the alliance, as any war does). A fleet of a kingdom that is merely neutral to the owner stays a bystander, as in any harbour fight. The raid and that harbour clash are **one engagement**: when the clash also drags a link member of the owner into the war, the aggressor opinion penalty is still paid only once. If you are already at war, the raid simply proceeds. You therefore cannot raid a kingdom and remain at peace with it — the Player Page warns you (⚠) before you set Raid stance.

**First come, only served**: when several fleets raid the same port in one turn, the first raid to reach the plunder step — anchor raids resolve first, in file-load order, then raids under sail as the fleets sail in — takes its share; every later raid on that port takes nothing (above). (A **linked group** raids as one — see §2.14.7: the flagship raids **once** with the group's summed power, not once per hull.)

**The treasury cap is first-come first-served too**: raids on *different* ports of the same victim are paid in the same processing order, each capped by what the treasury still holds — no proration — so a target that looks rich may already have been stripped bare by an earlier raider that turn.

A blockaded port (Section 2.9.3) generates no income, so a raid against it yields 0g.

**Raiding tires the crews.** A turn in which the fleet raids costs it status once, on top of its sailing and any harbour fight — see the **Raid** row of §5.10.6.

> ***▶ Example — the empty-port trap.** A player may reason: "you do not need fleets to defend ports — a raider has to dock the turn before, I read its hulls in my report, and I buy just enough ships to beat it." Two rules make that wrong:*
>
> *- **Raid under sail.** A raider plunders on turn N, the moment it sails into the harbour — and it need not even stop there. There is no warning turn. The only thing that stops it is a fleet moored in the harbour, yours or an ally's: the raider must beat it as it comes in, and takes nothing if it does not.*
>
> *- **Garrison bonus.** A reactive fleet bought on turn N+1 is a fleet **created this turn**: it was not in the port when the turn began, so it fights at **×1.00**. Had you kept even a small fleet docked there and bought hulls into it, that fleet fights at the full ×1.25 — the bonus follows the fleet that began the turn in the harbour, not the hulls. A fleet that sails in from the next port to help fights at ×1.00 too.*
>
> *Net effect: a standing fleet in the harbour is what defends a port. Buying ships after the enemy shows up still works — into a fleet that was already there, or as a new fleet with no bonus — and only after the first raid has already landed.*
>
> ***▶ Example — a raid along the coast.** Nemedia's Fleet II (8 Drommunds, 90 mp: three hops) sets Raid and plots (12,8) → (13,8) → (14,8), where (12,8) and (14,8) are Aquilonian ports and (13,8) open sea. Hop 1: the fleet enters (12,8); nobody is moored there. The raid declares war on Aquilonia, takes 60% of that port's income this turn — say 1,200g of 2,000g — and the fleet sails on. Hop 2: open sea. Hop 3: the fleet enters (14,8), where Aquilonia's Fleet I (2 Busse) and its ally Hyperborea's Fleet III (1 Busse) lie at anchor. Aquilonia is already at war; the raid now declares war on Hyperborea too, and the harbour battle is fought at once — Nemedia attacking, Aquilonia's fleet leading the defence at ×1.25 (it began the turn in its port, §5.9.2) with Hyperborea's beside it. Nemedia wins clearly: both defenders are driven out, the port gives 60% of its income, capped by whatever Aquilonia's treasury still holds after the first raid, and Fleet II ends the turn docked at (14,8), enemy of two kingdoms. Had the defenders held (a draw) or won, (14,8) would have paid nothing and the voyage would have ended there — the first port's 1,200g stays taken either way. Fleet II pays the raid's −3 status once, though it plundered two ports, on top of its three hops and the battle (§5.10.6).*

**2.14.5 Transported Armies**

**Only your own fleets carry your armies — and your fleets carry only your armies.** Transport never crosses a banner, whatever the relation: an ally's, liege's or vassal's fleet can never take your army aboard, and your fleet can never take theirs. Both the army and the fleet named in an embark order must be yours; the Player Page only offers your own fleets, and the Turn Processor looks for both among your own forces only. To move an ally's army by sea, the ally needs a fleet of its own.

**A port embark boards only in a port you own.** Your army and your own fleet standing together in a port is not enough: the port must be **yours**. An ally's port lets your fleet dock and **land** troops there, but never take them aboard — and a neutral or enemy port does not either. The Player Page only offers a port embark in your own ports, and the Turn Processor refuses any other with a **"Port embark failed"** card that says the port is not yours and how to board instead. Ownership is read at the start of the turn, when boarding happens (Pre-Phase 2). To board anywhere else, use a **beach embark**: your own fleet rides at anchor on a sea hex next to the army, and the army boards from the land — any land but a mountain, whoever owns it (§2.14.6).

**Where your army can board:**

|                                                          |                                   |                                               |                                     |
|----------------------------------------------------------|-----------------------------------|-----------------------------------------------|-------------------------------------|
| **Your army stands on…**                                 | **Your own fleet is…**            | **Port embark**                               | **Beach embark**                    |
| Your own port                                            | docked in that port               | ✅                                            | —                                   |
| An ally's port                                           | docked in that port               | ❌ refused (*not yours*)                      | —                                   |
| A neutral or enemy port                                  | docked in that port               | ❌ refused (*not yours*)                      | —                                   |
| Any land hex but a mountain — yours, an ally's, anyone's | at anchor on a sea hex next to it | —                                             | ✅                                  |
| A mountain                                               | at anchor next to it              | — (players cannot build a port on a mountain) | ❌ **never** — a cliff, not a shore |

**An army on a mountain cannot board at all.** There is no beach under a cliff, and players cannot build a port on a mountain. March it down to a lower coastal hex first — your own port for a port embark, or any other coastal land for a beach embark.

Either way the fleet must already be where the table says **at the start of the turn**: boarding happens in Pre-Phase 2, before any fleet sails (Phase 6). A fleet that sails into position this turn can take the army aboard from **next** turn. After a **port** embark the fleet may sail the same turn; a **beach** pickup holds it at anchor for that turn (§2.14.6).

> ***▶ Example — whose ships, and whose port.** Your Army II stands in your ally's port at (24,34), and you want it home.*
>
> *• Your ally's **Fleet I** is docked right there with room to spare. **Army II cannot board it**, and your ally cannot order it to — transport never crosses a banner.*
>
> *• Your own **Fleet III** is docked in the same port. A port embark is **refused** — "Army II and Fleet III are in a port that is not yours" — the army stays ashore and nothing is lost.*
>
> *• **Turn 1:** Fleet III sails out to the sea hex next door, (24,35). **Turn 2:** Army II boards it by **beach embark** at the start of the turn — a beach pickup holds the fleet at anchor for that turn (§2.14.6, row 6). **Turn 3:** Fleet III sails away with Army II aboard.*
>
> *• Had Army II and Fleet III stood together in **your own** port at (27,31), one port embark would have done it in a single turn — and a port embark does not hold the fleet, so it sails the same turn.*
>
> *• The other way round is open: Fleet III can sail into your ally's port with Army II aboard and **land** it there.*

A fleet transporting an army moves with the fleet in Phase 6. Armies do not move in Phase 5 while embarked.

**Hulls lost with an army aboard.** A fleet can only carry what its hulls hold — each soldier takes 1 tonnage, a mounted soldier 2 — and that is checked when the army boards. If a naval battle then sinks **some** of the fleet's ships, the soldiers the surviving ships cannot carry drown with the sunk hulls. The losses are spread proportionally across the army's units, the army is cut to exactly what the remaining ships hold, and a card tells you how many went down. It applies to the winner, the loser and a draw alike, after any captured prize ships have joined the fleet. The army's commander is not harmed by it. (If every ship sinks, the whole army goes down with the fleet.)

> ***▶ Example.** Fleet I carries 400 foot and 50 horsemen — 500 tonnage — in 5 Drommunds (100 capacity each). A battle sinks 2 of them: 300 capacity is left, so 200 tonnage must go. Proportionally that is 40% of each unit: 160 foot and 20 horsemen drown, and Army I sails on with 240 foot and 30 horsemen — exactly 300 tonnage.*

**2.14.6 Disembarkation**

When a fleet with a transported army moves to a position adjacent to (or at) a land hex, the army may disembark — but only via an **explicit \`disembark_army\` order** (sailing next to a coast does not unload the army by itself). **Landing into fog.** The landing hex is chosen next to where the voyage **ends**, and either hex may be unrevealed (❔): the Player Page offers a fog neighbour as *Unknown (fog)*, and the real terrain decides at the end of Phase 6. If a fog hex on the route proves to be land with no port, the fleet stops on the hex before it (§2.14.1), and a landing hex that is then not next to the fleet fails. If it proves to be a port, the fleet sails in, and can land from there only if the port is yours or a mutual ally's. A landing hex in fog that proves to be sea or a mountain coast is refused; one that proves to be land is landed on by the rows below. A refused landing leaves the army aboard, carded. **Timing:** disembarkation resolves **at the end of Phase 6**, in a separate pass **after every fleet — yours and the enemy's — has finished moving**, and always from the fleet's **final** position. It never happens at the start of the move or partway along the path: a fleet sails its whole route first, *then* the army lands. **Where the fleet may land from**: from a **sea hex** (any adjacent land hex is a valid target), or from a port owned by **your own kingdom or a mutual ally** (the port hex itself or any neighbour). A fleet docked in a **neutral or enemy** port cannot disembark anywhere — sail out to sea first. Embarking has its own gates (§2.14.5). What happens depends on the target hex:

|                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Target hex**                                                                                                                                                                                                             | **Result**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Own or allied territory, clear                                                                                                                                                                                             | Army lands freely.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Own or allied territory, **friendly army present** (own or allied, incl. an army stationed at your capital)                                                                                                                | Army **lands alongside it** — co-location, up to **3 armies per hex** (§5.11). Only a **full** hex (3 already) blocks the landing; the army then stays aboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Own or allied territory, **any army present that is not yours or a mutual ally's / liege's / vassal's** — even one at peace with you, and even with a friendly army standing beside it: the landing **declares war** on it | **Beach engagement** — an Amphibious Battle (§5.7, ×0.50 beach penalty) against the intruder. The hex **never changes hands** (you are reclaiming your own ground, or liberating an ally's); a repelled landing force re-boards the fleet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Enemy walled construction**                                                                                                                                                                                              | **Assault** resolves immediately (§5.6) — no Amphibious Battle when nobody stands outside; the army storms the walls directly from the beach. Every realm inside, your own ally included, is declared on (§5.6); the armies outside meet the landing first, on the beach, and if it wins, the Garrisons behind the walls defend the storm that follows (§5.8.0). **On a foreign walled hex, any army camped outside the walls that is not your mutual ally, vassal or liege is fought — at war or at peace — and a friend camped beside it does not shield it: your landing goes past that ground to the walls only when every army outside is a friend of yours.** The landing ranks the outside camp exactly as a march does (§2.13.3), so the sea route and the land route never disagree. Walls count as foreign when another realm owns them and it is not your mutual ally, vassal or liege — a neutral's walls included: a landing that loses or draws on the beach, or is repelled from the walls, does not re-board but digs in outside them (−20, §5.7.2). Walls nobody owns, and your own, an ally's, a vassal's or a liege's walls, follow the other rows. |
| **Enemy or unowned open land with an army on it**                                                                                                                                                                          | **Amphibious Battle** resolves (§5.7) — attacker suffers a ×0.50 beach landing penalty. The army you land against defends whoever it belongs to — war is declared on it — and every other army there at war with you, or linked under it, defends beside it; one at peace with you and unlinked is a bystander (§5.7). **A friend of yours is never fought**: you land beside it if the hex has room and take the hex as if it were empty, or stay aboard when it has none, carded *"No room beside X's army, a friend of yours"*. Win → land & seize (an unowned hex is claimed too); repelled → re-board.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Enemy open land, undefended                                                                                                                                                                                                | The populace fights as **militia** — a WP contest at the ×0.50 beach penalty (same resolution as a land seizure, §2.13.4); a hex with **no population at all** is simply taken. Win → land & seize; repelled → re-board the fleet (destroyed only if no unit survives the fight).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Enemy walled construction, outside zone already full**                                                                                                                                                                   | Landing **blocked** — the ground before the walls holds 3 armies already; the army stays aboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Siege March stance** onto an enemy walled hex with nobody camped outside                                                                                                                                                 | No fight: the army lands and **camps at the gates** (pays the −20), declaring war and **laying siege** (Siege stored; the ring closes at once if the force is enough, progress from next turn — §5.8.0) — the sea-borne twin of the marching Siege March (§5.4).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Unowned open land, clear (or held only by a friend of yours with room)                                                                                                                                                     | The populace fights as **militia**, exactly as on undefended enemy land (×0.50 beach penalty); a hex with **no population at all** is simply taken. Win → land and **claim** it — nobody owned it, so no war begins and no banner is lowered; repelled → re-board the fleet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Unowned walled construction**, clear                                                                                                                                                                                     | Army lands freely and **claims nothing** — walls nobody owns are taken only from the land side, by marching onto them (§2.13.3, §5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Mountain hex**, any owner                                                                                                                                                                                                | **Refused** — cliff, not shore: nowhere to run a boat aground, the twin of the beach-pickup rule. The army stays aboard and is carded; the Player Page never offers a mountain coast it can see — an **unrevealed** (❔) landing hex that turns out to be a mountain is refused the same way. Land on a lower coastal hex and march up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**Loading consumes the army's turn.** An army that embarks **cannot also land that same turn** — the Turn Processor refuses the landing with a card and the troops simply stay aboard, ready to land from the next turn on. This rule is not port-specific: it covers **both ways aboard** described below — a beach-picked-up army is just as landing-blocked this turn as a port-boarded one. The **fleet's own movement is unaffected by the army-side rule**: for a port embark, embark and sail as far as you like in one turn; only the landing waits (a beach pickup additionally holds the fleet itself — see below). This is the mirror of re-embarking, which has always taken effect only at the start of the following turn — every transition between shore and ship costs one turn boundary, in both directions. **Consequence for defenders**: an invasion fleet must spend at least one turn visibly at sea (or off your coast) before its troops can hit the beach — the single-turn embark-sail-land strike does not exist.

> ***⚠ Ordering — why a "safe" hex can still fall this turn.** Land combat (Phase 5) resolves **before** the navy (Phase 6). A coastal hex that no army marched on in Phase 5 is not safe for the turn: an enemy fleet that carried an army adjacent to it can disembark and seize it in Phase 6, after your land phase is already over. Defending a coastal hex against this means one of two things — **deny the sea** (a blockading or escorting fleet to sink or stop theirs before they reach the shore), or **hold the hex with an actual army** (then the landing resolves as an Amphibious Battle against your army, §5.7, not a one-sided militia contest). Militia alone, at the ×0.50 beach penalty, is often not enough.*
>
> ***Getting a landed army back to sea — two ways aboard.** Once an army has disembarked it is a **normal land army**, and there are two ways to re-embark it:*
>
> *- **Only your own fleets carry your armies** (both doors below): never an ally's fleet, though your own fleet may land your army in an ally's port (§2.14.5).*
>
> *- **Choosing the fleet.** When more than one fleet can take the army — two docked in the port, or a docked one and one riding at anchor on a neighbouring sea hex — the army card asks **which**, and states the price of each door: a docked boarding costs the army −5 readiness and the fleet nothing; a pickup from a fleet at anchor costs that fleet −15 as well.*
>
> *- **Port embark**: the army must be standing **in one of your own ports, with one of your own fleets docked there** (§2.14.5) — and you issue an **\`embark_army\` order**, which re-applies at the **start of the next turn** (Pre-Phase 2, §2.6). The boarded fleet may still sail that same turn.*
>
> *- **New fleets carry nothing on their first turn.** Embarkation re-applies at the **start** of the turn (Pre-Phase 2), but ships are only commissioned at **Phase 4** — so a fleet created this turn, or one whose ships were all ordered this turn, has **no hulls when boarding resolves**, and the embark is refused ("commissioned this turn" card). The Player Page blocks the order up front for the same reason. The working pipeline is two turns: **turn N** create the fleet and build its ships; **turn N+1** embark — and the fleet may still sail that same turn. Capacity follows the same clock: only ships that existed at the start of the turn count toward what an army can board this turn.*
>
> *- **Beach embark**: the army boards one of your own fleets **riding at anchor on an adjacent sea hex** — no port required. Issue **\`embark_army\` with \`beach:true\`**; it re-applies in the **same Pre-Phase 2 pass** as port embark, before Phase 5 combat runs (both paths share one order type and one ARMY LINK gate — a linked army cannot embark either way; UNLINK first, §5.11). The **fleet** side is gated too: a fleet in a **FLEET LINK** group (leader or member) cannot hold for a beach pickup either — UNLINK the fleet first, §2.14.7. There is **no ownership, siege, or diplomatic-stance gate on the origin hex** — the pickup works from your own ground, an ally's, a neutral's, or straight out of hostile territory you're holding, at peace or at war, besieged or not. There is exactly **one terrain that refuses it: \`mountain\`**. A mountain coast is cliff, not shore — there is nowhere to run a boat aground — so an army standing on a mountain hex cannot be picked up no matter how close the fleet rides. March it down to a lower coastal hex first. (This bites only the beach path: a port cannot be built on a mountain, so port embark is unaffected.) A refused pickup costs **no status** on either side. **Mind the asymmetry — the sea road onto a mountain runs one way.** Nothing stops you landing an army on a mountain coast; only the pickup is refused. An army put ashore there **cannot be taken off again by sea**: it must march down to a lower hex first, and on an isolated mountain coast with no friendly land to march to, it is stranded for good. Do not use a mountain as a beachhead. The trade-off is the fleet's whole turn: **loading over open water consumes the fleet's move** — its Phase 6 sail order is refused (carded "held for a beach pickup") and it sails again only next turn — on top of the shared no-same-turn-landing rule above. Every refusal is carded, never silent: the fleet isn't riding empty at anchor on a sea hex, the two aren't neighbours, another army already has the hold, the army's tonnage outweighs the fleet's capacity, the army is already aboard another fleet, the fleet is in a link group, or the army is standing on a mountain. Status: army **−5**, fleet **−15** (§5.10.2, §5.10.6).*
>
> ***⚠ Which door you used is decided by where the FLEET is, not where the ARMY is.** Standing on your own port hex does not make it a port embark. If the hull you board is riding at anchor on a **sea hex** rather than docked at the port, it is a **beach pickup** in every respect — including the two that surprise people: **that fleet gives up its turn** (its sail order is refused) and it pays the extra **−15 fleet status** for the open-water load. Your Player Page says so on the embark panel before you click, naming the fleet, **the sea hex it is riding at anchor on**, and the status charge. Read that coordinate, not the fleet's home port: a fleet's home port is only the **last port it docked at** (any owner; cleared if it is forced to flee a port), so "home port: your capital" tells you nothing about where the ship is today. If you want to embark and sail in the same turn, the fleet must actually be **docked in the port** with your army standing on that same hex.*
>
> ***Consequence:** an army landed deep in hostile territory is not automatically stranded — an escort fleet anchored within reach of the beachhead can pull the army out again next turn, regardless of who holds the ground. What still strands it is the absence of that fleet: with no hull of your own anchored adjacent (or docked at a reachable port) and no friendly land to retreat onto, a lost battle still **destroys the army where it stands**. Plan the extraction fleet before you plan the landing. A defeated army never retreats onto a ship mid-battle (retreat is land-only, §5.5) — embarking is always a deliberate order, never an automatic escape.*
>
> ***⚠ What this means — embarking is all-or-nothing.** While an army is aboard a fleet it cannot move on its own, recruit, siege, disband, dismiss units (§2.6), or split (§2.12b), and it shares the fleet's fate completely. If that fleet is sunk in naval combat — or scuttled when its last ship dies — **the embarked army is destroyed outright**: no survivors, no swimming to shore, no stranding on the nearest coast. One lost sea battle can erase your entire invasion force. Never sail your main army through waters an enemy fleet can reach without a fighting escort, and remember that a defended shore adds the beach-landing penalty on top (§5.7).*

**▶ Example — one turn, what fits.** The sequence that decides everything is fixed: **Pre-Phase 2 embark → Phase 5 army moves → Phase 6 fleets move → end of Phase 6 landings.** Nothing lets an army both change position on land and change ships in the same turn; every combination that tries is a ❌ below.

|        |                                                                    |               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\#** | **Combination in ONE turn**                                        | **Possible?** | **What actually happens**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1      | Port embark **+ fleet sails**                                      | ✅            | Army boards at turn start, the fleet carries it the whole route.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2      | Port embark **+ fleet sails + disembark** at the destination       | ❌ landing    | Army boards, fleet sails, the landing is **refused** ("troops still stowing aboard") — it stays aboard at the fleet's final hex and lands next turn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 3      | Port embark **+ army move order**                                  | ❌            | The army is aboard from Pre-Phase 2; its own march never runs (the Player Page blocks the order up front).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 4      | **Army marches to the port + embarks**                             | ❌            | Embark reads the army's **start-of-turn** hex. Turn N march, turn N+1 embark (and sail).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 5      | **Fleet sails into port + army embarks**                           | ❌            | The mirror: the fleet must already be docked or anchored at turn start. Turn N sail in, turn N+1 board (and sail out).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 6      | Beach pickup **+ fleet sails**                                     | ❌ fleet      | Army boards from the adjacent shore; the fleet's sail order is **refused** — it sits at anchor this turn and pays −15 status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 7      | Beach pickup **+ disembark**                                       | ❌ both       | Fleet held **and** landing refused. Nothing useful happens.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 8      | **Fleet sails + disembark** (army boarded on an earlier turn)      | ✅            | The invasion move: the fleet completes its route, then unloads from its **final** position onto any adjacent land hex — or, if it ends docked in an **own or allied** port, onto that port hex or any neighbour. From a neutral or enemy port: no landing.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 9      | Disembark **+ army move**                                          | ❌            | Landing is the last thing in Phase 6; Phase 5 is over. The army stands where it landed and marches **next** turn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 10     | Disembark **mid-route**, fleet continues                           | ❌            | Landings happen only from the final hex. End the route where you want the beach.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 11     | Disembark **+ re-embark** (beach or port)                          | ❌            | Embark is next turn's Pre-Phase 2 at the earliest. Land, wait a turn, then board.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 12     | Army aboard, **fleet sails, no landing**                           | ✅            | The army rides along, every turn if you like — its status is frozen while aboard (§5.10.2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 13     | Army aboard, fleet **fights at sea** before landing                | —             | If the fleet survives, the landing still resolves from its final hex; if it is sunk or scuttled the army is **destroyed outright**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 14     | Landing onto own/allied ground **already holding a friendly army** | ✅            | Lands alongside — up to **3 armies per hex** (§5.11); only a full hex blocks it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 15     | Landing on an enemy walled hex — defender in **any** stance        | —             | Every realm inside the walls is declared on (§5.6); only a Garrison stands inside (§5.8.0). Any army camped **outside** that is not yours or a mutual ally's / liege's / vassal's — the owner's armies not in Garrison and a **neutral** included — is fought first, in the open (ordinary beach engagement, no fortress bonus; war is declared); **win it** and the landing storms the walls the same phase; an **allied** camper is left alone. With the beach clear the landing assaults the Garrison inside (§5.8); a repelled survivor does **not** re-board — it unloads to a **beachhead outside the walls** (−20 status), and so does a landing that loses or draws the beach fight outside. |
| 16     | Embark by a **linked** army, or pickup by a **linked** fleet       | ❌            | Refused — UNLINK first (§5.11, §2.14.7).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 17     | Embark onto a fleet **created or fully built this turn**           | ❌            | Refused — ships commission in Phase 4, boarding is Pre-Phase 2. Turn N create + build, turn N+1 board + sail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 18     | Army moves ashore **and** its own fleet sails, unrelated           | ✅            | Independent orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Fastest legal pipelines: **invasion from home** — T1 create fleet + build ships → T2 embark + sail → T3 sail + land → T4 the army marches; **extraction from a hostile beach** — T1 fleet anchors adjacent → T2 beach pickup (fleet held, army boards) → T3 sail (and land elsewhere).

**2.14.7 Fleet Link Groups**

Friendly fleets that share a hex may **link** into a single group that sails, fights, raids and blockades as one — the naval twin of army link groups (§5.11). One fleet is the **flagship**; the others sail under its command.

- **Forming a link.** End a turn on the same hex as another of your fleets, or a mutual ally's, and use the ⛓ Fleet Link panel on the fleet card. Linking your **own** fleets forms the group immediately. Proposing to an **ally** sends an offer — the group forms when the ally submits a LINK ACCEPT (a same-turn handshake works, or they accept the standing offer on a later turn). A group holds at most **3 fleets** (the co-location cap).

- **Sailing as one.** Only the **flagship's** move order drives the group; a linked fleet's own move order is ignored — so the page never lets a queued route and a link **coexist**: you cannot link a fleet that has a route planned, and you cannot take back a queued UNLINK — or a queued *release* of a member — while the freed fleet still holds a route; clear the route first. Nor may a flagship that has a route planned take a **slower** fleet into its group — shorten the route to the new pace first. A formed fleet group likewise shares every member's hulls, readiness and commander with all of its members. The group sails at the pace of its **slowest hull of its slowest fleet** — and the flagship's Movement box budgets at that same group pace (marked *⛓ group pace*), so the route you can plan is the route the convoy will actually sail — and its members follow onto the flagship's hex. Readiness (status) **levels to the group's lowest** each turn — a docked group rests first, then syncs down to the weakest.

- **Combined offense.** When the flagship sails into an enemy-held hex, the **whole group fights** as one force, each fleet adding its own war-power. **Joining a link is a commitment**: the flagship points the group where it will, and every member fights there — **even against a kingdom that member is at peace, or allied, with.** Fighting means war, so a member so committed is **declared at war** with the flagship's target, and an existing alliance with that target is **broken**. The same holds when the group already lies in a port or at sea beside an enemy fleet as the turn begins: if the flagship's realm is at war with that fleet, the whole group fights the pre-movement clash; if only a member's realm is, that member fights and the flagship stays out. If the attack fails or is drawn, the group scatters; a member that never sailed onto the battle hex holds where it lies, and its card says so. **A member carried onto the flagship's final hex that is at war with a fleet already there attacks it on arrival**: the fleet already there defends, only carried fleets at war with it fight — the flagship stays out — there is no Ambush at sea, and a beaten member scatters the whole group and **falls back to the hex its flagship came from on its last step** — or, if that hex is closed to it, the nearest refuge from there — never back to where the voyage began; the flagship's card names the fleet of its group that was beaten. A member fleet of another realm is also carded when its flagship is halted for lack of room. Do not link under a flagship whose fights you are unwilling to join — wherever it attacks, defends or blockades, your realm goes to war with that enemy (linking under a flagship that is merely at war declares nothing); unlink first if you object to the target.

- **Defence pulls the group in, at any price** (army parity — §5.11). **Fleets already on the hex join an attack too**, on the land terms (§2.13.5) — a carried fleet's attack on arrival included. When the *flagship* is attacked, every fleet linked under it fights beside it — even one **at peace** with the attacker, which is thereby **declared at war** with it: the link is consent. That holds for the attacker's own ally, vassal or liege too: it fights beside its flagship and the alliance breaks. A co-located fleet *outside* the link joins only if it is already at war with the attacker — and not at war with the flagship's realm or another defender, its link members included. If the flagship loses, the group scatters and every member's card names the battle (§5.11 wording). **A kingdom never fights on both sides of one naval battle** either: your fleet in the defence stands aside, carded *"held back"* (§5.11.1).

- **Group raid and blockade.** A group **raids** a port **once**, with the members' **summed** power (not once per fleet), and **every** fleet in the group pays the raid's readiness cost (§5.10.6). A group **blockade** suppresses the port once, and **every** fleet in the group pays the blockade's readiness upkeep — and is party to it: a member whose realm is not yet at war with the port's owner is **declared at war** with it that turn, ending any alliance between them (the link is consent, exactly as when the group is attacked), and carded *"Fleet N joined a blockade"*; a realm charged for that war is not charged again by the harbour clash at that port the same turn — nor at any other port of the same owner its fleets blockade that turn. The war is declared once Phase 1's income is settled, so a pact between the two realms pays both or neither that turn, and it counts as a war begun this turn — no alliance can answer it until next turn (§8). **Both Player Pages warn**: the flagship's Blockade names the linked fleets of other realms it would put at war, and a fleet linked under a blockading flagship says its realm will be at war with the port's owner, naming an alliance — or a vassalage — that would end — unlink to stand apart. **And before you link at all**: a fleet-link offer from a flagship that ended the last turn holding a Blockade in an enemy port says so — on the offer's report card and beside **✓ Accept**: *"Accepting while it holds makes your realm a party to it — declared at war with \<owner\> this turn"*, adding *"ending your alliance with \<owner\>"* when your realm is the port owner's mutual ally — or *"ending the vassalage between you and \<owner\>"* when it is the owner's liege or vassal, since war ends vassalage (§2.16.4); an alliance you only proposed, and the owner never accepted, does not count (offers are settled before Phase 1, so the war comes the turn you accept if the blockade still bites; a realm already at war with the port's owner is only reminded). Every fleet-link offer carries the note *"A link is consent: wherever the flagship fights or blockades, your fleet goes with it — and your realm is declared at war with that enemy"*. That is the whole commitment: linking under a flagship that is merely at war with someone, and neither fights nor blockades them, declares nothing. A flagship set to Blockade in an enemy port shows a warning at the foot of its Fleet Link panel — while it offers an allied Propose, and still after the proposal is queued — that a realm accepting its link is declared at war with the port's owner. The offer's warning reads the flagship's stance at the end of the turn your report was written: a flagship that turns Blockade on in the same turn you accept is covered only by the consent note. A member's own raid/blockade order is ignored — the flagship acts for the group.

- **Leaving.** Any member may **UNLINK** to act independently again (same turn). The flagship may **release** a specific member or **dissolve** the whole group. The flagship's card shows only what is still possible: once a **dissolve** is queued the Release and Dissolve buttons disappear and the card reads "Queued: DISSOLVE GROUP" with a Cancel; a released member loses its Release button and is listed as "Queued: RELEASE F N"; releasing the **last** member is recorded as a dissolve (the engine dissolves a group of one anyway); and a Dissolve ordered over pending releases folds them in instead of being refused — unless a released member has already planned a route under that release, in which case the page asks you to clear that route first (the same rule that guards cancelling a release). The member list and the "last member" test read the group as the Turn Processor reports it, not the hexes' flags. The army card behaves the same way. A defeat in battle **scatters** the group and breaks the link; so does losing the flagship. And a link **cannot outlive the relationship it was built on**: war, an ended alliance or renounced fealty releases the member at the **end of that turn**, carded on both sides — the army rule, flagship ↔ member (§5.11 *Command*).

**2.14.8 Wrapped maps (per map)**

A map may declare that its opposite edges touch — **east↔west**, **north↔south**, or both. It is a property of the **map**, set by the GM in the Map Editor's *Map Settings* and carried with the export into the campaign; every page reads it from its report, so a map that says nothing about wrap is exactly the hard-edged map you know. On a wrapped axis there is no edge and no corner: every hex has six neighbours, an edge hex borrows the missing ones from the far side, and with both axes on a corner hex is one step from the opposite corner.

What changes on a wrapped axis, and only there:

|               |                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | **Wrapped axis**                                                                                                                                                 |
| **Movement**  | A hop across the seam is one ordinary hex; the route you plan shows the far-edge hexes as next hops.                                                             |
| **Distances** | Spy cost and loss chance, caravan transit and any range are measured the short way round (§2.8.2, §2.15). Nothing on a wrapped map is farther than half the map. |
| **Sea class** | A sea hex on the old edge that touches land across the seam is **coastal**, not high seas (§5.10.6).                                                             |
| **Borders**   | Kingdoms on opposite edges are neighbours for trade pacts and war.                                                                                               |
| **Defence**   | Edge and corner hexes lose the 4- and 3-approach advantage they have on a hard-edged map — every hex has six approaches.                                         |

**North↔south needs an even row count.** Hex rows alternate their offset, so wrapping the rows only lines up when the count is even; on an odd count the seam would be one-way (you could march across and not back). The Map Editor refuses to export it, the Turn Processor refuses to process it, and the state validator flags it — the flag simply cannot reach a campaign in that state. East↔west has no such limit.

**Running campaigns** can be converted with tools/set_map_wrap.mjs, applied between two turn processings; from the next processed turn the map sails wrapped and its reports carry the flag to every page. Expect the strategic consequences above to land at once on everyone. The tool backs the state file up before writing, and running it again never overwrites that backup — later runs take \_2, \_3…

**2.14.9 Pirate Hunt**

Only a **Pirate** kingdom's fleet can take the **Hunt** stance — a lone fleet, or a link flagship whose whole group is its own. Hunt stays set turn after turn — also on a turn you send no orders, and while the fleet sails — until you choose another stance. Any other fleet that orders Hunt is refused, told why on a card, and sails normally; a stored Hunt that becomes impossible (for example when an ally's fleet joins the group) ends, and a card says why.

**When it attacks.** A hunting fleet attacks when it **sails into** a hex holding a target, when a target **sails into** its hex, or when a target **shares its hex** once movement ends. A target is a fleet of any kingdom that is not at war with you and is not your mutual ally, vassal or liege — a trade pact does not protect it — unless that fleet lies inside **its own port**. When a fleet sails into a hunter's hex, the hunter judges only that fleet's kingdom. A fleet docked as a guest in a Pirate kingdom's port is not in its own port: it can be hunted there, and the hunter fights with its home-port bonus — the Player Page warns when you plan a voyage into one.

**The War Power test.** The hunter compares its side (itself and its link members on the hex) with the target kingdom's side (all that kingdom's fleets on the hex, plus the fleets linked with them that could themselves be hunted — never your own fleet, your ally's, vassal's or liege's, or a realm at war with you: those stay out of the fight and lose nothing — but if the group they sail in is beaten and scatters, their link to that group breaks, as after any naval battle), each fleet at its full battle War Power — roster, status, admiral, crowded decks, seamanship, port — without luck or initiative. It attacks only when its War Power is **strictly higher**. With several target kingdoms on the hex it attacks the strongest one it still out-guns. Two hunting Pirates on one hex: only the stronger attacks; equal, nobody does.

**The battle.** An ordinary naval battle — luck, initiative, casualties, retreat, prize ships and the win/loss opinion all apply — except that no war is declared, nobody pays an aggressor penalty, and only the hunter's side and the target kingdom's side fight; every other fleet on the hex watches. Both kingdoms stay at the relation they had. An army aboard a fleet sunk in a hunt is lost at sea all the same — no war is needed for that. The hunter's card names both War Powers; the victim's card says it is still at peace and may declare war.

**Limits.** One hunt attack per fleet per turn, whatever the outcome. A hunt fought on a hex ends the hunter's move there only if the kill was not clear (§2.14.2): a hunter that sinks or drives off its prey with hulls to spare sails on through its remaining hops, whichever of them sailed in; a prey that beats its hunter clearly sails on too. A fleet that fought any war battle this turn — attacking, defending or in a clash — does not hunt; but a fleet that fought one can still be hunted the same turn (a battered fleet is exactly what a pirate waits for). A hunter only sails into a hex it has room to enter (§2.14.2).

**Status.** A hunting fleet is on station: it loses FLEET_STATUS_HUNT_UPKEEP status every turn and never rests — docked or at anchor, sailing or not — and its link members share it. A long hunt wears the fleet down, and a worn fleet judges fewer targets weaker.

**2.15 Phase 7 — Espionage**

Players submit hire_spy orders specifying a target hex. The TP reads the assigned Spymaster's Politics stat from server state — the stat embedded in the order is ignored — and generates an intelligence report for that hex using final post-Phase-5 army positions.

**Cost**: scales with distance — min(200, 15 + 15 × dist) gold, where dist is the hex-distance from your **nearest owned hex** to the target. Frontier recon is cheap (own/adjacent ≈ 15–30g); deep enemy recon is expensive (up to the 200g cap). \**Limit: 3 spy missions per turn — and only* dispatched *(paid) missions count against it:*\* a mission refused for lack of gold is not dispatched, charges nothing, and frees its slot for the next mission in your orders. Both the cost and the cap are server-authoritative — the Turn Processor recomputes them and ignores any order-embedded value.

**Risk — the agent may not come back.** Every land mission carries a loss chance on the same curve as the cost: min(20%, 5% + 1.5% × dist). On your own doorstep that is 5%; deep recon reaches the 20% ceiling. A lost agent costs you the gold and brings home nothing. The Player Page shows the exact percentage beside the price before you commit.

**Water.** Spies work on land. A mission onto a sea hex is charged in full and returns the same "agent lost" card as any other failure — deliberately so. Under fog you cannot tell water from land before you commit, and if a sea target produced a distinctive answer, a player could map every island and coastline simply by cycling spy coordinates. For the same reason the loss card never names who took your agent: whether he drowned, was caught by a Spymaster (§8.8.5), or vanished on the road, the report reads the same — *"Agent lost at (c,r) — no report recovered."* Naming the captor would confirm who owns the hex and that they run counter-espionage. The **defender** still learns exactly whose agent they caught, and the GM log records every cause in full. **Silence is not evidence.**

**Settlements — walls, never names.** On a hex with a construction the report carries a 🧱 **Fortifications** row: the wall's **current points** (blurred like every other estimate, and further corrupted by counter-espionage) against its **exact maximum** — or *"None — an open settlement"* where the settlement builds no walls (itself telling: Orc low tiers and Generic villages fight unwalled). The report **deliberately never names the settlement's family or level** — no "FNO5". A spymaster brings you numbers; the deduction is yours: the population estimate, the wall maximum and the owner's race narrow the settlement's tier against the full ladders in §3.7.1a, and the wall figure feeds straight into siege-engine arithmetic (§5.8.6).

> ***▶ Example — reading a report on an Imperial metropolis.** A mid-tier spymaster (Politics 60, ±15%) scouts a garrisoned FI20 whose wall has been bombarded down to a true 21,300 of 25,000:*
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
> *The tier is never stated, but it is deducible: Imperial wall maxima at the top of the ladder run 5,000 / 10,000 / 15,000 / 20,000 / **25,000** (FI16–FI20), so the exact maximum plus the owner's race pins this as an **FI20** outright — and ~46,700 people corroborates it, since only FI20 holds 50,000. The current figure is the actionable part: "about 20,000 standing" tells a besieger with a full ten-engine train (2,500 wall damage per turn, §5.8.6) that a breach is roughly eight bombardment turns away — and tells a would-be stormer what fortress bonus the walls still pay. An elite spymaster (Politics \> 75) tightens the estimates to ±5%; at ≤ 50 they smear to ±30%. The maximum stays exact in every case.*

**Report accuracy** depends on the spymaster's Politics stat:

|              |              |                                      |                                                                     |
|--------------|--------------|--------------------------------------|---------------------------------------------------------------------|
| **Politics** | **Variance** | **Site Level Accuracy**              | **Troop Details**                                                   |
| \> 75        | ±5%          | Exact level                          | ~±5%; commander shown (explicit "none" line if unassigned)          |
| \> 50        | ±15%         | ±1 level (estimated)                 | ~±15%; commander **name shown**                                     |
| ≤ 50         | ±30%         | 40% chance to miss the site entirely | ~±30%; 25% chance of a **false phantom sighting** on an *empty* hex |

Variance formula: vary(v) = max(1, round(v × (1 − variance + rand×variance×2))) — e.g. a true count of 100 at ±15% reports somewhere in **85–115**; at ±30%, **70–130**.

> ***Two things this table is easy to misread:** **(1)** the commander's name is visible from **mid tier (Politics \> 50)** up. **(2)** A poor spymaster never hides a real army — only counter-espionage (§8.8.5) or a valid Ambush (§5.4) does; its failure is the opposite, a 25% chance of a **false alarm** on ground that is actually empty ("possible troop movement, unconfirmed"). So distrust a low-Politics sighting on open ground; never distrust a low-Politics silence.*

**Who the report names, and how.** Every foreign army on the hex gets its own row with its real relation to you: 🤝 **Allied Forces** (mutual ally, vassal or liege), 🏳 **Neutral Forces** (not allied and not at war — a trade partner or a stranger) or ⚔ **Enemy Forces** (at war with you); an empty hex reads *"No foreign forces observed"*. Counter-espionage blurs and drops **all** of these rows alike — an ally's army is no easier to read on a guarded hex. Spying on **your own** hex meets no counter-espionage and no Elf-territory penalty: your own Spymaster never works against your own agent. An army in valid **Ambush** is invisible to spies (stance table, §5.4).

The TP ignores state.spies from submitted player files. Spy records are historical reports, not active units on the map. Every hire_spy order is a one-time intelligence request with no persistent presence or upkeep.

**2.16 Phase 8 — Diplomacy**

**2.16.1 Diplomatic Stances**

|            |                                                                                                                                                                                      |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stance** | **Description**                                                                                                                                                                      |
| peace      | Default. No combat, no bonus.                                                                                                                                                        |
| war        | Combat enabled. Auto-declared by military action — army contact, a fleet battle, a port raid, a linked group's attack or defence, and a linked fleet in a biting blockade (§2.14.7). |
| alliance   | Both kingdoms fight as partners; no mutual combat. **Mutual only** — requires independent orders from both sides; one-sided is inert.                                                |
| trade      | Mutual bonus gold. Requires independent orders from both sides.                                                                                                                      |

**2.16.2 Transitions and Conflict Resolution**

All diplomatic orders are evaluated against the **turn-start** stance snapshot — taken before any of the turn's own war declarations (a standing siege or assault, a blockade link, Phase 5 contact, a Phase 6 raid), so none of those can pass for an old war in Phase 8.

**War beats all**: If two kingdoms submit conflicting orders (one war, one peace/alliance/trade), war wins.

**Befriending blocked after a fresh war**: If you went to war with a kingdom *this turn* — through any war begun earlier this turn: a standing siege or assault, a blockade link (Phase 1), Phase 5 combat, or a Phase 6 raid or sea fight — you cannot change your stance toward them (peace, alliance, or trade) in Phase 8 of that same turn. The war stands until next turn. This prevents a one-sided stance where you call it peace/alliance while they remain at war. Pre-existing wars can still be ended normally. A blocked stance change (this rule, or a trade pact refused for lack of a shared border) produces a ⚠ **"Diplomacy blocked"** card in your report — the order is not applied and your report never claims it was.

**Consent-based stances**: **War** is mirrored to the target automatically (war is always forced symmetric). **Trade and alliance are never mirrored** — each requires both kingdoms to set the stance independently. **Peace depends on where you start**: dropping a **mutual** alliance or trade pact to peace remains unilateral and mirrors the other side's stance down with it, but **ending a war is mutual-consent** — a peace order at war is a *proposal*, not a decree (see *Ending a war* below). A one-sided trade or alliance grants no benefits, and **either way you receive a "one-sided pact" notice in your report each turn it stays unreciprocated** (a 🤝 one-sided-alliance card, or a 📦 one-sided-trade card). **The target is notified as well**: each turn a proposal stays open, the proposed-to kingdom receives a 🤝 *"proposes an alliance"* (or 📦 *"seeks a trade pact"*) card telling it to reciprocate in Diplomacy — passive kingdoms included. When the proposal is finally reciprocated, the original proposer receives a *"accepted your alliance"* / *"opened trade with you"* confirmation card. Your own report card for the order reads **"proposed to"** (*"ALLIANCE proposed to"*) until the pact is mutual — only then does it read *forged*/*established* — and the Diplomacy tab shows the alliance as *"Alliance — proposed (awaiting reply)"*, with **⇢ SENT** beside its withdraw button (a one-sided trade pact shows ⇢ SENT too). The other side sees it in Diplomacy as well: the proposer's card carries **⇠ OFFERS ALLIANCE** (or **⇠ OFFERS TRADE**) beside the button that answers it — pressing that button forms the pact, and until the turn is processed the card shows **✓ ACCEPTING**. A trade offer from a kingdom you share no border with is tagged *(no border)*: a trade pact needs one, an alliance does not. Until then it grants no benefits at all (no through-movement, no allied recruiting, no pact bonus), and the Player Page treats a kingdom as a true ally only once the alliance is mutual. **Withdrawing an unanswered proposal is silent**: it is free, it leaves the other kingdom's own stance completely untouched, and it sends them no card at all — nothing was ever formed, so nothing ends. Passive (non-submitting) kingdoms never reciprocate, so they cannot be pulled into an alliance or trade.

**Ending a war — Propose Peace (mutual consent)**: at war, the Diplomacy tab offers 🕊 **Propose Peace** (an alliance or trade pact is ended with the ✕ **End Alliance** and ✕ **End Trade Pact** buttons). A peace order at war flips only **your** stance to peace, as a **standing offer**: the enemy keeps their war stance, and since a pair is at war while *either* side holds war, **the fighting continues unchanged** until they accept. Both sides are carded every turn the offer stays open (🕊 *"peace offered — war continues"* for you, 🕊 *"proposes peace"* for them), and your Diplomacy card is badged *"⚔ War — 🕊 peace offered"*. Peace **forms** when the other side also orders peace (their button reads 🕊 **Accept Peace** while your offer stands) — only then does the war end and the **peace dividend** (+1 to +3 opinion, both sides) pay out — nothing if the war is less than 3 turns old (§2.16.5). **Withdrawing**: re-declaring war while your offer stands simply takes the offer off the table — the war never ended, so it is **not** a new declaration and costs **no** opinion (the button reads ✕ *Withdraw Peace Offer*). **Passive kingdoms auto-accept**: a kingdom that submitted no orders that turn accepts a standing peace offer automatically (with the same dividend, and the same 3-turn rule), so a war against an absent or GM-run kingdom always remains endable.

**2.16.3 Opinion Effects of Diplomacy**

Every diplomatic transition moves opinion as the table in §8.5.3 lists — declaring war, breaking or downgrading a **mutual** alliance, forming peace. A standing peace offer pays nothing until peace forms, and withdrawing it (re-declaring war on an un-accepted offer) costs nothing.

**2.16.4 Vassalage (Phase 8c)**

**Becoming a vassal — the liege must accept**: a become_vassal order is an **offer of fealty**, never a bond by itself. The turn you send it, both realms are carded (🏳 *"Oath of fealty offered"* for you, 🏳 *"X offers fealty"* for the prospective liege) and nothing else changes — no liege, no alliance, no tribute. The liege answers **with its next orders**: the Diplomacy tab shows the oath on your card for that realm, with its tribute rate, and ✓ **Accept** / ✕ **Decline** (a vassal_offer_reply order; clicking the chosen answer again withdraws it). **Accepted** → you are sworn that turn (below). **Declined, or not answered** → the offer lapses, both sides are carded, and nothing changes; you may offer again. A realm that submits no orders never answers, so a passive kingdom cannot be made a liege. An offer awaiting its answer is shown on your own Diplomacy card for that realm. If you send a new oath while one awaits its answer, the waiting one is still answered that turn; your new oath goes out only if the waiting one is not accepted.

**Requirements** — checked when you offer **and again when the liege accepts** (Phase 8c, after every war of the turn): not at war with the prospective liege, so a war order, battle, raid, siege or blockade link between you voids the oath (queuing war on it in the Player Page cancels a queued oath at once and tells you); not already sworn to any kingdom, the prospective liege included; **you hold no vassals of your own** (a fallen vassal does not count) — a realm with vassals cannot swear fealty, so there are never chains of vassals (the Player Page does not offer the oath while you hold any, and disables Accept on an oath from a realm that does); the liege is not your own vassal; the liege is not itself a vassal of another kingdom (its Accept button is disabled); neither realm has fallen; and not your own realm. An oath that fails a requirement is refused with a card to whoever is affected — at acceptance, both realms. **Several acceptances in one turn** are settled one by one in a fixed order (the same every turn, whoever sent orders first), each checked against what the ones before it changed — so when two kingdoms offer fealty to each other, or a chain would form, exactly one oath is sworn and the other is refused with a card. **On the turn an oath is accepted**, a new oath you sent is not sent and a renouncing you sent is not carried out — both are carded; send them again with your next orders. **Accepting an oath makes you a liege**, so an oath of your own that same turn is refused: the Player Page withdraws your queued oath when you accept, and tells you.

On acceptance: both sides automatically set Alliance stance (it lasts until a war between them ends the bond, below); tribute rate set (1–5%, default 3%); tribute paid from vassal's Phase 1 gold income each turn — e.g. 1,000 gold at 3% pays floor(1,000 × 3 / 100) = 30 gold; a vassal that cannot cover it pays only what it has, and the liege is credited exactly that.

**Leaving vassalage**: leave_vassalage order. It resolves before the turn's new oaths, so you may renounce your liege and offer fealty to another in the same orders. You pay tribute **one final time** the turn you renounce — tribute is collected in Phase 1 while you are still a vassal, and the renounce only resolves in Phase 8 — then tribute stops from the next turn. Alliance stance maintained unless explicitly changed. Until you submit, the Diplomacy tab shows the renounce as pending under your liege's name, with ↺ **Undo Renounce**; undoing it also withdraws an oath to a new liege queued after it.

**War ends vassalage**. A war between a liege and its vassal — declared by **either** side, by **any** route: a war order, a battle, a raid, a siege or a blockade link — ends the vassalage **the moment the war begins**, in whatever phase: from then on the two are no longer friends — no port bonus in each other's harbours, no shelter inside each other's walls, no joining each other's defence — the liege's roster drops the vassal, and any army or fleet link between them is released at the end of the turn — though armies of the two camped in the same zone of one hex fight each other first, in that turn's Phase 5 if the war began in Phase 1 (the camp sweep, §2.13; fleets in Phase 6's cohabitation sweep). That turn's tribute is paid only if the war began after Phase 1's income (a war order, a Phase 5 or 6 battle, a raid, a blockade link); a war begun before it — by a standing siege or assault (its tick declares war on every realm inside, §5.6) — stops that turn's tribute too, and both cards say which happened. Both sides are carded — *"Vassalage to X ended — at war"* and *"X is no longer your vassal — at war"* — and the Player Page warns when you queue that war. No realm stays sworn to a liege it is at war with.

**A fallen realm's bond ends**. When a realm falls, every vassalage it is part of ends with it, both ways: a fallen vassal is freed from its liege, and a fallen liege's vassals are freed. Both sides are carded (🏳 *"X has fallen"* / *"Your liege X has fallen"*); from then on no tribute is paid and the two realms are no longer bound in alliance — their diplomacy stays as it stands until either changes it.

**Tribute rate**: Liege may adjust with set_vassal_tribute (clamped 1–5%). New rate applies from next Phase 1. A rate set in the same turn that a war ends the bond does nothing — by Phase 8c the realm is no longer your vassal (the GM log records the refusal; your report carries the "no longer your vassal" card instead).

**2.16.5 Messaging and Ceasefire (Phase 8 — after vassalage)**

Up to 3 messages per turn to any kingdoms. Messages up to 1000 characters. Delivered in the recipient's report.

**Your copy**: your next report keeps a copy of every message you sent — in full under **Sent** in the Messages tab, and as an event card — with what became of it: *delivered*, a broadcast with the number of kingdoms it reached, or *not delivered* when the kingdom you addressed is not in the turn.

**Broadcast to all kingdoms**: instead of choosing one recipient, you may address a message to **All Kingdoms**. It is delivered to every other kingdom — including those at peace, at war, or controlled by the GM/absent (passive) — and **counts as one of your 3 messages**. Recipients see it clearly labelled as a broadcast (📢), so they know it was sent to everyone rather than privately to them. Special commands (\[CEASEFIRE\], \[TRIBUTE\]) do **not** function inside a broadcast — it is a plain announcement only; to propose a ceasefire or send tribute you must message that kingdom directly.

**Ceasefire mechanic**: If both kingdoms at war independently include the token \[CEASEFIRE\] in a message addressed to each other in the same turn, peace is automatically established — provided war was not first declared this same Phase 8 (ceasefire cannot undo a war declared this turn). Opinion gain for both: +(2 + floor(rand×4)) = +2 to +5 — but only if the war has lasted at least 3 turns (TP_PEACE_OPINION_MIN_WAR_TURNS; a war declared on turn 10 pays from a ceasefire on turn 13). A younger war still ends; it just pays no opinion, and the card says why. The same holds for peace formed by mutual orders (§8.5.3).

> ***▶ Example — when a ceasefire pays.** Valdoria declares war on Corvia on turn 10: Valdoria loses 3–6 opinion, Corvia's does not move (§8.5.3).*
>
> *• **Both send \`\[CEASEFIRE\]\` on turn 11** — the war is 1 turn old. Peace returns, neither side gains anything; each card reads "Opinion +0 (the war was only 1 turn old; a ceasefire or peace pays opinion only after 3 turns of war)".*
>
> *• **Both send it on turn 13 instead** — the war is 3 turns old: peace, and each side gains +2 to +5.*
>
> *• **A war begun the same turn** — if Valdoria instead marches onto Corvia's land on turn 10 and both send \[CEASEFIRE\] that same turn, the march-in war is 0 turns old: it ends at once and pays nothing (Valdoria still pays its −3 to −8 for the declaration).*
>
> *• A ceasefire on turn 10 itself is impossible: a war declared in that turn's diplomacy cannot be undone the same turn.*

**2.17 Random Events**

There are no random events: no kingdom draws an event at any point of the turn.

**Dice still decide some fixed rules.** Each applies to every kingdom the same way, has a published range, and its card names the result — none of them is an event:

- population growth, 1–3% a turn (§2.9.1);

- port food (§2.9.4) and farm harvests (§3.6.1), rolled fresh every turn;

- trade and alliance pact income, 0–2% per partner (§2.9.8);

- herd growth, 1–3% a turn (§2.9.9), and Orc reproduction (§2.9.10);

- desertion and starvation when a kingdom cannot pay or feed its troops (§2.10);

- battles and the other rolls of combat (Part V), and spying (§2.15, §8.8).

> ***▶ Example.** "Horse herds grew by 2% (+9) — Your plains breed strong horses this season" is the herd-growth rule (§2.9.9), not an event: every kingdom with two or more horses breeds 1–3% every turn.*

**2.18 Report Generation**

After all phases, the Turn Processor generates one report per kingdom and one GM log.

**Player reports include**: fogged map state (own hexes = full, adjacent/army positions/spy-reported hexes = border, previously seen hexes = remembered — terrain plus the site/construction as last seen, §2.19 — rest = hidden), current resources, armies, fleets, characters, all battle events, income breakdown, diplomacy changes, incoming messages, spy reports. Enemy unit positions are shown on both full and border visibility hexes; foreign army and fleet markers are coloured by your diplomatic stance toward the owner — allied, neutral (peace), or hostile (war). Two concealments apply: an army in valid **Ambush** is never shown to other kingdoms, nor to their spies (§5.4), and **an army embarked aboard a fleet is never shown either — you see the fleet marker, not its cargo** (only an ally whose port the fleet is moored in is told what it carries, §2.14.2). **Your own harbours show more than a marker:** hovering a port you own lists every foreign fleet moored there with its numeral, hulls by type, war-power and commander, whatever your relation to its owner (§2.14.2). A fleet off your coast may be an empty raider or a full invasion force; the map will not tell you which.

Trade/alliance pact income is **itemized per partner** in the Events log — a 📦 card lists each pact partner with the percentage rolled (0–2%) and gold gained that turn — in addition to the single total line shown in the income summary. (The pre-turn "Expected Income" preview shows only an estimated total; the per-partner figures appear once the turn is processed.)

**Turn-log phase order.** Cards in your turn report are ordered by the engine phase that produced them — Recruitment (Pre-Phase 2b) → Sieges & Assaults (Pre-Phase 3) → Income → Upkeep → Market/Build → Ships & Hire → Transfers → Land Combat → Navy → Spies → Diplomacy → Messaging — and each card carries a small phase badge on its right edge (e.g. 🍖 PHASE 2 · Upkeep, 🏇 PHASE 5 · Combat). This lets you read the turn top-to-bottom in the exact order events were resolved.

**War Record**: each kingdom carries a running win–loss tally, shown as ⚔ **War Record (W–L)** in the territory band under your Profile ledger — separate army and fleet records (e.g. 4–1 army · 1–0 fleet). A win or loss is recorded only for a **real army-vs-army or fleet-vs-fleet battle** — field battles, sallies, garrisoned-settlement assaults, amphibious landings against a defending army, and naval battles. Fights against **militia only** (assaulting an ungarrisoned settlement) and **draws** are **not** counted. The tally accumulates across the whole game (it starts at 0–0 and is never reset). The **Rankings** tab includes a **🏆 Total Wins** leaderboard ranking every kingdom by army wins + fleet wins; like all leaderboards it shows standings (your position relative to rivals), not opponents' exact numbers — your own counts are in your Profile.

**2.19 Map Memory**

**How the map shows what you see.** Your own land is drawn in full. Land you can see but do not own — beside your borders, around your armies and fleets, from spy reports — is drawn in a greyed tint of its terrain (plains grey-green, forest dark green). Water you can see is drawn dimmed. Fog — hexes you have never seen — is black on the kingdom map. Hover any hex you can see for its terrain and owner.

**Map memory.** Your kingdom permanently remembers every hex it has ever seen — territory, scouting range, spy reports, and every hex your armies and fleets pass through on the march (each traveled hex and its surroundings). Remembered hexes stay on your map in future turns, drawn faded and hatched: you know the **terrain** and, below, the site and settlement as you last saw them — nothing live. No owners or troops are shown there — an empty remembered hex is NOT confirmed empty; an entire army could be standing on it. Only current vision (your land, your units' surroundings, this turn's spy reports) shows live information. **Your charts also remember what stood there**: the production site and the settlement/fortification *as you last saw them* — drawn muted on remembered hexes on every map and named in the hex tooltip ("last seen: ⚓ Port Lv.II · 🏰 G3"). The memory is refreshed only while a hex is in sight: a port built after you sailed away does not appear, a razed one keeps showing until you look again, and nothing about its owner, population or wall strength is kept. A remembered site is a memory, not intel — the engine never treats it as current (you may plan a landing at a remembered port, and the Turn Processor resolves it against the real map).

**PART III — WORLD & TERRAIN**

**3.1 Terrain Types**

|             |                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Terrain** | **Notes**                                                                                                                                                           |
| Plains      | Standard land. Hosts farms, ports (if adjacent to sea), quarries, and mines (7% prospect, Lv1 cap). Flat +1 food if no site.                                        |
| Hills       | Rugged. Hosts quarries (thin stone rate, §3.6.6) and mines (15%). Barbarian home terrain.                                                                           |
| Mountain    | Rocky. Hosts mines — the best veins (25% find chance, sole Lv3-capable terrain) — and quarries (thin stone rate, same as hills). Dwarf home terrain.                |
| Forest      | Dense. Hosts lumbermills, mines (5%, Lv1 only) and — **for an Elf kingdom only, under an Elven construction** — ports, if adjacent to sea (§3.6). Elf home terrain. |
| Desert      | Arid. Hosts mines (7%). Nomad home terrain.                                                                                                                         |
| Swamp       | Marshy. Hosts no sites at all. Orc home terrain.                                                                                                                    |
| Sea         | Water. Impassable to armies. Fleets only.                                                                                                                           |

**City and Capital are not terrains.** Settlement is a **construction** the GM places on one of the terrains above (§3.7); terrain decides what a hex is *made of*, the construction decides who *lives* there. Terrain carries no population of its own, and Imperial has no home terrain (§3.5).

**3.2 Base Population**

**Terrain carries no population.** A hex's population comes entirely from the **construction** standing on it, set by its family and level (§3.7.1); a hex with no construction has **zero**, permanently. Each construction starts the campaign at its level's full ceiling and grows from there (§3.8).

**3.3 Terrain Income Rules**

|                    |               |               |
|--------------------|---------------|---------------|
| **Terrain**        | **Gold/Turn** | **Food/Turn** |
| Plains (no site)   | —             | +1 food       |
| All other terrains | —             | —             |

**3.4 Terrain in Combat**

**Terrain multipliers** apply in field battle and assault when a race fights on its home terrain (see 3.5). Multipliers do not apply in naval combat or amphibious battle.

**Seizure resistance**: terrain gives neither side a bonus — seizing a hex is a field-style contest against the construction's militia (§2.13.4).

**3.5 Race Terrain Bonuses**

|           |                     |                                                                       |
|-----------|---------------------|-----------------------------------------------------------------------|
| **Race**  | **Home Terrain(s)** | **Combat Multiplier**                                                 |
| Dwarf     | Mountain            | ×1.30                                                                 |
| Elf       | Forest              | ×1.30                                                                 |
| Nomad     | Desert              | ×1.25                                                                 |
| Orc       | Swamp               | ×1.20                                                                 |
| Barbarian | Hills               | ×1.15                                                                 |
| Imperial  | —                   | none                                                                  |
| Aesir     | —                   | none (their bonus is naval: ×1.05 on every fleet-battle roll, §5.9.2) |

Applied to both attacker and defender when fighting on the matching terrain — and only to the matching race: any other kingdom fighting on that terrain type gets no bonus, whoever owns the hex.

> ***▶ Example — why home ground matters.** A non-forest attacker brings 200 WP against an **Elf** defender (forest home, ×1.30) holding a forest hex on Defensive stance (×1.20). The defender's roll builds from 200 × 1.30 × 1.20 = 312 before variance; the attacker builds from 200. To clear the decisive +20% margin (§5.5.2) the attacker needs roughly 312 × 1.2 ≈ 375 effective WP — nearly **double** the raw force. Assaulting an Elf in the woods, or a Dwarf in the mountains (also ×1.30), is a losing proposition without overwhelming numbers, a commander edge, or your own matching terrain to cancel theirs. (If the attacker were also an Elf, both sides would get ×1.30 and it would cancel out.)*

**3.5.1 Cavalry and Terrain**

Mounted units feel the ground under their hooves. In field battles and assaults, the **mounted share** of an army's WP is scaled by the battle hex's terrain:

|             |                                                                                                                                       |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Terrain** | **Cavalry Multiplier**                                                                                                                |
| Plains      | **×1.20** — open charge lanes; cavalry's decisive ground                                                                              |
| Hills       | ×0.90 — charges lose momentum uphill                                                                                                  |
| Forest      | ×0.70 — no formations between the trees (**Warg Riders exempt** — wargs are forest predators, not horses)                             |
| Swamp       | **×0.60** — horses bog and panic; the cavalry graveyard                                                                               |
| Mountain    | ×0.70 — defiles and scree favour infantry absolutely                                                                                  |
| Desert      | ×0.85 — heat and thirst punish outsiders' horses (**all Nomad cavalry exempt** — desert-bred; stacks with the Nomad ×1.25 race bonus) |

Rules of scope:

- Applies **roll-side only**, exactly like the race terrain bonus (§3.5): army WP shown in rankings, siege capacity, and spy estimates stays raw.

- Scales only each army's mounted fraction — a mixed army of 70% foot / 30% horse on swamp loses only 40% of the *mounted* contribution, not of the whole army.

- Both attacker and defender are affected; foot troops and **militia are never scaled**.

- **No modifier** in amphibious landings (the beach ×0.50 regime governs there, §5.7), or in seizure militia contests (terrain-free by design, §3.4).

> ***▶ Example — the charge and the bog.** 100 Equites (WP 19,200, all mounted) attack 200 Swordmasters (WP 20,000, all foot). On **plains** the Equites fight at 23,040 effective and win decisively — the charge pays. The same two forces in a **swamp** put the Equites at 11,520 effective, and the Swordmasters cut them down. Same armies, opposite outcomes; terrain is a weapon.*

**Cavalry against walls.** Storming a fortified settlement replaces the terrain rule for the attacker: every mounted unit in the assaulting army fights at **65%** of its war points — horses (and wargs) are no use on a ladder. This applies whether the walls are held by a garrison or only by the town's militia, and it replaces any terrain bonus (no plains charge into a gatehouse). The defenders' cavalry, sallies, and open-field battles are unaffected, and siege engines are not cavalry.

**3.6 Sites: Farms, Mines, Ports, Forges, Lumbermills, Quarries**

Each hex may have at most one site. Farms, mines, ports, lumbermills and quarries scale income at levels 1–3. Forges are fixed at level 1 and grant army experience rather than income.

**3.6.1 Farms**

- **Terrain**: Plains only

- **Build cost**: 1000g — guaranteed. **The farm does not roll to be built**: pay the fee, get the farm.

- **Income**: floor(pop × rate) food/turn, where rate is **rolled fresh every turn, for each farm separately** — Lv1 **5–25%**, Lv2 **20–50%**, Lv3 **40–80%** of the hex's population. The minimum is always above zero, so a farm never pays nothing while it has people: what you are guaranteed is the bottom of its range, and anything above that is the season. The Player Page counts only that floor in its income figures; the Production tab shows each farm's whole range (🎲 low–high).

- **Upgrade Lv2**: 2000g, 100% chance — guaranteed

- **Upgrade Lv3**: 3000g, 100% chance — guaranteed

> ***▶ The trade the farm makes.** A farm is a certainty to build and a gamble to harvest. The gold you spend is never wasted — 1000g always buys a farm and 5000g always takes it to Lv3 — but what it yields moves from turn to turn. Every upgrade is still a clear gain at both ends of its range (5–25% → 20–50% → 40–80%), so there is no level worth skipping. Plan your food on each farm's **minimum**; the Player Page's income figures count only that, deliberately (its Production tab shows the whole range), and your report tells you what each turn actually rolled.*

**3.6.2 Mines**

- **Terrain & discovery chance**: Mountain 25% · Hills 15% · Desert 7% · Plains 7% · Forest 5% (swamp hexes cannot be prospected)

- **Build cost**: 1000g per attempt — gold spent regardless of outcome

- **Income**: base\[level\] + floor(pop × siteLevel / 20) iron/turn — base Lv1: 10, Lv2: 20, Lv3: 50 (a flat per-level floor, since mountains are low-population); 0 if the hex has no population. E.g. a Lv3 mine on a 300-pop mountain = 50 + floor(900/20) = **95 iron/turn**; at Lv1 = 10 + 15 = **25**

- **Max level by terrain**: Mountain 3 · Hills/Desert 2 · Plains/Forest 1

- **Upgrade Lv2**: 2000g, 30% chance

- **Upgrade Lv3**: 3000g, 50% chance — **Dwarven kingdoms only**; like every site build or upgrade, the hex must carry a construction (§2.11.1); conquest degrades sites one level (§5.6.3), so a captured Lv3 arrives as Lv2 and only a Dwarven conqueror can restore it

Mountains remain the mining crown on every axis: the best find chance, the only Lv3 veins, and the Dwarf home-terrain defence on top. Everywhere else prospecting is a progressively worse gamble — hills are respectable, desert and plains are expensive outlets for mountain-poor kingdoms, forest is a last resort.

> ***⚠ What this means —** Building a mine is a gamble: you pay the full 1000g per attempt with no refund on a miss — expect roughly 4,000g of attempts on a mountain (25%) but up to ~20,000g in forest (5%) before a vein lands. Once a mine exists, deepening it is far easier (Lv1→Lv2 at 30%, Lv2→Lv3 at 50%) — the expensive part is finding the vein, not widening it. On plains, mind the opportunity cost: the same hex could hold a farm.*

**3.6.3 Ports**

> ***A port needs people, not just a harbour.** A port earns from the population of its own hex, and it can only crew a ship from that same population (§2.12.3). If the settlement on the hex is gone — a Nomad camp that moved away (§2.11.10), or a hex the GM painted with a port and no settlement — the harbour still shelters and launches fleets, but it earns nothing and can build nothing.*

- **Terrain**: Plains — **or forest, for an Elf kingdom only** (the Elven exception, §2.11.1) — hex must be adjacent to at least one sea hex

- **Build cost**: 5000g — guaranteed

- **Income/turn**: gold floor(pop × goldMult) — Lv1 ×0.20, Lv2 ×0.40, Lv3 ×0.60, never random — plus food rolled fresh every turn per port (0–5% / 0–10% / 0–15% of population); ports pay in brackets of 5, ranked biggest first. Full rules, floors and what the Player Page shows: §2.9.4.

- **Upgrade Lv2**: 10000g — deterministic (the fee is paid on the attempt, and the attempt always succeeds)

- **Upgrade Lv3**: 15000g — deterministic

- **Race gate**: Orc and Dwarf kingdoms cannot build ports — the order is refused and the 5000g refunded. Elf kingdoms may also build on coastal forest under an Elven construction (§2.11.1).

- A blockaded port produces nothing.

- Port hexes enable ship construction.

**3.6.4 Forge**

- **Race restriction**: Dwarf kingdoms only. Cannot be placed by or transferred to any other race.

- **Placement**: on a hex carrying a **Dwarf (FDW) construction**. Cannot coexist with a Mine.

- **Level**: Always level 1. No upgrades.

- **Not buildable**: Forges are placed by the GM in the Map Editor at campaign start — they cannot be constructed by player orders during a campaign.

- **Effect**: See §5.3.2 — stationary Dwarven armies at a forge hex gain a fixed +2% xp_wp at end of turn.

- **Display**: The forge icon (⚒) appears in the upper-right corner of the hex on the Player Page minimap, identical to port/mine/farm rendering. On the Production tab, the forge card reads "Stationary armies gain +2% XP per turn" in place of an income line.

- **GM note**: If you change a Dwarf kingdom's race to another race in the Map Editor's kingdom panel, all forge sites on that kingdom's hexes are automatically removed when you save.

**3.6.5 Lumbermills**

- **Terrain**: Forest only

- **Build cost**: 1000g — **100%** completion (no gamble)

- **Income**: pop \> 0 ? max(1, floor(pop × mult)) : 0 **wood**/turn — mult Lv1: 0.15, Lv2: 0.45, Lv3: 0.75

- **Upgrade Lv2**: 2000g, **100%** · **Upgrade Lv3**: 3000g, **100%** — max level 3 everywhere

- Cheap, reliable and deterministic — the forest economy is the opposite of mine prospecting. On a forest hex the real decision is lumbermill vs. the 5%-chance Lv1-capped iron mine (one site per hex); for wood, there is no contest.

**3.6.6 Quarries**

- **Terrain**: Plains, Hills or Mountain

- **Build cost**: 1000g — **100%** completion

- **Income**: pop \> 0 ? max(1, floor(pop × mult)) : 0 **stone**/turn — the mult is **terrain-rated**: Plains **0.15 / 0.45 / 0.75** · Hills & Mountain 0.10 / 0.40 / 0.70 *(plains is the richer stone terrain)*; a quarry on any other terrain earns the plains rate

- **Upgrade Lv2**: 2000g, **100%** · **Upgrade Lv3**: 3000g, **100%** — max level 3 everywhere

- On plains a quarry competes with farms, ports and mine prospects for the hex's single site slot; on hills and mountains it competes with mines — guaranteed but thinner stone versus gambled iron is the core trade-off.

Wood and stone are full commodities: they appear in your resource bar, can be bought and sold at the market (base 5g / 7g), sent to other kingdoms, and demanded as tribute. **Wood is consumed by unit recruitment** — every bow, crossbow, gun stock, javelin bundle, shield and axe haft in the game costs wood (see each race's roster table; missile troops are the hungriest at 8–12w, shield-walls 4–8w, plain hafts 2–3w; only the Elven pure-blade elites cost none). **Every ship hull also costs wood** — roughly half its troop capacity in timber (40–130w; see the ship roster tables) — so a fleet program requires a standing timber economy, the market, or captured prizes (prize ships arrive free). **Stone and wood also build walls**: founding, upgrading and repairing a construction spends the family's wall material (the construction family's fabric — wood for Aesir, Nomad and Orc, stone for the rest; Dwarf-family walls cost half, §2.11.7) — see §3.7.2 and §6.11. Siege engines also cost wood (50w each).

**3.7 Constructions**

**City and Capital are not terrain types.** Holding population, minting militia, carrying walls, being besieged and seating a capital are all done by a **construction**: a settlement object the GM places on a hex, belonging to one of eight racial families and standing at a level on that family's ladder.

A hex either carries a construction or it does not. **A hex with no construction has no population at all** — no tax, no militia, no recruiting, and any production site built there yields nothing (§3.6). Bare ground is genuinely empty; all settled life in the world sits inside a construction.

**3.7.1 The Eight Families**

Each race builds in its own idiom. A family fixes three things at every level: the **population ceiling** the settlement grows toward, the **wall** it stands behind, and the **gold cost** to reach that level from the one below.

|            |          |            |            |                      |                |                                                                                                                        |
|------------|----------|------------|------------|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------|
| **Family** | **Code** | **Fabric** | **Levels** | **Population range** | **Wall range** | **Character**                                                                                                          |
| Imperial   | FI       | stone      | 20         | 100 – 50,000         | 500 – 25,000   | The long road: cheap early rungs, then the biggest walls and populations in the world at ruinous cost                  |
| Barbarian  | FBA      | stone      | 20         | 100 – 20,000         | 500 – 6,000    | Wide and shallow — many rungs, modest walls, affordable most of the way                                                |
| Elf        | FLF      | stone      | 10         | 100 – 10,000         | 200 – 8,000    | Few, refined rungs; walls that climb steeply once the settlement matures                                               |
| Dwarf      | FDW      | stone      | 10         | 100 – 10,000         | 1,000 – 18,000 | Densest walls per head in the game, and the cheapest top tier — a Dwarf hold is a fortress first and a town second     |
| Aesir      | FAS      | wood       | 10         | 100 – 10,000         | 500 – 10,000   | Timber walls of 500 up to Lv.3, then matching the population ceiling one-for-one                                       |
| Nomad      | FNO      | wood       | 10         | 100 – 15,000         | 0 – 1,000      | A nomad people: vast settlements of tents behind barely any wall — ten cheap, quick rungs that never become a fortress |
| Orc        | FOR      | wood       | 10         | 1,000 – 50,000       | 0 – 12,000     | Vast, teeming, and **wall-less until Lv.4** — the horde is the defence                                                 |
| Generic    | POP      | stone      | 20         | 100 – 50,000         | 0 – 12,000     | Unaligned villages the GM scatters as neutral ground; **wall-less until Lv.5**                                         |

**Orc starts below its own first rung.** A founded Orc settlement opens at a wall-less **Level 0** tier below Lv.1; every other family, Nomads included, founds straight into Lv.1 (§3.7.4).

**3.7.1a The Full Ladders — every family, every level**

The complete per-level numbers, straight from the Turn Processor's CONSTR_TABLE (which remains the authority if this page and the code ever disagree). **Cost** is the gold paid for that rung — at upgrade time you additionally pay the **wall increment** in the family's building material (wood or stone; a Dwarf-family wall costs half its points in stone, §2.11.7). A wall of — means an open, unwalled settlement. These ladders are also your codebook for espionage: a spy report never names a settlement's tier (§2.15), but its exact wall maximum plus the owner's race reads straight off these tables.

**Imperial (FI — stone)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Lv** | **Population ceiling** | **Wall max** | **Cost (gold)** |
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

**Barbarian (FBA — stone)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Lv** | **Population ceiling** | **Wall max** | **Cost (gold)** |
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

**Elf (FLF — stone)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Lv** | **Population ceiling** | **Wall max** | **Cost (gold)** |
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

**Dwarf (FDW — stone)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Lv** | **Population ceiling** | **Wall max** | **Cost (gold)** |
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

**Aesir (FAS — wood)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Lv** | **Population ceiling** | **Wall max** | **Cost (gold)** |
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

**Nomad (FNO — wood)** *(ten rungs, wooden palisades, no founding tier — Lv.1 is the settler camp.)*

|                                           |                        |              |                 |
|-------------------------------------------|------------------------|--------------|-----------------|
| **Lv**                                    | **Population ceiling** | **Wall max** | **Cost (gold)** |
| 1 *(settler camp — what founding plants)* | 100                    | 0            | 0               |
| 2                                         | 500                    | 100          | 500             |
| 3                                         | 1,000                  | 200          | 750             |
| 4                                         | 1,500                  | 300          | 1,500           |
| 5                                         | 2,000                  | 400          | 2,000           |
| 6                                         | 3,000                  | 500          | 4,000           |
| 7                                         | 4,000                  | 600          | 7,000           |
| 8                                         | 6,000                  | 700          | 12,000          |
| 9                                         | 10,000                 | 800          | 20,000          |
| 10                                        | 15,000                 | 1,000        | 30,000          |

A Nomad wall never exceeds 1,000 points, so the fortress bonus (§5.6.1) tops out near ×1.6; a single siege engine hit (250 points) flattens a Lv.2 or Lv.3 palisade, and two hits flatten any wall up to Lv.6. That is the design: Nomads hold ground with people and riders, not walls. Wood, not stone, is the fabric — and desert hexes host neither quarries nor lumbermills, so timber comes from a forest hex or the market (base 5g).

**Orc (FOR — wood)**

|                                                                          |                        |              |                 |
|--------------------------------------------------------------------------|------------------------|--------------|-----------------|
| **Lv**                                                                   | **Population ceiling** | **Wall max** | **Cost (gold)** |
| 0 *(founding tier, §3.7.4 — only reached by founding, never by upgrade)* | 100                    | —            | —               |
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

**Generic (POP — stone)**

|        |                        |              |                 |
|--------|------------------------|--------------|-----------------|
| **Lv** | **Population ceiling** | **Wall max** | **Cost (gold)** |
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

The Player Page shows the current and next rung for every construction you own.

**Generic (POP) is the universal ladder.** It belongs to no race, and — uniquely — **any owner may upgrade it** (§2.11.7). Every other family answers only to its own people.

**3.7.2 The Wall**

A construction's wall has a **maximum** (set by its family and level) and a **current** value, the wall's *integrity*. A fresh construction stands at full integrity. Siege engines knock it down (§5.8.6); the repair_wall order builds it back (§2.11.8).

Integrity is not cosmetic — it scales the defender's fortress bonus continuously (§5.6.1). A settlement whose wall has been beaten to zero is **breached**, and fights as though it had no walls at all.

Families whose low levels list a wall of **0** (Orc Level 0–3, Generic Lv.1–4, Nomad Lv.1) have no wall to damage, no fortress bonus, and nothing to repair. They are open settlements.

**3.7.3 The Capital**

The capital is not a terrain type and not "the biggest settlement" — it is a **specific hex the GM designates** when building the map. That designation becomes the kingdom's **muster seat**: where a capital-based army musters, and the hex the profile banner calls your Capital.

A **Nomad** seat also travels when the camp it stands on moves (§2.11.10). If the designated seat is lost, it succeeds by the sticky ladder of **§2.13.10**, which also sets the seat's defensive perks (+0.10 fortress bonus, 6 pressed turns of siege instead of 5). On the Player Page the seat is marked with a **gold ★** (black-bordered) on all three maps — the kingdom map, the Army map and the Navy map — for **every seat you can see**, your own at full strength and foreign ones dimmed with the border-vision tint (seat locations are public to border vision). The star ignores the map-layer toggles: like fog, the capital marker always draws.

**3.7.4 Founding a New Construction**

The GM is not the only one who can put a settlement on the map. Once at least one construction exists anywhere, any kingdom may found new ones of its own on bare ground it holds — the full order is §2.11.9. This section covers what founding means for the family ladders above.

**A permanent choice.** Founding plants a settlement of one family — your own race's, or the neutral **Generic** ladder — and that family never changes afterward. Conquest can degrade a construction's level (§5.6.3) or lock it against your own upgrades if you did not build it (§2.11.7), but nothing ever moves it onto a different family's ladder.

**Where the settlers come from, and where they cannot go.** Founding moves 100 people out of your muster seat — never onto the seat itself — and never shrinks a hex (§2.11.9). To put a construction on a bare seat hex you must first lose the seat or move it — in practice, upgrade a different holding until succession moves the seat, or capture ground worth settling.

**One family starts below Level 1.** Orc settlements hold 1,000 population at their first table rung — starting a fresh founding there would open at a tenth of capacity. They instead found at a **Level 0** tier kept off the family ladder above (§3.7.1a): 100 population, no wall, reached only by founding — never by upgrading, and never painted by the GM. Every other family founds directly at Level 1.

Raising Level 0 to Level 1 is an ordinary upgrade (§2.11.7) with ordinary prices, read off the family's own ladder: population must first reach the Level 0 ceiling of **100**, then it costs the listed **Lv.1 gold price — 250g for Orc** — plus the wall the new level introduces. *(Nomads have no Level 0: FNO1 is the settler rung and FNO1 → FNO2 is an ordinary 500g + 100 wood upgrade.)* Since Level 0 has no wall, that increment is the whole Lv.1 wall: **nothing at all for Orc** (FOR1 is wall-less too). Note what the upgrade buys an Orc: the population ceiling jumps from 100 straight to 1,000.

**The founding turn is a fortification holiday.** A construction founded this turn fights as open ground until the next turn, though its wall is real from the start (§2.11.9).

**3.8 Population Mechanics**

Population lives **only inside constructions**. Each turn, a construction below its level's ceiling grows by:

growth = max(1, round(rate × ceiling)) rate = 1–3%, rolled per hex per turn

population = min(ceiling, population + growth)

rate is 0.01 + rand×0.02, so growth is 1–3% of the ceiling, never less than 1. The **population ceiling** is set by the hex's **construction level**, not by terrain (§3.7.1), and runs from 100 (a first-rung Imperial, Barbarian, Elf, Dwarf, Aesir or Generic holding, or an Orc Level 0 camp or a Nomad Lv.1 camp) to 50,000 (a maxed Imperial, Orc or Generic one). At campaign start the GM paints every construction in the Map Editor and each begins at its level's **full ceiling**. A construction hex drained to 0 grows back from 0 by the same rule — it is never snapped back to the ceiling.

Two consequences worth internalising:

- Growth is measured against the **ceiling of the level you have paid for**, not against current population, so a settlement grows at a steady absolute pace until it saturates (a 50,000-ceiling city can add up to +1,500 a turn). A large settlement one rung up the ladder grows in bigger absolute steps than a small one — levelling up accelerates you, and standing still stalls you at the ceiling.

- Growth **saturates and stops** at the ceiling; it never overshoots on its own. Population *above* the ceiling (which conquest degradation can leave behind, §5.6.3) is left exactly where it is — never clamped down, never grown.

- A **moved Nomad camp** takes its people and its ceiling with it, and leaves its old hex at zero (§2.11.10).

- At Opinion 40 or below no settlement grows and each loses people instead (emigration, §2.9.1).

> ***⚠ The consequence that bites hardest.** Because growth stops dead at the ceiling, a muster seat whose level holds fewer than 300 people can **never** send out settlers until the seat itself is upgraded (§2.11.9).*

**Bare hexes never grow, because they never had population to begin with.** (A legacy map with no construction at all still runs the old terrain path: terrain base population is seeded only when a hex has **no** population field; a hex **drained to 0** is never re-seeded and grows back by max(1, floor(pop × rate)) → 1, then 1–3%.)

Population drives:

- Tax income: floor(totalPop × taxRate / 100) gold (§2.9.5)

- Site output — farm food, port gold and food, mine iron, lumbermill wood, quarry stone (§3.6.1–§3.6.6; ports §2.9.4)

- Militia strength: floor(pop × 0.05) militia units (5% of population) at 20 WP each

- Spy report estimates

- The **upgrade gate**: a construction may only level up once its population has reached its current ceiling (§2.11.7)

Every site yields **0 if the hex population is 0** — which, in this era, means every site on a bare hex produces nothing at all. On a *populated* hex a site yields **at least 1**, except a port's rolled food, which can roll 0% and pay nothing (§2.9.4).

Population is also spent on recruits (Pre-Phase 2b, before growth) and ship crews (Phase 4, after growth) — never on siege engines (§2.12.1, §2.12.3).

> ***▶ Example — when the ceiling cuts the growth.** A realm's capital holds 6,866 people under a 7,000 ceiling; every other settlement is already full. This turn the capital grows 1–3% of its **ceiling** — 70 to 210 people — but only 134 more fit, so the gain is 70 to 134. The Profile says exactly that: 18,866 (+70–134 /turn) · only (60,65) has room to grow — 134 more people · 9 settlements are full: upgrade them to grow. Next turn the capital is full too, and the realm stops growing until a settlement is upgraded to a level with a higher ceiling.*

**PART IV — RACES**

**4.1 Race Overview and Asymmetry**

|           |                  |                   |                                                                |
|-----------|------------------|-------------------|----------------------------------------------------------------|
| **Race**  | **Home Terrain** | **Terrain Bonus** | **Special Mechanic**                                           |
| Imperial  | — (none)         | —                 | None                                                           |
| Barbarian | Hills            | ×1.15             | None                                                           |
| Elf       | Forest           | ×1.30             | None                                                           |
| Orc       | Swamp            | ×1.20             | Foot reproduction (swamp only); severe starvation              |
| Dwarf     | Mountain         | ×1.30             | Iron-dependent across all units                                |
| Aesir     | — (none)         | —                 | ×1.05 fleet-battle bonus (§5.9.2); the game's only 120-MP hull |
| Nomad     | Desert           | ×1.25             | Desert crossed at 30 MP where all others pay 60 (§2.13.2)      |

**4.2 Imperial**

**No terrain bonus — the Legion holds its walls instead.** The bonus is keyed on **constructions, ownership and role**, not terrain. An Imperial kingdom **defending a hex it owns** whose construction is of the Imperial family (FI) or the POP lineage rolls at **×1.10** — garrison under assault, sally, field battle on that hex and beach defence alike, and the hex's militia ride the same multiplier. It never applies as attacker — except on an ordered sally from its own walls (§2.13.7) — never on a hex the Imperial does not own at the moment of battle, never on another family's settlement (a captured Orc camp earns nothing), and never for an ally defending beside it (the bonus is per army). It stacks multiplicatively with stance, terrain and the fortress bonus, and like every terrain bonus it is roll-side only: rankings, spy estimates and the siege capacity gate never see it. On open ground the Imperial still fights bonus-less, like the Aesir. The battle card's ledger shows it as the legion row.

**Unit Roster:**

|                       |         |         |        |                        |            |        |             |
|-----------------------|---------|---------|--------|------------------------|------------|--------|-------------|
| **Unit**              | **ATK** | **DEF** | **HP** | **Cost**               | **Upkeep** | **WP** | **Mounted** |
| Velites               | 5       | 5       | 8      | 50g, 8f, 6w            | —          | 43     | No          |
| Legionnaire           | 7       | 9       | 11     | 60g, 1i, 8f, 5w        | —          | 67     | No          |
| Sagitarii             | 9       | 5       | 9      | 150g, 20i, 5f, 1h, 10w | 4g         | 121    | Yes         |
| Equites               | 11      | 7       | 13     | 200g, 40i, 1h, 3w      | 8g         | 192    | Yes         |
| Praetorians           | 10      | 10      | 16     | 300g, 100i, 10f, 5w    | 12g        | 356    | No          |
| Onager (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w         | 3g         | 10     | No          |

**Ship Roster:**

|          |         |         |              |                 |            |        |        |
|----------|---------|---------|--------------|-----------------|------------|--------|--------|
| **Ship** | **ATK** | **DEF** | **Capacity** | **Cost**        | **Upkeep** | **WP** | **MP** |
| Drommund | 6       | 5       | 100          | 155g, 9i, 50w   | 4g         | 66     | 90     |
| Cog      | 10      | 8       | 200          | 310g, 24i, 90w  | 8g         | 108    | 60     |
| Galley   | 12      | 11      | 300          | 550g, 36i, 130w | 15g        | 138    | 60     |

**4.3 Barbarian**

Cheapest recruitable infantry of any race. Raiders and Berserkers cost 40–50g with no gold or iron upkeep — they still eat headcount food (§2.10.4). High ATK ceiling; moderate DEF. Storm Horses costs 120g (plus 1 horse, like all mounted units except the Orc Warg Rider) — cheaper than every other cavalry except the Nomad Bedouin (90g) and the Orc Warg Rider (100g).

**Unit Roster:**

|                              |         |         |        |                     |            |        |             |
|------------------------------|---------|---------|--------|---------------------|------------|--------|-------------|
| **Unit**                     | **ATK** | **DEF** | **HP** | **Cost**            | **Upkeep** | **WP** | **Mounted** |
| Raiders                      | 7       | 4       | 10     | 50g, 15f, 4w        | —          | 48     | No          |
| Berserker                    | 8       | 5       | 12     | 40g, 10f, 2w        | —          | 55     | No          |
| Wild Archer                  | 10      | 8       | 13     | 220g, 12i, 20f, 12w | 5g         | 120    | No          |
| Storm Horses                 | 13      | 7       | 13     | 120g, 8f, 1h, 3w    | 4g         | 85     | Yes         |
| Warchief                     | 15      | 10      | 18     | 350g, 20i, 30f, 4w  | —          | 179    | No          |
| Stone-Thrower (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w      | 3g         | 10     | No          |

**Ship Roster:**

|          |         |         |              |                      |            |        |        |
|----------|---------|---------|--------------|----------------------|------------|--------|--------|
| **Ship** | **ATK** | **DEF** | **Capacity** | **Cost**             | **Upkeep** | **WP** | **MP** |
| Wolfship | 8       | 4       | 80           | 135g, 8i, 10f, 45w   | 3g         | 72     | 90     |
| Reaver   | 11      | 5       | 120          | 245g, 13i, 15f, 65w  | 5g         | 96     | 90     |
| Tigress  | 14      | 7       | 200          | 435g, 22i, 25f, 100w | 14g        | 126    | 60     |

*(The Barbarian hull is the Wolfship; "Longship" is an Aesir hull, §4.7.)*

**4.3.1 Pirate — Barbarian subset**

**Pirate is not a full race** — it is a flavour *subset* of Barbarian, set per kingdom in the Map Editor (race picker → Pirate; stored as race:'Barbarian' plus a pirate:true flag). A Pirate kingdom plays exactly like a Barbarian kingdom — same unit and ship rosters, costs, food, terrain bonuses, and the same ambush exclusion — with only these differences (and one Pirate-only fleet stance, Hunt):

- **Naval battle bonus ×1.10** — pirate fleets multiply their fleet-battle WP by 1.10. Fleet battles only: no effect on amphibious landings, blockades, raids, movement, or land combat.

- **Own heraldry & look** — pirate shields (shield-pirate-N, own numbering pool), logo, and battle art (missing pirate art falls back to Barbarian art); a pirate UI palette (weathered sea-chart in light theme, tar-black skull-and-bones in dark); and pirate force names — armies muster as **CREW**, fleets as **FLOTILLA**.

- **Own titles** — Haven of / Brotherhood of / Cove of / Crew of (independent / liege / vassal / vassal-of-a-vassal).

- **Label** — the UI shows the race as **Pirate** wherever it would say Barbarian.

- **Hunt stance** — only Pirate fleets can take Hunt: a hunting fleet attacks a fleet it meets and judges weaker, and no war is declared (§2.14.9).

**4.4 Elf**

Elite, expensive, iron-dependent. **The Swordmaster carries no gold upkeep** — upkeep parity: every race has an upkeep-free line unit. Only Swordmasters/Bladedancers cost food to recruit, but Elf armies still eat headcount food and starve without it (§2.10.4). All Elf ships are gold-only upkeep.

**Unit Roster:**

|                               |         |         |        |                   |            |        |             |
|-------------------------------|---------|---------|--------|-------------------|------------|--------|-------------|
| **Unit**                      | **ATK** | **DEF** | **HP** | **Cost**          | **Upkeep** | **WP** | **Mounted** |
| Swordmaster                   | 11      | 6       | 9      | 100g, 14i, 5f     | —          | 100    | No          |
| Bladedancer                   | 12      | 7       | 11     | 160g, 25i, 5f     | 6g         | 139    | No          |
| Ranger                        | 9       | 11      | 12     | 220g, 37i, 12w    | 8g         | 174    | No          |
| Elven Cavalry                 | 12      | 13      | 22     | 300g, 55i, 1h, 3w | 10g        | 247    | Yes         |
| High Guard                    | 15      | 12      | 18     | 400g, 104i, 3w    | 14g        | 362    | No          |
| Great Ballista (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w    | 3g         | 10     | No          |

**Ship Roster:**

|            |         |         |              |                |            |        |        |
|------------|---------|---------|--------------|----------------|------------|--------|--------|
| **Ship**   | **ATK** | **DEF** | **Capacity** | **Cost**       | **Upkeep** | **WP** | **MP** |
| Moonskiff  | 7       | 6       | 60           | 170g, 4i, 40w  | 5g         | 78     | 90     |
| White Ship | 10      | 9       | 100          | 295g, 7i, 60w  | 8g         | 114    | 90     |
| Swan Ship  | 16      | 8       | 150          | 545g, 13i, 85w | 16g        | 144    | 60     |

**Harbours among the trees.** Elves alone may build a **port on a coastal forest hex**, as well as on coastal plains — but only where the hex's construction is Elven (§2.11.1). **The hex stays forest**, so your ×1.30 home-terrain bonus defends that harbour on land — an Elven port is the best-defended port in the world, and the only one whose ground fights for it.

**4.5 Orc**

Foot soldiers reproduce passively (5–7% per army per turn if foot ≥ 10 **and the army stands on a swamp hex**, §2.9.10), and the breeding that carries your total foot past 300 / 500 / 1000 is broadcast to every rival. Starvation is disproportionately severe (10–20% vs 3–10%). Orc units carry little or no gold upkeep, but headcount food (§2.10.4), food-heavy recruitment and reproduction make food the central constraint.

> ***⚠ What this means — feed the horde or watch it rot.** An Orc can field-grow an army that never needed full paid recruitment, but a growing horde eats more every single turn — build farms and stockpile food ahead of the growth curve, or starvation will erase the soldiers reproduction just handed you.*

**Unit Roster:**

|                             |         |         |        |                |            |        |             |
|-----------------------------|---------|---------|--------|----------------|------------|--------|-------------|
| **Unit**                    | **ATK** | **DEF** | **HP** | **Cost**       | **Upkeep** | **WP** | **Mounted** |
| Goblin                      | 8       | 5       | 9      | 30g, 12f, 2w   | —          | 51     | No          |
| Orc                         | 13      | 6       | 15     | 150g, 20f, 3w  | 3g         | 88     | No          |
| Orc Archer                  | 11      | 10      | 20     | 200g, 25f, 10w | —          | 104    | No          |
| Warg Rider                  | 7       | 4       | 8      | 100g, 10f, 2w  | 4g         | 51     | Yes         |
| Uruk-Hai                    | 12      | 5       | 11     | 180g, 18f, 4w  | —          | 80     | No          |
| War Catapult (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w | 3g         | 10     | No          |

**Fleet capability**: Orc kingdoms cannot build or commission fleets.

**4.6 Dwarf**

Iron-first. All units require iron for production; several require iron upkeep. Dwarves still eat headcount food and starve like any race without it (§2.10.4). Thunderers have the highest ATK of any unit in the game (16). Dwarves in mountain terrain are a defensive fortress. Only Dwarven engineers can sink a Level 3 mine shaft (§3.6.2) — every deepest vein in the world is Dwarven-dug, and captured Dwarf mines are prized conquests.

**The Ironclad carries no gold upkeep** — upkeep parity: every race has an upkeep-free line unit.

**Unit Roster:**

|                          |         |         |        |                |            |        |             |
|--------------------------|---------|---------|--------|----------------|------------|--------|-------------|
| **Unit**                 | **ATK** | **DEF** | **HP** | **Cost**       | **Upkeep** | **WP** | **Mounted** |
| Warrior                  | 7       | 12      | 14     | 100g, 15i, 3w  | 3g, 1i     | 118    | No          |
| Ironclad                 | 11      | 6       | 8      | 90g, 10i, 2w   | —          | 93     | No          |
| Crossbowman              | 6       | 8       | 10     | 150g, 20i, 10w | 5g         | 117    | No          |
| Thunderers               | 16      | 5       | 8      | 320g, 70i, 8w  | 10g, 3i    | 278    | No          |
| Heartguard               | 12      | 12      | 16     | 240g, 50i, 3w  | 6g, 2i     | 237    | No          |
| Trebuchet (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w | 3g         | 10     | No          |

**Fleet capability**: Dwarf kingdoms cannot build or commission fleets.

**Forge**: placed by the GM at campaign start on a Dwarf (FDW) construction; a stationary army there gains +2% xp_wp a turn (§3.6.4, §5.3.2).

**4.7 Aesir**

Sea-raiders of the frozen fjords. The Aesir field an **all-foot** army — no mounted units and **no horse dependence anywhere in the race** — with a mid-cost roster whose top end (Jarl's Guard, WP 240) sits between Barbarian and Dwarf. On land they are deliberately plain: **no home-terrain bonus and standard movement costs**. Their entire edge is the sea: a **×1.05 fleet-battle bonus** on every naval roll (§5.9.2), the game's **only 120-MP hull** (an all-Snekkja fleet sails **4 sea hexes** per turn — the fastest thing afloat), and the Busse's capacity-220 hold for landing a full war-band. Play them as raiders: strike from the water, and remember the universal ×0.50 beach penalty (§5.7) still applies when you land.

**Unit Roster:**

|                           |         |         |        |                    |            |        |             |
|---------------------------|---------|---------|--------|--------------------|------------|--------|-------------|
| **Unit**                  | **ATK** | **DEF** | **HP** | **Cost**           | **Upkeep** | **WP** | **Mounted** |
| Shore Raider              | 7       | 4       | 10     | 42g, 15f, 5w       | —          | 48     | No          |
| Axe Thane                 | 9       | 6       | 12     | 76g, 3i, 15f, 3w   | 2g         | 75     | No          |
| Shield-Karl               | 7       | 10      | 13     | 119g, 16i, 8w      | 4g         | 110    | No          |
| Huscarl                   | 12      | 9       | 15     | 204g, 20i, 20f, 6w | 6g         | 170    | No          |
| Jarl's Guard              | 14      | 11      | 17     | 289g, 32i, 30f, 6w | 10g        | 240    | No          |
| Valslöngva (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w     | 3g         | 10     | No          |

**Ship Roster:**

|          |         |         |              |                      |            |        |         |
|----------|---------|---------|--------------|----------------------|------------|--------|---------|
| **Ship** | **ATK** | **DEF** | **Capacity** | **Cost**             | **Upkeep** | **WP** | **MP**  |
| Snekkja  | 8       | 4       | 80           | 120g, 9i, 10f, 45w   | 3g         | 72     | **120** |
| Longship | 12      | 6       | 140          | 300g, 20i, 20f, 75w  | 8g         | 112    | 90      |
| Busse    | 14      | 9       | 220          | 490g, 31i, 30f, 105w | 14g        | 136    | 60      |

**Naval bonus**: every Aesir fleet multiplies its battle roll by **×1.05** — attacker or defender, sea or port (§5.9.2). It is roll-only: displayed fleet WP, upkeep and rankings are unaffected.

**4.8 Nomad**

> ***Desert riders eat like footmen.** A Nomad **mounted** unit consumes **1 food per head**, not the 2 every other race's cavalry pays. Two of the six Nomad units ride — the Bedouin and the Askari — and they carry the lowest war-points per head of any cavalry in the game, so the standard mounted surcharge charged them double rations on the very troops that already needed the most bodies. Riders who live off the land is the same logic that grants the 1.25 desert bonus.*
>
> ***The camps move.** One FNO camp a turn may strike its tents and re-pitch up to 2 hexes away on your own land, for 1,000g, resting 6 turns between moves — people and palisade travel, sites stay behind and fall idle. No other people can do this. Full rules in §2.11.10.*

The desert Sultanate — swift riders and patient traders in the Ayyubid mould. The cheapest army in the game: the Rajjala costs 20g (plus 2 wood for its spear) and is pitched **deliberately just above militia** (WP 26 vs the militia's 20 per head), and the roster's ceiling (Askari, WP 143) is the lowest of any race. Nomad win by attrition economics and by owning the sand: **desert ×1.25 in battle** and **desert crossed at 30 MP** where every other race pays 60 — a Nomad foot army makes 2 desert hexes per turn, an all-mounted Bedouin/Askari force makes 3, while invaders crawl through at 1. The sand also hides ore: desert hexes can be prospected for mines (7% chance, Lv2 cap — §3.6.2), turning otherwise dead dunes into a modest iron income no rival will bother marching through desert to take. Their navy is a modest utility fleet: the Dhow ferries troops cheaply, and the Harraqa fire-ship stings far above its tonnage but cannot take a hit.

**Unit Roster:**

|                         |         |         |        |                   |            |        |             |
|-------------------------|---------|---------|--------|-------------------|------------|--------|-------------|
| **Unit**                | **ATK** | **DEF** | **HP** | **Cost**          | **Upkeep** | **WP** | **Mounted** |
| Rajjala                 | 4       | 3       | 6      | 20g, 8f, 2w       | —          | 26     | No          |
| Naffatun                | 7       | 4       | 8      | 40g, 10f, 5w      | —          | 50     | No          |
| Rumat                   | 9       | 5       | 9      | 90g, 5i, 15f, 10w | 2g         | 86     | No          |
| Bedouin                 | 10      | 5       | 10     | 90g, 8f, 1h, 6w   | 3g         | 88     | Yes         |
| Askari                  | 11      | 8       | 12     | 180g, 10f, 1h, 4w | 5g         | 143    | Yes         |
| Mangonel (siege engine) | 1       | 1       | 8      | 250g, 10i, 50w    | 3g         | 10     | No          |

**Ship Roster:**

|          |         |         |              |                   |            |        |        |
|----------|---------|---------|--------------|-------------------|------------|--------|--------|
| **Ship** | **ATK** | **DEF** | **Capacity** | **Cost**          | **Upkeep** | **WP** | **MP** |
| Dhow     | 6       | 4       | 100          | 145g, 2i, 5f, 50w | 3g         | 56     | 90     |
| Shini    | 10      | 6       | 140          | 300g, 10i, 70w    | 6g         | 98     | 60     |
| Harraqa  | 13      | 5       | 60           | 360g, 5i, 45w     | 10g        | 116    | 60     |

> ***▶ GM map-design note (both new races).** An Aesir kingdom **must** be given coastal port hexes at map creation or its entire racial identity (navy, raiding, the 120-MP hull) is unreachable — the inverse of the "no ports for Orc/Dwarf" rule. (An Elf realm needs less care: a forest coastline is enough, provided its coastal forest hexes carry Elven constructions — paint them with the Elf family, §2.11.1.) It also appreciates a **forest** hex or two: every hull costs timber, and a forestless Aesir fleet lives off the market, tribute and raiding (thematic, but deliberate hardship). A Nomad kingdom should hold or border **desert** hexes for the same reason.*

**PART V — UNITS & COMBAT**

**5.1 Reading a Unit Stat Block**

|           |                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------|
| **Field** | **Meaning**                                                                                                |
| ATK       | Attack power — reference value; WP is the combat value                                                     |
| DEF       | Defence power — reference value                                                                            |
| HP        | Hit Points — reference value                                                                               |
| Cost      | Resources to recruit one unit (g=gold, f=food, i=iron, h=horses, w=wood)                                   |
| Upkeep    | Resources per unit per turn (Phase 2)                                                                      |
| WP        | Base War Points — the actual combat value used in all rolls                                                |
| Mounted   | Yes/No — mounted units consume 2 food/turn (foot units 1); **Nomad** mounted units eat 1, like foot (§4.8) |

**5.2 War Points: The Combat Currency**

**War Points (WP)** are the sole combat value in all rolls. ATK, DEF, HP are reference values.

Army total WP: armyWP = sum of (unit.xp_wp × unit.count) across all stacks

unit.xp_wp starts at base WP and increases with combat experience.

> ***▶ Example — reading army strength.** An army of 40 Legionnaires (base WP 67) and 10 Equites (base WP 192), none yet experienced, totals armyWP = 40×67 + 10×192 = 2,680 + 1,920 = 4,600 WP. After several battles raise the Legionnaires to xp_wp 74, the same stacks total 40×74 + 10×192 = 4,880 WP — with no new recruits. War Points, not headcount, decide the math: a smaller veteran force can out-roll a larger green one.*

**5.3 Experience (xp_wp)**

**5.3.1 XP Gain from Battle**

After any battle (field, amphibious, assault, or naval), all surviving units gain experience:

- Roll: 1 + (0.03 + rand×0.02) × oppFactor — up to ×1.03 to ×1.05

- **\`oppFactor = min(1, opponent WP / your WP)\`** — experience scales with how dangerous the enemy actually was. Fighting an equal or stronger force grants the full roll; **crushing a token force teaches nothing** (against an enemy a fraction of your strength the gain rounds to zero). For an assault, the attacker's "opponent" is the full defence — garrison, militia and fortress together — so storming a real city always instructs. **The defending garrison is measured against that same full defence as its own "your WP"** — the walls it stands behind and the militia fighting beside it count as its strength, not just its own troops. Both sides of an assault therefore read the same two quantities, inverted, exactly as they already did in a field battle. The harder the walls and the larger the population, the less experience the garrison earns.

- new_xp_wp = min(cap, round(xp_wp × roll))

- Both sides gain experience regardless of outcome — the outmatched side, fighting up, always earns its full roll

**Fleets earn it the same way (§5.9).** After every naval battle — won, lost or drawn — each surviving **hull stack** of every fleet that fought rolls the same 1 + (0.03 + rand×0.02) × oppFactor, one roll per fleet applied to all its stacks, capped at 3 × base WP. Five things are specific to the sea:

- **\`oppFactor\` is side-wide.** In a coalition fight your fleet measures the *whole* opposing side against the *whole* of yours (the sums that decided the roll), so two fleets fighting as one squadron earn the same roll — neither is "the small one".

- **Prize hulls arrive green and then learn.** A captured ship joins you at its base WP whatever its old crew knew (§2.13.12), and from its next battle it rolls XP like any hull of yours — the cap is 3× its **own true base**, so a foreign hull is never worth more than the same hull built at home.

- **Veterancy is armour as well as power.** A hull's XP raises its war power *and* its price-equivalent in the casualty formula (§5.9.3: price × (1 + xp_wp/base − 1)), so veteran ships both hit harder and sink less often — the same double effect infantry gets on land.

- **Status is untouched.** Experience never restores readiness; a fleet at 40% after a hard fight is a veteran fleet at 40% (§5.10.6).

- **The card says so.** Your report carries a *"Battle XP — Fleet N sailors hardened at sea"* line naming each hull type's old and new WP, and the Readiness Report is separate.

Admirals gain **character** experience from the same battles on the land rule — one Military point per three battles commanded, draws included (§7.10).

> ***▶ Why the opponent scaling exists.** Without it, two colluding kingdoms could farm veterancy: one feeds throwaway single-unit armies into the other's host, each "battle" granting the full +3–5%. Under the scaling, a token sacrifice is worth exactly nothing — experience only flows from fights that were real.*

**5.3.2 XP Gain from Forge (Dwarf only)**

At the end of each turn, before Character Experience (then report generation), the Turn Processor applies a forge bonus to eligible Dwarven armies:

- **Eligible**: Dwarf kingdom, army not destroyed, army has at least one living unit, army not embarked on a fleet, **no \`move_army\` order submitted this turn**, army's current hex has a Forge site **and a Dwarf-family (FDW) construction**, and that hex is owned by the same kingdom.

- Rate: **+2%** (fixed) applied multiplicatively to all living unit stacks

- new_xp_wp = min(cap, round(xp_wp × roll))

- One roll per army, same multiplier applied to all unit types in that army

- Cap: same as battle XP — baseWP × 3

The stationary requirement is based on **submitted orders**, not outcome. An army with a move order that gets blocked mid-path does not receive forge XP, because the player intended to move it.

**5.3.3 XP Cap**

cap = baseWP × 3. A unit cannot exceed three times its base War Points.

**5.3.4 XP Blending on Recruitment**

xp_wp_new = round( (oldWP × existingCount + baseWP × newCount) / totalCount )

Raw recruits dilute veteran stacks proportionally.

**5.4 Army Stances**

|             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stance**  | **Effect**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Moving      | Executes movement path. No defensive modifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Defensive   | ×1.20 to defRoll. On walls it stands **outside** them — no fortress bonus, no militia (only Garrison is behind the walls, §5.8.0)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Ambush      | ×1.40 to defRoll (field battle) **while DEFENDING** — valid only for an **Elf in forest** or a **Dwarf in mountain** (otherwise Defensive). A valid Ambush stands **outside** the walls, hidden from maps and spies, and is spent once it fights — see *Ambush in detail* below                                                                                                                                                                                                                                                                            |
| Garrison    | ×1.20 to defRoll (field battle); ×1.30 to defRoll (assault); surrenders on siege auto-fall instead of retreating if its realm owns the walls (an ally's Garrison inside is expelled instead, §2.7). **The only stance behind the walls** (§5.8.0) — and it never comes out to join a fight. A **besieged** army holds Garrison whatever it ordered (§2.13.7). Valid only on a **fortified construction** (wall maximum \> 0) — on any other hex, or on a settlement founded this very turn (unfortified until next turn), the stance demotes to Defensive. |
| Siege March | Advances **one hex per turn** and **camps** at a foreign fortified hex instead of storming it, then lays siege by itself — the ring closes at once if the force is enough (§5.8.0). Defends at ×0.85 if attacked (§5.8.0).                                                                                                                                                                                                                                                                                                                                 |
| Siege       | Besieges the walled construction the army STANDS ON (march in first — a hasty assault; survive to camp); Siege Progress +1/turn                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Assault     | Ordered by an army already camped ON a foreign walled hex: it storms the walls in Pre-Phase 3 (§5.6). A march onto walls is a hasty assault of its own (§2.13.6b). An army that files a march together with this stance **marches** — the stance is ignored that turn and a *Stance Ignored* card says so                                                                                                                                                                                                                                                  |
| Sally       | Only for a **besieged** army: in Pre-Phase 3 it goes out with every other besieged army that orders it and fights the besiegers in the open, as the attacker. One turn only, never stored (§2.13.7).                                                                                                                                                                                                                                                                                                                                                       |

**Only the defender's stance counts.** The attacking side of any land battle carries no stance modifier whatever: a **sallier** (§2.13.7), the attacker of its own battle, fights at ×1.00 however it was standing.

**Ambush in detail.**

**Who may hold it.** Only an **Elf army in forest** or a **Dwarf army in mountain**; any other race or terrain demotes to Defensive. An **invalid** Ambush was never one — it plays out as an ordinary Defensive stance, outside the walls, at ×1.20.

**Outside the walls.** A valid Ambush on a fortified hex stands OUTSIDE the walls. The one exception is a **link member**, which stands wherever its LEADER stands and has no stance of its own (§5.8.0 Cases E and F). Like every stance but Garrison it stands outside (§5.8.0) — on your own hex, a mutual ally's, a vassal's or a liege's (§5.6, §9.10). Outside it is hidden, keeps its terrain and the ×1.40, but has no fortress bonus and no militia; an attacker coming for the walls must fight it in the open first: a march or an Assault that beats it storms the walls the same turn, while a Siege March or a Siege loses that turn's progress.

**Spent — but the ground is kept.** **Any ambush that fights — win, lose or draw — is spent:** it reverts to Defensive for next turn (a trap that has been sprung is no longer a trap). The army nonetheless goes on holding that hex outside the walls, turn after turn, until you set **🏰 Garrison** to bring it back in or march it away — re-filing Defensive changes nothing, because it is already Defensive. A stored Ambush keeps working on a turn its realm files no orders — the outside zone and the spending included.

**Hidden.** A valid ambusher is hidden from every other kingdom's map, allies included, **and is invisible to spies, allied spies included** — a spy mission on its hex does not report it (§2.15); only marching onto the hex finds it. A sprung ambush is drawn on every foreign map from that same turn. An ally beside it that cannot hold Ambush stands in plain sight, so the hex still shows an occupant.

**A trap, even off your land.** Ambush is not limited to your own land: an army at peace with you that marches onto the hex meets it as any other army — a battle, and war between your realms — though it could not see you.

**In a link.** A leader in Ambush keeps it, but its **allied** members are visible and fight without the bonus, and an ally's offer to an army in Ambush stands unanswered (§5.11).

> ***▶ Stances stay in force.** Siege, Defensive, Garrison and Ambush are **stored on the army**: order one once and it holds every turn until you file another stance or a march — no need to repeat it, and forgetting it costs nothing. **The reverse is the trap: an army with no stance in force defends at ×1.00** — a newly raised army (except one raised on your own walled seat, which is born in Garrison, §5.8.0), one that just marched (the march clears the stored stance) or one that fell back from a defeat has none until you set one. **Any forced move off the hex clears it** — a retreat, a withdrawal or an expulsion, including one forced before the march phase by a storm of the walls or a besieger's clash with a camp outside. The exceptions keep or gain a stance because they never leave the hex: a beaten Sally's survivors, a **besieged** army beaten on its own hex, and an army beaten outside its own walls — each ends inside, in Garrison (§2.13.7, §5.8.0). A besieged army's stored stance is **Garrison**, and it stays Garrison after the siege lifts, until you file another stance or a march. The Player Page warns on the army card (No stance in force — defends at ×1.00), and on a queued march that the army will arrive with no stance. The stored value is the stance as resolved (an invalid Garrison or Ambush is stored as Defensive, and a Siege only while its ring stands). Moving is the default; **Assault is never stored** — it is a per-turn order. Aboard a fleet an army carries no stance. The Player Page pre-selects a stored stance and marks its button (in force); picking another stance or planning a march replaces it.*

**5.5 Field Battle**

Triggered when a moving army enters a hex occupied by an enemy army.

**5.5.1 Roll Formula**

initiative = 1.05 + rand×0.05 (attacker only — attRoll; defRoll has no initiative term)

variance = 0.90 + rand×0.20 (BATTLE_VARIANCE = 0.10 → ±10 %, independent per roll)

cmdMult = 1 + military/1000 (0 if no commander)

attRoll = attWP × status × attTerrainMult × cavTerrainScale × initiative × attCmdMult × variance

defRoll = defWP × status × defTerrainMult × cavTerrainScale × defStanceMod × defCmdMult × legion × variance

legion = 1.10 if the defender is Imperial, owns the hex and its construction is FI or POP (§4.2); else 1.0 — militia included. The attacker's roll carries it in ONE case only: a SALLY, where the fort's owner is the side charging out (attRoll × legion)

attTerrainMult / defTerrainMult: race terrain bonus if fighting on home terrain, else 1.0 cavTerrainScale: per side — the army's **mounted** WP share scaled by the battle terrain (§3.5.1); all-foot armies ×1.0 defStanceMod: Ambush ×1.40, Defensive ×1.20, Garrison ×1.20, Siege March ×0.85 (SIEGE_MARCH_DEF_MULT, §5.4), **Siege ×0.85 when attacked by anything but the sally it faces** (SIEGE_RELIEF_DEF_MULT — a relief army arriving from outside by land **or landing from the sea**, or one already camped beside it; against the sally the besieger keeps ×1.00), else ×1.0 status: each army's **readiness**, 0.10–1.00 (10–100%; §5.10) — a fatigued army rolls proportionally weaker, so a worn-down force can lose a fight its raw War Points would win. This same × status factor applies in every combat roll (assault, amphibious, naval); militia levies have no status and are never scaled.

**5.5.2 Outcome**

|                          |               |
|--------------------------|---------------|
| **Condition**            | **Outcome**   |
| attRoll \> defRoll × 1.2 | Attacker wins |
| defRoll \> attRoll × 1.2 | Defender wins |
| Otherwise                | Draw          |

> ***▶ Example — the defender's edge, quantified.** Army A (300 WP) attacks Army B (280 WP) standing **Defensive** on neutral plains. Setting the random rolls aside (they apply similarly to both): B's defensive ×1.20 lifts its roll to about 280 × 1.20 = 336; A rolls from 300.*
>
> *• A wins only if attRoll \> defRoll × 1.2 → it would need \> 403. It has 300. No.*
>
> *• B wins only if defRoll \> attRoll × 1.2 → it would need \> 360. It has 336. No.*
>
> *• Neither margin is met → **Draw**, and on a draw the attacker retreats and takes 6–12% losses for nothing.*
>
> *Attacking with more raw WP than the defender still failed, purely because of the defensive stance plus the ±20% decisive margin. **Rule of thumb: to reliably win an attack on a dug-in Defensive enemy on equal terrain, bring about 1.5× its raw WP** — the ×1.20 stance and the ×1.2 margin compound to ≈1.44×. Add terrain or a commander and that number climbs.*

**5.5.3 Casualty Formulas**

ratio = winnerRoll / loserRoll

The **winner's** losses scale straight down with the ratio — there is **no minimum-casualty floor**, so a lopsided rout costs the victor almost nothing, while a close fight (ratio just over 1.2) still bleeds both sides.

**Attacker wins:**

attLoss = 0.10 / ratio (no floor — a crushing win costs the winner almost nothing)

defLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) below 10:1 (at least 12% of the WINNER's WP, capped at 60% of own force)

\> \*\*▶ The damage floor.\*\* The loser always bleeds at least \*\*12% of the \*winner's\* war points\*\* — so a big army inflicts \*at least as many\* absolute casualties on a small enemy as on a large one. In own-force terms the floor is \`12% × ratio\`; it overtakes the log curve from about \*\*2.1:1\*\*, and its \*\*60% cap\*\* binds from \*\*5:1\*\* — a beaten small army is mauled, never annihilated by odds alone below the 25:1 ramp. Being \*\*surrounded\*\* remains the one true annihilation, exactly as in the sieges of history. The winner's own losses carry no floor (10%/ratio — which is always 10% of the loser's WP in absolute terms).

max(the floored value, 0.50 + 0.50 × (ratio − 10) / 15) above 10:1 (the 60% floor-cap holds to 13:1, then the linear ramp to a total wipe at 25:1)

**Draw:**

attLoss = defLoss = 0.06 + rand×0.06 (6–12% each, same value)

**Defender wins:**

defLoss = 0.10 / ratio (no floor — the winner's losses scale with the fight)

attLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) below 10:1 (at least 12% of the WINNER's WP, capped at 60% of own force)

max(the floored value, 0.50 + 0.50 × (ratio − 10) / 15) above 10:1 (the 60% floor-cap holds to 13:1, then the linear ramp to a total wipe at 25:1)

Loser's loss by ratio: 1.2 → 15% · 1.5 → 19% · 2 → 24.5% · **from ≈2.1:1 the floor leads** — 3 → 36% · 4 → 48% · **5:1 → the 60% cap, and it holds flat to 13:1** (6:1, 8:1, 10:1, 12:1 all → 60%). **Beyond 13:1 the ramp leads:** 15:1 → 67% · 20:1 → 83% · **25:1 and beyond → no survivors at all**, armour included. At sea the ramp is shorter — a fleet is wiped at 10:1 (§5.9.3).

> ***▶ The armour dissolves with the odds.** What you actually lose is the battle percentage **times your armour** — and armour is what the price of a soldier buys you (§ death factor). Below 10:1 that is unchanged: a heavily equipped unit still bleeds far less than levies. Above 10:1 the armour is stripped away on the **same schedule as the loss**, reaching nothing at 25:1. A twenty-man elite unit loses **4 · 7 · 13 · 20** across 10:1 → 15:1 → 20:1 → 25:1. Numbers cannot save you from odds that large; they only decide how long it takes.*
>
> ***▶ Why there is a ramp and not a switch.** Overwhelming odds should end an army, but the boundary must not decide the battle by itself. A hard switch at 10:1 would mean 10.0 costing you half your force and 10.1 costing all of it — a hair's difference in war points flipping a defeat into an extinction. The ramp keeps the two ends honest: **below the ramp no ratio annihilates** — a badly beaten army walks away with at least 40% of its strength and rebuilds; above 13:1 every further step of superiority buys real destruction, until at 25:1 there is nothing left to save. Assaults keep their own harsher curve.*
>
> ***Why the curve is soft.** The loss curve is calibrated so that a **2:1–3:1 defeat is recoverable in 4–5 turns of recruiting from one city** — from a ≥500-pop seat (recruiting is capped at 5% of the hex's population per turn: a Lv5+ Imperial/Barbarian construction, Lv3+ Elf/Dwarf/Aesir; a Lv1 seat of 100 needs ~26 turns for the same loss). It is concave: superiority keeps paying — the winner's own loss still falls as 0.10/ratio and the loser's keeps climbing — but with diminishing returns — capped at 60% below 10:1 by the damage floor (§5.5.3), then ramping to a wipe at 25:1. Decisive destruction comes from **position, not arithmetic**: cut off the retreat and the survivors die where they stand. Assaults on walls (§5.6.2) deliberately keep their own, harsher curve.*

**5.5.4 Weighted Casualties**

Casualties within an army are not distributed uniformly. Survival is driven by a unit's **full price** — every coin and commodity spent on the soldier protects him, and veterancy scales that protection. Composition does not matter: each unit stack answers only for its own worth, whether it marches alone or beside elites:

price (g-eq) = gold + iron×12 + horses×20 + wood×5 (equipment — rations buy nothing)

deathFactor = clamp( 0.3 … 1.0 , 1.0 − price × (1 + veterancy) / 1100 )

losses = battle loss % × unit count × deathFactor (rounded per stack)

**Minimum one.** Casualties round to the nearest soldier, so a tiny or elite stack can round to zero losses. **Each army** on the losing side of a field, amphibious or populace fight always loses **at least one soldier** (the floor is per army, so a losing coalition buries at least one man per member) (taken from the unit closest to a casualty); winners and draws are unaffected.

The costliest soldiers in the game sit on the **0.3 floor** and shrug off ordinary battle percentages almost entirely; cheap levies ride near the **1.0 ceiling** and die at most one-for-one with the nominal battle losses — the factor only ever *protects*, it never amplifies (levied militia sit at exactly 1.0). An army's TOTAL casualties therefore depend on what it is made of — a levy horde bleeds at the headline rate where a professional army walks away.

> ***▶ Example — why equipment and veterans survive.** Velites (50g + 8 food + 6 wood×5 = 80 g-eq) carry deathFactor = 1.0 − 80/1100 ≈ 0.93; fresh Praetorians (300g + 100 iron×12 + 5 wood×5 = 1,525 g-eq) bottom out at the 0.3 floor (1.0 − 1,525/1100 \< 0.3). At a battle-wide 20% loss the Velites shed 20% × 0.93 ≈ 18.5% while the Praetorians lose 20% × 0.3 = 6% — and the per-stack rounding usually turns a small elite stack's fractional losses into **zero**. A veteran at 1.5× base WP counts as a soldier half again as expensive, so experience compounds survival toward the 3× XP cap.*

**5.5.5 Commander Death**

After combat, commanders are checked for death:

deathChance = min(0.4, lossPct × 0.5)

**Field battle**: both commanders checked unconditionally after battle. **Assault — attacker wins**: both commanders checked unconditionally. **Assault — repelled**: attacker's commander checked unconditionally; the garrison commander rolls on any positive loss too (see §7.7).

Commander death is permanent. The character is marked dead and no longer affects rolls.

**The enemy is told too.** When a commander falls, the kingdom that lost them gets its mourning card — and so does **every kingdom that fought on the other side of that engagement**, in a card naming the dead commander and their kingdom, and saying whether they led an army or a fleet — **never which one**: a body on the field is identifiable, but the number of an enemy force is intelligence and no card gives it away. Because battles here are fought by **coalitions** (§5.11) and no engine anywhere records whose blade landed the blow, all of the opposing kingdoms are told, and each is told **once per death** no matter how many armies it brought. The card claims no credit for any particular soldier — it reports a body found, not a duel won.

**The city that fought with nothing but its people counts.** In an assault, "the other side" is exactly the set the engine already uses to decide who you went to war with: the **garrison coalition plus the hex's owner**. So a kingdom whose settlement was stormed while it had **no army there at all** is still told what its militia took with it — its townsfolk were the whole defence, and a militia-only defender earns the card as surely as a garrison does. If the owner also garrisons the hex, it is still told **once**, not twice.

**At sea, the rule is the victor.** A commander who drowns with a transport is reported to whoever **won** the fight that sank it: the winning fleet in a naval battle, or the kingdom whose siege or storm made the port fall under a fleet trapped at its moorings. Winning coalitions are treated exactly as they are on land — every kingdom on the winning side is told, once each.

**Where nobody is told.** Only one death class is silent, and the reason is that there is **no victor to credit**: a naval **draw**, where the attackers fell back (the defenders hold on a draw) and the transport went under anyway (and its close cousin, a hull emptied by battle casualties on either side — that sweep can fire on the winner's own ship). The Witch King (§7.8) cannot be slain at all, so there is nothing to report either way.

**5.5.6 Retreat**

Retreating armies search up to **3 hops** outward for a valid hex:

- Valid destination: non-sea terrain, not enemy-owned territory, and **either empty of armies or held only by FRIENDLY armies with room** — own / mutual-ally / vassal / liege, stack **under the 3-army cap** — on a walled hex counted in the outside zone, where a retreat always arrives (§5.8.0). Because friendly armies may **share a hex** (up to 3), a beaten army may **rally onto its friends**; but a **full stack (3 armies)** or **any non-friendly army** on the hex blocks it, exactly as an enemy army does. **A muster with no soldiers left is not an army for any of this**: it neither bars a hex nor fills a friendly stack, so it can never push a beaten army onto a worse hex — or, with the alternatives closed, get it killed where it stands. The same rule holds everywhere the engine asks whether an army is present: who defends a hex, who joins a shield wall, and what blocks a path.

- **The search never crosses sea** (or leaves the map): the multi-hop cascade exists to slip past friendly-occupied or hostile *land*, not to ford open water. An army has no ships — it cannot rout to the far shore of a strait.

- If no valid hex is reachable within 3 hops **over land**: the army is **destroyed** where it stands (and its fallen are stripped in full by a decisive winner, §2.13.11). An army pinned against the coast, or defending an island without a friendly hex on it, has nowhere to run.

Among the hexes that *are* valid the search takes the **nearest** first; among hexes at the same distance it prefers the army's **origin** (where it came from), then your own land, then a mutual ally's, then neutral (a liege's or a vassal's land ranks as neutral here). Distance is the primary key: a free neutral hex one hop away beats your own land two hops away. There is **no special "fall back to the capital" rule** — the capital is just another own-territory hex.

> ***⚠ You can still close your own defender's escape.** Rallying onto friends works **only while the stack has room**. Recruitment and army placement (Pre-Phase 2 / 2b) resolve **before** combat — the pre-phase fights as well as Phase 5 — so filling the fall-back hex to its **3-army cap** — or leaving a **non-friendly** army on it — makes it an **invalid** retreat. The **capital** is not a special fallback: a full stack there (a capital-army can be what pushes it to the cap) blocks it like any other hex. Jam your own backfield to the cap and a beaten army with nowhere left to go is **destroyed**.*

Outcomes:

- Attacker wins: defender retreats; attacker claims the hex — except an army of the owner or a friend beaten outside its own walls, which goes inside in Garrison (§5.8.0)

- Draw: attacker retreats; defender holds

- Defender wins: attacker retreats

> ***Displacement mid-march.** Movement resolves as a round scheduler (§2.13.1): an army or fleet — including a member of an ARMY LINK or FLEET LINK group — can be forced from its hex by a **different** mover's battle fought earlier the same phase — a bystander caught up in someone else's fight, not its own. When that happens, the displaced mover **forfeits the remainder of its queued path**; it does not resume marching toward its original destination from wherever the battle left it. An honest "displaced mid-movement" card explains the halt rather than silently walking the mover back onto its plan.*

**5.5.7 Experience Grant**

Both surviving armies gain experience after every battle regardless of outcome, scaled by the opponent-strength factor (§5.3.1) — a walkover teaches nothing.

**5.6 Assault**

Triggered in Pre-Phase 3 for an army holding Assault stance ON a hex carrying a foreign **walled construction** (§3.7.2). A construction with no wall is not assaulted — it is simply fought over as open ground.

**Who defends — and how.** An assault — a march onto the walls, an Assault stance, a landing — first beats the armies outside, then **storms the walls**; every Garrison inside defends behind them at ×1.30, with the fortress bonus and the militia (§5.8.0), and nobody sallies unordered (§2.13.7). With no army inside, the militia holds the walls alone. **Every realm inside is a defender.** An army that storms walls or lays or presses a Siege on them declares war on **every realm with an army inside**: the owner, a realm at peace with it, and its own mutual ally, vassal or liege, whose alliance or fealty breaks on the spot (the attacker reads *A sworn alliance lies in ruins*, the realm inside *…lies shattered*), linked into the defence or not. It is declared again at **every siege turn**, so a realm that walks into a besieged city is at war with the besieger from its first turn inside. Only the attacking army's own kingdom declares — a member of its link group keeps the ordinary rules (§5.11.1). Armies camped **outside** the walls are not inside and are not touched by it — and every army not in Garrison stands outside (§5.8.0): any attacker coming for the walls must fight it there first. One exception inside: an army at war with **another defender** stands aside from the defence. A kingdom that files no orders has its armies with no stance on its own or a friend's walls put in Garrison while there is room and no army at war with it is camped outside (§5.8.0). Walls that **nobody owns** have no inside — there is no owner to shelter under — so an army of a kingdom at peace with you standing there is met as on open ground: war is declared and you fight it at the gates. **When walls fall, the hex's owner alone is carded the loss** — an ally whose army held them keeps its defeat card, and the conqueror lowers the owner's banner. An **amphibious assault** (a beach landing onto a coastal construction, §5.7) storms the walls the same way: a storm that is **repelled** leaves the survivors camped ashore at the gates, after the flat disembark cost (−20 status), as a marcher would (§5.8.0); re-boarding after a lost beach fight happens everywhere except on foreign walls (§5.7.2).

> ***▶ Worked example — war on every realm inside.** Gruk-Mor owns a walled town at (14,9). Inside stand Gruk-Mor's Army I (Garrison) and Sylvane's Army II (Garrison). Sylvane is allied to **both** Gruk-Mor and Aldoria; Aldoria is at war with Gruk-Mor and sends Army III in **Siege March**.*
>
> *- **Turn 1 — arrival.** III reaches the gates and lays siege by itself (§5.8); strong enough, it closes the ring at once. Laying it declares war on every realm inside: on Gruk-Mor (already at war) and on **Sylvane**. The Aldoria–Sylvane alliance breaks: Aldoria reads A sworn alliance lies in ruins, Sylvane …lies shattered.*
>
> *- **Turn 1, Phase 5 — a late guest.** Zingara, allied to Gruk-Mor, Aldoria **and** Sylvane, marches Army I up to the town — onto an ally's walls, past an ally's camp, so no battle. A march never carries Garrison: Zingara's I stands **outside**, and nobody declares on it.*
>
> *- **Turn 2 — the siege turn.** Zingara orders **Garrison** and goes inside. III's siege tick declares war again on every realm inside, so Aldoria and Zingara are now at war — and their alliance lies in ruins too. This is the first tick (progress 1, §5.8.0). Gruk-Mor and Sylvane have been besieged since this turn (the ring closed on arrival), so their orders were already only Garrison or Sally; Zingara, outside when the turn began, is besieged from turn 3. Had Zingara stayed outside, no war would have followed, and it would never be besieged.*
>
> *- **The fall.** Gruk-Mor's Army I surrenders and Sylvane's and Zingara's armies are expelled or cut down, exactly as in §2.7's the walls fall example.*
>
> *- **What the page shows.** Your Player Page warns before you commit. The march-in, Siege March, landing and Siege/Assault notes name every realm you can see inside that you are not yet at war with, and flag an ally with "the alliance breaks".*

**5.6.1 Roll Formula**

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

defStanceMod applies to **garrison WP only** (not militia): Garrison ×1.30 — only a Garrison stands inside (§5.8.0). Defender terrain bonus applies. cavAssaultScale: the attacker's **mounted** WP share is taxed ×0.65 when storming walls (replaces the terrain regime for the attacker); cavTerrainScale: the garrison's mounted share is terrain-scaled as in the field (§3.5.1). All-foot armies ×1.0 on both.

**Walls are worth what they are big enough to be worth.** The fortress bonus is derived from the wall's **size**. A timber palisade and a Dwarven citadel do not defend alike:

|                  |                                      |                                                                                                            |
|------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Wall maximum** | **Fortress bonus at full integrity** | **Roughly what the attacker needs (raw WP, after its ×0.85 storm penalty and an average initiative roll)** |
| 500 (palisade)   | ×1.55                                | ~2.0 : 1                                                                                                   |
| 2,500            | ×2.00                                | ~2.6 : 1                                                                                                   |
| 5,000            | ×3.00                                | ~3.9 : 1                                                                                                   |
| 10,000           | ×5.00                                | ~6.6 : 1                                                                                                   |
| 15,000 and above | ×7.00                                | ~9.2 : 1 — a great fortress is not stormed, it is starved                                                  |

The muster seat adds **+0.10** on top. Walls above 15,000 give nothing further — the curve caps there.

**Why the curve has two halves.** The bonus is the higher of two ramps: a steep one, 1 + 6×r, which sets the headline numbers above, and a gentler one, 1.5 + 1.5×r, which acts as a **floor**. They cross at a wall of about **1,667**. Below that crossing the floor rules — every 500-point palisade, every Dwarf FDW1–3. Above it the steep ramp rules, up to ×7.00 for a 15,000 wall.

**Integrity scales both sides of the fight, continuously.** A wall beaten to half strength gives half the bonus *above 1.0* — an FDW10 citadel at ×7.00 whole is ×4.00 at half integrity and ×1.00 once breached. And the attacker's penalty relaxes in step: a whole wall costs the attacker the familiar **×0.85**, a half-beaten wall ×0.925, and a **breached wall costs nothing at all (×1.00)**. Battering the wall down before you storm it is therefore worth two things at once, and this is exactly what siege engines are for (§5.8.6).

A construction with **no wall** — Orc Level 0–3, Generic Lv.1–4, Nomad Lv.1 — gives ×1.00 both ways. It is an open settlement, defended by its militia alone.

> ***▶ Example — storming a settlement is expensive, and breaching it is the discount.** Target: an Imperial **FI12** (wall maximum 1,500 ⇒ fortressBase = max(1.5 + 1.5×0.1, 1 + 6×0.1) = max(1.65, 1.60) = 1.65 — small walls sit on the floor), population 4,000, defended by a 200-WP garrison on **Garrison** stance (×1.30); both armies all-foot, so the cavalry factors are ×1.0. Population mints militia: floor(4,000 × 0.05) = 200 militia × 20 WP = 4,000 militiaWP (militia WP ≈ the population itself).*
>
> *• **Walls whole (integrity 1.0):** fortress ×1.65, attacker ×0.85. Defender roll (200 × 1.30 + 4,000) × 1.65 = 4,260 × 1.65 = 7,029. To clear the decisive margin the attacker needs attWP × 0.85 \> 7,029 × 1.2, i.e. **\`attWP \> ~9,920\`**.*
>
> *• **Walls breached (integrity 0.0):** fortress ×1.00, attacker ×1.00. Defender roll 4,260. Now the attacker needs only attWP \> 4,260 × 1.2 = **\`~5,110\`** — barely half.*
>
> *• Knocking that 1,500-point wall flat takes 1,500 ÷ 250 = **six engine-hits** — six engines bombarding for one turn, or three engines for two turns (§5.8.6). Whether that is cheaper than nearly doubling your army is the whole question of siege warfare.*
>
> *The **militia alone (≈ the population) dominates** the defence — the garrison and walls pile on top. Population itself is the weapon (more pop → proportionally more militia). The flip side: that militia is **drawn from the population, and its fallen are removed from it** afterwards (proportional to the fight, §2.13.4) — a repelled assault costs the settlement a sliver, a successful storm guts the levy, and a settlement can be worn down by repeated assault. If you can spare the turns, a **Siege** (§5.8) takes it with zero battle casualties to you; reserve assault for when you can't wait or can't gather the ring (§5.8.1).*

**5.6.2 Outcome and Casualties**

Same threshold as field battle (ratio \> 1.2 for decisive result).

**Attacker wins:**

attLoss = 0.15 / ratio (no floor)

defLoss = ratio ≥ 5 ? 1.0 : min(0.95, 0.25 × ratio)

**Draw:**

attLoss = defLoss = 0.10 + rand×0.08 (10–18%)

**Defender wins (assault repelled):**

defLoss = 0.12 / ratio (no floor)

attLoss = ratio ≥ 5 ? 1.0 : min(0.95, 0.30 × ratio)

Note: **assaults keep a harsher curve on purpose** — the soft curve (§5.5.3) applies to field and amphibious battles only. At the walls the loser climbs 0.25 × ratio (attacker repelled: 0.30 × ratio) and is **annihilated at ratio ≥ 5**. Storming walls is meant to be the one fight that can end an army in an afternoon. The **death-factor ceiling of 1.0** (§5.5.4; militia 1.0) applies to assault casualties as well — cheap bodies never die faster than the headline loss %, so a 100-man cheap garrison stormed at 3:1 loses 75 (by design).

**5.6.3 Degradation on Capture**

**Every** change of hex ownership — assault storm, siege auto-fall, land seizure, beach landing, amphibious assault — damages what stands on the hex. Two separate things degrade, each by the same rule, each at most once per turn.

**The production site**, if there is one:

- Site level **−1**, to a **minimum of level 1**. A site is never razed by conquest.

- The conqueror is notified with a **Captured Works Damaged** card; capturing a level-1 site changes nothing and is silent.

- Applies to farms, mines and ports alike. Forges are level-1-only and are unaffected.

- Consequence for mines: a captured Dwarven Lv3 mine arrives as **Lv2**, and only a Dwarven owner can ever dig it back to Lv3 (§3.6.2).

**The construction**, if there is one:

- Construction level **−1**, to a **minimum of level 1**. A settlement is never razed by conquest either — you always inherit something.

- The wall's maximum drops with the level, and current integrity is **clamped down** to the new maximum. A wall already below it is left where it is: conquest never *repairs*.

- **Population is untouched.** It keeps whatever it had, which after a degrade is very often *above* the new level's ceiling — legitimately so. Such a settlement simply stops growing (§3.8) until you raise it back up, and pays full tax and mints full militia in the meantime.

- The conqueror gets a **🏚 Fortifications Degraded** card naming the level it fell from and to.

> ***▶ Why this hurts more than it looks.** Storming an FI12 (wall 1,500, ceiling 3,000) leaves you an FI11 — wall maximum 1,000, ceiling 2,000 — holding 3,000 people. And if it was a foreign family's construction, you can never upgrade it back (§2.11.7): that lost level is permanent under your banner. Conquest of a rival's heartland yields a great many people living behind permanently diminished walls.*

**5.6.4 Post-Assault State**

**Victory**: Attacker occupies hex; siege progress clears.

**Repelled**: If no other besieger on that hex, siege progress resets to 0. If another kingdom is actively besieging, their progress continues. Either decisive outcome swings opinion like any battle (§8.5.3). (A **drawn** assault swings nobody's opinion — the attacker's card still reads *repelled*, since it was driven back, but no one gains or loses standing.)

**5.7 Amphibious Battle**

Triggered when a fleet with a transported army disembarks onto a defended land hex.

**Every army on the beach hex at war with the lander defends together**, and the defender's link members join, each at its own stance and commander — the land coalition rule (§5.11); Ambush ×1.40 and Siege March ×0.85 apply to a beach defender exactly as in the field.

**5.7.1 Roll Formula**

BEACH_PENALTY = 0.50

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (±10 %)

attRoll = attWP × status × 0.50 × initiative × attCmdMult × variance

defRoll = defWP × status × defStanceMod × defCmdMult × legion × variance

No terrain multiplier for either side. No fortress bonus for defender.

**5.7.2 Outcomes**

|                      |                          |           |                  |              |
|----------------------|--------------------------|-----------|------------------|--------------|
| **Outcome**          | **Condition**            | **Hex**   | **Attacker**     | **Defender** |
| **Attacker wins**    | attRoll \> defRoll × 1.2 | Seized    | Lands, holds hex | Retreats     |
| **Draw / Stalemate** | rolls within 20%         | No change | Re-boards fleet† | Holds hex    |
| **Defender wins**    | defRoll \> attRoll × 1.2 | No change | Re-boards fleet† | Holds hex    |

†If the attacker is destroyed (every unit lost in the fight — a landing force never searches for a retreat hex), the army is gone outright — no re-boarding. Re-boarding applies everywhere except on **foreign** walls: on a walled settlement or capital owned by another realm that is not your mutual ally, vassal or liege, the surviving landing force instead unloads, pays the flat disembark cost (−20 status) and holds a beachhead outside the walls, whether it was beaten on the beach or repelled from the walls (§5.6, §5.8.0). When the beach falls, the hex's **owner** is carded the loss — and when another kingdom's army was holding it for the owner, the card names that army: *"(X's army holding it was driven off the beach)"*. An **unowned** coast has no owner to card: nobody is told it was lost, and the conqueror's card reads *"No banner flew here; up goes yours…"*. On walls, an army of the owner or a friend camped outside that the landing beats goes inside in Garrison and defends the storm (§5.8.0); any other camper the landing beats retreats like any field defeat, or is cut down if it has nowhere to go.

War is declared in all three outcomes. A draw is a **stalemate**: the landing fails, the attacker re-boards under fire (on foreign walls it digs in instead, †), and the defender retains the hex. Unlike land battles (where a draw also favours no one), amphibious draws carry heavier attacker casualties (attacker 8–14% vs defender 5–10%, §10.2) due to the beach withdrawal.

> ***⚠ What this means — never land on a defended beach lightly.** The ×0.50 beach penalty halves your attacker WP before anything else applies. Against a defender of equal raw WP on Defensive (×1.20), your effective roll is 0.50 of base versus their 1.20 — you're outrolled better than two to one, and to actually win you need roughly **2–3× the defender's WP** (attWP × 0.50 \> defWP × 1.20 × 1.2 ⇒ attWP \> ~2.9 × defWP). Prefer landing on undefended open hexes (still a WP contest vs the local populace militia at the same ×0.50 penalty — no enemy army to face, but a populous coast resists and can repel a weak landing) or sailing into an undefended port and disembarking into the settlement; save opposed amphibious assaults for after you've already broken the local defenders — and recall that losing the preceding naval fight drowns the whole army (§2.14.6).*

**5.7.3 Casualties**

**Attacker wins:**

attLoss = 0.10 / ratio (no floor)

defLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) (same floored soft curve as the field, §5.5.3)

**Draw (stalemate — attacker re-boards, or digs in on foreign walls †):**

attLoss = 0.08 + rand×0.06 (8–14%)

defLoss = 0.05 + rand×0.05 (5–10%)

**Defender wins:**

defLoss = 0.10 / ratio (no floor)

attLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) (same floored soft curve as the field, §5.5.3)

The beach uses the field curve unchanged — the ×0.50 beach penalty already shifts the ratio against the lander, so no extra loss multiplier is needed. Only the draw keeps its landing-side asymmetry. A repelled landing force is never annihilated by ratio below the 25:1 ramp; it loses at most **60%** (the damage-floor cap, §5.5.3) and re-boards — or, on foreign walls, digs in outside them (†); with no fleet to re-board it is destroyed.

**5.8 Siege Warfare**

**5.8.0 The Walls — Inside and Outside (Siege On-Hex)**

**Sieges are pressed from the fortification's own hex.** A hex with a walled construction has two zones: **INSIDE the walls** and **OUTSIDE** (the hex's open ground). **Only an army in Garrison stands inside.** An army of the owner — or of a mutual ally, vassal or liege of the owner — whose stance is **Garrison** stands behind the walls: the fortress bonus, the militia and ×1.30 against a storm. **Every other stance stands OUTSIDE**, on the open ground, and fights there at its own stance (Defensive ×1.20, none ×1.00, a valid Ambush ×1.40 — §5.4). Enemies, strangers and neutrals always stand outside. Three more rules decide a zone: a **link member** stands where its leader stands (Cases E and F below); a **besieged** army is a Garrison and stays inside while that ring stands, whatever becomes of its alliance (§2.13.7); and a realm that files **no orders** holds its walls — its armies there with no stance are put in Garrison while there is room and no army at war with it is camped outside (a stance it chose is kept). Each zone holds at most **3 armies**. **To defend a city**, put up to 3 armies in Garrison; an army left outside on Defensive is a screen — the attacker must beat it first, and, beaten, it joins the Garrison for the storm. The Player Page draws the zones the engine decided (the fan is split by zone — §5.11), and this is deliberate intel: on any walled hex you can see, the walls badge (§5.11) tells you who stands **inside** — and therefore who the owner counts as friend, ally, vassal or liege — exactly as a scout would read the walls. A linked group marching onto walls arrives **outside** with its leader; a member friendly to the fort's owner leaves the group rather than fight that owner or its friends (§5.11.1 rule 3), and if the outside zone would overflow, the whole group halts at the gate; the card names the zone that is full.

**Getting inside — Garrison is the only door.** Order Garrison and the army stands inside from that turn's pre-phase on — **but never past an enemy**: an army that began the turn outside its walls with an army **at war** with it camped there cannot order its way in (the order reads as Defensive, ×1.20, and a card says why); it must beat that army first. **A march never carries Garrison**: an army that marches home arrives outside and orders Garrison the next turn. An army **raised** on a walled muster seat is born in Garrison, and one **split** from a Garrison stays inside. The inside fills like any zone: with 3 already in Garrison, a fourth Garrison order stays outside, carded. A **link group** goes in whole or not at all — beaten outside or ordered in (beaten, it goes in whole, but the link breaks as after any lost field battle, §5.11) — and past a camp it is barred if **any** of its realms is at war with the camp. Every other door is shut the same way: a link whose leader stands inside cannot form past an army at war with the joining army camped outside, nor into a full inside (Case F); and troops cannot be **transferred** from an army outside to one inside past such a camp (*troops do not pass into the walls*). An army that leaves its group this turn — by UNLINK, its leader's release or §5.11.1 rule 3 — and has filed Garrison passes the same door. A Sally filed by an army that is not besieged is a Garrison order and passes the same door. **A Garrison is a place on these walls:** an army driven off its hex during the turn (a retreat, a withdrawal) onto other walls stands outside them with no stance, whatever it filed. A leader that dissolves its group this turn and files Garrison is judged alone. **An army of the owner or a friend standing on its walls in any stance but Garrison is told so once** — *Army N stands outside the walls at (c,r)* — so nobody finds out in the middle of a storm. **Beaten outside, it goes in:** an army of the owner or a friend attacked on the open ground of its own walls that **loses** goes inside in Garrison (room permitting) and defends the storm that follows the same turn; a **draw** changes nothing for it — the attacker falls back. **That is only for the army already on the hex.** One that comes from outside — a relief marching in on the besieger — and loses or draws is the attacker: it falls back like any attacker, never into the city; and a besieged city is never a retreat destination, since the camp at its gates blocks it. An army caught **marching out of or through** its walls reads Moving, stands outside and fights there: win or draw, it marches on; beaten, it goes inside in Garrison. **The conqueror** of walls — by storm or by the fall of a siege — stands inside them in Garrison.

> ***▶ Examples — the door.***
>
> *- **Past a camp.** Hyperborea's II stands on Defensive outside its own walls at (24,34), and Aquilonia's VII, at war with it, is camped beside it. II orders Garrison: it reads **Defensive** (×1.20), carded Army II cannot go inside the walls at (24,34), and the Phase-5 camp sweep fights the two. If II wins, VII falls back and II may order Garrison next turn; if II loses, it goes inside in Garrison.*
>
> *- **A full inside.** Three of Hyperborea's armies hold (24,34) in Garrison. A fourth, IV, orders Garrison: it stays outside on **Defensive** (×1.20), carded Army IV cannot go inside the walls (no room inside); the Player Page greys the button out with no room inside. If one of the three marches away, order Garrison again: the refused order was kept as Defensive. A link group is counted whole — a leader and its member need two places.*
>
> *- **A mixed group.** Hyperborea's II leads Nemedia's VI outside (24,34), and Aquilonia's VII, at war with Nemedia only, is camped there. II orders Garrison: the whole group stays outside on Defensive, because one of its realms is at war with the camp. A transfer from a Nemedian army outside to a Nemedian army inside is refused the same way (troops do not pass into the walls).*
>
> *- **A realm that missed the turn.** Nemedia files no orders. Its VI, with no stance, stands on its own walls with room inside: VI is put in Garrison and holds the walls. Had VI been on Defensive, it would stay outside on Defensive; had an army at war with Nemedia been camped outside, VI would stay outside with no stance.*

To besiege or assault, **march onto the fort — and marching in is a HASTY ASSAULT** (assault-on-arrival). The march first meets **every hostile army outside** — the owner's and its friends' armies not in Garrison, a rival besieger, a relief force — in a **battle at the gates**, in the open. **Win it**, with no hostile camp left outside, and you **storm the walls the same turn**: against the Garrison inside (×1.30), the fortress bonus from the wall-size curve (×1.55–×7.00 scaled by integrity; attacker ×0.85 only at full integrity — §5.6.1) and the militia — the armies you beat outside went in and defend with them. **Lose or draw** the gate battle and the march ends and the attacker falls back (§5.5.6). A landing is the exception: its survivors dig in outside the walls (§5.7.2). With the open ground clear, you storm at once. **Win the storm and you take the fort. Be repelled but survive and you stay camped at the gates** (the outside zone) — that camp is the on-ramp to a multi-turn siege. A **Siege March** that wins the gates lays siege instead of storming (§5.8). An Assault ordered from a camp at the gates (§2.13.6) and a landing (§2.14.6) follow the same order: the open ground first, then the walls. **A Garrison never comes out** to join a fight at its gates — only a besieged army that orders **Sally** goes out (§2.13.7). Enemies do not share a zone for long: the next camp sweep fights them (§2.13.5) — inside a **besieged** city at every sweep, since its loser stays inside (§2.13.7); enemies **across the wall line** share the hex in peace, blade-distance apart.

> ***▶ Worked example — two marches onto one fort in a turn.** **X**, a link group of three armies (60 MP, status 97), and **Y** (60 MP, status 90) both order one plains step onto **Z**, a small walled port of Y's own realm — walls 50 HP, population 21, **no army inside**. X stands at (29,26) and Y at (27,27); Z is (28,26). (Three unlinked armies of X would take Z with the first and arrive outside with the other two, which Y would then meet in the open first.)*
>
> *\| Round 1 of Phase 5 \| What the engine does \| Why \|*
>
> *\|---\|---\|---\|*
>
> *\| **X steps first** (status 97 beats 90 — §2.13.1) \| Z is a foreign fort with nobody inside: **hasty assault** against the militia alone. 1,361 vs 21 — Z falls. X's three armies are now **inside** Z, in Garrison \| §5.8.0: marching in is a hasty assault; the conqueror stands inside in Garrison \|*
>
> *\| **Y steps second**, 30 MP spent, 30 left \| Z is now a foreign fort with three enemy armies inside: Y **storms the walls at once** (nobody stands outside). X's armies defend behind them in Garrison (×1.30), the militia of 21 beside them, walls 50 HP. Win → Z is Y's again and X's survivors retreat; repelled → Y digs in at the gates \| §5.8.0: the conqueror is a Garrison; §5.6 \|*
>
> ***MP never decide a battle:** Y's 30 leftover MP bought nothing — a battle costs no MP, and reaching walls ends a march whatever is left (§2.13.2).*

**Siege March — reaching the gates without storming them.** Marching onto an enemy walled construction normally means a **hasty assault** that same turn. An army in **Siege March** stance instead walks up and **camps** in the outside zone: the walls are not stormed, nobody inside fights, and even an undefended fort is not captured — you take it with next turn's Assault. The stance acts only where the march **ends**: a Siege March whose march ends anywhere but on enemy walls — or with no march at all — does nothing, and the army card says so. An army already camped at the gates attacks with **Assault**, not with a march. An **open settlement** (a level whose wall is 0, §3.7.1a) has no gates to camp at: a Siege March onto it is an ordinary march, and it is taken from its militia like any undefended hex (§2.13.4). The price is paid in tempo and exposure: the march covers **one hex per turn**, and if an enemy army attacks the column it defends at **×0.85** (a besieger already dug in at the gates defends at ×1.00 against the sally it faces, and at ×0.85 against a relief army that comes at it from outside). **Reaching the gates lays siege** — even when it first had to beat an enemy camped there. Laying it declares war on every realm inside, a friend of yours included (§5.6). The army's stored stance becomes Siege on arrival and, if the column passes the §5.8.1 force test there and then, **the ring closes at once** — unless another realm already holds the ring there, and then the next tick decides between the two besiegers (§5.8.2). A link group counts together, but a member that is a friend of the walls' owner leaves the group at those walls and does not count. The realms inside are besieged from the next turn (§2.13.7); the walls' owner and every realm inside are told that turn, and the siege makes its first progress at the next turn's tick. A column too small for the force test only camps: its Siege stays stored and closes the ring at the first tick it passes, a failure carded as usual. Order Assault or another stance to do otherwise. Investing a foreign fortress declares war, as an assault would. An enemy army already camped outside those walls is fought as an ordinary field battle (a besieger, like a march, fights the camper **at war** with it before a peaceful one) — Siege March exempts you from the *walls*, not from *armies*. **Camping costs rest too**: an army camped on a foreign fortified hex recovers no STATUS, whatever its stance (§5.10.5).

**The stance never storms walls, arriving or departing.** Marching off a fortified hex it is camped against, a Siege March disengages and advances one hex — as every stance does from a fortified origin; open ground is still claimed on departure (§2.13.2b).

Then, from the fort's hex, order **Siege** or **Assault** on later turns (there is no besieging from an adjacent hex). From the turn after the ring is laid — on a Siege March's arrival or at your first siege tick (§2.13.7) — the armies inside are **besieged**: they hold Garrison, cannot march out, and may order a **Sally**, fought before your siege tick or storm (§2.13.7). **The losing side of any field fight buries at least one soldier** — a one-man picket cannot sally forever. **A repelled assault does not abandon the siege**: its surviving attackers stay camped at the gates and can press on next turn — only annihilation, or losing the open ground in a battle at the gates, removes them. Reinforcing a besieged fort means fighting through the camp outside; retreating *into* a besieged fort through the siege lines is not possible, and a **link** does not cross the siege line either way (§2.13.7).

> ***▶ Worked example — A's walled town, B's army beside it, C coming for both.** A owns a walled hex; A's army and B's army (B is A's mutual ally) stand on it; C is at war with both. Every line below is what the engine actually does.*
>
> ***Turn 1 — C marches in (Moving stance); A holds Garrison, B holds Defensive.***
>
> *\| What happens \| Why \|*
>
> *\|---\|---\|*
>
> *\| **A is inside, B is outside.** Only a Garrison stands behind the walls: A holds them; B, on Defensive, stands on the open ground \| §5.8.0 \|*
>
> *\| **C meets B first, in the open** — B at ×1.20, no walls, no militia. **B wins** → C falls back, the walls are never reached. **B loses** → B goes inside in Garrison, and C storms the walls the same turn against A and B (Garrison ×1.30 each), the fortress bonus and the militia. **A draw** → C falls back; B stays outside \| §5.8.0 \|*
>
> *\| **C takes the walls — the fort is C's**, and A's and B's survivors are expelled. **C is repelled by the walls — it digs in at the gates** as a besieger, and next turn can order Siege \| §5.6, §5.8.0 \|*
>
> ***Turn 2 — C takes Siege stance; A and B are inside, in Garrison.***
>
> *\| What happens \| Why \|*
>
> *\|---\|---\|*
>
> *\| **No battle at all.** A besieger does not storm, and nobody inside is besieged yet — C's first tick lays the ring after the check (§2.13.7), so A and B may still march out this turn; they may Sally only from Turn 3 \| §5.8.2 \|*
>
> *\| **The siege counter rises by 1 a turn**, to a threshold of **4** — or **5** if the hex is your muster seat. Past the threshold the garrison surrenders, without a single battle \| §5.8.2–3 \|*
>
> *\| **From Turn 3, A and B are besieged** — Garrison or Sally, no march. To break the ring they order **Sally**: A and B go out **together**, linked or not, and fight C in the open as the attacker. Win → C falls back and the siege is lifted; draw → no progress that turn; loss → back inside in Garrison, and the siege ticks \| §2.13.7 \|*
>
> *\| **If they never sally**, the walls fall at the threshold: A's army surrenders with them (a besieged army is a Garrison); B, an ally's, is expelled — or cut down if cornered \| §2.7 \|*
>
> ***Case D — add a fourth army: D, A's own, an Elf standing in the hex's forest holding Ambush.***
>
> *\| What happens \| Why \|*
>
> *\|---\|---\|*
>
> *\| **D stands OUTSIDE the walls — Turn 1, Turn 2, whatever A and B do.** Only a Garrison is inside; an Ambush is not a Garrison. (D is unlinked here. A link changes this — see Cases E and F below: a member stands where its leader stands.) \| §5.4, §5.8.0 \|*
>
> *\| **Turn 1 (C marches in): C must fight D in the open FIRST** — with B too, if B is still outside on Defensive. D defends at Ambush ×1.40, hidden until struck. **C wins** → the beaten go inside in Garrison, and C storms the walls the same turn; **C loses or draws** → the march ends there, the walls untouched \| §5.4, §5.8.0 \|*
>
> *\| **Win, lose or draw, D's trap is now sprung.** Any Ambush that fights is spent — and **from that same turn D is drawn on every foreign map**, ally's and enemy's alike (a sprung ambush conceals nothing, even if the page re-files the Ambush order) \| §5.4 \|*
>
> *\| **D wins or draws → C falls back; D stays outside**, now on Defensive — no longer hidden, no longer bonused, until re-ordered into Ambush and its terrain validates again \| §5.4, §5.8.0 \|*
>
> *\| **D loses → D goes inside in Garrison** (room permitting) — beaten outside its own walls, the walls are its refuge — and defends the storm C launches the same turn. With no room inside it retreats like a field army (§5.5.6), destroyed if surrounded, and keeps no stance at all (§5.4) \| §5.8.0 \|*
>
> *\| **D is never besieged while it stands outside.** The siege besieges the armies INSIDE. If D steps back out later while C camps at the gates, the two share the **OUTSIDE** zone and the **Phase-5 camp sweep** fights them every turn until one dies or marches away — D at Defensive ×1.20 (or a fresh valid Ambush), in the open, with no walls and no militia. **An ambush outside your own gates buys you one good battle, not a standing siege-breaker** \| §2.13.5, §5.4, §2.13.7 \|*
>
> ***Case E — the link drags the garrison out. A links its army B to the ambusher D.***
>
> *The rule that does it is the plainest one in §5.11: **a link group stands together.** D is outside the walls, D is the leader, so every member of D's group is outside the walls too — including B, whose Garrison would otherwise have kept it behind them. **Linking an army to an ambusher takes it out of the castle.** It is not a bug and it is not reversible mid-turn: unlink it, or do not link it.*
>
> *\| Who \| Where it ends up \| What it fights with \|*
>
> *\|---\|---\|---\|*
>
> *\| **D — the leader, A's own Elf in Ambush** \| Outside. Hidden until struck \| Terrain × **Ambush ×1.40**. No fortress bonus, no militia \|*
>
> *\| **B — A's OWN army, linked under D** \| **Outside, dragged out by the link** \| It **inherits D's Ambush ×1.40** (a member has no stance of its own — it obeys the leader's, §5.11) and is **hidden with it**. But the walls are gone: no fortress bonus, no militia \|*
>
> *\| **B' — an ALLY's army, linked under D instead** \| **Outside, dragged out the same way** \| **Nothing.** An ally's member under a leader in Ambush reads moving (§5.4): **no stance bonus at all**, and it is **visible** on the enemy's map. It left the walls and got nothing for it \|*
>
> ***Read the third row twice before you accept an ally into an ambush group.** Your ally's army inside your city, in Garrison, has ×1.30, the fortress bonus and the militia. Linked to your ambusher it has ×1.00, no walls and no militia, and it is the one marker on the hex the enemy can see. The ambush gains a body; your ally pays for it. It is a real tactic — a visible member is also **bait**, and the enemy cannot see what stands beside it — but it is their army you are spending, so ask them first.*
>
> *The same holds for your own army in row two, minus the penalty: B keeps the ×1.40 and the concealment, and gives up the walls. That is the whole trade — **you are converting a garrison into a second ambusher.** Against an enemy that would have stormed the walls, that is usually good; against one that would have besieged and starved you, you have just given up the thing that was keeping you alive.*
>
> *One consequence that surprises people: because the group is outside, **B is now in the besieger's zone**, so the Phase-5 camp sweep will fight it every turn the two sides stay at war on that hex (Case D's row four), and B's Ambush — like D's — is spent the first time it fights.*
>
> ***Not under siege.** If B is already **besieged**, it cannot follow D out: it leaves D's group instead (besieged — left its link group) and stays inside (§2.13.7).*
>
> ***Case F — turn the link the other way round: B holds the walls and is the LEADER, D the ambusher is the MEMBER.** (The mirror of Case E, with the gates clear — C not yet arrived.)*
>
> *Same rule, opposite result. The group stands where the **leader** stands, and the leader is inside — so **the link pulls the ambusher IN**. And a member has no stance of its own: D's Ambush is not weakened, it is **gone**. D fights at B's stance.*
>
> *\| Who \| Where it ends up \| What it fights with \|*
>
> *\|---\|---\|---\|*
>
> *\| **B — the leader, holding the walls on Garrison** \| Inside, as before \| Garrison **×1.30**, fortress bonus, militia \|*
>
> *\| **D — the Elf ambusher, now a member** \| **Inside, pulled in by the link** \| **B's Garrison ×1.30**, fortress bonus, militia. **No Ambush at all** — not ×1.40, not concealment, not the trap \|*
>
> ***This one is usually a good trade, and Case E's usually is not.** ×1.30 behind walls with the militia beside you beats ×1.40 naked in the open. So the link is a way to call your ambusher in — and the reverse link is a way to take a garrison out. Choose the leader deliberately: **the leader's zone is the group's zone, in both directions.***
>
> *Details that catch people:*
>
> *- **Not past an enemy camp, and not into a full inside.** An inward link is a door like a Garrison order: with an army at war with D camped outside — C at the gates — or with 3 armies already inside, the link is refused (Link refused, the card names which) and D stays outside. A link between armies on opposite sides of the walls forms only when both are friends of the walls' owner.*
>
> *- **A spent ambusher comes in too** — a member stands where its leader stands.*
>
> *- **An ally's army in Ambush cannot be drawn into your group at all** — your offer simply stands unanswered, and you are never told why (§5.11). With an ally, the only lever you have is asking them.*
>
> *- **Not under siege.** If B is **besieged**, a link never carries an army across the siege line: D is dropped from the group (did not join the besieged group) and stays outside (§2.13.7).*
>
> ***Meanwhile, what can A do about C camped outside its own gates?** While C merely camps — no Siege yet — A is **not besieged**, so there is no Sally to order (§2.13.7), and inside against outside a wall is never a camp clash. A Garrison never comes out to join a fight (§5.8.0), and a departure never contests the ground. A has three ways to attack C:*
>
> *- **Step outside.** Order any stance but Garrison: the army stands outside from that turn's pre-phase, beside C, and the Phase-5 camp sweep fights them (A defends — the ground is A's). Beaten, it goes back in, in Garrison. It cannot simply order its way back in while C camps there (the door is shut past a camp, above): it must win, lose, or wait for C to go.*
>
> *- **March another army in.** An army arriving on its own hex where a non-friendly army stands fights it — "Reclaiming home ground — no hex changes hands" — and the zone does not shield C.*
>
> *- **March out and back.** Leaving costs nothing while A is not besieged (a departure never storms or contests, §2.13.2b); the return march is the attack.*
>
> *Whichever way, the army that marches is the **attacker**, with no walls and no stance bonus. **Once the ring holds**, A's armies inside can no longer march out or join that attack — only their own Sally, or a relief fighting alone, is left.*
>
> ***The mirror for C, camped outside A's walls.** A move order of zero steps (a path that starts and ends on the hex you stand on) is rejected — an order must step to a neighbour — so C cannot "re-enter" the hex it is already on. Marching **out** never provokes a fight (§2.13.2b); marching **back in** the same turn is an ordinary arrival on a foreign fortified hex, i.e. a **hasty assault** exactly like C's first march: the armies outside are fought first, then the Garrison inside is stormed. It is the same result as ordering **Assault** from the camp, at the price of two hexes of marching. Only an army returning to its own or an allied fort meets nothing but what stands outside: it arrives outside and never storms. **That is the real asymmetry of a siege: the besieger decides when the storm comes; the besieged decide only whether, and when, to Sally.***

**5.8.1 Minimum Siege Force**

Before a siege can begin, the besieging army must be large enough to encircle the target. **Both** of these must hold against the target hex's population (pop):

- **Force (bodies):** soldiers ≥ floor(pop × 0.3) — at least 30% of the population in **soldiers**, to ring the walls. **A mounted trooper counts as two:** riders patrol and cut the roads over ground a footman cannot cover, so they close a bigger arc of the ring. Note the deliberate mirror: the same rider is worth **double** for closing a ring and only **65%** for climbing a wall (§3.5.1) — cavalry seals a siege, infantry storms it. Recruits raised this turn (§2.6a) already count toward the bodies gate when a stationary tick is judged. **Engines are not bodies:** machines cannot man a siege line, so a 10-soldier army hauling 40 engines counts 10 besiegers, not 50. (Their war points still count below — engines fight.) The whole **link group** counts together, leader and members alike.

- **War power:** armyWP × status \> floor(pop × 0.05) × 20 — strong enough, **at the army's current status**, to overpower the settlement's militia (the same floor(pop × 5%) × 20 WP levy that defends an assault, §5.6). Nominal WP is scaled by status (the status of the turn just ended — the check runs before any recovery); a linked group sums each army's own scaled WP. Bodies are **not** scaled: an exhausted soldier still stands in the ring.

- **A linked group is tested as one, from its leader:** the bodies and the scaled WP of every member — your own armies and allied armies linked to the leader — are summed. A member's army card reads the same group.

If **either** falls short the siege does **not** advance: no Siege Progress, a first ring is not laid (a ring laid on an earlier turn stands, and the armies inside it stay besieged — the failure only stops the counter), and the army gets a *"Siege of (c,r) failed — force too small"* report card naming the shortfall; its army card shows the siege as *stalled* (no countdown) until the force suffices. The Siege stance is **kept** on a force-only failure: the ring is pressed with no further order the turn the force suffices — reinforce, and the card says so. It is kept too when an army ordered to Siege first had to clear an enemy camp at the gates and won (its ring is laid next turn; a Siege March closes it on arrival, §5.8.0), and while a **friend's** ring stands on the hex. A signed peace, or a Siege ordered on a turn that lays no ring, clears the stance instead (§5.8.5). The army simply holds its hex — it can be re-ordered to Assault, or wait for reinforcements.

Because the bar scales with the *target's* size, large settlements become effectively assault-only: a small holding (pop 500) needs ~150 troops and \>500 WP, but a grown seat (pop 10,000) needs ~3,000 troops. The check is judged against the population the besieger can see — an army camped on a foreign settlement's hex is shown its population in its report, so the requirement is known before you commit the order.

This force requirement applies to **Siege only**. You may always *attempt* an Assault (§5.6) with any size army (a tiny force just loses to the militia and walls). Nobody inside fights a Siege unless it is **besieged** and orders **Sally** (§2.13.7) — that battle comes *before* the siege gate is even reached.

> ***▶ Example.** A 1-unit army beside a 500-pop settlement: 1 \< floor(500 × 0.3) = 150 → **Siege Failed**, nothing happens. A 200-velite army (8,600 WP) at status 60 clears both gates (200 ≥ 150, 8,600 × 0.60 = 5,160 \> 500) and the siege proceeds normally.*
>
> ***▶ Worked example — a siege from the march to the fall.** Aldoria (**A**) is at war with Gruk-Mor (**G**), whose walled town **Z** has 1,000 people: the §5.8.1 bar is **300 soldiers** (mounted counting double) and **more than 1,000 WP at status** (floor(1000 × 0.05) × 20). Sylvane (**S**) is A's ally, also at war with G.*
>
> *\| Turn \| What happens \| Rule \|*
>
> *\|---\|---\|---\|*
>
> *\| **1** \| A's Army I (200 legionnaires, status 100) reaches Z's hex in **Siege March**. Nobody is camped outside, so it makes camp and **lays siege by itself**: Siege is stored, the card names the bar (300 soldiers, \>1,000 WP). With 200 bodies it is below that bar, so the ring is **not** closed yet. Had an enemy been camped at the gates, A would have fought it first — and, winning, laid siege just the same. \| §5.8.0 \|*
>
> *\| **2** \| Pre-phase: the ring is tested. 200 bodies \< 300 → "Siege of (c,r) failed — force too small" (effect: Siege stance STAYS IN FORCE). No tick, no ring, **the stance is kept**. The same turn A transfers 150 men from its Army II, camped beside I — transfers resolve in Phase 4.5, after this check. \| §5.8.1 \|*
>
> *\| **3** \| The 150 men transferred last turn now count: 350 ≥ 300 and 350 × 67 × status 0.95 ≈ 22,000 WP \> 1,000 → the ring closes with no order filed: "Siege tightens at (c,r) — 1/4". A pays 3 status of siege upkeep and recovers none while at foreign walls. \| §5.8.1 at status, §5.10 \|*
>
> *\| **4** \| G's relief army marches onto the hex from outside. A is the **defender** of that field battle at **Siege ×0.85** (a relief landing from the sea would find the same ×0.85; a sally from Z's own garrison would not — A holds ×1.00 against it). A wins: "2/4". \| §5.5.1 \|*
>
> *\| **5** \| S's Army I arrives in siege march and lays siege beside A. Pre-phase of turn 6: both press; A's WP × status is higher, so **S's lines yield** — "Siege lines yielded at Z — Aldoria holds the ring … you remain a besieger". S keeps its Siege, pays the same 3 upkeep, and a relief would find **both** at ×0.85. A: "3/4" on turn 5, "4/4" on turn 6. \| §5.8.2 \|*
>
> *\| **7** \| Progress 5 **exceeds** the threshold of 4 — Z falls to A in the pre-phase of turn 7 (a seat would have needed one more: threshold 5). Six pressed turns from the arrival, counting the failed one. \| §5.8.3 \|*
>
> *\| (alternative 6) \| A and G sign peace instead. A's ring lifts, and A's stored Siege is **cleared** — "Siege ended by peace" — so nothing re-declares the war next turn. A stays camped; give it a stance. **Z is not free:** S, still at war with G, still presses its own Siege at the gates, and the siege goes on under S. \| §5.8.1 \|*
>
> *One card you will not see in this thread: "Siege stance dropped" (only when a Siege you ordered laid no ring — walls nobody owns, for one — or a ring that stood at the start of the turn is gone for another reason).*

**5.8.2 Siege Progress**

Army with Siege stance standing ON a foreign walled construction (camped at the gates, and meeting the §5.8.1 minimum force): siege_progress += 1 per turn, capped at the threshold + 1. **One besieging kingdom per settlement.** If two kingdoms press the same walls in the same turn, the one with the higher war power **at its current status** (the same WP × status the §5.8.1 gate reads) holds the siege and the other's siege lines yield — but the yielder **stays a besieger**: its Siege stance is kept while a friend's ring stands, it pays the siege upkeep, and a relief army finds **both** allied besiegers defending at ×0.85 — it makes no progress that turn and is told so on a *Siege Yielded* card. If the yielding kingdom acted first it has already paid its −3 upkeep and fired its engines — only its progress tick is undone. A settlement **founded this very turn** has no walls yet and cannot be besieged or assaulted at the walls. Any army sharing the ground outside the walls that is not friendly to you — a rival besieger, a relief force, a **neutral** camper — must be fought first (war is declared on it) — that battle costs the turn's progress. Only one besieger's kingdom is tracked per hex (besieged_by field). A **Sally** from inside is fought before the tick: a won Sally lifts the siege, a drawn one costs the besiegers that fought it this turn's progress and Assault, and a beaten one changes nothing — the siege ticks the same turn (§2.13.7).

**5.8.3 Thresholds**

An ordinary walled construction falls when siege_progress \> 4 (after 5 consecutive turns of successful siege; a seat after 6). Your **muster seat** (§3.7.3) falls when siege_progress \> 5 (after 6 consecutive turns).

The counter must **strictly exceed** the threshold. The turn the besieger arrives never counts: the first tick is the next processing.

**Only a walled construction can be besieged at all.** A hex with no construction, or one whose family level lists a wall of 0 (Orc Level 0–3, Generic Lv.1–4, Nomad Lv.1), cannot hold a siege: any progress against it is cleared and the besieged marker removed. Such places are taken by simply marching in and beating whoever is standing there.

> ***▶ Example — how long is a siege?** Each turn an army holds Siege stance camped on the settlement's hex, progress goes +1. An **ordinary walled construction** falls when progress exceeds 4: siege turns 1-2-3-4 build it to 4 (the defender's card: Collapse imminent — falls next turn unless a Sally breaks the ring), the 5th siege turn pushes it to 5 and **the settlement falls in that same processing** — the auto-fall check runs right after the siege tick, so five consecutive siege turns take an ordinary walled construction (six take a muster seat). A **muster seat** needs progress past 5 — six siege turns. **Progress does not survive a gap:** the moment the besieging kingdom stops holding the siege — its last Siege/Assault-stance army leaves the fort's own hex — the **Siege Lift check** (run at each turn's pre-phase) clears the counter straight back to 0 (§5.8.5).*

**5.8.4 Auto-Fall (Pre-Phase 4)**

The fall is resolved exactly as §2.7 sets out: the hex transfers to the besieger with no battle fought, and its army, standing on its new hex, is now inside its walls. The owner's armies inside surrender, every other army is expelled or routed, defender fleets put to sea, the site drops one level (§5.6.3), and opinion swings as for a decisive battle (§8.5.3).

**5.8.5 Siege Lift**

A siege is lifted — progress back to 0, both sides carded — when:

- a **Sally** wins and no army of the besieging realm is left at the gates (§2.13.7);

- a **relief** army beats the besiegers (the lift shows the next turn);

- the besieging realm stops pressing — it files a stance other than Siege or Assault, marches away, or has no soldiers left at the gates. The cards read *lapsed* when the army stayed without a Siege order, *Siege of … abandoned* / *Siege broken … withdraws* when it marched away. **Engines are not soldiers**: an army reduced to its siege train alone has no one to man the lines *or* the machines, so its siege lifts and its volley is zero, though the train itself survives as an army until soldiers rejoin it;

- the besieger makes **peace with the walls' owner** — the ring lifts and the stored Siege is cleared (*Siege ended by peace* — the war does not resume by itself);

- the walls change hands.

Peace, or a broken alliance, involving any *other* realm inside frees nobody (§2.13.7). A besieger too weak for §5.8.1 only stops the counter; its ring still holds — the walls' owner and every realm with an army inside are told each such turn (*Still besieged … the siege counter stopped*): still Garrison or Sally only, and a relief army can still lift it. A Siege ordered on a turn that lays no ring — walls nobody owns, for one — is cleared and carded: *Siege stance dropped … no ring was laid this turn; order Siege again*.

**Progress does not survive a gap.** A later attacker **never inherits an abandoned siege** — it always starts from 0, so an old two-turn siege you walked away from gives the next army nothing.

**A repelled assault** resets the counter only when no besieger is present: the assaulter's **own** siege count survives its failed storm, so a besieger that storms early and is thrown back has lost nothing but the blood, and a kingdom holding besieged_by keeps its siege whatever a third party's failed assault does.

> ***⚠ What this means — siege vs. assault.** A completed siege captures the settlement with **no battle and no casualties to you** — and your besieging army, already on the hex, stands inside its new walls — but it must stand exposed for 5 turns (6 against a muster seat). An **assault** (§5.6) is immediate and does occupy the settlement on victory, but it's bloody and the walls heavily favour the defender. Siege progress only counts down to the fall: it does not thin the garrison or weaken the walls — only siege engines batter them (§5.8.6) — so a storm at 4/4 meets the same defence as on the first day. Typical play: siege to pin the defender, then at 4/4 (Falls next turn if the ring holds) either assault if you need the place now, or simply let it fall.*
>
> ***▶ Example — a full siege, gates to fall.** Cimeria and Aquilonia are at war. Cimeria's **III ARMY**, 300 Raiders, stands two hexes from Aquilonia's **FI8** walled settlement at hex (31,17) — an ordinary holding (not a muster seat), population 800.*
>
> *- **Turns 1–2 — approach.** Cimeria orders **Siege March**: the army covers one hex per turn, so it takes two turns to close the gap. An ordinary march onto that hex would instead have been a hasty assault against the walls the moment it arrived; Siege March buys the approach without a fight.*
>
> *- **Turn 2, arrival — camped at the gates.** III ARMY stands in the settlement's **outside zone**: no walls stormed. Investing a foreign fortress would declare war on its own — moot here, the two kingdoms are already at war. Arrival stores Siege by itself (§5.4) and, the column passing the force test (below), closes the ring at once (§5.8.0) — which blocks repair_wall from turn 3.*
>
> *- **Turn 3 — the first tick, no order filed.** The ring closed on arrival because the column cleared the force gate there: against population 800, bodies need floor(800 × 0.3) = 240 soldiers, war power needs \> floor(800 × 0.05) × 20 = 800. III ARMY's 300 Raiders clear both by a wide margin (300 ≥ 240; at 48 WP each, 14,400 WP × status ≫ 800). Now siege_progress starts ticking, and the −3 status bleed begins. Camped on a foreign fortified hex, III ARMY also recovers **no status** turn to turn — the price for pressing the ring never lets up.*
>
> *- **Aquilonia's options, from turn 3.** Any army inside is besieged — it holds Garrison (×1.30 against an eventual assault) and cannot march out; it can order a **Sally** to fight III ARMY in the open and break the ring (§2.13.7); a relief force can march onto the hex from outside and fight III ARMY at its ×0.85; or Aquilonia can absorb the −3/turn and the blocked repairs and simply wait it out — until the walls fall and every Aquilonian army inside surrenders.*
>
> *- **Turns 3–6 — the clock.** Four quiet siege turns build progress to 4: Aquilonia's card reads Collapse imminent!. Nothing before turn 7 forces the issue — Aquilonia could still order a Sally from inside, or relieve from outside.*
>
> *- **Turn 7 — progress exceeds the threshold.** A fifth siege turn pushes progress to 5, past the ordinary-construction bar of \> 4.*
>
> *- **Turn 7, pre-phase — Auto-Fall.** The hex transfers to Cimeria; every Aquilonian army inside surrenders; any Aquilonian army standing outside the walls retreats or is destroyed; Aquilonia's fleets run for open water; the settlement drops one level, FI8 to FI7. The hex is Cimeria's, and **III ARMY**, standing on its new walled hex, is now inside its walls.*
>
> *- **The trap.** Had Cimeria pulled III ARMY off the hex for even one turn between 3 and 6, the Siege Lift check would have cleared progress straight back to 0 — and a second Cimerian army arriving later would start from 0 too, not from where the first left off.*
>
> ***⚠ What this means —** the siege costs five exposed turns, a running status bleed and zero blood; an assault on arrival would have been immediate but fought the walls and the garrison at full integrity. Siege March is what makes the slow road available at all here — it turned what would have been a hasty assault at the gates into a free approach.*

**5.8.6 Siege Engines**

Starvation is not the only way through a wall. **Siege engines** batter it down directly, and a breached wall is worth more than a shortened siege — it strips the defender's fortress bonus *and* the attacker's own penalty (§5.6.1).

**They only work under a siege order.** Engines batter a wall on a **siege** — the standing order, which the engine will not even accept unless your force is large enough to encircle the place — and on the **Assault stance** ordered from the gates **only if that same force test passes** (an army too small to besiege that orders Assault every turn storms bare-handed; its report carries an *Engines Idle* card naming the shortfall) (§5.8.1). They do **not** batter it when an army simply marches onto a fortified hex and fights the hasty assault that follows, nor on an origin claim, nor on a beach landing. If you want the wall down, commit to the siege.

**The train is slow, and it burns in a rout.** An army hauling engines marches **one hex per turn, whatever the terrain** — and an engine-carrying member, an ally's included, slows its whole LINK group to the same crawl (§5.11). Plan further and the Turn Processor drops the extra hexes with a 🏗 card; the Player Page won't let you plan past one hex. Retreats are exempt from the cap. And if a battle goes wrong, **engines are abandoned on every retreat**: a routed army cannot drag its train from a lost field — the engines are destroyed on the spot (a Sally that loses or draws loses its engines in the scramble back inside, too, unless no outside hex was free) (🏗 card names the count), on top of whatever the battle itself cost them. Two deliberate exemptions: a bystander **displaced** off a hex someone *else's* battle conquered never fought — it withdraws in order and **keeps its train**; and **at sea the ships do the hauling** — an embarked train sails at full fleet speed (the crawl resumes the moment it lands). An army reduced to *nothing but* its train by the battle loses everything in the rout and is destroyed. Between the crawl and the rout rule, a siege train is a commitment: it arrives slowly, and it does not come home from a defeat.

Each race builds its own, all to identical stats:

|           |                |                                                                                                                                                                                                            |
|-----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Race**  | **Engine**     | **The real machine behind the name**                                                                                                                                                                       |
| Imperial  | Onager         | The Imperial torsion catapult (twisted sinew or hair), whose single arm "kicked" on release — hence the name: *onager*, the wild ass.                                                                      |
| Barbarian | Stone-Thrower  | The traction trebuchet (Chinese in origin, adopted across the ancient world): a pivoting beam yanked by dozens of men on ropes — collective brute-force artillery, no counterweight.                       |
| Elf       | Great Ballista | The Imperial ballista: a giant torsion crossbow of remarkable precision, hurling heavy bolts or stone spheres — the most surgical of the ancient machines.                                                 |
| Dwarf     | Trebuchet      | The medieval counterweight trebuchet (12th century onward): pure engineering — tons of ballast converting gravity into 100 kg projectiles; the machine that genuinely demolished walls before gunpowder.   |
| Orc       | War Catapult   | The generic term — any arm-thrown engine, from the Greek *katapeltēs*, "shield-piercer"; here in its crudest reading: big rock, wide arc, little aim.                                                      |
| Aesir     | Valslöngva     | A real Old Norse name (≈ "slaying-sling"): the throwing engine Scandinavian sources attest at Viking sieges — essentially the traction trebuchet in its Norse incarnation.                                 |
| Nomad     | Mangonel       | The medieval catch-all for the lighter torsion/traction catapult of the campaign trail — more portable than a trebuchet, the favourite of armies on the move (the *manjaniq* of steppe and Islamic hosts). |

**Stats:** attack 1, defence 1, HP 8, **10 WP**, foot. **Cost 250g + 50 wood + 10 iron**, upkeep **3g/turn**. Wall damage **250 per engine per turn**.

There is **no Generic engine** — Generic is a construction family, not a people, and has no roster of its own.

**How the bombardment resolves:**

- **Only crewed engines fire.** Each army operates at most floor(its own soldiers ÷ 5) of its engines — the same 5-per-engine crew that gates the build also gates the volley. Crewing is **per army**: a linked ally's soldiers never man *your* machines, and engines never crew engines. Uncrewed engines are dead weight — they ride, slow the march, fight (badly) and burn in routs, but add nothing to the wall; transferring engines to an under-crewed army is legal logistics but buys no firepower. **Battle losses therefore shrink the volley**: kill the besieger's soldiers and their guns fall silent one by one — an army reduced to engines alone fires nothing at all.

- Up to **10 crewed engines are counted** per hex per turn, so the ceiling is **2,500 points of wall per turn** however many you bring — and reaching it takes **50 soldiers standing** beside the 10 machines. An eleventh engine adds nothing.

- **Once per hex per turn, full stop.** Two separate besiegers each fielding engines still knock the wall down once, not twice.

- Under **Siege stance**, the engines of every army in a LINK group (§5.11) pool into a single volley — that is what makes linked siege groups worth forming.

- **When the siege matures into a storm**, the whole attacking coalition's engines pool and **the volley lands before the walls are measured**: bombard and storm in the same turn, so that storm is fought against the wall you *just* knocked down. This is the assault a siege ends in — the army has already met the siege force, so it has already earned its engines. A **hasty** assault (a march that walks into a fortified hex), an origin claim and a beach landing bring no volley at all: the engines are with the army, but nobody unlimbers them for a fight that was not planned.

- **A repelled assault leaves the damage standing.** You lose the storm; the wall stays broken. Come back next turn against a weaker place.

- Damage floors at **0** — a wall cannot go negative, and at 0 the settlement is **breached** (fortress ×1.00, attacker penalty ×1.00) until someone repairs it (§2.11.8).

Engines are near-useless in a fight — 10 WP, attack 1 — so an engine train needs real troops around it, five soldiers to the machine. They are built, not levied (§2.12.1): anywhere on land, with **no population drawn**, so a besieger can raise its train *at the siege camp itself* — and engines built this turn already bombard in this turn's stationary siege tick or assault, since they are built in Pre-Phase 2b.

> ***▶ Example — how long to breach?** A Dwarven **FDW10** citadel (wall 18,000) against the maximum 10-engine train takes 18,000 ÷ 2,500 = **8 turns** of bombardment. Against an Imperial **FI12** (wall 1,500), the same train breaks it **in a single turn**, with room to spare. This is the whole reason the fortress curve caps at 15,000: below it, engines answer walls quickly; at the top tier they are a genuine campaign, and starvation (5–6 turns) is often the faster road.*

**5.9 Naval Combat**

A naval victory takes ships and drives off the enemy — never the harbour. Ports change hands only by land assault or amphibious landing.

**5.9.1 Fleet Power**

fleetWP = sum of (ship.xp_wp × ship.count) across all ship stacks

**5.9.2 Roll Formula**

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (±10 %)

portMod = 1.25 PER FLEET, attacker or defender, whose kingdom owns the port or is a mutual ally, liege or vassal of its owner — else 1.0.

The bonus is earned only by a fleet that \*\*began the turn in that port\*\* — attacker or defender alike. Hulls it built or received this turn ride along at the full ×1.25; a fleet that sailed in this turn, or was created this turn, fights at ×1.00.

A fleet lying in an enemy or neutral harbour — a blockader or a squatter — gets nothing; a fleet sailing into its own or an ally's port to drive one out keeps it.

Mixed sides sum per fleet, so the ledger's side factor can read between 1.0 and 1.25.

cargoMod = 0.85 if fleet is transporting an army, else 1.0

cmdMult = 1 + fleetCommander.military / 1000

raceMod = 1.05 if the fleet's kingdom is Aesir; ×1.10 if it is a Pirate kingdom (§4.3.1); else 1.0 (either side)

attRoll = attWP × status × portMod × initiative × attCmdMult × attCargoMod × attRaceMod × variance

defRoll = defWP × status × portMod × defCmdMult × defCargoMod × defRaceMod × variance

huntWP(side) = Σ per fleet: fleetWP × status × cmdMult × cargoMod × raceMod × portMod (no initiative, no variance)

Pirate Hunt attacks iff huntWP(hunter side) \> huntWP(target kingdom side) (§2.14.9)

**5.9.3 Casualties**

Same outcome threshold (ratio \> 1.2). Both sides use identical loss formula:

**Attacker wins:** attLoss = 0.10/ratio, defLoss = min(0.60, max(0.12 + 0.18 × ln(ratio) \[cap 0.50\], 0.12 × ratio)) up to 5:1, then 0.60 + 0.40 × (ratio − 5) / 5 — a total loss at 10:1 **Draw:** both 0.06 + rand×0.06 (6–12%), same value for both **Defender wins:** defLoss = 0.10/ratio, attLoss as the attacker-wins defLoss above

**The sea uses the field battle's curve up to 5:1** (§5.5.3) — the log curve, the damage floor and its **60%** cap — **and then a shorter extreme-odds ramp**: from 5:1 the loss climbs in a straight line to a **total loss at 10:1** (6:1 → 68% · 7:1 → 76% · 8:1 → 84% · 9:1 → 92% · **10:1 and beyond → no hull survives**). The armour dissolve follows the same 5:1 → 10:1 schedule: up to 5:1 a hull's build cost protects it, beyond 5:1 that protection is stripped in step with the rising loss. A six-hull squadron of the heaviest warships (Imperial Galleys) loses 2 at 5:1, 3 at 7:1, 5 at 9:1 and all six at 10:1. Up to 5:1 a beaten fleet of several hulls sails home as a fighting remnant (a lone hull still pays its minimum one); beyond it, the odds alone can sink it.

**A fleet is annihilated by the odds at 10:1.** Below 10:1 the loss runs through the armour distribution, and a beaten fleet is destroyed outright when the rounding takes its last hulls — a squadron of two or three cheap hulls can go down entirely from about 8:1, a single hull always pays its minimum one — or when it has **nowhere to withdraw to** (no reachable free water, or bottled up in a port it cannot leave), the sea's version of the land rule that only a surrounded army is destroyed. **At 10:1 or worse the ramp reaches a total loss and the fleet goes down whether or not it had somewhere to run**. Fleet status counts toward the ratio, so worn crews reach 10:1 long before the hull count does.

**But the loser always pays at least one hull — per fleet.** If the armour distribution rounds every stack's loss down to zero, the single closest-to-losing stack still gives up one ship.

Naval winners bleed exactly like field winners: the winner's base loss is 0.10/ratio (vs 0.15/ratio at the walls). There is **no fixed minimum** — at high win ratios the winner's loss simply trends toward zero.

> *Which ships die is decided by what they cost, not by their DEF. Each hull's protection is its*
>
> *gold-equivalent price — gold at face value, iron at ×12, wood at ×5 — so an expensive warship*
>
> *loses a smaller share of its number than a cheap one in the same battle. Food buys no protection:*
>
> *rations are not armour. Veteran hulls count as proportionally pricier and so survive better.*
>
> *A hull is measured against a fixed scale, not against the rest of its own fleet — a squadron of*
>
> *one hull type is not uniformly protected.*
>
> ***▶ Example — fight at home, never while loaded.** Two 500-WP fleets clash. If the defender sits in its own **port** (×1.25, §5.9.2) it rolls from 625 while the attacker rolls from 500 — the attacker now needs \> 750 effective to win an engagement that would otherwise be even. Worse, a fleet **carrying an army** takes ×0.85 (cargoMod): a loaded 500-WP fleet rolls only 425, and if it loses, the embarked army drowns with it (§2.14.6). Escort your transports with empty warfleets, and try to force enemy fleets to fight you at your ports rather than theirs. The bonus follows the harbour, not the role — attacker or defender — but only for a fleet that began the turn in that port: one sent in to drive out an intruder fights at ×1.00, like the intruder (§5.9.2).*

**5.9.4 Transported Army Fate**

If the transporting fleet is sunk, the army aboard is destroyed with it — no survivors (§2.14.6).

**5.9.5 Defeat and Retreat**

A defeated fleet that still has ships afloat falls back to the **nearest refuge within 3 hexes**. A refuge that is a **port** docks the fleet there — it counts as in port for raids, embarking and harbour rules from that moment. In a coalition fight **every losing fleet retreats individually** — each finds its own refuge, exactly as land armies do (§5.5.6). **On a draw the attackers withdraw the same way and the defenders hold the hex** — a drawn attacker that finds no refuge sinks exactly as a beaten one would, and a draw yields no prizes to anyone. **Who fights on the defending side is automatic**, by the land rule (§5.11): every fleet on the hex at war with the attacker joins the defence unless it is at war with a defender, and fleets linked under the defending flagship always join, counting as defenders from the start; a fleet at peace with the attacker is a bystander and takes neither losses nor part. **One card per battle.** Your report shows a **single** battle card per naval engagement, titled with every fleet of yours that fought — *"Naval victory (Fleets I + II)"* — and listing each fleet's own ships beneath the side totals (losses are the kingdom's total for that fight). If one of your fleets sank while another pulled back, the card says which. Two fleets of yours in one fight are a squadron, not a coalition; the word *coalition* appears only when an **ally's** fleet stood with yours.

The search runs as a beaten army's does. First comes the hex the fleet **came from** on this hop (primary fleet only — co-belligerents start from their own hex). Otherwise the fleet takes the **nearest** usable hex up to **3 hexes** away, moving only through **open sea that holds no fleet at war with you** — a ring of enemy fleets still traps it, so a blockade or a bottled-up harbour keeps its teeth, while your own full stacks do not. Among hexes at the same distance it prefers:

1\. a **port of your own**;

2\. an **allied port** (mutual alliance, your liege, or one of your vassals);

3\. **open sea**;

4\. a **neutral port**.

A candidate is usable only if **no fleet at war with you** sits there, **it is not owned by a kingdom at war with you** (an enemy port — the rule that keeps a beaten army off enemy ground), **and the friendly stack has room** — the 3-fleet cap applies to retreats too, so a rout can never overfill a hex. Comrades, and merely **neutral** fleets, are refuge rather than a wall: a beaten fleet may rally onto a shared hex while a slot is free (§2.14.2).

If **no candidate qualifies, the fleet sinks where it fought**: every hull is lost, an embarked army **goes down with it** — no survivors (§5.9.4) — and its commander tests for death at 100% losses; the **fleet's own commander** has already rolled on the battle's hull losses like any army commander. Hulls lost this way are not prizes: only the hulls lost in the fight itself roll for capture (§2.13.12).

A forced flight is still sailing: the retreat **charges fleet status** for the entered hex like any move (the fatigue table's *"Retreat, or flee a fallen port"* row, §5.10.6). A fleet whose **port falls** to a storm or a siege does not use this search: it runs for the nearest free open-water hex it can reach through water — never a port, friendly or not — and is **destroyed at its moorings** if none is in reach (§2.7).

**5.10 Army Status (Readiness)**

Every army carries a **STATUS** value from **10% to 100%** — its readiness to march and fight. A rested army sits at 100%. The Player Page shows it on each army card (STATUS: 77%) and previews the projected loss of any planned route (Arrive at ~N%).

Status is the game's exhaustion clock. Nothing about an army's roster changes when it tires — the same regiments, the same War Points on paper — but a spent column arrives slower, hits softer, and moves last. Every point is spent by *doing* and bought back only by *resting*, so status is the price tag on tempo: every hex you march, every fight you pick, and every turn you keep a siege ring closed is paid for in readiness.

**5.10.1 What Status Does**

Status has exactly two mechanical effects, and both bite hard:

- **It multiplies battle power.** In every battle — field, sally, assault, amphibious, and the militia contest of a seizure — each army's War Points are multiplied by its status before the roll. A 10,000-WP army at 50% fights like a 5,000-WP one. Rankings and spy estimates use **raw** WP; battles and the siege capacity gate (§5.8.1) use WP **at status**.

- **It buys initiative.** Movement, sieges/assaults and fleet moves all resolve in **status order, highest first**, exact values (§2.13.1): a 99% army marches before a 98% one.

Two things that are *not* effects: status never changes what an army costs to feed, and it is **never visible to your enemies** — not on the map, not in spy reports. You are guessing at their exhaustion exactly as they are guessing at yours.

**Your report tells you why.** Every turn your own report carries a **Readiness Report** — own-report-only, never showing another kingdom's units — in two cards: the **armies** close Phase 5 and the **fleets** close Phase 6, each where its own fighting ended. Together they list each army and fleet whose status changed this turn, itemising every cause in the order it happened, next to the resulting battle-power multiplier. The causes, as the card words them:

- **Moving:** *marched N hexes (terrain)*, *fell back N hexes (terrain)* after a lost battle or a withdrawal, *pulled back inside the walls* for a lost or drawn sally's survivors, *sailed N hexes (coastal / high sea)*.

- **Boarding and landing:** *embarked*, *landed*, *beach pickup* (the fleet's cost for lifting troops off a beach).

- **Fighting:** *battle won / battle lost / battle drawn at (col,row)*. A seizure the populace throws back — draw or defeat — reads *battle lost*, matching the *Army Repelled* card.

- **Standing duty:** *siege upkeep*, *blockade*, *hunting* (a pirate fleet on Hunt), *raiding* (a fleet that raided this turn).

- **Recovering:** *rested* (an army, or a fleet docked in any port whose owner is not at war with you — a neutral's port included), *rode at anchor* (a fleet resting away from any port). A fleet docked in an enemy port recovers nothing.

- **Reorganising:** *levelled to the group's weakest* (a LINK group's members are levelled down to its weakest member — on joining, and again at the end of any turn their statuses drift apart), *reinforced by fresh recruits*, *reinforced by new hulls*, *absorbed transferred troops*.

Battle lines name the hex the fight was on — *battle lost at (20,28) −22* — and every battle is its own line: two battles on two hexes are two lines, and so are two battles on the **same** hex — an assault at 92% followed by a counter-attack at 84% reads *battle won at (24,34) −8 · battle won at (24,34) −3*, never one summed −11.

**The floor is reported too.** Status never drops below 10%, but a unit at the floor still pays for what it does — it simply has nothing left to lose. The card says so instead of staying silent: a fleet that sails three hexes at 10% reads *Fleet V 10 → 10 · sailed 3 hexes (coastal) −0 (at the 10% floor)*, and a march that runs into the floor counts every hex and names it — *Army II 12 → 10 · marched 2 hexes (plains) −2 (at the 10% floor)*.

A unit whose status ends below half (50%) also gets a "stand still a turn to recover" hint. A quiet turn — nothing paid, nothing recovered — carries no card at all.

**5.10.2 Every Action That Moves Status**

Every rule that moves an army's status, in one place. Costs are in status **points** (status is a 10–100 scale, so a point is a percentage point).

|                                                                                                    |                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Action**                                                                                         | **Status change**               | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **March into a hex**                                                                               | **−5 to −18** per hex           | By race × terrain — see §5.10.3. Charged per hex *entered*, so doubling back over a hex pays for it twice. Foot and mounted pay the same rate.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Retreat or expulsion**                                                                           | **−(terrain) × hexes fled**     | A forced march is still a march. Charged at the destination hex's terrain, multiplied by the distance fled. The Readiness Report reads *"fell back N hex"* — or *"pulled back inside the walls"* for a lost or drawn Sally's survivors. An army beaten outside its own walls goes inside without moving, so it has no such line.                                                                                                                                                                                                                                             |
| **Embark** (board a fleet)                                                                         | **−5**                          | A flat cost, paid once on boarding — the same whether boarding at a port or picked up on a beach (§2.14.6). Status then freezes for the voyage.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Disembark** (*any* landing)                                                                      | **−20**                         | A flat cost that **replaces** the terrain charge — every beach costs the same (a **mountain** coast cannot be landed on at all — cliff, not shore). An **opposed** landing pays its battle cost on top (§5.10.4); a landing that is **blocked** by a full stack pays nothing; a landing that fights and is **repelled** (or draws) re-boards without paying the −20 but **does** pay the battle's own cost (§5.10.4) — on foreign walls it does not re-board: the survivors dig in outside and pay the −20 too (§5.7.2); the fight was real even if the beach was not taken. |
| **Aboard a fleet (at sea)**                                                                        | **frozen**                      | A carried army neither tires nor rests. Its status is exactly what it was when it embarked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Win a battle**                                                                                   | **−3 to −15**                   | Scaled by how hard it was fought — see §5.10.4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Lose a battle**                                                                                  | **−15 to −30**                  | Also ratio-scaled; a crushed loser pays the full −30.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Draw a battle**                                                                                  | **−15** both sides              | A stalemate is the most expensive result per point of gain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Militia seizure contest**                                                                        | same as a battle                | The populace is not an army: **militia pays nothing**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Hold Siege stance**                                                                              | **−3 per turn**                 | Paid only while the ring is actually being pressed (an army too small to invest the settlement pays nothing — it never gets that far). Every member of a linked group on siege duty pays it.                                                                                                                                                                                                                                                                                                                                                                                 |
| \**Hold Siege* or Assault *stance*\*                                                               | **no recovery**                 | Neither ever rests: a besieger or a stormer only recovers after standing down. **Assault pays no −3** — it costs the battle, not the bleed. A storm that **takes** the walls also pays the hex's terrain entry, as a march would — the army moved inside.                                                                                                                                                                                                                                                                                                                    |
| **Fight this turn** (any battle, any phase, attacker or defender — a landing on your hex included) | no recovery this turn           | Rest is granted after the last battle of the turn, only to a unit nobody touched. The fight itself charges its own cost as normal.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Camp on a foreign fortified hex** (any stance)                                                   | **no recovery**                 | Extends "a besieger only recovers after standing down" to anyone camped at foreign walls — a Siege March army or a repelled assaulter dug in at the gates rests nothing while it holds that ground. An army on its own, or an allied, fortified hex still rests normally.                                                                                                                                                                                                                                                                                                    |
| **Rest** (no move order)                                                                           | **+33**                         | Capped at 100. See §5.10.5 for what disqualifies an army.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Recruit new units**                                                                              | **blends toward 100**           | Weighted by headcount — see §5.10.5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Receive a unit transfer**                                                                        | **target blends**               | The arriving troops drag the receiving army's status toward theirs (headcount-weighted); the *source* army's status is unchanged (§5.10.5).                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Muster a new army**                                                                              | **starts at 100**               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Belong to a LINK group**                                                                         | **levels to the group minimum** | Applied every turn, *after* resting (§5.11).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Floor**                                                                                          | **never below 10**              | Even a spent army fights at one-tenth strength — never zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**▶ Example — what a landing costs, situation by situation.** The −20 is flat and paid only when the army actually lands; a battle fought on the beach adds its §5.10.4 cost on top; a landing that never happens pays nothing.

|                                                                                                                 |                                                                                              |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Landing situation (§2.14.6)**                                                                                 | **Status paid by the army**                                                                  |
| Own/allied ground, clear — or alongside friends (co-location)                                                   | **−20**                                                                                      |
| Own/allied ground, hex already **full** (3 armies)                                                              | **0** — stays aboard                                                                         |
| Own/allied ground, **enemy army** there — beach engagement won                                                  | **−20** + winner's battle cost (max(3, min(15, 15 − 3(r−1))))                                |
| — beach engagement lost or drawn (re-boards)                                                                    | **0** landing cost + the loser's / draw battle cost (§5.10.4)                                |
| Enemy **walled** hex — assault from the beach won                                                               | **−20** + winner's battle cost (the flat landing cost replaces the terrain charge even here) |
| — beach fight at the gates lost or drawn, or assault repelled: survivor holds a **beachhead** outside the walls | **−20** + the loser's or draw battle cost (§5.10.4)                                          |
| Enemy/unowned open land, army or militia — won                                                                  | **−20** + winner's battle cost                                                               |
| — repelled (re-boards)                                                                                          | **0** landing cost + the loser's battle cost (§5.10.4)                                       |
| Landing refused because the army **embarked this turn**                                                         | **0**                                                                                        |
| Boarding (port or beach)                                                                                        | **−5** once; then **frozen** aboard                                                          |
| Fleet doing a **beach pickup**                                                                                  | fleet **−15**, and its move is spent                                                         |

**5.10.3 Marching Cost by Race and Terrain**

The cost of entering one hex, by the marching army's race and the destination terrain. Each race's homeland is its bargain, and its opposite is its ruin: a Dwarf crosses a mountain for 10 where everyone else pays 18 but flounders through forest at 12; an Orc wades a swamp at 9 that costs everyone else 15; the Aesir buy hills and forest cheaply and pay 16 for a desert nobody sent them to.

|             |              |           |         |               |         |           |           |
|-------------|--------------|-----------|---------|---------------|---------|-----------|-----------|
| **Terrain** | **Imperial** | **Nomad** | **Elf** | **Barbarian** | **Orc** | **Dwarf** | **Aesir** |
| Plains      | 5            | 5         | 5       | 5             | 5       | 6         | 5         |
| Hills       | 10           | 9         | 10      | 8             | 10      | 8         | 9         |
| Forest      | 8            | 8         | 6       | 8             | 10      | 12        | 7         |
| Desert      | 14           | 10        | 14      | 14            | 14      | 14        | 16        |
| Swamp       | 15           | 15        | 15      | 15            | 9       | 15        | 15        |
| Mountain    | 18           | 18        | 18      | 16            | 18      | 10        | 17        |

Mounted and foot pay the same **per hex** — but mounted armies have 90 MP to foot's 60, so they cover more hexes per turn and therefore tire *faster per turn*. Speed is bought with readiness, not given free.

This table prices **marching only**. A **landing** ignores terrain entirely and pays the flat **−20** of §5.10.2 — an amphibious army pays for the boats and the surf, not for the ground it steps onto.

**5.10.4 Battle Cost by Ratio**

A battle's cost is set by how lopsided it was. The **ratio** is the winner's combat roll ÷ the loser's roll (the same number that sets spoils tiers, §2.13.11):

- **Winner** pays 15 − 3 × (ratio − 1), clamped to **3–15**.

- **Loser** pays **30 − the winner's cost** — a hard fight exhausts both sides about equally. A **crushed** loser (ratio ≥ 5) pays the full **30** regardless.

- **Draws** cost both sides a flat **15**.

|                            |                 |                |
|----------------------------|-----------------|----------------|
| **Ratio (winner ÷ loser)** | **Winner pays** | **Loser pays** |
| ~1.0 — knife-edge win      | −15             | −15            |
| 2.0 — clear win            | −12             | −18            |
| 3.0 — decisive             | −9              | −21            |
| 4.0 — one-sided            | −6              | −24            |
| 4.9 — near-rout            | −3              | −27            |
| **≥ 5.0 — crushed**        | **−3**          | **−30**        |
| Draw (any ratio)           | −15             | −15            |

The shape is deliberate: **a walkover is nearly free, a close fight costs the winner almost as much as the loser.** Winning ugly against a real opponent leaves you at roughly half readiness and last in next turn's initiative — which is often the moment their ally marches.

**5.10.5 Recovering and Reinforcing**

**Resting.** An army that submits **no move order** "recovers instead of moving": **+33 points** (capped at 100) at the **end of the turn's fighting** (after Phase 6), and **only if nobody attacked it** — an idle army attacked that turn defends at its real, un-rested status and rests nothing. The disqualifiers are listed in the §5.10.2 table: a move order (its own or its link leader's — a landing, embark or retreat counts), Siege or Assault stance, any fight this turn, or standing on a foreign fortified hex whatever its stance. An **embarked** army rests nothing — its status stays frozen until it lands: the *carrier fleet* recovers at anchor, the troops in its hold do not.

Roughly: **two turns of marching on easy ground per turn of rest.** In hills or mountains the ratio inverts, and a mountain crossing can cost more than a full turn's rest can restore.

**Fresh blood restores spirit.** Reinforcement genuinely refreshes an army, because status blends by weight rather than being carried by the veterans:

- **New armies** muster at **100**.

- **Recruits** arrive at **100** and blend in **weighted by headcount** — 50 fresh troops joining 50 exhausted ones at 40% yield (40×50 + 100×50) ÷ 100 = **70%**. The blend lands in Pre-Phase 2b — before the standing sieges, sallies and assaults of Pre-Phase 3 and before the Phase-5 rest — so a garrison reinforced this turn is stormed, or sallies, at the blended figure.

- **Unit transfers** carry the **source army's** status into the target and blend the same way; the source army keeps its own.

This is the cheapest readiness in the game: a small veteran core topped up with recruits at the muster seat comes back to the front far fresher than the same army resting in place.

**5.10.6 Fleet Fatigue at Sea**

Fleets run the identical framework, with the sea supplying the terrain. Sailing costs status for every hex **entered**, classed by the hex you enter:

|                                                 |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fleet action**                                | **Status change**             | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Sail a coastal hex**                          | **−3** (Aesir **−2**)         | The hex is a port, or touches at least one land hex.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Sail a high-seas hex**                        | **−6** (Aesir **−4**)         | Open water on every side — the map's edge counts as ocean.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Beach pickup** (load an army over open water) | **−15**                       | Paid once, when the fleet takes an army aboard via embark_army with beach:true (§2.14.6) — on top of the army's own −5 boarding cost. Consumes the fleet's move for the turn: no sailing until the following turn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Naval battle**                                | same as land (§5.10.4)        | Each fleet's power is multiplied by its own status; the Aesir ×1.05 battle bonus stacks on top.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Retreat, or flee a fallen port**              | **−(entered hex class)**      | Forced movement charges like an army's retreat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Rest docked at a port**                       | **+33**                       | Own, allied or neutral port, and only with no move order. A fleet that **fought a port clash** this turn does not rest (the naval twin of the army rule above) — an enemy fleet sharing your harbour is fought *before* the crews stand down.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Anchored at sea**                             | **+16**                       | A fleet that simply stands still anywhere other than a friendly dock rides at anchor and recovers **half a shore leave**, open ocean included. Granted at the **end of the turn's fighting**, only if the fleet neither sailed nor fought — a fleet attacked at anchor fights at its real status and rests nothing that turn. Disqualified by anything that spends the fleet's turn, which is **not** the same as filing an order: a move that **actually sailed** (its own or its flagship's — an order the engine refuses, at a full stack say, leaves the fleet where it was and it rests like any idle fleet, paid at the end of the phase), a port clash fought this turn, blockade stance, **a forced retreat** (being chased off a hex is not standing still — it pays the sail cost and earns no rest for it), or **a beach pickup** (§2.14.6 — the pickup consumes the turn). |
| \**Docked at an* enemy *port*\*                 | **0**                         | An empty enemy port is a legal destination (§2.14.2) — but crews get no shore leave in a hostile harbour, and **no anchor rest either**: squatting in an enemy port is deliberately worse than open water.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Blockade stance**                             | **−2 per turn**               | And no recovery while on station.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Raid**                                        | **−3 in a turn it plunders**  | Paid **once** in any turn the fleet plunders a port (§2.14.3) — whatever it takes, 0g included, and however many ports the voyage plunders. Every fleet of a raiding link group pays it. A refused raid costs nothing, nor does a raid **under sail** beaten or held to a draw in the harbour: it never plunders. A raid **at anchor** plunders before its harbour fight, so it always pays. The fight charges its own battle cost and sailing is charged on top; the raided port gives no rest (*Docked at an enemy port*, above).                                                                                                                                                                                                                                                                                                                                                    |
| **Hunt stance** (pirates only)                  | **−2 per turn**               | And no recovery while hunting (§2.14.9).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Build ships**                                 | **blends toward 100**         | New hulls launch at 100 and blend **by ship count**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Ship transfer**                               | **target blends**             | The receiving fleet's status blends toward the incoming ships' (ship-count-weighted); the source fleet is unchanged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Captured prize ships**                        | **adopt the captor's status** | Prizes join the fleet that took them; they change nothing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Floor**                                       | **never below 10**            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

The Player Page's *Planned Route* box previews these costs hop by hop. A hex you cannot see (fog) is priced as **open water** — the worst case — and labelled *assumed open water*. The engine classifies the real hex when the fleet sails, so an unknown hex that turns out to be coastal costs less than previewed, never more.

**Every naval battle card names both sides.** The title carries the enemy fleet number(s) — *"Vanaheim (F III) driven from the sea"* — and when more than one fleet fought on your side the card ends with a **Your side:** roster listing each of them, allies included, with their surviving hulls: you shared a battle line, you see the ships. A lone fleet's card shows no roster — there is nothing to share.

A carried army neither changes the fleet's rate nor rests aboard — its own status stays frozen until it lands (§5.10.2).

> ***⚠ What this means —** Offensives have a tempo: roughly two turns of marching to one of rest on easy ground, worse in hills and mountains. An attacker who force-marches through a mountain pass arrives at two-thirds strength or less against a rested defender who may also hold a home-terrain battle bonus — defended ground is now defended twice over. Watch the Arrive at ~N% line in the route planner, and rest your armies before the border, not at it.*

**5.11 Army Co-location & LINK Groups**

**Raise-and-link works in one turn.** Links are formed *after* the turn's muster, so an army raised this turn can be linked — and marched as a group — in the same orders file. **Every refused link is carded with its reason** ("does not exist yet", "not on the same hex", "already linked", "aboard a fleet", "group full", "not a mutual ally"); a link that does not appear in your report was refused, never lost. One ordering note: an army that both embarks and is linked in the same turn embarks first and the link is refused (linked armies cannot board — §2.14.6).

**Friends may share a hex.** Up to **3 armies** may stand on one hex, in any friendly mix: your own armies, and armies of **mutual allies** (or vassal/liege). Co-location is automatic on **your own or allied ground**. On enemy or neutral ground a friend does not shield the hex from you (§2.13.3): if your whole group fits, you go in as if it were not there and it stays beside you as a bystander. Enemies on a hex still mean battle, never a lasting camp: armies that go to war while camped together fight at the start of the next Phase 5 (the camp sweep, §2.13). The one lasting camp of enemies is inside a besieged city, where the loser cannot leave (§2.13.7). The cap of 3 holds on **every** path onto an *open* hex: marching, disembarking, retreating, even mustering a new army — a full hex turns them all away. **Every army on the hex counts toward it, whatever its banner**: an army at peace with you takes a place just like a friend, so a group that cannot fit whole is refused whole with the usual *hex full* card, instead of walking in and leaving a member behind; the Player Page's warnings count every army it can see there too. **An army that marches onto a hex whose zone holds an army at war with it fights that army — enemies take no room against an attack**: the march is never refused as *hex full* because of them and the page's move warning stays silent; raises and splits still count every army. Before a foreign city's walls, **an army at war with you camped outside them is fought at the gates, never counted as room**, whoever else is camped there. A linked group **moving in behind its leader after a battle** obeys it too: a member that would overfill the hex (an allied army may already be camped there) stays where it stood and leaves the group. If the group is halted before a hex with no room, a member from another realm is carded too: *"Your army is linked under X, and the group halted: …"*. **On a hex with a walled construction the cap is per zone**, not per hex: up to **3 inside the walls and 3 outside** (up to 6 armies present in total), because a besieging camp and a garrison occupy different ground — see §5.8.0. A beaten army may also retreat onto a friendly-held hex with room (§5.5.6). A move ordered into a currently-full hex is still legal: if the occupants march out first (initiative order decides), you slot in; if not, your column halts in front of it. This is settled **live, round by round, not by reservation** (§2.13.1): a camp slot — outside the walls or on open ground alike — goes to whichever mover's hop actually arrives first, and is never held open for a mover still queued for a later round.

**Co-located armies defend together — automatically.** When an enemy attacks the hex, every army standing in the attacked zone of the hex (on walls, a Garrison defends only the storm, §5.8.0) that is **at war with the attacker** — the defender's own, its allies' and total strangers' alike (as at sea) — joins the defence as one force, **except an army at war with the defender or with another army already defending, which stands aside rather than fight beside its own enemy** (a member of the defender's LINK group joins even at peace with the attacker, who then declares war on it, and counts as defending from the start — **the attacker's own ally, vassal or liege included, whose alliance breaks** — §5.11; only the **primary** defender's group is pulled in this way, and a co-defender's own link members join only if they are themselves at war with the attacker): each contributes its own war points, terrain bonus, stance and commander; casualties fall on each participant in proportion to its size; every participant logs its own battle card, opinion swing and win/loss. A defensive victory's battle spoils are **split between the defending kingdoms in proportion to their war-point share**. An allied army **at peace** with the attacker and **outside the defender's link group** stands aside on open ground — nobody is dragged into a war by geography (nobody inside walls is a bystander, §5.6); a link is another matter (above). **A kingdom never fights on both sides of one battle**: if one of your armies **fights on the attacking side** — as a member of the attacker's link group, say — your army standing in the defence stands aside, does not defend, and is carded *"held back"*. Your attacking army still fights, and its blows are your kingdom's: you enter the war against the defender (the link is consent) — full rules and a worked example in §5.11.1. At a friend's walls, a member leaves a group that turns on that friend or its allies there (§5.11.1 rule 3). **Co-located armies attack together too** — your armies in the attacked zone, and an ally already at war with the whole defending side, join the attack; never a besieged army (§2.13.5).

**One battle, one card — and every army named, yours and theirs.** When two (or three) of your armies fight the same battle — linked, or co-located defenders joining automatically — you receive **one** battle card, not one per army. Land cards follow the same convention as fleet cards: the title carries your army label — *"(Army II)"*, or *"(Armies II + III)"* for a group — **and** the enemy's number(s): *"Victory on forest at (14,22) against Vanaheim (A III)! (Armies II + III)"* — the hex sits in the title, so army and place read together. The losses line is the group's total, the composition pools **every** army on your side, and when more than one army stood on your side the card adds a *"Your side:"* roster — each army, allies included, with its surviving units. Each side's counter on the battle card names the armies that met (§5.12), as the naval card names the fleets.

**LINK — marching and fighting as one, by choice.** A standing order welds up to 3 co-located armies into a **link group**:

- **Formation.** The **LINK LEADER** issues the order from its army card, picking co-located armies. Your own armies join **the same turn**, no consent needed. An **allied** army needs its owner's acceptance: the proposal becomes a pending offer (carded, shown on the ally's army card) accepted in a later turn — or, if you coordinate and both submit in the same turn (proposal + LINK ACCEPT), the group forms at once. An offer lapses (carded) if the armies part before acceptance. On a **fortified hex the group must stand together**, and the test is whether they would still stand apart **once linked**. A member adopts its leader's zone, so two armies on opposite sides of the walls may link when **both are friends of the fort's owner**: the group then stands on the leader's side (§5.8.0 Cases E and F). An **inward** link (leader inside) is refused while an army at war with the joining army is camped outside, or when the inside is full — it is a door like a Garrison order. Any other straddle is refused, on both the proposal and the acceptance (*Link refused — … stand on opposite sides of the walls*). A link at a friend's walls under a leader hostile to them is refused too (§5.11.1 rule 3). If diplomacy later re-derives a member to the other side of the walls, it is automatically released from the group (carded). An army in Ambush is never drawn into an ally's group (*Links and Ambush*, below). **A formed group grows the same way** — from the leader's card, any army standing on its hex can be added until the group holds 3 (leader included; a link already queued this turn counts); the card of an unlinked army sharing a leader's hex points you to that leader's card. Fleets are identical, from the flagship's card (§2.14.7).

- **Mutual proposals don't link.** The engine matches an ACCEPT to a specific proposal: if both players propose to each other instead of one proposing and the other accepting, that's two pending offers, and each side waits believing it is done. Agree in advance who leads — the proposer is the leader.

- **Links and Ambush**. **An army in Ambush may lead a link, but Ambush covers only its own kingdom's armies.** An Elf army in forest or a Dwarf army in mountain holding Ambush may add its own armies or propose a link to an ally's army (accepted the same turn or later), and it keeps its Ambush. Your own members stay hidden with it and fight at ×1.40. An **allied** member is **visible** on every other kingdom's map and fights with **no stance bonus** — not even Defensive — and its marker shows nothing that points to the hidden leader; the page warns you when you add or propose an ally from an army in Ambush. **An ally cannot draw an army in Ambush into its group:** its proposal stands as an ordinary pending offer that cannot be accepted while the Ambush lasts — the proposer is **not told why**, while you are told. If that ally already had an offer standing on your army, it is untouched and your card says so. **An offer made before the Ambush waits:** ✓ Accept is greyed while the army is in Ambush, an accept filed anyway is refused and the offer kept, and it can be taken the turn the Ambush ends (order another stance beside the accept). Linking an army in Ambush as a member of your own kingdom's group is allowed and ends its Ambush. "In Ambush" means the stance the army holds this turn: a stance filed this turn counts, and another stance or a march ends it. **It holds on a turn you file no orders**: the stored Ambush keeps working, your own members stay hidden with it and an allied member stays visible — a missed turn costs you nothing here.

- **Command.** The link is **persistent** until broken. The leader's move and stance orders drive the whole group; a slave's own move and stance orders are void — its one prerogative is **UNLINK** (same-turn effect: you can unlink and move in the same order sheet). The leader can release individual members or dissolve the group; the leader's death or disbandment dissolves it. **Nor does a link outlive the alliance it was built on**: if the member's kingdom and the leader's go to war, end their mutual alliance, or the vassal's oath of fealty is renounced, the member is released at the **end of that turn** — after diplomacy resolves — and both sides are carded with the reason. A live **vassal bond** keeps the link whatever the stance field says that turn (a vassal setting peace toward its liege does not scatter the group). The test is **leader ↔ member** only: two members of the same group who fall out with each other stay linked and fight side by side under the leader's orders until one unlinks. Slaves still **recruit and receive/send unit transfers** normally. **A queued march and a link never coexist on the page**: you cannot link an army that has a path planned, and you cannot take back a queued UNLINK — nor a queued *release* of a member from the leader's card — while the freed army still holds a path. Clear the path first; the engine would discard that march anyway, and the collapsed box would hide it from you. **A formed group shares its members with everyone in it:** your report lists each member's units, readiness, stance and commander — allies included, in both directions — so the group pace on your card is the real one, not a cautious guess. A *proposal* shares nothing until it is accepted, and the turn a member leaves it drops out of the roster. The same applies from the leader's side: an army whose planned march is longer than the pace a new, slower member would set must shorten the route before linking.

- **As fast, and as fresh, as its weakest man.** Status levels to the group **minimum** — at formation and again every turn (a resting group still recovers, each army by its own rules, *then* levels down to the minimum). Movement pace is the **lowest MP** in the group: one foot regiment slows the whole column to 60mp.

- **One force in battle — both ways.** The group attacks as a single combined force under the leader's orders and defends as one when struck. The link **is** consent: a linked ally at peace with the attacker fights anyway — and thereby **enters the war** — unless its own kingdom also fights on the attacking side, in which case it is held back (co-located defence, above). The link is consent **on both sides**: a member of the attacking group follows its leader into a fight against its own ally (the worked example below, Zingara), and a member of the defending group that is the attacker's own ally, vassal or liege fights beside its leader just the same (Ophir) — either way that alliance breaks — except at that ally's own walls, where the member leaves the group instead (§5.11.1 rule 3). Attacking-side spoils split by war-point share, exactly like the defensive split.

- **Sieges and assaults combine.** A linked group in siege stance meets the siege gate together (§5.8.1) and pools its engines' volley — two armies each too small to invest a settlement can hold the ring together. A linked assault storms the walls as one; on victory the group enters the settlement, still linked (a member friendly to the owner has already left it, §5.11.1 rule 3). Every member on siege duty pays the −3 status bleed.

- **Arriving beside an enemy — the arrival clash**. Members step onto the leader's hex behind it, on every step. If a member — or the leader — then stands in the same zone as an army **already there** that it is **at war with**, it **attacks on arrival**, before the march goes on: the army already there defends — even when both are friends of the ground's owner — and only the arriving armies at war with it fight — a leader at peace with that army stays out and declares nothing. An arriving army fights **one battle per step**: any other enemy in that zone that did not defend in it is fought in the next camp sweep, if they are still camped together. Armies already standing in that zone join the arriving attackers — the attacking kingdom's own, and an ally's only when already at war with every kingdom on the defending side (§2.13.5). Ambush, Defensive and Garrison count as in any field battle; no hex changes hands. Win, and the defender retreats and the group marches on together; lose or draw, and the **whole** group scatters — a leader that did not fight keeps its remaining path and walks it alone. Inside against outside a wall is a siege, never an arrival clash; armies already camped together at war wait for the camp sweep (§2.13.5). **Link members placed on the hex by a storm arrive the same way**: the members a storm has already put on the hop hex attack an army at war with them in their zone, and that army does not withdraw for free. The arriving army's own battle card says why it fought: *"Carried in Nemedia AII's group onto (5,5), your Army IV attacked Cimeria on arrival — your kingdoms are at war."*

- **Defeat scatters the group.** A linked group that loses a field battle, a beach fight, or its walls to an assault retreats army by army (beaten outside its own walls, it goes inside whole instead, §5.8.0) — except a member that never entered the battle hex, which holds where it stands (at sea too), carded *"Your army had not marched in with its leader — bruised, it held its position at (c,r)"* (a fleet: *"The survivors held their position at (c,r) — your fleet had not sailed in with its flagship"*) — and the **link breaks** (carded). **A drawn field battle scatters the attacking group too** — the attackers fall back army by army and the defenders hold — and its cards read *"Stalemate at (c,r) against X — the group fell back and scattered"*. A lost or drawn **Sally** does not scatter: its group is back inside the walls together (§2.13.7). An **attacking** group whose assault does not take the walls is **not** scattered: its survivors stay camped at the gates as besiegers, still linked (§5.8.0). The card names the battle: an army that fought reads *"Defeat at (c,r) against X — the group scattered"*; an army that was **not** in that battle reads that its leader was beaten there and that it is released — it is not told it lost. Whenever the leader itself did not fight (for example a member attacked on arrival), the card names the armies of your group that were beaten instead: *"Nemedia AII (in your group) was beaten at (5,5) by Cimeria — your army was not in that battle and is released; the group scattered"*. A member that did not survive that battle is named as destroyed: *"Nemedia AII (in your group) was destroyed at (5,5) by Cimeria — your army was not in that battle and is released; the group scattered"*. Reform it when you regroup.

- **No group embarkation.** Linked armies cannot board fleets — UNLINK first; each army embarks alone.

> ***▶ Example — an allied, cross-kingdom link.** Cimeria's **II ARMY** and Aquilonia's **III ARMY** are mutual allies, both standing on hex (24,18); Cimeria wants them to march as one, under its command.*
>
> *- **Turn 5 — Cimeria proposes.** On II ARMY's card, Cimeria picks Aquilonia's III ARMY and submits. Cimeria's report reads Link Offered — Cimeria A II offers a link to Aquilonia A III · awaiting the ally's LINK ACCEPT; Aquilonia's report carries the matching offer. **Nothing is linked yet** — if Cimeria orders II ARMY to march this turn, it marches alone.*
>
> *- **Turn 6 — Aquilonia accepts.** The offer now shows on Aquilonia's III ARMY card with a LINK ACCEPT control. Aquilonia accepts; both reports read Link Formed — Cimeria A II links Aquilonia A III (allied — accepted). Status immediately levels to the weaker of the two armies.*
>
> *- **Turn 7 onward.** Cimeria's II ARMY is the leader: its move and stance orders drive both armies. Aquilonia's III ARMY has its own move and stance orders ignored (carded); its one prerogative is UNLINK, which takes effect the same turn.*
>
> *The offer **persists across turns** until accepted — but lapses (carded) if the armies part, or if the alliance ends, war is declared, or a vassal's oath of fealty is renounced.*
>
> ***⚠ What this means —** the acceptance costs a full turn, so a cross-kingdom link must be arranged **before** the turn you need the combined force, not during it.*
>
> ***▶ Example — a link drags in kingdoms that never quarrelled.** Six kingdoms, two link groups of three armies each, one turn. Only the two **leaders** are at war going in — every other pair is at peace or allied, and two of the six are allied to the other side's leader. This is the trap: a member's own diplomacy never gets a vote once its army stands in the group.*
>
> *\| Attacking group (leader **Cimeria**) \| Relation to Nemedia's side \|*
>
> *\|---\|---\|*
>
> *\| **Cimeria** — I ARMY, 30 Legionnaire + 10 Equites, Gen. Strabo (military 40) \| **At war** with Nemedia \|*
>
> *\| **Aquilonia** — I ARMY, 40 Velites \| At peace with Nemedia, Vanaheim and Ophir \|*
>
> *\| **Zingara** — I ARMY, 40 Velites \| **Allied to Nemedia** \|*
>
> *\| Defending group (leader **Nemedia**, stance Defensive) \| Relation to Cimeria's side \|*
>
> *\|---\|---\|*
>
> *\| **Nemedia** — I ARMY, 80 Legionnaire, Gen. Numa (military 30) \| **At war** with Cimeria \|*
>
> *\| **Vanaheim** — I ARMY, 40 Legionnaire \| At peace with Cimeria, Aquilonia and Zingara \|*
>
> *\| **Ophir** — I ARMY, 40 Legionnaire \| **Allied to Cimeria** \|*
>
> *Every member is a **mutual ally of its own leader** (the link's one hard requirement) — Aquilonia and Zingara with Cimeria, Vanaheim and Ophir with Nemedia. Relations with the other side are untouched by that, and nobody checked them before signing on.*
>
> *- **Turn 1 — both groups link and Cimeria marches, all in one turn.** Cimeria's armies already share her hex; so do Nemedia's. Cimeria issues LINK on Aquilonia and Zingara; Nemedia issues LINK on Vanaheim and Ophir; all four allies submit LINK ACCEPT the same turn — every group forms immediately (§5.11's same-turn handshake). Cimeria then orders **I ARMY to march onto Nemedia's hex**. That single order drives the whole column: Aquilonia's and Zingara's own move orders are irrelevant — in fact Aquilonia's file still has one queued (a decoy march elsewhere), and her report explains why it never ran: "Army I follows its leader — Your Army I is linked under an allied Army I and marched with the group — its own move order was superseded. Only the leader moves the group; UNLINK to march independently." (the GM log keeps the terse line "Aquilonia — Army I is linked and follows its leader") Nemedia never gets to choose whether to fight; her hex is simply where the column ends up.*
>
> *- **Who actually fights.** All three attackers arrive as one coalition — Cimeria, Aquilonia, Zingara, **120 troops together**, Aquilonia and Zingara included even though neither has any quarrel with Nemedia. On the defending hex, gather-defenders pulls in every co-located army that is **at war with the attacker (and not at war with a defender) OR linked to the primary defender** — Vanaheim and Ophir are neither at war with Cimeria going in, but both are linked to Nemedia, so both are pulled in with no say at all. **160 troops** stand to receive the charge, all three inheriting Nemedia's Defensive stance through the link (a slave's stance is the leader's — §5.11).*
>
> *- **The arithmetic — real engine output, both sides** (re-run against the current engine, both groups already linked: every figure below reproduced). Battle terrain: open plains (no race bonus for either side, Imperial vs Imperial — attTerrainMult = defTerrainMult = 1.00). Cimeria's mixed foot-and-horse stack gives the **whole attacking coalition** a blended cavalry scale of **×1.10** (plains favours mounted troops, and only her own contingent rides); Aquilonia's and Zingara's pure-foot Velites carry no cavalry bonus of their own. Nemedia's Defensive stance applies **×1.20** to her whole linked side. Commander bonus applies **per army, to its own contingent only** (cmdMult = 1 + military/1000, §5.5.1): Strabo's military 40 gives Cimeria's own troops ×1.04; Numa's military 30 gives Nemedia's own troops ×1.03 — Aquilonia, Zingara, Vanaheim and Ophir fight uncommanded. Status entering the fight had already cost the marching column 5 points for the hop. Combining every army's raw WP, terrain, cavalry, status and commander multiplier into each side's effective strength, then rolling once per side (initiative = 1.075, luck pinned to exactly 1.00 for this worked example so the arithmetic is checkable):*
>
> *- **Attacker:** WP 7174 → roll **8280***
>
> *- **Defender:** WP 10720 × Defensive ×1.20 → roll **13057***
>
> *- defRoll (13057) \> attRoll (8280) × 1.2 (9936) → **Nemedia's side wins.** Ratio 13057 ÷ 8280 = **1.58**.*
>
> *- Casualty formula (§5.5.3) at ratio 1.58: loser ≈ 0.12 + 0.18 × ln(1.58) ≈ **20%**, winner 0.10 ÷ 1.58 ≈ **6%** — and that lands exactly on the engine's own numbers.*
>
> *- **Casualties, army by army.** Attacking coalition (120 → 99, **−21 troops**, ≈20% each): Cimeria 30 Legionnaire + 10 Equites → 24 + 9 (**−7**); Aquilonia 40 Velites → 33 (**−7**); Zingara 40 Velites → 33 (**−7**). Defending coalition (160 → 151, **−9 troops**, ≈6% each): Nemedia 80 Legionnaire → 75 (**−5**); Vanaheim 40 Legionnaire → 38 (**−2**); Ophir 40 Legionnaire → 38 (**−2**).*
>
> *- **FIGHTING MEANS WAR — the attacker pays for the fight it forced.** Every attacking kingdom that traded blows is now at war with every defending kingdom it faced — eight new wars from one battle (Cimeria–Nemedia was already at war and doesn't re-fire). **The aggressor's own opinion charge is capped at one per step of a march or voyage, and at one per battle for any other engagement** — this fight is one step of Cimeria's march, and a war declared on the hex's owner or its defenders as a march hop, landing or assault begins counts toward that one charge: however many kingdoms an attacker newly wars in this SAME step, every one of those wars is still declared and every kingdom still gets its own card — only the first pair processed costs the aggressor opinion; every later one that step is capped, still carded, no further loss:*
>
> *- Aquilonia declares on Nemedia, Vanaheim **and** Ophir (all three previously at peace) — all three wars fire, but only the Nemedia card carries the charge: "War declared against Nemedia! … Opinion -6 (aggressor penalty) … Previous stance: peace." Vanaheim's and Ophir's cards read the same "peace is over" prose but the capped effect line: "No further opinion penalty — already charged once this step."*
>
> *- Zingara declares on Nemedia, Vanaheim **and** Ophir — and the Nemedia card reads differently from the other two: "War declared against Nemedia! … A sworn alliance lies in ruins … Previous stance: alliance." Zingara followed Cimeria into a fight against her own ally and personally ended that alliance — and that's the ONE pair, of Zingara's three, that eats the −6 aggressor opinion penalty; Vanaheim's and Ophir's cards are capped the same way as Aquilonia's.*
>
> *- **Cimeria** — the leader who ordered the march — also declares on **Vanaheim and Ophir**, the two kingdoms pulled into Nemedia's defence purely by their link, neither of which had any quarrel with her going in: "War declared against Vanaheim! … The peace is over … Previous stance: peace … Opinion -6 (aggressor penalty)." Vanaheim is the pair that gets charged — Ophir's card carries the SAME broken-alliance prose ("A sworn alliance lies in ruins … Previous stance: alliance") but a capped effect line: "No further opinion penalty — already charged once this step." Ophir was Cimeria's own ally — marching on Nemedia's hex is what broke that alliance — but Cimeria pays the −6 only once for the whole step, not once per kingdom it drags into war.*
>
> *- Vanaheim and Ophir, pulled into the defence with no quarrel of their own, never carry an aggressor card for this fight — they get the **defender's** card for each attacker that just declared on them (Cimeria, Aquilonia, Zingara), and their opinion does not move — a declaration costs only the realm that makes it: "Cimeria is now at WAR with you! … No opinion change for you … Previous stance: peace" for Vanaheim, "… A sworn alliance lies shattered … Previous stance: alliance" for Ophir. The kingdom that marched in and forced the fight pays the opinion cost — once per step, however many kingdoms it newly wars in it; the kingdom that stood on its own ground and got dragged in by its link never pays at all.*
>
> *- **The defeat's aftermath.** Cimeria's group lost the field: Cimeria falls back to (1,2), the hex the column marched from — and Aquilonia and Zingara, which never left it (members follow their leader in only after a win), **hold where they stand** — and the moment the last one lands, the link breaks for all three. The GM log records it as one line, by kingdom name: "Cimeria AI + Aquilonia AI + Zingara AI — group dissolved · Defeat — the group scattered." Each of the three PLAYERS sees something different on their own report — their own army, not the roster of names: "Army I — link broken · The link group is no more — Defeat at (1,3) against Nemedia, Vanaheim, Ophir — the group scattered. The army acts independently again. · Independent command restored." Reforming it costs a fresh proposal and (for the allies) a fresh accept. Nemedia's group **held the ground and stays linked** — only the losing side scatters. Opinion moved on every kingdom that fought (winners +2, losers −3, independent of the war-declaration swings above), and Nemedia's coalition split 30% spoils of the field by war-point share.*
>
> *- **What each of the six sees.** Cimeria, Aquilonia and Zingara each get a full Defeat combat card (the same attWP/defWP/rolls/ratio payload transcribed above), their own casualty line, and their group's Link Broken card. Nemedia, Vanaheim and Ophir each get a Victory card, their own spoils share, and no Link Broken card at all. All six get the new-war cards for the pairs they personally fought — Vanaheim and Ophir's cards correctly name **Cimeria**, not themselves, as the one who started it.*
>
> ***⚠ What this means —** joining a link is signing a blank cheque on your own diplomacy — the link **is** consent, so your leader's wars become your wars the instant a battle finds your hex, whatever your own kingdom's diplomacy said the turn before. Check the leader's war list before you accept, not after. The one control you keep is UNLINK, effective the same turn you order it — the only way to opt out of a fight your leader picked — except at a friend's walls, where your army leaves a group that turns on that friend (§5.11.1 rule 3).*

**Bystanders — when the ground falls under your feet.** An army that sat out the battle for its hex (it was at peace with the attacker) resolves by its stance with the **conqueror** the moment the hex flips: **allied** with the conqueror → it **stays** — the ground now belongs to its own ally; at **peace or neutral** → it **withdraws in good order** to a valid neighbouring hex — no war, no losses, a withdrawal rather than a rout; **cornered** (no line of retreat) → cornered men don't surrender: the army **declares war** and fights a **last stand** against the conqueror's battle-weakened force — if it loses it dies where it stands, but if it **wins it retakes the hex**, won with blood. (Nobody **inside** walls is a bystander: whoever storms or besieges them is at war with every realm inside (§5.6), so this paragraph is about open ground and armies camped outside. A settlement falling to siege starvation treats a third kingdom's army camped outside the same way, except that one at war with the besieger with nowhere to run is routed and stripped, §2.7.) **An ally stays only while there is room**: after a successful storm every one of the conqueror's armies stands inside its new walls, in Garrison, and an ally counts room in its own zone — an allied bystander that would be the fourth in its zone withdraws to make room, carded *"made room"*. **If it has nowhere to go, the conqueror gives way instead**: one of the conqueror's armies in that zone that is neither the attack's leading army nor a link leader withdraws — the conqueror's own realm gives way before its allies, then by realm, last army first (never the order the turn's orders were read in) — in good order to a neighbouring hex — no losses — leaves its link group (its leader, whose group lives on, reads *"Army N — X AN left the group"*), and is carded *"withdrew … to make room"* with the reason (your ally there was cornered); the ally's card says who gave way. Only when none of those armies has a route out either (or every one of them leads) does the zone keep a fourth army — both sides are carded, the hex is marked for the GM's validator (that zone only), and the mark clears once an army moves out. **And when the defence holds**, an army that sat out but is now at war with an army still holding its zone withdraws instead of camping beside an enemy (§5.11.1) — never a **besieged** army, which stays inside (§2.13.7). **A cornered army's last stand is fought by the conqueror's own armies on the hex** — and by a friend's army only when that friend is already at war with the cornered army's kingdom: an ally that joined the attack, or a link member of another kingdom, does not start a new war there. If none of the conqueror's armies is left on the hex, a friend already at war with the cornered army fights it alone; should the cornered army win, it holds its ground there — no hex changes hands and no war begins with the conqueror, whose armies were not in that fight; its report says it holds its ground **still cornered**, with every way out closed. **Order:** the armies that are *not* allied with the conqueror resolve first — they withdraw or make their last stand — and only then its allies, who therefore count the room as it really is. **When a last stand retakes the hex, the rest of the camp resolves again against its new holder** — an ally of the retaking realm stays, a stranger withdraws or, cornered, makes its own last stand. *Already at war* counts a war declared by **either** side: a friend that still holds a peace offer to the cornered realm fights the last stand with its own stance unchanged — its offer stands, no war is declared for it and it pays no aggressor charge.

**Reading the map.** Co-located armies fan out in the hex's army slot — shields spread slightly so the stack's depth stays visible, with a **⚔×N** count on the fan. On the kingdom map the strongest army sits on top; on an army's own minimap, that army does. Your own shields take the left of the fan, in slot order, and foreign shields follow to their right. On a walled hex the fan is split by zone: the armies **inside** the walls fan in the upper slot, each wearing the **walls badge** — the hex's construction picture (its people's icon, or the village for a POP settlement; the citadel when no construction is known) on a dark disc at the shield's upper right — and the outside campers in the lower slot — only an army in Garrison, yours or a friend's, is inside (§5.8.0), and the **⚔×N** count is per zone. A planned group move previews the **whole fan** at the destination — allied members included, fleet groups too. A member you have just released, or a group you are dissolving, stays where it stands; the map's hover tooltips list the fan the same way. The link itself is **private**: enemies see only N armies sharing a hex, never who commands whom.

> ***⚠ What this means —** LINK turns three mid-sized armies into one crushing column — at the price of tempo (weakest-man pace and status) and fragility (one lost battle scatters the group). The automatic co-located defence is the cheaper tool: park two armies on a border hex and any attacker faces both, no orders needed. And watch the leveling: linking a fresh army to an exhausted one spends the fresh army's readiness on the spot.*

**5.11.1 Battles Between Your Allies (One Kingdom, Both Sides)**

A kingdom allied to two kingdoms that go to war with each other can find its armies on **both sides of the same fight**: one camped on the defender's hex — perhaps linked into the defender's group — and another marching in the attacker's link group. These rules decide who fights, which wars begin, and where every army stands when the dust settles. They apply to field battles and assaults on land and to naval battles at sea.

**1. A kingdom never fights on both sides of one battle.** If one of your armies fights on the attacking side, your army standing in the defence **stands aside**: it does not defend, loses nothing, and your report carries a *"held back"* card. Your attacking army still fights, and its blows are your kingdom's: you go to **war with the defender** and pay the aggressor's opinion penalty (the link is consent). Because you are now at war with the defender, your held-back army leaves the defender's link group at the end of the turn. The defender's own kingdom is never held back.

**2. Who else joins the defence** is the §5.11 rule above; rule 1 is the one exception to its link-group pull.

**3. At a friend's walls, a member leaves the group.** A linked army never fights a **friend** (its realm's mutual ally, vassal or liege) at that friend's own walls.

- **When it leaves.** Its group, at such walls, marches on them, storms them, besieges them or presses an Assault there; or is attacked there by the owner or the owner's friends (a relief, a Sally); or camps there while hostile to them — the leader's realm at war with the owner, holding the siege there, or the leader on Siege or Assault. It is carded *Army N left X's group at (c,r)*, and the leader's realm is told too.

- **When it stays.** A group camped there at peace, pressing nothing and attacked by nobody, keeps its member, which fights with it against anyone else there (a rival besieger). A group marching away this turn keeps its member, which marches with it.

- **What leaving means.** It stays where it stood, on its own and at peace with its friend: it adds nothing to the ring, is never carried inside, and no war is declared on its friend. Rule 1 does not apply. It keeps its own wars — a realm it is already at war with still meets it there.

- **At war with the army at the gates.** A member at war with the army it would face at the gates still fights that battle — beside its group, or on its own if it has already left a camped group — but it leaves the group before any storm of its friend's walls.

- **Getting in.** Filing Garrison, it passes the §5.8.0 door (not past an enemy camp, not into a full inside). Once inside, the besieger's next siege tick declares war on it like every realm inside (§5.6), even when the besieger is its own ally.

- **No new link** forms there under a leader hostile to those walls: the offer or order is refused, carded *Link refused*, with the cause.

> ***▶ Example.** Aquilonia's VII besieges Hyperborea's walls with Nemedia's VI linked; Nemedia is Hyperborea's ally. In the pre-phase VI leaves the group and stays at the gates, at peace — the ring counts only VII. Had VII marched away that turn, VI would have gone with it. Had VI filed Garrison, it would have gone inside (room permitting), and Aquilonia's siege tick would then put Aquilonia and Nemedia at war.*

Your army inside, in Garrison, is declared on like every realm inside (§5.6) and defends behind the walls; once besieged it may order Sally (§2.13.7). If the attacker's group would overflow the outside zone, the **whole group halts at the gate**, and the card names the zone that is full.

**4. After the battle — where everyone stands.**

- **The attacker takes the ground.** Armies that did not fight resolve by their relation with the conqueror (the *Bystanders* paragraph above): an ally of the conqueror stays while there is room — after a storm the conqueror's armies stand inside its new walls, in Garrison, and an ally counts room in its own zone (inside only if it is in Garrison), so an ally that would be the fourth there withdraws, carded *"made room"* — or, if it is cornered, one of the conqueror's non-leading armies withdraws in its place, carded with why (a fourth stays only if none of them can move either); anyone else withdraws, and a cornered enemy makes a last stand.

- **The defence holds.** An army that sat out but is now at **war** with an army still holding its zone of the hex **withdraws instead of camping beside an enemy** — carded *"withdrew"*, with no losses: it keeps its siege engines and pays only the usual retreat readiness cost (§5.10). One with nowhere to go stays, and is told so — and fights it out at the start of the next Phase 5 (the camp sweep, §2.13). This is exactly what happens to your held-back army when the defence holds, because your attacking army has just taken you to war with the defender. An army of the attacking kingdom standing in the attacker's zone never sits out in the first place: it joined the attack and shares its result (§2.13.5).

- **The attacker's group moves in.** Members follow the leader onto the hex only while it has room; a member that does not fit stays where it stood and leaves the group. A member whose kingdom is now at war with the leader is not carried either, and leaves the group at the end of the turn. A member carried in that is at war with an army still on the hex attacks it on arrival (§5.11).

- **A drawn or lost field battle scatters the attacking group**, and its cards read *"Stalemate at (c,r) against X — the group fell back and scattered"* or *"Defeat at …"*. **A Sally does not scatter:** its survivors go back inside in Garrison (§2.13.7). **A failed assault does not:** the attackers stay camped at the gates as besiegers, still linked (§5.8.0).

**5. At sea.** Rules 1 and 2 hold for fleets: if one of your fleets attacks with the attacker's group, your fleet in the defence stands aside, carded *"held back"*, and your attacking fleet takes you into the war. The sea has no zones and no withdrawal step: a fleet left sharing a hex with an enemy fights it in the next turn's cohabitation sweep, before movement (§2.14) — the land twin is the Phase 5 camp sweep (§2.13).

> ***▶ Worked example — Aldoria (A) and Sylvane (C) are at war, and both are allied to Gruk-Mor (B).** Aldoria's group of A I, A II and Gruk-Mor's B I holds a hex; Sylvane's group of C I, C II and Gruk-Mor's B II marches in. Real engine outcomes:*
>
> *\| The fight \| Gruk-Mor's army with Aldoria \| Gruk-Mor's army with Sylvane \| Gruk-Mor's wars at the end \| Links \|*
>
> *\|---\|---\|---\|---\|---\|*
>
> *\| Open ground, Sylvane wins \| Held back; stays as Sylvane's ally \| Attacks Aldoria \| At war with Aldoria, still allied with Sylvane \| B I leaves Aldoria's group; a Sylvane member that would make a fourth stays behind \|*
>
> *\| Open ground, Aldoria holds \| Held back, then withdraws \| Attacks from where it stood; never entered the hex, so it holds its position as the group scatters \| At war with Aldoria, still allied with Sylvane \| Sylvane's group scatters; B I leaves Aldoria's group \|*
>
> *\| Walled hex, Aldoria in Garrison \| Defends beside Aldoria — Sylvane declares war on every realm inside the walls, Gruk-Mor included (§5.6); when the walls fall it falls back with Aldoria \| Leaves Sylvane's group and stays where it stood — it does not storm \| At war with Sylvane, still allied with Aldoria \| B I's group dissolves; B II leaves Sylvane's group \|*
>
> *\| Walled hex, Aldoria's army outside on Defensive \| Defends beside Aldoria in the battle at the gates \| Leaves Sylvane's group before the battle at the gates — it fights neither that battle nor the storm (rule 3) \| At war with Sylvane, still allied with Aldoria \| B II leaves Sylvane's group; if Sylvane wins, Aldoria's group scatters \|*
>
> *\| Walled hex, outside zone already full \| — \| — \| No change \| Sylvane's whole group halts at the gate \|*
>
> ***The row "Aldoria's army outside on Defensive" in words.** Sylvane's column meets A I, A II and B I outside, on Defensive, in the open. B II marched with Sylvane but is Aldoria's friend: it leaves Sylvane's group, carded Army II left Sylvane's group at (c,r) once, stays where it stood, and no war is declared on Aldoria. If Sylvane wins, the beaten go inside in Garrison and C I and C II storm without B II; if Sylvane loses, it falls back alone.*
>
> *Nobody inside sallies against Sylvane's storm: Aldoria's armies and Gruk-Mor's in Garrison defend behind the walls at ×1.30; any of theirs outside are fought first. Only from the turn after Sylvane's first siege tick can they order a **Sally** (§2.13.7) — and then Aldoria's and Gruk-Mor's armies can go out together, linked or not.*

**5.12 Battle Card Derivation (Factor Ledger)**

Every land and naval battle card carries a **factor ledger** alongside the summary numbers described in §5.5–§5.9: an ordered list of every multiplier applied to the roll, recorded at the moment the resolver applies it rather than reconstructed afterward, so the printed Final Roll can always be reconciled against it — base War Power × Π(chain multipliers) ≈ Final Roll, to display rounding. The chain is kept **per participant**: a coalition battle lists each army's or fleet's own multipliers separately, plus a short side-wide **tail** (initiative, fortune, and side-only terms such as the assault attacker's wall penalty) applied once to the side's combined total. The naval port bonus is not a tail term: it is a per-fleet chain row, on whichever side a fleet fights at a friendly port (table below). For the overwhelming majority of battles — one army or fleet per side — the chain collapses to exactly one row and reads exactly like the formulas already given above.

Both battle cards — land and naval — are laid out as a combat-result sheet in the colours of your chosen theme: the two sides as counters (troops or ships, war power, losses), the **odds ruler** — the ratio of the final rolls on a 0.5–4+ scale, with the victory line at the win threshold (§5.5.2) — then the **Full derivation** beside the casualty ledger, every modifier on its own row with the running product (rounded for display only; a side without that modifier shows —). When either side fields several armies or fleets, the rows pair **Contingent 1** with Contingent 1 and so on, each cell naming its own unit, before both sides' totals and the battle-wide rows (initiative, fortune, walls, beach). A city's militia is its own counter and its own casualty line. The sheet ends with the result stamp and, where there are any, the spoils of war or the prizes taken (§2.13.12). A report from before the ledger shows the War Power and the summary modifiers it carried instead — on an assault, marked as already included in that war power. Both sides carry the complete chain, fortune included — and so does the card of a realm that only watched (a battle on its land or in its harbour), drawn *Attacker \| Defender* — its banner reads *"\<attacker\> WON"*, *"\<defender\> HELD"* or DRAW, port rows read *Port bonus (defender)* / *Port bonus (attacker)*, and each side's veterans note carries its kingdom — except a harbour fight involving a fleet that is not its friend, seen from its docks without the derivation; a realm whose own army fought in the battle gets its own battle card, never a watcher's — the total is visible on the card anyway, so withholding the reasons behind it would only force the player to subtract by hand. A factor equal to ×1.00 is left out of the chain, with one exception: **Army / Fleet status is always printed**, even at ×1.00, because it is the one factor a player tracks turn by turn. **Initiative** appears only on the attacker's side — a defender never rolls it. The summary table at the top of the card lists it on **both** players' cards, in the attacker's column.

Factor keys, by battle kind:

|                     |                                                                                                                                                                                                                                                                                                              |                                                                       |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Battle kind**     | **Per-participant factors**                                                                                                                                                                                                                                                                                  | **Side-wide (tail)**                                                  |
| Assault (§5.6)      | status, terrain, cav (the mounted-share cavAssaultScale/cavTerrainScale of §5.6.1), cmd; the garrison's stance and fortress bonus are per-participant, and so is legion (§4.2 — an Imperial owner's garrison, ×1.10); militia appears as its own named participant (militia, fortress, terrain, cmd, legion) | Attacker: wall (the attPenalty of §5.6.1), init, luck. Defender: luck |
| Field battle (§5.5) | status, terrain, cav, stance (defender only), cmd, legion (an Imperial owner defending its own FI/POP hex — or **sallying** from it, the one case where the row sits on the attacker; §4.2)                                                                                                                  | Attacker: init, luck. Defender: luck                                  |
| Amphibious (§5.7)   | Attacker: status, cmd. Defender: status, stance, cmd, legion (an Imperial owner holding its own FI/POP shore; §4.2)                                                                                                                                                                                          | Attacker: beach (BEACH_PENALTY), init, luck. Defender: luck           |
| Naval (§5.9)        | status, cmd, cargo (cargoMod), navrace (raceMod), port (portMod ×1.25 — any fleet fighting at a friendly port, attacker or defender, provided it began the turn in that port; a per-fleet row, so a mixed side shows it on some fleets only)                                                                 | Attacker: init, luck. Defender: luck                                  |

A second, independent ledger explains the casualty line: for each unit stack — and militia, in an assault — it names the stack, its count, its **death factor** (§5.5.4's deathFactor, the value actually used after the armour-dissolve blend of §5.5.3), the raw fractional loss, and the rounded headcount actually removed. A card with zero realised losses reads **"none"** — never a bare percentage standing next to nothing.

> ***▶ Example — a casualty line, named.** Eight Elven Cavalry (xp_wp 251) lose an assault. Their price-equivalent (§5.5.4) is gold + iron×12 + horses×20 + wood×5 = 300 + 660 + 20 + 15 = 995; veterancy vet = 251/247 − 1 ≈ 0.0162. landDeathFactor = max(0.3, 1 − 995 × 1.0162 / LAND_DEATH_BASELINE), where LAND_DEATH_BASELINE = 1,100 — the term inside works out at about 0.08, below the floor, so the **0.3 floor** binds. At a battle loss rate of 6.67%: rawLoss = 8 × 0.0667 × 0.30 ≈ 0.16 men, rounding to **0**. The casualty ledger states the row directly — unit "Elven Cavalry", count 8, df 0.30, raw 0.16, lost 0 — and the effect line reports the realised loss, never the curve's raw input. (A militia row, where one appears in an assault, uses MILITIA_DEATH_FACTOR = **1.0**.)*

**PART VI — ECONOMY & PRODUCTION**

**6.1 The Six Resources**

|              |                      |                                                                                                                                                                                                                                  |
|--------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resource** | **Primary Source**   | **Primary Drain**                                                                                                                                                                                                                |
| Gold         | Tax, ports, trade    | Unit/ship upkeep, construction, hiring                                                                                                                                                                                           |
| Food         | Farms, plains, ports | Army consumption, some unit costs                                                                                                                                                                                                |
| Iron         | Mines                | Unit/ship production, some upkeep                                                                                                                                                                                                |
| Horses       | Breeding             | Mounted unit production                                                                                                                                                                                                          |
| Wood         | Lumbermills          | Unit recruitment (40 of 42 units — only Swordmaster and Bladedancer cost none; every siege engine costs 50w), **all ship hulls** (40–130w by tonnage), and **Aesir/Nomad/Orc-family wall levels** (founding, upgrade and repair) |
| Stone        | Quarries             | **Wall levels** of every other construction family (founding, upgrade and repair; Dwarf-family walls cost half)                                                                                                                  |

**6.2 Income Sources Summary**

|                           |           |                                   |
|---------------------------|-----------|-----------------------------------|
| **Source**                | **Phase** | **Resource**                      |
| Plains (no site)          | Phase 1   | Food                              |
| Population tax            | Phase 1   | Gold                              |
| Farm sites                | Phase 1   | Food                              |
| Mine sites                | Phase 1   | Iron                              |
| Port sites                | Phase 1   | Gold + Food                       |
| Lumbermill sites          | Phase 1   | Wood                              |
| Quarry sites              | Phase 1   | Stone                             |
| Character bonuses         | Phase 1   | Gold / Food / Iron / Wood / Stone |
| Trade Pacts               | Phase 1   | Gold                              |
| Horse breeding            | Phase 1   | Horses                            |
| Orc reproduction          | Phase 1   | Troops (not resources)            |
| Vassal tribute (received) | Phase 1   | Gold                              |
| Market buys               | Phase 3   | Commodities                       |

**6.3 Population Tax**

rawTax = floor(totalPop × taxRate / 100)

Rate 1–10 (player-set, default 5), collected in full (see Section 2.9.5). Opinion modifies effective yield (see Section 2.9.6), and the rate you hold moves opinion every turn (see Section 2.9.13). Changes take effect next turn.

**6.4 Hex Terrain Income**

Plains (no site): 1 food/turn. There is no terrain gold.

**6.5 Site Production**

|                     |           |                                                                                                |                                                |
|---------------------|-----------|------------------------------------------------------------------------------------------------|------------------------------------------------|
| **Site**            | **Level** | **Formula**                                                                                    | **Resource**                                   |
| Farm                | 1 / 2 / 3 | max(1, floor(pop × **roll 5–25% / 20–50% / 40–80%**))                                          | Food (rolled per farm per turn)                |
| Mine                | 1 / 2 / 3 | 10 / 20 / 50 + floor(pop × level/20)                                                           | Iron                                           |
| Port                | 1 / 2 / 3 | max(1, floor(pop × 0.20 / 0.40 / 0.60)) gold + floor(pop × **roll 0–5% / 0–10% / 0–15%**) food | Gold + Food (food rolled per turn, 0 possible) |
| Lumbermill (forest) | 1 / 2 / 3 | max(1, floor(pop × 0.15 / 0.45 / 0.75))                                                        | Wood                                           |
| Quarry — plains     | 1 / 2 / 3 | max(1, floor(pop × 0.15 / 0.45 / 0.75))                                                        | Stone                                          |
| Quarry — hills/mtn  | 1 / 2 / 3 | max(1, floor(pop × 0.10 / 0.40 / 0.70))                                                        | Stone                                          |

*Every site yields at least 1 of its resource on a populated hex (a port's rolled food excepted), but 0 if the hex population is 0. Port rows are per port before the bracket factor (§2.9.4 / §10.3). Rules and exceptions: §3.6.*

**6.6 Trade Pacts**

A **mutual pact** — both kingdoms at trade or better — pays 0–2% of tax + port gold per partner per turn (floor(rand×3) → 0/1/2%), **at most 5 partners in a turn** (the rest: *market saturated*). Any pair short of full mutual alliance needs a shared border, re-checked every turn; full alliance benefits (through-movement, allied recruiting) need alliance on **both** sides. Full rules: §2.9.8.

**6.7 Vassal Tribute**

Rate 1–5%, default 3%, of Phase 1 tax + port gold (no Master bonus). Partial payment if funds insufficient. Vassal and liege automatically at Alliance stance — until a war between them ends the bond (§2.16.4).

**6.8 Upkeep Reference**

All upkeep is deducted in Phase 2. Food is consumed separately via army food consumption.

**6.8.1 Unit Upkeep (Gold and Iron per unit per turn)**

|           |               |          |          |
|-----------|---------------|----------|----------|
| **Race**  | **Unit**      | **Gold** | **Iron** |
| Imperial  | Velites       | —        | —        |
| Imperial  | Legionnaire   | —        | —        |
| Imperial  | Sagitarii     | 4        | —        |
| Imperial  | Equites       | 8        | —        |
| Imperial  | Praetorians   | 12       | —        |
| Barbarian | Raiders       | —        | —        |
| Barbarian | Berserker     | —        | —        |
| Barbarian | Wild Archer   | 5        | —        |
| Barbarian | Storm Horses  | 4        | —        |
| Barbarian | Warchief      | —        | —        |
| Elf       | Swordmaster   | —        | —        |
| Elf       | Bladedancer   | 6        | —        |
| Elf       | Ranger        | 8        | —        |
| Elf       | Elven Cavalry | 10       | —        |
| Elf       | High Guard    | 14       | —        |
| Orc       | Goblin        | —        | —        |
| Orc       | Orc           | 3        | —        |
| Orc       | Orc Archer    | —        | —        |
| Orc       | Warg Rider    | 4        | —        |
| Orc       | Uruk-Hai      | —        | —        |
| Dwarf     | Warrior       | 3        | 1        |
| Dwarf     | Ironclad      | —        | —        |
| Dwarf     | Crossbowman   | 5        | —        |
| Dwarf     | Thunderers    | 10       | 3        |
| Dwarf     | Heartguard    | 6        | 2        |
| Aesir     | Shore Raider  | —        | —        |
| Aesir     | Axe Thane     | 2        | —        |
| Aesir     | Shield-Karl   | 4        | —        |
| Aesir     | Huscarl       | 6        | —        |
| Aesir     | Jarl's Guard  | 10       | —        |
| Nomad     | Rajjala       | —        | —        |
| Nomad     | Naffatun      | —        | —        |
| Nomad     | Rumat         | 2        | —        |
| Nomad     | Bedouin       | 3        | —        |
| Nomad     | Askari        | 5        | —        |

> ***Food is not an upkeep cost.** No unit has food upkeep; every army eats by **headcount** (§2.10.4), so a unit shown with — in both columns still eats.*

**6.8.2 Ship Upkeep (per ship per turn)**

|           |            |          |          |
|-----------|------------|----------|----------|
| **Race**  | **Ship**   | **Gold** | **Iron** |
| Imperial  | Drommund   | 4        | —        |
| Imperial  | Cog        | 8        | —        |
| Imperial  | Galley     | 15       | —        |
| Barbarian | Wolfship   | 3        | —        |
| Barbarian | Reaver     | 5        | —        |
| Barbarian | Tigress    | 14       | —        |
| Elf       | Moonskiff  | 5        | —        |
| Elf       | White Ship | 8        | —        |
| Elf       | Swan Ship  | 16       | —        |
| Aesir     | Snekkja    | 3        | —        |
| Aesir     | Longship   | 8        | —        |
| Aesir     | Busse      | 14       | —        |
| Nomad     | Dhow       | 3        | —        |
| Nomad     | Shini      | 6        | —        |
| Nomad     | Harraqa    | 10       | —        |

**6.8.3 Deficit Consequences**

|                |                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Deficit**    | **Consequence**                                                                                                                       |
| Gold shortfall | 5–15% troop desertion from all armies (rounded down per stack, no minimum — never an army's last soldier, §2.10.2); opinion −5 to −12 |
| Iron shortfall | Reserves go to 0; no troop or opinion effect                                                                                          |
| Food shortfall | Starvation: Orc 10–20% troop loss; others 3–10%                                                                                       |

> ***⚠ What this means — two separate death spirals.** Larger armies cost more gold each turn, so an over-extended military can desert itself even in peacetime; food is a separate check (Orcs worst), and a poorly supplied kingdom can take both hits in the same Phase 2. Keep total upkeep comfortably under income — it is paid before raid gold or battle spoils (§2.13.11) arrive.*

**6.9 Resource Transfers**

Via send_resource orders (Shipments tab) or the \[TRIBUTE\] message token — **one unified system**, surplus-only at **end of turn** and **dispatched as a caravan**: transit 1 + floor(distance ÷ 5) turns between muster seats, a **3% all-or-nothing bandit check** every transit turn, and a turnback if the receiver holds no seat or no longer exists. Direct only to a mutual trade/alliance partner, liege or vassal; to a neutral it is an **offer**; never to a realm at war. **Vassalage tribute and market buy/sell remain instant.** Full rules: §2.8.2, §2.8.3, §8.7.

**6.10 The Market**

Prices, the 60% sell price, order clamps and the price dynamics are all in §2.11.4–§2.11.5. In practice:

- **You buy high and sell low.** A sale fetches about 60% of the price, so a flip always loses money — iron at 12g sells back for round(12 × 0.6) = 7g, a 5g loss per unit (food at 8g → round(4.8) = 5g).

- **Bottom line:** buy when something is cheap (near its base, or right after other kingdoms dumped it) and sell when it's expensive (after a demand spike). Don't churn the same commodity in and out — the buy/sell spread quietly eats your gold.

**6.11 Construction and Upgrades**

|                  |          |                                                                                                      |
|------------------|----------|------------------------------------------------------------------------------------------------------|
| **Action**       | **Cost** | **Chance**                                                                                           |
| Build Farm       | 1000g    | 100%                                                                                                 |
| Build Mine       | 1000g    | 25% mountain / 15% hills / 7% desert & plains / 5% forest                                            |
| Build Port       | 5000g    | 100%                                                                                                 |
| Build Lumbermill | 1000g    | 100%                                                                                                 |
| Build Quarry     | 1000g    | 100%                                                                                                 |
| Lumbermill Lv1→2 | 2000g    | 100%                                                                                                 |
| Lumbermill Lv2→3 | 3000g    | 100%                                                                                                 |
| Quarry Lv1→2     | 2000g    | 100%                                                                                                 |
| Quarry Lv2→3     | 3000g    | 100%                                                                                                 |
| Farm Lv1→2       | 2000g    | 100%                                                                                                 |
| Farm Lv2→3       | 3000g    | 100%                                                                                                 |
| Mine Lv1→2       | 2000g    | 30% — terrain must be mountain, hills or desert (plains/forest mines stay Lv1; refused and refunded) |
| Mine Lv2→3       | 3000g    | 50% — Dwarven kingdoms only; terrain must be mountain                                                |
| Port Lv1→2       | 10000g   | 100%                                                                                                 |
| Port Lv2→3       | 15000g   | 100%                                                                                                 |

**Constructions are the other half of building, and they work differently.** Sites are capped at level 3 and priced in the table above (§3.6), and only mines roll — to prospect and to deepen; constructions are expensive, **deterministic** (no dice — every gate is checked, then it simply happens) and run to 5–20 levels depending on family. They also cost **two** resources: gold *plus* the stone or wood of the wall increment.

|                                |                                                                                                                                                                                                               |                                                           |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **Action**                     | **Cost**                                                                                                                                                                                                      | **Chance**                                                |
| Found construction (§2.11.9)   | 500g blueprint + 100 settlers (seat must hold 300) + founding tier's **full wall** in stone/wood (Dwarf family: ceil(points/2); wall-less tiers — Orc Level 0, Nomad Lv.1, Generic Lv.1 — no material at all) | 100% if every gate passes; refused at zero cost otherwise |
| Upgrade construction (§2.11.7) | Next level's gold cost **+ wall increment** in stone/wood (Dwarf family: ceil(points/2))                                                                                                                      | 100% if every gate passes; refused at zero cost otherwise |
| Repair wall (§2.11.8)          | 1 stone/wood per point, up to floor(wallMax × 0.10) per turn                                                                                                                                                  | 100%, partial repairs succeed                             |
| Siege engine (§5.8.6)          | 250g + 50 wood + 10 iron each, 3g/turn upkeep                                                                                                                                                                 | 100% (an ordinary recruit)                                |

Per-level gold and wall figures vary by family and are listed in the Player Page's **🏰 Constructions tab** for every settlement you own. **All six construction order types share one slot per hex per turn** (§2.11.1).

**6.12 Horse Breeding**

A herd of 2+ horses breeds 1–3% a turn (plus a Master of Horses' points, §2.9.7), rounded up, on what is left after this turn's cavalry is paid (§2.9.9).

**PART VII — CHARACTERS**

**7.1 What Characters Do**

Characters are named individuals with four stats. Each occupies one assignment slot. Characters can die after combat — army commanders after a land battle, fleet commanders after a naval one, the same roll (§7.7). Death is permanent.

The **kingdom leader** shown on the Player Page banner is **derived, never stored**: it is simply the first living character in court order. There is no leader field in the kingdom state and the Turn Processor never reads one — every character effect is keyed to an assignment, so the crown itself grants nothing: no stat bonus, no mechanic. When a leader falls the next living character in list order succeeds at once (seniority decides, not stats, so the heir cannot change silently when the court changes); a character hired later never jumps the queue. If the whole court is dead or empty, the banner shows a **vacant throne** card until you hire again (§7.3).

**7.2 Character Stats**

Each stat is randomly generated at creation; afterwards it can only rise through experience (§7.10), to at most min(150, base + 20%).

- **Hired characters** (Phase 4 hire_character order): each stat rolled 1–100.

- **Initial rulers** assigned by the GM in the Map Editor at campaign creation: each stat rolled 20–100 (avoiding the pathological 1–19 range). Witch King stats are additionally doubled and capped at 150 — see §7.8.

|            |                                                          |                                                                                                                                                                                                            |
|------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stat**   | **Used By**                                              | **Effect**                                                                                                                                                                                                 |
| Military   | Army / Fleet commanders                                  | cmdMult = 1 + military/1000 added to combat roll                                                                                                                                                           |
| Economics  | Treasurer                                                | Bonus gold income: stat × 0.2% of tax gold                                                                                                                                                                 |
| Management | Masters of Farms/Mines/Ports/Lumbermills/Quarries/Horses | Bonus resource income: stat × 0.2% of relevant base (farm+port food, mine iron, port gold, lumbermill wood, quarry stone); the Master of Horses adds stat × 0.02 percentage points to herd growth (§2.9.9) |
| Politics   | Spymaster                                                | Spy accuracy tier (\>75 / \>50 / ≤50); the price of a rumour (§8.8.7)                                                                                                                                      |

**7.3 Hiring**

Default cost: **1000g** (CHAR_HIRE_COST_DEFAULT). Deducted at hire time. The order names a candidate_id from your court's **candidate pool — three applicants rolled by the TP** (topped back up to three each turn); any stats written into the order are ignored, the applicant's TP-rolled stats are what you get.

**Names are unique across the world.** No two characters — living **or fallen** — may share a name, in any kingdom, case-insensitive. A hire with a taken name is refused before any gold is spent (*"Choose another name — this name was already taken."*); the applicant stays in your pool for a renamed attempt next turn. The refusal never says **where** the name is borne — that would be free intelligence. The Map Editor applies the same rule to starting lords at export, and your own page catches duplicates within your court as you type.

**A name is plain text of up to 28 characters.** The Hire box takes at most 28 characters, and the Turn Processor enforces the same limit: a name that is longer, is not text, or contains a control character — including the invisible ones that reverse text direction or add zero-width spaces — is refused before any gold is spent (*"Choose another name — up to 28 characters of plain text"*), and the candidate stays in your pool. Spaces at either end are trimmed. Anything else — accents, apostrophes (*Bor'aqh*), any alphabet — is fine: your name reaches other realms' reports as the commander of your armies and fleets, and every page shows it as text, never as code.

**Court size limit: maximum 10 living characters.** Dead characters (fallen in battle, awaiting dismissal) do not count toward the cap — losing a commander in battle immediately frees a slot. The Witch King counts as one living character, so Orc kingdoms can hire at most 9 additional lords. When the court is full:

- The hire button in the Characters panel is disabled and shows **⛔ Court Full (10/10)**.

- A red banner appears above your character list.

- Any hire_character order submitted to the TP is rejected and returns no change (no gold deducted).

- Dismiss a dead or unwanted character to open a slot.

**7.4 Assignments**

|             |                                                              |               |                                        |
|-------------|--------------------------------------------------------------|---------------|----------------------------------------|
| **Key**     | **Role**                                                     | **Stat Used** |                                        |
| army_N      | Commander of Army N                                          | Military      |                                        |
| fleet_N     | Commander of Fleet N *(Orc, Dwarf: unavailable — no fleets)* | Military      |                                        |
| treasury    | Treasurer                                                    | Economics     |                                        |
| farms       | Master of Farms                                              | Management    |                                        |
| mines       | Master of Mines                                              | Management    |                                        |
| ports       | Master of Ports                                              | Management    | *(Orc, Dwarf: unavailable — no ports)* |
| lumbermills | Master of Lumbermills                                        | Management    |                                        |
| quarries    | Master of Quarries                                           | Management    |                                        |
| horses      | Master of Horses                                             | Management    |                                        |
| spy         | Spymaster                                                    | Politics      |                                        |
| none        | Unassigned                                                   | —             |                                        |

These keys are the **only** assignment strings the Turn Processor accepts, and only on assign_character. Anything else is refused with an ⚠ *"Assignment failed"* card and the current role is left untouched. The two race restrictions in the table above are enforced **server-side**: Master of Ports, and fleet command. A **hire always joins the court unassigned** — any assignment written on a hire_character order, valid or not, is ignored and carded; roles are given only through assign_character, which is where the race and one-commander-per-army checks live.

Spy accuracy uses the Politics stat of the character assigned as **Spymaster** (the spy assignment), read from server state at processing time. The Politics value embedded in the order object is ignored. A kingdom with no assigned Spymaster operates at the lowest accuracy tier.

> ***⚠ What this means — one person, one job.** Each character fills exactly one assignment slot, and your court is capped at 10 living characters (§7.3). A lord commanding an army cannot also run the treasury; putting your highest-Politics character on Spymaster duty means they aren't boosting income elsewhere. Match each character's strongest stat to its role — Military → commander, Economics → treasury, Management → a Master of Farms/Mines/Ports, Politics → Spymaster — and decide deliberately which bonuses you are choosing to forgo. With only 10 slots, a kingdom cannot do everything at once.*

**Assignments take effect the same turn.** An assign_character order resolves in Phase 4, so the character commands — and can die — in that same turn's Phase 5/6 battles; there is no travel time or delay, wherever the army or fleet stands. Assigning to an occupied army_N/fleet_N displaces the previous commander to none at once (by design). **Hiring and assigning in the same turn works:** the Player Page sends the hire and a separate assign_character together, and the new character takes the office that turn. What the office does first depends on when its phase runs: a **commander** leads in that turn's battles (Phases 5/6) and a **Spymaster** runs that turn's missions (Phase 7); an **income office** — Treasurer, the Masters of Farms, Mines, Ports, Lumbermills, Quarries and Horses — pays from the **next** turn, because Phase 1 computes income and breeding before Phase 4 assigns.

**7.5 Commander Bonus Formula**

cmdMult = 1 + military / 1000

Military 100 → ×1.10. Military 50 → ×1.05. No commander → ×1.0.

Applies to both attacker and defender combat rolls independently.

**7.6 Economic Bonus Formula**

bonus = stat × 0.2% of the relevant base income.

Management 80 on Farms = 16% bonus food on the farm **and port** food base (§2.9.7). Maximum at stat 100: 20% bonus.

**7.7 Commander Death**

deathChance = min(0.4, lossPct × 0.5)

80% casualties → 40% death chance (maximum) — field, amphibious **and naval** losses follow the soft curve (a seizure contest rolls no commander death): **30%** death chance at the 60% damage-floor cap (about 5:1 to 13:1), climbing with the wipe ramp to the full **40%** from roughly 20:1 (at sea, on its shorter ramp, from 7.5:1); at the walls 40% arrives at 80% casualties. Character becomes dead: true and permanently inactive. **Army and fleet commanders both roll** — a fleet commander on the battle's hull-loss percentage after a naval fight; an army commander aboard a fleet that sinks tests for death at 100% losses — the 40% maximum — while the army itself is lost (§5.9.4). A commander who lives through the loss of his army or fleet — in battle, at sea, with a fallen port, by disbanding or merging it away — is released from command at the end of the turn, with a card saying so, and can be given a new one. A commander you placed on a slot that holds no army or fleet yet keeps that slot. Every commander in a battle rolls on their own side's losses — win, lose or draw, field, walls or sea; there is no threshold below which a commander is safe.

A kill is **reported to the killers** — the opposing side, once each, never saying which army or fleet the commander led; who counts as the opposing side at the walls and at sea is set out in §5.5.5.

**7.8 The Witch King**

Orc kingdoms may be led by a **Witch King** — an undead ruler designated by the GM in the Map Editor at campaign creation. This is a permanent designation and cannot be changed during play.

**Properties:**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| **Property**    | **Value**                                                             |
| Stats           | Each stat rolled 20–100, doubled, capped at 150 (so 40–150 effective) |
| Death           | Immune — combat death check is suppressed entirely                    |
| Dismissal       | Cannot be dismissed; serves for the duration of the campaign          |
| Commander bonus | Military 150 → cmdMult = ×1.15 (maximum possible)                     |

The Witch King appears in the Characters panel with a ☠️ portrait and the title **Undying Ruler of the Horde**. No dismiss button is shown.

**GM note:** The Witch King option is available only to Orc kingdoms in the Map Editor. Enabling it for a kingdom is a campaign-level design decision — it cannot be reverted once the campaign starts.

**7.9 Dismissing a Character**

Characters (other than the Witch King) can be dismissed permanently from the Characters panel.

- **Live character** — press the **✕** button. The character leaves the realm at end of turn and will not appear in the next report.

- **Dead character** — press the **🗑** button. The fallen character's record is removed from GM state and will not appear in future reports.

Dismissal is processed in Phase 4 and is not reversible. Without a dismiss order, dead character records persist in GM state indefinitely (they have no gameplay effect but do occupy the Characters panel).

The Witch King cannot be dismissed. Attempting to dismiss them shows an error notification.

**7.10 Character Experience**

Lords and ladies grow with service. Each stat can rise at most **20% above its original value** (rounded down, minimum +1), never past 150.

- **Military** — +1 per **3 battles** fought by the army or fleet the character

commands. Victory, defeat and draws all count; army and naval battles both count. Fighting the populace militia does not — only battles against a real enemy army or fleet. An idle command earns nothing.

- **Economics / Management / Politics** — +1 per **10 turns** served in an

office of that skill: Treasurer (Economics); Master of Farms, Mines, Ports, Lumbermills, Quarries or Horses (Management); Spymaster (Politics). Turns in different offices of the same skill accumulate — progress survives reassignment, it only pauses while the character holds no such office.

The character card shows each stat's current value against its ceiling and the progress toward the next point. A stat increase is announced in your turn report. The Witch King grows under the same rules (the same min(150, original + 20%) ceiling — 150 is the absolute cap, not his special ceiling). Dead characters gain nothing.

Each commander's card also keeps a **battle record** — victories, draws, and defeats — counted for the same battles that grant military experience above. The record shows on the character card as **W · D · L** and stays visible even for a fallen commander. A lord's tally counts only the battles fought since battle records began in the campaign — an older veteran's record may be short.

**PART VIII — DIPLOMACY & ESPIONAGE**

**8.1 Diplomatic Stances**

Five stances: peace (default), war, alliance, trade, and vassal/liege (structural).

**8.2 Declaring War**

By diplomacy order (Phase 8) or by army contact (Phase 5 auto-declaration, §2.13.8). A war begun this turn blocks any peace, alliance or trade order toward that kingdom in Phase 8 of the same turn; the war stands until next turn (§2.16.2).

**8.3 Making Peace and Alliances**

**Walls override treaties.** Storming or besieging walls declares war on every realm with an army inside, an ally included (§5.6), and an army already **besieged** stays besieged while the ring stands, whatever peace or alliance its realm signs (§2.13.7).

Via Phase 8 diplomacy order; war beats all conflicting orders. Ending a **mutual** alliance or trade pact (✕ *End Alliance*, ✕ *End Trade Pact*) is unilateral and drops both sides to peace — breaking a mutual alliance costs opinion (§8.5.3). Ending a war takes the enemy's consent (🕊 *Propose Peace*), and an alliance takes both kingdoms' orders; passive kingdoms never reciprocate, so they cannot be allied. Cards, notices and withdrawals: §2.16.2.

**8.4 Trade Stance**

Requires independent orders from both kingdoms **and a shared border**, and pays the 0–2%/turn pact gold bonus per mutual partner — which a trade↔alliance pair keeps paying while the upgrade offer stands (§2.9.8). Offers, notices and the *"Diplomacy blocked"* card for a border refusal: §2.16.2.

**8.5 Opinion**

**8.5.1 Scale**

0–100. Default 90. Represents internal popular support. Does not represent inter-kingdom relations.

The Player Page's Profile names the mood beside the figure, following the bands of §8.5.2: **Content** above 50 (no tax lost), **Restless** 41–50 (a small tax penalty, nobody leaves), **Disgruntled** 21–40 (people leave, up to 30% of tax lost), **Rebellious** 20 or below (60–90% of tax lost, 5–10% of the people leave each turn).

**8.5.2 Opinion and Tax Income**

At opinion 50 or below a share of raw tax is lost (PENALTYTAX): 5% at 41–50, 10% at 31–40, 30% at 21–30, 60% at 11–20 and 90% at 0–10 (§2.9.6).

At opinion 40 or below people also leave: no settlement grows, and each loses 1% (31–40), 2.5% (21–30), 5% (11–20) or 10% (0–10) of its people every turn (emigration, §2.9.1).

**8.5.3 How Opinion Changes**

|                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cause**                                                                                                                             | **Effect**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Tax rate held, **every turn** (the rate that collected)                                                                               | +2 per point below 5%, −2 per point above up to 8%, then −10 at 9% and −15 at 10%: +8 at 1% to −15 at 10% (§2.9.13) · changing the rate costs nothing by itself                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Gold deficit                                                                                                                          | −5 to −12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Any battle won** — field, sally/liberation, beach, assault (stormed or repelled), naval, siege auto-fall                            | winner **+1 to +3** · all the victories of one turn together raise opinion by **at most +3** (TP_BATTLE_OPINION_CAP) — **per kingdom**: every realm on the winning side counts its own +3; a card says how much was held back                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Any battle lost** — same list                                                                                                       | loser **−2 to −4** · all the defeats of one turn together lower opinion by **at most −8** (TP_BATTLE_OPINION_LOSS_CAP) — per kingdom; a card says how much was given back                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Settlement stormed / assault repelled — **third-party owner** (someone else's garrison fought for your settlement)                    | owner takes the same swing as the garrison: −2 to −4 on a fall, +1 to +3 on a hold (a hold counts toward the owner's +3 victory cap, a fall toward its −8 defeat cap)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| War declared via diplomacy order (Phase 8), from peace                                                                                | aggressor −3 to −6; the target's opinion does not change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| War declared from movement or combat (Phases 5–6)                                                                                     | aggressor −3 to −8 — **once per step of a march or voyage** (the battle on entering the hex and any arrival clash that step leads to share one charge) and **once per battle** for any other engagement, however many kingdoms the fight drags in; the wars declared on the hex's owner and its occupant as a march step, landing, fleet move, assault or camp/harbour clash begins count toward that charge, a raid or a blockade link war counts as one engagement with the harbour clash at that port, and an origin claim and the march's first step count as two (§2.13.8); every further war is still declared and carded, its effect line reading *"No further opinion penalty — already charged once this step"* inside a march or voyage step and *"… once this battle"* anywhere else; the target's opinion does not change |
| War declared, unilateral, from alliance — **MUTUAL alliances only**                                                                   | aggressor −8 to −15; the target's opinion does not change; betrayal broadcast to every kingdom · declaring war after a one-sided *proposal* the target never reciprocated is an ordinary declaration (−3 to −6, no broadcast)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mutual war (both declare same turn)                                                                                                   | both −1 to −3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Break alliance (peace from alliance) — **MUTUAL alliances only**                                                                      | declarer −2 to −4; target −1 to −3 · both sides carded; withdrawing a one-sided alliance *proposal* the target never reciprocated is free for both                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Downgrade alliance to trade — **MUTUAL alliances only**                                                                               | declarer −1 to −2; target −1 to −2 · both sides carded; withdrawing an unreciprocated proposal is free                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Peace formed (mutual — the war ends only when both sides hold or order peace-or-better; war→alliance/trade orders alone give nothing) | both +1 to +3 · **+0 if the war is less than 3 turns old** (TP_PEACE_OPINION_MIN_WAR_TURNS)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Ceasefire accepted                                                                                                                    | both +2 to +5 · **+0 if the war is less than 3 turns old** (TP_PEACE_OPINION_MIN_WAR_TURNS)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

Floored at 0, capped at 100. Every battle-outcome swing is stated on its own report card (the effect line carries · Opinion +N / · Opinion −N). When the victory cap holds part of a turn's gains back, or the defeat cap gives part of its losses back, one more card says how much, at the end of the turn's combat section — so opinion never moves without a visible cause. The two caps count the battle cards' own figures, and the turn's battles move opinion once, after the last of them: opinion = clamp(opinion + min(wins, +3) − min(losses, 8)), kept inside 0–100 only at that point. So they are separate (a turn of wins and losses keeps up to +3 and up to −8, whatever the order of the battles — from Opinion 10, four +2 wins and five −3 defeats end at 10 + 3 − 8 = 5), and they cover battle outcomes only — war declarations, tax, a gold deficit, peace and ceasefires are never capped.

> ***▶ Example — the victory cap.** At Opinion 60, your five detachments each win a small fight in one turn, rolling +3, +1, +1, +3 and +3: each Victory card shows its own figure (+11 in all), but only +3 counts. Your report adds "Victories this turn: opinion +3 (of +11)" · "Opinion −8 (victory cap +3 a turn)", and you end at 63. Your enemy lost five battles: each Defeat card shows −2 to −4, but at most −8 counts in one turn, and its report adds "Defeats this turn: opinion −8 (of −N)". If an ally fought beside you in those battles, it counts its own +3 too. At Opinion 99 the same five wins still keep only +3 of their +11 — the cap card appears — and opinion stops at 100: min(100, 99 + 3) = 100.*
>
> ***▶ Example — wins and losses in one turn.** Your kingdom starts the turn at Opinion 45, taxing 5%. Early in the turn (Pre-Phase 3) your army storms a village: +3. In Phase 5 you lose four battles (−4, −3, −4, −2 = −13) and win one more (+2).*
>
> *• **Tax and emigration** read **45**, the opinion the turn started with — not the 48 the storm left before Phase 1: 5% of the tax is lost, nobody leaves.*
>
> *• **Victories** landed +5: only +3 counts — "Victories this turn: opinion +3 (of +5)" · "Opinion −2 (victory cap +3 a turn)".*
>
> *• **Defeats** landed −13: only −8 counts — "Defeats this turn: opinion −8 (of −13)" · "Opinion +5 (defeat cap −8 a turn)".*
>
> *• You end at 45 + 3 − 8 = 40: next turn starts in the 31–40 band — 10% of the tax lost and 1% of the people leave.*
>
> *• **Your enemy**, who won four of those battles (say +2, +3, +1, +3 = +9) and lost two (the storm and the last battle, say −3 and −4 = −7), keeps +3 and pays −7 in full (under the −8 cap): net −4.*
>
> ***▶ Example — a declaration on you.** Corvia, at peace with you, orders war on you. Corvia loses 3–6 opinion; yours does not move. Your card reads "Corvia declared war on you" · "No opinion change — a declaration costs only the realm that makes it". If Corvia instead marches onto your land, it pays −3 to −8 and your card reads "Corvia is now at WAR with you!" · "No opinion change for you — a declaration costs only the realm that makes it". Being declared on gains you nothing; winning the battles that follow can (+3 a turn at most).*
>
> ***▶ Example — opinion is a tax on aggression.** Opinion starts at 90 and costs nothing above 50. From 31 to 50 it skims 5–10% off your tax income; at 30 or below it takes 30–90% of it (the PENALTYTAX line on your income card). The real danger is the feedback loop: declaring wars, holding a tax rate above 5% (charged every turn), **and every lost battle (−2 to −4 each)** drag opinion down, and a run of them can push you under 30 exactly when a war demands maximum income — and at 40 or below your people start leaving (§2.9.1). Losses cost more than victories earn (+1 to +3 each and +3 a turn at most, against −2 to −4 each and −8 a turn at most), so a long grinding war erodes even a winner's standing. The sharpest hit is **betrayal** — declaring war on an ally costs −8 to −15 in one stroke, plus a broadcast to every other kingdom. A single alliance-stab can drop you from comfortable to taxed-and-distrusted. Treat opinion as a budget you spend on aggression, and hold the tax rate below 5% (+2 per point, every turn) to recover between wars.*

**8.6 Vassalage**

**8.6.1 Becoming a Vassal**

become_vassal order — an offer the liege accepts or declines with its next orders; requirements, including the rule against chains of vassals and same-turn acceptances, in §2.16.4.

**8.6.2 Tribute**

Rate 1–5% of Phase 1 gold income (tax + port gold, without the Masters' bonuses — not the treasury), default 3%, adjusted by the liege with set_vassal_tribute (§2.16.4). The liege trades protection and a guaranteed peaceful border for a modest, income-scaled cut — the vassal keeps 95–99% of its earnings.

**8.6.3 Leaving**

leave_vassalage ends tribute from the next turn, after one last payment; a war between liege and vassal ends the bond the moment it begins (§2.16.4).

**8.7 Messaging and Ceasefire**

Message limits, the 📢 broadcast and the mutual \[CEASEFIRE\] token are set out in §2.16.5.

\[TRIBUTE: amount resource\] in a message sends resources to the addressed kingdom through the **same caravan system** as the **Shipments → Send Resources** panel, standing rules included (§2.8.2, §2.8.3). Format is an integer amount followed by one of gold, food, iron, horses, wood, or stone — e.g. \[TRIBUTE: 500 gold\] or \[TRIBUTE: 200 wood\]. One tribute per message (only the first \[TRIBUTE:…\] token fires); use separate messages for multiple recipients or commodities. It does not fire inside a broadcast, and its caravan carries a **🏛 tribute** tag on the Shipments lists.

**8.8 Espionage**

**8.8.1 Cost and Requirements**

Cost min(200, 15 + 15 × dist) gold by distance from your nearest owned hex, a loss risk on the same curve, and **maximum 3 spy missions per turn** — full rules in §2.15. Accuracy comes from the character assigned as Spymaster (server-read at processing time). Target any hex by coordinate.

**8.8.2 Report Contents**

After Phase 5 movement: population estimate, site type/level, a 🧱 Fortifications row on any construction hex, and every foreign army present except one in valid Ambush, labelled by its relation to you, with approximate troop count and owner — full contents in §2.15.

**8.8.3 Accuracy Tiers**

Variance, site accuracy, troop estimates and the vary() formula per tier are in §2.15's accuracy table. The tiers also decide the composition assessment: full at \> 75, coarse at \> 50, none at ≤ 50.

**Composition assessment** (two-axis): mounted share is checked first — over ⅔ mounted reads *"Cavalry host — predominantly mounted"*, over ⅓ *"Mixed force — foot and horse"* — then iron equipment by **build-cost** iron: over 40% iron-built units reads *"Heavy armoured infantry — iron-equipped"*, else *"Mixed foot soldiers — standard equipment"*. The mid tier (\>50) sees the vaguer *"Mounted troops sighted"* / *"Heavily armoured troops"* / *"Standard troops"*.

**8.8.4 Elf Territory Penalty**

Targeting a hex owned by an **Elf** kingdom degrades accuracy by one tier, regardless of spymaster Politics. Elven society is uniquely resistant to foreign intelligence-gathering.

|                        |                     |                            |
|------------------------|---------------------|----------------------------|
| **Spymaster Politics** | **Normal Tier**     | **Tier vs. Elf Territory** |
| \> 75                  | High confidence     | Moderate confidence        |
| \> 50                  | Moderate confidence | Low confidence             |
| ≤ 50                   | Low confidence      | Low confidence (unchanged) |

The quality note in both the spy order preview and the final report reflects the degraded tier. This stacks with counter-espionage interference.

> ***▶ Example — what a real spy report looks like.** Your Spymaster has Politics 60 (the \>50 "moderate" tier: ±15% on numbers, site level ±1, commander name shown). You scout an enemy hex that truly holds 1,000 population, a Level-3 mine, and a 200-soldier garrison.*
>
> *• **Population** returns somewhere within ±15% — roughly 850 to 1,150.*
>
> *• **Mine** reads as "about Level 3" (could show Level 2, 3, or 4).*
>
> *• **Troops** report at roughly 170–230, and the enemy commander's name is legible (visible from the \>50 tier up — an elite spymaster is needed only to read the numbers precisely, not to learn who leads).*
>
> *Now make the hex **Elf-owned**: the Elf penalty (§8.8.4) knocks you down one tier to "low" (±30%, a 40% chance to miss the site entirely, and — on a hex that is actually empty — a 25% chance of a false phantom sighting; a real garrison is still never hidden from you by low Politics alone). And if the defender has built **Counter-Espionage ≥ 20%**, whole military rows may vanish from the report on top of that — at **≥ 40%** your agent risks being burned outright. Politics, target race, and enemy counter-intelligence all compound: against a fortified Elf with strong counter-espionage, even an excellent Spymaster brings home little more than guesses. Spy before you commit an army, and never bet a campaign on a single low-tier report.*

**8.8.5 Counter-Espionage Interference**

Defending kingdoms accumulate **Counter-Espionage (CE) strength** by assigning a character to the spy (spymaster) role — CE interference is floor(defending spymaster's Politics × 0.5), so a high-Politics spymaster on defence is what blinds incoming agents. When an incoming spy report is processed, TP measures the CE interference percentage and applies cumulative degradation:

|                     |                                                         |
|---------------------|---------------------------------------------------------|
| **CE Interference** | **Effect**                                              |
| \> 0%               | Population estimates are noisier than usual             |
| ≥ 15%               | Site levels and troop counts may be inaccurate          |
| ≥ 20%               | Some military intelligence rows may be missing entirely |
| ≥ 40%               | **Spy burn risk** — the agent may have been neutralised |

> ***You are never told who took your agent.** A burned spy, a mission lost on the road and a target that turned out to be open water all produce the **same** agent-lost card (§2.15); treat the silence as information about nothing.*

Effects are cumulative: a 40% report degrades all four tiers simultaneously. The spy report card in Player Page displays the exact interference percentage and the active tier warnings. The Elf territory penalty (§8.8.4) and CE interference stack independently.

**8.8.6 Spy Lifecycle**

Each hire_spy order is a one-time intelligence request resolved in Phase 7 — no persistent map unit, no upkeep (§2.15). Every land mission first rolls a baseline loss of min(0.20, 0.05 + 0.015 × dist); a sea-hex target is always lost (charged, no report); on top of that, CE interference at the burn-risk tier (§8.8.5) may burn the agent. All three produce the same generic agent-lost card.

**8.8.7 Gossip & Rumours (Phase 10)**

A realm with a **Spymaster** (the spy office, §7) may spread **one rumour a turn**: a free text of up to 1,000 characters that reaches **every kingdom** — your own, at war, at peace and absent realms alike — as a 🗣 *Rumours spread through the courts* card, the last card of the turn's report (Phase 10). **It carries no sender**: no kingdom can learn who spread it, and nothing in the game traces it. Only the GM's processing log names the author.

- **Price:** round(500 × (1 − Politics / 200)) gold, paid when the rumour spreads — Politics 50 pays 375g, 90 pays 275g, 100 pays 250g, 150 pays 125g. The price is **set aside before Messaging**, so no shipment or \[TRIBUTE\] of that turn can spend it; a rumour that is then not spread (struck by the GM, no Spymaster, nothing written) costs nothing. A realm that cannot pay at that moment has nothing set aside; it spreads the rumour only if it can still pay when Phase 10 comes (gold arriving by caravan counts), and is told so otherwise.

> ***▶ Example.** Your Spymaster has Politics 90 (price 275g) and you end the turn with 3,390g. You queue a rumour and send \[TRIBUTE: 5000 gold\] to an ally. 275g is set aside first; the tribute carries the 3,115g left; the rumour spreads; your treasury ends at 0.*

- **A Spymaster assigned this turn already serves**: Phase 10 runs after the Phase 4 assignments. No Spymaster, nothing spreads (carded).

- **Words only.** A rumour moves no opinion, stance or resource; \[CEASEFIRE\] and \[TRIBUTE\] do nothing inside it. Whether to believe it is the reader's call.

- **The GM sees every rumour before the turn is processed** and may strike one that breaks the Code of Conduct (§1.5); what follows a strike depends on how serious it is (§1.5, rule 6.6). A struck rumour does not spread and costs nothing; its author reads *Rumour not spread — The Game Master struck your rumour — it broke the code of conduct.*

- The Player Page's **Spies** tab holds the rumour box, its price and the reason it is greyed out (no Spymaster, not enough gold).

> ***▶ Example — one rumour, start to finish.** Realm B's Spymaster has Politics 90, so a rumour costs round(500 × (1 − 90/200)) = **275g**. B writes "They say the queen of Belmora keeps a dragon in the cellars" in the Spies tab; the 275g come off at once (cancel, and they come back). In Phase 10 every kingdom — B too — finds the card 🗣 Rumours spread through the courts — "They say the queen…" · Source unknown, last in its report; only B also gets Your rumour spread … −275g. Had B's treasury fallen below 275g by Phase 10 (an upkeep bill, a purchase), the rumour would not spread and B would read Rumour not spread — Spreading it costs 275g … and the treasury holds …g, with nothing charged.*

**PART IX — STRATEGY GUIDE**

**9.1 General Principles**

**Economy compounds; armies depreciate.** Sites generate income every turn. An army costs upkeep every turn. The player who builds faster infrastructure early will outspend opponents in the mid-game without needing to win every battle.

**Opinion is a tax multiplier.** A kingdom at 20 opinion loses 60% of its tax income to unrest, one at 10 or below loses 90%, and at 40 or below its people start leaving (§2.9.6, §2.9.1). Gold deficit triggers desertion and opinion loss simultaneously, creating a cascade: shortfall → fewer soldiers → more shortfall. Avoid this spiral.

**Casualties follow price.** The deathFactor = clamp(0.3–1.0, 1.0 − price×(1+veterancy)/1100) formula (price = the unit's full recruit cost in gold-equivalent) means cheap troops die at the full battle percentage while the costliest units barely bleed — regardless of what else marches beside them. Attack power buys no survival; gold, iron (×16), horses, wood and experience do — food never does.

**The market is a collective state.** Prices move with the volume traded by all kingdoms together — a lone trader barely moves a large market (§2.11.5). If you can anticipate when food will be scarce (after starvation events hit multiple kingdoms), you can profit from pre-positioning.

**9.2 Economy Priorities by Turn Phase**

**Early**: Secure plains with a settlement on them for farms (1000g, guaranteed; a farm needs a construction on the hex and starts paying the turn after it is built, and its harvest is rolled each turn — §3.6.1). Farm food scales with the settlement's population, so the farms that matter are the ones on your biggest towns.

**Mid**: Port upgrades. Port Lv3 on a high-population construction generates substantial dual income (gold + food). The upgrades are deterministic but dear — 10000g (Lv1→2) and 15000g (Lv2→3), on top of the 5000g harbour — so they pay for themselves only once the settlement has real population behind them.

**Late**: Mine upgrades become significant once the mine sits on a populous construction (era maps do not grow a bare mountain hex — the population is the settlement's, §3.2). Mine Lv3 at 600 population = 50 + floor(600 × 3 / 20) = 140 iron/turn. With multiple Dwarven-territory mines, iron surplus enables either direct military production or market leverage.

**9.3 Faction Strategy: Imperial**

Imperial's edge is **reach, not a bonus roll**. Three things are true of the Empire and of nobody else:

- **It recruits everywhere.** The compatibility table (§2.12) is mutual and the Empire is compatible with **every** family, so an Imperial army standing on any foreign construction of a friend can raise that family's two-unit pair — Elf, Dwarf, Orc, Barbarian, Aesir or Nomad. An Elf or a Nomad can do that in three families, an Orc in four. Imperial expansion never runs out of recruiting ground, whoever built the town it stands in.

- **The Legion holds its own walls.** Your armies and militia roll **×1.10** defending your own FI/POP settlements, on top of the walls (§4.2). Nothing else in the game rewards a race for fighting from inside its own stonework.

- **The tallest ladder.** Twenty rungs, the largest population ceilings (50,000) and the tallest walls (25,000) in the game, at the steepest prices at the top (FI17–FI20; the middle rungs sit in the Barbarian band). A grown Imperial seat is the hardest thing on the map to take — and, at 30% of its people in besiegers, effectively assault-only (§5.8.1).

There is **no terrain bonus** and no cheap unit: Praetorians (WP 356, 300g+100i+10f+5w) are the second-highest infantry WP in the game, and the iron makes them dependent on mines. The weighted casualty formula favours them — a Praetorian-heavy army survives at lower loss rates against high-WP defenders. Play the Empire as the power that builds, holds and garrisons, and that turns every ally's town into a recruiting ground.

**9.4 Faction Strategy: Barbarian**

Fast expansion via cheap infantry. Raiders (48 WP, 50g) and Berserkers (55 WP, 40g) have no gold upkeep — they only drain food. An early Barbarian strategy can flood territory quickly before other races can mass elite units.

The risk is food supply — headcount food (§2.10.4) and food-heavy recruitment (Warchief 30f, Wild Archer 20f). Large forces need deep farm income. Hills terrain bonus (×1.15) rewards Barbarian players who position armies on hills for defence.

Storm Horses (WP 85, 120g + 1 horse, 4g upkeep) is a cheap mounted unit (only Bedouin 90g and Warg Rider 100g cost less) — useful for flanking and seizure before opponents build cavalry counters. Keep a horse stock (market or breeding) to field them at scale.

**9.5 Faction Strategy: Elf**

Elf armies pay upkeep in gold only, but still eat headcount food and starve without it (§2.10.4) — low food dependence, not immunity.

Forest terrain (×1.30) is the highest terrain bonus in the game alongside Dwarf mountains. Defending forest hexes with Ranger stacks (WP 174, no food in the recruit cost) is extremely cost-efficient.

Iron dependency is the strategic pressure point. Elf players without mine infrastructure cannot build High Guard (104 iron each) or Elven Cavalry (55 iron each) at scale. Forest prospecting exists but is the worst gamble in the game (5% chance, Lv1 cap) — the market or conquest is usually the cheaper path to iron.

**Intelligence resistance:** All hexes owned by Elf kingdoms impose a one-tier accuracy penalty on enemy spies (see §8.8.4). High-confidence enemy spymasters are degraded to moderate; moderate to low. This makes Elf territory significantly harder to scout — an advantage in defensive campaigns where opponents rely on intelligence to time attacks.

**Weigh your prizes.** The Elf navy is among the fastest afloat — Moonskiffs and White Ships make 3 sea hexes — a pace every race's 90-mp hull can match, but only a fleet kept free of 60-mp hulls (only a pure Aesir Snekkja pack outruns them at 4, §4.7). That speed makes Elves a race with much to *lose* from naval spoils (§2.13.12): a captured 60-mp hull (a Cog, a Galley, a Tigress) drags the whole fleet down to 2 hexes. Take the prize, but park it — transfer slow hulls to a second-line fleet and keep the raiding squadrons pure.

**9.6 Faction Strategy: Orc**

Orc armies grow without recruitment if given time on swamp ground. An army that starts at 50 foot soldiers and is never committed to battle can reach 100+ soldiers after many turns via passive reproduction. This mechanic is most powerful combined with low-cost units (Goblins: 30g, 12f) that reproduce freely.

Food is Orc's central concern. Headcount food (§2.10.4), food-heavy recruitment, reproduction growth and the steep 10–20% starvation penalty mean an Orc horde that outstrips its food supply collapses faster than any other race. Farm infrastructure is existential.

**Feed the Waaagh by winning.** An Orc victor **eats the fallen**, and the food scales with the *headcount* of the dead (§2.13.11) — a large, bloody, decisively-won battle can return more food than a farm yields in a turn, so an Orc that keeps winning land battles can sustain a horde farming alone could not. The catch: you must **win, and win decisively** — a draw or a defeat feeds no one, and a narrow win yields only 20% against 60% for a decisive one. So pick fights you will overrun, and feast between them. And do not spare the villages: fallen **militia** are food too — an Orc conquest of populated land feeds itself as it burns, and even your own townsfolk, fallen defending your walls, return to the larder.

Waaagh Frenzy event (+2 xp_wp to all unit types) is a flat per-unit-type boost — strongest on cheap low-WP units (Barbarian Fury Unchained's ×1.03 beats it on any unit above 67 WP).

**Witch King campaigns:** If the GM assigns a Witch King ruler, the Orc kingdom gains a permanent commander with doubled stats (Military up to 150, cmdMult ×1.15) who cannot die or be dismissed. This is the strongest possible commander bonus in the game. The Witch King cannot lead a fleet — Orc kingdoms cannot build or crew fleets regardless.

**9.7 Faction Strategy: Dwarf**

Iron-first economy is both the strength and the constraint. Dwarves in mountains (×1.30) with Warrior stacks (WP 118, DEF 12) are exceptionally hard to dislodge. Heartguard (WP 237) and Thunderers (WP 278, ATK 16) are the strongest attack options.

The Ale Festival event (+gold) and Vein Strike (+iron) both benefit from large populations — prioritise population-growing hexes.

**Forge exploitation**: A Dwarven army stationed at a forge hex and given no move order gains +2% xp_wp every turn it stays. This compounds: an army sitting on a forge for 10 turns while other armies fight elsewhere will enter the field at significantly higher WP than a freshly raised one. Rotate armies through forge hexes during peacetime to build a permanently superior core force. The forge bonus stacks with battle XP — an army that fights, survives, and then rests at a forge reaches the hard 3× cap faster than any other race can achieve — and stops there.

**9.8 Faction Strategy: Aesir**

Aesir are a plain infantry race on land and the best navy afloat — play the water or you are playing a worse Barbarian. There is **no home-terrain bonus and no movement discount** (every land hex costs the Imperial baseline), and the roster is **all-foot**: no horses to breed or buy, no cavalry terrain scaling, no ×0.65 cavalry tax when storming walls. The racial edge is entirely at sea: **×1.05 on every fleet-battle roll** (attacker or defender, sea or port — roll-only, never shown in WP), the game's **only 120-MP hull** (an all-Snekkja fleet makes **4 sea hexes** a turn where the fastest rivals make 3), and the Busse's **220-capacity** hold.

**Keep the packs pure.** A fleet sails at its slowest hull, so one Longship (90 MP) drops a Snekkja pack to 3 hexes and one Busse (60 MP) to 2. Build two kinds of fleet and never mix them: Snekkja packs (80 men per hull, 3g upkeep) for raiding, blockade and beach extraction; Busse/Longship convoys for the war-band. The same rule governs prizes (§2.13.12) — park a captured 60-MP hull in the slow fleet. Raid pays gold but **declares war** (§2.14.3). The landing itself is still **×0.50** on the beach and costs **−20 status** — win the sea fight first, land unopposed where you can.

**Wood is the Aesir economy.** Every hull costs timber (Snekkja 45w, Longship 75w, Busse 105w), and the **FAS** construction family builds **wooden walls** that track population one-for-one (FAS4 1,000 wall at 1,250g; FAS10 10,000 wall at 22,000g) — each rung's wall increment and every repair_wall is paid in wood. Lumbermills sit on **forest only**; an Aesir kingdom without forest lives off the market (base 5g), tribute, or raid gold. Secure forest before anything else.

**The infantry is honest, not cheap.** Shore Raiders (WP 48, 42g, no gold upkeep) flood a coast; Shield-Karls (WP 110, DEF 10, 16i) hold it; Jarl's Guard (WP 240, 289g + 32i, 10g upkeep) win it. The iron bill climbs steeply, and the casualty formula rewards it: a Jarl's Guard's ~703 gold-equivalent price gives a deathFactor of about 0.36 where a Shore Raider bleeds at ~0.94. Stay off desert and mountain — Aesir pay **16 and 17 status per hex** there, the worst desert rate in the game. Far Raid Returns (+10% income gold, +1.5% pop food) and Whale-Road Bounty (+3% pop food) scale with population, not army size.

**9.9 Faction Strategy: Nomad**

Nomads own the sand and nothing else. **Desert ×1.25** in battle, **desert at 30 MP** where every other race pays 60 (a Nomad foot army makes 2 desert hexes a turn, an all-mounted one 3, an invader 1), **Nomad cavalry exempt from the ×0.85 desert cavalry penalty**, and only **10 status per desert hex** against everyone else's 14–16. An all-Bedouin/Askari force crosses three desert hexes for 30 readiness and is back at full strength (+33/turn rest) before an enemy column has cleared one dune. Off the sand you are the lowest-WP roster in the game (ceiling Askari 143) with no terrain help — fight where the map says you fight.

**Mounted-heavy is the doctrine, not an option.** A Nomad rider eats **1 food per head**, not the 2 every other cavalry pays — a hundred Askari cost 100 food/turn where a hundred Elven Cavalry cost 200. Bedouin (WP 88, 90g + 1 horse, 3g upkeep) and Askari (WP 143, 180g + 1 horse, 5g upkeep) are the cheapest sustained cavalry in the game, provided the horse supply holds: breed (§2.9.9) or buy, because every rider costs a horse. On plains they still get the **×1.20** open-ground bonus; in forest, swamp and mountain they are taxed 0.70/0.60/0.70 like anyone's — never ride into trees.

**Walls are where the Askari dies.** The cavalry assault rule charges every mounted war-point **×0.65** when storming walls, desert-bred or not. Siege with Mangonels (250 wall damage), starve, or send Rumat (WP 86, 5i) and Naffatun (WP 50, no gold upkeep) into the breach, and keep the riders for the open field — or an ordered Sally (§2.13.7). The Rajjala (WP 26, 20g, no upkeep, deathFactor ~0.97) is militia with a spear: a body count for seizures, never a line.

**Nomad camps move** (§2.11.10) — the people and the palisade travel; the sites do not. That is the trade: mobility is the compensation for the weakest walls in the game, and the price is the mine or port you walk away from. Use it to chase a frontier, to slip a low camp out of a slow campaign of conquest, or to put your seat somewhere an enemy did not plan for — never to dodge a battle already joined, because the move resolves after the fighting.

**Nomad settlements are camps, not castles.** The **FNO** family has **ten** wooden rungs and founds straight into **FNO1** — the settler camp (100 pop, no wall, free). The rungs are cheap and quick (FNO2 500 pop for 500g + 100 wood; FNO5 2,000 pop for 2,000g; FNO10 15,000 pop for 30,000g — 77,750g and 1,000 wood for the whole ladder) but the walls never pass 1,000 points, so a Nomad seat is never a fortress: the bonus tops out near ×1.6 and one engine hit clears any rung below Lv.6. Hold ground with riders, and keep the seat's population high — that, not the palisade, is what an assault has to chew through. Timber comes from a forest lumbermill or the market (base 5g); desert hexes offer neither. Population is the Nomad's real wealth: Caravan Tolls (+12% of income) and Oasis Bloom (+3% pop food) pay on it, and desert hexes prospect for mines (7%, Lv2 cap) nobody will cross the sand to take. Foreign recruiting is thin — Nomads muster only at **Imperial and Barbarian** constructions (§2.12).

**9.10 Defensive Play**

**Stance priority for pure defence**: in the open field Ambush (×1.40) \> Defensive = Garrison (×1.20 — a Garrison counts as Defensive outside a storm); behind walls only Garrison (×1.30) stands at all — every other stance is outside them (§5.8.0).

**A valid Ambush stands apart from the walls.** Use it to make any attacker beat a hidden army in the open before it reaches your gates — and a link can carry an ambusher in or a garrison out (§5.8.0 Cases E and F). It is a one-shot: once it fights it is spent, so a second attacker meets an ordinary field army (§5.4).

**Only a Garrison stands behind the walls** (×1.30, fortress, militia — §5.8.0); an army left outside on Defensive fights the attacker first and, beaten, goes inside to defend the storm. Once **besieged** (§2.13.7) your only way to fight is a **Sally** — in the open, with no stance bonus and no walls: order it when the besieger is weak enough to beat there; otherwise stay behind the walls, and remember that a siege that runs its course ends with every army of the owner inside surrendering.

Stances are **stored** (§5.4), so an Ambush filed turns ago still holds the outside zone. A **besieged** army is offered only Garrison and 🚪 Sally, and cannot queue a march (§2.13.7).

**Fortress bonus stacks with stance**. Garrison behind a 15,000+ wall at your muster seat: garrisonWP × 1.30 × 7.10 = garrisonWP × 9.23 before militia (7.10 = the r=1 curve plus the +0.10 seat, at full integrity) — and only while the wall is whole (§5.6.1). Keeping it repaired is the single highest-leverage defensive act in the game.

**Siege defence**: only driving the besieger off — a winning Sally, a relief army from outside, or a third party's attack — or the besieger ceasing to press prevents the auto-fall (§5.8.5); a drawn Sally only buys a turn, and a besieger too weak for the §5.8.1 gate still holds your armies inside. Besieged settlements still produce income as long as they haven't fallen, so waiting pays only while help is on the way: the besieger must hold siege stance on the hex for all 5 turns (6 against a muster seat).

**9.11 Naval Strategy**

**Port modifier ×1.25**: fight at your own or a friend's port with a fleet that **began the turn there** (§5.9.2), whether defending or attacking an intruder; a fleet that sails in earns nothing, and neither does anyone at an enemy or neutral harbour, so a blockader or squatter fights without it. Keep a fleet docked at home before committing to offensive naval operations.

**Cargo penalty ×0.85**: A fleet transporting an army fights at reduced strength. Win sea control before loading armies.

**Blockade**: it needs war and a berth inside the enemy port (§2.9.3) — an undefended port costs nothing but the sail in, a defended one must be won first against the port bonus. Holding a high-level enemy port removes a major income source without storming its walls.

**Raid**: a raid takes a share of a foreign port's Phase 1 gold, capped by what the owner holds, and is always an act of war — on the owner and on its friends moored there (§2.14.3). A raid under sail must beat a defended harbour before any gold changes hands, so the easy raids are on empty harbours; an anchor raid plunders first and fights after, and still lets the fleet leave the same turn. Every raiding turn costs the fleet 3 status and the raided port gives no rest (§5.10.6), so a fleet that raids turn after turn wears down. Time your raids for wars you actually want, or wars already underway.

**Transport and disembark**: Amphibious battle is high-risk — only an outright attacker victory seizes the hex. A draw is a stalemate: your army re-boards with casualties (on foreign walls it digs in at the gates, §5.7.2) and the defender holds. Only commit to a beach landing when you have a clear WP advantage; a costly stalemate leaves your army reduced and still at sea. Use beach landings as a second front when you can guarantee the numbers, not as a low-cost probe.

**Beach extraction — sea control buys extraction**: a beachhead is not married to a port — an escort fleet anchored next to the landing can lift the army straight back off next turn, whoever owns that ground (§2.14.6). This cuts both ways: **a coastal siege leaks unless the besieger also brings sea power** — a besieged garrison with one of its own hulls at anchor offshore can board it and sail away the turn after. Deny the extraction, not just the port: patrol or blockade the adjacent sea hexes, or the siege you think you're winning empties out from under you. Budget the readiness too: each pickup costs the fleet **−15 status** and its turn (§5.10.6), so an extraction fleet used repeatedly will arrive tired and slow to the next job.

**9.12 Diplomatic Manipulation**

**Opinion leveraging**: betraying a mutual ally is the largest single opinion hit in the game (§8.5.3). If you are about to be eliminated, breaking an alliance to go to war costs you more than the war itself.

**Ceasefire timing**: a mutual \[CEASEFIRE\] (§2.16.5) makes peace in the same turn, with no diplomatic order to wait on — agree it with the other side and send both messages together when you need to pivot quickly. It pays opinion only once the war is 3 turns old (§2.16.5).

**Pact stacking**: Each mutual pact — trade **or** alliance — contributes a 0–2% gold bonus independently per turn. Three mutual partners average ~3% bonus gold (0–6% range). It scales with income, so richer players get more absolute value. At most 5 partners pay in a turn, so pact income tops out at 10% of tax + ports — up to five allies are an economic engine; beyond five, allies are for war, not gold.

**Alliance betrayal broadcast**: All other kingdoms receive a notification when an alliance is broken for war. This can be diplomatically exploited — if your target is universally unpopular, the betrayal broadcast will be ignored. If you have many allies, the broadcast may cost you more than the war.

**PART X — GLOSSARY & REFERENCE**

**10.1 Glossary**

**Alliance** — Diplomatic stance, **mutual only**: both kingdoms must declare it, or it is inert. Prevents mutual combat, enables joint operations and pays the 0–2% pact gold bonus with no border needed. §2.16.1, §2.9.8.

**Ambush** — Army stance: ×1.40 to defRoll when defending, valid only for an Elf army in forest or a Dwarf army in mountain. Stands outside its walls, hidden from maps and spies, and is spent once it fights. §5.4.

**Camp sweep** — Start of Phase 5: armies already at war camped in the same zone of one hex fight before anyone marches; no hex changes hands, a besieged loser stays inside its walls, and the owner's or a friend's loser outside its walls goes inside in Garrison. §2.13.5.

**Arrival clash** — An army, or a link member carried in behind it, that ends a march step in the zone of an army it is at war with attacks at once. Fleets likewise. §5.11, §2.14.7.

**Cohabitation sweep** — Start of Phase 6: fleets at war sharing a hex or port fight before movement; the port owner or a friend of it defends. Land twin: the *camp sweep*. §2.14.2.

**Pirate** — Not a race: a Barbarian-subset flag per kingdom (§4.3.1). Identical mechanics to Barbarian; ×1.10 fleet-battle WP, the Hunt fleet stance (§2.14.9), own shields/art/titles, and the UI race label reads Pirate.

**Army** — A collection of unit stacks belonging to one kingdom, occupying a single hex.

**Assault** — Combat order targeting a hex with a walled construction.

**ATK** — Attack stat. Reference value; War Points is the actual combat value.

**Base WP** — The War Points value from the unit roster, before experience modification.

**Besieged (army)** — Inside walls under an enemy siege ring, from the turn after the ring is laid (§2.13.7) and for as long as it stands, whatever peace or alliance is signed: Garrison or Sally only, no march, embarking open (§2.13.7).

**Besieged By** — The kingdom ID recorded on a hex actively under siege.

**Blockade** — Fleet stance: a fleet lying inside an enemy port, at war, suppresses its gold and food; stored while it bites, −2 status a turn, linked fleets party to it. §2.9.3, §2.14.7.

**Blueprint** — The flat **500-gold** fee every founding order pays, whatever the family or tier, on top of the settlers and the wall material. §2.11.9.

**Bystander** — An army on a battle hex that takes no part — at peace with the attacker and outside the defender's link, or *held back*; never one inside walls. It then stays, withdraws or makes a last stand. §5.11, §5.6.

**Capital** — The hex the GM designates as a kingdom's **muster seat** (§3.7.3); not a terrain. +0.10 fortress bonus and siege threshold 5; if lost, the seat succeeds as in §2.13.10.

**Cargo Penalty** — ×0.85 naval combat modifier for a fleet transporting an army.

**Construction** — A settlement placed on a hex, of one of eight racial families, standing at a level on that family's ladder. Carries **all** the hex's population, its wall, and its militia. A hex without one is empty ground. §3.7.

**Commander Death** — Permanent loss of a character after combat (chance = min(0.4, lossPct×0.5)).

**DEF** — Defence stat. Reference value.

**Defensive** — Army stance. ×1.20 to defRoll. On walls it stands outside, in the open (§5.8.0).

**Disembark** — Landing a transported army from a fleet onto a land hex.

**Embark** — Putting your own army aboard your own fleet: a **port** embark only in a port you own, a **beach** embark from any land but a mountain, with the fleet at anchor next to it. §2.14.5, §2.14.6.

**Fleet** — A collection of ship stacks belonging to one kingdom on a sea or port hex.

**Forge** — Dwarf-only site the GM places at campaign start on a Dwarf (FDW) construction; stationary Dwarven armies there gain +2% xp_wp a turn. Never beside a mine. §3.6.4, §5.3.2.

**Fog of War** — Visibility: Full on own hexes, Border on adjacent, spied and army/fleet hexes, Remembered on hexes once seen, Hidden elsewhere; forces met on a route are reported that turn. §2.18, §2.19, §2.13.2.

**Legion** — The Imperial battle identity: ×1.10 for an Imperial army and the militia defending, or sallying from, an owned FI or POP settlement; never as attacker elsewhere, never for an ally. §4.2.

**Fortress Bonus** — Defender's assault multiplier from wall **size**, scaled by wall **integrity**: ×1.55 (palisade) to ×7.10 (a 15,000+ wall at the muster seat); a breached wall gives ×1.00. §5.6.1.

**Founding Tier** — The level a founding order plants a settlement at: Level 1 for every family except Orc, which founds at a wall-less **Level 0** (100 population) reached only by founding. §2.11.9, §3.7.4.

**Founding Turn (combat inertia)** — A construction founded this turn fights as **unfortified** open ground for the rest of that turn, though its wall already stands at full integrity. §2.11.9.

**Muster Seat** — The hex new armies muster at: the GM-designated capital, or, if that is lost, the greatest surviving construction by its level's population ceiling (headcount breaks ties). §2.13.10, §3.7.3.

**Siege Engine** — Per-race unit (Onager, Trebuchet, War Catapult …) that knocks **250 points of wall** down per turn under a siege order; 5 crew each, only crewed engines fire. §5.8.6, §2.12.1.

**Wall Integrity** — A construction's current wall as a fraction of its level's maximum. Scales the fortress bonus and the attacker's penalty continuously; at 0 the settlement is **breached** and fights as if unwalled. §3.7.2.

**Camp move** — A Nomad kingdom re-pitching one FNO camp up to 2 hexes on its own land, for 1,000g, at the end of the turn; the camp then rests 6 turns. §2.11.10.

**Wall Material** — The stone or wood a construction's walls are built from, fixed by its **family** (wood for Aesir, Orc and Nomad, stone for the rest) — not by its owner's race. §2.11.7.

**Garrison** — The only army stance behind walls: ×1.30 to defRoll against a storm (×1.20 in the open), with the fortress and the militia; every other stance stands outside. §5.8.0, §5.4.

**GM State** — The authoritative game state maintained and distributed by the Turn Processor.

**HP** — Hit Points. Reference value.

**Held back** — Card for an army that stands aside, losing nothing, because its kingdom also attacks in that battle (§5.11.1); *held back from the sally* marks a besieged army barred from a sally (§2.13.7); *Army N left X's group* marks a link member that left rather than fight a friend at its walls (§5.11.1).

**Hunt** — Pirate-only fleet stance: attacks a weaker non-allied fleet it meets without declaring war; the fleet bleeds status while hunting (§2.14.9).

**Initiative** — Per-roll multiplier for attacker: 1.05–1.10. Represents first-move advantage.

**Iron** — Resource. Used in unit/ship production and some upkeep.

**Link** — A standing order that joins up to 3 co-located armies under a leader: members move, take its stance and stand in its zone. §5.11.

**Liege** — A kingdom that holds one or more vassals (§2.16.4).

**Militia** — Automatic defenders raised from a construction's population. floor(pop × 0.05) units (5% of population) each worth 20 WP, so militia WP ≈ the population.

**Mounted** — Unit type. Consumes 2 food/turn (foot units 1); Nomad mounted eat 1.

**ODD-R** — The hex grid coordinate system used by TREVASXXI.

**Opinion** — Internal popularity metric (0–100, default 90). Affects tax income (§2.9.6) and, at 40 or below, population (emigration, §2.9.1); the tax rate you hold moves it every turn (§2.9.13).

**Option A** — The state reset architecture: TP discards all player-submitted state before processing; a realm with no saved state is checked and rebuilt instead (§2.5).

**Peace** — Default diplomatic stance. No combat, no bonus.

**Phase** — A named step in the turn sequence.

**Population** — Per-hex inhabitant count. Grows 1–3%/turn. Drives tax, site income, and militia.

**Port Modifier** — ×1.25 naval bonus, attacker or defender, for a fleet at a **friendly** port (own, mutual ally, liege or vassal) that began the turn there; ×1.00 otherwise. §5.9.2.

**Raid** — Fleet stance, per turn: plunders the foreign port it lies in and every foreign port its voyage sails into; always an act of war; −3 status in a turn it plunders. §2.14.3, §5.10.6. **Route sightings** — When your army or fleet steps into a hex where a foreign force stands, both sides are told, even if they end the turn out of sight. Route sightings, §2.13.2 and §2.14.1.

**Sally** — Per-turn stance of a **besieged** army: with every other besieged army that orders it, it fights the besiegers in the open in Pre-Phase 3 (§2.13.7). Nobody sallies unordered.

**Settlers** — The **100 people** a founding order marches out of the muster seat. The seat must hold **300** at processing time; a seat whose ceiling is below 300 can never found until upgraded. §2.11.9.

**Siege Progress** — Counter on a besieged hex. Increments by 1 each turn the ring is pressed — one besieging kingdom per hex (§5.8.2).

**Siege Threshold** — 4 for an ordinary walled construction, 5 for the muster seat. Hex falls when progress strictly exceeds this. A wall-less construction cannot be besieged at all.

**Spoils of War** — Iron and horses (and Orc food) salvaged from the fallen after a won land battle: 20–60% of build cost by margin, 60–80% from a surrendered garrison; none at sea. §2.13.11.

**Prize Ships** — Hulls taken from the ships the loser lost in a won sea battle: each is captured on a d6 roll of 1–4, sunk on 5–6; they keep their stats and join with green crews. §2.13.12.

**Stance** — Diplomatic status (peace/war/alliance/trade) or army posture.

**Trade** — Diplomatic stance, mutual only, that **requires a shared border**: it pays the 0–2% pact gold bonus per partner per turn only while the two realms still border. §2.16.1, §2.9.8.

**Turn Processor** — The authoritative GM application that resolves all orders.

**Upkeep** — Per-unit/ship resource cost paid in Phase 2.

**Variance** — The 0.90 + rand×0.20 luck multiplier applied to every combat roll, both sides, independently (range 0.90–1.10; BATTLE_VARIANCE = 0.10, ±10 %).

**Vassal** — A kingdom paying tribute to a liege, in alliance with it for as long as the bond lasts: a war between the two ends it (§2.16.4).

**War Points (WP)** — The sole combat value used in all rolls.

**Weighted Casualties** — Formula by which stronger units within an army die proportionally less.

**xp_wp** — A unit stack's current experienced War Points. Starts at base WP; grows with combat.

**10.2 Full Combat Formula Reference**

**Field Battle:**

initiative = 1.05 + rand×0.05

variance = 0.90 + rand×0.20 (BATTLE_VARIANCE = 0.10 → ±10 %, independent per roll)

cmdMult = 1 + military/1000

attRoll = attWP × status × attTerrainMult × attCavTerrainScale × initiative × attCmdMult × variance

defRoll = defWP × status × defTerrainMult × defCavTerrainScale × defStanceMod × defCmdMult × legion × variance

(cavTerrainScale: each side's mounted WP share scaled by terrain, §5.5; garrison stance counts as defensive ×1.20 here)

Outcome: attRoll \> defRoll×1.2 → att wins; defRoll \> attRoll×1.2 → def wins; else draw

Att wins: attLoss=0.10/ratio; defLoss=softLossPct(ratio)

Draw: attLoss=defLoss=0.06+rand×0.06

Def wins: defLoss=0.10/ratio; attLoss=softLossPct(ratio)

softLossPct(r): base=min(0.50, 0.12+0.18×ln r); floored=max(base, min(0.60, 0.12×r)) (damage floor)

r≤10 → floored; r\>10 → max(floored, min(1.0, 0.50+0.50×(r−10)/15)) (wipe ramp; 1.0 at 25:1)

(destroyed only when no retreat hex — §5.5.6)

**Assault:**

militiaWP = floor(pop × 0.05) × 20

integrity = wall_hp / wallMax

fortressBase = max(1.5 + 1.5×r, 1 + 6×r), r = min(1, wallMax/15000) (+0.10 muster seat)

fortressBonus = 1 + (fortressBase − 1) × integrity // 1.00 when breached or unwalled

attPenalty = 1 − 0.15 × integrity // 0.85 whole … 1.00 breached

attRoll = attWP × status × attTerrainMult × attCavAssaultScale × attPenalty × initiative × attCmdMult × variance

defRoll = (garrisonWP × status × defStanceMod × defCavTerrainScale + militiaWP) × fortressBonus × defTerrainMult × defCmdMult × legion × variance

(legion = 1.10 for an Imperial owner of an FI/POP settlement, §4.2 — on the defender in every resolver, and on the ATTACKER only when the attacker is the owner sallying out)

(attCavAssaultScale: attacker's mounted WP share ×0.65; defCavTerrainScale as in field, §5.5)

Att wins: attLoss=0.15/ratio; defLoss=ratio≥5?1.0:min(0.95,0.25×ratio)

Draw: attLoss=defLoss=0.10+rand×0.08

Def wins: defLoss=0.12/ratio; attLoss=ratio≥5?1.0:min(0.95,0.30×ratio)

**Amphibious Battle:**

attRoll = attWP × status × 0.50 × initiative × attCmdMult × variance

defRoll = defWP × status × defStanceMod × defCmdMult × legion × variance

(no terrain mult; draw = stalemate, attacker re-boards — digs in on foreign walls)

Att wins: attLoss=0.10/ratio; defLoss=softLossPct(ratio) (same soft curve as field, floor and ramp included)

Draw: attLoss=0.08+rand×0.06; defLoss=0.05+rand×0.05

Def wins: defLoss=0.10/ratio; attLoss=softLossPct(ratio)

**Naval Battle:**

portMod = 1.25 per fleet, attacker or defender, at a FRIENDLY port (own / ally / liege / vassal) where it began the turn, else 1.0

cargoMod = 0.85 if transporting army, else 1.0

attWP = fleetPower × fleetStatus (each side's own STATUS, §5.10 — applied here, once)

attRoll = attWP × portMod × initiative × attCmdMult × attCargoMod × attRaceMod × variance

defRoll = defWP × portMod × defCmdMult × defCargoMod × defRaceMod × variance

Att wins: attLoss=0.10/ratio; defLoss=softLossPct(ratio, sea ramp) (the field curve up to 5:1, then the sea's own ramp)

Draw: attLoss=defLoss=0.06+rand×0.06

Def wins: defLoss=0.10/ratio; attLoss=softLossPct(ratio, sea ramp)

softLossPct(r, sea ramp): r≤5 → floored (as field); r\>5 → max(floored, min(1.0, 0.60+0.40×(r−5)/5)) (1.0 at 10:1)

(the loser's armour dissolves on the same 5:1 → 10:1 schedule; minimum one hull; a total wipe at 10:1 goes through the ≥1.0 bypass — see §5.9.3)

**Weighted Casualties:**

price (g-eq) = gold + iron×12 + horses×20 + wood×5 (equipment; rations buy nothing)

deathFactor = clamp(0.3 … 1.0, 1.0 − price × (1 + max(0, xp_wp/baseWP − 1)) / 1100)

rawLoss = count × lossPct × deathFactor

loss = round(rawLoss)

(if lossPct≥1.0: entire army wiped, distribution bypassed — assault ratios ≥ 5 reach it directly; field, amphibious and militia-seizure reach it at 25:1 through the wipe ramp and sit at the 0.60 damage-floor cap below 10:1)

**Naval Weighted Casualties:**

price (g-eq) = gold + iron×12 + horses×20 + wood×5 (equipment; rations buy nothing)

deathFactor = clamp(0.20 … 1.5, 0.9 − price × (1 + max(0, xp_wp/baseWP − 1)) / 4900)

rawLoss = count × lossPct × deathFactor

loss = round(rawLoss)

(the ≥1.0 wipe bypass is reached at sea at 10:1, through the sea's 5:1 → 10:1 ramp; above 5:1 deathFactor → df + (1 − df) × (r − 5)/5)

**Commander Death:**

deathChance = min(0.4, lossPct × 0.5)

**XP Gain:**

roll = 1 + (0.03 + rand×0.02) × clamp(0, 1, oppFactor) (×1.03 to ×1.05 at full opposition)

cap = baseWP × 3

new = min(cap, round(xp_wp × roll))

**10.3 Full Income Formula Reference**

terrainGold = 0

terrainFood = plainsWithoutSiteCount × 1

farmFood = Σ max(1, floor(pop × rate)) per populated farm rate: ROLLED per farm per turn — Lv1 \[0.05,0.25\], Lv2 \[0.20,0.50\], Lv3 \[0.40,0.80\] (§2.9.4)

mineIron = Σ base\[level\] + floor(pop × siteLevel / 20) base: Lv1=10, Lv2=20, Lv3=50

portGold = Σ floor(pop × goldMult) goldMult: Lv1=0.20, Lv2=0.40, Lv3=0.60

portFood = Σ floor(pop × foodRate) foodRate: ROLLED per port per turn at EVERY level — Lv1 \[0,0.05\], Lv2 \[0,0.10\], Lv3 \[0,0.15\]; a 0 pays 0

× bracketFactor per port: rank ports by gold DESC; factor = max(0, 1 − floor((rank−1)/5) × 0.10)

(blockaded ports contribute 0 but keep their rank slot)

forgeXP = +2% (fixed) to unit xp_wp (Dwarf armies, stationary, at forge hex, end of turn)

emigPct = opinion\<=10?10 : opinion\<=20?5 : opinion\<=30?2.5 : opinion\<=40?1 : 0 (TP_EMIGRATION_BANDS, start-of-turn opinion; replaces growth, before income)

pop −= max(1, floor(pop × emigPct / 100)) per populated settlement when emigPct \> 0

rawTax = floor(totalPop × taxRate / 100)

penaltyPct = opinion\<=10?90 : opinion\<=20?60 : opinion\<=30?30 : opinion\<=40?10 : opinion\<=50?5 : 0 (TP_TAX_PENALTY_BANDS, start-of-turn opinion)

netTax = max(0, rawTax − floor(rawTax × penaltyPct / 100))

opinion += (TP_TAX_OPINION_NEUTRAL − taxRate) × TP_TAX_OPINION_PER_POINT (9% and 10%: −TP_TAX_OPINION_TOP instead; right after the tax, kept inside 0–100; a tax_change applies after this)

baseGold = netTax + portGold

treasGold = floor(netTax × economics × 0.2 / 100)

farmBonus = floor((farmFood+portFood) × management × 0.2 / 100)

mineBonus = floor(mineIron × management × 0.2 / 100)

portBonus = floor(portGold × management × 0.2 / 100)

tradeBonus = Σ per paying pact partner: floor(baseGold × pct / 100)

pact pays if: mutual alliance (no border needed), or mutual trade / mixed trade+alliance with a shared border

where pct = floor(rand×3) (0, 1, or 2% — some turns a pact pays nothing)

totalGold = baseGold + treasGold + portBonus + tradeBonus

totalFood = terrainFood + farmFood + portFood + farmBonus

totalIron = mineIron + mineBonus

totalWood = lumberWood + lumberBonus (lumbermills on forest hexes)

totalStone = quarryStone + quarryBonus (quarries on plains/hills/mountain)

Vassal tribute deducted from totalGold after calculation: floor(tributeBase × tributeRate / 100).

**10.4 Random Events Reference**

There are no random events (§2.17).

**10.5 Terrain Quick Reference**

**City and Capital are not terrains** — settlement is a construction placed *on* a terrain (§3.7), and terrain carries no population of its own.

|             |                          |               |                  |                                                                         |
|-------------|--------------------------|---------------|------------------|-------------------------------------------------------------------------|
| **Terrain** | **Population**           | **Food/Turn** | **Combat Bonus** | **Sites allowed**                                                       |
| Plains      | Only from a construction | +1f (no site) | —                | Farm, Mine (7%), Port, Quarry                                           |
| Hills       | Only from a construction | —             | Barbarian ×1.15  | Mine (15%), Quarry                                                      |
| Forest      | Only from a construction | —             | Elf ×1.30        | Mine (5%), Lumbermill, **Port (Elf only, coastal, Elven construction)** |
| Mountain    | Only from a construction | —             | Dwarf ×1.30      | Mine (25%), Quarry                                                      |
| Swamp       | Only from a construction | —             | Orc ×1.20        | —                                                                       |
| Desert      | Only from a construction | —             | Nomad ×1.25      | Mine (7%)                                                               |
| Sea         | None                     | —             | —                | —                                                                       |

**Imperial and Aesir have no land terrain bonus** (the Aesir bonus is naval — §5.9; the Imperial bonus is construction-keyed — the Legion, §4.2). Mounted units additionally scale with terrain — see §3.5.1.

Militia and seizure strength come from the **construction's population**, not from terrain (§3.8). A bare hex mints no militia at all, whatever it is made of.

**10.6 Turn Sequence Quick Reference**

Pre-Phase 1 Option A State Reset — TP discards player state, uses gmState

Pre-Phase 2 Create/Disband/Embark re-applied

Pre-Phase 2b Recruitment (§2.6a) — paid before income; pop from the PRE-growth population (5% own / 1% allied cap); engines built. Recruits fight every battle below.

Pre-Phase 3 Siege & Assault — besieged armies fixed (march refused, Garrison/Sally only); ordered sallies fought first (after link members friendly to the owner leave a hostile group, §5.11.1 rule 3); then STATIONARY besiegers tick — one with an army not friendly to it (a neutral included) camped outside fights it instead and makes no progress that turn; Assault stances fight the armies outside, then storm (all before income)

Pre-Phase 4 Siege Auto-Fall — hexes with progress \> threshold transfer

Phase 1 Population Growth (1–3% per hex) — or, at opinion 40 or below, emigration instead (§2.9.1)

\+ Terrain income (plains +1f; no terrain gold)

\+ Blockade suppression check

\+ Site income (farms→food, mines→iron, ports→gold+food, lumbermills→wood, quarries→stone)

\+ Population tax (taxRate%, opinion penalty applied), then opinion moves by the rate that collected (§2.9.13)

\+ Character bonuses (treasurer, masters, ports)

\+ Trade/alliance pact bonuses (0–2% per mutual partner)

\+ Horse breeding (1–3%, + a Master of Horses' points)

\+ Orc reproduction (5–7% foot per army if foot≥10 and on swamp)

\+ Vassal tribute deducted/paid

\+ Tax rate change (new rate next turn; the change itself moves no opinion)

\+ Blockade link wars — declared after every kingdom's Phase 1 (§2.14.7)

Phase 2 Gold upkeep deducted → deficit: 5–15% desertion (rounded down per stack — never a last soldier), opinion −5 to −12

\+ Iron upkeep deducted (no consequence on shortfall)

\+ Food consumption (foot 1, mounted 2; Nomad mounted 1)

→ Starvation if shortage: Orc 10–20%, others 3–10%

Phase 3 Market buy/sell orders executed FIRST, kingdom by kingdom (a sale pays for this turn's builds)

\+ Build/upgrade/found/camp-move orders processed

\+ Market price adjustment (net traded volume vs depth, ±15% a turn)

Phase 4 Ships & Hire — build ships (fleet docked at an OWN port; crew from port pop)

\+ Hire (1000g default) / assign / dismiss characters

Phase 5 Camp sweep: armies at war camped in one zone of a hex fight first (§2.13.5)

Phase 5 Army move orders ranked by STATUS (highest first; random among exact ties)

\+ Hex-by-hex movement: seizure (populace-militia WP contest) / field battle / assault / Siege March camp (lays siege; the ring closes at once if strong enough, progress from next turn)

\+ Auto war declaration on enemy hex entry

\+ Victors of a decisive land battle claim spoils — iron/horses (Orc: +food from the fallen), §2.13.11

Phase 6 Anchor raids: Raid-stance fleets docked in a foreign port plunder it (§2.14.3)

\+ Cohabitation sweep — at-war fleets sharing a hex fight before movement (§2.14.2); the port owner or its friend defends, ×1.25 only if it began the turn there; a new fleet with no hulls is scuttled

\+ Fleet move orders ranked by STATUS (highest first; random among exact ties)

\+ Hex-by-hex movement: port entry (any port) / naval combat — a CLEAR victory sails on, a draw or defeat ends the voyage

\+ Raid under sail, at each foreign port entered: war, harbour fight, plunder only on a CLEAR win, sail on (§2.14.3)

\+ Disembarkation (AFTER all fleet movement): landings at the ×0.50 beach

penalty can seize a coastal hex — land conquest also happens here (§2.14.6)

\+ Victors of a naval battle take prize ships — each hull the loser lost in the fight is captured on a d6 roll of 1–4, §2.13.12

Phase 7 Spy intelligence reports generated (post-Phase-5 positions)

Phase 8 Diplomacy orders (war beats all; no peace/alliance/trade toward a kingdom you went to war with this turn, by any route)

Phase 8 ·V Vassalage — last turn's oaths answered (vassal_offer_reply), then leave_vassalage, then become_vassal (an offer), then set_vassal_tribute; a liege–vassal war has already ended the bond (runs BEFORE messaging)

Phase 8 ·M Messages (up to 3; \[CEASEFIRE\] auto-peace if mutual; \[TRIBUTE: n res\], §2.8.3)

End of turn Resource Transfers — last turn's accepted offers, then send_resource (\[TRIBUTE\] already left in Phase 8 ·M) (surplus only, applied after all spending)

Sweeps Empty-force & link-integrity sweeps

Forge Dwarf armies stationed at a Forge site gain XP

Phase 10 Gossip & Rumours — one anonymous rumour per realm with a Spymaster, to every kingdom; a rumour the GM struck spreads nowhere and costs nothing (§8.8.7)

Char XP Character Experience (§7.10)

Reports Generated with fog applied per kingdom

**10.7 Order Reference**

Every order a Player Page exports is one object in the orders file's orders\[\] array, keyed by type. Two kinds of traffic do **not** travel as order types: market trades ride in market_orders\[\] (action: buy / sell, with commodity and qty — §2.11.4) and messages ride in message_orders\[\] (up to 3 per turn — §2.16.5). Everything else is in the table below. This is a lookup index — the mechanics live in the sections cited; the phase column uses the names of §2.4.

|                      |                                                                                                                                                                           |                                                                                                       |                               |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------|
| **Order type**       | **Phase**                                                                                                                                                                 | **Key fields**                                                                                        | **See §**                     |
| create_army          | Pre-Phase 2 (Create / Disband re-apply)                                                                                                                                   | army_num, label                                                                                       | §2.6, §2.12.1                 |
| disband_army         | Pre-Phase 2                                                                                                                                                               | army_num                                                                                              | §2.6                          |
| disband_units        | Pre-Phase 2                                                                                                                                                               | army_num, unit_id, qty (clamped to the stack; refused aboard a fleet or below engine crew; no refund) | §2.6                          |
| create_fleet         | Pre-Phase 2                                                                                                                                                               | fleet_num, port                                                                                       | §2.6, §2.14.2                 |
| disband_fleet        | Pre-Phase 2                                                                                                                                                               | fleet_num                                                                                             | §2.6                          |
| disband_ships        | Pre-Phase 2                                                                                                                                                               | fleet_num, ship_id, qty (clamped to the stack; refused while carrying an army; no refund)             | §2.6                          |
| link_armies          | Pre-Phase 2 (link re-apply)                                                                                                                                               | army_num (leader), targets\[\]                                                                        | §5.11                         |
| link_accept          | Pre-Phase 2                                                                                                                                                               | army_num, leader_kingdom_id, leader_army_num                                                          | §5.11                         |
| unlink               | Pre-Phase 2                                                                                                                                                               | army_num                                                                                              | §5.11                         |
| link_fleets          | Pre-Phase 2                                                                                                                                                               | fleet_num (flagship), targets\[\]                                                                     | §2.14.7                       |
| fleet_link_accept    | Pre-Phase 2                                                                                                                                                               | fleet_num, leader_kingdom_id, leader_fleet_num                                                        | §2.14.7                       |
| fleet_unlink         | Pre-Phase 2                                                                                                                                                               | fleet_num                                                                                             | §2.14.7                       |
| embark_army          | Pre-Phase 2 (embark re-apply)                                                                                                                                             | army_num, fleet_num, beach (true = beach pickup)                                                      | §2.6, §2.14.5, §9.11          |
| set_army_stance      | Read at Pre-Phase 3 (siege / assault / sally) and in Phase 5 combat                                                                                                       | army_num, stance, siege_target {col,row}                                                              | §5.4, §2.6b, §2.13.6, §2.13.7 |
| set_fleet_stance     | Read in Phase 1 (blockade) and Phase 6 raid pre-pass; a biting blockade (the fleet lies inside an enemy port at war) is stored on the fleet until it lapses or is changed | fleet_num, stance (sailing / blockade / raid / hunt; hunt is Pirate-only and stored like a blockade)  | §2.9.3, §2.14.3, §2.14.9      |
| tax_change           | Phase 1 (applied to next turn's rate)                                                                                                                                     | to (1–10, ±1 per turn)                                                                                | §2.9.13                       |
| build_site           | Phase 3                                                                                                                                                                   | col, row, site_type                                                                                   | §2.11.1                       |
| upgrade_site         | Phase 3                                                                                                                                                                   | col, row, site_type                                                                                   | §2.11.2                       |
| raze_site            | Phase 3                                                                                                                                                                   | col, row                                                                                              | §2.11.6                       |
| upgrade_construction | Phase 3                                                                                                                                                                   | col, row                                                                                              | §2.11.7, §3.7                 |
| repair_wall          | Phase 3                                                                                                                                                                   | col, row                                                                                              | §2.11.8, §3.7.2               |
| found_construction   | Phase 3                                                                                                                                                                   | col, row, family                                                                                      | §2.11.9, §3.7.4               |
| recruit_unit         | Pre-Phase 2b (Recruitment)                                                                                                                                                | army_num, unit_id, qty                                                                                | §2.6a, §2.12.1                |
| build_ship           | Phase 4                                                                                                                                                                   | fleet_num, ship_id, qty                                                                               | §2.12.3                       |
| hire_character       | Phase 4                                                                                                                                                                   | candidate_id (cost and stats are TP-authoritative)                                                    | §2.12.4, §7.3                 |
| assign_character     | Phase 4 (after hires)                                                                                                                                                     | char_id, assignment                                                                                   | §7.4                          |
| dismiss_character    | Phase 4                                                                                                                                                                   | char_id                                                                                               | §7.9                          |
| transfer_units       | Phase 4.5                                                                                                                                                                 | from_army_num, to_army_num, units\[\] (or all: true)                                                  | §2.12b                        |
| split_army           | Phase 4.5 (before transfers)                                                                                                                                              | from_army_num, new_army_num (empty slot), units\[\] — new army on the same hex, held this turn        | §2.12b                        |
| transfer_ships       | Phase 4.6                                                                                                                                                                 | from_fleet_num, to_fleet_num, ships\[\]                                                               | §2.12b                        |
| split_fleet          | Phase 4.6 (before transfers)                                                                                                                                              | from_fleet_num, new_fleet_num (empty slot), ships\[\] — new fleet on the same hex, held this turn     | §2.12b                        |
| move_army            | Phase 5 (refused for a besieged army)                                                                                                                                     | army_num, path\[\] of {col,row}                                                                       | §2.13.2, §2.13.7              |
| move_fleet           | Phase 6                                                                                                                                                                   | fleet_num, path\[\] of {col,row}                                                                      | §2.14.1                       |
| disembark_army       | Phase 6 (after all fleet movement)                                                                                                                                        | army_num, fleet_num, col, row                                                                         | §2.14.6                       |
| hire_spy             | Phase 7                                                                                                                                                                   | col, row (max 3 per turn; cost TP-authoritative)                                                      | §2.15, §8.8                   |
| diplomacy            | Phase 8                                                                                                                                                                   | target_id, new_status                                                                                 | §2.16, §8.1–8.3               |
| become_vassal        | Phase 8c (Vassalage)                                                                                                                                                      | liege_id, optional tax_rate (1–5, default 3) — an offer the liege answers next turn                   | §2.16.4, §8.6.1               |
| vassal_offer_reply   | Phase 8c (Vassalage)                                                                                                                                                      | offer_id, accept (true/false) — the liege's answer to an oath                                         | §2.16.4                       |
| set_vassal_tribute   | Phase 8c                                                                                                                                                                  | vassal_id, rate (1–5)                                                                                 | §8.6.2                        |
| leave_vassalage      | Phase 8c                                                                                                                                                                  | —                                                                                                     | §8.6.3                        |
| send_resource        | End of turn (Resource Transfers)                                                                                                                                          | to_kingdom_id, commodity, amount                                                                      | §2.8, §6.9                    |
| transfer_hex         | End of turn (Resource Transfers)                                                                                                                                          | col, row, to_kingdom_id                                                                               | §2.8.1                        |

Any field not listed here that a page writes into an order (costs, stats, spymaster politics, \_-prefixed keys) is ignored or stripped by the Turn Processor — orders are self-signed, so the server recomputes everything it can.

*All mechanics sourced directly from the current \`turn_processor_V\<N\>.html\` and \`player_page_V\<N\>.html\` (highest N). Code comment values are unreliable — all figures in this manual are taken from actual constant assignments and runtime logic.*

*Map icons "Qaitbay Citadel", "Village", "Greek Temple", "Viking Longhouse", "Goblin Camp" and "Miner" by Delapouite, and "Elven Castle" by Pepijn Poolman, from game-icons.net (https://game-icons.net), licensed CC BY 3.0 (https://creativecommons.org/licenses/by/3.0/) — recoloured and outlined, and shown on the map and on the Constructions tab's cards (the miner on a round sign). The yurt and the dwarven hold were drawn for TREVAS in the same style.*
