from rank_bm25 import BM25Okapi

# Example corpus (replace with your KB chunks)
DOCUMENTS = [
    "To reset the power module, power off the system and wait 30 seconds.",
    "The second power module is hot-swappable.",
    "Resetting the PSU requires disconnecting the power cable.",
    "Do not reset the power module while the system is running."
]

tokenized_docs = [doc.split() for doc in DOCUMENTS]
bm25 = BM25Okapi(tokenized_docs)


def bm25_search(query, k=3):
    tokenized_query = query.split()
    scores = bm25.get_scores(tokenized_query)

    # 🔥 Sort by score DESCENDING
    ranked = sorted(
        zip(scores, DOCUMENTS),
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for _, doc in ranked[:k]]
