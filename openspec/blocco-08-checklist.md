# Blocco 8 — Checklist Operativa Finale (~10 min)

## Obiettivo del blocco
Chiudere la formazione con strumenti concreti e immediatamente utilizzabili: un albero decisionale per scegliere l'approccio AI giusto, le regole d'oro per lavorare con gli LLM in modo sicuro ed efficace, e un template di prompt aziendale da copiare e riusare dal giorno dopo. Questo blocco trasforma la conoscenza acquisita nei blocchi 0-7 in azione.

---

## Slide previste: 4

### Slide 8.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ BLOCCO 8"
  - Heading grande: "La vostra cassetta degli attrezzi"
  - Sottotitolo: "Decision tree, regole d'oro e template pronti all'uso"
  - Sotto il sottotitolo, piccola nota: "~10 minuti — da qui portate a casa gli strumenti operativi"
- **Stellina**: `correbussola.png` — in basso a destra (tema: navigare velocemente, orientarsi, checklist operativa)
- **Animazioni**: Auto-reveal elementi in sequenza all'ingresso — ★☆☆
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Abbiamo coperto tantissimo terreno. Ora condensiamo tutto in strumenti pratici che potete usare da domani. Tre cose: un albero per scegliere l'approccio giusto, le regole d'oro, e un template di prompt standard."

---

### Slide 8.1 — Decision Tree: che approccio usare?
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ SCEGLI L'APPROCCIO"
  - Numero: ①
  - Heading: "L'albero delle decisioni AI"
  - Sotto-heading: "Parti dalla task, arrivi allo strumento giusto"
  - Albero decisionale interattivo navigabile:
    - **Nodo radice**: "La tua task richiede azioni esterne o integrazioni?"
      - **Sì** → "AGENTE (con tool appropriati)"
        - "La task è scomponibile in sotto-compiti?"
          - **Sì** → "Orchestrazione multi-agente" (foglia, con icona multi-nodo)
          - **No** → "Singolo agente" (foglia, con icona agente)
      - **No** → "Solo LLM"
        - "Servono dati aziendali o fonti specifiche?"
          - **Sì** → "RAG (retrieval + generazione)¹" (foglia, con icona documenti)
          - **No** → "Prompt diretto"
            - "Task complessa multi-step?"
              - **Sì** → "Reasoning model²" (foglia, con icona cervello)
              - **No** → "Modello standard"
                - "Serve creatività?"
                  - **Sì** → "Temperatura alta + few-shot³" (foglia, con icona fiamma)
                  - **No** → "Temperatura bassa + vincoli stretti" (foglia, con icona target)
  - Ogni foglia ha una mini-descrizione (1 riga) che appare quando il nodo è attivo
  - Box consiglio in basso: "Regola d'oro: inizia sempre dalla soluzione più semplice. Aggiungi complessità solo quando serve.⁴"
- **Stellina**: Nessuna (il diagramma interattivo è il focus)
- **Animazioni**:
  - L'albero è navigabile: click su una scelta → si apre il ramo successivo con transizione fluida
  - I nodi non selezionati si sfumano (opacità ridotta)
  - Quando si raggiunge una foglia, appare la mini-descrizione con un effetto highlight
  - Possibilità di "tornare indietro" cliccando sul nodo genitore
  - Stato iniziale: solo il nodo radice visibile
  - Complessità: ★★★
- **Citazioni previste** (footnote in basso a destra):
  - `¹ Lakera, 2025` — RAG riduce le allucinazioni del 71% rispetto a LLM senza grounding
  - `² Vellum, 2024` — I reasoning model sono ~30x più lenti e ~6x più costosi dei modelli standard
  - `³ IBM, 2025` — Temperatura: scala 0.0-2.0 che controlla la creatività dell'output
  - `⁴ Anthropic, 2024` — "Optimizing single LLM calls with retrieval and in-context examples is usually enough"
- **Note presentatore**: "Questo albero è il vostro compagno quotidiano. Non dovete ricordare tutto — basta seguire le domande. Il principio chiave è: partite dal più semplice. Un prompt ben fatto batte un agente mal configurato nel 90% dei casi. Se un prompt diretto non basta, salite di complessità. Notate che il RAG — dare al modello i vostri documenti — riduce le allucinazioni del 71%. È la prima cosa da considerare quando lavorate con dati aziendali."

---

### Slide 8.2 — Regole d'oro per UX/Comms
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ REGOLE D'ORO"
  - Numero: ②
  - Heading: "8 regole per lavorare con l'AI"
  - Sotto-heading: "Da stampare e appendere accanto al monitor"
  - 8 regole disposte in griglia 2×4, ciascuna con un'icona/emoji simbolica e una frase breve:
    1. 🔍 **Mai senza fonte** — Chiedi citazioni o fornisci il testo sorgente. Tasso allucinazione: 0.7%–33% anche nei migliori modelli¹
    2. 🧱 **Separa sempre** — Obiettivo / vincoli / fonti / output atteso. Un prompt strutturato batte uno generico, sempre²
    3. ✏️ **Bozza + revisione** — Per contenuti pubblici o verso clienti, tratta l'output AI come prima bozza. Sempre revisione umana
    4. 🔒 **Zero dati sensibili** — Mai PII, dati cliente o info riservate in tool AI pubblici. Principio di minimizzazione³
    5. 🔄 **Itera** — Non accontentatevi della prima risposta. Perfezionate il prompt. I team con template condivisi: +67% produttività⁴
    6. ✅ **Verifica** — Specialmente fatti, numeri, citazioni, link. "Eloquenza ≠ accuratezza" (ricordate il Blocco 0?)
    7. 🧪 **Sperimenta** — Provate modelli, approcci, temperature diversi. Non c'è formula magica
    8. 🛠️ **Usate i tool** — Figma Make, Claude, generazione file — sono lì per accelerarvi
  - Box nota in basso: "Queste regole valgono per qualsiasi modello e qualsiasi strumento AI — oggi e domani."
- **Stellina**: `controllo.png` — piccola, in basso a destra (tema: verifica, controllo qualità)
- **Animazioni**:
  - Le 8 regole appaiono a coppie (2 alla volta, 4 click totali) con fade-in
  - Ultimo click: appare il box nota in basso
  - Complessità: ★☆☆
- **Citazioni previste** (footnote in basso a destra):
  - `¹ AI Multiple / About Chromebooks, 2025` — Tasso allucinazione: da 0.7% (Gemini 2.0 Flash) a 33% (o3 su domande specifiche)
  - `² Parloa, 2024` — Organizzazioni con framework strutturati: +67% produttività media
  - `³ Protecto, 2025` — Dati nei modelli possono essere memorizzati e estratti; minimizzazione come principio base
  - `⁴ MIT Sloan, 2025` — Prompt templates condivisi superano il prompting individuale
- **Note presentatore**: "Queste otto regole coprono il 90% delle situazioni. Le prime due — verificare e strutturare — sono quelle su cui insisto di più. Non è questione di diffidenza: è professionalità. Come un designer fa user testing, un professionista che usa AI fa fact-checking. La regola 4 sui dati sensibili è critica: quello che mettete in un tool AI pubblico potrebbe finire nei dati di training. Claude non lo fa di default, ma altri sì — leggete sempre i terms of service."

---

### Slide 8.3 — Prompt Template Standard Aziendale
- **Tipo**: `CONTENT` con layout speciale (template copiabile)
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ IL VOSTRO TEMPLATE"
  - Numero: ③
  - Heading: "Il template MemorAIz"
  - Sotto-heading: "Copiate, incollate, compilate — funziona con qualsiasi LLM"
  - Template visualizzato come "card" con sfondo scuro (stile codice/terminale ma senza monospace) con 6 sezioni chiaramente distinte da separatori e label colorate:

    ```
    ## SCOPO
    [Cosa deve fare il modello — 1-2 righe chiare]

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

  - A destra del template (o sotto, in base al layout), box con mini-esempio compilato:
    > **Esempio compilato:**
    > SCOPO: Scrivi 3 varianti di microcopy per la schermata "nessun risultato" dell'app MemorAIz
    > AUDIENCE: Utenti HR manager, tono professionale ma empatico
    > VINCOLI: Italiano, max 2 righe per variante, no emoji
    > OUTPUT ATTESO: Tabella con colonne: variante, tono, n° parole
  - Nota in basso: "Questo template segue il framework RTF esteso (Role-Task-Format + Context)¹ — lo standard emergente per prompt efficaci²"
- **Stellina**: `matita.png` — piccola, accanto all'heading (tema: scrivere, creare contenuti)
- **Animazioni**:
  - Click 1: appare il template vuoto (card scura con le 6 sezioni)
  - Click 2: le sezioni si "compilano" una alla volta con testo dorato (effetto typing o fade-in rapido)
  - Click 3: appare il mini-esempio compilato a destra/sotto
  - Click 4: appare la nota in basso
  - Complessità: ★★☆
- **Citazioni previste** (footnote in basso a destra):
  - `¹ Easy AI Beginner / Prompt Warrior, 2024` — Framework RTF (Role-Task-Format) come base per prompt strutturati
  - `² MIT Sloan, 2025` — "Prompt engineering is so 2024 — try prompt templates instead"
- **Note presentatore**: "Questo template è il vostro punto di partenza per qualsiasi interazione con un LLM. Le sezioni SCOPO e OUTPUT ATTESO sono le più importanti — se le compilate bene, il risultato migliora drasticamente. La sezione FONTI/CONTESTO è dove mettete i documenti di riferimento — è il vostro RAG manuale. La CHECKLIST QUALITÀ è il vostro fatto-checking integrato: elencate i criteri prima di iniziare, e verificateli alla fine. Vi invierò questo template via email dopo la formazione — salvatelo e usatelo."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 4 |
| Animazioni | Titolo: auto-reveal ★☆☆; Decision tree: navigabile ★★★; Regole: reveal a coppie ★☆☆; Template: reveal + typing ★★☆ |
| Stelline usate | `correbussola.png` (8.0), `controllo.png` (8.2), `matita.png` (8.3) |
| Gradienti | Default (8.0, 8.2), Peach (8.1, 8.3) — alternanza per ritmo visivo |
| Interattività complessa | 1 animazione ★★★ (decision tree navigabile), 1 animazione ★★☆ (template con typing) |
| Ricerca web necessaria | Alta — dati su hallucination rate, costi reasoning model, framework prompt, privacy |

---

## Mini-spec animazione ★★★: Decision Tree Navigabile (Slide 8.1)

### Descrizione visiva
Un albero decisionale con nodi arrotondati (stile card MemorAIz con bordi gold) disposto dall'alto verso il basso. Ogni nodo-domanda ha un bordo `--color-gold` e sfondo semi-trasparente scuro. Le foglie (risultati finali) hanno uno sfondo più intenso con un'icona simbolica. Le connessioni tra nodi sono linee curve con label "Sì"/"No" in pill.

### Comportamento step-by-step
1. **Stato iniziale**: solo il nodo radice visibile, centrato in alto ("La tua task richiede azioni esterne?")
2. **Click su "Sì"**: il ramo sinistro si espande con animazione (300ms ease-out). Il ramo "No" resta sfumato come alternativa cliccabile
3. **Click su "No"**: il ramo destro si espande, il ramo "Sì" si sfuma
4. **Navigazione progressiva**: ogni scelta apre il sotto-ramo successivo con la stessa logica
5. **Foglia raggiunta**: la foglia si evidenzia con bordo gold più spesso + glow leggero. Appare sotto una mini-card con 1-2 righe di spiegazione
6. **Torna indietro**: click sul nodo genitore → il sotto-albero si ritrae con animazione inversa (300ms)
7. **Reset**: doppio click sul nodo radice → tutto l'albero si resetta allo stato iniziale

### Elementi visivi
- **Nodi domanda**: rettangoli arrotondati (border-radius: 12px), sfondo `rgba(26,26,46,0.8)`, bordo `--color-gold` 2px, testo bianco, padding 16px 24px
- **Nodi foglia**: simili ma con sfondo più saturo (gradiente sottile verso `--color-gold` a 10% opacità), icona a sinistra del testo
- **Connessioni**: linee SVG curve (cubic bezier), colore `--color-gold` a 40% opacità. Quando attive: 100% opacità + animazione draw (stroke-dashoffset)
- **Label Sì/No**: pill piccole (font-size 14px) posizionate sulle connessioni, sfondo `--color-gold`, testo `--color-navy`
- **Nodi inattivi**: opacità 30%, nessun bordo gold
- **Nodo attivo**: opacità 100%, bordo gold pieno, leggera ombra dorata (box-shadow)

### Vincoli tecnici
- **Layout**: SVG-based per le connessioni curve, nodi come div posizionati con absolute/relative
- **Max-height**: `min(60vh, 500px)` — l'albero completo non deve richiedere scroll
- **Sizing nodi**: si ridimensionano proporzionalmente al container. Font size minimo 14px
- **Resize**: observer su container, ricalcola posizioni nodi e curve SVG
- **No canvas**: usare SVG + DOM, non canvas (l'interazione è click-based, non c'è animazione continua)
- **No requestAnimationFrame**: le transizioni sono CSS-based (transition: all 300ms ease-out)
- **Accessibilità**: ogni nodo è focusable (tabindex), navigazione anche da tastiera (Enter per selezionare, Escape per tornare indietro)

### Edge case
- **Cambio slide**: l'albero si resetta allo stato iniziale (solo nodo radice visibile)
- **Ritorno alla slide**: l'albero è nello stato iniziale (non ricorda lo stato precedente)
- **Resize finestra**: le posizioni si ricalcolano, le curve SVG si ri-disegnano
- **Click rapidi**: debounce di 200ms per evitare animazioni simultanee

---

## Mini-spec animazione ★★☆: Template con Typing Effect (Slide 8.3)

### Descrizione visiva
Una card con sfondo scuro (`rgba(26,26,46,0.95)`) che contiene il template strutturato in 6 sezioni. Ogni sezione ha una label colorata (colore `--color-gold`) e un'area di testo. A destra (desktop) o sotto (mobile), una card più piccola con l'esempio compilato.

### Comportamento step-by-step
1. **Click 1**: la card scura appare con fade-in (300ms). Le 6 sezioni sono visibili ma il contenuto placeholder è un grigio chiaro (`[Cosa deve fare il modello...]`)
2. **Click 2**: le label delle sezioni si illuminano una alla volta dall'alto verso il basso (100ms ciascuna, effetto cascata), il testo placeholder diventa bianco pieno
3. **Click 3**: la card esempio appare a destra/sotto con slide-in laterale. Il testo dell'esempio è in `--color-gold` per distinguerlo dal template vuoto
4. **Click 4**: la nota in basso con le citazioni appare in fade-in

### Elementi visivi
- **Card template**: max-width 600px, border-radius 16px, sfondo scuro, bordo `--color-gold` 1px, padding 32px
- **Label sezioni**: font DM Sans bold, colore `--color-gold`, font-size 14px, text-transform uppercase
- **Testo placeholder**: font DM Sans, colore `rgba(255,255,255,0.5)`, font-size 16px
- **Testo attivo**: colore bianco pieno
- **Card esempio**: sfondo leggermente più chiaro, bordo `--color-gold` dashed 1px, label "Esempio compilato" in pill gold
- **Separatori sezione**: linea 1px `rgba(255,255,255,0.1)` tra ogni sezione

### Vincoli tecnici
- **Max-height**: la card si adatta al contenuto, max-height `min(70vh, 550px)` con overflow hidden
- **Responsive**: su schermi < 900px, l'esempio va sotto la card template (stack verticale)
- **No canvas**: puro CSS + DOM
- **Transizioni**: CSS transitions, 300ms ease-out per tutti gli effetti
- **Font-size**: minimo 14px per leggibilità anche proiettato

### Edge case
- **Cambio slide**: nessun cleanup necessario (no animazioni continue)
- **Ritorno alla slide**: tutto è nello stato iniziale (click 1 da ripetere)
- **Resize**: layout flexbox/grid, si adatta automaticamente

---

## Dipendenze e note

- Questo blocco è l'ultimo della formazione e **richiama concetti da tutti i blocchi precedenti**:
  - Decision tree: agenti (Blocco 7), RAG (Blocco 5), reasoning models (Blocco 6), temperatura (Blocco 3), prompt (Blocco 4)
  - Regola 1 "Mai senza fonte": richiama "Eloquenza ≠ accuratezza" dal Blocco 0
  - Regola 2 "Separa sempre": richiama il context engineering del Blocco 4
  - Template: è la sintesi pratica del Blocco 4
- Il decision tree navigabile (★★★) è l'animazione di chiusura del deck — deve essere visivamente impattante e funzionare perfettamente, perché è l'ultimo "wow moment" della formazione
- Il template prompt va inviato ai partecipanti dopo la formazione (menzionare nelle speaker notes)
- Lo stile "card scura" del template si distingue dal resto delle slide per dare il senso di "strumento pratico", quasi un'app o un tool
