import sqlite3

# Create or connect to the database
conn = sqlite3.connect('faculty.db')
cursor = conn.cursor()

# Create faculty table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        block TEXT NOT NULL,
        floor TEXT NOT NULL,
        cabin_no TEXT NOT NULL
    )
''')

# Insert sample data
sample_data = [
    ('Dr. John Smith', 'Computer Science', 'A', '2', '201'),
    ('Prof. Jane Doe', 'Electronics', 'B', '1', '102'),
    ('Dr. Michael Brown', 'Mechanical', 'C', '3', '305'),
    ('Prof. Sarah Wilson', 'Civil', 'A', '2', '206'),
    ('Dr. Robert Taylor', 'Electrical', 'B', '2', '204')
]

for data in sample_data:
    cursor.execute('INSERT INTO faculty (name, department, block, floor, cabin_no) VALUES (?, ?, ?, ?, ?)', data)

conn.commit()
conn.close()

print('Database created and populated successfully!')
