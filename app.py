import asyncio
from asr import stream_transcript
from rag import rewrite_query, add_to_history
from hybrid_search import hybrid_search
from reranker import rerank
from filler import filler_response
from voice_postprocess import voice_optimize


async def slow_rerank(query, docs):
    return rerank(query, docs)


async def handle_query(full_text):
    print("\nUser said:", full_text)

    # ASR streaming (simulated)
    partials = stream_transcript(full_text)

    # Use final stabilized transcript
    rewritten_query = rewrite_query(partials[-1])
    add_to_history(full_text)

    print("\nRewritten query:")
    print(rewritten_query)

    # FAST hybrid retrieval
    docs = hybrid_search(rewritten_query)

    # SLOW reranker (async)
    rerank_task = asyncio.create_task(
        slow_rerank(rewritten_query, docs)
    )

    # Immediate voice response
    print("\nVOICE OUTPUT (immediate):")
    print(filler_response())

    # Wait for reranker
    final_docs = await rerank_task

    print("\nVOICE-OPTIMIZED OUTPUT:")
    spoken_chunks = voice_optimize(final_docs[0])

    for chunk in spoken_chunks:
        print("🔊", chunk)


if __name__ == "__main__":
    query = "How do I reset the second power module?"
    asyncio.run(handle_query(query))
