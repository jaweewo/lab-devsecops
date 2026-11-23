import os
import sqlite3
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# VULNERABILIDAD 1 (Lab 1 - Secreto expuesto en el código):
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"



@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# VULNERABILIDAD 2 (Lab 2 - SQL Injection - Slide 264):
@app.route("/usuario")
def buscar_usuario():
    username = request.args.get("username", "")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INT, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin')")

    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)
    return jsonify({"resultado": cursor.fetchall()})


# VULNERABILIDAD 3 (Lab 2 - Command Injection):
@app.route("/ping")
def ping_host():
    host = request.args.get("host", "127.0.0.1")
    salida = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return jsonify({"salida": salida.decode()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)