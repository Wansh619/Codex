import base64
import sqlite3
import tempfile
import os
import json

# Paste your Base64 SQLite content here
def get_data():
    with open('data.json' ) as f:
        data=json.load(f) 
        return data['data']
# Decode and save DB
db_bytes = base64.b64decode(get_data())

with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as f:
    f.write(db_bytes)
    db_path = f.name

print(f"Database saved at: {db_path}")

# Open SQLite DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\nTables:")
for table in tables:
    print("-", table[0])

# Example: print contents of each table
for table in tables:
    table_name = table[0]
    print(f"\n=== {table_name} ===")

    try:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)

conn.close()
os.unlink(db_path)