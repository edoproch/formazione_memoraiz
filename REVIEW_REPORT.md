# Report di Review Completo — Deck Formazione AI MemorAIz

**Data**: 4 marzo 2026
**Metodo**: 9 agenti di review paralleli, uno per blocco, analisi incrociata con outline e fonti
**Scope**: Tutti i 9 blocchi (86 slide totali), index.html master, navigazione cross-block

---

## Riepilogo Esecutivo

| Blocco | Slide | Voto | Issue critiche |
|--------|-------|------|----------------|
| 00 — Setup | 3 | 8.0 | "Psychofancy" errato, demo mancante |
| 01 — Storia & Mappa | 5 | 8.5 | Timeline compressa, "Perceptron" non spiegato |
| 02 — Fondamenti ML | 10 | 8.0 | Gmail spam errato, "trilioni" ambiguo |
| 03 — Come funzionano LLM | 11 | **7.5** | **2 sezioni outline ASSENTI (Allucinazioni + Multimodalita)** |
| 04 — Context Engineering | 9 | 8.5 | Slide titolo con animazione (viola CLAUDE.md) |
| 05 — Embeddings & RAG | 13 | 8.5 | Cluster senza etichette, t-SNE non spiegato |
| 06 — Reasoning Models | 10 | 8.0 | Nomi modelli da verificare, ponti deboli |
| 07 — Agenti AI | 15 | 8.5 | Citazioni vaghe ("Industria, 2025") |
| 08 — Checklist | 10 | 8.0 | **Appendice outline ASSENTE (Glossario + Limiti)** |
| **MEDIA** | **86** | **8.2/10** | |

---

## 1. ERRORI CONCETTUALI

### CRITICI

| # | Blocco | Slide | Errore | Impatto | Fix |
|---|--------|-------|--------|---------|-----|
| 1 | 00 | 4 | **"Psychofancy"** usato al posto di **"Sycophancy"** | Il termine accademico corretto e "sycophancy" (Sharma et al., 2024). Chi cerca "psychofancy" non trova nulla. | Sostituire con "Sycophancy (compiacenza)" |
| 2 | 02 | 2.2 | **Gmail spam** come esempio di unsupervised learning | Gmail usa supervised learning (dati etichettati spam/non-spam). Esempio fattualmente scorretto. | Sostituire con esempio genuinamente unsupervised (es. segmentazione clienti, topic modeling) |
| 3 | 02 | 2.7 | **"Trilioni"** ambiguita linguistica | In italiano "trilioni" = 10^18 (scala lunga). L'intento e 2×10^12 (2 mila miliardi, scala americana). | Scrivere "2.000 miliardi" o "2 trilioni (scala americana)" |

### SIGNIFICATIVI

| # | Blocco | Slide | Errore | Fix |
|---|--------|-------|--------|-----|
| 4 | 01 | 1.1 | Timeline **1974-1987 conflata** primo AI Winter + Expert Systems boom in un unico periodo | Separare o chiarire le due fasi nel testo |
| 5 | 02 | 2.7 | **"17B attivi"** (MoE) menzionato senza spiegazione | Aggiungere nota breve o rimuovere il dettaglio |
| 6 | 03 | 3.1 | Claude context **"fino a 1M"** senza indicare che e beta/esteso | Aggiungere "(beta)" o "in anteprima" |
| 7 | 03 | 3.6 | **RLVR** presentato come sotto-tipo della Fase 3, quando e piu un'estensione recente | Chiarire che e un'evoluzione, non parte del pipeline classico |
| 8 | 06 | 6.1 | **Gemini 3.1** potrebbe non esistere (ultima confermata: 2.5 Pro); **Kimi K2** non e un reasoning model | Verificare nomi e versioni attuali |
| 9 | 06 | 6.6 | Stat **RouteLLM** (95% qualita, 14% chiamate) presentata come regola generale — e specifica al setup GPT-4/Mixtral | Contestualizzare la stat |

### MINORI

| # | Blocco | Slide | Nota |
|---|--------|-------|------|
| 10 | 00 | 3 | "Probabilistico, non deterministico" — tecnicamente "deterministico" riguarda input→output identico, non l'affidabilita. Accettabile come semplificazione. |
| 11 | 01 | 1.1 | "Perceptron" raggruppato con "sistemi simbolici" — il Perceptron era una rete neurale, non un sistema simbolico. |
| 12 | 03 | 3.1 | Token IDs fabbricati (es. "!" = ID 0, che di solito e un token speciale). Accettabile per didattica. |
| 13 | 04 | 4.4 | "'Agisci come' > 'Sei un'" presentato come gerarchia netta — in realta entrambi funzionano. |
| 14 | 06 | 6.8 | Stat "4.7M campioni da 263 benchmark" — il paper parla di rischio di contaminazione, non di esposizione diretta. |

---

## 2. COMPRENSIBILITA PER IL TARGET (UX/UI + Comunicazione)

### Analogie eccellenti (da preservare)

| Blocco | Analogia | Perche funziona |
|--------|----------|-----------------|
| 01 | Veicoli → Tesla Model S (gerarchia AI) | Progressione familiare, nessun gergo |
| 02 | "Porto l'ombrello?" (neurone) | Decisione quotidiana, pesi intuitivi |
| 02 | Accordare una chitarra (backpropagation) | Processo iterativo tangibile |
| 03 | Cuoco che segue/improvvisa ricetta (temperatura) | Creativo vs preciso, immediato |
| 04 | Bicchiere di vetro (context window) | Risorsa finita, sezioni che competono |
| 05 | Mappa con quartieri (embeddings) | Designers capiscono spazi e prossimita |
| 05 | Studente che consulta appunti (RAG) | Universale, nessun gergo |
| 07 | Esperto in stanza senza telefono → con telefono (LLM vs Agent) | Differenza tangibile |
| 07 | Orchestra (multi-agent) | Ruoli specializzati che cooperano |

### Punti che rischiano di confondere il target

| # | Blocco | Slide | Problema | Suggerimento |
|---|--------|-------|----------|--------------|
| 1 | 00 | 4 | "Conoscenza vs Comportamento vs Accesso" — usa gergo non ancora spiegato (training, fine-tuning, tool/RAG) | Usare analogie: "cosa ha studiato a scuola" / "come gli hanno insegnato a rispondere" / "cosa puo cercare adesso" |
| 2 | 01 | 1.1 | "Perceptron" citato senza spiegazione | Spiegare in 5 parole o rimuovere |
| 3 | 01 | 1.1 | "ML statistico" troppo sintetico nella timeline | Espandere: "Le macchine imparano dai dati" |
| 4 | 02 | 2.5 | **"Sigma + f"** nel diagramma del neurone — simbolo intimidatorio | Sostituire con "Calcolo" o icona ingranaggio |
| 5 | 02 | 2.7 | "17B attivi" senza spiegare MoE | Rimuovere o aggiungere nota breve |
| 6 | 03 | 3.6 | **Acronimi RLHF/RLAIF/DPO/GRPO** — sovraccarico per il target | Tenere solo RLHF concettuale, relegare varianti a nota curiosita |
| 7 | 04 | 4.3 | **CO-STAR** menzionato ma non mappato al template 6 blocchi | Mostrare la corrispondenza o rimuovere il riferimento |
| 8 | 05 | 5.5 | **t-SNE/UMAP** e "riduzione dimensionale" non spiegati | Aggiungere analogia: "comprimere una foto 3D in 2D mantenendo le distanze" |
| 9 | 06 | 6.1 | "Reinforcement learning" citato senza callback al Blocco 3 | Aggiungere "(il sistema di premio/punizione visto nel Blocco 3)" |
| 10 | 06 | 6.9 | **"Open-weight"** — "pesi" potrebbe non essere chiaro | Aggiungere: "i pesi = le connessioni che definiscono cosa il modello ha imparato" |
| 11 | 07 | 7.4 | **JSON** potrebbe essere opaco per designer | Aggiungere label: "formato standard per scambiare dati" |
| 12 | 07 | 7.11 | **"Vector store"** senza spiegazione | Aggiungere "(vedi Blocco 5)" |
| 13 | 08 | 8.3 | **"Pattern DSPy"** mai introdotto nella formazione | Sostituire con "Pattern a 4 livelli" senza brand name |
| 14 | 08 | 8.2 | **Regola #9 "Piu bias = meglio"** — "bias" ha connotazione negativa (pregiudizio) gia discussa | Riformulare: "Piu vincoli = piu preciso" |

---

## 3. ERRORI GRAFICI E ANIMAZIONI

### Bug tecnici

| # | Blocco | Slide | Severita | Problema | Fix |
|---|--------|-------|----------|----------|-----|
| 1 | 03 | 3.3 | **MEDIA** | `requestAnimationFrame` in `_animateSliderTo()` **senza `cancelAnimationFrame`**. Se l'utente avanza rapidamente, l'animazione continua in background. | Salvare l'ID e cancellarlo in `stopAnimation()` |
| 2 | 04 | 4.0 | **MEDIA** | Slide titolo ha `data-steps="3"` — **viola regola CLAUDE.md** (titoli sezione devono avere `data-steps="0"`) | Cambiare a `data-steps="0"` e rendere tutti gli step visibili |
| 3 | 02 | 2.7 | **BASSA** | Coordinate SVG dei nodi (x=220,380) non corrispondono agli endpoint delle linee (x=210,370) — offset ~10px | Allineare le coordinate |

### Rischi cross-platform

| # | Blocco | Problema |
|---|--------|----------|
| 4 | 00,04,05,07 | Filename `dubbioso:pensieroso.png` contiene `:` — funziona su macOS ma **fallira su Windows e alcuni web server** |
| 5 | 05 | SVG transitions non coperte da `prefers-reduced-motion` — utenti con riduzione del moto vedranno comunque le animazioni SVG |
| 6 | 01 | Timeline potrebbe risultare compressa su viewport mobile (nessun breakpoint per il layout alternato) |

### Rischio UX

| # | Blocco | Slide | Problema |
|---|--------|-------|----------|
| 7 | 06 | 6.2 | Barre metriche: "Cost" alto = cattivo, ma visivamente la barra lunga sembra "buono". Rischio di misinterpretazione. |

### Nota positiva

Nessun blocco usa `requestAnimationFrame` in modo critico tranne il Blocco 03 (slider temperatura). Tutti gli altri usano CSS transitions/SVG con cleanup corretto. Il Blocco 02 (backpropagation loop) usa `setTimeout` con cleanup appropriato via `clearTimeout`. L'infrastruttura di lifecycle management e presente in tutti i blocchi.

---

## 4. FONTI E CITAZIONI

### Fonti deboli o vaghe

| # | Blocco | Slide | Fonte | Problema | Fix |
|---|--------|-------|-------|----------|-----|
| 1 | 02 | 2.3 | Stack Overflow, 2025 | Fonte debole per definizione accademica di self-supervised learning | Sostituire con Stanford CS229 o paper originale (Devlin et al. per BERT) |
| 2 | 06 | 6.9 | letsdatascience.com, 2026 | Blog oscuro come fonte primaria per "30x cost difference" | Usare fonte piu autorevole |
| 3 | 07 | 7.9,7.13 | **"Industria, 2025"** (3 occorrenze) | Non e una citazione reale — troppo vago | Specificare la fonte (es. "Anthropic, 2025" o "LangChain, 2025") |

### Citazioni mancanti

| # | Blocco | Slide | Cosa manca |
|---|--------|-------|------------|
| 4 | 03 | 3.3 | Slide temperatura **senza nessuna citazione** — serve almeno una fonte per il meccanismo di sampling |
| 5 | 07 | 7.11 | Slide Memory **senza citazioni** — concetti di short/long-term memory e governance meritano fonte |
| 6 | 08 | — | Citazione ICO/GDPR non presente in `references/sources.md` |
| 7 | 02 | 2.1-2.6 | Slide su supervised/unsupervised/neurone/strati senza footnote — le definizioni tecniche meriterebbero almeno una fonte ciascuna |

### Nota positiva

I blocchi 01, 04, 05 e 08 hanno citazioni eccellenti e complete. Il file `references/sources.md` e molto ben mantenuto con 150+ fonti organizzate per blocco e tema.

---

## 5. ARGOMENTI PONTE MANCANTI

### Transizioni deboli tra blocchi

| Da → A | Problema | Suggerimento |
|--------|----------|--------------|
| Blocco 0 → 1 | Nessun elemento di transizione alla fine del blocco 0 | Aggiungere una slide di transizione o una frase "Nella prossima sezione..." |
| Blocco 1 → 2 | Nessun callback alla gerarchia AI/ML/DL/LLM dal blocco 1 | Aggiungere frase iniziale: "Nel blocco precedente abbiamo visto COSA sono ML e DL. Ora vediamo COME funzionano" |
| Blocco 3 → 4 | **Salto concettuale piu grande del deck** (teoria → pratica). Solo il sottotitolo lo segnala. | Aggiungere frase esplicita: "Ora che sapete COME funziona, vediamo come USARLO al meglio" |
| Blocco 5 → 6 | Nessun ponte esplicito da RAG a reasoning models | Aggiungere: "Ora che sappiamo come dare ai modelli conoscenza esterna, vediamo come farli ragionare meglio" |
| Blocco 6 → 7 | **Ponte critico mancante**: i reasoning model sono spesso il "cervello" degli agenti AI. Questo concetto non e mai menzionato. | Aggiungere alla fine del Blocco 6: "Sapere quando usare quale modello e il primo passo verso gli agenti AI — sistemi che fanno queste scelte autonomamente" |

### Transizioni deboli intra-blocco

| Blocco | Transizione | Problema |
|--------|-------------|----------|
| 03 | Tokenizzazione → Next-token prediction | Manca frase ponte: "Ora che sappiamo COME il modello legge il testo, vediamo COSA ne fa" |
| 07 | Failure modes → MCP | Manca spiegazione del perche si passa dai problemi dei tool allo standard MCP |
| 07 | Security → Orchestrazione | Salto brusco da sicurezza a multi-agente |

### Callback mancanti a blocchi precedenti

| Blocco | Concetto | Callback suggerito |
|--------|----------|-------------------|
| 04 | Context window → next-token prediction (Blocco 3) | "Ricordate che il modello predice un token alla volta — il contesto e TUTTO cio che ha" |
| 06 | RL → Fase 3 addestramento (Blocco 3) | "Il sistema di premio/punizione che abbiamo visto nel Blocco 3" |
| 07 | Vector store → Embeddings (Blocco 5) | "(vedi Blocco 5)" |

---

## 6. COPERTURA — CONCETTI MANCANTI

### LACUNE CRITICHE

| # | Blocco | Sezione outline | Importanza per il target | Stato |
|---|--------|----------------|--------------------------|-------|
| **1** | **03** | **3.6 Allucinazioni** — cosa sono, perche succedono, implicazioni per il lavoro | **MASSIMA** — i designer devono progettare per le allucinazioni, capire quando fidarsi | **COMPLETAMENTE ASSENTE** |
| **2** | **03** | **3.7 Multimodalita** — vision, audio, video, codice, Figma Make | **ALTA** — direttamente rilevante per chi lavora con Figma e contenuti visivi | **COMPLETAMENTE ASSENTE** |
| **3** | **08** | **Appendice A: Glossario** (23 termini) | **ALTA** — riferimento post-formazione per il team | **COMPLETAMENTE ASSENTE** |
| **4** | **08** | **Appendice C: Limiti attuali** (7 limitazioni note) | **ALTA** — essenziale per vendere/usare AI onestamente | **COMPLETAMENTE ASSENTE** |

### LACUNE SIGNIFICATIVE

| # | Blocco | Sezione | Stato |
|---|--------|---------|-------|
| 5 | 03 | **Top-p / nucleus sampling** — outline 3.3 lo include esplicitamente | ASSENTE dalla slide temperatura |
| 6 | 08 | **Appendice B: 3 mini-demo suggerite** | ASSENTE |
| 7 | 00 | **Demo suggerita** (outline 0.2) — "stessa domanda, risposte diverse" | ASSENTE (potrebbe essere fatta live) |
| 8 | 01 | **Messaggio chiave esplicito** — "L'AI non e nata ieri... la scala dei dati, la potenza di calcolo e l'architettura Transformer" | IMPLICITO ma non evidenziato come takeaway |

### AGGIUNTE NON NELL'OUTLINE (tutte positive)

| Blocco | Contenuto aggiunto | Valore |
|--------|-------------------|--------|
| 03 | Distillazione e quantizzazione (slide 3.7b) | Utile — spiega come rendere i modelli accessibili |
| 05 | "Dagli LLM agli embedding" (slide 5.2) | Eccellente — colma gap pedagogico |
| 05 | Lost in the Middle (slide 5.9) | Molto utile — pratico per context engineering |
| 05 | Innovazioni RAG 2024-2025 (slide 5.10) | Buono — aggiorna il contenuto |
| 06 | Faithfulness (slide 6.5) | Eccellente — concetto critico per fiducia |
| 06 | Benchmarks + contaminazione (slides 6.7-6.8) | Utile ma possibile scope creep |
| 06 | Open vs closed weights (slide 6.9) | Utile per panoramica modelli |
| 08 | Bibliografia completa (slides 8.5-8.9) | Eccellente — credibilita accademica |

---

## 7. VALUTAZIONE GENERALE

### Punteggi per blocco

```
Blocco 00  ████████░░  8.0/10  — Solido setup, errore terminologico
Blocco 01  ████████▌░  8.5/10  — Buona narrazione storica, dettagli da affinare
Blocco 02  ████████░░  8.0/10  — Analogie ottime, esempio Gmail sbagliato
Blocco 03  ███████▌░░  7.5/10  — Animazioni eccellenti, MA 2 sezioni mancanti
Blocco 04  ████████▌░  8.5/10  — Il piu pratico e utile per il target
Blocco 05  ████████▌░  8.5/10  — Struttura narrativa eccellente, fonti rigorose
Blocco 06  ████████░░  8.0/10  — Buono ma nomi modelli da verificare
Blocco 07  ████████▌░  8.5/10  — Copertura 100%, animazioni pulite
Blocco 08  ████████░░  8.0/10  — Decision tree eccellente, appendice mancante

MEDIA DECK  ████████░░  8.2/10
```

### Punti di forza del deck

1. **Analogie di altissima qualita** — ogni concetto tecnico ha un'analogia concreta e vicina all'esperienza del target
2. **Animazioni didattiche** — temperature slider, next-token prediction, MCP chaos→order, backpropagation loop sono strumenti di insegnamento eccellenti
3. **Design visivo coerente** — palette MemorAIz, tipografia Anton/Darker Grotesque, layout puliti in tutti i 9 blocchi
4. **Step-by-step reveal** — il presentatore controlla il ritmo in ogni slide
5. **Fonti abbondanti e rigorose** — 150+ riferimenti in `sources.md`, citazioni inline nella maggior parte delle slide
6. **Progressione logica** — dal concettuale (blocchi 0-3) al pratico (4-5) all'avanzato (6-7) al riassuntivo (8)
7. **Rilevanza per MemorAIz** — riferimenti a Figma MCP, skills, prodotti dell'azienda

### Debolezze principali

1. **Due sezioni critiche dell'outline completamente assenti** (Allucinazioni + Multimodalita nel Blocco 3) — sono tra i concetti piu importanti per il target
2. **Appendice mancante** (Glossario + Limiti) — il team perde un riferimento post-formazione essenziale
3. **Ponti tra blocchi inconsistenti** — alcuni blocchi finiscono con bridge espliciti, altri no
4. **Filename con `:` ripetuto in 4 blocchi** — rischio deployment cross-platform
5. **Un bug tecnico** — cancelAnimationFrame mancante nel Blocco 03

---

## 8. PIANO DI FIX PRIORITIZZATO

### P0 — Critici (da fare prima della formazione)

- [ ] **Aggiungere slide Allucinazioni** al Blocco 03 (1-2 slide: cosa sono, perche succedono, implicazioni per il lavoro)
- [ ] **Aggiungere slide Multimodalita** al Blocco 03 (1 slide: vision, audio, codice, Figma Make)
- [ ] **Fix "Psychofancy" → "Sycophancy"** nel Blocco 00
- [ ] **Fix esempio Gmail** nel Blocco 02 — sostituire con esempio unsupervised genuino
- [ ] **Verificare nomi modelli** nel Blocco 06 (Gemini 3.1, Kimi K2)

### P1 — Importanti (migliorano significativamente il deck)

- [ ] **Aggiungere Glossario** come appendice al Blocco 08 (23 termini dall'outline)
- [ ] **Aggiungere Limiti attuali** come appendice al Blocco 08
- [ ] **Fix `data-steps` della slide titolo** Blocco 04 (da "3" a "0")
- [ ] **Aggiungere `cancelAnimationFrame`** allo slider temperatura (Blocco 03)
- [ ] **Aggiungere top-p/nucleus sampling** alla slide temperatura (Blocco 03)
- [ ] **Rinominare file** `dubbioso:pensieroso.png` → `dubbioso-pensieroso.png` e aggiornare tutti i riferimenti
- [ ] **Aggiungere ponte Blocco 6 → 7**: "reasoning models come cervello degli agenti"
- [ ] **Fix "trilioni"** nel Blocco 02 — chiarire scala

### P2 — Polish (migliorano la qualita complessiva)

- [ ] Sostituire "Sigma + f" con "Calcolo" nel neurone (Blocco 02)
- [ ] Aggiungere callback a blocchi precedenti dove mancano (vedi sezione 5)
- [ ] Semplificare acronimi RL nel Blocco 03
- [ ] Mappare CO-STAR al template nel Blocco 04
- [ ] Aggiungere etichette ai cluster nell'embedding visualizer (Blocco 05)
- [ ] Specificare fonti vaghe "Industria, 2025" nel Blocco 07
- [ ] Riformulare "Piu bias = meglio" → "Piu vincoli = piu preciso" nel Blocco 08
- [ ] Rimuovere "Pattern DSPy" → "Pattern a 4 livelli" nel Blocco 08
- [ ] Aggiungere citazioni mancanti (temperatura Blocco 03, Memory Blocco 07)
- [ ] Chiarire barre costo nel Blocco 06 (invertire direzione o etichettare)

---

*Report generato da uno swarm di 9 agenti di review specializzati, sintetizzato dal team lead.*
