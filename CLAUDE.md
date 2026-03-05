# CLAUDE.md — Formazione AI Interna MemorAIz

## Progetto
Creazione di un deck di slide interattive per una formazione AI interna (~3-4 ore) destinata al team UX/UI e Comunicazione di MemorAIz. Il contenuto completo e la struttura dei blocchi si trovano nel file `formazione-ai-outline.md` nella root del progetto.

---

## Workflow obbligatorio

### 1. Pianificazione con OpenSpec
Prima di scrivere qualsiasi slide, usa la skill `openspec` per produrre un piano dettagliato dell'intero deck. Il piano deve:
- Elencare ogni slide (o gruppo di 2-5 slide per concetto) con titolo, tipo (contenuto, animazione, diagramma, workshop, ecc.) e stima di complessità.
- Indicare quali slide richiedono esempi animati e descriverne brevemente il comportamento atteso.
- Essere approvato dall'utente prima di procedere alla realizzazione.

### 2. Realizzazione con frontend-slides
Tutte le slide devono essere create utilizzando **esclusivamente** la skill `frontend-slides`. Lo stile da applicare è il preset **MemorAIz** definito in:
```
/Users/edo/.claude/skills/frontend-slides/STYLE_PRESETS.md
```
Leggi quel file prima di generare qualsiasi slide e rispettane rigorosamente palette, tipografia, layout e linee guida.

### 3. Feedback incrementale obbligatorio
**Non procedere mai a un nuovo concetto senza aver ricevuto feedback esplicito dall'utente sul blocco corrente.**

Il flusso per ogni unità di lavoro è:
```
1. Genera la slide (o il gruppo di 2-5 slide per un singolo concetto/esempio)
2. Presenta il risultato all'utente
3. Chiedi esplicitamente: "Vuoi modifiche a questo blocco o posso procedere?"
4. Se ci sono modifiche → applica e ri-presenta
5. Solo dopo approvazione → passa al blocco successivo
```

Un "blocco" corrisponde a una sezione atomica dell'outline (es. "3.2 Il cuore di un LLM: predire il prossimo token" è un blocco, "3.4 Le tre fasi di addestramento" è un altro blocco). Ogni blocco può generare da 1 a 5 slide.

---

## Esempi animati e interattivi

Questa è una priorità alta del progetto. Dove il concetto lo richiede o lo beneficia, crea **animazioni ed elementi interattivi** nelle slide. Dedica effort significativo alla qualità di queste animazioni — sono lo strumento principale per far comprendere i concetti a un pubblico non tecnico.

### Dove sono richiesti o fortemente consigliati:

| Concetto | Tipo di animazione/interazione suggerita |
|---|---|
| Cerchi concentrici AI ⊃ ML ⊃ DL ⊃ LLM | Animazione zoom-in progressivo, ogni cerchio si illumina e mostra la definizione |
| Rete neurale e pesi | Rete interattiva: l'utente vede i segnali propagarsi tra i nodi, i pesi che cambiano colore/spessore |
| Backpropagation | Animazione step-by-step: forward pass → errore → backward pass con i pesi che si aggiustano |
| Predizione next token | Animazione che mostra la frase che si costruisce token per token, con la distribuzione di probabilità visibile sopra |
| Temperatura / sampling | Slider interattivo: temperatura bassa → poche opzioni evidenziate; temperatura alta → distribuzione piatta, più token candidati |
| Pre-training → SFT → RL | Tre fasi animate in sequenza, il "modello" (rappresentato visivamente) cambia comportamento ad ogni fase |
| Lost in the Middle | Visualizzazione di un contesto lungo dove le sezioni centrali si "sfumano" rispetto a inizio e fine |
| Embeddings nello spazio | Spazio 2D/3D con parole come punti, animazione dell'operazione re - uomo + donna ≈ regina con i vettori che si muovono |
| Pipeline RAG | Flusso animato dei 6 step: documento → chunk → vettori → ricerca → reranking → risposta con citazione |
| Loop agente | Animazione ciclica: Observe → Think → Act → verifica → loop o risposta finale |
| Tool calling | Sequenza animata: LLM genera JSON → sistema esegue → risultato torna all'LLM |
| Orchestrazione agenti | I tre pattern (singolo, fan-out, swarm) con animazione dei flussi di comunicazione |
| Decision tree finale | Albero interattivo navigabile: click su una scelta → si apre il ramo successivo |

### Linee guida per le animazioni
- Preferire animazioni **step-by-step controllate dall'utente** (click/tap per avanzare) rispetto a animazioni automatiche, così il presentatore controlla il ritmo.
- Le animazioni devono essere **chiare e didattiche**, non decorative. Ogni movimento deve trasmettere un concetto.
- Usare transizioni fluide e tempi ragionevoli (300-500ms per step).
- Mantenere sempre la coerenza con la palette e lo stile MemorAIz.

### Workflow per animazioni complesse (obbligatorio)

Le animazioni sono classificate per complessità:

| Livello | Descrizione | Esempi |
|---------|------------|--------|
| ★☆☆ Semplice | CSS transitions, fade-in, step reveal | Auto-reveal elements, highlight boxes |
| ★★☆ Media | SVG animate, CSS keyframes multi-step, canvas statici | Cerchi concentrici, timeline animate, diagrammi di flusso |
| ★★★ Complessa | Canvas con requestAnimationFrame, interazioni multi-stato, simulazioni | Rete neurale, backpropagation, embeddings 3D, loop agente |

**Per animazioni ★☆☆**: procedi normalmente come parte della slide.

**Per animazioni ★★☆ e ★★★**: FERMA la creazione della slide e segui questo workflow:

```
1. STOP — Non codificare l'animazione inline nella slide
2. NOTIFICA — Informa l'utente: "Questa slide richiede un'animazione complessa [★★☆/★★★]: [nome]"
3. MINI-SPEC — Proponi una specifica dell'animazione che includa:
   a. Descrizione visiva: cosa si vede in ogni stato/step
   b. Comportamento step-by-step: cosa succede ad ogni click/avanzamento
   c. Elementi visivi: nodi, connessioni, colori, dimensioni (relativi al container)
   d. Vincoli tecnici: max-height del canvas, cleanup di animationFrame, gestione resize
   e. Edge case: cosa succede se l'utente torna indietro, cambia slide, ridimensiona la finestra
4. APPROVAZIONE — Attendi l'ok dell'utente sulla specifica
5. IMPLEMENTA — Crea l'animazione come componente isolato, testabile separatamente
6. INTEGRA — Solo dopo aver verificato che funziona, integrala nella slide
```

### Regole tecniche per canvas e animazioni

Ogni animazione canvas-based DEVE rispettare queste regole:

1. **Containment**: Il canvas deve avere `max-height` esplicito (es. `max-height: min(50vh, 400px)`). Non usare MAI `flex: 1` senza un `max-height`.

2. **Cleanup obbligatorio**: Ogni `requestAnimationFrame` deve:
   - Salvare l'ID restituito (`this._animFrameId = requestAnimationFrame(...)`)
   - Essere cancellato con `cancelAnimationFrame(this._animFrameId)` quando:
     - L'utente cambia slide
     - L'utente torna indietro nello step
     - La finestra viene ridimensionata (prima di re-inizializzare)

3. **Lifecycle management**: Usare un pattern di attivazione/disattivazione:
   ```javascript
   startAnimation(slideIndex) { ... }
   stopAnimation(slideIndex) {
       if (this._animFrameId) {
           cancelAnimationFrame(this._animFrameId);
           this._animFrameId = null;
       }
   }
   ```

4. **Sizing**: Il canvas deve usare il DPR (devicePixelRatio) per la nitidezza, ma le dimensioni CSS devono essere vincolate dal container padre con dimensioni esplicite.

5. **No loop infiniti**: Le animazioni loop (es. segnali che si propagano) devono fermarsi dopo ~5 secondi oppure essere controllate dall'utente.

---

## Ricerca web obbligatoria

Questo progetto riguarda formazione: **l'accuratezza dei contenuti è critica**.

### Regole:
- **Prima di scrivere il contenuto di ogni slide**, effettua una ricerca web per verificare che i concetti, le definizioni e gli esempi siano corretti e aggiornati.
- Non fare affidamento esclusivamente sulla tua conoscenza per spiegazioni tecniche. Verifica almeno:
  - Definizioni (es. cosa è esattamente MCP, come funziona RLHF, cosa sono i reasoning model).
  - Numeri e parametri (es. dimensioni context window dei modelli attuali, numero di parametri).
  - Stato dell'arte (es. quali reasoning model esistono oggi, quali MCP server sono disponibili).
- Se trovi informazioni contrastanti tra fonti, segnalalo all'utente e chiedi come procedere.
- **⚠️ Aggiorna SEMPRE il file `references/sources.md`** dopo ogni ricerca web. Per ogni blocco, registra tutte le fonti consultate con tema, nome fonte e URL in formato tabellare. Non rimandare: l'aggiornamento delle fonti fa parte del completamento del blocco.

### Citazioni inline nelle slide (obbligatorie)
Ogni concetto, dato numerico, definizione tecnica o affermazione fattuale derivata da una fonte web **DEVE avere una citazione inline nella slide stessa**. Il formato è:

- **Apice numerico** (`¹`, `²`, `³`…) posizionato subito dopo la parola o frase citata, in corpo piccolo (superscript).
- **Reference in basso a destra della slide**: un blocco discreto (font piccolo, opacità ridotta, stile `footnote`) che elenca le citazioni usate in quella slide, nel formato:
  ```
  ¹ Nome Fonte, anno   ² Nome Fonte, anno
  ```
- **Non inserire URL nelle slide** — gli URL completi restano solo nel file `references/sources.md`. Nelle slide appare solo il nome della fonte e l'anno.
- La numerazione delle citazioni **riparte da ¹ in ogni slide** (non è progressiva nell'intero deck).
- Le citazioni rendono le slide di **alto livello formativo**, verificabili e professionali.
- **Dove mettere le citazioni**: su dati numerici (parametri, costi, date), definizioni tecniche, affermazioni sullo stato dell'arte, e nomi di modelli/architetture quando si fa un'affermazione specifica.
- **Dove NON servono**: su analogie originali, opinioni del presentatore, frasi di transizione, o concetti di cultura generale.

**Esempio:**
> "Llama 4 Maverick ha 400 miliardi di parametri totali ma solo 17 miliardi attivi¹"
> → footnote in basso a destra: `¹ Meta AI Blog, 2025`

Nei file di piano (openspec/blocco-XX.md), indicare per ogni slide:
- **Citazioni previste**: elenco delle affermazioni che richiedono citazione e la fonte corrispondente.

---

## Asset grafici

Nella root del progetto è presente una cartella `images/` con:

```
images/
├── logo.svg                 ← logo MemorAIz (SVG, wordmark completo)
├── image_descriptions.md    ← ⚠️ CONSULTARE SEMPRE prima di piazzare immagini
└── stars/                   ← stelline mascotte MemorAIz (26 varianti PNG)
    └── ...
```

### ⚠️ Regola obbligatoria: consultare `images/image_descriptions.md`
**Prima di inserire qualsiasi stellina in una slide**, leggere il file `images/image_descriptions.md`. Contiene:
- La descrizione visiva di ogni immagine
- Il mood e il contesto d'uso suggerito per ciascuna
- L'associazione semantica tra stellina e concetto formativo

Scegliere la stellina il cui significato si collega al contenuto della slide (es. `lampadina.png` per un insight chiave, `connessione1.png` per MCP/integrazioni, `dubbioso-pensieroso.png` per errori comuni). **Non scegliere a caso.**

### Logo MemorAIz
- File: `images/logo.svg`
- **Deve essere presente in OGNI slide**, come elemento di header o footer (posizione coerente in tutto il deck).
- Dimensione discreta: deve essere riconoscibile ma non dominare il contenuto.
- Posizionamento e dimensione devono restare identici in tutte le slide per coerenza visiva.

### Stelline mascotte
- Sono le mascotte di MemorAIz e possono essere usate per **abbellire** le slide quando è appropriato (es. slide di apertura blocco, transizioni, momenti più leggeri, punti chiave da ricordare).
- **⚠️ Uso moderato e professionale**: non riempire le slide di stelline. L'output finale deve avere una qualità professionale, condivisibile su LinkedIn senza sembrare infantile o sovraccarico.
- Regola pratica: massimo 1-2 stelline per slide, e solo dove aggiungono valore visivo. Molte slide non ne avranno affatto.
- Nelle slide con animazioni tecniche complesse o diagrammi densi, evitarle del tutto per non creare rumore visivo.

---

## Struttura del progetto

```
/
├── CLAUDE.md                          ← questo file
├── formazione-ai-outline.md           ← outline completo dei contenuti
├── images/                            ← asset grafici
│   ├── logo.svg                       ← logo (presente in ogni slide)
│   ├── image_descriptions.md          ← descrizione + uso suggerito di ogni immagine
│   └── stars/                         ← stelline mascotte (26 varianti, uso moderato)
├── openspec/                          ← output della pianificazione openspec
│   └── plan.md                        ← piano dettagliato delle slide
├── slides/                            ← output delle slide (gestito da frontend-slides)
│   ├── 00-setup/
│   ├── 01-storia-mappa/
│   ├── 02-fondamenti-ml/
│   ├── 03-come-funzionano-llm/
│   ├── 04-context-engineering/
│   ├── 05-embeddings-rag/
│   ├── 06-reasoning-models/
│   ├── 07-safety-rischi/
│   ├── 08-agenti/
│   └── 09-checklist/
└── references/                        ← fonti utilizzate per la verifica dei contenuti
    └── sources.md
```

---

## Stile e tono dei contenuti

- **Pubblico**: designer UX/UI e professionisti della comunicazione. Non hanno background in informatica o matematica.
- **Tono**: professionale ma accessibile, mai accademico. Usare analogie concrete e vicine alla loro esperienza.
- **Lingua**: italiano per tutti i contenuti. Termini tecnici inglesi mantenuti dove sono standard (token, embedding, fine-tuning, ecc.) ma sempre con spiegazione alla prima occorrenza.
- **Zero formule matematiche**. I concetti quantitativi vanno spiegati con analogie, visualizzazioni e animazioni.
- **Ogni slide deve avere poco testo**: le slide servono come supporto visivo per il presentatore, non come documento da leggere. Il contenuto dettagliato è nell'outline e nelle speaker notes.
- **Le slide di titolo di sezione (blocco) non devono avere animazioni**: tutto il testo deve essere visibile immediatamente (`data-steps="0"`), senza step reveal. Queste slide servono come separatori visivi e il presentatore non ha bisogno di "rivelare" un titolo.

---

## Checklist pre-consegna di ogni blocco

Prima di presentare un blocco all'utente per il feedback, verifica:
- [ ] Lo stile è conforme al preset MemorAIz di STYLE_PRESETS.md
- [ ] Il logo MemorAIz è presente in ogni slide (header o footer, posizione coerente)
- [ ] Le stelline mascotte, se usate, sono scelte consultando `images/image_descriptions.md` e sono al massimo 1-2 per slide
- [ ] Il contenuto è stato verificato con ricerca web
- [ ] Ogni dato/definizione/affermazione fattuale ha la citazione inline (apice numerico + footnote in basso a destra)
- [ ] Le citazioni usano il formato corretto: `¹ Nome Fonte, anno` (no URL nelle slide)
- [ ] Il file `references/sources.md` è aggiornato con tutte le fonti del blocco
- [ ] Le animazioni (se presenti) funzionano e sono controllabili step-by-step
- [ ] Le animazioni canvas hanno max-height esplicito e non espandono oltre il container
- [ ] Ogni requestAnimationFrame ha il corrispondente cancelAnimationFrame nel cleanup
- [ ] Le animazioni si fermano quando si cambia slide
- [ ] Le animazioni ★★☆/★★★ sono state approvate tramite mini-spec prima dell'implementazione
- [ ] Il testo nelle slide è minimale (il dettaglio è nelle speaker notes o nell'outline)
- [ ] La lingua è italiana, i tecnicismi inglesi sono spiegati
- [ ] Non ci sono errori fattuali rispetto all'outline approvato
- [ ] L'output è professionale e condivisibile su LinkedIn

---

## Registrazione blocchi in `slides/index.html` (obbligatoria)

Quando un nuovo blocco di slide viene completato e approvato dall'utente, **devi aggiornare `slides/index.html`** prima di considerare il blocco consegnato. Le modifiche necessarie sono:

1. **Nell'array `BLOCKS`**: trova l'oggetto con lo `slug` corrispondente al blocco appena creato e cambia `ready: false` → `ready: true`. Se il numero di slide era un range (es. `'8-10'`), aggiornalo al numero effettivo di slide create.

2. **Progress bar**: aggiorna i tre valori correlati:
   - `.progress-fill` → proprietà CSS `width` nella sezione `<style>`: calcola `Math.round((blocchi_pronti / 9) * 100)` e imposta come percentuale.
   - `#progressText` → testo nell'HTML: aggiorna "X di 9 blocchi pronti" con il nuovo conteggio.

Questo garantisce che il master deck rifletta sempre lo stato reale dei blocchi disponibili.

---

## Comandi rapidi

Se l'utente dice:
- **"prossimo"** o **"avanti"** → il blocco corrente è approvato, procedi al successivo
- **"modifica [X]"** → applica la modifica richiesta e ri-presenta il blocco
- **"rifare"** → il blocco non va bene, ricrealo da zero con un approccio diverso
- **"overview"** → mostra lo stato di avanzamento (blocchi completati / rimanenti)
- **"fonti"** → mostra le fonti web consultate per il blocco corrente
