# Blocco 1 — Storia dell'AI + Mappa Concetti (~25 min)

## Obiettivo del blocco
Dare ai partecipanti un contesto storico essenziale (l'AI non è nata ieri) e costruire la mappa mentale fondamentale: AI ⊃ ML ⊃ DL ⊃ LLM. Introdurre la distinzione training vs inference, che sarà richiamata in ogni blocco successivo.

---

## Slide previste: 6

### Slide 1.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ BLOCCO 1"
  - Heading grande: "Una breve storia dell'AI"
  - Sottotitolo: "…e la mappa per orientarsi"
- **Stellina**: `bussola.png` — in basso a destra, piccola (orientamento, navigazione)
- **Animazioni**: Auto-reveal degli elementi in sequenza all'ingresso della slide — ★☆☆
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Prima di entrare nel 'come funziona', capiamo 'da dove viene'. Vi darà prospettiva su perché certi limiti esistono ancora oggi."

---

### Slide 1.1 — Timeline essenziale
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ STORIA"
  - Heading: "70 anni in un minuto"
  - Timeline verticale animata con 6 tappe:
    1. **1950s–60s** — Nascita dell'AI. Sistemi simbolici: regole scritte a mano. Il Perceptron di Rosenblatt¹ (1957).
    2. **1974–1987** — Primo AI Winter² (1974-80): i fondi si prosciugano dopo il Lighthill Report³. Revival con i sistemi esperti⁴ (1980-87), poi secondo inverno.
    3. **1990s–2000s** — Machine Learning statistico. Le macchine imparano dai dati. Deep Blue batte Kasparov⁵ (maggio 1997).
    4. **2012** — Svolta: AlexNet⁶ vince ImageNet. Il Deep Learning funziona su larga scala grazie alle GPU.
    5. **2017** — "Attention Is All You Need"⁷ (Vaswani et al.) — nasce il Transformer, fondamento di tutti gli LLM.
    6. **2020–oggi** — GPT-3⁸ (2020), ChatGPT⁹ (nov 2022), Claude¹⁰ (mar 2023), Gemini¹¹ (dic 2023). Esplosione consumer e enterprise.
  - La timeline è una linea verticale scura al centro. Ogni tappa ha un cerchio numerato sulla linea, con il testo alternato a sinistra e a destra.
- **Stellina**: Nessuna (slide densa, niente rumore visivo)
- **Animazioni**:
  - Le tappe appaiono una alla volta al click (dall'alto verso il basso)
  - Ogni tappa fa fade-in + slide laterale (da sinistra o da destra, alternato)
  - Complessità: ★★☆
- **Citazioni previste** (footnote in basso a destra):
  - `¹ Cornell Chronicle, 2019` — Perceptron di Rosenblatt (1957)
  - `² Wikipedia AI Winter` — Primo AI Winter 1974-1980
  - `³ Lighthill Report, 1973` — Taglio fondi UK
  - `⁴ Holloway, 2024` — Expert systems boom 1980-1987
  - `⁵ IBM / HISTORY.com` — Deep Blue vs Kasparov, maggio 1997
  - `⁶ IEEE Spectrum, 2024` — AlexNet, ImageNet 2012
  - `⁷ Vaswani et al., 2017` — Transformer paper (arXiv 1706.03762)
  - `⁸ OpenAI, 2020` — GPT-3
  - `⁹ OpenAI, 2022` — ChatGPT (30 novembre 2022)
  - `¹⁰ Anthropic, 2023` — Claude (marzo 2023)
  - `¹¹ Google DeepMind, 2023` — Gemini (6 dicembre 2023)
  - ⚠️ **Nota**: questa slide ha molte citazioni. Nel layout, raggrupparle in modo compatto (es. su 2-3 righe con numeri ravvicinati) per non occupare troppo spazio. Alternativa: usare un singolo footnote "Fonti: vedi references/sources.md" se diventa troppo denso.
- **Note presentatore**: "Non serve ricordare le date. Il messaggio è: ogni ondata ha spostato il confine tra 'cosa automatizziamo' e 'cosa resta umano'. Oggi siamo nella sesta ondata."

---

### Slide 1.2 — I cerchi concentrici: AI ⊃ ML ⊃ DL ⊃ LLM
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ LA MAPPA"
  - Numero: ①
  - Heading: "La matrioska dell'intelligenza artificiale"
  - Visualizzazione a cerchi concentrici (dal più grande al più piccolo):
    - **AI** (cerchio esterno, più chiaro) — "Qualsiasi sistema che esegue compiti che richiederebbero intelligenza umana"
    - **ML** — "Il sistema impara dai dati invece di seguire regole esplicite"
    - **DL** — "Reti neurali con molti strati, capaci di rappresentazioni sempre più astratte"
    - **LLM** (cerchio interno, più intenso) — "Reti neurali molto grandi, addestrate su enormi quantità di testo"
  - Ogni cerchio si anima con un effetto zoom-in progressivo
  - Quando un cerchio è attivo, si illumina e mostra la definizione in un tooltip/box laterale
- **Stellina**: Nessuna (l'animazione è il centro dell'attenzione)
- **Animazioni**:
  - Stato iniziale: i 4 cerchi visibili ma "spenti" (opacità bassa, senza etichette)
  - Click 1: cerchio AI si illumina (bordo oro, opacità piena), compare definizione a destra
  - Click 2: zoom leggero verso il centro, cerchio ML si illumina, definizione si aggiorna
  - Click 3: zoom continua, cerchio DL si illumina
  - Click 4: zoom al centro, cerchio LLM si illumina con accent gold più marcato
  - Complessità: ★★★
- **Citazioni previste**: Le 4 definizioni sono cultura generale consolidata del campo, ma citiamo una fonte autorevole per la tassonomia complessiva:
  - `¹ IBM, 2025` — sulla definizione e tassonomia AI ⊃ ML ⊃ DL ⊃ LLM
- **Ricerca web**: ✅ Verificato — definizioni standard confermate (IBM, Sebastian Raschka).
- **Note presentatore**: "Pensatela come una matrioska. Ogni livello è più specifico del precedente. Noi oggi ci concentriamo soprattutto sull'anello più interno — gli LLM — ma è importante sapere che fanno parte di un campo molto più ampio."

---

### Slide 1.3 — Analogia veicoli
- **Tipo**: `ANALOGY`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ ANALOGIA"
  - Heading: "Pensatela così"
  - Layout a 4 colonne orizzontali (o 2x2 su mobile), ciascuna con:
    - Icona/simbolo CSS (semplice, astratto)
    - Nome del livello (AI, ML, DL, LLM)
    - Analogia: "Veicoli" → "Veicoli a motore" → "Automobili" → "Tesla Model S"
  - Freccia o linea di connessione tra le 4 colonne per mostrare la progressione
  - In basso, frase riassuntiva: "Ogni livello è più specifico del precedente"
- **Stellina**: Nessuna
- **Animazioni**: Le 4 colonne appaiono in sequenza da sinistra a destra (click per ciascuna) — ★☆☆
- **Citazioni previste**: Nessuna (analogia originale, non derivata da fonte)
- **Note presentatore**: "L'analogia non è perfetta, ma vi dà l'idea. Quando qualcuno dice 'AI' potrebbe intendere cose molto diverse. Chiedete sempre: 'che tipo di AI?'"

---

### Slide 1.4 — Training vs Inference
- **Tipo**: `BRIDGE`
- **Gradiente**: `--slide-bg-blue`
- **Contenuto**:
  - Section label: "★ CONCETTO PONTE"
  - Numero: ②
  - Heading: "Training vs Inference"
  - Layout a due colonne (split visivo):
    - **Colonna sinistra — Training**:
      - Icona/simbolo: ingranaggi o "costruzione"
      - "La fase in cui il modello impara"
      - "Miliardi di dati, settimane di GPU"
      - "Costa milioni di dollari"
    - **Colonna destra — Inference**:
      - Icona/simbolo: fulmine o "conversazione"
      - "La fase in cui il modello risponde"
      - "È quello che succede quando chattate con Claude"
      - "Ogni conversazione parte dallo stesso modello base"
  - In basso, highlight box con la frase chiave: "Quando chattate con un LLM, non lo state insegnando. Il modello non impara dalla vostra conversazione."
- **Stellina**: `conoscenza.png` — nella colonna Training, piccola, a indicare "apprendimento"
- **Animazioni**:
  - Click 1: colonna Training appare
  - Click 2: colonna Inference appare
  - Click 3: highlight box in basso appare
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Epoch AI, 2025` — "Costa milioni di dollari" (costi di training dei modelli frontier)
- **Note presentatore**: "Questa distinzione è fondamentale. Molte persone pensano che il modello 'impari' dalla loro conversazione. Non è così, salvo meccanismi espliciti di memoria che vedremo più avanti."

---

### Slide 1.5 — Cosa rende gli LLM diversi
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ LLM"
  - Numero: ③
  - Heading: "Cosa rende gli LLM 'diversi'"
  - 4 bullet con gold dots:
    - **Scala** — Trilioni di token di dati¹, centinaia di miliardi di parametri²
    - **Architettura** — Il Transformer³ con il meccanismo di attenzione (lo vedremo nel Blocco 3)
    - **Obiettivo semplice ma potente** — Predire il prossimo token (lo vedremo nel Blocco 3)
    - **Emergenza di abilità** — Capacità che emergono con la scala⁴ (ragionamento, traduzione, coding) ma senza garanzia di verità
- **Stellina**: `super.png` — in basso a destra, piccola (concetti "potenti", superpotere degli LLM)
- **Animazioni**: Reveal sequenziale dei 4 bullet al click — ★☆☆
- **Citazioni previste**:
  - `¹ Meta AI Blog, 2025` — 30+ trilioni di token di training (Llama 4)
  - `² Meta AI Blog, 2025` — Fino a 400B parametri (Llama 4 Maverick) / ~2T (Behemoth annunciato)
  - `³ Vaswani et al., 2017` — Architettura Transformer
  - `⁴ Sebastian Raschka, 2025` — Emergent abilities degli LLM
- **Ricerca web**: ✅ Verificato — numeri aggiornati al 2026. Llama 4 training: 30T+ token. Parametri: fino a 2T (Behemoth).
- **Note presentatore**: "Quattro ingredienti. Scala pazzesca, un'architettura geniale (il Transformer), un obiettivo semplicissimo (predire la prossima parola) e qualcosa di quasi magico: abilità che emergono senza essere state programmate. Ma attenzione — emergenza non significa affidabilità."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 6 |
| Animazioni ★☆☆ | 3 slide (titolo, analogia, LLM diversi) |
| Animazioni ★★☆ | 2 slide (timeline, training vs inference) |
| Animazioni ★★★ | 1 slide (cerchi concentrici con zoom progressivo) |
| Stelline usate | `bussola.png` (1.0), `conoscenza.png` (1.4), `super.png` (1.5) |
| Gradienti | Blue (1.0, 1.2, 1.4), Default (1.1, 1.3, 1.5) — alternanza |
| Ricerca web | Definizioni AI/ML/DL/LLM, numeri scala modelli attuali |

---

## Dipendenze e note

- La slide 1.2 (cerchi concentrici) è una delle animazioni "hero" del deck — merita effort significativo per la fluidità e l'impatto visivo.
- I concetti di **training** e **inference** (slide 1.4) vengono richiamati in quasi tutti i blocchi successivi. Il visual deve essere memorabile.
- I "4 ingredienti" della slide 1.5 saranno sviluppati in dettaglio nei Blocchi 2 e 3.
- La timeline (slide 1.1) deve essere compatta — 6 tappe è il massimo per stare in una singola slide senza overflow.
