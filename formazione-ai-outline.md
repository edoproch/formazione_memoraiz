# Formazione AI Interna — MemorAIz
## Outline completo per ~3-4 ore di formazione (team UX/UI e Comunicazione)

> **Obiettivo**: dare ai colleghi un'intuizione solida su come funzionano i sistemi AI, così da poter (1) lavorare meglio con gli strumenti AI-first, (2) capire cosa si può e non si può fare quando si vendono servizi AI, (3) dialogare con il team tecnico con un linguaggio comune.

---

## Tabella tempi stimati

| Blocco | Durata | Contenuto |
|--------|-------:|-----------|
| 0. Setup | 10' | Aspettative, framing mentale |
| 1. Storia + mappa concetti | 25' | Timeline, AI ⊃ ML ⊃ DL ⊃ LLM, training vs inference |
| 2. Fondamenti ML | 35' | Supervised/unsupervised/self-supervised, reti neurali, backprop, generalizzazione |
| 3. Come funzionano gli LLM | 55' | Token, next-token, pretraining/SFT/RL, attenzione, allucinazioni, multimodalità |
| 4. Context engineering | 40' | Perché il contesto domina, best practice, context rot, prompt injection, mini-workshop |
| 5. Embeddings & RAG | 35' | Spazio semantico, tipi di embedding, pipeline RAG |
| 6. Reasoning models | 20' | Quando usarli, trade-off costo/latenza/affidabilità |
| 7. Agenti (deep dive) | 55' | Tools, MCP, orchestrazione, memory, skills, observability, sicurezza |
| 8. Checklist operativa | 10' | Decision tree, regole d'oro, template prompt aziendale |

> **Se vuoi chiudere in 3 ore**: riduci Blocco 2 a 20' e Blocco 6 a 10', rendi la parte agenti più demo-centrica.

---

# BLOCCO 0 — SETUP (~10 min)

## 0.1 Perché questa formazione
- Obiettivo: linguaggio comune + "guardrail" operativi (qualità, privacy, sicurezza, IP).
- Output atteso: saper scrivere richieste efficaci, valutare risposte, e capire cosa vendere (e cosa no) ai clienti.

## 0.2 Concetto fondamentale: "Probabilistico, non deterministico"
- Un LLM **non "sa"** come un umano: produce testo **plausibile** dato un contesto.
- **Eloquenza ≠ accuratezza**: il fatto che una risposta suoni sicura e ben scritta non significa che sia vera.
- Piccola demo suggerita: stessa domanda, risposte diverse (cambiando temperatura o riformulando leggermente).

## 0.3 Dove si sbaglia più spesso
- Confondere **conoscenza** (cosa il modello "sa") vs **comportamento** (come risponde) vs **accesso a dati** (cosa può consultare).
- Pensare che "ha funzionato una volta" significhi "funzionerà sempre".
- Scambiare il chatbot per un database di fatti verificati.

---

# BLOCCO 1 — STORIA DELL'AI + MAPPA CONCETTI (~25 min)

## 1.1 Timeline essenziale
- **1950s-60s**: Nascita dell'AI come campo (Turing, Dartmouth Conference 1956). Primi sistemi simbolici: regole scritte a mano ("if-then"). Grandi promesse.
- **1970s-80s**: Primo "AI Winter" — i sistemi simbolici non scalano. Poi i sistemi esperti (anni '80) portano un revival breve.
- **1990s-2000s**: Machine Learning statistico prende piede. Le macchine imparano dai dati invece che da regole scritte. Deep Blue batte Kasparov (1997), ma è ancora un sistema molto specializzato.
- **2012**: Momento di svolta — AlexNet vince ImageNet. Il Deep Learning dimostra di funzionare su larga scala grazie alle GPU.
- **2017**: Paper "Attention Is All You Need" — nasce l'architettura Transformer, fondamento di tutti gli LLM moderni.
- **2020-oggi**: GPT-3, ChatGPT, Claude, Gemini, modelli multimodali, agenti. Esplosione consumer e enterprise.

> **💡 Messaggio chiave**: L'AI non è nata ieri. Quello che è cambiato è la scala dei dati, la potenza di calcolo e l'architettura Transformer. Ogni ondata ha spostato il confine tra "cosa automatizziamo" e "cosa resta umano".

## 1.2 I cerchi concentrici: AI ⊃ ML ⊃ Deep Learning ⊃ LLM
Visualizzare come cerchi concentrici (tipo matrioska):

- **Artificial Intelligence (AI)**: Qualsiasi sistema che esegue compiti che normalmente richiederebbero intelligenza umana. Include anche sistemi basati su regole scritte a mano (es. un chatbot con risposte pre-programmate).
- **Machine Learning (ML)**: Sottoinsieme dell'AI. Il sistema **impara dai dati** invece di seguire regole esplicite. Trova pattern nei dati e li usa per fare previsioni.
- **Deep Learning (DL)**: Sottoinsieme del ML. Usa **reti neurali con molti strati** (da qui "deep"). Capace di imparare rappresentazioni sempre più astratte e complesse.
- **LLM (Large Language Model)**: Sottoinsieme del DL. Reti neurali **molto grandi**, addestrate su **enormi quantità di testo**, specializzate nel comprendere e generare linguaggio naturale.

> **💡 Analogia**: AI è "veicoli", ML è "veicoli a motore", DL è "automobili", LLM è "Tesla Model S". Ogni livello è più specifico del precedente.

## 1.3 🔗 Concetto ponte: Training vs Inference
- **Training** = la fase in cui il modello impara dai dati, aggiustando miliardi di pesi. Costa milioni di dollari e settimane di GPU.
- **Inference** = la fase in cui il modello usa quei pesi per generare output. È quello che succede quando chattate con Claude o ChatGPT.
- **Implicazione pratica fondamentale**: quando chattate con un LLM, **non lo state "insegnando"**. Il modello non impara dalla vostra conversazione (salvo meccanismi espliciti di memoria, che sono altra cosa). Ogni conversazione parte dallo stesso modello base.

## 1.4 Cosa rende gli LLM "diversi" dal ML tradizionale
- **Scala**: trilioni di token di dati, centinaia di miliardi di parametri.
- **Architettura**: il Transformer con il meccanismo di attenzione.
- **Obiettivo semplice ma potente**: predire il prossimo token.
- **Emergenza di abilità**: capacità che emergono con la scala (ragionamento, traduzione, coding) ma **senza garanzia di verità**.

---

# BLOCCO 2 — FONDAMENTI ML "SENZA MATEMATICA" (~35 min)

## 2.1 Supervised Learning (Apprendimento Supervisionato)
- Il modello impara da **esempi etichettati**: coppie (input → output corretto).
- Come un insegnante che corregge i compiti: il modello fa una previsione, viene confrontata con la risposta giusta, e il modello si aggiusta.
- **Esempi vicini a UX/Comms**: classificazione email (spam/non spam), moderazione contenuti, analisi sentiment di recensioni, classificazione ticket di supporto.

## 2.2 Unsupervised Learning (Apprendimento Non Supervisionato)
- Il modello riceve **dati senza etichette** e deve trovare struttura e pattern da solo.
- Come dare a qualcuno un mazzo di carte sconosciute e chiedergli di organizzarle in gruppi sensati.
- **Esempi**: segmentazione clienti per comportamento, clustering di temi, scoperta di anomalie.

## 2.3 🔗 Concetto ponte: Self-Supervised Learning
- **Fondamentale per capire gli LLM!** È una via di mezzo: il modello crea le proprie "etichette" dal testo stesso.
- Esempio: prendi una frase, nascondi l'ultima parola, e il modello deve prevederla. L'etichetta è la parola nascosta, che era già nel testo originale.
- Questo è esattamente ciò che fanno gli LLM durante il pre-training: predire il prossimo token. Nessun umano etichetta "a mano" ogni frase — il segnale di supervisione viene dai dati stessi.

## 2.4 🔗 Concetto ponte: Generalizzazione vs Overfitting
- **Overfitting**: il modello "impara a memoria" i dati di training. Funziona benissimo sugli esempi già visti, va male su casi nuovi.
- **Generalizzazione**: il modello cattura pattern veri che funzionano anche su dati nuovi, mai visti.
- **Analogia**: studiare per un esame memorizzando le risposte di quello dell'anno scorso (overfitting) vs capire la materia e saper rispondere a domande nuove (generalizzazione).
- **Implicazione pratica**: "l'LLM ha risposto bene a questa domanda una volta" **non significa** che risponderà sempre bene a domande simili. Serve testare su casi diversi.

## 2.5 Struttura di una rete neurale (intuitiva, zero formule)

### Il neurone artificiale
- Prende degli **input** (numeri), li **pesa** (alcuni input contano di più di altri), li **somma**, e produce un **output**.
- **Analogia**: come prendere una decisione. "Devo portare l'ombrello?" → Guardo il cielo (peso: alto), guardo il meteo (peso: alto), guardo se ho fretta (peso: basso). Peso le informazioni e decido.

### La rete
- I neuroni sono organizzati in **strati** (layers):
  - **Input layer**: riceve i dati grezzi.
  - **Hidden layers**: strati intermedi dove avviene la "magia" — il modello impara rappresentazioni sempre più astratte.
  - **Output layer**: produce il risultato finale.
- **Più strati = più capacità di catturare complessità** (ecco perché "deep" learning).
- **Analogia visiva**: immaginare una catena di montaggio. Ogni stazione (layer) lavora il pezzo un po' di più, aggiungendo dettaglio e raffinamento.

### I pesi (weights)
- Ogni connessione tra neuroni ha un **peso**: un numero che dice "quanto è importante questa connessione".
- All'inizio i pesi sono **casuali** → il modello spara a caso.
- Durante l'addestramento, i pesi vengono **aggiustati** per migliorare le previsioni.
- **Quando diciamo che un modello ha "175 miliardi di parametri" (come GPT-3), stiamo dicendo che ha 175 miliardi di questi pesi da regolare.**

## 2.6 Backpropagation (l'intuizione)
- Il modello fa una previsione → la confronta con la risposta giusta → calcola **quanto ha sbagliato** (errore/loss).
- Poi "torna indietro" lungo la rete (da qui "back-propagation") e **aggiusta i pesi** per sbagliare un po' meno la prossima volta.
- Ripete questo processo **milioni/miliardi di volte** su enormi dataset.
- **Analogia**: come accordare una chitarra. Suoni una nota, senti che è stonata, giri la chiave un po'. Risuoni. Ancora stonata ma meno. Continui finché non è accordata. Ora immagina di dover accordare 175 miliardi di chiavi contemporaneamente — ecco perché servono le GPU.

> **💡 Concetto chiave**: L'addestramento è un processo di **ottimizzazione iterativa**, non "regole scritte a mano". Il modello non "capisce" — aggiusta pesi per minimizzare l'errore sugli esempi di training.

---

# BLOCCO 3 — COME FUNZIONANO GLI LLM (~55 min)

## 3.1 Tokenizzazione — Concetto ponte fondamentale
Prima di tutto: gli LLM non leggono "parole". Leggono **token**.

- Un **token** è un frammento di testo: può essere una parola, una parte di parola, un segno di punteggiatura, uno spazio.
- Esempio: "MemorAIz è fantastica" → potrebbe diventare `["Memor", "AI", "z", " è", " fantast", "ica"]`
- Perché è importante:
  - I **limiti di contesto** si misurano in token (es. 200K token per Claude).
  - I **costi API** si misurano in token (input + output).
  - Lingue diverse hanno efficienza diversa: l'italiano usa ~1.5x più token dell'inglese per lo stesso concetto.
  - La **compressione e la struttura** del testo contano: un prompt ben scritto usa meno token e lascia più spazio al contesto utile.

## 3.2 Il cuore di un LLM: predire il prossimo token
- **Task fondamentale**: dato tutto il testo precedente, qual è il token più probabile che viene dopo?
- Il modello produce una **distribuzione di probabilità** su tutto il suo vocabolario (es. 100.000+ token possibili) e sceglie.
- Esempio: "Il gatto si è seduto sul ___" → {tappeto: 15%, divano: 12%, pavimento: 8%, ...}
- **La generazione è autoregressiva**: il token scelto viene aggiunto al contesto, e il modello predice il prossimo, e così via. Parola dopo parola, frase dopo frase.

> **💡 Insight fondamentale**: Tutto ciò che un LLM produce — saggi, codice, poesie, analisi — emerge da questo meccanismo apparentemente semplice ripetuto migliaia di volte. La complessità emerge dalla scala.

## 3.3 Temperatura e Sampling (Decoding)
Come il modello sceglie tra i token possibili:

- **Temperatura** = quanto il modello è "creativo" nella scelta del prossimo token.
  - **Temperatura bassa (es. 0)**: sceglie quasi sempre il token più probabile → output deterministico, prevedibile, "sicuro".
  - **Temperatura alta (es. 1+)**: distribuisce le probabilità più uniformemente → output più vario, creativo, ma anche più rischioso.
- **Top-p (nucleus sampling)**: invece di considerare tutti i token, considera solo quelli che insieme coprono una certa probabilità (es. il 90%). Altro modo di controllare la "varietà".
- **Analogia**: come un cuoco. Temperatura bassa = segue la ricetta alla lettera. Temperatura alta = improvvisa e sperimenta.
- **Implicazione pratica**: per task creativi (brainstorming, copy) si usa temperatura più alta; per task precisi (analisi dati, codice, policy) temperatura più bassa. Stessa distribuzione → scelte diverse: ecco perché la stessa domanda può dare risposte diverse.

## 3.4 Le tre fasi di addestramento

### Fase 1: Pre-Training
- Il modello viene addestrato su **enormi quantità di testo** (internet, libri, articoli, codice...) — trilioni di token.
- Task: self-supervised learning → predire il prossimo token.
- **Cosa ottiene il modello**: una vastissima "conoscenza del mondo" e la capacità di generare testo coerente. Ma è come un enciclopedista senza filtro — sa tutto ma non sa come essere utile.
- **Analogia**: è come leggere l'intera biblioteca di Babele. Sai tantissimo, ma nessuno ti ha detto come usare quella conoscenza per aiutare qualcuno.

### Fase 2: Supervised Fine-Tuning (SFT)
- Il modello viene addestrato su **esempi curati** di conversazioni domanda-risposta di alta qualità, scritte da annotatori umani.
- **Cosa aggiunge**: il modello impara il **formato** di un assistente utile. Impara a seguire istruzioni, a rispondere alle domande invece di continuare il testo, a dire "non lo so" invece di inventare.
- **Analogia**: dopo aver letto tutta la biblioteca, un tutor ti insegna come usare quella conoscenza per rispondere alle domande degli studenti.

### Fase 3: Reinforcement Learning (RL / RLHF / RLAIF)
- Annotatori umani (o un altro modello AI nel caso di RLAIF) **valutano e confrontano** le risposte del modello: "questa risposta è migliore di quest'altra".
- Il modello viene aggiustato per produrre risposte che gli umani preferiscono.
- **Cosa aggiunge**: allineamento con le preferenze umane — sicurezza, utilità, onestà, tono appropriato. È qui che il modello impara a non essere tossico, a rifiutare richieste pericolose, ecc.
- **⚠️ Attenzione**: RL cambia il **comportamento** del modello, non aggiunge "fatti" in modo affidabile. Non è una nuova enciclopedia.
- **Analogia**: come un cameriere che impara non solo a servire i piatti (SFT), ma a capire come il cliente preferisce essere servito, cosa non dire, come gestire lamentele (RL).

> **💡 Schema mentale**: Pre-training = conoscenza grezza | SFT = saper seguire istruzioni | RL = saper farlo *bene e in modo sicuro*

## 3.5 Tutto il contesto influenza la risposta

### Il meccanismo di Attenzione (semplificato)
- Quando un LLM genera un token, **non guarda solo le ultime parole**. Guarda **tutto il contesto** disponibile e decide quali parti sono più rilevanti in quel momento.
- Questo è il meccanismo di **attenzione** (attention) — l'innovazione chiave dei Transformer.
- **Analogia**: quando leggi una frase ambigua in un libro, i tuoi occhi tornano indietro a cercare indizi nel paragrafo precedente, o nel capitolo, o persino nel titolo. L'attenzione fa qualcosa di simile, ma su tutto il contesto simultaneamente.

### Implicazioni pratiche cruciali
- **Il system prompt** influenza ogni singola risposta.
- **L'ordine** in cui presenti le informazioni conta.
- **Anche le risposte precedenti** del modello (nella stessa conversazione) influenzano le risposte successive — se il modello "sbaglia" e non lo correggi, continuerà su quella strada.
- **Tutto ciò che è nel contesto è "segnale"** — informazioni irrilevanti o contraddittorie possono degradare la qualità.
- Il modello non ha "intenzioni": segue segnali nel prompt. Ordine, salienza, esempi e vincoli cambiano la traiettoria.

## 3.6 Allucinazioni (Hallucinations)

### Cosa sono
- Quando un LLM genera informazioni **plausibili ma false**: fatti inventati, citazioni inesistenti, dati fabbricati.
- **Non è un "bug raro"**: è una modalità normale del modello quando mancano vincoli o fonti. È una conseguenza diretta del meccanismo di predizione del prossimo token — il modello sceglie token probabili, non token "veri".

### Perché succedono
- Il modello non ha un "database di fatti" da consultare. Ha pattern statistici appresi dal training data.
- Se non ha abbastanza informazioni su un argomento, **riempie i buchi** con token probabili — che possono essere completamente inventati.
- Il modello non "sa di non sapere" in modo affidabile (il fine-tuning e l'RL aiutano, ma non risolvono al 100%).

### Implicazioni per il nostro lavoro
- **Mai fidarsi ciecamente** dell'output di un LLM per fatti specifici, numeri, date, citazioni.
- Usare RAG per ancorare le risposte a fonti verificabili.
- Progettare i prodotti con meccanismi di **verifica e attribuzione** (es. mostrare le fonti).
- Comunicare ai clienti i limiti reali del sistema.
- Un "non lo so" è accettabile e preferibile a un'invenzione.

## 3.7 🔗 Concetto ponte: Multimodalità
- I modelli moderni non lavorano solo con testo. Possono **comprendere e/o generare** anche:
  - **Immagini** (vision): analizzare screenshot, foto, documenti scansionati, mockup.
  - **Audio**: trascrizione, comprensione, generazione vocale.
  - **Video**: analisi di contenuti video (emergente).
  - **Codice**: lettura e scrittura di codice in molti linguaggi.
- **Implicazione pratica**: potete dare a Claude uno screenshot di un design e chiedergli di generare il codice, o dargli un'immagine di una tabella e chiedergli di estrarre i dati. Figma Make si basa esattamente su questo.

---

# BLOCCO 4 — CONTEXT ENGINEERING & PROMPTING (~40 min)

Questa è la parte più direttamente utile per il team UX/Comms. Qui si passa dalla teoria alla pratica.

## 4.1 Context Window: cosa è
- La **quantità massima di testo** (in token) che un LLM può "vedere" in una singola interazione.
- Esempi attuali: Claude → 200K token (~150K parole), GPT-4o → 128K token.
- **Include tutto**: system prompt + cronologia conversazione + documenti allegati + la domanda + la risposta in generazione.

## 4.2 Context Engineering: definizione operativa
- **Non è solo "prompt engineering"** (scrivere un buon prompt). È la disciplina di **progettare tutto ciò che entra nella finestra di contesto**: cosa ci va, in che forma, in che ordine, con quali vincoli.
- Obiettivo: ridurre ambiguità e aumentare verificabilità.

## 4.3 Template pratico (riusabile dal team)
Un buon prompt strutturato contiene:
1. **Scopo** (1 riga): cosa deve fare il modello.
2. **Pubblico/Tono** (brand voice, registro).
3. **Vincoli** (lunghezza, lingua, formato, cosa NON fare).
4. **Fonti** (testo di riferimento, estratti, link).
5. **Criteri di qualità** (checklist per valutare l'output).
6. **Output atteso** (un esempio concreto di come dovrebbe essere il risultato).

> **💡 Regola d'oro**: separare le **istruzioni** (cosa fare) dalle **fonti** (su cosa basarsi). Mescolarle aumenta allucinazioni e fraintendimenti.

## 4.4 Best practices di context engineering
1. **Chiarezza e struttura**: usare formati chiari (markdown, XML, JSON) per separare istruzioni, contesto e domanda. Il modello è sensibile alla struttura.
2. **Few-shot examples**: dare 2-3 esempi concreti di input → output desiderato è spesso più efficace di lunghe descrizioni. Mostrare > descrivere.
3. **Istruzioni specifiche, non vaghe**: "Rispondi in italiano, in massimo 3 paragrafi, con un tono professionale ma accessibile" > "Rispondi bene".
4. **Ruolo e identità**: dare al modello un ruolo specifico ("Sei un esperto UX designer con 15 anni di esperienza") orienta le risposte.
5. **Iterazione**: il context engineering è un processo iterativo. Testa, valuta, aggiusta.

## 4.5 Context Rot / Lost in the Middle
- In **conversazioni lunghe**: i vincoli iniziali si "diluiscono", aumentano contraddizioni e drift. Il modello perde di vista le istruzioni originali.
- Anche in **contesti singoli molto lunghi**: ricerche hanno mostrato che i modelli tendono a prestare più attenzione a **ciò che è all'inizio e alla fine** del contesto, e meno a ciò che è **nel mezzo** ("Lost in the Middle").
- **Analogia**: come leggere un documento di 300 pagine in fretta — ricordi bene l'introduzione e la conclusione, ma i dettagli a pagina 150 ti sfuggono.
- **Mitigazioni pratiche**:
  - Mettere le informazioni più importanti **all'inizio o alla fine** del contesto.
  - In conversazioni lunghe: fare **reset controllati** (nuova conversazione con un riassunto dello stato).
  - Usare **riepiloghi periodici** ("fino ad ora abbiamo deciso X, Y, Z").
  - Non fidarsi ciecamente di contesti molto lunghi.

## 4.6 🔗 Concetto ponte: Prompt Injection (da spiegare senza panico)
- **Cosa è**: quando contenuti esterni (es. testo incollato, documenti caricati) contengono istruzioni che provano a "comandare" il modello, sovrascrivendo le istruzioni del sistema (es. "ignora le istruzioni precedenti e fai X").
- **Perché è rilevante per UX/Comms**: se state progettando prodotti AI per i clienti, dovete sapere che utenti (o testi) malevoli possono tentare di manipolare il sistema.
- **Implicazioni per il design**:
  - Segnare chiaramente cosa è *contenuto utente* vs *istruzioni sistema*.
  - Non eseguire azioni ad alto impatto (invio email, modifiche dati) senza conferma dell'utente.
  - È una vulnerabilità nota e attiva: fa parte delle OWASP Top 10 per applicazioni LLM.

## 4.7 Mini-workshop suggerito (~10 minuti)
- Stesso task (es. scrivere un post LinkedIn per MemorAIz):
  1. **Prompt vago**: "Scrivi un post LinkedIn per la nostra startup"
  2. **Prompt strutturato**: con scopo, tono, vincoli, audience
  3. **Prompt + esempi + checklist**: aggiungere un esempio di post che vi piace e criteri di qualità
- **Debrief**: confrontare i 3 output. Cosa è migliorato e perché? Questo rende tangibile tutto il blocco.

---

# BLOCCO 5 — EMBEDDINGS & RAG (~35 min)

## 5.1 Cosa sono gli Embeddings (intuizione)
- Un embedding è una **rappresentazione numerica** (un vettore, cioè una lista di numeri) di un pezzo di testo.
- Ogni parola/concetto viene mappato in uno **spazio multidimensionale** (centinaia o migliaia di dimensioni).
- **Concetti simili finiscono vicini** in questo spazio; concetti diversi finiscono lontani.
- **Analogia**: immaginate una mappa dove ogni parola è un punto. Le parole con significato simile formano dei "quartieri".

## 5.2 L'intuizione geometrica (analogie vettoriali)
- La cosa straordinaria: le **direzioni** nello spazio catturano relazioni semantiche.
- Il famoso esempio: `vettore("re") - vettore("uomo") + vettore("donna") ≈ vettore("regina")`
  - La "direzione" da uomo a donna, applicata a re, porta a regina!
  - Questo funziona perché il modello ha catturato la relazione semantica di genere.
- Altri esempi: `Parigi - Francia + Italia ≈ Roma`, `buono - migliore ≈ cattivo - peggiore`
- **⚠️ Nota**: questa intuizione viene da embedding *statici* tipo word2vec. Con embedding moderni (contestuali, di frase/documento) l'intuizione geometrica resta valida, ma l'analogia aritmetica non è una legge universale — è un'illustrazione del principio.

## 5.3 🔗 Concetto ponte: Tipi di embedding
- **Embedding di parola (statici)**: ogni parola ha un unico vettore fisso (word2vec, GloVe). "Banco" ha lo stesso vettore sia in "banco di scuola" che in "banco di pesci".
- **Embedding contestuali**: la rappresentazione dipende dal contesto. "Banco" ha vettori diversi nelle due frasi sopra. Sono quelli usati internamente dai Transformer.
- **Embedding di frase/documento**: rappresentano interi chunk di testo in un unico vettore. Sono quelli usati per la RAG — catturano il significato complessivo di un paragrafo.

## 5.4 Visualizzazione
- In realtà gli embeddings vivono in spazi con centinaia di dimensioni (es. 1536 per alcuni modelli OpenAI, 3072 per altri).
- Per visualizzarli, si usano tecniche di **riduzione dimensionale** (t-SNE, UMAP) per proiettarli in 2D o 3D.
- Nei grafici 2D/3D si vedono chiaramente i "cluster" di concetti simili.
- Suggerimento: mostrare una demo live o screenshot di un embedding visualizer.

## 5.5 RAG (Retrieval-Augmented Generation)

### Il problema
- Gli LLM hanno una **conoscenza fissa** (cristallizzata al momento del training) e una **finestra di contesto limitata**.
- Non conoscono i documenti interni della vostra azienda, le informazioni aggiornate, o dati specifici del vostro dominio.
- Se gli chiedi qualcosa che non sa, potrebbe **inventare** (allucinare).

### La soluzione: RAG
- **Retrieve**: prima di far rispondere l'LLM, cerchi nei tuoi documenti/database le informazioni rilevanti alla domanda dell'utente, usando embeddings e ricerca semantica.
- **Augment**: inserisci i frammenti trovati nel contesto dell'LLM come materiale di riferimento.
- **Generate**: l'LLM genera la risposta basandosi sia sulla sua conoscenza che sui documenti forniti.
- **Analogia**: come uno studente che, prima di rispondere a una domanda d'esame, può consultare i suoi appunti. Non deve ricordare tutto a memoria — basta che sappia dove cercare e come usare ciò che trova.

## 5.6 La pipeline RAG in dettaglio (6 passi)
1. **Ingest & pulizia**: raccogliere i documenti, pulirli, normalizzare formati.
2. **Chunking**: dividere i documenti in frammenti di dimensione gestibile (paragrafi, sezioni).
3. **Embedding**: trasformare ogni chunk nel suo vettore numerico.
4. **Retrieval**: quando arriva una domanda, convertirla in vettore e trovare i chunk più simili (nearest neighbor search).
5. **Reranking/filtri**: ri-ordinare e filtrare i risultati per qualità e rilevanza (opzionale ma molto utile).
6. **Generation + citazioni**: passare i chunk migliori all'LLM nel contesto e generare la risposta, idealmente con citazioni alle fonti.

> **💡 Nota critica**: La qualità di un sistema RAG dipende enormemente dalla qualità del retrieval. Se recuperi i documenti sbagliati, anche il miglior LLM darà risposte sbagliate. "Garbage in, garbage out."

## 5.7 Implicazioni per UX/Comms
- **Citazioni**: mostrare le fonti aumenta la fiducia dell'utente e permette audit.
- **"Non lo so" è accettabile**: se il retrieval non trova nulla di rilevante, il sistema dovrebbe dirlo chiaramente invece di inventare.
- **UI patterns**: mostrare le fonti, permettere "apri passaggio originale", indicare la data di aggiornamento dei documenti.

---

# BLOCCO 6 — REASONING MODELS (~20 min)

## 6.1 Cosa sono
- Modelli addestrati specificamente per **"pensare passo dopo passo"** prima di dare una risposta.
- Esempi: OpenAI o1/o3, Claude con extended thinking, DeepSeek R1.
- Generano una **catena di ragionamento** (chain of thought) — a volte visibile, a volte nascosta — prima della risposta finale.
- **Importante**: anche loro restano modelli di *next-token*. Non è magia: cambia il training (più RL orientato al ragionamento) e l'inference (più token dedicati al "pensare").

## 6.2 Come funzionano (intuitivo)
- Invece di rispondere "di getto" (come un modello standard), usano token extra per ragionare, scomporre il problema, valutare opzioni, verificare la propria logica.
- Sono addestrati con RL specifico per il ragionamento: vengono premiati non solo per la risposta giusta, ma per il processo logico.

## 6.3 Quando usarli
- **Sì**: problemi complessi multi-step, pianificazione, analisi con criteri, coding complesso, decisioni con molte variabili, trasformazioni dove la precisione è critica.
- **No**: task semplici e diretti (traduzioni, riassunti, micro-copy rapido). Spesso basta un modello più leggero.
- **Trade-off**: più costo, più latenza, spesso più affidabilità su compiti difficili.

## 6.4 🔗 Concetto ponte: Routing
- Pattern emergente: usare un **modello leggero e veloce** per task semplici, e **escalare automaticamente** a un reasoning model quando il task è complesso.
- Permette di ottimizzare il rapporto costo/qualità. Non serve sempre il modello più potente.
- **Per il team**: scegliere il modello giusto per il task è una decisione di design, non solo tecnica.

---

# BLOCCO 7 — AGENTI AI: IL DEEP DIVE (~55 min)

## 7.1 Dall'LLM all'Agente: cosa cambia

### Solo LLM
- Riceve input → genera output testuale. Fine.
- È **reattivo**: risponde a ciò che gli chiedi, una volta, dentro la finestra di contesto.
- Non può fare azioni nel mondo reale, non può cercare informazioni in tempo reale, non può eseguire codice.
- **Analogia**: un esperto seduto in una stanza senza telefono né computer, che risponde solo a voce alle tue domande.

### Agente AI
- Un LLM + la capacità di **osservare, pianificare, agire e iterare**.
- Ha un **loop**: riceve un obiettivo → ragiona su come procedere → usa strumenti → osserva il risultato → decide se ha finito o deve continuare.
- Può **interagire con il mondo esterno**: cercare su internet, leggere/scrivere file, chiamare API, eseguire codice.
- Differenza chiave: ha **azioni** e **stato**.
- **Analogia**: lo stesso esperto, ma ora ha un telefono, un computer, accesso a database, e sa usarli autonomamente per completare compiti complessi.

### Il loop agente (Observe → Think → Act)
```
              ┌──────────────────────┐
              │   Obiettivo/Prompt   │
              └──────────┬───────────┘
                         ▼
              ┌──────────────────────┐
              │   🔍 OBSERVE         │
              │   (leggi contesto,   │
              │    risultati tools)  │
              └──────────┬───────────┘
                         ▼
              ┌──────────────────────┐
              │   🧠 THINK           │
              │   (ragiona, pianifica│
              │    prossima azione)  │
              └──────────┬───────────┘
                         ▼
              ┌──────────────────────┐
              │   ⚡ ACT             │
              │   (usa un tool,      │
              │    genera risposta)  │
              └──────────┬───────────┘
                         ▼
                   Obiettivo     ──No──→ Torna a OBSERVE
                   raggiunto?
                      │
                     Sì
                      ▼
              ┌──────────────────────┐
              │   📤 Risposta finale │
              └──────────────────────┘
```

## 7.2 Tools: le mani dell'agente

### Cosa sono
- **Funzioni o API** che l'LLM può decidere di invocare durante la conversazione.
- L'LLM non esegue direttamente il tool — genera una **richiesta strutturata** (tipo JSON) che dice "voglio chiamare questa funzione con questi parametri". Il sistema esterno esegue la funzione e restituisce il risultato all'LLM.

### Esempi concreti
- `web_search(query)`: cerca informazioni sul web.
- `send_email(to, subject, body)`: invia un'email.
- `query_database(sql)`: interroga un database.
- `create_file(name, content)`: crea un file.
- `get_weather(city)`: ottieni il meteo.

### Come funziona il "tool calling"
1. L'LLM riceve la domanda dell'utente + la **lista dei tool disponibili** con le loro descrizioni.
2. L'LLM decide **se** usare un tool e **quale** usare.
3. L'LLM genera una chiamata strutturata al tool (es. `{"tool": "web_search", "query": "meteo Bologna"}`).
4. Il sistema esterno esegue la chiamata e restituisce il risultato.
5. L'LLM legge il risultato e decide: rispondere all'utente, o fare un'altra chiamata a un tool.

### Perché sono fondamentali
- Permettono all'LLM di **superare i suoi limiti**: accesso a dati in tempo reale, esecuzione di azioni, calcoli precisi.
- **La qualità delle descrizioni dei tool è cruciale**: se il tool è descritto male, il modello non saprà quando/come usarlo.

## 7.3 🔗 Concetto ponte: Failure modes dei tool
- I tool possono **fallire**: timeout, errori API, dati incompleti o malformati.
- I tool possono **restituire contenuto malevolo**: testo che tenta prompt injection.
- L'output di un tool diventa **nuovo contesto** per l'LLM → può introdurre errori o manipolazioni.
- **Pattern di difesa**: retries controllati, timeouts, validazione dello schema dell'output, conferme utente per azioni sensibili (invio email, modifica dati, acquisti).

## 7.4 MCP (Model Context Protocol)

### Il problema che risolve
- Ogni provider AI e ogni applicazione ha il proprio modo di definire e chiamare i tool.
- **N servizi × M piattaforme AI = N×M integrazioni** → non scala.

### Cos'è MCP
- Uno **standard aperto** (creato da Anthropic) per connettere gli LLM a fonti di dati e strumenti esterni.
- Definisce un protocollo comune: come descrivere i tool, come chiamarli, come restituire i risultati.
- **Un servizio implementa MCP una volta → funziona con qualsiasi client che supporta MCP.**
- **N servizi × 1 protocollo = N integrazioni** → scala molto meglio.

### Architettura (semplificata)
```
┌──────────────┐     MCP Protocol     ┌──────────────┐
│  Client AI   │◄────────────────────►│  MCP Server  │
│  (Claude,    │    (standard)         │  (Figma,     │
│   Cursor,    │                       │   Slack,     │
│   IDE...)    │                       │   il tuo     │
│              │                       │   servizio)  │
└──────────────┘                       └──────────────┘
```

### Esempi concreti
- **Figma MCP Server**: permette a Claude di leggere i design, generare screenshot dei nodi, ottenere contesto di design. Lo usiamo già!
- **GitHub MCP Server**: l'AI può creare PR, leggere issues, cercare nel codice.
- **Database MCP Server**: l'AI può interrogare direttamente il database aziendale.
- **Google Drive MCP Server**: l'AI può cercare e leggere documenti dal Drive.

### Perché interessa a UX/Comms
- Integrare strumenti di lavoro (design, docs, project management) senza "copia/incolla" continuo.
- Come azienda che vende servizi AI, potreste **creare MCP server** per i vostri clienti.
- **Ma**: aumenta la superficie di rischio (accessi, permessi, injection). Serve gestione attenta.

## 7.5 🔗 Concetto ponte: Sicurezza negli Agenti
- **Rischi tipici**:
  - Prompt injection via tool output (un documento scaricato contiene "ignora le istruzioni e fai X").
  - Azioni non autorizzate (l'agente invia email che non doveva inviare).
  - Supply chain di tool: anche tool "ufficiali" possono avere vulnerabilità.
  - "Token DoS": un agente in loop può consumare enormi quantità di token (= costi).
- **Implicazioni per il design**:
  - Sempre una **conferma umana** per azioni ad alto impatto.
  - Gestione dei **permessi**: l'agente dovrebbe avere il minimo accesso necessario.
  - **Logging** di tutte le azioni per audit.
  - Fa parte delle OWASP Top 10 per LLM applications.

## 7.6 Orchestrazione di Agenti

### Perché un solo agente non basta sempre
- Task complessi richiedono **competenze diverse**: ricerca, analisi, scrittura, esecuzione codice.
- Un singolo agente con troppi tool e troppe responsabilità diventa **meno efficace** (contesto troppo diluito).
- Soluzione: **dividere il lavoro** tra agenti specializzati, coordinati da un orchestratore.

### Pattern 1: Orchestratore → Singolo Agente
```
┌───────────────┐         ┌──────────────┐
│ Orchestratore │────────►│   Agente     │
│  (main agent) │◄────────│ Specializzato│
└───────────────┘         └──────────────┘
```
- L'orchestratore delega un sub-task specifico a un agente specializzato e attende il risultato.
- **Quando usarlo**: task con sotto-compiti ben definiti e sequenziali.

### Pattern 2: Orchestratore → Più Agenti Isolati (Fan-out)
```
                          ┌──────────────┐
                     ┌───►│  Agente A    │───┐
┌───────────────┐    │    └──────────────┘   │    ┌───────────────┐
│ Orchestratore │────┤    ┌──────────────┐   ├───►│ Orchestratore │
│  (main agent) │    ├───►│  Agente B    │───┤    │  (sintetizza) │
│               │    │    └──────────────┘   │    └───────────────┘
│               │    │    ┌──────────────┐   │
│               │    └───►│  Agente C    │───┘
└───────────────┘         └──────────────┘
```
- Ogni agente lavora **indipendentemente**. L'orchestratore raccoglie e sintetizza.
- **Quando usarlo**: task scomponibili in sotto-compiti indipendenti, parallelizzabili.

### Pattern 3: Agent Swarm (con comunicazione inter-agente)
```
                          ┌──────────────┐
                     ┌───►│  Agente A    │◄──┐
┌───────────────┐    │    └──────┬───────┘   │
│ Orchestratore │────┤           │           │
│  (main agent) │    │    ┌──────▼───────┐   │
│               │    ├───►│  Agente B    │───┘
│               │    │    └──────┬───────┘
│               │    │           │
│               │    │    ┌──────▼───────┐
│               │    └───►│  Agente C    │
└───────────────┘         └──────────────┘
```
- I sotto-agenti possono **comunicare tra loro** prima di restituire all'orchestratore.
- **Esempio**: un agente "scrittore" produce una bozza, un agente "critico" la rivede, lo "scrittore" incorpora le modifiche.
- **Quando usarlo**: task che richiedono collaborazione, revisione incrociata, o negoziazione.

### Come scegliere il pattern giusto
- Criteri: complessità task, tempo, rischio, bisogno di parallelismo, costo.
- **Regola pratica**: partire semplice (singolo agente), crescere solo quando hai metriche e logging che dimostrano che serve più complessità.
- Più agenti = più chiamate LLM = più costi e latenza + debugging molto più complesso.

## 7.7 🔗 Concetto ponte: Memory negli Agenti
- La "memoria" di un agente **non è magia**: è **stato persistente** salvato in un database, oppure riassunti + retrieval inseriti nel contesto.
- **Tipi**:
  - **Short-term**: la conversazione corrente (il contesto).
  - **Long-term**: informazioni salvate tra sessioni diverse (database, vector store).
- **Implicazioni**: memoria senza governance = rischio privacy (dati utente persistenti) + drift (il sistema "ricorda" informazioni obsolete o errate).

## 7.8 Skills: competenze pacchettizzate

### Cosa sono
- **Pacchetti riusabili di istruzioni, template, policy, esempi e test** che danno a un agente competenze specifiche e ripetibili.
- Non sono tool (che sono azioni esecutive) — sono **conoscenza procedurale**: "come fare bene una certa cosa".

### Come funzionano
- Tipicamente un file (es. SKILL.md) che contiene:
  - Istruzioni dettagliate per eseguire un tipo specifico di compito.
  - Template e formati da seguire.
  - Best practice ed errori comuni da evitare.
  - Esempi di output di alta qualità.
- L'agente **legge la skill** prima di eseguire il compito, come un professionista che consulta un manuale operativo.

### Esempi concreti
- **Skill "crea presentazione PPTX"**: istruzioni su come strutturare le slide, formattare il testo, gestire layout e immagini.
- **Skill "crea documento Word"**: come generare un .docx professionale con TOC, header, stili.
- **Skill "frontend design"**: principi di design, come evitare l'estetica "generica AI", librerie disponibili.

### Skill lifecycle
- **Spec** → **Esempi** → **Test** → **Deploy** → **Monitor** → **Iterazione**
- **Concetto chiave**: una skill senza valutazione (eval) è una demo, non un asset di produzione. Serve testare che la skill produca output consistenti e di qualità.

### Perché sono importanti per MemorAIz
- Permettono di **standardizzare la qualità** degli output e ridurre la variabilità tra persone e progetti.
- Sono **riutilizzabili e migliorabili** nel tempo.
- Per i clienti: potete creare skill personalizzate che garantiscono output consistenti con il loro brand.

## 7.9 🔗 Concetto ponte: Observability (monitorare gli agenti)
- Non basta costruire un agente: bisogna poterlo **monitorare** in produzione.
- **Cosa loggare**:
  - Prompt e risposte (per debug).
  - Tool chiamati e loro output.
  - Costi (token consumati per task).
  - Errori e fallimenti.
- **Tracing**: tracciare la catena decisionale dell'agente (quale tool ha chiamato, perché, cosa ha ottenuto). Non "credere" alla spiegazione del modello — verificare la sequenza di azioni.
- **KPI suggeriti**: tasso di fallback/errore, precisione del retrieval, tempo medio per task, costo per task, soddisfazione utente.

---

# BLOCCO 8 — CHECKLIST OPERATIVA FINALE (~10 min)

## 8.1 Decision tree: che approccio usare?
```
La task richiede azioni esterne o integrazioni?
├── Sì → AGENTE (con tools appropriati)
│         La task è scomponibile in sotto-compiti?
│         ├── Sì → Orchestrazione multi-agente
│         └── No → Singolo agente
└── No → Solo LLM
         Servono dati aziendali o fonti specifiche?
         ├── Sì → RAG (retrieval + generazione)
         └── No → Prompt diretto
                  Task complessa multi-step?
                  ├── Sì → Reasoning model
                  └── No → Modello standard
                           Serve creatività?
                           ├── Sì → Temperatura alta + few-shot
                           └── No → Temperatura bassa + vincoli stretti
```

## 8.2 Regole d'oro per UX/Comms
1. **Mai assumere verità senza fonte**: chiedi citazioni o fornisci il testo sorgente.
2. **Separare sempre**: obiettivo / vincoli / fonti / output atteso.
3. **Preferire "bozze" + revisione umana** per qualsiasi contenuto pubblico o rivolto ai clienti.
4. **Evitare di inserire PII** o dati cliente non necessari nel contesto (principio di minimizzazione dei dati).
5. **Iterare**: non accontentatevi della prima risposta. Perfezionate il prompt.
6. **Verificare**: specialmente fatti, numeri, citazioni, link.
7. **Sperimentare**: provate diversi modelli, approcci, temperature. Non c'è una formula magica.
8. **Usare i tool disponibili**: Figma Make, Claude con computer use, generazione di file — sono lì per accelerarvi.

## 8.3 Prompt Template Standard Aziendale (da incollare e riusare)
```
## SCOPO
[Cosa deve fare il modello — 1-2 righe]

## AUDIENCE E TONO
[Chi leggerà l'output, che tono usare]

## VINCOLI
- Lingua: [...]
- Lunghezza: [...]
- Formato: [...]
- Cosa NON fare: [...]

## FONTI / CONTESTO
[Incollare qui i testi di riferimento, separati chiaramente]

## OUTPUT ATTESO
[Esempio concreto o descrizione precisa del formato desiderato]

## CHECKLIST QUALITÀ
- [ ] [Criterio 1]
- [ ] [Criterio 2]
- [ ] [Criterio 3]
```

---

# APPENDICE

## A) Glossario rapido

| Termine | Significato |
|---|---|
| **Token** | Frammento di testo (parola o parte di parola) — unità base degli LLM |
| **Context window** | Quantità massima di testo che un LLM può elaborare in una volta |
| **System prompt** | Istruzioni di base date al modello prima della conversazione |
| **Few-shot** | Dare al modello esempi concreti di input/output desiderati |
| **Fine-tuning** | Ri-addestrare un modello su dati specifici per un compito |
| **Embedding** | Rappresentazione numerica di un testo in uno spazio multidimensionale |
| **Chunk** | Frammento di documento usato per il retrieval in RAG |
| **RAG** | Retrieval-Augmented Generation — dare al modello documenti rilevanti |
| **Hallucination** | Quando il modello genera informazioni false ma plausibili |
| **Grounding** | Ancorare le risposte del modello a fonti verificabili |
| **Tool calling** | Capacità dell'LLM di invocare funzioni/API esterne |
| **MCP** | Model Context Protocol — standard per connettere LLM a servizi esterni |
| **Agent** | LLM + loop di ragionamento + capacità di usare tool |
| **Orchestratore** | Agente principale che coordina sotto-agenti specializzati |
| **Skill** | Pacchetto di istruzioni che dà a un agente competenze specifiche |
| **Eval** | Processo di valutazione sistematica delle performance di un modello/skill |
| **RLHF** | Reinforcement Learning from Human Feedback |
| **Temperatura** | Parametro che controlla la "creatività" dell'output |
| **Top-p** | Parametro di sampling che limita i token considerati per probabilità cumulativa |
| **Inference** | Il momento in cui il modello genera una risposta (vs training) |
| **Latenza** | Tempo che il modello impiega per rispondere |
| **Guardrails** | Regole e filtri per limitare output indesiderati o pericolosi |
| **Prompt injection** | Tentativo di manipolare un LLM tramite istruzioni nascoste nell'input |
| **Reranker** | Modello che ri-ordina i risultati del retrieval per rilevanza |

## B) 3 mini-demo ad alto impatto (suggerite)
1. **Prompting**: da vago a strutturato (stesso task, confrontare 3 output).
2. **RAG**: domanda su documento interno → senza RAG il modello inventa / con RAG cita le fonti.
3. **Agente**: "crea bozza post + cerca dati di mercato + genera checklist di revisione" — mostra il tool-use in azione, le conferme, e il loop.

## C) Limiti attuali da conoscere (per vendere e usare AI onestamente)
- **Allucinazioni**: i modelli possono inventare fatti con assoluta sicurezza.
- **Conoscenza non aggiornata**: senza RAG o web search, il modello sa solo ciò che era nel training data.
- **Nessuna comprensione causale vera**: i modelli trovano correlazioni, non capiscono cause ed effetti come gli umani.
- **Sensibilità al prompt**: piccoli cambiamenti nel prompt possono dare risultati molto diversi.
- **Privacy e sicurezza**: attenzione a cosa si mette nel contesto (dati sensibili, PII).
- **Bias**: i modelli ereditano i bias presenti nei dati di training.
- **Costi**: modelli più potenti costano di più. Ogni token ha un costo. Il design del sistema influenza direttamente i costi.
