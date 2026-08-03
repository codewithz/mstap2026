# JS Training Playground — Node Project Setup

This is a minimal Node project. It's not here to build anything heavy — it exists so we can practice real `export`/`import` syntax (ES Modules) before you write the same syntax in a browser later.

---

## Requirements

- [Node.js](https://nodejs.org) installed — check with:
  ```
  node -v
  ```
  Any recent LTS version (18+) works fine.

## Project structure

```
js-training/
├── package.json
├── src/
│   ├── 1-index.js
│   ├── 2-understanding-variables.js
│   ├── ... one file per topic
└── explainers/
    └── 01-js-101/
        ├── 01-variables.md
        ├── 02-objects.md
        └── ... one explainer per topic
```

## Running a file

```
node src/2-understanding-variables.js
```

Every file in `src/` can be run directly — no build step, no bundler.

## ⚠️ GOTCHA: ES Modules vs CommonJS

Look at the top of `package.json`:

```json
{
  "type": "module"
}
```

This line tells Node to treat every `.js` file as an **ES Module**, which means:
- You can use `import`/`export` syntax directly (no `require()`)
- Implicit globals (assigning to an undeclared variable) throw an error instead of silently working — you'll see this firsthand in the Variables explainer

If `"type": "module"` were removed or set to `"commonjs"`, `import`/`export` syntax would throw a `SyntaxError` and you'd need `require()`/`module.exports` instead. We're using ESM because it matches the `<script type="module">` syntax you'll use in the browser later.

## 💡 WHY a Node project at all, if we're building for the browser?

Two reasons:
1. **Fast feedback loop** — running `node file.js` gives instant console output, no browser refresh needed, while you're learning core syntax.
2. **`import`/`export` practice** — once your explainer files start splitting logic across multiple files (e.g., a `customers.js` module and an `api.js` module), you need real module syntax. Practicing it here first, with quick `node` runs, is faster than debugging module errors in the browser.

---

## Track Index

1. **JS-101** — `explainers/01-js-101/` — 11 files, core JS fundamentals *(built)*
2. **Promises/Async** — `explainers/02-promises-async/` — 4 files *(built)*
3. **Fetch** — `explainers/03-fetch/` — 3 files *(built — calls the real, free, no-auth [JSONPlaceholder](https://jsonplaceholder.typicode.com) API; `mock-server/` is kept as an optional offline fallback if internet access isn't available during a session)*
4. **DOM + Flask CRUD** — `explainers/04-dom-flask-crud/` — 3 files, capstone using the Customer Management page *(built — see `src/dom-flask/` for the working `customers.html` + `app.js`/`api.js`/`render.js`, verified end-to-end against `mock-server/`)*

All four tracks are complete.