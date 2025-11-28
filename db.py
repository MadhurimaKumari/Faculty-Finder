import sqlite3

conn=sqlite3.connect('faculty.db')
cursor=conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS faculty(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            block TEXT NOT NULL,
            floor INT NOT NULL,
            cabin_no INT NOT NULL
        )
''')

cursor.execute("INSERT INTO faculty(id,name,department,block,floor,cabin_no) VALUES (1,'Anil','CSE','A',2,101)")
cursor.execute("INSERT INTO faculty(id,name,department,block,floor,cabin_no) VALUES (2,'Ram','AI-ML','AI',2,101)")
cursor.execute("INSERT INTO faculty(id,name,department,block,floor,cabin_no) VALUES (3,'Sunil','CSE','A',3,112)")
cursor.execute("INSERT INTO faculty(id,name,department,block,floor,cabin_no) VALUES (4,'Mohan','Law','B',1,123)")
cursor.execute("INSERT INTO faculty(id,name,department,block,floor,cabin_no) VALUES (5,'Sohan','CSE','A',2,103)")

conn.commit()
conn.close()
