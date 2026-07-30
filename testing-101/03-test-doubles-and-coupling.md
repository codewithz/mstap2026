# 03 — Test Doubles & Coupling

## 🎭 Mocks Are Not Stubs

A very common mistake early on: treating "mock" as a catch-all word for "any fake object I use in a test." It isn't. **Mock is one specific type of a broader category called a *test double*.**

The definitive reference for this is Martin Fowler, in his article **"TestDouble"** at [martinfowler.com/bliki/TestDouble.html](https://martinfowler.com/bliki/TestDouble.html), where he lays out (drawing on Gerard Meszaros's *xUnit Test Patterns*) five kinds of test double:

- **Dummy** — an object passed around but never actually used. It exists purely to satisfy a parameter list (e.g. a method needs a `Logger` argument but your test doesn't care about logging at all).
- **Fake** — has a real, working implementation, but takes a shortcut that makes it unsuitable for production (e.g. an in-memory database used instead of a real one).
- **Stub** — provides canned, pre-programmed answers to calls made during the test. It doesn't respond to anything it wasn't told to expect.
- **Spy** — a stub that *also* records how it was called, so the test can inspect that afterwards (e.g. "was `send_email` called exactly once?").
- **Mock** — pre-programmed with *expectations*, forming a specification of the calls it expects to receive. A mock can make the test fail if it *doesn't* receive the calls it expected.

Fowler has a companion article specifically on the distinction that trips people up most: **"Mocks Aren't Stubs"** at [martinfowler.com/articles/mocksArentStubs.html](https://martinfowler.com/articles/mocksArentStubs.html). The short version: a **stub** helps you control what your code receives (state-based — did the result come out right?). A **mock** helps you verify what your code *did* (behaviour-based — was this method actually called, with these arguments, this many times?).

We're going to focus mainly on mocks in this course, but knowing the family they come from will save you a lot of confusion when you read other people's test code or documentation.

---

## 🔗 Tight Coupling vs Loose Coupling

Before we can talk about *why* we need test doubles at all, we need to talk about coupling.

Imagine two classes, `A` and `B`.

**Tightly coupled version:**

```python
class B:
    def get_data(self):
        # imagine this hits a real database
        return "real data from the database"


class A:
    def process(self):
        b = B()  # A creates its own concrete instance of B
        data = b.get_data()
        return data.upper()
```

Here, `A` reaches out and creates its own instance of `B` directly, inside itself. `A` is welded to this one specific, concrete version of `B`. There's no way to swap `B` out for anything else without editing `A`'s source code.

**Loosely coupled version:**

```python
class A:
    def __init__(self, b):
        self.b = b  # B is handed in from outside — "injected"

    def process(self):
        data = self.b.get_data()
        return data.upper()
```

Now `A` doesn't know or care what concrete thing `self.b` actually is — it only cares that whatever it's handed has a `get_data()` method. This is called **dependency injection**, and it's what makes swapping in a test double possible at all.

---

## 🤔 So Why Do We Need Test Doubles?

Go back to what we already established: **unit tests must be deterministic, and they must not perform IO** — no database calls, no network calls, no file access.

Now look at the tightly coupled version of `A` above. If you write a unit test for `A.process()`, you have no choice but to also run `B.get_data()` — and if `B.get_data()` hits a real database, your "unit test for A" has secretly become an integration test that depends on a database being up, reachable, and in a known state.

This is the exact tension that should be nagging at you right now: **we said tests can't do IO — so how do you test something whose whole job depends on IO?**

The answer is: you don't test the real IO-performing dependency at all. In the loosely coupled version, because `B` is *injected* rather than created internally, your test can hand `A` a **test double** instead of a real `B` — something that looks like a `B` (has a `get_data()` method) but is completely fake, in-memory, instant, and fully under your control.

```python
def test_process_uppercases_the_data(mocker):
    # Arrange
    fake_b = mocker.Mock()
    fake_b.get_data.return_value = "fake data"
    a = A(fake_b)

    # Act
    result = a.process()

    # Assert
    assert result == "FAKE DATA"
```

No database. No network. Fully deterministic. Fully isolated. This is only possible *because* `A` and `B` are loosely coupled in the first place — tight coupling and testability are directly at odds with each other.

---

## 💥 Real Incident: Flaky Tests and the "Boy Who Cried Wolf" Problem

Google has written extensively (in their public engineering blog and the *Software Engineering at Google* book) about a recurring failure mode in large codebases: teams end up with test suites that are **tightly coupled to real infrastructure** — real databases, real network calls, real shared test environments. These tests aren't isolated, so they fail intermittently for reasons that have nothing to do with actual bugs — a shared test database is slow today, a network blip happens, another team's test left bad data behind.

The result is entirely predictable: engineers start seeing red (failing) tests so often, for reasons unrelated to their own changes, that they stop trusting the signal. People start re-running failed tests "to see if it passes this time," or worse, start ignoring failures altogether and merging anyway. This is the **"boy who cried wolf" problem** — once a test suite lies to you often enough, you stop believing it even when it's telling the truth about a real bug.

The fix Google and countless other engineering organisations converged on is exactly what we're building toward: **isolate your unit tests from real infrastructure using test doubles**, and reserve the real infrastructure (real databases, real network calls) for a much smaller number of integration and system tests, further up the pyramid, that are *expected* to be slower and are run less frequently.

---

## 🚀 Challenge Task

Take the tightly coupled `A`/`B` example from a piece of your own code (or one from an earlier session). Rewrite it so the dependency is injected rather than created internally, and identify which kind of test double from Fowler's taxonomy (Dummy, Fake, Stub, Spy, Mock) you'd use to unit test it — and why that one specifically, rather than another.

No solution provided. Bring your answer to the walkthrough.
