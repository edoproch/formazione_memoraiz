# Change: Formazione AI Interna per Team Non-Tecnici

Questa proposal produce un deck di slide interattive (~65-86 slide, ~3-4 ore) per formare il team UX/UI e Comunicazione di MemorAIz sui fondamenti dell'AI e degli LLM.

## Why

### Il problema: gap di conoscenza AI nel team non-tecnico

MemorAIz è un'azienda AI-first, ma i team UX/UI e Comunicazione operano quotidianamente con strumenti e prodotti AI senza una comprensione strutturata di come funzionano. Questo crea frizioni concrete:

1. **Aspettative disallineate sul prodotto** — I designer propongono feature che presuppongono comportamento deterministico ("il sistema deve sempre rispondere X a questa domanda"), quando gli LLM sono intrinsecamente probabilistici. Risultato: cicli di revisione aggiuntivi e frustrazione quando il prodotto "non fa quello che doveva fare".

2. **Linguaggio non condiviso con il team tecnico** — Termini come "context window", "embedding", "RAG", "agent", "tool calling" vengono usati in modo impreciso o non vengono usati affatto. I meeting cross-funzionali richiedono più tempo perché il team tecnico deve spiegare concetti base ripetutamente.

3. **Incapacità di valutare le risposte AI** — Chi scrive prompt per il lavoro quotidiano (copywriting, analisi, ricerca) non sa distinguere un output affidabile da un'allucinazione. Eloquenza viene scambiata per accuratezza.

4. **Comunicazione esterna a rischio** — Il team Comunicazione descrive le capacità AI del prodotto senza comprenderne i limiti reali. Questo può portare a promesse eccessive verso clienti e stakeholder ("il nostro AI sa tutto sui vostri documenti" vs la realtà del RAG).

5. **Sotto-utilizzo degli strumenti AI** — I colleghi usano Claude/ChatGPT come "Google migliorato" perché non conoscono pattern avanzati (context engineering, few-shot, chain-of-thought) e non capiscono quando un task richiede RAG, un agent, o un semplice prompt.

### Cosa succede se non facciamo nulla

- Il team tecnico continua a essere il collo di bottiglia per ogni decisione di prodotto che coinvolge AI
- I designer progettano UX per sistemi AI basandosi su modelli mentali sbagliati
- La comunicazione aziendale resta vaga o inaccurata sulle capacità del prodotto
- Il team non-tecnico non riesce a contribuire a decisioni strategiche su feature AI

### Chi ne beneficia

- **Team UX/UI**: progettano interfacce AI-aware (gestione allucinazioni, citazioni, feedback loops)
- **Team Comunicazione**: descrivono il prodotto con precisione tecnica accessibile
- **Team tecnico** (indirettamente): meno tempo speso a spiegare concetti base, review più efficaci
- **Azienda**: decisioni di prodotto più informate, comunicazione esterna più credibile

## What Changes

- Creazione di un deck di ~65-86 slide interattive in HTML/CSS/JS, organizzato in 9 blocchi tematici
- Inclusione di 30+ animazioni didattiche (da semplici reveal a simulazioni interattive)
- Copertura end-to-end: dalla storia dell'AI fino ad agenti, MCP, e checklist operative
- Materiale riutilizzabile come riferimento interno post-formazione

See `design.md` for detailed decisions on format, tools, and pedagogical approach.

## Impact

- **Specs coinvolte**: `openspec/plan.md`, 9 file `blocco-*.md`
- **Output**: 9 file HTML autonomi in `slides/00-setup/` ... `slides/08-checklist/`
- **Fonti**: 200+ URL tracciate in `references/sources.md`
- **Durata stimata della formazione**: ~285 minuti (3-4 ore con pause)
- **Pubblico diretto**: ~5-10 persone (team UX/UI + Comunicazione)
