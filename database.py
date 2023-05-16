import os;
import sqlite3;
import crypto;

# checks whether there password.db is in current directory
def check():
    if os.path.isfile('passwords.db') and os.path.getsize('passwords.db') > 0:
        db_exists=True
    else:
        db_exists=False
    return db_exists

def create():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  key TEXT NOT NULL,
                  service TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def getkey():
    # gets the key form the passwords.db
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT key FROM passwords")
    rows=str(c.fetchone())
    KEY=rows.strip("(),")
    conn.close()
    return KEY

def add_password(service, username, password, KEY):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    encrypted_service = crypto.encrypt(service,KEY)
    encrypted_username = crypto.encrypt(username,KEY)
    encrypted_password = crypto.encrypt(password,KEY)
    c.execute("INSERT INTO passwords (key, service, username, password) VALUES (?, ?, ?, ?)",
              (KEY,encrypted_service, encrypted_username, encrypted_password))
    conn.commit()
    conn.close()

def read_passwords(KEY):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT service, username, password FROM passwords")
    rows = c.fetchall()
    passwords = []
    for row in rows:
        service = crypto.decrypt(row[0],KEY).strip()
        username = crypto.decrypt(row[1],KEY).strip()
        password = crypto.decrypt(row[2],KEY).strip()
        passwords.append((service, username, password))
    conn.close()
    return passwords
    