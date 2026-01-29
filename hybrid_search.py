from retriever import vector_search
from bm25_search import bm25_search


def hybrid_search(query, k=3):
    """
    Hybrid retrieval using:
    - Vector search (semantic recall)
    - BM25 search (keyword precision)
    """

    vec_results = vector_search(query, k=k)
    bm25_results = bm25_search(query, k=k)

    # Merge and remove duplicates while preserving order
    combined = list(dict.fromkeys(vec_results + bm25_results))

    return combined
