# AI Engineering Coaching Log

Persistent record for cross-session coaching. Updated after every completed session.

---
## Coaching Protocol

**Standing rules — apply every session, every phase:**

1. **Best interview answer included always.** After critiquing your response, I always close with the exact phrasing an interviewer would want to hear. Use it as the benchmark to calibrate your own answer against.
2. **Critique structure:** What landed → What was wrong/missing → Best interview answer.
3. **Clarifying questions welcome mid-session.** If a concept is unclear, ask before moving on — logged as a teachable moment, not a gap.
4. **Re-answer to lock in.** After critique, you can re-answer in your own words to confirm the concept is internalized. Encouraged but not required.

---


## Baseline (2026-09-03)

**Background:**
- SRE @ Procter & Gamble — autonomous agents in prod (LangGraph, LangChain, MCP)
- Authored Agent Skills as incident copilot across Claude, Copilot, Gemini
- 2× peer-reviewed NLP publications (Seq2Seq, multi-label classification)
- MS CS @ DLSU, 3.9 GPA

**Strengths going in:**
- Agentic patterns (LangGraph, MCP) from real production work
- NLP research background (sequence modeling, low-resource settings)
- SRE observability — can instrument and measure AI systems in prod

**Gaps to close before October:**
- LLM internals (attention, KV cache, scaling laws) — from-scratch explanation
- RAG pipeline design — chunking, reranking, hybrid search
- Eval methodology — metrics, LLM-as-judge, RAGAS
- PEFT stack — LoRA, QLoRA, DPO (classic DL background, not modern PEFT)
- Inference & serving — quantization, vLLM, speculative decoding
- Safety & alignment — RLHF, RLAIF, red-teaming

---

## Sessions

### Session 1 — 2026-09-04 — Phase 1.1: Transformer architecture ✅ Complete

**Reading:** Jay Alammar — *The Illustrated Transformer* (jalammar.github.io/illustrated-transformer/). Completed prior to session.

**Debrief:**

| Question | Performance | Notes |
|----------|-------------|-------|
| Q1 — Encoder vs decoder / GPT decoder-only | ⚠️ Weak | Correct direction; missed bidirectional vs causal attention distinction; GPT decoder-only rationale entirely absent |
| Q2 — Why residual connections exist | ⚠️ Weak | Described WHERE (add+norm), not WHY (gradient flow); conflated residual connections with layer norm; missed 2 per block |
| Gradient flow clarification | ✅ Good instinct | Asked before moving on — correct behavior; concept now understood |
| Q3 — What layer norm does | ❌ Wrong | Said 0–1 scaling (that's sigmoid/softmax); correct answer: zero mean, unit variance per token |
| Q4 — FFN role | ❌ Wrong | Said "next RNN" — no RNNs in transformers; missed per-token independence and parameter dominance |
| Q5 — Attention vs FFN | ⚠️ Partial | Correct that attention evaluates word-to-word relevance; missed the key contrast: attention=cross-token mixing, FFN=per-token transformation |

**Overall:** Directionally aware but precision not yet at interview level. Expected — these are LLM internals gaps identified at baseline. Right instincts, wrong mechanics. Needs one more pass on transformer block structure before 1.2.

**Concepts to re-read before Phase 1.2:**
- Residual connections: WHY (gradient flow) not just WHERE
- Layer norm: zero mean + unit variance (not 0–1 scaling)
- FFN: per-token, independent, ~2/3 of parameters, no RNNs

**Coding exercise:** Not yet attempted (Phase 1 exercise: implement scaled dot-product attention in NumPy — due after Phase 1.2).

---

### Session 2 — 2026-09-04 — Phase 1.2: Attention deep-dive (Q/K/V) 🔜 Up next

---

## How to Update This File

After each session, tell me:
- What phase/session we covered
- Which probing questions you answered well vs. struggled with
- Whether you completed the coding exercise

I'll log the debrief and update PLAN.md progress tracker.
