import pickle
import faiss
from sentence_transformers import SentenceTransformer


def simple_split(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks


def ingest(documents):
    chunks = simple_split(documents)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    with open("rag_store.pkl", "wb") as f:
        pickle.dump((index, chunks), f)

    print(f"✅ Vector store created with {len(chunks)} chunks")


if __name__ == "__main__":
    with open("data/manual.txt", "r", encoding="utf-8") as f:
        ingest(f.read())
