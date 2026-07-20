# Two Cities, One Repo: The Story of Loopline

*A one-read explainer covering everything you'll practice in the labs — no steps to follow here, just read it like a story.*

---

## The Idea

Kata is sitting in a café near Deák Ferenc tér in Budapest with her laptop open and a half-finished sketch of a website on the screen. She's building **Loopline** — a tiny tool that helps small teams share standup updates without another Slack channel nobody reads. It's just an idea right now: three files, a folder called `loopline`, and a lot of ambition.

Four thousand kilometers away — well, not that far, but far enough that they've never met in person — Tom is in London, replying to her email. *"I'm in. Let's build it."*

Neither of them knows it yet, but the next few weeks are going to teach them everything they need to know about Git — not because they read a manual, but because things kept going wrong in exactly the ways that make you learn.

---

## Kata's First Commit

Kata starts alone. She's got `index.html`, `style.css`, and `script.js` — a plain page that says, more or less, "Loopline: coming soon." Before she does anything else, she turns the folder into a Git repository.

```
git init
```

Nothing dramatic happens on screen, but something important just did: this folder now has a memory. It's a real, complete repository — and it has never once talked to the internet. Tom doesn't know it exists yet. That's fine. Local first, always.

```
git status
```

Git tells her, plainly, that it sees three files and has no idea what they are. Untracked. She stages them:

```
git add index.html style.css script.js
```

And now comes the part Kata almost skips, the way most people do the first time — writing the commit message. She could type `first commit` and move on. Instead she pauses and writes something a stranger could understand six months from now:

```
git commit -m "Add initial landing page skeleton"
```

That's the whole discipline, really: not being clever, just being clear. *If applied, this commit will add the initial landing page skeleton.* Done.

She keeps working. Changes a heading, checks the difference before committing:

```
git diff
git add index.html
git commit -m "Update homepage headline"
```

`git log` now shows two commits, small and specific, each one a sentence someone could actually use later. This is the rhythm she'll keep for the rest of the project: change, check, stage, commit, in small enough pieces that each commit means one thing.

---

## Oops

Two days in, Kata tries something ambitious — a fancy animated hero section — and it goes badly. The page looks broken. She hasn't staged it yet, so:

```
git checkout -- style.css
```

Gone. Back to the last commit, like it never happened.

Later, she stages a change she's not ready to commit — she just wanted to see the diff — and unstages it:

```
git reset HEAD script.js
```

The edit is still there, just not queued up anymore.

And then, the classic: she commits, and immediately notices she forgot to update `index.html` to match. Rather than adding a second commit titled `fix`, she folds it into the one she just made:

```
git add index.html
git commit --amend
```

One clean commit, not two messy ones. She makes a mental note, though — this trick only works because nobody else has seen this commit yet. Once it's shared, rewriting it stops being harmless. She doesn't know exactly why yet. She'll find out soon.

One more thing before Tom arrives: her editor keeps dropping a `.DS_Store` file into the folder, and it keeps showing up in `git status` like an uninvited guest. She writes a `.gitignore`:

```
echo ".DS_Store" > .gitignore
git add .gitignore
git commit -m "Ignore OS junk files"
```

Silence. Exactly what she wanted.

---

## Two Desks, Two Ideas

Tom pulls the project down and gets to work from his kitchen table in London. They quickly realize they're both about to build things that touch the same page, so they each start on a branch — their own private lane to work in without stepping on each other.

Kata, in Budapest:

```
git checkout -b signup
```

She builds a signup form. Tom, in London:

```
git checkout -b login
```

He builds a login page. Neither of them can see what the other is doing — and neither of their branches affects `main`, which still just shows the plain homepage. That's the whole point. Two people, two ideas, zero collisions, for now.

When Kata's signup form is done, she merges it back in:

```
git checkout main
git merge signup
```

Fast-forward. No drama. `main` simply absorbs her work, because nothing else had changed on `main` in the meantime.

Tom's login page merges the same easy way — until they both, separately and for entirely reasonable reasons, decide the header color needs to change. Kata thinks navy. Tom thinks forest green. They each commit their version on their own branch. When Tom tries to merge his in:

```
git merge kata-header-tweak
```

Git stops him cold:

```
CONFLICT (content): Merge conflict in style.css
```

This is not a bug. This is Git being honest — it genuinely cannot know whose header color they actually want. Tom opens the file, sees the markers:

```
<<<<<<< HEAD
header { background-color: forestgreen; }
=======
header { background-color: navy; }
>>>>>>> kata-header-tweak
```

He video-calls Kata (finally, an actual conversation instead of commits flying past each other). They agree: navy. He deletes the markers, keeps navy, and finishes the merge:

```
git add style.css
git commit -m "Resolve header color conflict, keep navy"
```

Nobody's code was overwritten by accident. Git just made them talk to each other before it let the merge complete.

---

## Crossing the Channel

Up to this point, everything has lived on two separate laptops that have never once compared notes automatically. Kata's repo and Tom's repo are two completely independent things — they only match because people occasionally run commands to copy history between them. It's time to give them a shared home: GitHub.

Kata creates an empty repository and connects her local one to it:

```
git remote add origin https://github.com/loopline/loopline.git
git push -u origin main
```

She refreshes the page in her browser. There it is — every commit, every branch, sitting on a server neither of them owns personally, reachable from anywhere. Tom clones it down onto his machine in London, and now they both have a full copy of the same history.

A week later, Tom pushes a fix. Kata, mid-morning in Budapest, wants to see it:

```
git fetch origin
```

Her files don't change. Nothing visibly happens — because `fetch` is Git quietly checking in with the server, downloading what's new without touching her working copy. She has to actually apply it:

```
git merge origin/main
```

*Now* her files update. Soon enough she stops doing this in two steps and just runs `git pull`, which does both at once — the everyday shortcut for "get me up to date."

Then, one Friday, Tom does something he immediately regrets. He amends a commit that's *already* been pushed — the same trick Kata used earlier, except this time it's not harmless, because Kata already pulled the old version. His push gets rejected. He's tempted, for about four seconds, to just force it through:

```
git push --force
```

He doesn't. He messages Kata first: *"hey, I need to rewrite one commit, can you hold off pulling for ten minutes?"* She says fine. He force-pushes, she re-pulls cleanly, and nothing is lost. The rule he takes away from it: force-push is for branches you own alone, and always, always with a warning first if anyone else might have already pulled.

---

## The Review

By week three, Loopline has a third teammate — Priya, hired to help with the backend, based in Manchester. With three people now touching the code, pushing straight to `main` starts to feel reckless. So they add a step: before anything reaches `main`, someone else looks at it.

Kata builds a "forgot password" page on its own branch, pushes it, and opens a Pull Request instead of merging it herself:

```
git push -u origin forgot-password
```

On GitHub, she describes what she built and tags Priya as reviewer. Priya reads the diff, leaves a comment about a missing label on one of the form fields, and Kata pushes a quick fix to the same branch — the PR updates itself, no need to start over. Priya approves.

Now comes a small decision: how to actually bring it into `main`. They could keep the full branch history with a **merge commit** — good when the story of *how* something was built still matters. They could **squash** Kata's several small `wip` commits into one clean line — better when the branch's internal history is messy and nobody needs to see the scaffolding. Or they could **rebase**, replaying her commits on top of `main` for a perfectly straight line — powerful, but risky on anything more than one person is touching.

For this one, they squash. One tidy commit lands on `main`: *"Add forgot password page."* Kata and Tom both pull it down, and the site — now spanning three contributors and two countries — keeps moving forward without anyone stepping on anyone else's work.

---

## Launch Day

Loopline ships. It's small, it's a little rough around the edges, and it works. Looking back, the things that actually saved them weren't clever tricks — they were habits:

Kata never let a commit message get away with saying nothing. Tom learned, the hard way, that force-pushing without warning is how you lose a teammate's afternoon. They both learned to commit at the size of "one coherent, working idea" — not every keystroke, not once a day, but right at the point where the work would still make sense to a stranger reading it later. And once there was more than one person in the room, nothing reached `main` without someone else looking at it first.

None of it was really about Git commands. It was about two people, in two countries, trusting a folder full of history to keep them honest with each other.

---

*Every command in this story — `init`, `add`, `commit`, `diff`, `log`, `checkout --`, `reset`, `commit --amend`, `.gitignore`, `branch`, `merge`, conflict resolution, `remote add`, `push`, `fetch`, `pull`, `--force`, and Pull Requests — is one you'll actually run yourself in today's labs. Read this once, then go build something.*