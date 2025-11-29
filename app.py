from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from db import init_db

app = Flask(__name__)
CORS(app)
init_db()

DB_PATH = 'logs.db'

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# REST API to add a log
@app.route('/api/logs', methods=['POST'])
def add_log():
    data = request.json
    if not all(k in data for k in ('source','type','message','severity')):
        return jsonify({'error':'Missing fields'}), 400
    query_db('INSERT INTO logs (source,type,message,severity) VALUES (?,?,?,?)',
             (data['source'], data['type'], data['message'], data['severity']))
    return jsonify({'success': True})

# REST API to get logs
@app.route('/api/logs', methods=['GET'])
def get_logs():
    rows = query_db('SELECT * FROM logs ORDER BY timestamp DESC LIMIT 100')
    logs = [dict(row) for row in rows]
    return jsonify(logs)

# Dashboard
@app.route('/')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
