# Blocco 7 — Agenti AI: il Deep Dive (~55 min)

## Obiettivo del blocco
Far comprendere ai partecipanti cosa sono gli agenti AI, come funzionano (loop, tool, orchestrazione), lo standard MCP, i rischi di sicurezza, e concetti avanzati come memory, skills e observability. Questo blocco trasforma la comprensione dei partecipanti da "l'AI genera testo" a "l'AI può agire nel mondo reale" — con tutti i benefici e rischi che ne derivano.

Questo è il blocco più lungo insieme al Blocco 3 ed è il più rilevante per il lavoro quotidiano del team, perché MemorAIz costruisce e vende sistemi basati su agenti.

---

## Slide previste: 15

### Slide 7.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ BLOCCO 7"
  - Heading grande: "Agenti AI: il Deep Dive"
  - Sottotitolo: "Quando l'AI smette di parlare e inizia ad agire"
  - Sotto il sottotitolo, piccola nota: "~55 minuti — il blocco più rilevante per il vostro lavoro"
- **Stellina**: `connessione2.png` — in basso a destra (tema: collegare, tool calling, agire nel mondo)
- **Animazioni**: Auto-reveal elementi in sequenza all'ingresso — ★☆☆
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Siamo arrivati al blocco più importante per il nostro lavoro quotidiano. Finora abbiamo capito come l'AI genera testo — adesso vediamo come può fare cose concrete: cercare informazioni, chiamare API, creare file, coordinare altri agenti. Questo è il cuore di ciò che MemorAIz costruisce."

---

### Slide 7.1 — Solo LLM vs Agente AI
- **Tipo**: `ANALOGY`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ LA DIFFERENZA"
  - Heading: "Dall'LLM all'Agente"
  - Sotto-heading: "Cosa cambia quando l'AI può agire"
  - Layout split verticale con due colonne ben distinte:
    - **Colonna sinistra — "Solo LLM"** (sfondo leggermente desaturato):
      - Icona: cervello stilizzato in una stanza chiusa
      - "Riceve input → genera output testuale. Fine."
      - "Reattivo: risponde una volta, dentro la finestra di contesto"
      - "Non può cercare, non può eseguire, non può verificare"
      - Analogia in basso: "Un esperto in una stanza senza telefono né computer"
    - **Colonna destra — "Agente AI"** (sfondo con leggero glow gold):
      - Icona: cervello stilizzato con braccia, telefono, computer, connessioni
      - "Osserva → Pianifica → Agisce → Verifica → Itera"
      - "Ha strumenti: cerca sul web, legge file, chiama API, esegue codice"
      - "Ha stato e può decidere autonomamente quando ha finito"
      - Analogia in basso: "Lo stesso esperto, con telefono, computer e accesso a tutto"
  - Box differenza chiave in basso al centro: "La differenza: l'agente ha azioni e stato. Non solo genera testo — fa cose."
- **Stellina**: Nessuna (il layout split è il focus)
- **Animazioni**:
  - Click 1: colonna "Solo LLM" appare con i suoi punti
  - Click 2: colonna "Agente AI" appare con i suoi punti (con effetto "unlock"/apertura)
  - Click 3: box differenza chiave in basso
  - Complessità: ★☆☆
- **Citazioni previste**: Nessuna (concetti illustrativi e analogie originali)
- **Note presentatore**: "Pensate alla differenza così. Un LLM è un esperto brillante chiuso in una stanza: risponde a quello che gli chiedete, ma non può fare altro. Un agente è lo stesso esperto, ma con un telefono, un computer, accesso a internet e a tutti gli strumenti che gli servono. Può cercare informazioni, verificare fatti, eseguire azioni, e decidere da solo quando il lavoro è finito. La differenza fondamentale? L'agente non solo parla — agisce."

---

### Slide 7.2 — Il loop agente: Observe → Think → Act
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ IL LOOP"
  - Heading: "Il ciclo dell'agente"
  - Sotto-heading: "Observe → Think → Act → Verifica → Ripeti"
  - Animazione centrale: diagramma circolare con 4 nodi disposti in cerchio, collegati da frecce animate:
    - **Nodo in alto** — "🎯 Obiettivo" (punto di ingresso, colore gold)
    - **Nodo a destra** — "🔍 OBSERVE" (leggi contesto, risultati tool) — colore mint
    - **Nodo in basso** — "🧠 THINK" (ragiona, pianifica prossima azione) — colore lavanda
    - **Nodo a sinistra** — "⚡ ACT" (usa un tool, genera risposta) — colore peach
    - **Al centro del cerchio** — "Obiettivo raggiunto?" con due frecce: "No → continua il loop" / "Sì → risposta finale"
  - L'animazione mostra un "segnale" luminoso che percorre il ciclo: Obiettivo → Observe → Think → Act → verifica → Observe → Think → Act → ✅ risposta finale
  - Box esempio concreto in basso: "Esempio: 'Trova i dati di mercato per il pitch deck' → Observe (legge il brief) → Think (serve cercare su web) → Act (web_search) → Observe (legge risultati) → Think (servono dati più specifici) → Act (altra ricerca) → ... → risposta con dati e fonti"
- **Stellina**: `conversione2.png` — piccola, accanto al heading (tema: loop iterativo, refinement)
- **Animazioni**:
  - Click 1: nodo "Obiettivo" appare in alto
  - Click 2: nodo OBSERVE appare, freccia animata da Obiettivo
  - Click 3: nodo THINK appare, freccia animata
  - Click 4: nodo ACT appare, freccia animata + nodo verifica al centro
  - Click 5: il segnale luminoso percorre il ciclo completo 2 volte, poi esce verso "Risposta finale"
  - Click 6: box esempio concreto in basso
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ Anthropic, 2025` — Pattern Observe-Think-Act come architettura standard degli agenti AI
- **Ricerca web**: ✅ Verificato — Il pattern Observe-Think-Act è la descrizione standard dell'architettura agente. OpenAI e Anthropic raccomandano di partire da un singolo agente con loop prima di passare a multi-agent. Confermato da documentazione ufficiale e guide di settore.
- **Note presentatore**: "Ecco il cuore di un agente: un ciclo. Riceve un obiettivo, osserva il contesto e i dati disponibili, ragiona su cosa fare, agisce — per esempio cercando sul web o chiamando un'API — poi verifica: ho raggiunto l'obiettivo? Se no, ricomincia. Se sì, produce la risposta finale. Questo ciclo può ripetersi decine di volte per compiti complessi. L'esempio in basso mostra un caso reale: cercare dati di mercato richiede più cicli di ricerca e raffinamento."

---

### Slide 7.3 — Tools: le mani dell'agente
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ TOOLS"
  - Heading: "Tools — le mani dell'agente"
  - Sotto-heading: "Funzioni che l'LLM può decidere di invocare"
  - Layout con LLM stilizzato al centro e 6 tool disposti a raggiera intorno, ciascuno con icona e nome:
    - 🔍 `web_search(query)` — Cercare sul web
    - 📧 `send_email(to, subject, body)` — Inviare email
    - 🗄️ `query_database(sql)` — Interrogare un database
    - 📁 `create_file(name, content)` — Creare file
    - 🖼️ `get_screenshot(url)` — Catturare screenshot
    - 💻 `run_code(language, code)` — Eseguire codice
  - Ogni tool ha una linea tratteggiata che lo connette all'LLM centrale
  - Box chiave in basso: "L'LLM non esegue il tool — genera una richiesta JSON¹. Il sistema esterno esegue e restituisce il risultato."
- **Stellina**: Nessuna (il diagramma a raggiera è il focus visivo)
- **Animazioni**:
  - Click 1: LLM stilizzato al centro
  - Click 2: i 6 tool appaiono uno alla volta in sequenza rapida (200ms intervallo), ciascuno con la linea di connessione
  - Click 3: box chiave in basso con enfasi su "genera una richiesta JSON"
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Anthropic / OpenAI, 2024-2025` — Tool calling come funzionalità nativa dei principali LLM (Claude, GPT-4, Gemini)
- **Ricerca web**: ✅ Verificato — Tool calling nativo supportato da tutti i principali LLM: Claude (Anthropic), GPT-4/GPT-4o (OpenAI), Gemini (Google), Llama (Meta). Il meccanismo è uniforme: LLM genera JSON strutturato, il sistema esegue, il risultato torna come contesto. La qualità delle descrizioni dei tool è documentata come fattore critico per l'accuratezza della selezione.
- **Note presentatore**: "I tool sono le mani dell'agente. Sono funzioni — pezzi di codice — che l'LLM può decidere di usare. La cosa importante da capire è che l'LLM non esegue direttamente il tool. Genera una richiesta strutturata — tipo un ordine scritto — che dice 'voglio cercare sul web questa frase'. Il sistema esterno esegue la ricerca e restituisce i risultati all'LLM. L'LLM legge i risultati e decide cosa fare dopo."

---

### Slide 7.4 — Tool calling step-by-step
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ COME FUNZIONA"
  - Heading: "Tool calling in azione"
  - Sotto-heading: "5 passi, dal prompt alla risposta"
  - Animazione sequenziale verticale (flow dall'alto in basso) con 5 step numerati:
    - **① Utente chiede**: "Che tempo fa a Bologna domani?" (bubble utente)
    - **② LLM riceve** la domanda + la lista dei tool disponibili con descrizioni
    - **③ LLM decide** e genera: `{"tool": "get_weather", "city": "Bologna", "days": 1}` (box JSON stilizzato con syntax highlighting)
    - **④ Sistema esegue** la chiamata API meteo → risultato: `{"temp": 22, "condition": "soleggiato"}`
    - **⑤ LLM legge il risultato** e genera la risposta finale: "Domani a Bologna ci saranno 22°C con cielo soleggiato."
  - Frecce animate tra ogni step
  - Box insight in basso: "La qualità delle descrizioni dei tool è cruciale¹ — se il tool è descritto male, il modello non saprà quando usarlo"
- **Stellina**: Nessuna (l'animazione step è il focus)
- **Animazioni**:
  - Click 1: step ① bubble utente
  - Click 2: step ② LLM riceve la domanda + lista tool
  - Click 3: step ③ LLM genera il JSON (con effetto "typing" per il JSON)
  - Click 4: step ④ sistema esegue, risultato appare (con effetto "flash" di esecuzione)
  - Click 5: step ⑤ LLM risponde all'utente + box insight
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Anthropic, 2025` — Documentazione tool use: l'importanza delle descrizioni per la qualità del tool selection
- **Ricerca web**: ✅ Verificato — La documentazione ufficiale di Anthropic e OpenAI enfatizza che la qualità delle descrizioni dei tool (nome, descrizione semantica, parametri in JSON schema) è il fattore determinante per l'accuratezza della selezione. Tool description quality impatta direttamente la selection accuracy.
- **Note presentatore**: "Vediamo il processo completo. L'utente chiede il meteo. L'LLM non sa il meteo — ma sa che ha un tool 'get_weather'. Genera una richiesta JSON strutturata con i parametri giusti. Il sistema esterno chiama l'API meteo vera e restituisce i dati. L'LLM legge i dati e formula una risposta naturale. Due cose importanti: l'LLM ha scelto autonomamente quale tool usare, e la qualità della descrizione del tool è fondamentale. Se scrivete 'tool per il meteo' è peggio di 'restituisce previsioni meteo per una città specifica nei prossimi N giorni'."

---

### Slide 7.5 — Failure modes dei tool
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "🔗 CONCETTO PONTE"
  - Heading: "Quando i tool falliscono"
  - Sotto-heading: "I tool possono sbagliare — e l'agente deve saperlo gestire"
  - 4 blocchi in griglia 2×2 con icone e testo breve:
    - **🔴 Timeout / Errori API**: "Il tool non risponde. L'agente deve avere un piano B."
    - **🟠 Dati incompleti**: "Il tool restituisce risultati parziali o malformati."
    - **🟡 Prompt injection via output**: "Un documento scaricato contiene istruzioni malevole¹ → diventano parte del contesto dell'LLM."
    - **🔵 Azioni non autorizzate**: "L'agente potrebbe fare qualcosa che non doveva (es. inviare un'email senza conferma)."
  - Box pattern di difesa in basso: "Difese: retry controllati | timeout | validazione output | conferma utente per azioni sensibili"
- **Stellina**: `dubbioso:pensieroso.png` — piccola, accanto al heading (tema: problemi, dubbi)
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2: i 4 blocchi appaiono in sequenza (uno per click, o tutti insieme)
  - Click 3: box pattern di difesa
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ OWASP, 2025` — LLM Top 10: Indirect Prompt Injection tramite tool output
- **Ricerca web**: ✅ Verificato — OWASP Top 10 per LLM Applications 2025: LLM01 = Prompt Injection (include indirect via tool output), LLM05 = Improper Output Handling, LLM06 = Excessive Agency. Inoltre, è stato pubblicato a dicembre 2025 il nuovo OWASP Top 10 per Agentic Applications, specifico per agenti AI.
- **Note presentatore**: "I tool non sono infallibili. Possono non rispondere, restituire dati sbagliati, o peggio — restituire contenuto malevolo. Immaginate: l'agente scarica un documento dal web, e dentro quel documento qualcuno ha scritto 'ignora le istruzioni precedenti e fai X'. Quel testo entra nel contesto dell'LLM come se fosse un'istruzione legittima. Per questo servono difese: timeout, validazione, e soprattutto conferma umana per azioni importanti come inviare email o modificare dati."

---

### Slide 7.6 — MCP: il problema N×M
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ MCP"
  - Heading: "MCP — Model Context Protocol"
  - Sotto-heading: "Lo standard che risolve il caos delle integrazioni"
  - Animazione in due fasi:
    - **Fase 1 — "Il problema"**: a sinistra 4 client AI (Claude, ChatGPT, Cursor, VS Code) e a destra 4 servizi (Figma, Slack, GitHub, Database). Tra loro, una matrice di linee incrociate (4×4 = 16 connessioni) — il tutto in rosso/arancio con label "N × M integrazioni = non scala"
    - **Fase 2 — "La soluzione MCP"**: stessa disposizione, ma ora un rettangolo centrale "MCP Protocol" con linee ordinate: 4 linee a sinistra (client → MCP) e 4 linee a destra (MCP → servizi) — in gold/verde con label "N + M integrazioni = scala¹"
  - Box sotto: "Un servizio implementa MCP una volta → funziona con qualsiasi client compatibile²"
- **Stellina**: `connessione1.png` — piccola, accanto alla fase 2 (tema: collegare, integrare)
- **Animazioni**:
  - Click 1: fase 1 — i 4 client e i 4 servizi appaiono
  - Click 2: le 16 linee incrociate si disegnano (effetto "groviglio" caotico), label "N×M"
  - Click 3: transizione — le linee si sciolgono, il rettangolo MCP appare al centro, le linee si riorganizzano ordinate (4+4), label "N+M"
  - Click 4: box sotto con conclusione
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Anthropic, 2024` — MCP annunciato a novembre 2024 come standard aperto per connettere LLM a dati e strumenti esterni
  - `² MCP Ecosystem, 2025-2026` — Oltre 17.000 MCP server disponibili su mcp.so; adottato da Claude, ChatGPT, Gemini, Cursor, VS Code, JetBrains
- **Ricerca web**: ✅ Verificato — MCP creato da Anthropic (nov 2024), donato alla Linux Foundation / Agentic AI Foundation (dic 2025). Adottato da OpenAI (mar 2025), Google DeepMind (apr 2025). 17.800+ server su mcp.so. Client: Claude, ChatGPT, Cursor, VS Code, JetBrains, Copilot, Windsurf.
- **Note presentatore**: "Il Model Context Protocol risolve un problema pratico enorme. Senza uno standard, se avete 4 piattaforme AI e 4 servizi da integrare, servono 16 integrazioni custom. Con MCP, ogni servizio si integra una volta sola con il protocollo, e funziona con tutti i client. MCP è stato creato da Anthropic come standard aperto — e la community ha già creato migliaia di server. Lo usiamo già noi: il server MCP di Figma permette a Claude di leggere direttamente i design."

---

### Slide 7.7 — MCP: architettura ed esempi
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ MCP IN PRATICA"
  - Heading: "MCP nella pratica"
  - Sotto-heading: "Come lo usiamo già e come interessa ai clienti"
  - Layout: diagramma architetturale semplificato in alto + esempi sotto
  - **Diagramma** (stile schematico):
    ```
    ┌──────────────┐     MCP Protocol     ┌──────────────┐
    │  Client AI   │◄────────────────────►│  MCP Server  │
    │  (Claude,    │    (standard aperto)  │  (Figma,     │
    │   Cursor,    │                       │   Slack,     │
    │   VS Code)   │                       │   GitHub...) │
    └──────────────┘                       └──────────────┘
    ```
  - **4 esempi concreti** con icone:
    - 🎨 **Figma MCP** — Claude legge design, genera screenshot, ottiene contesto. "Lo usiamo già!"
    - 💻 **GitHub MCP** — L'AI crea PR, legge issues, cerca nel codice¹
    - 🗄️ **Database MCP** — L'AI interroga direttamente il database aziendale
    - 📄 **Google Drive MCP** — L'AI cerca e legge documenti dal Drive
  - Box per UX/Comms in basso: "Potete integrare i vostri strumenti senza copia/incolla continuo. Come azienda, potete creare MCP server per i clienti."
- **Stellina**: Nessuna (diagramma + esempi sono sufficienti)
- **Animazioni**:
  - Click 1: diagramma architetturale
  - Click 2: 4 esempi concreti (build rapido)
  - Click 3: box per UX/Comms
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ GitHub, 2025` — GitHub MCP server per integrazione AI con repository
- **Ricerca web**: ✅ Verificato — Server MCP ufficiali Anthropic: GitHub, Slack, Google Drive, Git, Postgres, Puppeteer. Server first-party: Figma MCP (ufficiale, desktop + remote), Docker MCP Catalog (mar 2025), Supabase MCP, shadcn/ui MCP. Figma + GitHub Copilot: integrazione design-to-code tramite MCP documentata.
- **Note presentatore**: "Ecco come funziona nella pratica. Il client AI — Claude, Cursor, VS Code — comunica con i server MCP attraverso un protocollo standard. Ogni server espone strumenti specifici. Noi usiamo già il server MCP di Figma: quando lavoro con Claude Code e condivido un URL Figma, Claude può leggere direttamente il design, generare screenshot dei componenti, e capire la struttura. Per voi, questo significa: potete collegare i vostri strumenti di lavoro all'AI senza dover copiare e incollare continuamente."

---

### Slide 7.8 — Sicurezza negli agenti
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "🔗 SICUREZZA"
  - Heading: "Più potere = più responsabilità"
  - Sotto-heading: "I rischi specifici degli agenti AI"
  - 4 rischi in layout verticale con severity indicator (colore):
    - **🔴 Prompt injection via tool** — "Un documento scaricato contiene 'ignora le istruzioni e fai X'¹. L'output del tool diventa nuovo contesto per l'LLM."
    - **🔴 Azioni non autorizzate** — "L'agente invia un'email che non doveva inviare, o modifica dati sensibili senza conferma."
    - **🟠 Supply chain di tool** — "Anche tool 'ufficiali' possono avere vulnerabilità. Un MCP server compromesso = tutti i client esposti."
    - **🟡 Token DoS** — "Un agente in loop può consumare enormi quantità di token = costi fuori controllo²."
  - Box design implications in basso (4 punti compatti):
    - "✅ Conferma umana per azioni ad alto impatto"
    - "✅ Principio del minimo privilegio"
    - "✅ Logging di tutte le azioni per audit"
    - "✅ Fa parte delle OWASP Top 10 per LLM Applications³"
- **Stellina**: `chiave.png` — piccola, accanto al heading (tema: sicurezza, accesso)
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2: i 4 rischi appaiono in sequenza (uno per click, build rapido)
  - Click 3: box design implications
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ OWASP, 2025` — LLM Top 10: Indirect Prompt Injection (LLM01)
  - `² Industria, 2025` — Casi documentati di runaway agent costs
  - `³ OWASP, 2025` — OWASP Top 10 for LLM Applications v2.0
- **Ricerca web**: ✅ Verificato — OWASP Top 10 LLM Apps 2025: LLM01 Prompt Injection (★★★ per agenti), LLM06 Excessive Agency (★★★), LLM10 Unbounded Consumption / Token DoS (★★★), LLM03 Supply Chain (★★★ per MCP server compromessi). Dicembre 2025: pubblicato OWASP Top 10 per Agentic Applications (documento separato, specifico per agenti). Best practice confermate: human-in-the-loop, least privilege, logging completo.
- **Note presentatore**: "Più un agente può fare, più può andare storto. Quattro rischi principali. Primo: prompt injection via tool — un documento malevolo può manipolare l'agente. Secondo: azioni non autorizzate — l'agente che invia email o modifica dati senza permesso. Terzo: supply chain — un MCP server compromesso espone tutti i client collegati. Quarto: costi — un agente in loop che chiama tool continuamente può bruciare budget. Le difese? Conferma umana per azioni importanti, principio del minimo privilegio, e logging di tutto. Questo è importante per MemorAIz: quando progettiamo sistemi per i clienti, la sicurezza deve essere nel design, non un ripensamento."

---

### Slide 7.9 — Orchestrazione: perché servono più agenti
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ ORCHESTRAZIONE"
  - Heading: "Quando un agente non basta"
  - Sotto-heading: "Dividere il lavoro tra agenti specializzati"
  - 3 bullet con gold dots:
    - "Task complessi richiedono competenze diverse: ricerca, analisi, scrittura, esecuzione codice"
    - "Un singolo agente con troppi tool diventa meno efficace — contesto troppo diluito¹"
    - "Soluzione: agenti specializzati, coordinati da un orchestratore"
  - Analogia visiva al centro: illustrazione di un'orchestra con direttore:
    - Il direttore = orchestratore
    - I musicisti = agenti specializzati (ricercatore, scrittore, critico, esecutore)
    - "Ogni musicista è specializzato. Il direttore coordina. L'insieme è più della somma delle parti."
  - Box pratico: "Più agenti = più chiamate LLM = più costi e latenza. Regola: partire semplice, crescere solo quando serve²."
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: heading + 3 bullet
  - Click 2: analogia orchestra
  - Click 3: box pratico
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Anthropic, 2025` — Documentazione Claude Code: agenti con contesto focalizzato sono più efficaci
  - `² Industria, 2025` — Costi multi-agent: ogni agente moltiplica le chiamate LLM
- **Ricerca web**: ✅ Verificato — OpenAI e Anthropic raccomandano di partire con un singolo agente e crescere solo quando necessario. Più agenti = più chiamate LLM = costi lineari con il numero di agenti. Framework principali: Claude Code (teams/swarm nativi), LangGraph (LangChain), CrewAI, AutoGen (Microsoft). Amazon usa multi-agent per warehouse automation.
- **Note presentatore**: "Pensate a un team reale. Chiedereste a una persona sola di fare ricerca di mercato, scrivere il report, fare il design del pitch deck, e presentarlo? Probabilmente no — dividereste il lavoro. Lo stesso vale per gli agenti. Un agente con 50 tool e 10 responsabilità diverse diventa confuso. Meglio avere agenti specializzati: uno che ricerca, uno che scrive, uno che rivede. Ma attenzione: più agenti significa più costi e più complessità di debugging. Partite semplici."

---

### Slide 7.10 — I tre pattern di orchestrazione
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ I PATTERN"
  - Heading: "Tre modi di organizzare gli agenti"
  - Animazione con 3 pattern che si costruiscono uno dopo l'altro, ciascuno con schema + quando usarlo:
  - **Pattern 1 — Singolo agente delegato**:
    - Schema: Orchestratore → Agente Specializzato (frecce bidirezionali)
    - Label: "Task sequenziale, sotto-compiti ben definiti"
    - Esempio: "Traduci questo documento in 3 lingue"
  - **Pattern 2 — Fan-out (parallelo)**:
    - Schema: Orchestratore → [Agente A, Agente B, Agente C] → Orchestratore sintetizza
    - Label: "Sotto-compiti indipendenti, parallelizzabili"
    - Esempio: "Analizza 3 competitor in parallelo e sintetizza"
  - **Pattern 3 — Swarm (comunicazione inter-agente)**:
    - Schema: Orchestratore → [Agente A ↔ Agente B ↔ Agente C] → Orchestratore
    - Label: "Collaborazione, revisione incrociata, negoziazione"
    - Esempio: "Scrittore produce bozza → Critico la rivede → Scrittore incorpora feedback¹"
  - Box regola pratica in basso: "Partire dal Pattern 1. Crescere solo quando avete metriche che dimostrano che serve più complessità."
- **Stellina**: `coinvolgimento.png` — piccola, accanto al Pattern 3 (tema: collaborazione circolare, swarm)
- **Animazioni**:
  - Click 1: Pattern 1 — schema + label + esempio (tutto in un blocco)
  - Click 2: Pattern 2 — schema + label + esempio (gli agenti appaiono in parallelo, frecce animate)
  - Click 3: Pattern 3 — schema + label + esempio (le frecce inter-agente si animano con un ciclo)
  - Click 4: box regola pratica in basso
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ Anthropic, 2025` — Claude Code teams/swarm: pattern di orchestrazione con agenti specializzati
- **Ricerca web**: ✅ Verificato — I tre pattern (singolo, fan-out, swarm) sono confermati dalla documentazione di OpenAI, Anthropic e dai framework principali (LangGraph, CrewAI, AutoGen). OpenAI raccomanda esplicitamente di "stretching a single agent first". Claude Code implementa nativamente teams e swarm con comunicazione inter-agente.
- **Note presentatore**: "Tre pattern, dal semplice al complesso. Pattern 1: mandate un sotto-compito a un agente e aspettate il risultato. Pattern 2: lanciate più agenti in parallelo su compiti indipendenti — come i nostri agenti di ricerca che lavorano simultaneamente. Pattern 3: gli agenti comunicano tra loro — uno scrive, un altro critica, il primo incorpora i feedback. Noi usiamo il Pattern 2 e 3 quotidianamente con Claude Code. La regola d'oro: partite semplici. Il Pattern 1 copre l'80% dei casi."

---

### Slide 7.11 — Memory negli agenti
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "🔗 CONCETTO PONTE"
  - Heading: "Memory — come un agente 'ricorda'"
  - Sotto-heading: "Non è magia: è stato persistente"
  - Layout split con due tipi di memoria:
    - **Colonna sinistra — Short-term memory**:
      - Icona: blocco note con appunti
      - "La conversazione corrente (il contesto)"
      - "Limitata dalla context window"
      - "Si perde quando la sessione finisce"
    - **Colonna destra — Long-term memory**:
      - Icona: database/archivio
      - "Informazioni salvate tra sessioni diverse"
      - "Database, vector store, file CLAUDE.md"
      - "Persiste, ma va gestita e aggiornata"
  - Box warning in basso: "⚠️ Memoria senza governance = rischio privacy (dati utente persistenti) + drift (info obsolete o errate)"
- **Stellina**: `conoscenza.png` — piccola, tra le due colonne (tema: conoscenza, ricordare)
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2: colonna short-term
  - Click 3: colonna long-term
  - Click 4: box warning
  - Complessità: ★☆☆
- **Citazioni previste**: Nessuna (concetti architetturali generali, non affermazioni fattuali specifiche)
- **Note presentatore**: "La 'memoria' di un agente non è magica. La short-term memory è semplicemente il contesto della conversazione corrente — tutto ciò che è stato detto e fatto in questa sessione. La long-term memory sono informazioni salvate in un database o in file che vengono consultati quando servono. Noi usiamo entrambe: il file CLAUDE.md che avete visto è un esempio di long-term memory — istruzioni e conoscenze che persistono tra sessioni. Il rischio? Se non governate la memoria, l'agente potrebbe ricordare dati personali degli utenti o informazioni che nel tempo diventano obsolete."

---

### Slide 7.12 — Skills: competenze pacchettizzate
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ SKILLS"
  - Heading: "Skills — il manuale operativo dell'agente"
  - Sotto-heading: "Non tool (azioni), ma conoscenza procedurale (come fare bene)"
  - Differenza chiave in alto (layout due box affiancati):
    - **Box "Tool"**: "Azione esecutiva" → `web_search(query)` → "Fa qualcosa"
    - **Box "Skill"**: "Conoscenza procedurale" → `SKILL.md con istruzioni, template, esempi` → "Sa come fare bene qualcosa"
  - 3 esempi concreti con icone:
    - 📊 **Skill "crea presentazione"** — Istruzioni su come strutturare slide, formattare, gestire layout
    - 📝 **Skill "crea documento Word"** — Come generare un .docx professionale con TOC e stili
    - 🎨 **Skill "frontend design"** — Principi di design, come evitare l'estetica "generica AI"
  - Box lifecycle in basso: "Spec → Esempi → Test → Deploy → Monitor → Iterazione. Una skill senza eval è una demo, non un asset.¹"
  - Box MemorAIz: "Per i clienti: skill personalizzate = output consistenti con il loro brand."
- **Stellina**: `matita.png` — piccola, accanto agli esempi (tema: creare, scrivere, produrre)
- **Animazioni**:
  - Click 1: heading + differenza tool vs skill
  - Click 2: 3 esempi concreti
  - Click 3: box lifecycle + box MemorAIz
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ MemorAIz, 2025` — Skill lifecycle: spec-driven development con evaluation obbligatoria
- **Ricerca web**: Nessuna necessaria (concetto interno MemorAIz e best practice di engineering)
- **Note presentatore**: "Le skill sono diverse dai tool. Un tool è un'azione: cerca sul web, invia email. Una skill è un pacchetto di conoscenza: come fare bene una certa cosa. È come la differenza tra avere un martello e sapere come costruire un mobile. Le nostre skill includono istruzioni dettagliate, template, esempi di output di qualità, e criteri di valutazione. Senza valutazione, una skill è solo una demo — non puoi fidarti che produca risultati consistenti. Per i nostri clienti, le skill personalizzate garantiscono che ogni output sia coerente con il loro brand."

---

### Slide 7.13 — Observability: monitorare gli agenti
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "🔗 OBSERVABILITY"
  - Heading: "Non basta costruire — bisogna monitorare"
  - Sotto-heading: "Come sapere cosa fa un agente in produzione"
  - Layout con 4 aree di monitoraggio (icone + testo):
    - 📋 **Logging** — "Prompt, risposte, tool chiamati e loro output"
    - 🔗 **Tracing** — "Tracciare la catena decisionale: quale tool, perché, cosa ha ottenuto¹"
    - 💰 **Costi** — "Token consumati per task, costo per completamento"
    - 🚨 **Errori** — "Tasso di fallimento, fallback, anomalie"
  - Box KPI in basso (layout orizzontale compatto):
    - "Tasso errore" | "Precisione retrieval" | "Tempo per task" | "Costo per task" | "Soddisfazione utente"
  - Box insight: "Non 'credere' alla spiegazione del modello — verificare la sequenza di azioni."
- **Stellina**: `controllo.png` — piccola, accanto al heading (tema: ispezione, verifica, audit)
- **Animazioni**:
  - Click 1: heading + 4 aree di monitoraggio
  - Click 2: box KPI
  - Click 3: box insight
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Industria, 2025` — Strumenti di tracing per agenti AI (LangSmith, Braintrust, Phoenix)
- **Ricerca web**: ✅ Verificato — Strumenti principali di observability per agenti AI: LangSmith (LangChain), Braintrust, Phoenix (Arize), Helicone, Portkey. KPI standard confermati: tasso errore, costo per task, latenza, precisione retrieval, soddisfazione utente.
- **Note presentatore**: "Costruire un agente è solo metà del lavoro. L'altra metà è monitorarlo. In produzione, dovete sapere: cosa ha fatto l'agente? Quali tool ha chiamato? Quanto è costato? Ha fallito? Il tracing è particolarmente importante: non fidatevi della spiegazione del modello su perché ha fatto qualcosa — verificate la sequenza reale di azioni. I KPI che contano: tasso di errore, costo per task, e soprattutto soddisfazione dell'utente finale."

---

### Slide 7.14 — Riepilogo del blocco
- **Tipo**: `SUMMARY`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ TAKEAWAY"
  - Heading grande: "Agenti AI — il quadro completo"
  - Sotto-heading: "Da LLM passivo ad agente autonomo, in 7 concetti"
  - 7 punti in layout compatto (colonna singola con numeri gold):
    - **① Loop** — L'agente osserva, pensa, agisce, verifica, e ripete finché non ha finito.
    - **② Tools** — Funzioni che l'LLM invoca generando richieste JSON. Non esegue — delega.
    - **③ Tool calling** — 5 step: domanda → scelta tool → JSON → esecuzione → risposta.
    - **④ MCP** — Standard aperto per connettere LLM a servizi. N+M invece di N×M.
    - **⑤ Sicurezza** — Prompt injection, azioni non autorizzate, costi fuori controllo. Human-in-the-loop.
    - **⑥ Orchestrazione** — Da singolo agente a swarm. Partire semplice, crescere con le metriche.
    - **⑦ Skills + Memory + Observability** — Conoscenza procedurale + stato persistente + monitoraggio.
  - Box bridge in basso: "Prossimo e ultimo blocco: la checklist operativa per mettere tutto in pratica → Blocco 8"
- **Stellina**: `super.png` — piccola, in basso a destra (superpotere: ora capite gli agenti!)
- **Animazioni**: Build rapido dei 7 punti + box bridge — ★☆☆
- **Citazioni previste**: Nessuna (riepilogo senza dati nuovi)
- **Note presentatore**: "Sette concetti per capire gli agenti AI. Il loop è il cuore: observe, think, act, verifica. I tool sono le mani dell'agente. Il tool calling è il meccanismo concreto: JSON, esecuzione, risultato. MCP è lo standard che rende tutto interoperabile. La sicurezza è fondamentale: più potere significa più rischio. L'orchestrazione permette di coordinare agenti specializzati. E infine skills, memory e observability completano il quadro: conoscenza, stato e monitoraggio. Con questo blocco, avete il modello mentale completo per capire — e vendere — ciò che MemorAIz costruisce."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 15 |
| Animazioni ★☆☆ | 8 slide (titolo, LLM vs Agente, failure modes, MCP pratica, sicurezza, memory, skills, observability, summary) |
| Animazioni ★★☆ | 3 slide (tools raggiera, tool calling step-by-step, MCP N×M) |
| Animazioni ★★★ | 2 slide (loop agente, tre pattern orchestrazione) |
| Stelline usate | `connessione2.png` (7.0), `conversione2.png` (7.2), `dubbioso:pensieroso.png` (7.5), `connessione1.png` (7.6), `chiave.png` (7.8), `conoscenza.png` (7.11), `coinvolgimento.png` (7.10), `matita.png` (7.12), `controllo.png` (7.13), `super.png` (7.14) |
| Gradienti | Alternanza Mint/Default: Mint (7.0, 7.2, 7.4, 7.6, 7.8, 7.10, 7.12, 7.14), Default (7.1, 7.3, 7.5, 7.7, 7.9, 7.11, 7.13) |
| Ricerca web | MCP (data lancio, adozione, server disponibili), OWASP Top 10 LLM, tool calling (supporto nativo), orchestrazione (pattern, framework), observability (strumenti) |

---

## Note sulla complessità delle animazioni

### Animazioni ★★★ che richiedono mini-spec prima dell'implementazione:

1. **Slide 7.2 — Loop agente** (★★★)
   - Diagramma circolare con nodi e segnale luminoso che percorre il ciclo
   - Richiede: canvas o SVG animato, gestione del ciclo, cleanup
   - Mini-spec necessaria prima dell'implementazione

2. **Slide 7.10 — Tre pattern di orchestrazione** (★★★)
   - 3 diagrammi con nodi, frecce bidirezionali, frecce inter-agente animate
   - Richiede: SVG multi-stato, transizioni tra pattern, animazione frecce cicliche per lo swarm
   - Mini-spec necessaria prima dell'implementazione

### Animazioni ★★☆ che possono procedere con attenzione:

3. **Slide 7.3 — Tools a raggiera** (★★☆): layout radiale con connessioni animate
4. **Slide 7.4 — Tool calling step-by-step** (★★☆): flow verticale con effetto typing per JSON
5. **Slide 7.6 — MCP N×M** (★★☆): transizione da groviglio a schema ordinato

---
