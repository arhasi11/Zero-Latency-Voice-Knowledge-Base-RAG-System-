from rank_bm25 import BM25Okapi
from kb import DOCUMENTS

# Tokenize documents once
tokenized_docs = [doc.lower().split() for doc in DOCUMENTS]

bm25 = BM25Okapi(tokenized_docs)


def bm25_search(query, k=3):
    tokenized_query = query.lower().split()
    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(
        zip(scores, DOCUMENTS),
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for _, doc in ranked[:k]]
