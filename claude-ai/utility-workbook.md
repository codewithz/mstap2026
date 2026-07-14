# Hands-On Session: Building "utility-master" with Claude Code

In this session, you'll build a small Python app from scratch, using Claude Code the whole way through. By the end you'll have:

- A date utility (days between two dates, leap year check)
- A currency converter
- A password strength checker
- A simple command-line menu tying it all together
- A `CLAUDE.md` file you write yourself, so Claude remembers your project's rules every time you start a new session

You won't write any code by hand — you'll describe what you want, review what Claude Code proposes, and approve or adjust it.

---

## Before you start

- Have Claude Code installed and signed in
- Create an empty folder for this project and open it in VS Code (or your terminal)
- Start Claude Code:
  ```bash
  claude
  ```

---

## Step 1: See what Claude Code can do

Type:
```
/help
```
This shows you every built-in command. You'll use several of these — `/plan`, `/model`, `/compact`, `/diff`, `/clear` — as we go.

---

## Step 2: Scaffold the project

Type:
```
/plan
```
Then:
```
Create a new Python project called utility-master. I want a src/ folder
for the code and a tests/ folder for pytest tests. Set up a
requirements.txt with pytest. Don't add any features yet, just the
folder structure and an empty README.md.
```

Claude Code will show you a numbered plan before touching anything. Read it, then choose **Yes** to proceed.

---

## Step 3: Build the date utility

Type:
```
In src/date_util.py, write a function days_between(date1, date2) that
takes two dates in "YYYY-MM-DD" string format and returns the number
of days between them as an integer.
```

Once that's done, add a second function to the same file:
```
Now add a function is_leap_year(year) to the same file.
```

Now ask for tests:
```
Write pytest tests for both functions in tests/test_date_util.py and
run them.
```

When the tests pass, save some context space before moving on:
```
/compact
```

---

## Step 4: Build the currency converter

**First, try this on your own — just to see what happens:**
```
add a currency converter
```
Look at what you get. Would you know exactly how to use it? What's missing — which currencies, what rate format, rounding, error handling?

**Now try being specific.** Start with a plan:
```
/plan
```
Then:
```
In src/currency_converter.py, add a function convert(amount,
from_currency, to_currency, rates) where rates is a dict of
{currency_code: units_per_usd}. Round the result to 2 decimal places.
Raise ValueError if amount is negative.
```
Approve the plan. After Claude implements it, before running the tests, take a look at exactly what changed:
```
/diff
```

Now add tests:
```
Write pytest tests for convert() covering USD to GBP, GBP to USD, and
the negative-amount error case. Run them.
```

**Notice:** the first prompt and the second one asked for the same thing — but one was vague and one was specific. Compare the results.

---

## Step 5: Build the password strength checker

This next task is simple, so let's use a lighter model:
```
/model
```
Pick Haiku from the list.

Now build it:
```
In src/password_strength.py, add a function check_strength(password)
that returns "weak", "medium", or "strong" based on length (>=8) and
whether it contains uppercase, lowercase, digits, and special
characters. Score 1 point per category met.
```

**Now for an important experiment.** Ask for a test the easy way:
```
Write a unit test for check_strength() in password_strength.py
```
Let it pass — see what it checks.

Then ask again, but describe the *requirement* instead of pointing at the code:
```
Now write tests for check_strength() based on this spec, not the code:
a password needs length >= 8 AND all four of uppercase, lowercase,
digit, and special character to be "strong". Anything with 2-3
categories is "medium". Anything less is "weak". Test edge cases like
exactly 8 characters and exactly 2 categories.
```

**Compare the two sets of tests.** Which one would actually catch a mistake in your code, and which one just confirms whatever the code already does?

---

## Step 6: Bring it all together

This step touches all three files you've built, so plan first:
```
/plan
```
Then:
```
Create src/main.py with a simple command-line menu that lets the user
choose: 1) calculate days between two dates, 2) convert currency,
3) check password strength. Use input() prompts, no external
libraries.
```

Review the plan — check it references all three of your existing modules — then approve it.

Once it's built, run your app:
```bash
python -m src.main
```

---

## Step 7: Write your CLAUDE.md

`CLAUDE.md` is a file Claude Code reads automatically at the start of every session in this project. It saves you from re-explaining your conventions every time.

Create a file called `CLAUDE.md` in your project's root folder (`utility-master/CLAUDE.md`) with this content — edit it to match your own preferences if you like:

```markdown
# Project: utility-master

A small Python CLI app with three utilities: date calculations,
currency conversion, and password strength checking.

## Commands
- run tests: `pytest`
- run the app: `python -m src.main`

## Structure
- `src/date_util.py` — days_between(), is_leap_year()
- `src/currency_converter.py` — convert()
- `src/password_strength.py` — check_strength()
- `src/main.py` — CLI menu tying the three together
- `tests/` — pytest tests, one file per module

## Conventions
- Python 3.10+, standard library only (no third-party deps except pytest)
- Every function gets a docstring and at least one test
- Money values always rounded to 2 decimal places

## Do / Don't
- Do: write a test whenever you add a new function
- Do: ask for the spec, not the code, when generating tests
- Don't: add new third-party dependencies without asking first
- Don't: silently touch main.py when only asked to change one module
```

---

## Step 8: See CLAUDE.md in action

Clear your conversation so Claude Code has no memory of what you just discussed:
```
/clear
```

Now ask for a new function, without repeating any of your conventions:
```
add a function to src/date_util.py that returns the day-of-week name
for a given date
```

**Notice:** Claude still adds a docstring, and if you ask for a test it still follows your conventions — even though you cleared the conversation. That's `CLAUDE.md` working, not memory of your earlier chat.

---

## Quick reference: commands used today

| Command | What it does |
|---|---|
| `/help` | Lists all available commands |
| `/plan` | Shows a plan before making changes — use for anything non-trivial or multi-file |
| `/diff` | Shows exactly what's changed in your files so far |
| `/model` | Switch between Haiku / Sonnet / Opus depending on task complexity |
| `/compact` | Summarizes the conversation so far to save space |
| `/clear` | Wipes the current conversation (CLAUDE.md still applies) |

---

## What you built today

By now you should have:
- ✅ A working `utility-master` project with three modules and passing tests
- ✅ A command-line app tying them together
- ✅ Your own `CLAUDE.md` file
- ✅ Hands-on experience with `/plan`, `/diff`, `/model`, `/compact`, and `/clear`
- ✅ A feel for the difference between a vague prompt and a specific one, and between testing code vs. testing a spec

Take this project home — it's yours to keep experimenting with.

---
*Commands referenced in this guide are accurate as of July 2026. If a command doesn't behave exactly as described, type `/help` inside Claude Code to see the current list — the tool is updated frequently.*