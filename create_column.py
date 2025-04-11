import sqlite3

conn = sqlite3.connect('buspass.db')
cursor = conn.cursor()

# Add new column for file path
cursor.execute("ALTER TABLE applications ADD COLUMN id_path TEXT")

conn.commit()
conn.close()

print("✅ Column 'id_path' added to applications table.")
