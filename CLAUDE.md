# Interview Prep — AI Instructions

Rules for every session in this repo. Read this file at the start of every session
before touching any coaching log or plan file.

---

## Session Start Checklist

Every session, in order:

1. Read `DSA/COACHING.md` — restore battle plan, DSA topic status, last session state
2. Read `System-Design/COACHING.md` — restore last SD session and debrief
3. Read `AI-Engineering/COACHING.md` — restore last AI session and debrief
4. Surface today's plan across all three tracks before doing anything else

The user may be on a different machine with a fresh clone. Never assume prior
in-memory state carries over — the coaching logs are the source of truth.

---

## Standing Coaching Rules

### All tracks
1. **Best interview answer always.** After critiquing any response, close with the
   exact phrasing an interviewer wants to hear. Format: What landed → What was
   wrong/missing → Best interview answer.
2. **Plan checks are cross-track.** Any request to check the plan or today's
   progress must report status across all three tracks — DSA, System Design,
   and AI Engineering.
3. **Clarifying questions welcome mid-session.** Log as a teachable moment, not a gap.

### DSA review rubric (apply to every submitted solution)
1. **Correctness first** — loop bounds, off-by-one, edge cases (empty, single element, all-invalid input)
2. **Python idiom** — snake_case vars, no redundant `else` after `return`, no parens on `while`/`if`
3. **Space/time tradeoffs** — name the variant not written (e.g. O(n) copy vs O(1) in-place)
4. **Talk-aloud check** — restate + edge cases → plan → complexity → variant, unprompted
5. **Workflow** — user pastes solution → review vs rubric → user revises → only then commit/push

---

## End-of-Session Checklist

Before every commit and push, verify these files are current:

| File | What to check |
|------|---------------|
| `README.md` | LeetCode solved count, track statuses |
| `DSA/LeetCode/README.md` | Problem list and topic counts |
| `System-Design/Concepts/README.md` | Session status per concept file |
| `System-Design/Case-Studies/README.md` | Mock session statuses |
| `AI-Engineering/Concepts/README.md` | Session status per concept file |
| `AI-Engineering/Exercises/README.md` | Coding exercise statuses |

Then commit with Conventional Commits format and push to master.

---

## Repo Structure (quick reference)

```
Interview-Prep/
├── CLAUDE.md                        ← you are here
├── README.md                        ← public-facing progress
├── DSA/
│   ├── COACHING.md                  ← session log + battle plan + baseline
│   └── LeetCode/                    ← solutions by topic
├── System-Design/
│   ├── PLAN.md                      ← phase curriculum
│   ├── COACHING.md                  ← session log + debriefs
│   ├── Concepts/                    ← one .md per topic
│   └── Case-Studies/                ← mock design write-ups
└── AI-Engineering/
    ├── PLAN.md                      ← phase curriculum
    ├── COACHING.md                  ← session log + debriefs
    ├── Concepts/                    ← one .md per topic
    └── Exercises/                   ← from-scratch implementations
```
