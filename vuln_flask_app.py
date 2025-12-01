#TEST FILE 03

from flask import Flask, request
import subprocess
import sqlite3

app = Flask(__name__)

# SQL Injection (B608)
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
    return str(cursor.fetchall())

# Command Injection (B602, B607)
@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)

# Hardcoded secret key (B105)
app.config["SECRET_KEY"] = "mysecret123"

app.run()
