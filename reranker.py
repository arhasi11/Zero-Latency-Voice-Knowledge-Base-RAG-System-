from sentence_transformers import CrossEncoder

# Cross-encoder = slow but accurate
reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query, docs):
    pairs = [(query, doc) for doc in docs]
    scores = reranker_model.predict(pairs)

    ranked = sorted(
        zip(scores, docs),
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for _, doc in ranked]
