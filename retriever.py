from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from kb import DOCUMENTS

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(DOCUMENTS)
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def retrieve(query, k=1):
    q_emb = model.encode([query])
    _, indices = index.search(np.array(q_emb), k)
    return [DOCUMENTS[i] for i in indices[0]]
