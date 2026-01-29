import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


# Load FAISS index built offline by rag.py
with open("rag_store.pkl", "rb") as f:
    index, chunks = pickle.load(f)

# Same embedding model used during ingestion
model = SentenceTransformer("all-MiniLM-L6-v2")


def vector_search(query, k=3):
    """
    Semantic vector search using FAISS.
    """

    query_embedding = model.encode([query])
    _, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    return [chunks[i] for i in indices[0]]
