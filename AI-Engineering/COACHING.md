# AI Engineering Coaching Log

Persistent record for cross-session coaching. Updated after every completed session.

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

### Session 1 — 2026-09-04 — Phase 1.1: Transformer architecture ⏳ Reading assigned

**Reading:** Jay Alammar — *The Illustrated Transformer* (jalammar.github.io/illustrated-transformer/). First pass, skip fine math.

**Quiz prep (explain in one sentence each, quizzed next session):**
1. Encoder vs decoder stack (GPT-style = decoder-only)
2. Why residual connections exist (gradient flow in deep stacks)
3. What layer norm does (stabilize per-token activations)
4. What the FFN adds after attention (per-token nonlinearity; most parameters)
5. Where attention fits (mixes info across tokens; FFN is per-token)

Note: attention deep-dive (Q/K/V) is deferred to Phase 1.2 — don't rabbit-hole.

---

## How to Update This File

After each session, tell me:
- What phase/session we covered
- Which probing questions you answered well vs. struggled with
- Whether you completed the coding exercise

I'll log the debrief and update PLAN.md progress tracker.
