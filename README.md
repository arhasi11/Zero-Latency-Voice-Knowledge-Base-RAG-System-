# Zero-Latency Voice Knowledge Base (RAG System)

## Overview
This project implements a zero-latency, voice-based Retrieval-Augmented Generation (RAG) system for a CCaaS-style Voice AI agent.  
The system answers complex hardware troubleshooting questions by querying large technical manuals (1000+ pages) while maintaining a sub-800ms Time-to-First-Byte (TTFB) for audio output.

The key idea is to optimize perceived latency using parallel execution and speculative inference instead of a traditional sequential pipeline.

---

## Problem Statement
Voice AI agents must respond quickly while reasoning over large technical documentation.  
A linear pipeline (ASR → RAG → LLM → TTS) introduces unacceptable latency for real-time conversations.

This project solves that problem by overlapping speech recognition, retrieval, reranking, and speech synthesis.

---

## Architecture

Traditional Pipeline (Slow):
ASR → RAG → LLM → TTS

Proposed Pipeline (Fast):
Streaming ASR → Parallel RAG Prefetch + Query Rewriting → Hybrid Retrieval → Async Reranking → Voice-Optimized LLM → Streaming TTS

The system starts retrieval as soon as partial speech is available and produces early audio output while heavy components run asynchronously.

---

## Core Features

### 1. Parallelized & Speculative RAG
- Uses streaming ASR to obtain partial transcripts
- Triggers RAG prefetch before speech completion
- Overlaps computation to reduce end-to-end latency

---

### 2. Context-Aware Query Rewriting
User queries containing references like:
"And what about the second one?"

are rewritten into fully explicit queries using conversation history before hitting the vector database.

This significantly improves retrieval accuracy for follow-up questions.

---

### 3. Hybrid Search with Reranking
- Vector search using FAISS for semantic similarity
- BM25 keyword search for technical terminology
- Combined results are reranked using a cross-encoder

This approach improves precision for complex, multi-constraint hardware queries.

---

### 4. Latency Masking with Filler Speech
Cross-encoder rerankers are computationally expensive.

To maintain low perceived latency:
- A short filler response is synthesized immediately
- The final answer replaces the filler once reranking completes

This keeps audio TTFB within SLA while preserving answer quality.

---

### 5. Voice-Optimized Answer Generation
Raw RAG output is transformed into spoken English:
- Short sentences
- Simpler vocabulary
- Acronym expansion
- Phonetic pronunciation for technical terms

This improves speech naturalness and reduces TTS synthesis time.

---

## Latency Breakdown (Approximate)

| Component | Latency |
|---------|--------|
| Partial ASR transcript | ~250 ms |
| Hybrid retrieval | ~120 ms |
| Filler TTS start | ~400 ms |
| Final answer TTS | ~650–750 ms |

Observed audio TTFB: ~450–600 ms

---

## Failure Handling
- If reranking exceeds a timeout threshold, the system falls back to top-k hybrid retrieval results
- Ensures latency SLA is maintained under load or degraded conditions

---

## Tech Stack
- ASR (STT): Whisper (Streaming) / Groq
- LLM: Groq (LLaMA-3 / Mixtral)
- Embeddings: BGE / MiniLM
- Vector Store: FAISS
- Keyword Search: BM25
- Reranker: MiniLM Cross-Encoder
- TTS: Coqui TTS / ElevenLabs (Free Tier)
- Backend: FastAPI with asyncio

---

## Key Insight
The system optimizes perceived latency by overlapping ASR, retrieval, reranking, and TTS using speculative execution rather than waiting for sequential completion.

---

## Conclusion
This project demonstrates a production-oriented Voice RAG system that balances low latency, high retrieval accuracy, and natural conversational speech output.  
The design reflects real-world CCaaS Voice AI constraints and prioritizes user experience.
