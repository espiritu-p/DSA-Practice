# System Design Coaching Log

Persistent record. Updated after every completed session.

---

## Baseline (2026-09-03)

**Relevant production experience:**
- SRE @ P&G — 3,000+ servers, Prometheus, Thanos, Grafana, Splunk, Puppet; SLO/error budget ownership
- Samsung — Kubernetes, Jenkins CI/CD, cloud orchestration UI, CNF/VNF topology
- AZ-900 certified; SRE Foundation + Practitioner certified

**Strengths going in:**
- Reliability engineering: SLOs, error budgets, observability, MTTR reduction
- Fleet automation at scale: Puppet, Prometheus alerting, auto-ticketing
- Deployment discipline: 97% change success rate over 3,000+ servers
- Containerized workloads: Kubernetes, Jenkins

**Gaps to close before October:**
- Database internals at interview depth (replication, sharding, CAP)
- Message queue / event streaming patterns (Kafka internals, saga pattern)
- AWS service landscape (background is Azure/Kubernetes-heavy)
- Structured mock design practice — frameworks and timing

---

## Sessions

### Session 1 — 2026-09-04 — Phase 1.1: Scale of numbers + estimation

**Format:** 3-question quiz (QPS estimation, latency orders of magnitude, storage estimation)

**What landed:**
- Latency ordering correct without prompting (memory < SSD < cross-continent)
- Storage estimation method correct (units × rate × time)

**Gaps found (all vocabulary/arithmetic, not reasoning):**
- Didn't know **DAU** (daily active users), **QPS** (queries/sec), **peak multiplier** (~2–3× average) — the three starting terms of every SD interview
- Latency numbers not yet memorized: memory ~100**ns** → SSD ~100**µs** → cross-continent ~100**ms** (each hop ~1000×; Jeff Dean's table)
- Storage math dropped ~100×: 200M tweets × 280B = 56 GB/day ≈ 20 TB/year (not 480MB)
- "What did you ignore" answer to internalize: **metadata, indexes (2–5×), replication (×3 for durability), media (dominates → PB-scale, not TB)**

**Key formulas to memorize:**
- `QPS = (DAU × actions/user) ÷ 86,400` (~100K sec/day)
- Storage ladder: KB → MB → GB → TB → PB (×1000 each)

**Drill assigned:** redo Q1 math + recite latency ladder from memory.

**Drill result:** QPS math ✅ (10M DAU × 10 actions ≈ 1K QPS via shortcut). Latency ladder ✅ with one label slip (said "RAM" for rung 2 — RAM *is* main memory; rung 2 is SSD). Payoff line learned: "disk is 1000× slower than memory, so we cache; cross-continent is 1000× slower than disk, so we use CDNs."

**Follow-up Q&A:** caching (copy in fast memory, e.g. Redis — deep dive in SD 2.6) and CDN (copies on servers near the user, e.g. Cloudflare — deep dive in SD 1.4). Both framed as the same idea at different distances.

**Status: Phase 1.1 ✅ complete**

---

> Coaching protocol and session rules live in [`CLAUDE.md`](../CLAUDE.md) at the repo root.
