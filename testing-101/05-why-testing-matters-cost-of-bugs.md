# 05 — Why Testing Matters: The Cost of Bugs

## 📈 The Cost-of-Bugs-Escaping Curve

There's a well-established idea in software engineering: **the later a bug is found, the more expensive it is to fix.** Not just "somewhat more" — often by orders of magnitude.

| Where the Bug Is Caught | Rough Cost | What Fixing It Involves |
|---|---|---|
| **Unit test (before commit)** | Minutes | Change a few lines, re-run the test, done |
| **Code review** | Minutes to hours | A conversation, a small revision |
| **Integration/QA environment** | Hours | Reproduce it, trace it across components, retest |
| **Production** | Hours to days (or worse) | Incident response, rollback or hotfix, root cause analysis, customer communication, on-call pages at 2am, potential reputational and financial damage |

A bug caught by a unit test *never leaves your machine*. A bug caught in production has already been experienced by real users, has potentially corrupted real data, and now requires a whole additional process — incident response — layered on top of the actual fix. The fix itself might still be one line of code. **Everything around it is what becomes expensive.**

This is the entire economic case for testing at the unit level: it's not about writing tests because it's "good practice" in the abstract — it's because **it is dramatically cheaper to catch a bug the moment it's introduced than to catch it after it's shipped.**

Two of software history's most well-documented disasters make this concrete.

---

## 🚀 Real Incident: Ariane 5 Flight 501 (1996)

The European Space Agency's Ariane 5 rocket exploded **37 seconds after launch** on its maiden flight, destroying a payload worth roughly $370 million.

The cause: a piece of guidance software was **reused from the earlier Ariane 4 rocket**, where it had worked correctly for years. That code converted a 64-bit floating-point number representing horizontal velocity into a 16-bit integer. On Ariane 4, the velocity values involved never came close to overflowing that 16-bit range. **Ariane 5 flew a different flight profile, with higher horizontal velocity — and the value overflowed.** The overflow triggered an unhandled exception, which crashed the guidance system, which caused the rocket to veer off course and self-destruct.

**What testing discipline would have caught this:** the reused module was never re-tested against Ariane 5's actual flight parameters — it was assumed to be safe because it had worked on a *different* system with *different* operating conditions. A test that fed this specific conversion function realistic Ariane 5 velocity values — a boundary/edge-case unit test — would have surfaced the overflow before a single rocket left the ground. This is a direct, real-world lesson in why "it worked before, in a similar system" is never a substitute for testing the actual code, under the actual conditions it will really run in.

---

## ☢️ Real Incident: Therac-25 (1985–1987)

The Therac-25 was a radiation therapy machine. Due to a **race condition** in its control software — combined with the removal of hardware safety interlocks that earlier models had relied on — the machine could, under a specific timing of operator inputs, deliver radiation doses **hundreds of times greater than intended**. At least six patients received massive overdoses, and several died as a direct result.

Earlier models of the machine had physical, hardware-based interlocks that made this scenario impossible regardless of what the software did. In the Therac-25, those hardware protections were removed, and the *software alone* was trusted to prevent an unsafe state — but the software had a timing-dependent bug that only manifested when an operator entered commands in a particular sequence, quickly. This bug had **not been caught** by the testing the software had undergone.

**What testing discipline would have caught this:** race conditions are notoriously hard to catch with a single "happy path" manual test — they depend on specific timing and sequences of input that a casual test run is unlikely to stumble into by chance. This is exactly the kind of scenario where deliberate, repeatable, automated tests — specifically written to simulate rapid or unusual input sequences — are far more likely to expose a bug than ad hoc manual testing ever would. It's also a stark, life-and-death illustration of why safety-critical software cannot rely on "it seemed to work when we tried it."

---

## 🧵 Tying It All Back Together

Look back across all five files in this module, and you'll see the same thread running through every one of them:

- **File 1:** Knight Capital lost $440M because no automated check verified system state before deployment.
- **File 2:** the *same* Knight Capital incident, seen again, shows why unit tests alone aren't enough — different bugs hide at different layers of the pyramid.
- **File 3:** tightly coupled, un-isolated tests erode trust in test suites altogether — the "boy who cried wolf" problem.
- **File 4:** an unmocked dependency on a live external API means the *first* time a failure path executes is often in production, live.
- **File 5:** Ariane 5 and Therac-25 show what happens when reused or safety-critical code isn't tested against realistic, edge-case conditions.

None of this is abstract "best practice for its own sake." **Every property we insisted on — isolated, independent, deterministic, no IO, one thing at a time — exists because violating each one, specifically, is what let a real incident happen.** That's the case for testing, made not by us, but by the history of the industry itself.

---

## 🚀 Challenge Task

Pick one of the five real incidents covered across this module (Knight Capital, Toyota, Google's flaky tests, the third-party API outage pattern, Ariane 5, or Therac-25). Write two or three sentences on which *specific* unit test property from File 1 (tests one thing, fast, independent, isolated, deterministic) — if it had been rigorously applied to the code involved — would most plausibly have caught the problem before it shipped.

No solution provided. Bring your answer to the walkthrough.
