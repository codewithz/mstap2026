# 04 — Mocking in Practice

## 🔧 Code-Along: From a Real List to a Mocked List

Let's build this up exactly the way we do it live in class — one small change at a time.

**Step 1 — a completely real, non-mocked test:**

```python
def test_list_size_after_adding_items():
    # Arrange
    items = []
    items.append("apple")
    items.append("banana")
    items.append("cherry")

    # Act
    size = len(items)

    # Assert
    assert size == 3
```

Nothing fancy here — a real Python list, populated with dummy data in Arrange, its size captured in Act, and checked in Assert. Everyone can read this, everyone agrees it works, because it's just... real code doing a real thing.

**Step 2 — replace the real list with a mocked list, and change nothing else:**

```python
from unittest.mock import Mock

def test_list_size_after_adding_items_mocked():
    # Arrange
    items = Mock()
    items.append("apple")
    items.append("banana")
    items.append("cherry")

    # Act
    size = len(items)

    # Assert
    assert size == 3
```

Run this, and it **fails**. Not because your logic is wrong — because a `Mock()` object doesn't actually know how to behave like a list. It doesn't track appended items, and it doesn't know what `len()` should return, because *nobody told it what to do*.

**Why it fails is the entire point.** A mock, by default, is just **scaffolding** — an empty shell that will accept any call you throw at it, but has no built-in behaviour. It doesn't know anything unless you explicitly configure it.

**Step 3 — give the mock behaviour with `return_value` (Python's equivalent of Mockito's `when(...)`):**

```python
from unittest.mock import Mock

def test_list_size_after_adding_items_mocked_correctly():
    # Arrange
    items = Mock()
    items.append("apple")
    items.append("banana")
    items.append("cherry")
    items.__len__ = Mock(return_value=3)  # tell the mock what len() should return

    # Act
    size = len(items)

    # Assert
    assert size == 3
```

Now it passes. Nothing about the Arrange/Act/Assert structure changed — we just told the mock, explicitly, what to do when `len()` is called on it. **The `Mock()` was the scaffolding. `return_value` is the meat that makes the scaffolding actually do something.**

This is the core idea behind every mock you'll ever write: *a mock does nothing on its own — you tell it exactly how to behave, and it faithfully plays back exactly that.*

---

## 🌦️ The Weather API Problem: "Carry Your Umbrella"

Here's a scenario that makes the *need* for mocking impossible to ignore.

Say we're building an app called **Carry Your Umbrella**. Its whole job is simple: check tomorrow's weather forecast using the Google Weather API, and tell the user whether to bring an umbrella.

```python
def should_carry_umbrella(weather_client, date):
    forecast = weather_client.get_forecast(date)
    return forecast.chance_of_rain > 50
```

Now — how do you test this? Specifically, how do you test **what happens in November**, if you happen to be writing this code, and running your tests, in September?

You can't. Not with the real `weather_client`. A real call to the Google Weather API on a September afternoon can only ever return September's forecast — the *real* API has no concept of "pretend it's November and tell me what you'd say." You are completely at the mercy of whatever the live, real-world weather actually is, on the actual day you happen to run your test.

And it gets worse than just "wrong season." Think about everything else you can *never* deterministically test against a real, live API:

- What does the app do if the API times out?
- What does the app do if the API returns malformed or unexpected data?
- What does the app do if `chance_of_rain` is exactly `50` (the boundary case)?
- What does the app do on a day where rain is 100% certain — a scenario you can't just wait around for?

**None of these are testable, on demand, deterministically, against a real API.** This is precisely why we mock it:

```python
from unittest.mock import Mock

def test_should_carry_umbrella_when_high_chance_of_rain():
    # Arrange
    mock_weather_client = Mock()
    mock_weather_client.get_forecast.return_value = Mock(chance_of_rain=80)

    # Act
    result = should_carry_umbrella(mock_weather_client, date="2026-11-15")

    # Assert
    assert result is True


def test_should_not_carry_umbrella_when_low_chance_of_rain():
    # Arrange
    mock_weather_client = Mock()
    mock_weather_client.get_forecast.return_value = Mock(chance_of_rain=10)

    # Act
    result = should_carry_umbrella(mock_weather_client, date="2026-11-15")

    # Assert
    assert result is False


def test_handles_api_failure_gracefully():
    # Arrange
    mock_weather_client = Mock()
    mock_weather_client.get_forecast.side_effect = TimeoutError("API timed out")

    # Act & Assert
    # Now we can deliberately test a scenario the real API
    # would almost never let us reproduce on demand.
    ...
```

We can now test November, a boundary value of exactly 50%, and a total API outage — **all on a random Tuesday in September**, all instantly, all deterministically, without a single real network call. That's the entire value proposition of mocking, in one example.

---

## 💥 Real Incident: The Cost of an Unmocked, Untested Third-Party Dependency

A recurring pattern behind real production outages: a system has a **hard runtime dependency on a live third-party API**, and the team never wrote tests that simulated that API being slow, down, or returning bad data — because doing so against the *real* API isn't practically possible, and nobody built the mocking layer to simulate it instead.

This is exactly the same trap as our umbrella app, just at production scale: if you can only ever test against the *real*, currently-available response from a live external service, you can never verify — before it happens for real, to real users — what your system does when that service inevitably fails, slows down, or misbehaves. The **first time** the untested failure path executes is often the **first time it executes in production, live, in front of users.** A mocked test that simulates `TimeoutError` costs you two minutes to write. An unhandled timeout discovered in production can cost hours of incident response and real damage to user trust.

The fix isn't "test against the real API more" — it's the same fix as always: **mock the dependency, and deliberately test the failure paths you can never reliably trigger from the real thing.**

---

## 🧪 Lab

Using the `should_carry_umbrella` function above, write tests for:
1. `chance_of_rain` exactly at the boundary (50)
2. The forecast API returning `None` instead of a proper forecast object

## 🚀 Challenge Task

Find a function in your own code that calls an external service, a database, or reads a file. Identify one failure scenario for that dependency that you currently have **no way** of testing without mocking. Write the test.

No solution provided. Bring your answer to the walkthrough.
