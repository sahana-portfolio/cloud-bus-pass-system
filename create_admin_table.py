import sqlite3

# Connect to DB
conn = sqlite3.connect('buspass.db')
cursor = conn.cursor()

# Create admin table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert a sample admin
cursor.execute("INSERT INTO admins (username, password) VALUES (?, ?)", ("admin", "admin123"))

conn.commit()
conn.close()

print("✅ Admin table created and admin user added.")
