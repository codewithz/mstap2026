# Hands-On: Building a Branded Student Portal with Claude Code

In this session, you'll build a small login + dashboard app twice — once with no styling guidance, and once with a proper brand brief — so you can see exactly what a `CLAUDE.md` file does to the output.

**What you're building:** a login page (username `student`, password `neueda`) that takes you to a dashboard showing your Attendance, Linux, and SQL scores.

---

## Part 1: Build it with no guidance

### Step 1: Start a fresh project
```bash
mkdir student-portal && cd student-portal
claude
```
Don't create a `CLAUDE.md` yet — we want to see what Claude Code gives us with zero styling direction first.

### Step 2: Build the login page
Type:
```
Create a simple HTML/CSS/JS login page called index.html. It should have a
username field and a password field. If the username is "student" and the
password is "neueda", redirect to dashboard.html. Otherwise show an error
message. Keep it in separate files: index.html, style.css, script.js.
```

### Step 3: Build the dashboard
Type:
```
Now create dashboard.html. It should welcome the student and show three
score cards: Attendance (92%), Linux (78%), and SQL (85%). Add a logout
button that clears the session and sends the user back to index.html. If
someone isn't logged in, dashboard.html should redirect them to index.html.
```

### Step 4: Run it and take a look
No server needed — just open `index.html` directly in your browser (double-click it, or right-click → Open With → your browser).

Log in with `student` / `neueda`.

**Take a moment here.** Does this look like it belongs to a real company? What's missing?

---

## Part 2: Add a brand and rebuild

### Step 5: Look at the reference site
Open **neueda.com**. Notice:
- Dark navy background sections
- Orange used consistently for accents, icons, and highlights
- Clean, modern sans-serif type
- Generous whitespace, rounded card-based layout
- The `neueda` wordmark with a small bracket-style mark

### Step 6: Write your CLAUDE.md
Create a file called `CLAUDE.md` in your project folder. Ask yourself: *what would I need to tell Claude to get that look instead of what we just built?* Use this as a starting point:

```markdown
# Project: student-portal

## Structure
- index.html — login page (username: student, password: neueda)
- dashboard.html — shows Attendance, Linux, and SQL scores
- style.css — all styling
- script.js — login logic
- dashboard.js — auth guard + logout

## Brand: Neueda
This project should look like it belongs on neueda.com.

**Colors**
- Background: dark navy, #191a24
- Card/surface: #22232f
- Accent (buttons, highlights): orange, #f47c20 (hover #ff9142)
- Primary text: near-white, #f5f5f7
- Muted text: #a9abb8

**Typography**
- Clean system sans-serif stack
- Small uppercase orange "eyebrow" labels above headings
- Bold headings, muted subtext underneath

**Layout & components**
- Rounded cards (10-14px), generous padding, centered content
- Login form in a centered card on a dark background
- Dashboard: top bar with logo + logout, then a grid of score cards
- Score cards show a big number and a thin orange progress bar
- Logo: an orange bracket mark [ ] next to the wordmark "neueda"

## Conventions
- No CSS frameworks — plain CSS with :root custom properties for the palette
- Keep script.js and dashboard.js logic unchanged when restyling — only
  touch style.css and markup/classes unless asked otherwise
```

### Step 7: Clear the conversation and restyle
Type:
```
/clear
```
Then:
```
Restyle this app to match the CLAUDE.md brand guidelines. Don't change the
login logic or the score values — just the look.
```

### Step 8: Compare, side by side
Refresh `index.html` in your browser (it's still just a local file — no server, no restart). Same login, same scores — but take a look at how different it feels now.

**Ask yourself:** what actually changed here? Was it that Claude Code got "smarter" between Part 1 and Part 2 — or something else?

---

## What to notice

- The login logic and the score values never changed between the two versions — only the styling did. That's the whole point: `CLAUDE.md` doesn't make Claude Code more capable, it gives it a brief to work from — the same way a designer needs a brand guide, not more talent, to make something feel "on brand."
- You ran `/clear` before restyling, which wipes the conversation. The new look still showed up correctly — because it came from `CLAUDE.md`, not from Claude remembering what you'd typed earlier in the chat.
- This mirrors a real onboarding scenario: a new developer joining a team can write perfectly working code that still doesn't match the house style, until someone hands them a design system to work from. `CLAUDE.md` is that handoff.

---

## Keep going
Try asking Claude Code to:
- Add a "forgot password" link (styling only, no real functionality needed)
- Add a fourth score card for a subject of your choice
- Try changing just the accent color in `CLAUDE.md` and see how consistently it gets picked up across every element