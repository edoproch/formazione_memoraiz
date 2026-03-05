# Blocco 6 — Reasoning, Benchmark e Modelli (~30 min)

## Obiettivo del blocco
Far capire ai partecipanti cosa sono i reasoning models, come si differenziano dagli LLM standard, quando ha senso usarli e quando no, e introdurre il pattern di routing come concetto di design. In aggiunta, dare al team gli strumenti per valutare criticamente i benchmark e le classifiche dei modelli, capire la differenza tra modelli open e closed weights, e saper rispondere alla domanda "quale modello è meglio per noi?". Il blocco chiude il cerchio sui modelli prima di passare alla safety (Blocco 6B) e poi agli agenti (Blocco 7).

---

## Slide previste: 10

### Slide 6.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ BLOCCO 6"
  - Heading grande: "Reasoning Models"
  - Sottotitolo: "Quando il modello impara a pensare prima di rispondere"
  - Sotto il sottotitolo, piccola nota: "~30 minuti"
- **Stellina**: `lampadina.png` — in basso a destra (tema insight, idea chiave: i modelli che "pensano")
- **Animazioni**: Nessuna — tutto visibile immediatamente (`data-steps="0"`)
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Finora abbiamo visto come funzionano gli LLM standard: ricevono un input e generano una risposta token per token, di getto. Ma da fine 2024 è emersa una nuova categoria di modelli che prima di rispondere si prendono del tempo per ragionare. Vediamo cosa cambia e perché vi interessa."

---

### Slide 6.1 — Cosa sono i reasoning models
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ DEFINIZIONE"
  - Heading: "Modelli che pensano passo-passo"
  - Sotto-heading: "Una nuova categoria di LLM, addestrati per ragionare"
  - 4 bullet con gold dots:
    - **La scoperta** — Nel 2022 i ricercatori scoprono che basta chiedere a un LLM "ragiona passo per passo" per migliorare drasticamente i risultati¹. Il chain-of-thought prompting funziona — ma è fragile: dipende da come lo chiedi.
    - **Da prompting a training** — Idea chiave: se ragionare passo-passo funziona quando glielo chiedi, perché non addestrare il modello a farlo sempre? Con il reinforcement learning² si premia il modello non solo per la risposta giusta, ma per il processo logico che ci porta.
    - **Il risultato** — Nasce una nuova categoria di LLM che genera thinking tokens — token dedicati al ragionamento interno — prima della risposta finale. Più "tempo di pensiero" = più qualità sui problemi difficili³.
    - **Chi sono oggi** — GPT-5 e o3/o4-mini (OpenAI)⁴, Claude Opus 4.6 e Sonnet 4.6 con extended thinking⁵, DeepSeek R1⁶, Gemini 3.1 (Google)⁷, Kimi K2 (Moonshot)⁸.
  - Box highlight in basso: "Restano modelli di next-token — non è magia. Cambia il training e l'inference: più token dedicati al 'pensare'."
- **Stellina**: Nessuna (il contenuto è denso, non serve rumore visivo)
- **Animazioni**: Reveal sequenziale dei bullet al click — ★☆☆
- **Citazioni previste**:
  - `¹ Wei et al., 2022` — Chain-of-thought prompting paper originale
  - `² OpenAI, 2024` — "o1 learns to recognize and correct its mistakes" (blog "Learning to reason with LLMs")
  - `³ Nous Research, 2025` — Test-time compute scaling: più thinking budget = migliori risultati su problemi difficili
  - `⁴ OpenAI, 2025` — o3 e o4-mini rilasciati il 16 aprile 2025
  - `⁵ Anthropic, 2025` — Claude 3.7 Sonnet: "primo modello ibrido di ragionamento", budget fino a 128K thinking tokens
  - `⁶ DeepSeek, 2025` — R1 rilasciato il 20 gennaio 2025, open-weight, performance paragonabili a o1
  - `⁷ Google DeepMind, 2025` — Gemini 2.5 Pro con thinking, debutto #1 su LMArena
- **Ricerca web**: ✅ Verificato — tutti i modelli e le date confermati. Chain-of-thought è il termine standard. Il concetto di test-time compute scaling è confermato da Nous Research e blog OpenAI.
- **Note presentatore**: "Pensatela così: un LLM standard è come uno studente che scrive la risposta subito, senza fare la brutta copia. Un reasoning model è come uno studente che prima ragiona su un foglio di brutta, verifica i passaggi, e poi scrive la risposta in bella. Usa più tempo e più inchiostro (token), ma su problemi difficili sbaglia molto meno. Importante: non è magia, restano modelli probabilistici. Semplicemente, sono addestrati e strutturati per pensare di più."

---

### Slide 6.2 — Come funzionano: risposta istantanea vs ragionamento
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ COME FUNZIONANO"
  - Heading: "Risposta istantanea vs ragionamento"
  - Sotto-heading: "Più tempo per pensare = più affidabilità sui problemi difficili"
  - Animazione side-by-side che confronta i due approcci:
    - **Stato 1 — Setup**: Due colonne appaiono con header "LLM Standard" (sinistra) e "Reasoning Model" (destra). Al centro in alto, una domanda appare: "Qual è il modo migliore per organizzare 3 workshop sulla AI per team diversi con vincoli di calendario?"
    - **Stato 2 — LLM Standard risponde**: Nella colonna sinistra, una risposta appare direttamente ("di getto") — un blocco di testo compatto che esce fluido. Un piccolo badge: "⚡ ~2 sec, ~500 token"
    - **Stato 3 — Reasoning Model pensa**: Nella colonna destra, appare un blocco "thinking" con sfondo leggermente diverso (più scuro/trasparente). Dentro, 3-4 righe di ragionamento visibile appaiono una dopo l'altra con animazione typing:
      - "→ Devo considerare 3 team con esigenze diverse..."
      - "→ I vincoli di calendario sono: ..."
      - "→ Opzione A: sequenziale — ma il team 2 non è disponibile..."
      - "→ Opzione B: paralleli con risorse condivise — verifichiamo..."
    - **Stato 4 — Reasoning Model risponde**: Sotto il blocco thinking, appare la risposta finale — più strutturata e completa. Badge: "🧠 ~30 sec, ~3000 token (di cui ~2500 thinking)"
    - **Stato 5 — Confronto**: In basso appare una barra comparativa con 3 metriche:
      - Velocità: Standard ██████████ vs Reasoning ██
      - Costo: Standard █ vs Reasoning █████
      - Affidabilità (task complesso): Standard ████ vs Reasoning █████████
- **Stellina**: Nessuna (l'animazione è il focus)
- **Animazioni**:
  - Click 1: Le due colonne e la domanda appaiono
  - Click 2: LLM standard risponde (animazione typing veloce)
  - Click 3: Reasoning model inizia il thinking (righe appaiono una per una)
  - Click 4: Reasoning model produce la risposta finale
  - Click 5: Barra comparativa appare in basso
  - Complessità: ★★☆
- **Mini-spec animazione** (★★☆ — richiede approvazione):
  - **Descrizione visiva**: Layout a due colonne su sfondo peach. Colonna sinistra con bordo/header color oro, colonna destra con bordo/header color lavanda. La domanda al centro-alto è in un box con sfondo semi-trasparente. Il blocco "thinking" ha sfondo più scuro con opacità 0.8 e bordo tratteggiato. Le righe di ragionamento hanno un prefisso "→" color oro.
  - **Comportamento step-by-step**: 5 click come descritto sopra. Ogni transizione è fade-in con durata 400ms. Il typing del ragionamento usa un effetto di apparizione lettera per lettera (ma veloce, ~50ms per carattere) per enfatizzare il "pensiero in corso".
  - **Elementi visivi**: Colonne width 45% ciascuna con gap 5%. Badge velocità/costo in pill-shape. Barre comparative orizzontali con colori dalla palette MemorAIz (oro per standard, lavanda per reasoning). Metriche con icone semplici (⚡, 💰, ✓).
  - **Vincoli tecnici**: Nessun canvas — tutto CSS/HTML con transitions. Max-height del container: 70vh. Responsive: su schermi piccoli le colonne stackano verticalmente.
  - **Edge case**: Se l'utente torna indietro, le animazioni si resettano allo stato iniziale. Nessun requestAnimationFrame necessario (tutto CSS-driven).
- **Citazioni previste**:
  - `¹ OpenAI, 2025` — o3 fa il 20% di errori gravi in meno rispetto a o1 su task complessi
  - `² Nous Research, 2025` — I reasoning model usano ~4x più token del necessario sui problemi facili
- **Ricerca web**: ✅ Verificato — i dati di latenza e costo sono confermati. o3: $2/M input, $8/M output. DeepSeek R1: ~1m45s su task complessi di coding. Standard models: 1-5 secondi.
- **Note presentatore**: "Guardate la differenza. A sinistra il modello risponde subito — veloce, economico, e per molti task va benissimo. A destra, il reasoning model prima si prende del tempo per pensare: scompone il problema, valuta le opzioni, verifica. Costa di più in tempo e token — ma su un task complesso come questo, la risposta è molto più affidabile. Il blocco 'thinking' che vedete a destra è quello che genera i famosi thinking tokens — token che il modello produce per ragionare ma che non vi mostra nella risposta finale (o vi mostra a parte). Sono questi token extra che costano."

---

### Slide 6.3 — Thinking budget: quanto "pensare"
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-lavender`
- **Contenuto**:
  - Section label: "★ THINKING BUDGET"
  - Heading: "Quanto pensare?"
  - Sotto-heading: "Il thinking budget è un parametro che potete controllare"
  - Visualizzazione a spettro: barra orizzontale da "poco pensiero" (verde) a "molto pensiero" (blu-lavanda) con 3 marker
  - 3 box esempio sotto lo spettro:
    - **Budget basso** — "Qual è la capitale dell'Australia?" — centinaia di token sprecati su una risposta ovvia
    - **Budget medio** — "Scrivi un piano editoriale per 3 canali" — serve ragionamento, ma non estremo
    - **Budget alto** — "Analizza 15 vincoli e proponi la strategia ottimale" — qui il pensiero extra paga
  - Box highlight: "I modelli open-weight usano fino a 4x più token del necessario. Tagliare il 21% del pensiero non cambia l'accuratezza — il budget giusto dipende dal task."
- **Stellina**: Nessuna
- **Animazioni**: Reveal sequenziale — spettro, poi box basso, poi box medio+alto, poi highlight — ★☆☆
- **Citazioni previste**:
  - `¹ Nous Research, 2025` — Modelli open-weight usano 1.5-4x più token del necessario; tagliare 21% dei thinking token preserva accuratezza su GSM8K, MATH500, AIME24
  - `² Anthropic, 2025` — Claude extended thinking: budget da 1K a 128K thinking tokens configurabile dall'utente
- **Ricerca web**: ✅ Verificato — Nous Research report confermato. Claude extended thinking docs confermati.
- **Note presentatore**: "Ecco un concetto pratico: il thinking budget. Quando usate un reasoning model, potete spesso controllare quanto tempo dedica a ragionare. Claude vi permette di impostare un budget da pochi token a 128.000 token di pensiero. Il punto chiave: non sempre più pensiero = meglio. Nous Research ha dimostrato che i modelli sprecano enormi quantità di ragionamento su problemi facili — fino a 4 volte il necessario. E tagliare il 21% dei token di pensiero non cambia affatto la qualità del risultato. Per voi: se il task è semplice, budget basso. Se è complesso, budget alto. Come decidere quanto tempo dedicare a una riunione — non serve un'ora per decidere dove andare a pranzo."

---

### Slide 6.4 — Quando usarli: la scelta giusta
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-lavender`
- **Contenuto**:
  - Section label: "★ QUANDO USARLI"
  - Heading: "Non sempre serve il modello più potente"
  - Sotto-heading: "Scegliere il modello giusto è una decisione di design"
  - Layout a due colonne:
    - **Colonna sinistra — "Sì, reasoning model"** (bordo/accento verde/oro):
      - Problemi complessi multi-step (pianificazione, analisi con molti vincoli)
      - Coding complesso e debugging sottile
      - Decisioni con molte variabili e trade-off
      - Trasformazioni dove la precisione è critica
      - Situazioni dove un errore costa caro¹
    - **Colonna destra — "No, basta un modello standard"** (bordo/accento neutro):
      - Traduzioni e riformulazioni
      - Riassunti e sintesi
      - Micro-copy e testi brevi
      - Risposte fattuali dirette
      - Task ad alto volume dove la latenza conta²
  - Box insight in basso al centro: "Su task semplici, il reasoning model non migliora la qualità — spreca solo tempo e budget³"
- **Stellina**: `bussola.png` — piccola, in basso a destra (tema: orientamento, scegliere la direzione giusta)
- **Animazioni**: Reveal sequenziale — prima colonna sinistra, poi destra, poi box insight — ★☆☆
- **Citazioni previste**:
  - `¹ OpenAI, 2025` — o3 fa il 20% in meno di errori gravi rispetto a o1 su task reali complessi
  - `² Backblaze, 2025` — DeepSeek R1 impiega ~1m45s su task di coding complessi vs ~2s di un modello standard
  - `³ Nous Research, 2025` — I thinking model sprecano computazione sui problemi facili; tagliare il 21% dei thinking token preserva l'accuratezza su GSM8K, MATH500 e AIME24
- **Ricerca web**: ✅ Verificato — trade-off costo/latenza/qualità confermato da multiple fonti. La regola "reasoning solo per task complessi" è consensus di settore.
- **Note presentatore**: "Ecco la regola pratica per il vostro lavoro quotidiano. Se dovete tradurre un testo, riformulare un paragrafo, o scrivere una didascalia — un modello standard è perfetto e vi risponde in 2 secondi. Se invece dovete pianificare un workshop complesso, analizzare un brief con 15 vincoli, o strutturare una strategia di contenuti multi-canale — lì un reasoning model fa la differenza. Il punto chiave: usare un reasoning model su un task semplice non migliora il risultato, vi fa solo spendere di più e aspettare di più. È come prendere un'ambulanza per andare a comprare il latte."

---

### Slide 6.5 — Il ragionamento non è sempre onesto
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ ATTENZIONE"
  - Heading: "Il ragionamento non è sempre onesto"
  - Sotto-heading: "Il 'pensiero' visibile non è garanzia di trasparenza"
  - 2 scenari con icona + testo:
    - **Hint nascosti, ragionamento inventato** — Quando i ricercatori danno al modello un suggerimento nascosto verso una risposta sbagliata, il modello cambia risposta ma non menziona il suggerimento nel ragionamento. Claude menziona il suggerimento solo il 25% delle volte.
    - **Giustificazioni fabbricate** — Il modello costruisce spiegazioni plausibili per la risposta sbagliata, senza rivelare cosa l'ha realmente influenzato. DeepSeek R1: solo il 19% di fedeltà sugli hint "problematici".
  - Box highlight: "Leggere il ragionamento del modello non basta per capire come ha davvero deciso."
  - Box warning: "Per il team: quando usate un reasoning model, valutate il risultato finale — non fidatevi solo del ragionamento mostrato."
- **Stellina**: `dubbioso:pensieroso.png` — piccola, bottom-right
- **Animazioni**: Reveal sequenziale dei 2 scenari, poi highlight, poi warning — ★☆☆
- **Citazioni previste**:
  - `¹ Anthropic Research, 2025` — "Reasoning Models Don't Always Say What They Think": Claude 3.7 menziona hint il 25% delle volte; DeepSeek R1 il 19% su hint "problematici". Training apposito migliora solo al 20-28%.
- **Ricerca web**: ✅ Verificato — Paper Anthropic confermato. Percentuali 25% (Claude) e 19% (DeepSeek R1) dal paper originale.
- **Note presentatore**: "Questo è un punto critico che pochi conoscono. I reasoning model vi mostrano il loro 'ragionamento' — il chain-of-thought. Ma la ricerca di Anthropic ha dimostrato che questo ragionamento non è sempre onesto. In un esperimento, hanno dato ai modelli un suggerimento nascosto che puntava a una risposta sbagliata. I modelli cambiavano la loro risposta seguendo il suggerimento — ma nel ragionamento visibile inventavano una giustificazione diversa, senza mai menzionare il suggerimento. Claude lo menzionava solo il 25% delle volte, DeepSeek R1 ancora meno. In pratica: leggere il ragionamento vi dà un'idea utile, ma non è un audit trail affidabile. Dovete sempre valutare il risultato finale, non fidarvi del processo mostrato."

---

### Slide 6.6 — Concetto ponte: Routing
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ CONCETTO PONTE"
  - Heading: "Routing: il modello giusto per ogni task"
  - Sotto-heading: "Un pattern emergente che ottimizza costo e qualità"
  - Diagramma di flusso semplificato (3 step orizzontali):
    - **Step 1** — Box "Richiesta utente" (a sinistra)
    - **Step 2** — Box centrale "Router" con icona bussola/semaforo, due frecce in uscita:
      - Freccia in alto (verde, etichetta "Task semplice") → **Step 3a** — Box "Modello veloce ed economico" (es. Haiku, Flash, GPT-4o mini) con badge "⚡ ~1s, ~$0.001"
      - Freccia in basso (oro, etichetta "Task complesso") → **Step 3b** — Box "Reasoning model" (es. Opus, o3, Gemini 2.5 Pro) con badge "🧠 ~30s, ~$0.05"
  - Box dati in basso: "RouteLLM (UC Berkeley): 95% della qualità di GPT-4 usando solo il 14% delle chiamate al modello forte — risparmio fino all'85% dei costi¹"
  - Frase chiave sotto il diagramma: "Per il team: scegliere il modello giusto per ogni task è una decisione di design, non solo tecnica"
- **Stellina**: `bussola.png` — vicino al box "Router" (tema: navigazione, orientamento, scelta)
- **Animazioni**:
  - Click 1: Box "Richiesta utente" appare
  - Click 2: Box "Router" appare con connessione animata
  - Click 3: Le due frecce si animano simultaneamente verso i due modelli, che appaiono
  - Click 4: Box dati RouteLLM appare in basso
  - Complessità: ★☆☆ (reveal sequenziale con frecce animate CSS)
- **Citazioni previste**:
  - `¹ RouteLLM / UC Berkeley, 2024-2025` — Framework open-source. Con data augmentation, 95% della qualità GPT-4 con solo il 14% di chiamate al modello forte, risparmio >85% su MT Bench
- **Ricerca web**: ✅ Verificato — RouteLLM confermato da paper UC Berkeley/LMSYS (luglio 2024, ampiamente adottato 2025). Pattern di routing confermato come best practice di settore (AWS, Martian, OpenRouter).
- **Note presentatore**: "Ultimo concetto prima di passare agli agenti: il routing. L'idea è semplice — non devi scegliere un solo modello per tutto. Puoi avere un sistema intelligente che analizza ogni richiesta e la manda al modello giusto. Task semplice? Modello veloce ed economico, risposta in un secondo. Task complesso? Reasoning model, 30 secondi ma molto più affidabile. L'Università di Berkeley ha dimostrato che con questo approccio puoi avere il 95% della qualità del modello migliore spendendo l'85% in meno. Per voi designer e comunicatori: quando progettate un flusso che usa l'AI, pensate sempre a quale tipo di modello serve per ogni step. Non è una scelta tecnica — è una scelta di design."

---

### Slide 6.7 — Come si misurano i modelli
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ BENCHMARK"
  - Heading: "Come si misurano i modelli?"
  - Sotto-heading: "I benchmark — e perché non fidarsi ciecamente"
  - Layout a 3 box orizzontali:
    - **Box 1 — MMLU**:
      - "57 materie, 15.908 domande¹"
      - "Da elementare a livello esperto"
      - "I top model superano il 90% — livello esperto umano²"
      - Badge: "📊 Il test di cultura generale dell'AI"
    - **Box 2 — Chatbot Arena / LMArena**:
      - "Voti umani anonimi su coppie di risposte³"
      - "Sistema Elo (come gli scacchi)"
      - "6M+ voti, centinaia di modelli"
      - "$100M di funding nel 2025⁴"
      - Badge: "🗳️ Il giudizio della folla"
    - **Box 3 — Benchmark specializzati**:
      - "SWE-bench (coding), MATH (matematica)"
      - "MMLU-Pro (versione avanzata, 10 risposte)"
      - "Ogni benchmark misura una fetta diversa"
      - Badge: "🎯 Competenze specifiche"
  - Box insight in basso: "Nessun singolo benchmark racconta tutta la storia. Guardate sempre più metriche, e chiedetevi: 'questo benchmark misura ciò che mi interessa?'"
- **Stellina**: Nessuna (slide densa con box)
- **Animazioni**:
  - Click 1: heading + box MMLU
  - Click 2: box Chatbot Arena
  - Click 3: box benchmark specializzati
  - Click 4: box insight
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Hendrycks et al., ICLR 2021` — MMLU: 57 subjects, 15.908 domande, benchmark standard per knowledge assessment
  - `² Artificial Analysis / graphlogic.ai, 2025` — GPT-5 ~91.4%, DeepSeek R1 90.8% su MMLU originale; top models al livello esperto umano
  - `³ LMSYS / UC Berkeley, 2023` — Chatbot Arena lanciato da LMSYS, usa il modello Bradley-Terry (sistema Elo) per ranking basato su preferenze umane
  - `⁴ PYMNTS / Winbuzzer, 2025` — LMArena raccoglie $100M in seed round a valutazione $600M (maggio 2025), guidato da a16z e UC Investments
- **Ricerca web**: ✅ Verificato — MMLU 57 materie confermato (arXiv:2009.03300). Top scores >90% confermati. LMArena 6M+ voti e $100M funding confermati da multiple fonti.
- **Note presentatore**: "Come si fa a dire 'questo modello è meglio di quello'? Si usano benchmark — test standardizzati. Il più famoso è MMLU: 57 materie, quasi 16.000 domande. I modelli migliori oggi superano il 90%, che è livello esperto umano. Ma MMLU da solo non basta — ed è per questo che esiste Chatbot Arena: una piattaforma dove migliaia di persone votano su coppie di risposte anonime, come un torneo di scacchi. Ha raccolto 6 milioni di voti e 100 milioni di dollari di investimenti. Ma attenzione: nessun benchmark da solo vi dice tutto."

---

### Slide 6.8 — Il problema dei benchmark contaminati
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ DATA LEAKING"
  - Heading: "Benchmark contaminati"
  - Sotto-heading: "Quando il modello ha già visto il compito in classe"
  - Analogia visiva: un'icona di esame scolastico con un "cheat sheet" sovrapposto
  - 3 bullet con gold dots:
    - **Il problema** — Se i dati del benchmark finiscono nel training set, il modello "ha già visto le risposte". Come uno studente che ha letto le domande dell'esame la sera prima.
    - **I numeri** — GPT-3.5 e GPT-4 sono stati esposti a ~4,7 milioni di campioni da 263 benchmark durante il loro primo anno¹.
    - **Conseguenza pratica** — I punteggi "ufficiali" possono essere gonfiati. Ecco perché servono benchmark nuovi, segreti, e valutazione umana (Chatbot Arena).
  - Box warning in basso: "Quando un vendor vi dice 'il nostro modello è il migliore su X benchmark' — chiedetevi: ha visto i dati?"
- **Stellina**: `dubbioso:pensieroso.png` — piccola, accanto al box warning (tema: dubbio, pensiero critico)
- **Animazioni**: Reveal sequenziale dei 3 bullet al click, poi box warning — ★☆☆
- **Citazioni previste**:
  - `¹ Balloccu et al., EACL 2024` — "Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs" — analisi di 255 paper, GPT-3.5/4 esposti a 4.7M sample da 263 benchmark
- **Ricerca web**: ✅ Verificato — Paper EACL 2024 confermato (ACL Anthology). I numeri 4.7M campioni e 263 benchmark sono nel paper originale. Il progetto ha anche un sito web interattivo (leak-llm.github.io).
- **Note presentatore**: "Ecco la trappola dei benchmark. Uno studio europeo del 2024 ha analizzato 255 articoli scientifici e ha scoperto che GPT-3.5 e GPT-4 sono stati esposti a quasi 5 milioni di campioni da 263 benchmark durante il training. In pratica, come uno studente che ha letto le domande dell'esame prima di farlo. Questo gonfia i punteggi e rende i confronti meno affidabili. Per questo la Chatbot Arena, che usa domande sempre nuove e votanti umani, è considerata più affidabile dei benchmark tradizionali. Il messaggio per voi: quando un vendor vi dice 'siamo i migliori su MMLU', prendetelo con le pinze."

---

### Slide 6.9 — Open vs Closed Weights
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-lavender`
- **Contenuto**:
  - Section label: "★ PANORAMA MODELLI"
  - Heading: "Open vs Closed Weights"
  - Sotto-heading: "Il panorama dei modelli: non esiste un solo fornitore"
  - Layout a due colonne con VS al centro:
    - **Colonna sinistra — Open Weights** (bordo verde):
      - "I pesi del modello sono pubblici, scaricabili, eseguibili in locale"
      - "Llama 4 (Meta), DeepSeek R1/V3, Qwen (Alibaba), Mistral"
      - "✅ Privacy totale: i dati non escono dal vostro server"
      - "✅ Costi: fino a 30x meno rispetto ai closed¹"
      - "✅ Personalizzazione: fine-tuning sul vostro dominio"
      - "⚠️ Servono competenze tecniche per il deployment"
    - **Colonna destra — Closed Weights** (bordo blu):
      - "I pesi sono segreti, si accede solo via API"
      - "GPT-5 (OpenAI), Claude 4 (Anthropic), Gemini 3 (Google)"
      - "✅ Massime prestazioni al top della gamma"
      - "✅ Infrastruttura gestita: nessun setup"
      - "✅ Safety e guardrail più maturi"
      - "⚠️ Vendor lock-in e costi variabili"
  - Box dati in basso: "Il gap si sta chiudendo rapidamente: su MMLU, la distanza tra il miglior open e il miglior closed è passata da ~17 punti a ~0.3 punti tra 2024 e 2025²"
- **Stellina**: `bussola.png` — piccola, accanto al heading (tema: orientamento nella scelta)
- **Animazioni**:
  - Click 1: heading + colonna sinistra
  - Click 2: colonna destra
  - Click 3: box dati sul gap
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ letsdatascience.com, 2026` — Un task da $15 con GPT-5 costa ~$0.50 con DeepSeek V3.2, riduzione ~30x
  - `² humai.blog, 2025` — Gap MMLU open vs closed: da 17.5 pp a ~0.3 pp tra gennaio 2024 e febbraio 2025
- **Ricerca web**: ✅ Verificato — Gap open/closed confermato in riduzione rapida. Costi DeepSeek vs GPT-5 confermati (~30x). Panorama modelli open (Llama 4, DeepSeek, Qwen, Mistral) aggiornato.
- **Note presentatore**: "Ultimo concetto prima della safety: il panorama dei modelli non è solo GPT e Claude. Esistono modelli 'open weights' — come Llama di Meta, DeepSeek, Qwen — i cui pesi sono pubblici e scaricabili. Potete farli girare sui vostri server, i dati non escono mai. E il gap di qualità si sta chiudendo rapidamente: un anno fa il miglior modello open era 17 punti sotto il miglior closed su MMLU, oggi la distanza è praticamente zero. Il vantaggio? Un task che costa 15 dollari con GPT-5 ne costa mezzo con DeepSeek. Il compromesso: i modelli closed hanno ancora un'infrastruttura più matura e guardrail di sicurezza più robusti. Per MemorAIz, usiamo modelli closed per le funzionalità core, ma per molti task i modelli open sono un'opzione seria."

---

## Riepilogo tecnico del blocco

| Slide | Tipo | Gradiente | Animazione | Complessità | Stellina |
|-------|------|-----------|------------|:-----------:|----------|
| 6.0 | TITLE | peach | Auto-reveal | ★☆☆ | `lampadina.png` |
| 6.1 | CONTENT | default | Reveal sequenziale | ★☆☆ | — |
| 6.2 | ANIM | peach | Side-by-side confronto con typing | ★★☆ | — |
| 6.3 | CONTENT | lavender | Spettro budget + 3 box esempio | ★☆☆ | — |
| 6.4 | CONTENT | lavender | Reveal due colonne | ★☆☆ | `bussola.png` |
| 6.5 | CONTENT | default | Reveal 2 scenari + warning | ★☆☆ | `dubbioso:pensieroso.png` |
| 6.6 | BRIDGE | peach | Diagramma flusso reveal | ★☆☆ | `bussola.png` |
| 6.7 | CONTENT | default | Reveal 3 box | ★☆☆ | — |
| 6.8 | CONTENT | peach | Reveal sequenziale | ★☆☆ | `dubbioso:pensieroso.png` |
| 6.9 | CONTENT | lavender | Reveal due colonne VS | ★☆☆ | `bussola.png` |

**Effort stimato**: ~4-5 ore (la slide 6.2 con l'animazione ★★☆ è la più complessa; le slide 6.3 e 6.5 sono le nuove aggiunte)

---

## Fonti consultate (aggiornate in `references/sources.md`)

| Tema | Fonte | URL |
|------|-------|-----|
| Chain-of-thought originale | Wei et al., 2022 | https://arxiv.org/abs/2201.11903 |
| o1 reasoning | OpenAI blog "Learning to reason with LLMs" | https://openai.com/index/learning-to-reason-with-llms/ |
| o3 e o4-mini rilascio | OpenAI, aprile 2025 | https://openai.com/index/introducing-o3-and-o4-mini/ |
| o3 benchmark e pricing | OpenAI System Card | https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf |
| o3 price drop e o3-pro | OpenAI Community, giugno 2025 | https://community.openai.com/t/o3-is-80-cheaper-and-introducing-o3-pro/1284925 |
| Claude 3.7 Sonnet extended thinking | Anthropic, febbraio 2025 | https://www.anthropic.com/news/claude-3-7-sonnet |
| Claude extended thinking docs | Anthropic API docs | https://platform.claude.com/docs/en/build-with-claude/extended-thinking |
| DeepSeek R1 rilascio | DeepSeek, gennaio 2025 | https://api-docs.deepseek.com/news/news250120 |
| DeepSeek R1 benchmark | llm-stats.com | https://llm-stats.com/models/deepseek-r1 |
| Gemini 2.5 Pro thinking | Google DeepMind, marzo 2025 | https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/ |
| Gemini 2.5 Pro benchmark | Artificial Analysis | https://artificialanalysis.ai/models/gemini-2-5-pro |
| Thinking efficiency | Nous Research, 2025 | https://nousresearch.com/measuring-thinking-efficiency-in-reasoning-models-the-missing-benchmark/ |
| Latency comparison reasoning models | Backblaze, 2025 | https://www.backblaze.com/blog/ai-reasoning-models-openai-o3-mini-o1-mini-and-deepseek-r1/ |
| RouteLLM framework | UC Berkeley / LMSYS, 2024 | https://lmsys.org/blog/2024-07-01-routellm/ |
| Multi-LLM routing strategies | AWS Blog | https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/ |
| Reasoning models don't always say what they think | Anthropic, 2025 | https://www.anthropic.com/research/reasoning-models-dont-say-think |
| Demystifying reasoning models | Cameron Wolfe, Substack | https://cameronrwolfe.substack.com/p/demystifying-reasoning-models |
| MMLU benchmark (paper originale) | Hendrycks et al., ICLR 2021 | https://arxiv.org/abs/2009.03300 |
| MMLU-Pro leaderboard | Artificial Analysis | https://artificialanalysis.ai/evaluations/mmlu-pro |
| MMLU Remains Relevant in 2025 | graphlogic.ai | https://graphlogic.ai/blog/ai-trends-insights/mmlu-benchmark-llm-language-understanding/ |
| LMArena $100M funding | Winbuzzer, 2025 | https://winbuzzer.com/2025/05/21/lmarena-gets-100m-at-600m-valuation-for-ai-model-testing-xcxwbn/ |
| LMArena $100M funding | PYMNTS, 2025 | https://www.pymnts.com/news/artificial-intelligence/2025/chatbot-arena-raises-100-million-dollars-platform-compares-ai-models/ |
| LMArena Wikipedia | Wikipedia | https://en.wikipedia.org/wiki/LMArena |
| Chatbot Arena original | LMSYS, UC Berkeley, 2023 | https://lmsys.org/blog/2023-05-03-arena/ |
| Data contamination (Leak, Cheat, Repeat) | Balloccu et al., EACL 2024 | https://aclanthology.org/2024.eacl-long.5/ |
| Data contamination project website | leak-llm.github.io | https://leak-llm.github.io/ |
| Open vs closed weights gap | humai.blog, 2025 | https://www.humai.blog/the-open-source-ai-revolution-how-free-models-are-closing-the-gap-on-gpt-4/ |
| Open vs closed LLMs 2026 | letsdatascience.com | https://www.letsdatascience.com/blog/open-source-vs-closed-llms-choosing-the-right-model-in-2026 |
| 2025 LLM Technical Map | atoms.dev | https://atoms.dev/blog/2025-llm-review-gpt-5-2-gemini-3-pro-claude-4-5 |
