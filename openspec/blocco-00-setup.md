# Blocco 0 — Setup (~10 min)

## Obiettivo del blocco
Accogliere i partecipanti, definire le aspettative, e piantare il seme concettuale più importante dell'intera formazione: un LLM è probabilistico, non deterministico. Eloquenza ≠ accuratezza.

---

## Slide previste: 4

### Slide 0.1 — Copertina formazione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Titolo principale: "Capire l'AI — Dal funzionamento alla pratica"
  - Sottotitolo in pill: "Formazione interna per il team UX/UI e Comunicazione"
  - Logo MemorAIz prominente (centrato, più grande del solito — è la copertina)
  - Data e durata: "~3-4 ore · Febbraio 2026"
- **Stellina**: `indica.png` — in basso a destra, piccola, che "presenta" il titolo
- **Animazioni**: Nessuna (slide statica, primo impatto)
- **Citazioni previste**: Nessuna (slide di copertina)
- **Note presentatore**: Benvenuto, presentazione rapida del programma, logistica (pause, domande).

---

### Slide 0.2 — Perché questa formazione
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ SETUP"
  - Numero: ①
  - Heading: "Perché siamo qui"
  - 3 bullet points con gold dots:
    - **Linguaggio comune** — Parlare la stessa lingua del team tecnico quando si discute di AI
    - **Guardrail operativi** — Sapere cosa si può e cosa non si può fare (qualità, privacy, sicurezza, IP)
    - **Capacità pratica** — Scrivere richieste efficaci, valutare risposte, capire cosa vendere ai clienti
- **Stellina**: Nessuna (slide pulita, contenuto chiaro)
- **Animazioni**: Reveal sequenziale dei 3 bullet (fade-in uno alla volta al click) — ★☆☆
- **Citazioni previste**: Nessuna (obiettivi interni della formazione, non fatti verificabili)
- **Note presentatore**: "Non diventerete ingegneri ML. L'obiettivo è darvi le intuizioni giuste per lavorare meglio con questi strumenti e parlare con cognizione di causa con clienti e colleghi tecnici."

---

### Slide 0.3 — Il concetto fondamentale
- **Tipo**: `CONTENT` con enfasi visiva
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ CONCETTO CHIAVE"
  - Heading grande: "Probabilistico, non deterministico"
  - Sotto-heading: "L'idea più importante di tutta la giornata"
  - 2 bullet con gold dots:
    - **Un LLM non "sa"** — Produce testo plausibile dato un contesto. Non ha conoscenza nel senso umano del termine.
    - **Eloquenza ≠ accuratezza** — Una risposta che suona sicura e ben scritta non è necessariamente vera.
  - Box/highlight visivo in basso con frase chiave in pill: "Se portate a casa solo una cosa oggi, sia questa."
- **Stellina**: `lampadina.png` — accanto all'heading o in alto a destra, a indicare l'insight fondamentale
- **Animazioni**:
  - Heading appare per primo
  - Poi i due bullet in sequenza (click)
  - Infine il box highlight (click)
  - Complessità: ★☆☆
- **Citazioni previste**: Nessuna (concetto di framing concettuale, non dato fattuale specifico — il concetto di LLM come sistema probabilistico è cultura generale del campo)
- **Note presentatore**: "Questo è il filtro mentale che dovete avere sempre attivo. Ogni volta che leggete un output AI, chiedetevi: 'È vero o è solo plausibile?'"

---

### Slide 0.4 — Dove si sbaglia più spesso
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-peach`
- **Contenuto**:
  - Section label: "★ ERRORI COMUNI"
  - Numero: ②
  - Heading: "Le quattro confusioni più frequenti"
  - 3 bullet con gold dots, ciascuno con un'icona concettuale (emoji o simbolo CSS):
    - **Conoscenza vs Comportamento vs Accesso** — Il modello "sa" cose (training), "si comporta" in un certo modo (fine-tuning), e "accede" a dati (tool/RAG). Sono tre cose diverse.
    - **"Ha funzionato una volta" ≠ "Funzionerà sempre"** — L'output è probabilistico: la stessa domanda può dare risposte diverse. Serve testare su casi diversi.
    - **Chatbot ≠ Database di fatti** — Non è un'enciclopedia verificata. È un generatore di testo plausibile.
    - **Psychofancy (compiacenza)** — Il modello tende a confermare ciò che l'utente dice, anche quando è sbagliato. Se insistete su un errore, il modello vi darà ragione — non perché siete corretti, ma perché è addestrato a compiacervi¹.
- **Stellina**: `dubbioso:pensieroso.png` — piccola, in basso a destra, a rafforzare il tema "dubbi e errori"
- **Animazioni**: Reveal sequenziale dei 4 errori (click per ciascuno) — ★☆☆
- **Citazioni previste**:
  - `¹ Anthropic / OpenAI, 2024-2025` — Sycophancy (psychofancy) è un problema noto e documentato: il modello cambia risposta corretta se l'utente insiste, massimizzando il reward di compiacenza
- **Note presentatore**: "Questi errori li fanno tutti, anche gli esperti. Non è una colpa — è che l'interfaccia (chat in linguaggio naturale) ci inganna. Sembra di parlare con qualcuno che sa, ma il meccanismo sotto è completamente diverso. Quarto punto, molto insidioso: la psychofancy. Se dite al modello 'sei sicuro? io penso che sia X', il modello tenderà a darvi ragione — anche se aveva ragione lui prima. È addestrato per compiacervi. Non fidatevi delle conferme: fidatevi dei ragionamenti."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 4 |
| Animazioni | 3 slide con reveal sequenziale (★☆☆) |
| Stelline usate | `indica.png` (slide 0.1), `lampadina.png` (slide 0.3), `dubbioso:pensieroso.png` (slide 0.4) |
| Gradienti | Default (0.1, 0.3), Peach (0.2, 0.4) — alternanza per ritmo visivo |
| Interattività complessa | Nessuna (il blocco è introduttivo, si punta su chiarezza e impatto) |
| Ricerca web necessaria | Minima — i contenuti sono concettuali e di framing, non tecnici |

---

## Dipendenze e note

- Questo blocco è autocontenuto, non dipende da altri.
- La slide 0.3 ("Probabilistico, non deterministico") verrà richiamata concettualmente in più punti dei blocchi successivi (3.2 next-token, 3.6 allucinazioni, 4.x context engineering). Importante che il visual sia memorabile.
- Il blocco è volutamente leggero: serve a creare il mindset giusto prima di entrare nei contenuti tecnici.
