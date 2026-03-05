<p align="center">
  <img src="images/logo.svg" alt="MemorAIz" width="220">
</p>

<h1 align="center">Formazione AI Interna</h1>

<p align="center">
  <strong>Un viaggio visivo e interattivo nell'Intelligenza Artificiale</strong><br>
  <em>Pensato per chi progetta esperienze, non per chi scrive codice.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/slide-~86-f5a623?style=flat-square&labelColor=1a1a4e" alt="Slide">
  <img src="https://img.shields.io/badge/durata-~3--4_ore-f5a623?style=flat-square&labelColor=1a1a4e" alt="Durata">
  <img src="https://img.shields.io/badge/pubblico-UX%2FUI_%26_Comunicazione-f5a623?style=flat-square&labelColor=1a1a4e" alt="Pubblico">
  <img src="https://img.shields.io/badge/lingua-italiano-f5a623?style=flat-square&labelColor=1a1a4e" alt="Lingua">
  <img src="https://img.shields.io/badge/licenza-CC_BY--NC--ND_4.0-f5a623?style=flat-square&labelColor=1a1a4e" alt="Licenza">
</p>

---

## Cosa troverai

Questo repository contiene un **deck di slide interattive** creato da [**Edoardo Procino**](https://www.linkedin.com/in/edoardo-procino-b7a236261/) per la formazione interna del team UX/UI e Comunicazione di [MemorAIz](https://memoraiz.com). L'obiettivo non e' insegnare a programmare, ma costruire un **linguaggio comune** sull'AI: capire come funziona, cosa puo' (e non puo') fare, e come lavorarci ogni giorno in modo consapevole.

Le slide sono pensate per essere **presentate**, non lette come un documento. Ogni concetto tecnico e' spiegato attraverso **analogie concrete, animazioni interattive e visualizzazioni step-by-step** — zero formule matematiche, zero prerequisiti informatici.

---

## Percorso formativo

Il deck e' organizzato in **9 blocchi** che costruiscono la comprensione in modo progressivo:

| # | Blocco | Cosa imparerai |
|:-:|--------|----------------|
| **0** | **Setup & Aspettative** | Perche' questa formazione, il concetto di "probabilistico vs deterministico", gli errori piu' comuni |
| **1** | **Storia & Mappa AI** | Dal Perceptron a GPT-4, la mappa AI ⊃ ML ⊃ Deep Learning ⊃ LLM, training vs inference |
| **2** | **Fondamenti ML** | Reti neurali, pesi, backpropagation — spiegati con animazioni, senza una formula |
| **3** | **Come funzionano gli LLM** | Token, predizione next-token, temperatura, le tre fasi di addestramento (pre-training, SFT, RLHF) |
| **4** | **Context Engineering** | Context window, prompt design, system prompt, few-shot, chain-of-thought, prompt injection |
| **5** | **Embeddings & RAG** | Spazi vettoriali, similarita' semantica, la pipeline RAG completa in 6 step |
| **6** | **Reasoning Models** | Chain-of-thought, modelli o1/o3, thinking budget, quando usarli e quando no |
| **7** | **Agenti AI** | Il loop agente, tool calling, MCP, orchestrazione multi-agente, sicurezza |
| **8** | **Checklist & Chiusura** | Albero decisionale interattivo, regole d'oro, template operativi |

---

## Come visualizzare le slide

### Online (GitHub Pages)

Le slide sono pubblicate e navigabili direttamente nel browser:

**[Apri la presentazione](https://edoproch.github.io/formazione_memoraiz/slides/)**

### In locale

```bash
git clone https://github.com/edoproch/formazione_memoraiz.git
```

Apri `slides/index.html` direttamente nel browser — non serve nessun server o installazione.

### Navigazione

| Comando | Azione |
|---------|--------|
| `→` / `Space` | Avanza di uno step |
| `←` | Torna indietro |
| `F` | Modalita' fullscreen |
| `Esc` | Torna alla panoramica |

---

## Struttura del progetto

```
formazione_memoraiz/
├── slides/                 ← Le slide HTML (un file per blocco)
│   ├── index.html          ← Master deck con navigazione tra blocchi
│   ├── 00-setup/
│   ├── 01-storia-mappa/
│   ├── ...
│   └── 09-checklist/
├── openspec/               ← Specifiche di pianificazione per ogni blocco
├── references/             ← Fonti web consultate e verificate
├── images/                 ← Logo MemorAIz e stelline mascotte
└── formazione-ai-outline.md ← Outline completo dei contenuti
```

---

## Per chi e' pensato

Questa formazione e' stata progettata per **designer UX/UI e professionisti della comunicazione** che lavorano in un contesto AI-first. Non richiede nessun background tecnico. L'obiettivo e' tripartito:

1. **Lavorare meglio** con gli strumenti AI-first
2. **Capire cosa si puo' vendere** (e cosa no) ai clienti
3. **Dialogare con il team tecnico** con un linguaggio comune

---

## Licenza

<p>
  <img src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png" alt="CC BY-NC-ND 4.0">
</p>

Questo materiale e' distribuito con licenza [**Creative Commons Attribuzione - Non commerciale - Non opere derivate 4.0 Internazionale (CC BY-NC-ND 4.0)**](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it).

In pratica:
- **Puoi** consultare, leggere e condividere questo materiale liberamente
- **Devi** citare [Edoardo Procino](https://www.linkedin.com/in/edoardo-procino-b7a236261/), [MemorAIz](https://memoraiz.com) e [Francesca Tucci](https://www.linkedin.com/in/francesca-tucci-a5740631a/) come autrice delle illustrazioni
- **Non puoi** modificarlo, adattarlo o creare opere derivate
- **Non puoi** usarlo per scopi commerciali

---

<p align="center">
  <img src="images/stars/lampadina.png" width="64" alt="Stellina lampadina">
  <br><br>
  <strong>Realizzato da <a href="https://www.linkedin.com/in/edoardo-procino-b7a236261/">Edoardo Procino</a> per <a href="https://memoraiz.com">MemorAIz</a></strong><br>
  <strong>Illustrazioni mascotte</strong> di <a href="https://www.linkedin.com/in/francesca-tucci-a5740631a/">Francesca Tucci</a><br>
  <em>Perche' capire l'AI non dovrebbe richiedere una laurea in informatica.</em>
</p>
