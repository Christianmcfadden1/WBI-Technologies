from flask import Flask, request, redirect, render_template
import sqlite3
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    
    if user:
        return render_template("welcome.html")
    else:
        return render_template("error.html")

if __name__ == '__main__':
  conn = sqlite3.connect("users.db")
  c = conn.cursor()
  c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text)")
  c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin"))
  conn.commit()
  conn.close()
  app.run(host='0.0.0.0',  port=random.randint(2000, 9000))