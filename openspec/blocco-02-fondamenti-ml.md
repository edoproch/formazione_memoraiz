# Blocco 2 — Fondamenti ML "senza matematica" (~35 min)

## Obiettivo del blocco
Dare ai partecipanti le intuizioni fondamentali su come le macchine "imparano": i tre paradigmi di apprendimento (supervised, unsupervised, self-supervised), la struttura di una rete neurale, e il meccanismo di backpropagation. Tutto senza una singola formula matematica, usando analogie concrete.

Questo blocco costruisce le basi per capire il Blocco 3 (come funzionano gli LLM).

---

## Slide previste: 10

### Slide 2.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ BLOCCO 2"
  - Heading grande: "Come imparano le macchine"
  - Sottotitolo: "Fondamenti di Machine Learning — zero formule, solo intuizioni"
- **Stellina**: `conoscenza.png` — in basso a destra (tema apprendimento/studio)
- **Animazioni**: Auto-reveal elementi in sequenza all'ingresso — ★☆☆
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Ora entriamo nel 'come'. Non vi chiederò di fare calcoli — vi chiederò di capire il meccanismo. Pensatelo come capire come funziona un motore senza dover saper costruirne uno."

---

### Slide 2.1 — Supervised Learning
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ PARADIGMI"
  - Numero: ①
  - Heading: "Apprendimento supervisionato"
  - Sotto-heading: "Il modello impara da esempi corretti"
  - 3 bullet con gold dots:
    - **Il meccanismo** — Il modello riceve coppie (input → output corretto). Fa una previsione, viene confrontata con la risposta giusta, e si aggiusta.
    - **L'analogia** — Come un insegnante che corregge i compiti: sbaglio → correzione → miglioramento.
    - **Esempi concreti** — Classificazione email (spam / non spam), moderazione contenuti, analisi sentiment di recensioni, classificazione ticket di supporto.
  - Box in basso con keyword: "Servono dati etichettati → costosi da creare"
- **Stellina**: Nessuna
- **Animazioni**: Reveal sequenziale dei bullet al click — ★☆☆
- **Citazioni previste**: Nessuna (definizione standard di supervised learning, cultura generale ML)
- **Ricerca web**: ✅ Verificato — definizione standard confermata, esempi ancora rilevanti nel 2026.
- **Note presentatore**: "Questo è il paradigma più intuitivo: mostri al modello migliaia di email e per ognuna dici 'questa è spam, questa no'. Il modello impara il pattern. Il limite? Serve qualcuno che etichetti tutti quei dati, e costa."

---

### Slide 2.2 — Unsupervised Learning
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ PARADIGMI"
  - Numero: ②
  - Heading: "Apprendimento non supervisionato"
  - Sotto-heading: "Il modello trova struttura nei dati da solo"
  - 3 bullet con gold dots:
    - **Il meccanismo** — Il modello riceve dati senza etichette e deve trovare pattern, gruppi e strutture autonomamente.
    - **L'analogia** — Come dare a qualcuno un mazzo di carte sconosciute e chiedergli di organizzarle in gruppi sensati.
    - **Esempi concreti** — Segmentazione clienti per comportamento, clustering di temi in feedback, scoperta di anomalie (frodi, guasti).
  - Box in basso con keyword: "Non servono etichette → scala facilmente, ma meno controllabile"
- **Stellina**: Nessuna
- **Animazioni**: Reveal sequenziale dei bullet al click — ★☆☆
- **Citazioni previste**: Nessuna (definizione standard di unsupervised learning, cultura generale ML)
- **Note presentatore**: "Qui nessuno dice al modello cosa è giusto o sbagliato. Gli dai un milione di clienti e lui trova da solo che ci sono 5 tipi diversi di comportamento. Utile quando non sai nemmeno cosa cercare."

---

### Slide 2.3 — Self-Supervised Learning (concetto ponte)
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ CONCETTO PONTE"
  - Numero: ③
  - Heading: "Self-supervised learning"
  - Sotto-heading: "Il segreto dietro gli LLM"
  - Layout a due righe:
    - **Riga 1 — Il meccanismo**: "Il modello crea le proprie 'etichette' dal testo stesso. Prendi una frase, nascondi l'ultima parola: l'etichetta è la parola nascosta."
    - **Riga 2 — Il collegamento con gli LLM**: "È esattamente ciò che fanno gli LLM nel pre-training¹: predire il prossimo token². Nessun umano etichetta a mano — il segnale viene dai dati stessi."
  - Box highlight in basso: "Self-supervised = scala infinita. Internet intera come materiale di training."
- **Stellina**: `lampadina.png` — accanto al box highlight (insight fondamentale)
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2: riga meccanismo
  - Click 3: riga collegamento LLM
  - Click 4: box highlight
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Comet, 2025` — Pre-training pipeline degli LLM come task self-supervised
  - `² IBM, 2025` — Next-token prediction come meccanismo base degli LLM
- **Ricerca web**: ✅ Verificato — "self-supervised learning" è ancora il termine standard nel 2026 per il pre-training degli LLM. La terminologia non è cambiata.
- **Note presentatore**: "Questo è il trick geniale. Non serve pagare umani per etichettare miliardi di testi: il testo si etichetta da solo. Nascondi una parola → il modello la indovina → confronti → il modello migliora. Ripeti trilioni di volte e ottieni GPT-5 o Claude."

---

### Slide 2.4 — Overfitting vs Generalizzazione
- **Tipo**: `ANALOGY`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ CONCETTO PONTE"
  - Heading: "Imparare a memoria vs capire davvero"
  - Layout split a due colonne con contrasto visivo:
    - **Colonna sinistra — Overfitting** ❌:
      - Icona: libro aperto con catena/lucchetto
      - "Il modello memorizza i dati di training"
      - "Perfetto sugli esempi già visti"
      - "Fallisce su casi nuovi"
      - Analogia: "Studiare memorizzando le risposte dell'esame dell'anno scorso"
    - **Colonna destra — Generalizzazione** ✅:
      - Icona: bussola / mappa
      - "Il modello cattura pattern veri"
      - "Funziona anche su dati mai visti"
      - "L'obiettivo di ogni training"
      - Analogia: "Capire la materia e saper rispondere a domande nuove"
  - Box in basso: "Implicazione pratica: 'Ha risposto bene una volta' ≠ 'Funzionerà sempre'. Serve testare su casi diversi."
- **Stellina**: Nessuna (slide densa, contrasto visivo sufficiente)
- **Animazioni**:
  - Click 1: colonna Overfitting
  - Click 2: colonna Generalizzazione
  - Click 3: box implicazione pratica
  - Complessità: ★★☆
- **Citazioni previste**: Nessuna (concetti standard ML + analogie originali)
- **Note presentatore**: "Tutti noi abbiamo avuto compagni di classe che memorizzavano le risposte senza capire. Funziona finché le domande sono le stesse. Ma nella vita reale — e nell'AI — le domande cambiano sempre. Ecco perché una singola risposta corretta non è una garanzia."

---

### Slide 2.5 — Il neurone artificiale
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ RETI NEURALI"
  - Numero: ④
  - Heading: "Il neurone artificiale"
  - Sotto-heading: "L'unità base di ogni rete neurale"
  - Visualizzazione animata di un singolo neurone:
    - **A sinistra**: 3-4 frecce di input (etichettate "Input 1", "Input 2", "Input 3"), ciascuna con un indicatore di peso (spessore della freccia variabile)
    - **Al centro**: un cerchio che rappresenta il neurone (con operazione: somma pesata)
    - **A destra**: una freccia di output
  - Analogia in basso: "Come prendere una decisione: 'Porto l'ombrello?' → Guardo il cielo (peso: alto), guardo il meteo (peso: alto), guardo se ho fretta (peso: basso). Peso le informazioni e decido."
- **Stellina**: Nessuna (l'animazione è il focus)
- **Animazioni**:
  - Click 1: appaiono gli input (frecce a sinistra) con etichette
  - Click 2: appaiono i pesi (le frecce cambiano spessore, numeri piccoli appaiono)
  - Click 3: il neurone centrale si "attiva" (glow/pulse) — i segnali arrivano e vengono sommati
  - Click 4: l'output esce a destra, l'analogia dell'ombrello appare in basso
  - Complessità: ★★☆
- **Citazioni previste**: Nessuna (struttura base del neurone artificiale, cultura generale ML consolidata)
- **Note presentatore**: "Un singolo neurone è semplicissimo: prende degli input, li pesa (alcuni contano più di altri), li somma e produce un output. La magia non è nel singolo neurone — è in cosa succede quando ne metti insieme miliardi."

---

### Slide 2.6 — La rete neurale (strati)
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ RETI NEURALI"
  - Numero: ⑤
  - Heading: "Dalla singola unità alla rete"
  - Visualizzazione animata di una rete neurale a 4 strati:
    - **Input layer** (3-4 nodi) — etichetta: "Dati grezzi"
    - **Hidden layer 1** (5-6 nodi) — etichetta: "Pattern semplici"
    - **Hidden layer 2** (5-6 nodi) — etichetta: "Pattern complessi"
    - **Output layer** (2-3 nodi) — etichetta: "Risultato"
  - Connessioni visibili tra tutti i nodi degli strati adiacenti (linee sottili)
  - Analogia in basso: "Come una catena di montaggio: ogni stazione lavora il pezzo un po' di più"
  - Box in basso: "Più strati = più capacità di catturare complessità → ecco perché 'deep' learning"
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: input layer appare (nodi + etichetta)
  - Click 2: hidden layer 1 appare, con connessioni che si animano dall'input layer (linee che "crescono")
  - Click 3: hidden layer 2 appare con connessioni
  - Click 4: output layer appare con connessioni, poi l'analogia e il box sotto
  - Opzionale: un "segnale luminoso" che percorre la rete da sinistra a destra (forward pass visivo)
  - Complessità: ★★★
- **Citazioni previste**: Nessuna (struttura base di una rete neurale, cultura generale ML — i numeri specifici sono nella slide successiva)
- **Note presentatore**: "Ecco la rete. Ogni cerchio è un neurone come quello di prima. Ogni linea è una connessione con un peso. I dati entrano da sinistra, vengono trasformati strato dopo strato, e il risultato esce a destra. I modelli più recenti come GPT-5 o Claude hanno centinaia di strati e centinaia di miliardi di queste connessioni."

---

### Slide 2.7 — I pesi: il cuore dell'apprendimento
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ RETI NEURALI"
  - Numero: ⑥
  - Heading: "I pesi — il DNA del modello"
  - Rete neurale semplificata (3 strati, 3-4 nodi ciascuno) dove le connessioni hanno colori/spessori che indicano il peso:
    - **Stato 1 (iniziale)**: pesi casuali → connessioni tutte dello stesso spessore, colori neutri → il modello "spara a caso"
    - **Stato 2 (dopo training)**: pesi ottimizzati → alcune connessioni spesse e gold (importanti), altre sottili e grigie (poco importanti) → il modello ha imparato
  - Box dati in basso con numeri aggiornati al 2026:
    - "GPT-3 (2020): 175 miliardi di parametri¹"
    - "Llama 4 Maverick (2025): 400 miliardi totali, 17 miliardi attivi²"
    - "Llama 4 Behemoth (annunciato): ~2 trilioni di parametri²"
    - "'Parametri' = pesi da regolare. Più ce ne sono, più il modello è capace — ma anche più costoso."
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: rete con pesi casuali, etichetta "Prima del training — pesi casuali"
  - Click 2: transizione animata — i pesi cambiano spessore e colore, alcune connessioni diventano gold e spesse, altre grigie e sottili. Etichetta "Dopo il training — pesi ottimizzati"
  - Click 3: box dati con i numeri appaiono in basso
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ OpenAI / Wikipedia, 2020` — GPT-3: 175 miliardi di parametri
  - `² Meta AI Blog, 2025` — Llama 4 Maverick: 400B totali / 17B attivi (MoE, 128 esperti); Behemoth: ~2T
- **Ricerca web**: ✅ Verificato — GPT-3 = 175B confermato. Llama 4 Maverick = 400B totali / 17B attivi (architettura MoE con 128 esperti). Behemoth = ~2T (annunciato, non ancora rilasciato a febbraio 2026).
- **Note presentatore**: "All'inizio i pesi sono casuali — il modello non sa nulla. Durante l'addestramento, ogni peso viene aggiustato per migliorare le previsioni. Quando diciamo che Llama 4 ha 400 miliardi di parametri, stiamo dicendo che ha 400 miliardi di queste connessioni che sono state ottimizzate. E ora ci sono modelli annunciati con 2 trilioni — duemila miliardi — di parametri."

---

### Slide 2.8 — Backpropagation
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ COME IMPARA"
  - Numero: ⑦
  - Heading: "Backpropagation — come il modello si corregge"
  - Animazione step-by-step sulla stessa rete neurale delle slide precedenti:
    - **Step 1 — Forward pass**: un input entra, i segnali si propagano in avanti (sinistra → destra), ogni connessione si illumina in sequenza. Output: "Gatto" (previsione del modello).
    - **Step 2 — Confronto**: l'output viene confrontato con la risposta corretta ("Cane"). Appare un indicatore di errore rosso: "Errore: alto!"
    - **Step 3 — Backward pass**: l'errore si propaga all'indietro (destra → sinistra), le connessioni si illuminano in rosso/arancio in sequenza inversa.
    - **Step 4 — Aggiustamento**: i pesi cambiano leggermente (alcune connessioni cambiano spessore). Etichetta: "Pesi aggiustati per sbagliare meno"
    - **Step 5 (opzionale)**: ripetizione veloce — lo stesso ciclo si ripete 2-3 volte con l'errore che diminuisce progressivamente (barra errore che si abbassa).
  - Analogia in basso: "Come accordare una chitarra: suoni, senti che è stonata, giri la chiave. Ripeti. Ora immagina 400 miliardi di chiavi."
- **Stellina**: Nessuna (animazione complessa, zero rumore visivo)
- **Animazioni**:
  - 4-5 step controllati da click
  - Colori: forward pass in gold/verde, errore in rosso, backward pass in arancio/rosso, aggiustamento in gold
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ arXiv (NoProp), 2025` — Alternative in ricerca (NoProp, Forward-Forward) ma nessuna in produzione
  - ⚠️ La backpropagation in sé non richiede citazione (metodo standard dal 1986, cultura generale ML). Citiamo solo l'affermazione "ancora il metodo standard nel 2026" come dato verificato.
- **Ricerca web**: ✅ Verificato — la backpropagation è ancora il metodo standard nel 2026. Esistono alternative in ricerca (NoProp, Forward-Forward Algorithm di Hinton) ma nessuna è usata in produzione nei modelli frontier.
- **Note presentatore**: "Ecco come impara un modello. Forward pass: fa una previsione. Confronto: quanto ha sbagliato? Backward pass: ripercorre la rete al contrario per capire quali pesi hanno contribuito all'errore. Aggiustamento: cambia quei pesi un pochino. Ripete questo ciclo miliardi di volte. Dopo trilioni di iterazioni, i pesi sono calibrati per fare previsioni accurate. Questo è ancora il metodo standard nel 2026 — nessuna alternativa l'ha sostituito in produzione."

---

### Slide 2.9 — Concetto chiave del blocco
- **Tipo**: `SUMMARY`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ TAKEAWAY"
  - Heading grande: "Il modello non 'capisce'"
  - Sotto-heading: "Aggiusta pesi per minimizzare l'errore sugli esempi di training"
  - 3 bullet con gold dots — i tre takeaway del blocco:
    - **Self-supervised** — Gli LLM imparano prevedendo il prossimo token¹. Il testo di Internet si etichetta da solo → scala infinita.
    - **Più pesi = più capace** — Da 175 miliardi (GPT-3, 2020)² a 2 trilioni (Llama 4 Behemoth, 2025)³. Ma capace ≠ affidabile.
    - **L'addestramento è ottimizzazione, non comprensione** — Il modello minimizza errori statistici. Non "sa" nel senso umano del termine.
  - Box highlight in basso — frase chiave: "Ricordate la slide 0.3: probabilistico, non deterministico. Ora sapete il perché."
- **Stellina**: `lampadina.png` — piccola, accanto al box highlight
- **Animazioni**: Reveal sequenziale dei 3 takeaway + box finale — ★☆☆
- **Citazioni previste**:
  - `¹ IBM, 2025` — Next-token prediction come meccanismo base LLM
  - `² Wikipedia / OpenAI, 2020` — GPT-3: 175B parametri
  - `³ Meta AI Blog, 2025` — Llama 4 Behemoth: ~2T parametri
- **Note presentatore**: "Tre cose da portare a casa. Uno: il trick del self-supervised learning è ciò che ha permesso la scala degli LLM — usano Internet come libro di testo. Due: i numeri sono impressionanti ma più parametri non significano più verità. Tre: il modello ottimizza, non capisce. Ecco perché può scrivere testi brillanti e sbagliare un calcolo banale."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 10 |
| Animazioni ★☆☆ | 4 slide (titolo, supervised, unsupervised, summary) |
| Animazioni ★★☆ | 3 slide (self-supervised, overfitting/generalizzazione, neurone) |
| Animazioni ★★★ | 3 slide (rete neurale strati, pesi, backpropagation) |
| Stelline usate | `conoscenza.png` (2.0), `lampadina.png` (2.3, 2.9) |
| Gradienti | Peach (2.0, 2.2, 2.4, 2.6, 2.8), Default (2.1, 2.3, 2.5, 2.7, 2.9) — alternanza |
| Ricerca web | Self-supervised learning (terminologia 2026), parametri modelli attuali, backpropagation status |

---

## Dipendenze e note

- La slide 2.3 (self-supervised learning) è il concetto ponte più importante verso il Blocco 3 — il next-token prediction è un task self-supervised.
- Le slide 2.5–2.8 (neurone → rete → pesi → backprop) formano una sequenza narrativa: ogni slide costruisce sulla precedente. **Non possono essere riordinate.**
- I numeri sulla scala dei modelli (slide 2.7) si agganciano a informazioni aggiornate al 2026:
  - GPT-3: 175B parametri (2020) — dato storico confermato
  - Llama 4 Maverick: 400B totali / 17B attivi con architettura MoE a 128 esperti (aprile 2025)
  - Llama 4 Behemoth: ~2T parametri, annunciato ma non rilasciato (febbraio 2026)
  - Architettura MoE (Mixture of Experts): spiegata come "team di specialisti dove solo quelli rilevanti vengono coinvolti per ogni domanda"
- La backpropagation (slide 2.8) è l'animazione più complessa del blocco e una delle animazioni "hero" dell'intero deck — merita effort significativo.
- Il richiamo alla slide 0.3 nel summary (2.9) chiude il cerchio concettuale aperto nel Blocco 0.
- **Nota sui modelli MoE**: nella slide 2.7 si introduce il concetto di "parametri attivi vs totali" (17B attivi su 400B totali). Questo è nuovo rispetto all'outline originale ed è necessario per dare numeri onesti e aggiornati — dire solo "400 miliardi di parametri" sarebbe fuorviante senza spiegare che non sono tutti attivi contemporaneamente.

---

## Fonti consultate

- Definizioni supervised/unsupervised/self-supervised: terminologia standard confermata, nessun cambio nel 2026.
- Self-supervised learning come base del pre-training LLM: confermato come descrizione standard (IBM, Comet, Sebastian Raschka).
- Parametri modelli: Llama 4 (ai.meta.com), GPT-5/gpt-oss (openai.com), DeepSeek V3 (deepseek.ai).
- Backpropagation: ancora metodo standard. Alternative in ricerca (NoProp, Forward-Forward) non in produzione (arXiv 2025).
- Architettura MoE: trend dominante 2024-2026 (GPT-5, Llama 4, DeepSeek V3 tutti usano MoE).
- Costi training: $500M stimati per GPT-5 (Epoch AI), $5.6M dichiarati per DeepSeek V3 (Interconnects.ai).
