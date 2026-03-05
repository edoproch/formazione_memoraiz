# Design: Formazione AI Interna MemorAIz

## Context

Il team UX/UI e Comunicazione necessita di una formazione strutturata sull'AI (~3-4 ore). Il contenuto è definito in `formazione-ai-outline.md`. Le specifiche dettagliate delle slide sono nei file `blocco-*.md`. Questo documento registra le decisioni architetturali e didattiche prese per la realizzazione.

## Goals

1. Rendere comprensibili concetti tecnici complessi a un pubblico senza background informatico/matematico
2. Creare materiale visivamente professionale, coerente con il brand MemorAIz, riutilizzabile post-formazione
3. Massimizzare la comprensione attraverso animazioni interattive e analogie concrete
4. Garantire accuratezza fattuale verificabile (citazioni inline, fonti tracciate)

## Non-Goals

1. Insegnare a programmare o a scrivere codice
2. Creare un corso completo di ML/AI (è un'introduzione operativa, non accademica)
3. Produrre un documento di testo da leggere autonomamente (le slide sono supporto per un presentatore)
4. Coprire aspetti legali/compliance in profondità (GDPR, AI Act — solo cenni dove rilevante)

## Decisions

### D1: Formato — Slide HTML autonome, non PowerPoint

**Decision:** Ogni blocco produce un singolo file HTML autonomo (CSS e JS inline) nella directory `slides/XX-nome/index.html`. Non si usa PowerPoint, Google Slides, o altri formati di presentazione tradizionali.

**Alternatives rejected:**

- **PowerPoint/Google Slides** — Impossibile creare animazioni interattive complesse (rete neurale, slider temperatura, spazio embeddings). Le transizioni native sono limitate a fade/slide, non permettono interazione utente.
- **Framework JS per presentazioni (Reveal.js, Slidev)** — Aggiungono complessità di setup e dipendenze. Per un progetto one-shot, il costo di configurazione non si giustifica.
- **PDF statico** — Nessuna interattività, nessuna animazione. Perde il valore didattico principale del progetto.

**Rationale:** HTML autonomo offre il massimo controllo sulle animazioni (Canvas, SVG, CSS animations), zero dipendenze esterne, e funziona in qualsiasi browser. Il trade-off è maggiore effort di sviluppo per slide, compensato dalla qualità didattica delle animazioni.

### D2: Approccio didattico — Analogie concrete + animazioni step-by-step, zero matematica

**Decision:** Ogni concetto tecnico viene spiegato attraverso analogie vicine all'esperienza del pubblico (design, comunicazione, vita quotidiana). Le animazioni sono controllate dall'utente (click per avanzare), non automatiche. Nessuna formula matematica in tutto il deck.

**Alternatives rejected:**

- **Approccio top-down accademico** (definizioni formali → esempi) — Il pubblico non ha background matematico; le definizioni formali creerebbero barriera all'ingresso e disengagement.
- **Animazioni automatiche con timeline fissa** — Il presentatore perde il controllo del ritmo. In una formazione con domande e discussione, il timing fisso è controproducente.
- **Formule semplificate** ("giusto un po' di matematica per capire") — Anche formule semplici creano ansia e disengagement in un pubblico non-STEM. Le analogie visive trasmettono la stessa intuizione senza la barriera.

**Rationale:** Il pubblico target (designer, comunicatori) pensa visivamente e per analogie. Le animazioni step-by-step permettono al presentatore di calibrare il ritmo sulla comprensione della sala. Trade-off: si perde precisione formale, ma per gli obiettivi di questa formazione l'intuizione operativa vale più della precisione accademica.

### D3: Struttura — 9 blocchi sequenziali con feedback incrementale obbligatorio

**Decision:** Il deck è diviso in 9 blocchi (0-8), ciascuno come unità atomica. Ogni blocco deve essere approvato dall'utente prima di procedere al successivo. Un blocco genera da 1 a 5 slide per concetto.

**Alternatives rejected:**

- **Produzione monolitica** (tutto il deck in una volta, review finale) — Rischio alto di rework massivo se lo stile o l'approccio del primo blocco non convince. Il costo di correzione cresce esponenzialmente con il numero di slide prodotte.
- **Slide singole come unità di feedback** (review per ogni slide) — Troppo granulare, rallenta il processo senza aggiungere valore. Una slide isolata non ha senso senza il contesto del suo blocco.

**Rationale:** Il blocco è l'unità naturale di contenuto didattico (un concetto con le sue sfaccettature). Il feedback incrementale cattura problemi presto senza frammentare eccessivamente il flusso di lavoro. Trade-off: processo più lento rispetto alla produzione monolitica, ma rischio di rework quasi azzerato.

### D4: Stile visivo — Preset MemorAIz "Illuminated Knowledge"

**Decision:** Tutto il deck usa il preset MemorAIz definito in `STYLE_PRESETS.md`: palette con Deep Night (#0B0E1A), Warm Gold (#D4A853), gradienti caldi, tipografia Fraunces (titoli) + DM Sans (corpo), layout full-bleed con bordi arrotondati.

**Alternatives rejected:**

- **Stile neutro/generico** (bianco, sans-serif, minimal) — Perde l'opportunità di branding interno e non crea connessione emotiva con il brand MemorAIz.
- **Stile custom per la formazione** (palette/font diversi dal brand) — Incoerenza con il resto dei materiali MemorAIz, effort aggiuntivo di design senza beneficio.

**Rationale:** Il preset esiste già e definisce un'identità visiva forte e professionale. Usarlo rafforza il branding interno e garantisce coerenza con altri materiali aziendali. Trade-off: vincola le scelte cromatiche delle animazioni, ma la palette è sufficientemente ricca (6 gradienti disponibili).

### D5: Citazioni — Apice numerico inline + footnote per slide, fonti complete in file separato

**Decision:** Ogni dato, definizione o affermazione fattuale ha un apice numerico (¹, ², ³) nella slide con footnote discreta in basso a destra (nome fonte + anno). Gli URL completi restano solo in `references/sources.md`. La numerazione riparte da ¹ in ogni slide.

**Alternatives rejected:**

- **Nessuna citazione** (fidarsi del contenuto) — Per materiale formativo, l'assenza di fonti riduce credibilità e verificabilità. Il pubblico non può approfondire autonomamente.
- **Citazioni accademiche complete** (autore, anno, journal, DOI) — Troppo rumore visivo per slide che devono avere poco testo. Inadeguato per il formato presentazione.
- **Numerazione progressiva nell'intero deck** — Con 65-86 slide si arriverebbe a numeri alti (⁴⁷), poco leggibili e inutilmente complessi.

**Rationale:** L'apice numerico è lo standard per presentazioni professionali. Bilancia credibilità (la fonte è citata) e pulizia visiva (solo nome + anno). Il file separato `sources.md` offre il dettaglio completo per chi vuole approfondire. Trade-off: l'utente deve consultare un file separato per gli URL, ma nelle slide gli URL sarebbero illeggibili comunque.

### D6: Animazioni complesse — Workflow con mini-spec obbligatoria

**Decision:** Le animazioni di complessità ★★☆ e ★★★ richiedono una mini-spec approvata prima dell'implementazione. La mini-spec descrive: stati visivi, comportamento step-by-step, vincoli tecnici (max-height, cleanup animationFrame, resize), ed edge case.

**Alternatives rejected:**

- **Implementazione diretta** (codificare l'animazione senza specifica) — Alto rischio di animazioni che non corrispondono alle aspettative, richiedendo rework costoso (le animazioni canvas sono le parti più effort-intensive).
- **Specifica solo testuale** (descrizione a parole senza struttura) — Troppo ambigua, non cattura edge case tecnici (cosa succede se l'utente torna indietro? Se ridimensiona la finestra?).

**Rationale:** Le animazioni sono lo strumento didattico principale di questo deck e rappresentano il ~60% dell'effort di sviluppo. Una specifica strutturata prima dell'implementazione previene rework. Trade-off: rallenta l'avvio dell'implementazione, ma riduce il rischio di riscritture complete.

### D7: Verifica contenuti — Ricerca web obbligatoria per ogni blocco

**Decision:** Prima di scrivere il contenuto di ogni slide, si effettua una ricerca web per verificare definizioni, numeri, parametri e stato dell'arte. Le fonti vengono tracciate in `references/sources.md` in formato tabellare.

**Alternatives rejected:**

- **Affidarsi alla conoscenza del modello AI** — La knowledge cutoff e il rischio di allucinazioni rendono inaccettabile l'assenza di verifica per materiale formativo. Un errore fattuale in formazione ha impatto reputazionale.
- **Verifica solo post-produzione** — Correggere errori fattuali dopo aver creato le slide richiede rework significativo (il contenuto influenza layout, animazioni, citazioni).

**Rationale:** Il costo di una ricerca web per blocco è basso (~5-10 min). Il costo di un errore fattuale in materiale formativo è alto (credibilità, necessità di rettifica, confusione nel team). Trade-off: rallenta la produzione, ma il materiale risultante è verificabile e aggiornato.
