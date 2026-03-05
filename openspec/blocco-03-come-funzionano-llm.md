# Blocco 3 — Come funzionano gli LLM (~55 min)

## Obiettivo del blocco
Far capire ai partecipanti il funzionamento interno degli LLM: come leggono il testo (token), come generano risposte (next-token prediction), come vengono addestrati (le 3 fasi), come gestiscono il contesto (attenzione), perché "inventano" cose (allucinazioni) e cosa possono vedere oltre al testo (multimodalità).

Questo è il blocco più denso e importante del deck — è il cuore tecnico della formazione. Dopo questo blocco, i partecipanti avranno un modello mentale solido per capire tutti i blocchi successivi.

---

## Slide previste: 15

### Slide 3.0 — Titolo di sezione
- **Tipo**: `TITLE`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ BLOCCO 3"
  - Heading grande: "Come funzionano gli LLM"
  - Sottotitolo: "Dal testo al token, dalla probabilità alla risposta"
  - Sotto il sottotitolo, piccola nota: "~55 minuti — il cuore tecnico della formazione"
- **Stellina**: `conoscenza.png` — in basso a destra (tema comprensione profonda)
- **Animazioni**: Auto-reveal elementi in sequenza all'ingresso — ★☆☆
- **Citazioni previste**: Nessuna (slide di titolo sezione)
- **Note presentatore**: "Questo è il blocco più lungo e più importante. Dopo questi 55 minuti avrete un modello mentale solido di come funzionano gli strumenti che usate ogni giorno. Niente panico — niente formule, solo intuizioni e animazioni."

---

### Slide 3.1 — Tokenizzazione
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ COME LEGGONO"
  - Heading: "Gli LLM non leggono parole"
  - Sotto-heading: "Leggono token — frammenti di testo"
  - Animazione interattiva di tokenizzazione:
    - **Stato 1**: Frase in italiano: "MemorAIz è fantastica!" appare come testo normale
    - **Stato 2**: La frase si "spezza" in token colorati con bordi arrotondati: `["Memor", "AI", "z", " è", " fantast", "ica", "!"]` — ogni token ha un colore diverso dalla palette MemorAIz
    - **Stato 3**: Sotto ogni token, appare un piccolo numero (l'ID nel vocabolario)
  - Box dati in basso (3 colonne):
    - "Vocabolario: ~100K-256K token possibili¹"
    - "Contesto Claude: 200K token (~150K parole)²"
    - "Italiano = ~1.5x più token dell'inglese³"
  - Box curiosità in basso a sinistra: "🍓 Lo 'Strawberry Problem': quante 'r' ci sono in 'strawberry'? Gli LLM sbagliano perché non vedono lettere singole — solo token. Il modello o1 di OpenAI fu internamente chiamato 'Strawberry' proprio per aver risolto questo problema con il ragionamento⁴."
  - Box costi in basso a destra: "I costi API si misurano in token: input + output"
- **Stellina**: Nessuna (l'animazione è il focus)
- **Animazioni**:
  - Click 1: frase appare come testo normale
  - Click 2: la frase si frantuma animata nei singoli token (ogni pezzo si stacca, si colora, e assume un bordo)
  - Click 3: gli ID token appaiono sotto ciascun pezzo
  - Click 4: il box dati appare in basso
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ OpenAI / Google, 2025` — Vocabolari dei tokenizer: GPT-4 ~200K (o200k_base), Gemini ~256K
  - `² Anthropic, 2025` — Claude context window: 200K token
  - `³ Studi empirici su tokenizzazione multilingue` — Lingue romanze ~1.3-1.5x più token dell'inglese
  - `⁴ Reuters / Axios, 2024` — OpenAI sviluppò internamente il modello o1 con il nome in codice "Strawberry", rilasciato come o1-preview il 12 settembre 2024
- **Ricerca web**: ✅ Verificato — vocabolari confermati. Claude 200K confermato. Rapporto italiano/inglese 1.3-1.5x confermato da test empirici su diversi tokenizer. Strawberry problem confermato da multiple fonti (SecWest, Arbisoft, Axios).
- **Note presentatore**: "Prima sorpresa: gli LLM non leggono parole. Leggono pezzetti di testo chiamati token. La parola 'MemorAIz' potrebbe diventare tre token. Perché vi interessa? Perché tutto si misura in token: i limiti di contesto, i costi, e anche la qualità. E l'italiano costa di più dell'inglese — circa il 50% in più — perché le nostre parole sono più lunghe e il modello le spezza in più pezzi."

---

### Slide 3.2 — Next-token prediction
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ IL CUORE"
  - Heading: "Predire il prossimo token"
  - Sotto-heading: "Il meccanismo fondamentale di ogni LLM"
  - Animazione step-by-step di generazione autoregressiva:
    - **Area principale**: una frase che si costruisce token per token
    - **Area sopra**: una distribuzione di probabilità (barre verticali) che mostra i candidati per il prossimo token
    - Frase iniziale: "Il gatto si è seduto sul ___"
    - La distribuzione mostra: {tappeto: 15%, divano: 12%, pavimento: 8%, letto: 6%, ...}
    - Il token "tappeto" viene scelto (la barra si illumina gold) e si aggiunge alla frase
    - La frase diventa: "Il gatto si è seduto sul tappeto ___"
    - Nuova distribuzione per il prossimo token
    - Il token "." viene scelto e la frase si completa
  - Box insight in basso: "Tutto ciò che un LLM produce — saggi, codice, poesie — emerge da questo meccanismo ripetuto migliaia di volte¹"
- **Stellina**: `lampadina.png` — piccola, accanto al box insight
- **Animazioni**:
  - Click 1: frase iniziale con "___" alla fine
  - Click 2: distribuzione di probabilità appare sopra con barre animate
  - Click 3: il token "tappeto" viene scelto (barra gold, animazione di selezione), si aggiunge alla frase
  - Click 4: nuova distribuzione per il prossimo token → "." scelto, frase completa
  - Click 5: box insight appare in basso
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ IBM, 2025` — LLM come modelli di next-token prediction
- **Ricerca web**: ✅ Verificato — next-token prediction è la descrizione standard del funzionamento fondamentale degli LLM. Confermato da tutte le fonti principali.
- **Note presentatore**: "Ecco il segreto. Un LLM fa una sola cosa: dato tutto il testo che ha visto finora, calcola la probabilità di ogni token possibile come prossimo pezzo. Poi sceglie. Il token scelto si aggiunge alla frase, e il ciclo ricomincia. È come un autocomplete sofisticatissimo. Tutto — codice, poesie, analisi — emerge da questo meccanismo apparentemente semplice ripetuto migliaia di volte."

---

### Slide 3.3 — Temperatura e Sampling
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ CONTROLLO"
  - Heading: "Temperatura — il termostato della creatività"
  - Sotto-heading: "Come il modello sceglie tra i token possibili"
  - **Slider interattivo** al centro della slide:
    - Cursore che va da "Temperatura 0" (sinistra, colore freddo/blu) a "Temperatura 1+" (destra, colore caldo/arancio)
    - Sopra lo slider: una distribuzione di probabilità che cambia forma in tempo reale
      - **T=0**: una barra domina (quasi deterministica), le altre quasi invisibili
      - **T=0.5**: alcune barre evidenti, le piccole più visibili
      - **T=1+**: distribuzione molto più piatta, molti candidati con probabilità simile
    - Sotto lo slider: indicazione del tipo di output atteso
      - T bassa: "Preciso, prevedibile, ripetitivo"
      - T alta: "Creativo, vario, più rischioso"
  - Box analogia in basso: "Come un cuoco: temperatura bassa = segue la ricetta | temperatura alta = improvvisa"
  - Box pratico in basso a destra: "Analisi dati, codice → T bassa | Brainstorming, copy → T alta"
- **Stellina**: Nessuna (lo slider è il focus visivo)
- **Animazioni**:
  - Click 1: slider appare con distribuzione a T=0 (una barra dominante)
  - Click 2: il cursore si muove verso T=0.5, la distribuzione si redistribuisce animata
  - Click 3: il cursore si muove verso T=1+, la distribuzione diventa piatta
  - Click 4: box analogia e box pratico appaiono
  - (Idealmente: lo slider è davvero interattivo, il presentatore può trascinarlo)
  - Complessità: ★★★
- **Citazioni previste**: Nessuna (il concetto di temperatura è standard e documentato in ogni guida LLM. Le definizioni sono cultura generale.)
- **Note presentatore**: "La temperatura è il parametro che controlla quanto il modello 'osa'. A temperatura zero, sceglie quasi sempre il token più probabile — output prevedibili e sicuri. Alzando la temperatura, la distribuzione si appiattisce e il modello considera opzioni meno ovvie — più creatività ma anche più rischio di errore. Ecco perché la stessa domanda può dare risposte diverse: stessa distribuzione, scelte diverse."

---

### Slide 3.4 — Pre-Training (Fase 1)
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ LE 3 FASI"
  - Numero: ①
  - Heading: "Pre-Training — leggere tutta Internet"
  - Layout animato con una rappresentazione visiva del modello (un cervello/sfera stilizzata al centro) che "assorbe" dati:
    - **A sinistra**: icone/simboli che rappresentano le fonti dati — libri, pagine web, codice, articoli, Wikipedia — con frecce che fluiscono verso il modello
    - **Al centro**: il modello si "riempie" progressivamente (barra di progresso o cambio colore)
    - **A destra**: output → il modello genera testo ma caotico/disordinato (parla di tutto, senza filtro)
  - Dati numerici sotto:
    - "Trilioni di token di training data¹"
    - "Costo: centinaia di milioni di dollari²"
    - "Task: predire il prossimo token (self-supervised)"
  - Analogia in basso: "Come leggere l'intera biblioteca di Babele. Sai tantissimo, ma nessuno ti ha detto come essere utile."
- **Stellina**: `globo.png` — piccola, accanto ai dati numerici (tema: scala, Internet)
- **Animazioni**:
  - Click 1: icone fonti dati appaiono a sinistra con etichette
  - Click 2: le frecce si animano verso il modello centrale, che si "riempie" progressivamente
  - Click 3: a destra, il modello produce testo caotico/disordinato. Dati numerici appaiono sotto.
  - Click 4: analogia della biblioteca appare in basso
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Meta AI, 2025` — Llama 4 addestrato su 30T+ token
  - `² Epoch AI, 2025` — Costi training modelli frontier: GPT-5 stimato ~$500M
- **Ricerca web**: ✅ Verificato — Llama 4 pre-trained su 30T+ token (Meta AI Blog). Costi training frontier: $500M stimato per GPT-5 (Epoch AI), $5.6M dichiarato per DeepSeek V3.
- **Note presentatore**: "Fase uno: il modello legge tutto Internet. Trilioni di token — libri, articoli, codice, Wikipedia, forum. Il task è semplicissimo: prevedi il prossimo token. Dopo trilioni di ripetizioni, il modello ha assorbito un'enormità di conoscenza. Ma è come un'enciclopedia vivente senza filtro: sa tutto ma non sa come essere utile. Se gli chiedete qualcosa, potrebbe rispondere, continuare il vostro testo, o dire qualcosa di completamente fuori tema."

---

### Slide 3.5 — SFT (Fase 2)
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ LE 3 FASI"
  - Numero: ②
  - Heading: "Supervised Fine-Tuning — imparare a essere utile"
  - Layout continuativo (stesso modello stilizzato della slide 3.4, ma ora il modello cambia "postura"):
    - **A sinistra**: icone di conversazioni domanda-risposta curate (clipboard con checkmark), scritte da annotatori umani
    - **Al centro**: il modello si "allinea" — la sfera caotica diventa più ordinata, forma più definita
    - **A destra**: output → il modello risponde in modo strutturato a domande
  - Bullet sotto (2 punti):
    - "Il modello impara il formato dell'assistente¹: seguire istruzioni, rispondere alle domande, dire 'non lo so'"
    - "Dati: migliaia di conversazioni di alta qualità scritte da annotatori umani²"
  - Analogia in basso: "Dopo aver letto tutta la biblioteca, un tutor ti insegna come usare quella conoscenza per rispondere agli studenti."
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: conversazioni curate appaiono a sinistra
  - Click 2: le conversazioni fluiscono verso il modello, che si trasforma (da caotico a ordinato)
  - Click 3: a destra, il modello produce risposte strutturate. Bullet sotto appaiono.
  - Click 4: analogia in basso
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ Anthropic / OpenAI, 2023-2025` — SFT come fase standard della pipeline di training LLM
  - `² InstructGPT paper, 2022` — Primo paper sistematico sulla pipeline SFT → RLHF (Ouyang et al.)
- **Ricerca web**: ✅ Verificato — SFT è ancora il termine e il metodo standard. InstructGPT (2022) ha definito la pipeline.
- **Note presentatore**: "Fase due: il fine-tuning supervisionato. Annotatori umani scrivono migliaia di conversazioni di alta qualità — 'se un utente chiede X, una buona risposta è Y'. Il modello impara il formato: come rispondere a una domanda invece di continuare il testo, come seguire istruzioni, quando dire 'non lo so'. È come dare un corso di comunicazione a quell'enciclopedista."

---

### Slide 3.6 — RL / Allineamento (Fase 3)
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ LE 3 FASI"
  - Numero: ③
  - Heading: "Reinforcement Learning — imparare a farlo bene"
  - Layout continuativo:
    - **A sinistra**: icone di valutatori umani (o AI) che confrontano risposte con 👍/👎 e ordinamenti
    - **Al centro**: il modello si "raffina" — la sfera diventa più lucida/polished
    - **A destra**: output → risposte sicure, utili, con il tono giusto
  - Bullet sotto (3 punti):
    - "Valutatori confrontano risposte: 'questa è migliore di questa'¹"
    - "Il modello impara preferenze umane: sicurezza, utilità, onestà, tono²"
    - "⚠️ RL cambia il comportamento, non aggiunge fatti. Non è una nuova enciclopedia."
  - Box con varianti tecniche (piccolo, per i curiosi): "RLHF (umani) | RLAIF (AI come valutatore)³ | DPO (ottimizzazione diretta)⁴"
  - Box curiosità in basso a sinistra: "📌 'Effetto Nigeria': ChatGPT usa la parola 'Delve' 10-100x più del normale⁵. Perché? Molti annotatori RLHF erano nigeriani, dove 'Delve' è comune nell'inglese formale. Il bias degli annotatori diventa bias del modello."
  - Analogia in basso: "Come un cameriere che impara non solo a servire, ma come il cliente preferisce essere servito."
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: valutatori con confronti appaiono a sinistra
  - Click 2: il modello si raffina, output strutturato a destra
  - Click 3: bullet sotto + warning sull'RL
  - Click 4: box varianti tecniche + analogia
  - Complessità: ★★☆
- **Citazioni previste**:
  - `¹ InstructGPT / Ouyang et al., 2022` — Pipeline RLHF con reward model e PPO
  - `² Anthropic, 2023` — Constitutional AI / RLAIF come approccio di allineamento scalabile
  - `³ Anthropic, 2023` — RLAIF: usare AI come valutatore anziché solo umani
  - `⁴ Rafailov et al., 2023` — DPO: Direct Preference Optimization, alternativa semplificata a RLHF con reward model
  - `⁵ Simon Willison / Towards AI, 2024` — L'uso anomalo di "Delve" in ChatGPT correlato al background culturale degli annotatori RLHF nigeriani. La parola è apparsa nelle pubblicazioni mediche 10-100x più del normale dopo l'adozione di GPT.
- **Ricerca web**: ✅ Verificato — RLHF è ancora il termine "ombrello" colloquiale. DPO è l'innovazione più adottata (open source specialmente). GRPO usato da DeepSeek. Constitutional AI ben consolidato per Anthropic. Effetto Nigeria/Delve confermato da Simon Willison, Towards AI e Tony Zador (osservazione virale su X).
- **Note presentatore**: "Fase tre: il raffinamento. Valutatori umani — o altri modelli AI — confrontano coppie di risposte: 'questa è migliore'. Il modello viene premiato per le risposte preferite. È qui che impara a essere sicuro, utile, onesto, a non dire cose tossiche. Punto critico: l'RL cambia il *comportamento*, non aggiunge fatti. Non è una nuova Wikipedia — è un corso di buone maniere."

---

### Slide 3.7 — Schema riassuntivo delle 3 fasi
- **Tipo**: `DIAGRAM`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ SCHEMA"
  - Heading: "Le tre fasi in sintesi"
  - Diagramma orizzontale a 3 blocchi collegati da frecce:
    - **Blocco 1 — Pre-Training**: icona libro/globo → "Conoscenza grezza" → sotto: "Trilioni di token, ~$500M"
    - **Blocco 2 — SFT**: icona conversazione → "Saper seguire istruzioni" → sotto: "Migliaia di esempi curati"
    - **Blocco 3 — RL**: icona pollice su/giù → "Farlo bene e in modo sicuro" → sotto: "Preferenze umane/AI"
  - Sotto il diagramma, formula visiva:
    - "Pre-training = conoscenza grezza | SFT = formato assistente | RL = allineamento e sicurezza"
- **Stellina**: Nessuna (diagramma è già denso)
- **Animazioni**:
  - Click 1: blocco Pre-Training
  - Click 2: freccia + blocco SFT
  - Click 3: freccia + blocco RL
  - Click 4: formula visiva riassuntiva
  - Complessità: ★★☆
- **Citazioni previste**: Nessuna (riassunto visivo delle slide precedenti, nessun dato nuovo)
- **Note presentatore**: "Ecco lo schema completo. Tre fasi: prima legge tutto, poi impara a rispondere, poi impara a farlo bene. Ricordate: la conoscenza viene dalla fase 1, il comportamento dalle fasi 2 e 3. Ecco perché un modello può 'sapere' qualcosa ma comportarsi male, o viceversa — le due cose sono addestrate separatamente."

---

### Slide 3.7b — Ottimizzazione post-addestramento: distillazione e quantizzazione
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ OTTIMIZZAZIONE"
  - Heading: "Rendere i modelli più piccoli e veloci"
  - Sotto-heading: "Distillazione e quantizzazione — perché esistono modelli economici"
  - Layout a due colonne:
    - **Colonna sinistra — Distillazione (Teacher → Student)**:
      - "Un modello grande (teacher) insegna a un modello piccolo (student)¹"
      - "Il teacher genera esempi di alta qualità, lo student impara a replicarli"
      - "Esempio: DeepSeek R1 (671B) → R1-Distill-Qwen-7B: un modello 7B che batte GPT-4o su alcuni benchmark²"
      - Analogia: "Come un mentore esperto che forma un apprendista — l'apprendista non sa tutto, ma impara i pattern più importanti"
    - **Colonna destra — Quantizzazione**:
      - "Comprimere i pesi del modello: da 32 bit a 4 bit per numero³"
      - "Il modello diventa ~4x più piccolo, un po' meno preciso"
      - "Modelli da 70B parametri possono girare su una GPU consumer"
      - "Strumenti: Llama.cpp, Ollama — AI locale sul vostro Mac"
      - Analogia: "Come comprimere un JPEG — il file è 4x più piccolo, perdete un po' di dettaglio ma è ancora utilizzabile"
  - Box insight in basso: "Ecco perché esistono modelli 'mini' economici e modelli 'pro' costosi: distillazione + quantizzazione rendono l'AI accessibile a tutti"
- **Stellina**: Nessuna (slide con due colonne dense)
- **Animazioni**:
  - Click 1: heading + colonna sinistra (distillazione)
  - Click 2: colonna destra (quantizzazione)
  - Click 3: box insight
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ DataCamp, 2024` — Knowledge distillation: tecnica consolidata per creare modelli compatti (GPT-4o → GPT-4o mini)
  - `² DeepSeek, 2025` — R1-Distill-Qwen-7B addestrato su ~800K sample generati da R1, outperforma GPT-4o su benchmark matematici
  - `³ LocalLLM / TDS, 2025` — Quantizzazione GGUF: FP32 → INT4 riduce la RAM necessaria di ~8x (7B: da 28GB a ~3.5GB)
- **Ricerca web**: ✅ Verificato — Distillazione confermata come tecnica standard (GPT-4o mini, R1-Distill). Quantizzazione INT4 confermata (llama.cpp, Ollama). DeepSeek R1-Distill-Qwen-7B: 28.9% AIME, 83.9% MATH, supera GPT-4o.
- **Note presentatore**: "Dopo le tre fasi di addestramento, ci sono due tecniche importanti per rendere i modelli utilizzabili nella pratica. La distillazione: un modello grande e costoso — il 'maestro' — genera migliaia di esempi di alta qualità, e un modello piccolo — l'apprendista — impara da quelli. Il risultato? DeepSeek ha creato un modello da 7 miliardi di parametri che batte GPT-4o su certi task. La quantizzazione: comprimere i numeri che compongono il modello da 32 bit a 4 bit. Come un JPEG: il file è 4 volte più piccolo, perdete un po' di dettaglio ma funziona. Grazie a queste tecniche, potete far girare modelli AI sul vostro portatile con Ollama."

---

### Slide 3.8 — Il meccanismo di Attenzione
- **Tipo**: `ANIM`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ ATTENZIONE"
  - Heading: "Come il modello 'guarda' il contesto"
  - Sotto-heading: "Il meccanismo di Attenzione — l'innovazione chiave dei Transformer¹"
  - Visualizzazione animata:
    - Una frase in alto: "Il gatto che avevo adottato dal rifugio l'anno scorso si è finalmente seduto sul mio tappeto nuovo"
    - Sotto, il modello sta generando il prossimo token dopo "nuovo"
    - Linee di "attenzione" colorate collegano la posizione corrente a varie parole della frase. Le linee hanno spessori diversi:
      - **Spessa e gold**: collegamento a "gatto" (soggetto principale)
      - **Spessa e gold**: collegamento a "seduto" (verbo principale)
      - **Media**: collegamento a "tappeto" (oggetto diretto)
      - **Sottile**: collegamento a "rifugio", "anno", ecc. (meno rilevanti)
    - Le parole con attenzione alta si illuminano
  - Analogia in basso: "Come leggere una frase ambigua in un libro: i tuoi occhi tornano indietro a cercare indizi. L'attenzione fa questo su tutto il contesto, simultaneamente."
- **Stellina**: Nessuna
- **Animazioni**:
  - Click 1: frase appare in alto
  - Click 2: il modello "punta" alla posizione finale (cursore lampeggiante dopo "nuovo")
  - Click 3: le linee di attenzione si disegnano animatamente dalla posizione corrente verso le parole rilevanti, con spessori diversi. Le parole target si illuminano.
  - Click 4: analogia in basso
  - Complessità: ★★★
- **Citazioni previste**:
  - `¹ Vaswani et al., 2017` — "Attention Is All You Need" — paper fondativo dei Transformer
- **Ricerca web**: ✅ Verificato — Attention Is All You Need (2017) è ancora il paper di riferimento. L'architettura Transformer con self-attention è alla base di tutti i modelli frontier. Miglioramenti (GQA, FlashAttention, MoE) sono ottimizzazioni, non sostituzioni.
- **Note presentatore**: "Quando il modello genera un token, non guarda solo le ultime parole. Guarda tutto il contesto e decide quali parti sono più rilevanti in quel momento. Questa è l'attenzione — l'innovazione del 2017 che ha reso possibili tutti gli LLM moderni. Nella frase 'Il gatto che avevo adottato dal rifugio l'anno scorso si è seduto sul mio tappeto nuovo', per generare ciò che viene dopo, il modello presta più attenzione a 'gatto' e 'seduto' che a 'rifugio' o 'anno'. È come avere un evidenziatore automatico che sottolinea le parti più importanti."

---

### Slide 3.9 — Implicazioni pratiche dell'attenzione
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ IMPLICAZIONI"
  - Heading: "Tutto il contesto influenza la risposta"
  - Sotto-heading: "Conseguenze pratiche per il vostro lavoro quotidiano"
  - 4 bullet con gold dots:
    - **System prompt** — Influenza ogni singola risposta. È come il brief per un freelancer: più è chiaro, migliore è il risultato.
    - **Ordine** — L'ordine in cui presentate le informazioni conta. Info all'inizio e alla fine pesano di più¹.
    - **Risposte precedenti** — Se il modello "sbaglia" e non lo correggete, continuerà su quella strada. Ogni risposta diventa contesto per la successiva.
    - **Rumore nel contesto** — Informazioni irrilevanti o contraddittorie degradano la qualità. Meno è meglio, se è rilevante.
  - Box in basso con regola d'oro: "Il modello non ha 'intenzioni': segue segnali nel contesto. Ordine, salienza, esempi e vincoli cambiano la traiettoria."
- **Stellina**: Nessuna
- **Animazioni**: Reveal sequenziale dei 4 bullet al click, poi box — ★☆☆
- **Citazioni previste**:
  - `¹ Liu et al., 2024` — "Lost in the Middle" — i modelli prestano più attenzione a inizio e fine del contesto
- **Ricerca web**: ✅ Verificato — "Lost in the Middle" (Liu et al., 2024) è lo studio di riferimento su questo fenomeno. Confermato e replicato.
- **Note presentatore**: "Quattro cose da ricordare quando lavorate con un LLM. Uno: il system prompt è il brief — scrivetelo bene. Due: l'ordine conta — mettete le cose importanti all'inizio o alla fine. Tre: se il modello sbaglia e non lo correggete, quel errore diventa parte del contesto e si amplifica. Quattro: più roba inutile mettete nel contesto, peggiore sarà la risposta. Il contesto non è una discarica — è uno strumento di precisione."

---

### Slide 3.10 — Allucinazioni: cosa sono
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ ALLUCINAZIONI"
  - Heading: "Quando il modello inventa"
  - Sotto-heading: "Informazioni plausibili ma false"
  - Layout split:
    - **Colonna sinistra — Cosa sono**:
      - "Fatti inventati, citazioni inesistenti, dati fabbricati"
      - "Non è un bug raro — è una modalità normale¹"
      - "Conseguenza diretta del next-token: il modello sceglie token probabili, non token veri"
    - **Colonna destra — Perché succedono**:
      - "Il modello non ha un database di fatti. Ha pattern statistici"
      - "Se non ha abbastanza info, riempie i buchi con token probabili"
      - "Non 'sa di non sapere' in modo affidabile²"
  - Box dati in basso: "Modelli frontier 2025-26: ~3-10% di allucinazioni su fatti specifici³, in calo dal ~15-25% dei modelli 2022-23"
- **Stellina**: `dubbioso:pensieroso.png` — piccola, a lato del heading (tema: dubbio, errore)
- **Animazioni**:
  - Click 1: heading + colonna "cosa sono"
  - Click 2: colonna "perché succedono"
  - Click 3: box dati in basso
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ IBM / Anthropic, 2025` — Allucinazioni come proprietà intrinseca dei modelli generativi
  - `² OpenAI, 2024` — SimpleQA benchmark: GPT-4o ~38% corretto su domande fattuali semplici
  - `³ Stima industria, 2025` — Riduzione progressiva delle allucinazioni nei modelli frontier
- **Ricerca web**: ✅ Verificato — SimpleQA (OpenAI) mostra che anche modelli frontier hanno margini di errore significativi. I reasoning model (o3, Claude con extended thinking) riducono ma non eliminano le allucinazioni.
- **Note presentatore**: "Ecco il lato oscuro. Le allucinazioni non sono un difetto occasionale — sono una conseguenza del meccanismo di base. Il modello genera token probabili, non token veri. Se non ha informazioni sufficienti, riempie i buchi con roba che suona bene ma è inventata. I modelli di oggi sono migliorati parecchio — siamo passati dal 15-25% di errori nei primi ChatGPT a circa 3-10% nei modelli frontier — ma il problema non è risolto."

---

### Slide 3.11 — Allucinazioni: implicazioni per il lavoro
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ DIFESE"
  - Heading: "Come difendersi dalle allucinazioni"
  - Sotto-heading: "Regole operative per il team"
  - 5 bullet con gold dots e icone:
    - 🔍 **Mai fidarsi ciecamente** — Verificare sempre fatti, numeri, date, citazioni prodotti dall'LLM
    - 📎 **Usare RAG** — Ancorare le risposte a documenti verificabili (ne parleremo nel Blocco 5)
    - 📋 **Progettare con verifica** — Nei prodotti AI: mostrare le fonti, permettere audit, indicare il livello di certezza
    - 💬 **"Non lo so" è OK** — Un "non ho informazioni sufficienti" è molto meglio di un'invenzione
    - 🗣️ **Comunicare i limiti** — Ai clienti, dire onestamente cosa il sistema può e non può fare
  - Box regola in basso: "Eloquenza ≠ accuratezza. Ricordate il Blocco 0."
- **Stellina**: Nessuna (slide densa con icone)
- **Animazioni**: Reveal sequenziale dei 5 bullet al click, poi box — ★☆☆
- **Citazioni previste**: Nessuna (raccomandazioni operative, non affermazioni fattuali)
- **Note presentatore**: "Cinque regole. Uno: mai fidarsi. Due: quando possibile, date al modello i documenti su cui basarsi — RAG, ne parleremo. Tre: se progettate prodotti AI, mettete sempre le fonti visibili. Quattro: insegnate al sistema a dire 'non lo so'. Cinque: siate onesti con i clienti. E ricordate la prima slide di oggi: eloquenza non significa accuratezza."

---

### Slide 3.12 — Multimodalità
- **Tipo**: `CONTENT`
- **Gradiente**: `--slide-bg-mint`
- **Contenuto**:
  - Section label: "★ OLTRE IL TESTO"
  - Heading: "Non solo parole"
  - Sotto-heading: "I modelli moderni vedono, ascoltano e generano"
  - Tabella visiva (layout griglia con icone):

    |  | Claude | GPT-4o/5 | Gemini 2.5 |
    |---|---|---|---|
    | 📝 Testo | ✅ In+Out | ✅ In+Out | ✅ In+Out |
    | 🖼️ Immagini | ✅ Input | ✅ In+Out¹ | ✅ In+Out |
    | 🎤 Audio | ❌ | ✅ In+Out² | ✅ In+Out |
    | 🎬 Video | ❌ | ✅ Limitato | ✅ Fino a 1h+³ |
    | 💻 Codice | ✅ In+Out | ✅ In+Out | ✅ In+Out |

  - Box pratico in basso: "Potete dare a Claude uno screenshot di un design e chiedergli di generare il codice. Figma Make si basa esattamente su questo."
- **Stellina**: `ascolta.png` — piccola, accanto al heading (tema: multimodalità, input diversi)
- **Animazioni**:
  - Click 1: heading + sotto-heading
  - Click 2: tabella si popola riga per riga (animazione build)
  - Click 3: box pratico
  - Complessità: ★☆☆
- **Citazioni previste**:
  - `¹ OpenAI, 2025` — GPT-4o con generazione nativa di immagini (marzo 2025)
  - `² OpenAI, 2024` — GPT-4o audio nativo real-time con espressione emotiva
  - `³ Google, 2025` — Gemini 2.5 Pro comprensione video fino a 1+ ora
- **Ricerca web**: ✅ Verificato — GPT-4o generazione immagini nativa da marzo 2025. Audio real-time confermato. Gemini leader per video understanding. Claude resta text+vision in input, text in output.
- **Note presentatore**: "I modelli moderni non lavorano solo con testo. Come vedete nella tabella, GPT-4o può generare immagini e audio nativamente, Gemini può analizzare video di un'ora. Claude si concentra su testo e visione — eccelle nel ragionamento e nell'uso di strumenti, che è il focus di MemorAIz. La cosa pratica per voi: potete dare al modello screenshot di design, foto di whiteboard, documenti scansionati, e ottenere analisi, codice, o testo strutturato."

---

### Slide 3.13 — Riepilogo del blocco
- **Tipo**: `SUMMARY`
- **Gradiente**: `--slide-bg-default`
- **Contenuto**:
  - Section label: "★ TAKEAWAY"
  - Heading grande: "Il modello mentale completo"
  - Sotto-heading: "Come funziona un LLM, in 6 concetti"
  - 6 punti in layout compatto (2 colonne × 3 righe):
    - **① Token** — L'LLM legge frammenti, non parole. I limiti e i costi si misurano in token.
    - **② Next-token** — Tutto emerge dalla predizione ripetuta del prossimo token.
    - **③ Temperatura** — Il termostato creatività/precisione. Stessa distribuzione, scelte diverse.
    - **④ Tre fasi** — Pre-training (conoscenza) → SFT (formato) → RL (allineamento).
    - **⑤ Attenzione** — Il modello guarda tutto il contesto. L'ordine e la qualità del contesto contano.
    - **⑥ Allucinazioni** — Token probabili ≠ token veri. Verificare sempre.
  - Box bridge in basso: "Nel prossimo blocco: come sfruttare tutto questo nella pratica → Context Engineering"
- **Stellina**: `super.png` — piccola, in basso a destra (superpotere: avete capito il meccanismo!)
- **Animazioni**: Build rapido dei 6 punti + box bridge — ★☆☆
- **Citazioni previste**: Nessuna (riepilogo senza dati nuovi)
- **Note presentatore**: "Sei concetti. Se li avete capiti, avete capito l'essenziale di come funziona un LLM. Token: non parole, ma frammenti. Next-token: il meccanismo unico ripetuto migliaia di volte. Temperatura: il controllo della creatività. Tre fasi: conoscenza, formato, allineamento. Attenzione: il modello vede tutto il contesto. Allucinazioni: probabile non significa vero. Con questi sei concetti in testa, siete pronti per la parte pratica."

---

## Riepilogo tecnico del blocco

| Aspetto | Dettaglio |
|---------|-----------|
| Slide totali | 15 (aggiunta slide 3.7b: distillazione e quantizzazione) |
| Animazioni ★☆☆ | 6 slide (titolo, distillazione/quantizzazione, implicazioni attenzione, allucinazioni cosa, difese, multimodalità, summary) |
| Animazioni ★★☆ | 5 slide (tokenizzazione, pre-training, SFT, RL, schema 3 fasi) |
| Animazioni ★★★ | 3 slide (next-token prediction, temperatura/slider, meccanismo attenzione) |
| Stelline usate | `conoscenza.png` (3.0), `lampadina.png` (3.2), `globo.png` (3.4), `dubbioso:pensieroso.png` (3.10), `ascolta.png` (3.12), `super.png` (3.13) |
| Gradienti | Mint (3.0, 3.2, 3.4, 3.6, 3.8, 3.10, 3.12), Default (3.1, 3.3, 3.5, 3.7, 3.9, 3.11, 3.13) — alternanza |
| Ricerca web | Tokenizzazione, context window, 3 fasi training (RLHF/DPO/GRPO), attenzione, allucinazioni (SimpleQA), multimodalità |

---

## Dipendenze e note

- **Prerequisiti**: Il Blocco 2 è prerequisito obbligatorio — le slide 2.3 (self-supervised) e 2.5-2.8 (reti neurali, pesi, backprop) costruiscono le basi per questo blocco.
- **Sequenza narrativa**: Le slide 3.4-3.7 (le 3 fasi) formano una sequenza narrativa continua. Il modello visivo si evolve da slide a slide (sfera caotica → ordinata → raffinata). **Non possono essere riordinate.**
- **Animazioni "hero"**: Le 3 animazioni ★★★ sono il cuore visivo del blocco:
  - 3.2 (next-token prediction): la più importante — fa capire il meccanismo base
  - 3.3 (temperatura/slider): la più interattiva — se possibile, rendere lo slider davvero trascinabile
  - 3.8 (attenzione): la più elegante — le linee di attenzione con spessori diversi sono molto efficaci visivamente
- **Ponte verso il Blocco 4**: La slide 3.9 (implicazioni attenzione) anticipa il Blocco 4 (Context Engineering). La slide 3.13 lo dichiara esplicitamente.
- **Ponte verso il Blocco 5**: La slide 3.11 (difese allucinazioni) anticipa RAG (Blocco 5).
- **Dati aggiornati utilizzati**:
  - Vocabolari tokenizer: GPT-4 ~200K, Gemini ~256K, Claude non pubblico
  - Context window: Claude 200K, GPT-4o 128K, Gemini 2.5 Pro 1M, Llama 4 Scout 10M (claimed)
  - Training data: Llama 4 30T+ token (Meta AI Blog)
  - Costi: GPT-5 ~$500M (Epoch AI), DeepSeek V3 $5.6M (Interconnects.ai)
  - Allineamento: RLHF standard, DPO ampiamente adottato, GRPO da DeepSeek, RLAIF/Constitutional AI da Anthropic
  - Allucinazioni: SimpleQA benchmark (GPT-4o ~38% corretto), stima industria 3-10% per frontier
  - Multimodalità: GPT-4o generazione immagini nativa (marzo 2025), Gemini video 1h+, Claude text+vision
- **Nota sulla multimodalità**: La tabella nella slide 3.12 potrebbe necessitare aggiornamento al momento della realizzazione delle slide — il panorama evolve rapidamente. Verificare lo stato di GPT-5 e Gemini 3 prima di finalizzare.
- **Nota sul tono**: Questo è il blocco più tecnico — mantenere il tono accessibile è la sfida principale. Le analogie (biblioteca di Babele, cuoco, cameriere, evidenziatore) sono il veicolo principale per la comprensione.

---

## Fonti consultate

- Tokenizzazione: OpenAI tiktoken docs, Google AI docs, studi empirici su efficienza multilingue
- Context window: Anthropic docs (Claude 200K), OpenAI (GPT-4o 128K), Google (Gemini 2.5 Pro 1M), Meta AI Blog (Llama 4 Scout 10M)
- Training pipeline: Sebastian Raschka "State of LLMs 2025", InstructGPT paper (Ouyang et al., 2022), DPO paper (Rafailov et al., 2023)
- Allineamento: Anthropic Constitutional AI paper, DeepSeek blog (GRPO), Klizos LLM training methodologies
- Attenzione: "Attention Is All You Need" (Vaswani et al., 2017), FlashAttention papers, GQA papers
- Allucinazioni: OpenAI SimpleQA benchmark, IBM LLM docs, stima industria da multiple fonti
- Multimodalità: OpenAI announcements (GPT-4o image gen, marzo 2025), Google I/O 2025 (Gemini), Meta AI Blog (Llama 4 multimodal)
