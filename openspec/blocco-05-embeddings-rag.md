# Blocco 5 — Embeddings & RAG (~35 min)

## Obiettivo del blocco
Far comprendere ai partecipanti cosa sono gli embeddings (rappresentazioni numeriche del testo nello spazio), come funziona la ricerca semantica, e come la RAG (Retrieval-Augmented Generation) risolve il problema della conoscenza limitata degli LLM — ancorandoli a documenti verificabili. Il blocco costruisce direttamente sul concetto di allucinazioni (Blocco 3) e di context engineering (Blocco 4), mostrando la soluzione pratica.

---

## Slide previste: 13

### Slide 5.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ BLOCCO 5"
  - Heading grande: "Embeddings & RAG"
  - Sottotitolo: "Come dare memoria ai modelli"
  - Sotto il sottotitolo, piccola nota: "~35 minuti — dalla rappresentazione del significato alla ricerca intelligente"
- **Stellina**: `astronauta.png` — in basso a destra (tema: esplorazione di spazi nuovi, embeddings nello spazio)
- **Animazioni**: Auto-reveal elementi in sequenza all'ingresso — ★☆☆
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Siamo al blocco 5 — uno dei più pratici e rilevanti per il lavoro di MemorAIz. Finora abbiamo visto come funzionano gli LLM e come strutturare il contesto. Ma c'è un problema: i modelli non conoscono i vostri documenti interni, i dati dei clienti, le informazioni aggiornate. Come si risolve? Con una tecnica chiamata RAG — e per capirla, dobbiamo prima capire cosa sono gli embeddings."

---

### Slide 5.1 — Cosa sono gli embeddings
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ RAPPRESENTAZIONE"
  - Heading: "Trasformare parole in numeri"
  - Sotto-heading: "Gli embedding: una mappa del significato"
  - Layout a due colonne:
    - **Colonna sinistra — Il concetto**:
      - "Un embedding è una **lista di numeri** (un vettore) che rappresenta il significato di un testo¹"
      - "Centinaia o migliaia di dimensioni (es. 1536 per OpenAI, 3072 per Google)²"
      - "Ogni dimensione cattura un aspetto del significato"
    - **Colonna destra — L'analogia visiva**:
      - Illustrazione semplificata: una mappa 2D con punti-parola raggruppati
      - Cluster "animali" (gatto, cane, leone vicini), cluster "veicoli" (auto, treno, aereo vicini)
      - Le distanze tra punti rappresentano la similarità semantica
  - Box analogia in basso: "Come una mappa dove le parole formano quartieri: nel quartiere 'animali' trovate gatto e cane vicini, lontani dal quartiere 'veicoli'."
- **Stellina**: `lampadina.png` — piccola, accanto all'analogia (insight fondamentale)
- **Animazioni**:
  - Click 1: heading + colonna sinistra
  - Click 2: mappa 2D con punti-parola che appaiono e si raggruppano in cluster
  - Click 3: box analogia
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Google, 2025` — Definizione embedding come rappresentazione vettoriale densa
  - `² OpenAI / Google, 2025` — Dimensioni: text-embedding-3-small = 1536, gemini-embedding-001 = 3072
- **Ricerca web**: ✅ Verificato — Dimensioni confermate. OpenAI text-embedding-3-small 1536, text-embedding-3-large 3072. Google gemini-embedding-001 3072 (default). Cohere Embed v4 1536 default. Tutti supportano MRL (Matryoshka Representation Learning).
- **Note presentatore**: "Immaginate di dover spiegare a un computer il significato di una parola. Non potete usare altre parole — il computer non le capisce. Allora usate numeri: una lista di 1536 numeri che, insieme, descrivono il significato. Questa lista si chiama embedding. La cosa magica è che parole con significato simile hanno numeri simili. Se mettete tutti questi vettori su una mappa, vedete che 'gatto' e 'cane' stanno vicini, lontani da 'aereo' e 'treno'. È una mappa del significato."

---

### Slide 5.2 — Dagli LLM agli embedding (NUOVA)
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ CONNESSIONE"
  - Heading: "Dagli LLM agli embedding"
  - Sotto-heading: "Gli embedding non sono separati dai modelli — ne sono il cuore"
  - Layout: diagramma verticale a 4 blocchi impilati con frecce ↓:
    1. **Token** — "La parola viene spezzata in token (come visto nel Blocco 3)"
    2. **Embedding iniziale** — "Ogni token diventa un vettore grezzo — una posizione iniziale nello spazio¹"
    3. **Layer Transformer (×N)** — "Ad ogni layer, l'attenzione aggiorna il vettore guardando il contesto. Il vettore si muove nello spazio, avvicinandosi al significato contestuale²" (blocco evidenziato gold)
    4. **Embedding finale** — "L'output dell'ultimo layer è un embedding raffinato, ricco di contesto" (blocco evidenziato gold)
  - Box insight: "Un modello di embedding dedicato è un Transformer addestrato apposta per produrre vettori ottimali per la ricerca semantica — è un 'cugino specializzato' degli LLM"
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2-5: reveal sequenziale dei 4 blocchi + frecce + insight box
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Dremio, 2025` — How LLMs Work: Tokens, Embeddings, and Transformers
  - `² Stack Overflow Blog, 2023` — Transformer layers progressively enrich token embeddings
- **Ricerca web**: ✅ Verificato — Neptune.ai, Dremio, Machine Learning Mastery confermano che gli embedding sono le rappresentazioni interne dei Transformer. Ogni layer aggiorna il vettore tramite attenzione, costruendo rappresentazioni progressivamente più astratte.
- **Note presentatore**: "Prima di andare avanti con l'aritmetica vettoriale, fermiamoci un momento. Gli embedding non sono una tecnologia separata dagli LLM — sono esattamente ciò che un LLM fa internamente. Ricordate i Transformer dal Blocco 3? Ogni token entra come vettore grezzo e, layer dopo layer, il meccanismo di attenzione sposta quel vettore nello spazio, avvicinandolo al suo significato nel contesto. L'output dell'ultimo layer è un embedding ricco e raffinato. I modelli di embedding dedicati — quelli che usiamo per la ricerca semantica — sono semplicemente dei Transformer addestrati specificamente per produrre vettori ottimali per confrontare testi. Sono cugini degli LLM."

---

### Slide 5.3 — Aritmetica del significato (analogie vettoriali) [ex 5.2, RIDISEGNATA]
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ GEOMETRIA"
  - Heading: "Le direzioni catturano relazioni"
  - Sotto-heading: "L'aritmetica del significato"
  - **Animazione centrale** — spazio 2D con punti-parola e vettori:
    - Stato 1: quattro punti appaiono nello spazio: "re", "uomo", "donna", "regina"
    - Stato 2: una freccia (vettore) da "uomo" a "donna" appare, etichettata "direzione di genere"
    - Stato 3: la stessa freccia viene applicata partendo da "re" — la punta arriva vicino a "regina". L'operazione `re - uomo + donna ≈ regina` appare sopra
    - Stato 4: secondo esempio: "Parigi", "Francia", "Italia", "Roma" con la stessa logica → `Parigi - Francia + Italia ≈ Roma`
  - Box caveat in basso (⚠️): "Questa illustrazione viene dagli embedding statici (word2vec, 2013). Il principio è reale — le direzioni nello spazio catturano relazioni semantiche — ma non è una formula esatta.¹"
- **Stellina**: Nessuna (l'animazione è il focus)
- **Animazioni**:
  - Click 1: punti "re", "uomo", "donna", "regina" appaiono nello spazio 2D
  - Click 2: freccia "direzione di genere" da "uomo" a "donna" si disegna animata
  - Click 3: la freccia si copia e si applica da "re", arrivando vicino a "regina". Formula appare sopra
  - Click 4: secondo esempio (Parigi/Francia/Italia/Roma) con la stessa meccanica
  - Click 5: box caveat con warning
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ Mikolov et al., 2013 / critiche successive` — L'aritmetica vettoriale funziona come illustrazione ma non è una legge universale. Senza escludere i termini di input dalla ricerca, il risultato più vicino a "re - uomo + donna" è spesso "re" stesso.
- **Ricerca web**: ✅ Verificato — L'analogia word2vec è pedagogicamente valida come intuizione. Critiche fondate: senza escludere i termini input il nearest neighbor è "king" stesso (Mc Cheng, 2023); le analogie maschio/femmina funzionano insolitamente bene come outlier (Netherlands eScience Center); nessuna risposta univoca (Plotly). Il principio geometrico (direzioni = relazioni) resta valido.
- **Note presentatore**: "Ecco la cosa sorprendente degli embedding. Se prendete il vettore di 're' e ci sottraete 'uomo' e ci aggiungete 'donna', ottenete qualcosa molto vicino a 'regina'. Perché? Perché la direzione da 'uomo' a 'donna' nello spazio cattura la relazione semantica di genere. E se la applicate a 're', cambia il genere → 'regina'. Lo stesso funziona per le capitali: Parigi meno Francia più Italia dà Roma. Attenzione: questa è un'illustrazione bellissima, non una formula esatta. Con embedding moderni l'aritmetica non sempre funziona così pulita, ma il principio — le direzioni nello spazio catturano relazioni — è assolutamente reale."

---

### Slide 5.4 — Tipi di embedding [ex 5.3]
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ TIPOLOGIE"
  - Heading: "Non tutti gli embedding sono uguali"
  - Sotto-heading: "Tre generazioni di rappresentazioni"
  - Layout a 3 blocchi orizzontali, come una timeline evolutiva:
    - **Blocco 1 — Statici (word2vec, GloVe)**:
      - Icona: un punto fisso
      - "Un vettore fisso per ogni parola"
      - "'banco' ha lo stesso vettore sia in 'banco di scuola' che in 'banco di pesci'¹"
      - Etichetta: "2013-2017"
    - **Blocco 2 — Contestuali (Transformer interni)**:
      - Icona: un punto che cambia colore
      - "Il vettore dipende dal contesto"
      - "'banco' ha vettori diversi nelle due frasi"
      - Etichetta: "2018-oggi, interni ai modelli"
    - **Blocco 3 — Di documento/frase (per RAG)**:
      - Icona: un blocco di testo → un vettore
      - "Un intero paragrafo diventa un unico vettore"
      - "Usati per la ricerca semantica e la RAG²"
      - Etichetta: "2020-oggi, il tipo che ci interessa"
  - Freccia in basso che collega i 3 blocchi: "Evoluzione: da parole singole → a contesto → a documenti interi"
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: blocco 1 (statici) appare
  - Click 2: blocco 2 (contestuali) appare
  - Click 3: blocco 3 (documento/frase) appare, evidenziato come "il tipo che ci interessa"
  - Click 4: freccia evolutiva in basso
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Mikolov et al., 2013` — Word2vec: embedding statici, un vettore per parola indipendente dal contesto
  - `² OpenAI / Cohere / Google, 2025` — Modelli embedding moderni producono vettori di frase/documento per ricerca semantica
- **Ricerca web**: ✅ Verificato — La distinzione statici/contestuali/documento è standard nella letteratura. Word2vec (2013), BERT contestuali (2018), sentence-transformers e modelli dedicati (2020+). Tutti i provider principali (OpenAI, Cohere, Google) offrono modelli di document/sentence embedding.
- **Note presentatore**: "Tre generazioni di embedding. I primi, come word2vec del 2013, davano un vettore fisso a ogni parola — 'banco' aveva lo stesso vettore sia per il banco di scuola che per il banco di pesci. Problema ovvio. Poi sono arrivati gli embedding contestuali, quelli interni ai Transformer: il vettore cambia in base al contesto. Ma quelli che ci interessano per la RAG sono la terza generazione: modelli che prendono un intero paragrafo e lo trasformano in un unico vettore. È così che possiamo 'cercare per significato' nei documenti."

---

### Slide 5.5 — Visualizzazione degli embedding [ex 5.4]
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ VISUALIZZAZIONE"
  - Heading: "Vedere l'invisibile"
  - Sotto-heading: "Come si esplorano spazi a 1536 dimensioni"
  - Layout:
    - **Area principale**: screenshot/mockup dell'Embedding Projector di TensorFlow (projector.tensorflow.org) che mostra parole come punti nello spazio 3D con cluster visibili¹
    - **A destra**, due bullet:
      - "Gli embedding vivono in spazi con centinaia di dimensioni — impossibili da visualizzare direttamente"
      - "Tecniche come t-SNE e UMAP li proiettano in 2D o 3D, preservando le relazioni di vicinanza²"
    - **Sotto**, box:
      - "⚠️ Attenzione: queste proiezioni sono approssimazioni. Le distanze tra cluster non sempre riflettono le distanze reali nello spazio originale."
  - Box demo in basso: "🔗 Demo live: projector.tensorflow.org — provate a cercare una parola e vedrete i suoi 'vicini' nello spazio"
- **Stellina**: Nessuna (lo screenshot è il focus)
- **Animazioni**:
  - Click 1: heading + screenshot/mockup
  - Click 2: bullet a destra
  - Click 3: box warning + box demo
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Google, 2016` — TensorFlow Embedding Projector: strumento open source per visualizzare embedding ad alta dimensionalità
  - `² van der Maaten & Hinton, 2008 / McInnes et al., 2018` — t-SNE e UMAP come tecniche standard di riduzione dimensionale
- **Ricerca web**: ✅ Verificato — TensorFlow Embedding Projector ancora online e funzionante. Supporta PCA, t-SNE, UMAP. Pre-caricato con word2vec 10K parole. Nomic Atlas è un'alternativa più moderna per dataset reali. t-SNE preserva solo struttura locale, UMAP anche globale (più veloce).
- **Note presentatore**: "Come si fa a vedere uno spazio con 1536 dimensioni? Ovviamente non si può direttamente. Ma ci sono tecniche matematiche — t-SNE e UMAP — che proiettano questi spazi in 2D o 3D, cercando di mantenere le relazioni di vicinanza. Il risultato sono mappe come questa, dove si vedono chiaramente i cluster di concetti simili. Un avvertimento: queste mappe sono approssimazioni utili, non fotografie perfette dello spazio reale. Se volete provare, projector.tensorflow.org vi permette di esplorare gli embedding interattivamente nel browser."

---

### Slide 5.6 — Il problema che RAG risolve [ex 5.5]
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ IL PROBLEMA"
  - Heading: "Perché gli LLM non bastano da soli"
  - Sotto-heading: "Tre limiti fondamentali"
  - 3 blocchi verticali con icone e gold border:
    - **① Conoscenza cristallizzata**: "Il modello sa solo ciò che ha letto durante il training. Niente di dopo, niente di interno alla vostra azienda."
    - **② Finestra di contesto limitata**: "Non potete incollare migliaia di documenti nel prompt. Anche con 200K token, serve selezionare."
    - **③ Allucinazioni**: "Senza documenti di riferimento, il modello potrebbe inventare (ricordate il Blocco 3).¹"
  - Box ponte in basso (gold border): "Serve un modo per dare al modello le informazioni giuste, al momento giusto, da fonti verificabili. → Questo è RAG."
- **Stellina**: `dubbioso:pensieroso.png` — piccola, accanto al titolo (tema: limiti, problemi)
- **Animazioni**:
  - Click 1: heading
  - Click 2: blocco ①
  - Click 3: blocco ②
  - Click 4: blocco ③
  - Click 5: box ponte
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Rimando interno` — Riferimento al Blocco 3, slide 3.10-3.11 (allucinazioni)
- **Ricerca web**: Non necessaria (concetti consolidati, già verificati nei blocchi precedenti)
- **Note presentatore**: "Tre problemi. Primo: il modello è stato addestrato mesi o anni fa — non sa cosa è successo ieri, non conosce i vostri documenti interni, i brief dei clienti, le linee guida del brand. Secondo: anche se il contesto è grande, 200K token non bastano per contenere migliaia di documenti — e inserire troppo rumore peggiora le risposte (ricordate 'Lost in the Middle' dal blocco 4). Terzo: senza riferimenti, il modello inventa. La soluzione? RAG — Retrieval-Augmented Generation."

---

### Slide 5.7 — RAG: il concetto [ex 5.6]
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ LA SOLUZIONE"
  - Heading: "RAG — Retrieval-Augmented Generation"
  - Sotto-heading: "Consultare gli appunti prima di rispondere"
  - Layout a 3 blocchi orizzontali collegati da frecce:
    - **R — Retrieve**: "Cerca nei tuoi documenti le informazioni rilevanti alla domanda, usando la ricerca semantica (embedding)"
    - **A — Augment**: "Inserisci i frammenti trovati nel contesto del modello come materiale di riferimento"
    - **G — Generate**: "Il modello genera la risposta basandosi sulla sua conoscenza + i documenti forniti"
  - Box analogia in basso (grande, evidenziato): "Come uno studente che, prima di rispondere a un esame, può consultare i suoi appunti. Non deve ricordare tutto a memoria — basta che sappia dove cercare e come usare ciò che trova.¹"
- **Stellina**: `conoscenza.png` — piccola, accanto all'analogia (tema: consultare la conoscenza)
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2: blocco R (Retrieve)
  - Click 3: freccia + blocco A (Augment)
  - Click 4: freccia + blocco G (Generate)
  - Click 5: box analogia
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Lewis et al., 2020` — RAG: paper originale "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Facebook AI Research)
- **Ricerca web**: ✅ Verificato — RAG paper originale di Lewis et al. (2020, Facebook AI Research). Il termine e il pattern sono ancora lo standard nel 2025-2026. L'evoluzione include Contextual Retrieval (Anthropic, 2024), GraphRAG (Microsoft, 2024), Agentic RAG (2025).
- **Note presentatore**: "RAG sta per Retrieval-Augmented Generation. L'idea è semplice: prima di far rispondere il modello, gli diamo i documenti giusti da consultare. Tre passi: Retrieve — cerchi nei documenti le parti rilevanti. Augment — le inserisci nel contesto. Generate — il modello risponde con quelle informazioni come riferimento. L'analogia perfetta: è come un esame open-book. Lo studente non deve ricordare tutto a memoria — deve sapere dove cercare e come usare ciò che trova. E le risposte saranno molto più accurate e verificabili."

---

### Slide 5.8 — La pipeline RAG in dettaglio (6 passi) [ex 5.7]
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ PIPELINE"
  - Heading: "Come funziona in pratica"
  - Sotto-heading: "I 6 passi della pipeline RAG"
  - **Animazione**: flusso orizzontale/serpentina con 6 blocchi collegati da frecce, che si costruisce step by step:
    - **① Ingest**: icona documento → "Raccogli e pulisci i documenti (PDF, pagine web, database)"
    - **② Chunking**: icona forbici → "Dividi in frammenti gestibili (400-512 token con overlap)¹"
    - **③ Embedding**: icona vettore → "Trasforma ogni chunk in un vettore numerico"
    - **④ Retrieval**: icona lente → "Domanda → vettore → trova i chunk più simili (nearest neighbor)²"
    - **⑤ Reranking**: icona ordinamento → "Ri-ordina per rilevanza con un modello specializzato (+33-40% accuratezza)³"
    - **⑥ Generation**: icona LLM → "LLM genera la risposta con citazioni alle fonti"
  - Box critico in basso (⚠️, gold border): "La qualità di RAG dipende dal retrieval. Documenti sbagliati in input → risposte sbagliate in output. Garbage in, garbage out."
- **Stellina**: Nessuna (diagramma è già denso)
- **Animazioni**:
  - Click 1: heading + blocco ① (Ingest) con icona e descrizione
  - Click 2: freccia + blocco ② (Chunking)
  - Click 3: freccia + blocco ③ (Embedding)
  - Click 4: freccia + blocco ④ (Retrieval)
  - Click 5: freccia + blocco ⑤ (Reranking)
  - Click 6: freccia + blocco ⑥ (Generation)
  - Click 7: box critico in basso
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ NVIDIA / Weaviate, 2024-2025` — Best practice chunking: 400-512 token con 10-20% overlap (RecursiveCharacterTextSplitter)
  - `² Weaviate / Neo4j, 2025` — Hybrid retrieval (vettoriale + keyword BM25) come default raccomandato per produzione
  - `³ Ailog RAG, 2025` — Cross-encoder reranking: +33-40% accuratezza per ~120ms di latenza aggiuntiva
- **Ricerca web**: ✅ Verificato — Chunking 400-512 token è il best practice corrente (NVIDIA benchmark, Firecrawl 2025). Hybrid retrieval (dense + BM25) è lo standard in produzione. Reranking con cross-encoder dà +33-40% accuratezza (studio Ailog). Cohere Rerank 4 Pro e mxbai-rerank-large-v2 sono i top model.
- **Note presentatore**: "Vediamo i sei passi nel dettaglio. Primo: raccogliere e pulire i documenti — PDF, pagine web, database interni. Secondo: il chunking — dividere i documenti in pezzi di 400-500 token con un po' di sovrapposizione, così non si perdono informazioni ai bordi. Terzo: ogni pezzo diventa un vettore numerico tramite un modello di embedding. Quarto: quando arriva una domanda, anche quella diventa un vettore, e si cercano i pezzi più simili — ricerca semantica. Quinto: un modello specializzato ri-ordina i risultati per rilevanza — questo passaggio da solo migliora l'accuratezza del 33-40%. Sesto: i migliori pezzi vanno nel contesto dell'LLM, che genera la risposta con citazioni. Il punto critico: tutto dipende dalla qualità del retrieval. Se recuperi i documenti sbagliati, anche il miglior modello darà risposte sbagliate."

---

### Slide 5.9 — Lost in the Middle [ex 5.8]
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ ATTENZIONE"
  - Heading: "Lost in the Middle"
  - Sotto-heading: "Dove metti i documenti nel contesto conta"
  - **Animazione**: visualizzazione di un contesto lungo come una barra orizzontale suddivisa in sezioni:
    - Stato 1: barra del contesto divisa in sezioni (inizio | ... centro ... | fine), tutta dello stesso colore
    - Stato 2: le sezioni di inizio e fine si illuminano (gold/alta opacità), le sezioni centrali si sfumano (bassa opacità). Sopra appare una curva a U
    - Stato 3: etichette appaiono: "Alta attenzione" su inizio e fine, "Bassa attenzione" al centro
    - Stato 4: regola pratica appare sotto: "Metti le informazioni più importanti all'inizio o alla fine del contesto"
  - Box dati: "L'effetto può ridurre le performance di oltre il 30% quando le informazioni chiave sono al centro del contesto¹"
  - Box collegamento: "Ecco perché il reranking è importante: non solo quali documenti, ma anche in che ordine li presenti al modello"
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: heading + barra contesto (tutta uguale)
  - Click 2: inizio e fine si illuminano, centro si sfuma, curva U appare
  - Click 3: etichette + regola pratica
  - Click 4: box dati + box collegamento
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Liu et al., 2023` — "Lost in the Middle: How Language Models Use Long Contexts" (Stanford/UW) — performance U-shaped, degradazione >30% al centro
- **Ricerca web**: ✅ Verificato — Paper di Liu et al. (2023, arXiv:2307.03172) ancora il riferimento principale. Performance U-shaped confermata. Causa strutturale: Rotary Position Embedding (RoPE) introduce decay per token centrali. Mitigazione: ordinare i documenti strategicamente dopo il reranking.
- **Note presentatore**: "Ricordate dal Blocco 4 il concetto di 'Lost in the Middle'? Ecco perché è particolarmente importante per la RAG. Quando inserite documenti nel contesto, il modello presta più attenzione a ciò che sta all'inizio e alla fine. Le informazioni al centro vengono 'perse'. L'effetto può ridurre le performance di oltre il 30%. Ecco perché l'ordine in cui presentate i documenti al modello conta — non è solo 'quali' documenti, ma 'dove' li mettete."

---

### Slide 5.10 — Innovazioni RAG 2024-2025 [ex 5.9]
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ FRONTIERA"
  - Heading: "RAG evolve velocemente"
  - Sotto-heading: "Le innovazioni più importanti"
  - 3 blocchi con gold border, layout verticale:
    - **Contextual Retrieval (Anthropic, 2024)**:
      - "Aggiunge contesto a ogni chunk prima dell'embedding: 'questo paragrafo parla di...'"
      - "Risultato: **-67% errori di retrieval**¹"
    - **GraphRAG (Microsoft, 2024)**:
      - "Costruisce un grafo di relazioni (entità, connessioni) sopra i documenti"
      - "Risponde a domande globali ('quali temi emergono dal corpus?') impossibili con RAG standard²"
    - **Agentic RAG (2025)**:
      - "Un agente AI pianifica più passaggi di ricerca, usa tool, verifica risultati intermedi"
      - "Per task complessi che richiedono ragionamento multi-step³"
  - Box nota in basso: "L'evoluzione va da 'cerca e rispondi' a 'ragiona, cerca, verifica, rispondi' — un pattern che vedremo nel Blocco 7 (Agenti)."
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: heading
  - Click 2: blocco Contextual Retrieval
  - Click 3: blocco GraphRAG
  - Click 4: blocco Agentic RAG
  - Click 5: box nota ponte
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Anthropic, 2024` — Contextual Retrieval: -35% errori con embedding contestuali, -67% combinando con hybrid search + reranking
  - `² Microsoft Research, 2024` — GraphRAG: knowledge graph automatico + community summaries per query globali
  - `³ arXiv survey, 2025` — Agentic RAG: agenti che pianificano retrieval multi-step con tool e verifica
- **Ricerca web**: ✅ Verificato — Contextual Retrieval (Anthropic, settembre 2024) riduce errori del 67% con la combinazione completa. GraphRAG (Microsoft, aprile 2024) open source su GitHub. Agentic RAG survey (arXiv, gennaio 2025) documenta il pattern emergente.
- **Note presentatore**: "La RAG non è ferma. Tre innovazioni importanti. Prima: Contextual Retrieval di Anthropic. L'idea è semplice ma potente — prima di fare l'embedding di un pezzo di documento, si aggiunge un breve contesto generato dall'LLM: 'questo paragrafo è parte del capitolo X e parla di Y'. Risultato: 67% in meno di errori nel retrieval. Seconda: GraphRAG di Microsoft. Invece di cercare solo per similarità, costruisce un grafo di relazioni tra concetti. Può rispondere a domande come 'quali temi emergono da tutti questi documenti?' — impossibile con RAG standard. Terza: Agentic RAG, dove un agente AI pianifica più passaggi di ricerca, verifica i risultati, e ragiona prima di rispondere. Vedremo questo pattern nel Blocco 7 sugli agenti."

---

### Slide 5.11 — Implicazioni per UX/Comms [ex 5.10]
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ PER VOI"
  - Heading: "Progettare con RAG in mente"
  - Sotto-heading: "Pattern UX per sistemi basati su retrieval"
  - 4 bullet con gold dots e icone:
    - 📎 **Mostrare le fonti** — Ogni risposta deve indicare da quali documenti proviene. Questo costruisce fiducia e permette audit.¹
    - 🔗 **"Apri passaggio originale"** — Permettere all'utente di leggere il contesto completo da cui è stata estratta l'informazione.
    - 📅 **Indicare la data** — Mostrare quando il documento fonte è stato aggiornato. Informazione vecchia = rischio.
    - 🤷 **"Non ho trovato informazioni"** — Se il retrieval non trova nulla di rilevante, il sistema deve dirlo chiaramente invece di inventare.
  - Box regola in basso (gold): "La trasparenza delle fonti è la differenza tra un chatbot che 'risponde' e un assistente di cui ci si fida."
- **Stellina**: `controllo.png` — piccola, in basso a destra (tema: verifica, audit, controllo qualità)
- **Animazioni**:
  - Click 1: heading
  - Click 2-5: reveal sequenziale dei 4 bullet
  - Click 6: box regola
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ Stanford Law, 2025` — Anche tool RAG in ambito legale (LexisNexis, Thomson Reuters) allucinano nel 17-33% dei casi. La trasparenza delle fonti è essenziale.
- **Ricerca web**: ✅ Verificato — Studio Stanford Law (2025): tool legal RAG allucinano 17-33% del tempo. Pattern UX di mostrare fonti e permettere audit è best practice consolidata. FACTUM framework (arXiv, 2025) propone pipeline di verifica citazioni.
- **Note presentatore**: "Quattro pattern UX che dovete conoscere quando progettate sistemi RAG. Uno: mostrare sempre le fonti. Ogni risposta deve dire 'ho trovato questo nel documento X'. Due: permettere all'utente di aprire il passaggio originale. Tre: mostrare la data — un documento di tre anni fa potrebbe non essere più valido. Quattro: se il sistema non trova nulla di rilevante, deve dirlo. 'Non ho trovato informazioni su questo argomento' è molto meglio di un'invenzione. Dato importante: anche i migliori tool RAG in ambito legale — come quelli di LexisNexis — allucinano nel 17-33% dei casi secondo Stanford. La trasparenza è essenziale."

---

### Slide 5.12 — Riepilogo del blocco [ex 5.11]
- **Tipo**: `SUMMARY`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ TAKEAWAY"
  - Heading grande: "Embeddings & RAG in 5 concetti"
  - 5 punti in layout compatto (colonna singola, più leggibile):
    - **① Embeddings** — Trasformano testo in numeri. Concetti simili → vettori vicini nello spazio.
    - **② Ricerca semantica** — Cercare per significato, non per parole chiave. La base di tutto il sistema RAG.
    - **③ RAG = Retrieve + Augment + Generate** — Dare al modello documenti verificabili prima di fargli rispondere. L'esame open-book.
    - **④ Pipeline in 6 passi** — Ingest → Chunk → Embed → Retrieve → Rerank → Generate. Ogni passo conta.
    - **⑤ Fonti e trasparenza** — Mostrare le fonti, permettere audit, dire "non lo so". La fiducia si costruisce con la verificabilità.
  - Box bridge in basso: "Nel prossimo blocco: i Reasoning Model — quando il modello 'pensa' prima di rispondere"
- **Stellina**: `conversione1.png` — piccola, in basso a destra (tema: trasformazione caos → ordine, strutturare informazioni — perfetto per RAG)
- **Animazioni**: Build rapido dei 5 punti + box bridge — ★☆☆
- **Citazioni previste**: Nessuna (riepilogo senza dati nuovi)
- **Note presentatore**: "Cinque concetti. Uno: gli embeddings trasformano testo in numeri, e concetti simili finiscono vicini nello spazio. Due: la ricerca semantica — cercare per significato, non per parole esatte. Tre: RAG è l'esame open-book — dai al modello i documenti giusti e lui risponde meglio. Quattro: la pipeline ha sei passi, e la qualità di ognuno conta — soprattutto il retrieval. Cinque: la fiducia si costruisce con la trasparenza — fonti visibili, passaggi verificabili, 'non lo so' quando serve. Nel prossimo blocco vedremo i reasoning model — quando il modello si ferma a pensare prima di rispondere."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 13 (5.0 → 5.12) |
| Animazioni ★☆☆ | 9 slide (titolo, embeddings intro, LLM→embedding, tipi, visualizzazione, problema, RAG concetto, UX, summary) |
| Animazioni ★★☆ | 2 slide (pipeline RAG 6 passi, Lost in the Middle) |
| Animazioni ★★★ | 1 slide (aritmetica vettoriale nello spazio 2D) |
| Stelline usate | `astronauta.png` (5.0), `lampadina.png` (5.1), `dubbioso:pensieroso.png` (5.5), `conoscenza.png` (5.6), `controllo.png` (5.10), `conversione1.png` (5.11) |
| Gradienti | Blue (5.0, 5.2, 5.4, 5.6, 5.8, 5.10), Default (5.1, 5.3, 5.5, 5.7, 5.9, 5.11) — alternanza |
| Ricerca web | Modelli embedding (dimensioni, MRL), word2vec analogie (critiche), t-SNE/UMAP, RAG pipeline (chunking, reranking), Lost in the Middle, innovazioni RAG 2024-2025, hallucination rates |

---

## Dipendenze e note

- **Prerequisiti**: I Blocchi 3 (allucinazioni) e 4 (context engineering, Lost in the Middle) sono prerequisiti. La slide 5.5 fa riferimento esplicito al Blocco 3, la slide 5.8 riprende "Lost in the Middle" dal Blocco 4.
- **Sequenza narrativa**: Le slide 5.1-5.4 (embeddings) costruiscono la base concettuale per le slide 5.5-5.10 (RAG). Non possono essere invertite.
- **Animazione "hero"**: L'unica animazione ★★★ è la 5.2 (aritmetica vettoriale). È il momento visivo più forte del blocco — deve rendere tangibile il concetto astratto di "direzioni nello spazio semantico".
- **Ponte dal Blocco 3**: La slide 3.11 anticipava RAG come difesa contro le allucinazioni. Questo blocco mantiene quella promessa.
- **Ponte verso il Blocco 7**: La slide 5.9 (Agentic RAG) anticipa il Blocco 7 (Agenti). La slide 5.11 collega al Blocco 6 (Reasoning Models).
- **Demo live suggerita**: Durante la presentazione della slide 5.4, il presentatore potrebbe aprire projector.tensorflow.org per una demo interattiva di 2-3 minuti.
- **Nota sullo stile**: Questo blocco è più "pratico" dei precedenti. Il tono deve trasmettere utilità immediata — "ecco come funzionano i sistemi che costruiamo/usiamo".
- **Dati aggiornati utilizzati**:
  - Dimensioni embedding: OpenAI 1536/3072, Google gemini-embedding-001 3072, Cohere Embed v4 1536
  - MRL (Matryoshka Representation Learning): standard 2025, tutti i provider principali
  - Chunking: 400-512 token con 10-20% overlap (NVIDIA, Weaviate, Firecrawl)
  - Reranking: +33-40% accuratezza (Ailog studio cross-encoder)
  - Lost in the Middle: >30% degradazione (Liu et al., 2023)
  - Contextual Retrieval: -67% errori retrieval (Anthropic, 2024)
  - GraphRAG: Microsoft Research, 2024
  - Legal RAG hallucinations: 17-33% (Stanford Law, 2025)
- **Nota su word2vec**: La slide 5.2 include esplicitamente il caveat che l'aritmetica vettoriale è un'illustrazione, non una formula esatta. Questo è importante per la credibilità della formazione — presentare un'intuizione valida senza oversimplificare.

---

## Animazioni — Dettagli tecnici

### Animazione ★★★: Aritmetica vettoriale (slide 5.2)

Questa animazione richiede il workflow mini-spec prima dell'implementazione.

**Descrizione visiva**: Spazio 2D con sfondo a griglia sottile. Quattro punti-parola posizionati in modo da rendere visivamente chiara l'operazione vettoriale. Le parole sono etichettate con font leggibile.

**Comportamento step-by-step**:
1. I quattro punti ("re", "uomo", "donna", "regina") appaiono con una transizione fade-in, ciascuno come cerchio colorato con etichetta
2. Una freccia (vettore) si disegna animata da "uomo" a "donna", con etichetta "direzione di genere" che appare lungo la freccia
3. La freccia viene duplicata (ghost/tratteggiata della stessa direzione e lunghezza) e si sposta partendo da "re". La punta arriva vicino a "regina". Il punto "regina" si illumina gold. La formula `re - uomo + donna ≈ regina` appare sopra con animazione typewriter
4. Tutto si resetta con fade, poi appare il secondo esempio con "Parigi", "Francia", "Italia", "Roma" e la stessa meccanica
5. Box caveat appare in basso con fade-in

**Elementi visivi**:
- Canvas/SVG con sfondo griglia tenue (colore `--slide-bg-blue` come base)
- Punti: cerchi di raggio ~20px, colori dalla palette MemorAIz (gold per re/regina, accent per uomo/donna)
- Frecce: linea con punta, spessore 2-3px, colore gold
- Freccia duplicata: tratteggiata, stessa direzione/lunghezza
- Font: mono o sans-serif per le etichette, body per la formula
- Container: max-height `min(50vh, 400px)`

**Vincoli tecnici**:
- Implementazione: SVG preferito a Canvas per questa animazione (pochi elementi, vettori definiti)
- Transizioni: 400ms per ogni step
- Cleanup: cancellare eventuali timer/animation quando si cambia slide
- Resize: ricalcolare posizioni relative al container

**Edge case**:
- Torna indietro: resettare allo stato del click precedente
- Cambio slide: fermare tutte le animazioni in corso
- Resize: le posizioni dei punti sono relative (%) al container

### Animazione ★★☆: Pipeline RAG (slide 5.7)

**Descrizione**: Flusso a 6 blocchi collegati da frecce, costruzione progressiva. Ogni blocco ha un'icona, un titolo e una breve descrizione. Il flusso può essere orizzontale (se c'è spazio) o a serpentina (2 righe × 3 blocchi).

**Implementazione**: CSS transitions + step reveal. Ogni click aggiunge un blocco con la freccia di connessione. I blocchi non ancora rivelati sono invisibili. Nessun canvas necessario — HTML/CSS puro con transizioni.

**Vincoli**: Nessun requestAnimationFrame necessario — solo CSS transitions.

### Animazione ★★☆: Lost in the Middle (slide 5.8)

**Descrizione**: Barra orizzontale che rappresenta il contesto, divisa in sezioni. Le sezioni centrali si sfumano mentre inizio e fine si illuminano. Una curva U appare sopra.

**Implementazione**: HTML/CSS con opacità controllate. La curva U può essere un SVG path semplice. Step reveal con CSS transitions.

**Vincoli**: Nessun canvas necessario — SVG per la curva U, CSS per le opacità delle sezioni.

---

## Fonti consultate

Tutte le fonti sono registrate nel file `references/sources.md` sotto le sezioni:
- "Modelli di embedding attuali"
- "Analogia word2vec — validità e critiche"
- "Strumenti di visualizzazione degli embedding"
- "t-SNE vs UMAP"
- "Sviluppi recenti embedding (2025-2026)"
- "RAG — Pipeline e best practice"
- "RAG — Reranking"
- "RAG — Vector databases"
- "RAG — Limitazioni e Lost in the Middle"
- "RAG — Innovazioni 2024-2025"
