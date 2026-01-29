from retriever import retrieve as vector_search
from bm25_search import bm25_search


def hybrid_search(query):
    vec_results = vector_search(query, k=3)
    bm25_results = bm25_search(query, k=3)

    # Merge and remove duplicates (keep order)
    combined = list(dict.fromkeys(vec_results + bm25_results))

    return combined
