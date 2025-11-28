from flask import Flask, render_template, request, jsonify
import sqlite3
import json

app = Flask(__name__)
DATABASE = 'faculty.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/faculty')
def get_all_faculty():
    conn = get_db_connection()
    faculty = conn.execute('SELECT * FROM faculty').fetchall()
    conn.close()
    return jsonify([dict(f) for f in faculty])

@app.route('/api/faculty/<int:faculty_id>')
def get_faculty(faculty_id):
    conn = get_db_connection()
    faculty = conn.execute('SELECT * FROM faculty WHERE id = ?', (faculty_id,)).fetchone()
    conn.close()
    if faculty:
        return jsonify(dict(faculty))
    else:
        return jsonify({'error': 'Faculty not found'}), 404

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    faculty = conn.execute('SELECT * FROM faculty WHERE name LIKE ?', ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('result.html', faculty=faculty, query=query)

if __name__ == '__main__':
    app.run(debug=True)
