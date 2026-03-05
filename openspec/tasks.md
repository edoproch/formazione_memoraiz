# Tasks: Formazione AI Interna MemorAIz

## Legenda

| Stato | Significato |
|-------|-------------|
| `[x]` | Completato |
| `[ ]` | Da fare |
| `[~]` | In corso |
| `[-]` | Bloccato / in attesa |

---

## Fase 1: Pianificazione

- [x] **T-01** Stesura outline completo dei contenuti (`formazione-ai-outline.md`)
- [x] **T-02** Creazione piano generale slide (`openspec/plan.md`)
- [x] **T-03** Specifica dettagliata blocco 0 — Setup (`openspec/blocco-00-setup.md`)
- [x] **T-04** Specifica dettagliata blocco 1 — Storia + Mappa (`openspec/blocco-01-storia-mappa.md`)
- [x] **T-05** Specifica dettagliata blocco 2 — Fondamenti ML (`openspec/blocco-02-fondamenti-ml.md`)
- [x] **T-06** Specifica dettagliata blocco 3 — Come funzionano gli LLM (`openspec/blocco-03-come-funzionano-llm.md`)
- [x] **T-07** Specifica dettagliata blocco 4 — Context Engineering (`openspec/blocco-04-context-engineering.md`)
- [x] **T-08** Specifica dettagliata blocco 5 — Embeddings & RAG (`openspec/blocco-05-embeddings-rag.md`)
- [x] **T-09** Specifica dettagliata blocco 6 — Reasoning Models (`openspec/blocco-06-reasoning-models.md`)
- [x] **T-10** Specifica dettagliata blocco 7 — Agenti (`openspec/blocco-07-agenti.md`)
- [x] **T-11** Specifica dettagliata blocco 8 — Checklist operativa (`openspec/blocco-08-checklist.md`)
- [x] **T-12** Raccolta fonti web per tutti i blocchi (`references/sources.md` — 200+ URL)
- [x] **T-13** Stesura proposal (`openspec/proposal.md`)
- [x] **T-14** Stesura design document (`openspec/design.md`)
- [x] **T-15** Stesura tasks tracking (`openspec/tasks.md`)

---

## Fase 2: Realizzazione slide

Ogni task segue il workflow: ricerca web → creazione slide → citazioni inline → aggiornamento fonti → presentazione → feedback → approvazione.

### Blocco 0 — Setup (3 slide, ~15 min formazione)
- [x] **T-20** Realizzazione slide blocco 0 con `frontend-slides`
  - Slide 0.1: Cover (TITLE)
  - Slide 0.2: Perché siamo qui (CONTENT, reveal ★☆☆)
  - Slide 0.3: Probabilistico, non deterministico (CONTENT+ANALOGY)
- [x] **T-21** Feedback e revisione blocco 0

### Blocco 1 — Storia + Mappa concetti (5 slide, ~25 min)
- [x] **T-22** Mini-spec animazione timeline (★★☆)
- [x] **T-23** Mini-spec animazione cerchi concentrici AI⊃ML⊃DL⊃LLM (★★☆)
- [x] **T-24** Realizzazione slide blocco 1 con `frontend-slides`
- [x] **T-25** Feedback e revisione blocco 1

### Blocco 2 — Fondamenti ML (10 slide, ~30 min)
- [x] **T-26** Mini-spec animazione rete neurale (★★☆)
- [x] **T-27** Mini-spec animazione backpropagation (★★☆)
- [x] **T-28** Realizzazione slide blocco 2 con `frontend-slides`
- [x] **T-29** Feedback e revisione blocco 2

### Blocco 3 — Come funzionano gli LLM (11 slide, ~40 min)
- [x] **T-30** Mini-spec animazione tokenization (★★☆)
- [x] **T-31** Mini-spec animazione next-token prediction (★★☆)
- [x] **T-32** Mini-spec animazione temperatura/sampling con slider (★★★)
- [x] **T-33** Mini-spec animazione 3 fasi addestramento (★★☆)
- [x] **T-34** Mini-spec animazione attenzione (★★☆)
- [x] **T-35** Realizzazione slide blocco 3 con `frontend-slides`
- [x] **T-36** Feedback e revisione blocco 3

### Blocco 4 — Context Engineering (9 slide, ~35 min)
- [x] **T-37** Mini-spec animazione context window (★★☆)
- [x] **T-38** Mini-spec animazione lost in the middle (★★☆)
- [x] **T-39** Realizzazione slide blocco 4 con `frontend-slides`
- [x] **T-40** Feedback e revisione blocco 4

### Blocco 5 — Embeddings & RAG (13 slide, ~35 min)
- [x] **T-41** Mini-spec animazione embeddings nello spazio 2D/3D (★★★)
- [x] **T-42** Mini-spec animazione pipeline RAG (★★☆)
- [x] **T-43** Mini-spec animazione t-SNE/UMAP visualization (★★☆)
- [x] **T-44** Realizzazione slide blocco 5 con `frontend-slides`
- [x] **T-45** Feedback e revisione blocco 5

### Blocco 6 — Reasoning, Benchmark, Safety & Modelli (10 slide, ~30 min)
- [x] **T-46** Realizzazione slide blocco 6 con `frontend-slides`
  - Slide 6.0-6.7 (titolo, definizione, come funzionano, quando usarli, routing, benchmark, arena, open vs closed)
- [x] **T-47** Ricerca web aggiornata per reasoning models e benchmark
- [x] **T-48** Feedback e revisione blocco 6

### Blocco 7 — Safety & Rischi AI (5 slide, ~15 min)
- [x] **T-58** Specifica dettagliata blocco 7 — Safety & Rischi AI (`openspec/blocco-06b-safety-rischi.md`)
- [x] **T-59** Realizzazione slide blocco 7 con `frontend-slides`
  - Slide 7.0: Titolo sezione
  - Slide 7.1: Disallineamento e Alignment Faking
  - Slide 7.2: Comportamenti emergenti rischiosi (Deception, Scheming, Reward Hacking, Sandbagging)
  - Slide 7.3: Framework di sicurezza istituzionali (Anthropic ASL, OpenAI Preparedness Framework)
  - Slide 7.4: "Intelligenza Fragile" — limiti concreti e takeaway
- [x] **T-65** Feedback e revisione blocco 7

### Blocco 8 — Agenti (15 slide, ~45 min)
- [x] **T-49** Mini-spec animazione agent loop (★★☆)
- [x] **T-50** Mini-spec animazione tool calling (★★☆)
- [x] **T-51** Mini-spec animazione MCP (★★☆)
- [x] **T-52** Mini-spec animazione orchestrazione 3 pattern (★★☆)
- [x] **T-53** Realizzazione slide blocco 8 con `frontend-slides`
- [x] **T-54** Feedback e revisione blocco 8

### Blocco 9 — Checklist operativa (10 slide, ~15 min)
- [x] **T-55** Mini-spec animazione decision tree interattivo (★★☆)
- [x] **T-56** Realizzazione slide blocco 9 con `frontend-slides`
- [x] **T-57** Feedback e revisione blocco 9

---

## Fase 3: Revisione finale

- [x] **T-60** Review coerenza visiva cross-blocchi (gradienti, logo, font, spaziature)
- [x] **T-61** Review accuratezza contenuti (cross-check con sources.md)
- [x] **T-62** Test animazioni su diversi browser/risoluzioni
- [x] **T-63** Verifica tutte le citazioni inline presenti e corrette
- [x] **T-64** Review finale utente e approvazione deck completo

---

## Dipendenze

```
T-01..T-15 (Fase 1) ──── completati ────►

T-20 → T-21 ──────────────────────────────►  Blocco 0  ✅
T-22, T-23 → T-24 → T-25 ────────────────►  Blocco 1  ✅
T-26, T-27 → T-28 → T-29 ────────────────►  Blocco 2  ✅
T-30..T-34 → T-35 → T-36 ────────────────►  Blocco 3  ✅
T-37, T-38 → T-39 → T-40 ────────────────►  Blocco 4  ✅
T-41..T-43 → T-44 → T-45 ────────────────►  Blocco 5  ✅
T-47 → T-46 → T-48 ──────────────────────►  Blocco 6  ✅
T-58 → T-59 → T-65 ──────────────────────►  Blocco 7  ✅
T-49..T-52 → T-53 → T-54 ────────────────►  Blocco 8  ✅
T-55 → T-56 → T-57 ──────────────────────►  Blocco 9  ✅

T-60..T-64 (Fase 3) ─────────────────────►  ✅
```

---

## Metriche di avanzamento

| Fase | Task totali | Completati | % |
|------|:-----------:|:----------:|:-:|
| Pianificazione | 15 | 15 | 100% |
| Realizzazione | 41 | 41 | 100% |
| Revisione finale | 5 | 5 | 100% |
| **Totale** | **61** | **61** | **100%** |
