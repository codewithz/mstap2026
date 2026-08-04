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