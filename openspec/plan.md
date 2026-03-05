# OpenSpec — Piano Deck Formazione AI Interna MemorAIz

## Panoramica

**Progetto**: Deck di slide interattive per formazione AI interna (~3-4 ore)
**Pubblico**: Team UX/UI e Comunicazione di MemorAIz
**Stile**: Preset MemorAIz "Illuminated Knowledge" (full-bleed, gradienti caldi, Fraunces + DM Sans)
**Lingua**: Italiano (tecnicismi inglesi mantenuti con spiegazione)
**Principio guida**: Poco testo per slide, animazioni didattiche step-by-step, zero formule matematiche

---

## Struttura dei blocchi e stima slide

| # | Blocco | Durata | Slide stimate | Complessità | File dettaglio |
|---|--------|-------:|:--------------:|:-----------:|----------------|
| 0 | Setup | 10' | 3-4 | Bassa | `blocco-00-setup.md` |
| 1 | Storia + Mappa concetti | 25' | 5-7 | Media | `blocco-01-storia-mappa.md` |
| 2 | Fondamenti ML | 35' | 8-12 | Alta | `blocco-02-fondamenti-ml.md` |
| 3 | Come funzionano gli LLM | 55' | 12-16 | Molto alta | `blocco-03-come-funzionano-llm.md` |
| 4 | Context Engineering | 40' | 8-10 | Media-alta | `blocco-04-context-engineering.md` |
| 5 | Embeddings & RAG | 35' | 8-10 | Alta | `blocco-05-embeddings-rag.md` |
| 6 | Reasoning, Benchmark e Modelli | 30' | 7-8 | Media-alta | `blocco-06-reasoning-models.md` |
| 6B | Safety & Rischi AI | 15-20' | 4-5 | Media-alta | `blocco-06b-safety-rischi.md` |
| 7 | Agenti (deep dive) | 55' | 14-18 | Molto alta | `blocco-07-agenti.md` |
| 8 | Checklist operativa | 10' | 3-4 | Media | `blocco-08-checklist.md` |
| **Totale** | | **~310-320'** | **~75-97** | | |

---

## Convenzioni del piano

### Tipi di slide

| Codice | Tipo | Descrizione |
|--------|------|-------------|
| `TITLE` | Titolo di sezione | Apertura blocco: numero, titolo, sottotitolo, stellina mascotte opzionale |
| `CONTENT` | Contenuto standard | Heading + bullet list con gold dots, max 4-6 punti |
| `ANALOGY` | Analogia visiva | Concetto astratto reso concreto con metafora visiva |
| `ANIM` | Animazione interattiva | Animazione step-by-step controllata dall'utente (click per avanzare) |
| `DIAGRAM` | Diagramma/schema | Flusso, architettura, schema strutturale |
| `DEMO` | Demo/esempio live | Slide che mostra un esempio concreto o una demo |
| `WORKSHOP` | Esercizio pratico | Mini-attività per i partecipanti |
| `BRIDGE` | Concetto ponte | Collegamento tra blocchi, transizione |
| `SUMMARY` | Riepilogo | Punti chiave del blocco appena trattato |

### Complessità animazioni

| Livello | Descrizione | Effort stimato |
|---------|-------------|----------------|
| ★☆☆ | Reveal sequenziale (fade-in/slide-in di elementi) | 15-20 min |
| ★★☆ | Animazione multi-step con stato (click per avanzare tra fasi) | 30-45 min |
| ★★★ | Interattivo complesso (slider, drag, input utente, spazio 2D/3D) | 60-90 min |

### Gradiente slide per blocco

Ogni blocco ha un gradiente "primario" assegnato per coerenza visiva:

| Blocco | Gradiente primario | Alternativo |
|--------|-------------------|-------------|
| 0 - Setup | `--slide-bg-default` | `--slide-bg-peach` |
| 1 - Storia | `--slide-bg-blue` | `--slide-bg-default` |
| 2 - Fondamenti ML | `--slide-bg-peach` | `--slide-bg-default` |
| 3 - LLM | `--slide-bg-mint` | `--slide-bg-blue` |
| 4 - Context Eng. | `--slide-bg-lavender` | `--slide-bg-default` |
| 5 - Embeddings/RAG | `--slide-bg-blue` | `--slide-bg-mint` |
| 6 - Reasoning/Benchmark | `--slide-bg-peach` | `--slide-bg-lavender` |
| 6B - Safety & Rischi | `--slide-bg-lavender` | `--slide-bg-peach` |
| 7 - Agenti | `--slide-bg-mint` | `--slide-bg-blue` |
| 8 - Checklist | `--slide-bg-default` | `--slide-bg-peach` |

### Uso stelline mascotte

Le stelline verranno usate con moderazione (max 1-2 per slide, molte slide senza). La scelta è basata su `images/image_descriptions.md`. L'uso è indicato nel piano di ciascun blocco solo dove aggiunge valore.

### Logo

`images/logo.svg` presente in **ogni** slide come elemento di footer (posizione bottom-left, dimensione coerente).

---

## Output tecnico

Ogni blocco produce **un singolo file HTML** nella directory `slides/XX-nome-blocco/index.html`. Ogni file è autonomo (CSS inline, JS inline) e rispetta il preset MemorAIz da `STYLE_PRESETS.md`.

---

## Flusso di lavoro

1. Approvazione di questo piano generale ✋
2. Per ogni blocco (0→8, incluso 6B tra 6 e 7):
   a. Approvazione del file di dettaglio del blocco ✋
   b. Realizzazione delle slide con `frontend-slides`
   c. Presentazione e feedback ✋
   d. Eventuali revisioni
   e. Approvazione finale del blocco ✋
3. Revisione finale dell'intero deck

---

## Prossimi passi

Dopo l'approvazione di questo file, procederò a scrivere i file di dettaglio blocco per blocco, partendo da `blocco-00-setup.md`.
