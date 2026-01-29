from sentence_transformers import CrossEncoder
import time

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    time.sleep(0.5)  # simulate latency
    pairs = [[query, d] for d in docs]
    scores = reranker.predict(pairs)
    return docs[scores.argmax()]
