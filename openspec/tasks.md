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

### Blocco 0 — Setup (4 slide, ~10 min formazione)
- [ ] **T-20** Realizzazione slide blocco 0 con `frontend-slides`
  - Slide 0.1: Cover (TITLE)
  - Slide 0.2: Perché siamo qui (CONTENT, reveal ★☆☆)
  - Slide 0.3: Probabilistico, non deterministico (CONTENT+ANALOGY)
  - Slide 0.4: Errori comuni (CONTENT, reveal ★☆☆)
- [ ] **T-21** Feedback e revisione blocco 0

### Blocco 1 — Storia + Mappa concetti (6 slide, ~25 min)
- [ ] **T-22** Mini-spec animazione timeline (★★☆)
- [ ] **T-23** Mini-spec animazione cerchi concentrici AI⊃ML⊃DL⊃LLM (★★☆)
- [ ] **T-24** Realizzazione slide blocco 1 con `frontend-slides`
  - Slide 1.0: Titolo sezione (TITLE)
  - Slide 1.1: Timeline (ANIM ★★☆)
  - Slide 1.2: Cerchi concentrici (ANIM ★★☆)
  - Slide 1.3: Training vs Inference (CONTENT)
  - Slide 1.4: Cosa rende diversi gli LLM (CONTENT)
  - Slide 1.5: Emergenza di abilità (CONTENT)
- [ ] **T-25** Feedback e revisione blocco 1

### Blocco 2 — Fondamenti ML (10 slide, ~35 min)
- [ ] **T-26** Mini-spec animazione rete neurale (★★☆)
- [ ] **T-27** Mini-spec animazione backpropagation (★★☆)
- [ ] **T-28** Realizzazione slide blocco 2 con `frontend-slides`
  - Slide 2.0-2.9 (supervised, unsupervised, self-supervised, generalizzazione, rete neurale, pesi, backprop, gradient descent, riepilogo)
- [ ] **T-29** Feedback e revisione blocco 2

### Blocco 3 — Come funzionano gli LLM (15 slide, ~55 min)
- [ ] **T-30** Mini-spec animazione tokenization (★★☆)
- [ ] **T-31** Mini-spec animazione next-token prediction (★★☆)
- [ ] **T-32** Mini-spec animazione temperatura/sampling con slider (★★★)
- [ ] **T-33** Mini-spec animazione 3 fasi addestramento (★★☆)
- [ ] **T-34** Mini-spec animazione attenzione (★★☆)
- [ ] **T-35** Realizzazione slide blocco 3 con `frontend-slides`
  - Slide 3.0-3.13 + 3.7b (token, next-token, temperatura, pre-training, SFT, RL, 3 fasi, distillazione/quantizzazione, attenzione, contesto, allucinazioni, perché, mitigazione, multimodalità)
- [ ] **T-36** Feedback e revisione blocco 3

### Blocco 4 — Context Engineering (9 slide, ~40 min)
- [ ] **T-37** Mini-spec animazione context window (★★☆)
- [ ] **T-38** Mini-spec animazione lost in the middle (★★☆)
- [ ] **T-39** Realizzazione slide blocco 4 con `frontend-slides`
  - Slide 4.0-4.9 (titolo, context window, definizione, template, best practice, lost in the middle, context rot, prompt injection, workshop prep, workshop)
- [ ] **T-40** Feedback e revisione blocco 4

### Blocco 5 — Embeddings & RAG (13 slide, ~35 min)
- [ ] **T-41** Mini-spec animazione embeddings nello spazio 2D/3D (★★★)
- [ ] **T-42** Mini-spec animazione pipeline RAG (★★☆)
- [ ] **T-43** Mini-spec animazione t-SNE/UMAP visualization (★★☆)
- [ ] **T-44** Realizzazione slide blocco 5 con `frontend-slides`
  - Slide 5.0-5.12 (titolo, embeddings, LLM→embedding, geometria, tipi, visualizzazione, problema RAG, soluzione, pipeline 6-step, qualità retrieval, UX implications, innovazioni, riepilogo)
- [ ] **T-45** Feedback e revisione blocco 5

### Blocco 6 — Reasoning, Benchmark e Modelli (7-8 slide, ~30 min)
- [ ] **T-46** Realizzazione slide blocco 6 con `frontend-slides`
  - Slide 6.0-6.4 (titolo, definizione, come funzionano, quando usarli, routing)
  - Slide 6.5: Come si misurano i modelli (MMLU, benchmark principali)
  - Slide 6.6: Chatbot Arena e il problema del data leaking (LMArena Elo, contaminazione)
  - Slide 6.7: Open vs Closed Weights (panorama modelli, tradeoff)
- [ ] **T-47** Ricerca web aggiornata per reasoning models e benchmark (fonti placeholder in sources.md)
- [ ] **T-48** Feedback e revisione blocco 6

### Blocco 6B — Safety & Rischi AI (4-5 slide, ~15-20 min)
- [ ] **T-58** Specifica dettagliata blocco 6B — Safety & Rischi AI (`openspec/blocco-06b-safety-rischi.md`)
- [ ] **T-59** Realizzazione slide blocco 6B con `frontend-slides`
  - Slide 6B.0: Titolo sezione
  - Slide 6B.1: Disallineamento e Alignment Faking
  - Slide 6B.2: Comportamenti emergenti rischiosi (Deception, Scheming, Reward Hacking, Sandbagging)
  - Slide 6B.3: Framework di sicurezza istituzionali (Anthropic ASL, OpenAI Preparedness Framework)
  - Slide 6B.4: "Intelligenza Fragile" — limiti concreti e takeaway
- [ ] **T-65** Feedback e revisione blocco 6B

### Blocco 7 — Agenti (15 slide, ~55 min)
- [ ] **T-49** Mini-spec animazione agent loop (★★☆)
- [ ] **T-50** Mini-spec animazione tool calling (★★☆)
- [ ] **T-51** Mini-spec animazione MCP (★★☆)
- [ ] **T-52** Mini-spec animazione orchestrazione 3 pattern (★★☆)
- [ ] **T-53** Realizzazione slide blocco 7 con `frontend-slides`
  - Slide 7.0-7.14 (titolo, LLM vs agent, loop, tools, tool calling, failure modes, MCP, architettura MCP, esempi MCP, sicurezza, orchestrazione, scelta pattern, memoria, skills, observability)
- [ ] **T-54** Feedback e revisione blocco 7

### Blocco 8 — Checklist operativa (4 slide, ~10 min)
- [ ] **T-55** Mini-spec animazione decision tree interattivo (★★☆)
- [ ] **T-56** Realizzazione slide blocco 8 con `frontend-slides`
  - Slide 8.0-8.4 (titolo, decision tree, golden rules, template prompt, takeaways)
- [ ] **T-57** Feedback e revisione blocco 8

---

## Fase 3: Revisione finale

- [ ] **T-60** Review coerenza visiva cross-blocchi (gradienti, logo, font, spaziature)
- [ ] **T-61** Review accuratezza contenuti (cross-check con sources.md)
- [ ] **T-62** Test animazioni su diversi browser/risoluzioni
- [ ] **T-63** Verifica tutte le citazioni inline presenti e corrette
- [ ] **T-64** Review finale utente e approvazione deck completo

---

## Dipendenze

```
T-01..T-15 (Fase 1) ──── completati ────►

T-20 → T-21 ──────────────────────────────►  Blocco 0
T-22, T-23 → T-24 → T-25 ────────────────►  Blocco 1
T-26, T-27 → T-28 → T-29 ────────────────►  Blocco 2
T-30..T-34 → T-35 → T-36 ────────────────►  Blocco 3
T-37, T-38 → T-39 → T-40 ────────────────►  Blocco 4
T-41..T-43 → T-44 → T-45 ────────────────►  Blocco 5
T-47 → T-46 → T-48 ──────────────────────►  Blocco 6
T-58 → T-59 → T-65 ──────────────────────►  Blocco 6B
T-49..T-52 → T-53 → T-54 ────────────────►  Blocco 7
T-55 → T-56 → T-57 ──────────────────────►  Blocco 8

T-21, T-25, T-29, T-36, T-40, T-45, T-48, T-65, T-54, T-57 → T-60..T-64 (Fase 3)
```

**Nota**: I blocchi possono essere realizzati solo in sequenza (0→8, incluso 6B tra 6 e 7) per il vincolo di feedback incrementale. Le mini-spec delle animazioni di un blocco possono essere preparate in anticipo.

---

## Metriche di avanzamento

| Fase | Task totali | Completati | % |
|------|:-----------:|:----------:|:-:|
| Pianificazione | 15 | 15 | 100% |
| Realizzazione | 41 | 0 | 0% |
| Revisione finale | 5 | 0 | 0% |
| **Totale** | **61** | **15** | **25%** |
