from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('faculty.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/faculty')
def get_faculty():
    conn = get_db_connection()
    faculty = conn.execute('SELECT * FROM faculty').fetchall()
    conn.close()
    return jsonify([dict(row) for row in faculty])

@app.route('/api/faculty/<int:id>')
def get_faculty_by_id(id):
    conn = get_db_connection()
    faculty = conn.execute('SELECT * FROM faculty WHERE id = ?', (id,)).fetchone()
    conn.close()
    if faculty is None:
        return jsonify({'error': 'Faculty not found'}), 404
    return jsonify(dict(faculty))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    faculty = conn.execute('SELECT * FROM faculty WHERE name LIKE ?',
                          ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('result.html', faculty=faculty, query=query)

if __name__ == '__main__':
    app.run(debug=True)
