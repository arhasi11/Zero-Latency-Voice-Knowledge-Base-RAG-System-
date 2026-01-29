import asyncio
import time

from asr import stream_transcript
from rag import rewrite_query, add_to_history
from hybrid_search import hybrid_search
from reranker import rerank
from filler import filler_response
from voice_postprocess import voice_optimize


async def slow_rerank(query, docs):
    # Simulate slow cross-encoder reranker
    return rerank(query, docs)  # returns a STRING (best document)


async def handle_query(full_text):
    start_time = time.time()

    print("\nUser said:")
    print(full_text)

    # 1️⃣ ASR streaming (partial transcripts)
    partials = stream_transcript(full_text)

    # 2️⃣ 🔥 SPECULATIVE EXECUTION
    # Start RAG on FIRST meaningful partial
    first_partial = partials[0]

    rewritten_query = rewrite_query(first_partial)
    add_to_history(full_text)

    print("\nRewritten query:")
    print(rewritten_query)

    # 3️⃣ FAST hybrid retrieval (vector + BM25)
    docs = hybrid_search(rewritten_query)

    # 4️⃣ SLOW reranker runs in parallel
    rerank_task = asyncio.create_task(
        slow_rerank(rewritten_query, docs)
    )

    # 5️⃣ Immediate filler voice output (TTFB < 800ms)
    print("\nVOICE OUTPUT (immediate):")
    print(filler_response())

    # 6️⃣ Wait for reranker to finish
    final_doc = await rerank_task   # ✅ single document STRING

    # 7️⃣ Voice-optimized final response (Task C)
    print("\nVOICE-OPTIMIZED OUTPUT:")
    spoken_chunks = voice_optimize(final_doc)

    for chunk in spoken_chunks:
        print("🔊", chunk)

    print(
        f"\nTTFB: {(time.time() - start_time) * 1000:.0f} ms"
    )


if __name__ == "__main__":
    query = "How do I reset the second power module?"
    asyncio.run(handle_query(query))
