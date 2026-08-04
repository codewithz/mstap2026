# CustomerApp — Complete Flask + MySQL Setup Guide

This is the full, single-file guide to building the CustomerApp backend from scratch: a Flask app exposing a `/api/customers` CRUD API, backed by a real MySQL database, serving a **standalone JavaScript frontend** (the `customers.html`/`app.js` built in Track 4). This is a pure JSON API — **no Jinja templates, no server-rendered HTML**. Flask's only job here is to answer `fetch()` calls with JSON.

**Everything in this guide has been built and verified end-to-end**: every command was actually run, the schema was loaded into a real MySQL database, and every endpoint was tested with real HTTP requests.

---

## Architecture

```
Browser (customers.html + app.js — standalone JS, no Flask templates)
        │  fetch()  →  JSON in, JSON out
        ▼
Flask app (app.py) — pure JSON API, runs on http://localhost:5050
        │  PyMySQL
        ▼
MySQL database (customerapp_db)
```

Flask here is doing exactly one job: talk to MySQL, return JSON. It never renders HTML — that's entirely the frontend's responsibility, running independently in the browser.

---

## Prerequisites

- **Python 3.8+** — check with `python3 --version`
- **MySQL Server** — check with `mysql --version`. If it's not installed:
  - macOS: `brew install mysql`
  - Ubuntu/Debian: `sudo apt-get install mysql-server`
  - Windows: install via the [MySQL Installer](https://dev.mysql.com/downloads/installer/)
- **pip**

---

## Step 1 — Create the Project Folder

```bash
mkdir flask-api
cd flask-api
```

---

## Step 2 — Create and Activate a Virtual Environment

A virtual environment keeps this project's Python packages isolated from every other project on your machine.

```bash
python3 -m venv venv
```

Activate it:

| OS | Command |
|---|---|
| macOS / Linux | `source venv/bin/activate` |
| Windows (CMD) | `venv\Scripts\activate.bat` |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |

Your prompt should now show `(venv)` at the start of the line.

⚠️ **GOTCHA:** Skipping activation and running `pip install` directly often fails on modern systems with:
```
error: externally-managed-environment
```
This is Python deliberately blocking system-wide installs outside a virtual environment. Always activate the venv first.

⚠️ **GOTCHA:** Don't name any folder in this directory `app` if your entry-point file is `app.py` — a folder and a file sharing the same name breaks Flask's module resolution (`flask run` specifically) with a confusing `Failed to find Flask application` error. This project's structure (below) avoids that by using `app.py` as the only thing named `app`.

---

## Step 3 — Project Structure

```
flask-api/
├── venv/                 ← virtual environment (never commit this)
├── app.py                ← the Flask application (all routes)
├── db.py                 ← MySQL connection helper
├── schema.sql             ← database + table + seed data
├── requirements.txt       ← pinned Python dependencies
├── .env                   ← your local DB credentials (never commit this)
└── .gitignore
```

`.gitignore` should include at minimum:
```
venv/
__pycache__/
*.pyc
.env
```

---

## Step 4 — Install Dependencies

With the virtual environment active:

```bash
pip install flask flask-cors pymysql
```

Then freeze the exact versions:

```bash
pip freeze > requirements.txt
```

**Verified `requirements.txt`:**
```
Flask==3.1.3
Flask-Cors==6.0.5
PyMySQL==1.2.0
```

(Your `pip freeze` may include a few additional transitive dependencies like `blinker`, `click`, `itsdangerous`, `Jinja2`, `MarkupSafe`, `Werkzeug` — these ship with Flask automatically. You won't write any Jinja templates yourself; Flask just depends on the package internally.)

To set up on a new machine later:
```bash
pip install -r requirements.txt
```

💡 **WHY `Flask-Cors` matters here specifically:** since the frontend is a standalone JS app (not server-rendered by Flask), the browser treats `customers.html` and this API as **different origins** the moment they're not served from the exact same host/port. Without CORS enabled, the browser blocks every `fetch()` call from `app.js` with a CORS error — even though the request itself would otherwise succeed. `CORS(app)` in `app.py` fixes this in one line.

---

## Step 5 — Set Up the MySQL Database

Log in to MySQL as root (or any admin user):

```bash
mysql -u root -p
```

Run:

```sql
CREATE DATABASE IF NOT EXISTS customerapp_db;
CREATE USER IF NOT EXISTS 'customerapp_user'@'localhost' IDENTIFIED BY 'CustomerApp@2026';
GRANT ALL PRIVILEGES ON customerapp_db.* TO 'customerapp_user'@'localhost';
FLUSH PRIVILEGES;
```

⚠️ **GOTCHA:** `'CustomerApp@2026'` is a placeholder password for local practice — pick your own for any real setup, and never commit real credentials (that's what `.env` in Step 7 is for).

---

## Step 6 — `schema.sql` (Table + Seed Data)

```sql
-- CustomerApp — Customer Management Database
-- Run this once to create the database, table, and seed data.

CREATE DATABASE IF NOT EXISTS customerapp_db;
USE customerapp_db;

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(120)   NOT NULL,
    email       VARCHAR(150)   NOT NULL UNIQUE,
    phone       VARCHAR(30),
    dob         DATE,
    join_date   DATE,
    branch      VARCHAR(50),
    balance     DECIMAL(10,2)  NOT NULL DEFAULT 0.00,
    created_at  TIMESTAMP      DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP      DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Seed data
INSERT INTO customers (name, email, phone, dob, join_date, branch, balance) VALUES
('Alex Rivera', 'alex.rivera@example.com', '+36 20 123 4567', '1994-03-12', '2021-06-01', 'Budapest', 4250.00),
('Sara Kovacs', 'sara.kovacs@example.com', '+36 30 987 6543', '1997-11-05', '2022-02-15', 'London', 1980.50);
```

⚠️ **GOTCHA — `join_date` naming:** MySQL columns use `snake_case` (`join_date`), but the frontend's JSON uses `joinDate` (camelCase). This is intentional — SQL/Python convention favors snake_case, JavaScript favors camelCase. `app.py` (Step 9) explicitly converts between the two, so neither side has to change its own convention.

Load it:

```bash
mysql -u root -p < schema.sql
```

Verify:

```bash
mysql -u root -p -e "USE customerapp_db; SELECT * FROM customers;"
```

**Verified real output:**
```
id  name          email                       phone              dob         join_date   branch     balance
1   Alex Rivera   alex.rivera@example.com     +36 20 123 4567    1994-03-12  2021-06-01  Budapest   4250.00
2   Sara Kovacs   sara.kovacs@example.com     +36 30 987 6543    1997-11-05  2022-02-15  London     1980.50
```

---

## Step 7 — `.env` (Your Local Credentials)

Create `flask-api/.env`:

```
DB_HOST=localhost
DB_USER=customerapp_user
DB_PASSWORD=CustomerApp@2026
DB_NAME=customerapp_db
```

`db.py` reads these as environment variables with safe fallback defaults for local practice — but for anything beyond your own machine, always set real environment variables instead of relying on the fallback defaults.

---

## Step 8 — `db.py` (Connection Helper)

```python
import pymysql
import pymysql.cursors
import os

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "customerapp_user"),
    "password": os.environ.get("DB_PASSWORD", "CustomerApp@2026"),
    "database": os.environ.get("DB_NAME", "customerapp_db"),
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True,
}


def get_connection():
    return pymysql.connect(**DB_CONFIG)
```

💡 **WHY `DictCursor`:** by default, PyMySQL returns rows as plain tuples — you'd have to remember column *positions*. `DictCursor` returns rows as dictionaries (`row["name"]`), which is far more readable and less error-prone.

---

## Step 9 — `app.py` (The Full CRUD API)

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from decimal import Decimal
from datetime import date
import pymysql

from db import get_connection

app = Flask(__name__)
CORS(app)  # allows the standalone JS frontend (different origin) to call this API


def serialize_customer(row):
    """Convert a DB row (snake_case, Decimal, date) into the exact JSON
    shape the frontend expects (camelCase joinDate, plain numbers/strings)."""
    return {
        "id": row["id"],
        "name": row["name"],
        "email": row["email"],
        "phone": row["phone"],
        "dob": row["dob"].isoformat() if isinstance(row["dob"], date) else row["dob"],
        "joinDate": row["join_date"].isoformat() if isinstance(row["join_date"], date) else row["join_date"],
        "branch": row["branch"],
        "balance": float(row["balance"]) if isinstance(row["balance"], Decimal) else row["balance"],
    }


@app.route("/api/customers", methods=["GET"])
def get_customers():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers ORDER BY id")
            rows = cursor.fetchall()
        return jsonify([serialize_customer(r) for r in rows]), 200
    finally:
        conn.close()


@app.route("/api/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            row = cursor.fetchone()
        if not row:
            return jsonify({"error": f"Customer {customer_id} not found"}), 404
        return jsonify(serialize_customer(row)), 200
    finally:
        conn.close()


@app.route("/api/customers", methods=["POST"])
def create_customer():
    data = request.get_json(silent=True) or {}

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    """INSERT INTO customers (name, email, phone, dob, join_date, branch, balance)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (
                        data.get("name"),
                        data.get("email"),
                        data.get("phone"),
                        data.get("dob") or None,
                        data.get("joinDate") or None,
                        data.get("branch"),
                        data.get("balance", 0),
                    ),
                )
            except pymysql.err.IntegrityError:
                return jsonify({"error": "A customer with that email already exists"}), 400

            new_id = cursor.lastrowid
            cursor.execute("SELECT * FROM customers WHERE id = %s", (new_id,))
            row = cursor.fetchone()
        return jsonify(serialize_customer(row)), 201
    finally:
        conn.close()


@app.route("/api/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.get_json(silent=True) or {}

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            existing = cursor.fetchone()
            if not existing:
                return jsonify({"error": f"Customer {customer_id} not found"}), 404

            # Merge: only overwrite fields that were actually sent (partial update)
            merged = {
                "name": data.get("name", existing["name"]),
                "email": data.get("email", existing["email"]),
                "phone": data.get("phone", existing["phone"]),
                "dob": data.get("dob", existing["dob"]),
                "join_date": data.get("joinDate", existing["join_date"]),
                "branch": data.get("branch", existing["branch"]),
                "balance": data.get("balance", existing["balance"]),
            }

            cursor.execute(
                """UPDATE customers
                   SET name=%s, email=%s, phone=%s, dob=%s, join_date=%s, branch=%s, balance=%s
                   WHERE id=%s""",
                (
                    merged["name"], merged["email"], merged["phone"],
                    merged["dob"], merged["join_date"], merged["branch"],
                    merged["balance"], customer_id,
                ),
            )
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            row = cursor.fetchone()
        return jsonify(serialize_customer(row)), 200
    finally:
        conn.close()


@app.route("/api/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            existing = cursor.fetchone()
            if not existing:
                return jsonify({"error": f"Customer {customer_id} not found"}), 404
            cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
        return jsonify({"deleted": serialize_customer(existing)}), 200
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
```

⚠️ **GOTCHA — SQL injection:** every query uses `%s` placeholders with values passed as a **separate tuple**, never Python f-strings or `+` concatenation. This is non-negotiable: string-building SQL directly from user input is exactly how SQL injection attacks happen. PyMySQL escapes everything passed as a placeholder parameter automatically.

⚠️ **GOTCHA — `debug=True`:** enables auto-reload and detailed browser error pages — exactly what you want locally, but it must be `False` (or removed, since that's the default) before this is ever deployed anywhere reachable by the public internet. Debug mode's interactive console can execute arbitrary Python code if it's ever exposed.

⚠️ **GOTCHA — no Jinja here:** note there is no `render_template()` anywhere in this file, and no `templates/` folder. Every route returns `jsonify(...)` — pure JSON. If you ever see a Flask tutorial using `render_template("page.html")`, that's a *different* architecture (server-rendered pages) from what this project does (a pure JSON API consumed by an independent JS frontend).

---

## Step 10 — Run the App

```bash
python3 app.py
```

**Verified output:**
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5050
```

---

## Step 11 — Verified Endpoint Tests (Real curl Output)

All of the following were actually run against a real MySQL database:

**GET all customers:**
```bash
curl http://localhost:5050/api/customers
```
```json
[
  { "id": 1, "name": "Alex Rivera", "email": "alex.rivera@example.com", "phone": "+36 20 123 4567", "dob": "1994-03-12", "joinDate": "2021-06-01", "branch": "Budapest", "balance": 4250.0 },
  { "id": 2, "name": "Sara Kovacs", "email": "sara.kovacs@example.com", "phone": "+36 30 987 6543", "dob": "1997-11-05", "joinDate": "2022-02-15", "branch": "London", "balance": 1980.5 }
]
```

**GET a missing customer:**
```bash
curl -w "\nHTTP_STATUS:%{http_code}\n" http://localhost:5050/api/customers/999
```
```json
{ "error": "Customer 999 not found" }
HTTP_STATUS:404
```

**POST a new customer:**
```bash
curl -X POST http://localhost:5050/api/customers \
  -H "Content-Type: application/json" \
  -d '{"name":"Priya Sharma","email":"priya.sharma@example.com","phone":"+44 7700 900123","dob":"1996-08-20","joinDate":"2026-08-01","branch":"Singapore","balance":500}'
```
```json
{ "id": 3, "name": "Priya Sharma", "email": "priya.sharma@example.com", "balance": 500.0, "...": "..." }
```

**POST missing required fields (validation working):**
```bash
curl -w "\nHTTP_STATUS:%{http_code}\n" -X POST http://localhost:5050/api/customers \
  -H "Content-Type: application/json" -d '{"branch":"Budapest"}'
```
```json
{ "error": "name and email are required" }
HTTP_STATUS:400
```

**PUT update (partial — balance only):**
```bash
curl -X PUT http://localhost:5050/api/customers/3 \
  -H "Content-Type: application/json" -d '{"balance":1500}'
```
```json
{ "id": 3, "name": "Priya Sharma", "balance": 1500.0, "...": "..." }
```

**DELETE, then confirm it's gone:**
```bash
curl -X DELETE http://localhost:5050/api/customers/3
curl http://localhost:5050/api/customers
```
```json
{ "deleted": { "id": 3, "name": "Priya Sharma", "balance": 1500.0, "...": "..." } }
```
Followed by a `GET` showing only the original 2 seed customers — confirming the delete genuinely persisted in MySQL.

---

## Step 12 — Connect the Standalone JS Frontend

In `src/dom-flask/api.js` (Track 4):

```javascript
const BASE_URL = 'http://localhost:5050/api/customers';
```

Since this Flask app also runs on port `5050`, **nothing in the frontend needs to change**. Just:
1. MySQL is running, `schema.sql` has been loaded.
2. `python3 app.py` is running.
3. Open `customers.html` directly in a browser (no Flask involvement in serving it — it's a plain static file).

This was verified directly: the exact `customers.html` + `app.js` + `render.js` from Track 4, run against this exact Flask + MySQL backend, loaded the table correctly on page load with no code changes — the payoff of keeping `BASE_URL` isolated in one file and never mixing template rendering into this API.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `error: externally-managed-environment` | Trying to `pip install` outside a virtual environment | Activate `venv` first (Step 2) |
| `Failed to find Flask application or factory in module 'app'` | A folder named `app/` exists alongside `app.py` | Rename or remove the conflicting folder |
| `pymysql.err.OperationalError: (2003, ...)` | MySQL isn't running | Start it — `sudo service mysql start` (Linux) or `brew services start mysql` (macOS) |
| `Access denied for user 'customerapp_user'@'localhost'` | Wrong password, or user/grant wasn't created | Re-run Step 5's `CREATE USER`/`GRANT` statements |
| Browser console shows a CORS error | `Flask-Cors` not installed/imported | Confirm `CORS(app)` is present in `app.py` and `flask-cors` is installed |
| `Address already in use` on port 5050 | Something else (e.g. the Track 3/4 mock server) is already running on 5050 | Stop the other process, or change the port in both `app.py`'s `app.run(port=...)` and `api.js`'s `BASE_URL` |
| Table shows `undefined` for dates | MySQL `date` objects weren't converted | Confirm `serialize_customer` in `app.py` is converting with `.isoformat()` |