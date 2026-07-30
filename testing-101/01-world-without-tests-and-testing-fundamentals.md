# 01 — A World Without Tests & Testing Fundamentals

## 🌍 A World Without Tests

Imagine you're a developer at a company with zero tests. No unit tests, no integration tests, nothing. Every deploy is a leap of faith. Here's what that world actually looks like day to day:

- **Every change is a gamble.** You touch one method, and you have no idea what else it might have broken, because nothing tells you.
- **Refactoring becomes terrifying.** "Don't touch that, we don't know why it works" becomes an actual engineering principle.
- **Regressions ship silently.** A bug fixed six months ago quietly comes back, and nobody notices until a customer does.
- **Manual testing eats the whole team's time**, and even then, humans miss things machines wouldn't.

This isn't hypothetical. It's exactly what happened to a company called **Knight Capital**.

> ### 💥 Real Incident: Knight Capital Group (2012)
> Knight Capital was one of the largest traders in U.S. equities. On August 1, 2012, they deployed new trading software to their production servers. The deployment went to 7 out of 8 servers correctly — the 8th server still had a **dead, years-old code path** left over from a feature that had been repurposed. Nobody had tests in place to catch the fact that this old code was still live and would now behave completely differently under the new system.
>
> The result: in **45 minutes**, that one server executed millions of unintended trades, and Knight Capital lost **$440 million**. The company was nearly wiped out overnight and was acquired by a competitor months later.
>
> **The lesson isn't "write more code carefully."** It's that there was no automated safety net — no test, at any level — that verified "this old code path is disabled" or "this server matches what we expect before it goes live." A test doesn't need to be clever to save a company. It just needs to exist.

This is the world testing pulls us out of. Before we write a single test, we need to understand what *kind* of test we're even talking about — because "testing" isn't one thing.

---

## 🚗 System Tests vs Unit Tests — The Car Analogy

Here's a question: when Ford or BMW put a car together, do they *manufacture* every single part in that car?

No. They **assemble** it.

The brakes might come from Brembo. The sensors might come from Bosch. The electronics might come from Continental. Ford and BMW buy these parts from specialist suppliers and put them together into a finished vehicle.

So here's the real question: **who is responsible for testing the brake pads?**

It can't reasonably be Ford. Ford didn't design the brake pad's internal compound, they didn't choose the metallurgy, they don't know its failure points at a component level. **The responsibility for testing that a part works correctly, on its own, has to sit with the people who made that part** — the supplier.

Ford's job is different. Ford's job is to test that when *all these parts are put together*, the **whole car** works as a system — the brakes respond correctly to the pedal, the sensors talk to the dashboard, everything integrates.

This maps directly onto software:

| Car World | Software World |
|---|---|
| A single part (brake pad, sensor) | A single class or function |
| The parts supplier tests their part in isolation | **You test your unit (class/function) in isolation — this is a unit test** |
| Ford assembles the parts into a car | Your code assembles classes/functions into a working system |
| Ford test-drives the finished car | **A system/integration test verifies the assembled system behaves correctly** |

> ### 🚗 Real Incident: Toyota Unintended Acceleration (2009–2011)
> Toyota faced a wave of reports of vehicles accelerating unexpectedly, tied to over a dozen deaths. Investigations focused heavily on the electronic throttle control system, supplied in large part by **Denso**. This became a real-world, high-stakes version of exactly the question above: where does the *supplier's* responsibility to test their part end, and where does the *assembler's* (Toyota's) responsibility to test the integrated system begin? Congressional and NASA investigations spent enormous effort trying to draw that line after the fact — a boundary that should have been crystal clear, and rigorously tested on both sides, before the cars ever shipped.
>
> The takeaway for us: the *line* between "unit responsibility" and "system responsibility" isn't just an academic diagram — when it's blurry in the real world, in high-stakes systems, people get hurt and companies get investigated by governments.

We're going to use this exact concept in our code. **A unit test tests one "part" — one class, one method — in complete isolation, the same way a supplier tests a brake pad before it ever reaches an assembly line.**

---

## 🔧 What Makes a Unit Test a *Unit* Test

Not every test that's small is a *good* unit test. A proper unit test has to satisfy several properties at once. Let's go through each one — not just naming them, but understanding *why* they matter and what breaks when you violate them.

### 1. Tests One Thing Only

A unit test should verify a single behaviour of a single unit. If your test is called `testUserRegistration()` but it checks that the user was created, an email was sent, AND a log entry was written — that's not one test, that's three tests wearing a trench coat.

**Why this matters:** when a test with five assertions fails, which of the five things actually broke? You don't know until you dig in. A test that checks one thing tells you *exactly* what broke, the moment it fails. This is the difference between a test that saves you time and a test that creates a mystery for you to solve.

### 2. Fast

Unit tests should run in milliseconds. A full unit test suite for a mid-sized codebase should run in seconds, not minutes.

**Why this matters:** speed changes behaviour. If your tests take 20 minutes to run, you'll run them once before lunch and hope for the best. If they take 3 seconds, you'll run them after every single change, catching problems the moment you introduce them rather than discovering them in a pile, hours later.

### 3. Independent

Test order must never matter. Test B must never depend on state that Test A happened to leave behind. If you can run your tests in a completely random order, or run just *one* of them on its own, and get the exact same result every time — your tests are independent.

**Why this matters:** imagine Test A creates a user called "Bob" and doesn't clean up. Test B checks "there should be zero users in the system" and passes *only if it runs before Test A*. Now your test suite has a hidden, invisible dependency on run order. One day someone reorders the tests (or runs just Test B in isolation while debugging), and a perfectly correct piece of code suddenly appears broken. Independence means every test builds its own world from scratch and cleans up after itself.

### 4. Isolated

The unit under test should be cut off from its collaborators — the other classes, services, or components it normally works with. When you're unit testing Class A, you don't want the *real* Class B running too; you want a controlled stand-in for it.

**Why this matters:** if Class A's test also exercises the real Class B, and Class B has a bug, both tests fail — but only one of them (Class B's own test) should be telling you about that bug. Isolation means each unit test only fails because of a problem in *the unit it's actually testing*. (We'll build heavily on this idea in the mocking module — isolation is exactly why test doubles exist.)

### 5. Deterministic

Given the same input, a test must produce the same result — every time, on every machine, at any time of day. No randomness, no flakiness, no "well it usually passes."

**Why this matters — and why no IO/DB calls:** ask yourself, why can't a unit test touch a database or make a network call? Because the moment it does, the test's outcome depends on something *outside your control* — is the database up? Is the network fast today? Did someone else's test leave data in that table? A test that calls a real database might pass on your machine and fail on a teammate's, or pass today and fail tomorrow, for reasons that have nothing to do with your code being wrong. **Determinism is the whole point of a unit test** — it's supposed to be a repeatable, reliable signal, not a coin flip.

---

## 🧱 The Three Parts of Every Unit Test — AAA

Every well-formed unit test is made of exactly three parts, always in this order:

- **Arrange** — set up everything the test needs: create objects, prepare input data, configure any dependencies.
- **Act** — perform the single action you're actually testing (call the method).
- **Assert** — check that the outcome is what you expected.

```python
def test_should_return_correct_sum():
    # Arrange
    calculator = Calculator()

    # Act
    result = calculator.add(2, 3)

    # Assert
    assert result == 5
```

That's it. Three clearly separated steps, one behaviour under test, no hidden dependencies, no randomness, no IO. This structure is going to show up in *every single test* you write from here on — in the walkthrough, in the labs, and later when we get into mocking.

---

## 🚀 Challenge Task

Look back at a piece of code you've written recently (in this course or elsewhere) that touches a file, a database, or makes a network call.

- Could you currently write a *unit* test for it, following everything above?
- If not — what's standing in the way?

No solution provided. Bring your answer to the walkthrough.
