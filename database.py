import os
import sqlite3
import crypto

def check():
    if os.path.isfile('passwords.db') and os.path.getsize('password.db') > 0:
        db_exists=True
    else:
        db_exists=False
    return db_exists

def create():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  service TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_password(service, username, password):
    conn = sqlite3.connect()
    c = conn.cursor()
    encrypted_service = crypto.encrypt(service)
    encrypted_username = crypto.encrypt(username)
    encrypted_password = crypto.encrypt(password)
    c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
              (encrypted_service, encrypted_username, encrypted_password))
    conn.commit()
    conn.close()
    
    