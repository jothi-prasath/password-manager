import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import database
import crypto
import main_window

###temp key#####
#KEY = b'mzItZH9CMtULeYtR-YLFtGcLZetP2Q0b0DGV1q3BCqU='
#KEY = "730a107cecab83da37f6468d831dcdbbdedf156dc0c45bb037d4f7b0f31cf860"  ### ==>test
KEY = b'n4bQgYhMfWWaL-qgxVrQFaO_TxsrC4Is0V1sFbDwCgg='
################

print("database exist: ", database.check())
print("database create:", database.create())

def validation():
    if crypto.generate(master_password_entry.get()) == KEY:
        print("correct password")
        login_window.destroy() 
        main_window.create(KEY) 

    else:
        print("wrong password")

login_window = tk.Tk()
login_window.title("Password Manager")
login_window.geometry("400x300")
password_lable = tk.Label(login_window, text="Master Password")
password_lable.pack()

master_password_entry = tk.Entry(login_window, show="*")
master_password_entry.pack()
add_button = tk.Button(login_window, text="submit", command=validation)
add_button.pack()


login_window.mainloop()