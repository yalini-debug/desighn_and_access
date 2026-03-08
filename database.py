import sqlite3

def init_db():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("INSERT INTO users (username,password,role) VALUES ('admin','admin123','admin')")
    cursor.execute("INSERT INTO users (username,password,role) VALUES ('employee','emp123','employee')")
    cursor.execute("INSERT INTO users (username,password,role) VALUES ('contractor','con123','contractor')")

    conn.commit()
    conn.close()