import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. HARDCODED SECRET (SAST Vulnerability for Semgrep to flag)
API_SECRET_KEY = "sk_live_99f8d7c6b5a413241" 

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, role) VALUES (1, 'admin', 'administrator')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    # 2. REFLECTED CROSS-SITE SCRIPTING / XSS (Unsanitized user input rendered directly into HTML string)
    name = request.args.get('name', 'Guest')
    template = f"<h1>Welcome, {name}!</h1><p>Search for a user using ?user=username</p>"
    return render_template_string(template)

@app.route('/search')
def search():
    # 3. SQL INJECTION / SQLi (Direct string formatting into a raw SQL query)
    username = request.args.get('user', '')
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    query = f"SELECT username, role FROM users WHERE username = '{username}'"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return f"Query executed: {query} <br> Results: {result}"
    except Exception as e:
        return f"Database Error: {e}"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)