import sqlite3

conn = sqlite3.connect('buspass.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    college TEXT NOT NULL,
    route TEXT NOT NULL,
    duration TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("✅ Database and table created successfully!")
