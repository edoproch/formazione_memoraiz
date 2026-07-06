"""
Genera vectors.tsv e metadata.tsv per la demo live con il TensorFlow Embedding
Projector (projector.tensorflow.org), usata nel Blocco 5 - Embeddings & RAG
(slide 5.5 - "Vedere l'invisibile").

150 parole italiane suddivise in 5 categorie semantiche nettamente distinte
(30 per categoria), pensate per formare cluster densi e ben visibili una
volta proiettate in 3D.

Uso:
    python3 generate_embeddings.py

Richiede la variabile OPENAI_API_KEY in .env.local nella root del progetto.
"""

import os
import sys
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

PROJECT_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = Path(__file__).resolve().parent
EMBEDDING_MODEL = "text-embedding-3-small"

# (parola, categoria) - 5 cluster semantici x 30 parole, scelti per essere
# il più possibile distinti tra loro (poco overlap semantico) ed evitando
# omonimi rischiosi (es. "panda" = anche auto Fiat, "tasso" = anche animale).
WORDS = [
    ("cane", "Animali"), ("gatto", "Animali"), ("leone", "Animali"), ("elefante", "Animali"),
    ("delfino", "Animali"), ("aquila", "Animali"), ("tigre", "Animali"), ("orso", "Animali"),
    ("coniglio", "Animali"), ("cavallo", "Animali"), ("gallina", "Animali"), ("mucca", "Animali"),
    ("pecora", "Animali"), ("capra", "Animali"), ("lupo", "Animali"), ("volpe", "Animali"),
    ("scoiattolo", "Animali"), ("topo", "Animali"), ("serpente", "Animali"), ("coccodrillo", "Animali"),
    ("giraffa", "Animali"), ("zebra", "Animali"), ("canguro", "Animali"), ("koala", "Animali"),
    ("renna", "Animali"), ("gufo", "Animali"), ("pinguino", "Animali"), ("tartaruga", "Animali"),
    ("balena", "Animali"), ("squalo", "Animali"),

    ("pizza", "Cucina italiana"), ("pasta", "Cucina italiana"), ("risotto", "Cucina italiana"),
    ("tiramisù", "Cucina italiana"), ("lasagne", "Cucina italiana"), ("gelato", "Cucina italiana"),
    ("espresso", "Cucina italiana"), ("parmigiano", "Cucina italiana"), ("focaccia", "Cucina italiana"),
    ("tortellini", "Cucina italiana"), ("cappuccino", "Cucina italiana"), ("prosciutto", "Cucina italiana"),
    ("mozzarella", "Cucina italiana"), ("ravioli", "Cucina italiana"), ("bruschetta", "Cucina italiana"),
    ("minestrone", "Cucina italiana"), ("polenta", "Cucina italiana"), ("panettone", "Cucina italiana"),
    ("cannoli", "Cucina italiana"), ("arancini", "Cucina italiana"), ("carbonara", "Cucina italiana"),
    ("bolognese", "Cucina italiana"), ("caprese", "Cucina italiana"), ("panna cotta", "Cucina italiana"),
    ("grissini", "Cucina italiana"), ("mortadella", "Cucina italiana"), ("pecorino", "Cucina italiana"),
    ("gnocchi", "Cucina italiana"), ("ribollita", "Cucina italiana"), ("limoncello", "Cucina italiana"),

    ("investimento", "Finanza"), ("bilancio", "Finanza"), ("fatturato", "Finanza"),
    ("dividendo", "Finanza"), ("mutuo", "Finanza"), ("borsa", "Finanza"), ("bonifico", "Finanza"),
    ("profitto", "Finanza"), ("budget", "Finanza"), ("tassazione", "Finanza"), ("obbligazione", "Finanza"),
    ("patrimonio", "Finanza"), ("capitale", "Finanza"), ("credito", "Finanza"), ("debito", "Finanza"),
    ("tasso d'interesse", "Finanza"), ("liquidità", "Finanza"), ("contabilità", "Finanza"),
    ("fatturazione", "Finanza"), ("assicurazione", "Finanza"), ("fondo pensione", "Finanza"),
    ("risparmio", "Finanza"), ("prestito", "Finanza"), ("ricavo", "Finanza"), ("costo", "Finanza"),
    ("imposta", "Finanza"), ("fattura", "Finanza"), ("contanti", "Finanza"), ("plusvalenza", "Finanza"),
    ("flusso di cassa", "Finanza"),

    ("calcio", "Sport"), ("tennis", "Sport"), ("pallacanestro", "Sport"), ("nuoto", "Sport"),
    ("ciclismo", "Sport"), ("maratona", "Sport"), ("arbitro", "Sport"), ("campionato", "Sport"),
    ("allenamento", "Sport"), ("squadra", "Sport"), ("pallavolo", "Sport"), ("rugby", "Sport"),
    ("golf", "Sport"), ("scherma", "Sport"), ("atletica", "Sport"), ("pugilato", "Sport"),
    ("pattinaggio", "Sport"), ("canottaggio", "Sport"), ("vela", "Sport"), ("pallanuoto", "Sport"),
    ("hockey", "Sport"), ("judo", "Sport"), ("karate", "Sport"), ("arrampicata", "Sport"),
    ("triathlon", "Sport"), ("podismo", "Sport"), ("pallamano", "Sport"), ("badminton", "Sport"),
    ("skateboard", "Sport"), ("surf", "Sport"),

    ("software", "Tecnologia"), ("algoritmo", "Tecnologia"), ("server", "Tecnologia"),
    ("database", "Tecnologia"), ("cloud", "Tecnologia"), ("intelligenza artificiale", "Tecnologia"),
    ("rete", "Tecnologia"), ("cybersicurezza", "Tecnologia"), ("hardware", "Tecnologia"),
    ("blockchain", "Tecnologia"), ("smartphone", "Tecnologia"), ("app", "Tecnologia"),
    ("browser", "Tecnologia"), ("firewall", "Tecnologia"), ("crittografia", "Tecnologia"),
    ("streaming", "Tecnologia"), ("router", "Tecnologia"), ("processore", "Tecnologia"),
    ("wifi", "Tecnologia"), ("chip", "Tecnologia"), ("robotica", "Tecnologia"),
    ("automazione", "Tecnologia"), ("programmazione", "Tecnologia"), ("big data", "Tecnologia"),
    ("machine learning", "Tecnologia"), ("chatbot", "Tecnologia"), ("interfaccia", "Tecnologia"),
    ("API", "Tecnologia"), ("GPU", "Tecnologia"), ("open source", "Tecnologia"),
]


def main():
    load_dotenv(PROJECT_ROOT / ".env.local")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OPENAI_API_KEY non trovata: controlla .env.local nella root del progetto.")

    words = [w for w, _ in WORDS]
    categories = [c for _, c in WORDS]

    client = OpenAI(api_key=api_key)
    print(f"Richiesta embedding per {len(words)} parole con {EMBEDDING_MODEL}...")
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=words)
    embeddings = np.array([d.embedding for d in response.data])
    print(f"Ricevuti {embeddings.shape[0]} vettori a {embeddings.shape[1]} dimensioni.")

    pca = PCA(n_components=3)
    coords = pca.fit_transform(embeddings)
    print(f"Varianza spiegata dalle prime 3 componenti PCA: {pca.explained_variance_ratio_.sum():.1%}")

    # Diagnostica: quanto bene le 5 categorie si separano nello spazio 3D proiettato.
    # Silhouette score in [-1, 1]: piu' alto = cluster piu' compatti e separati.
    score = silhouette_score(coords, categories)
    print(f"Silhouette score (separazione cluster nello spazio 3D): {score:.3f}")

    vectors_path = OUTPUT_DIR / "vectors.tsv"
    metadata_path = OUTPUT_DIR / "metadata.tsv"

    with open(vectors_path, "w") as f:
        for row in coords:
            f.write("\t".join(f"{v:.6f}" for v in row) + "\n")

    with open(metadata_path, "w") as f:
        f.write("Parola\tCategoria\n")
        for word, cat in zip(words, categories):
            f.write(f"{word}\t{cat}\n")

    print(f"Salvati {len(words)} punti in:\n  {vectors_path}\n  {metadata_path}")


if __name__ == "__main__":
    main()
