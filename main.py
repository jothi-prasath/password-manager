import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import sqlite3
import database
import crypto

###temp key#####
#KEY = b'mzItZH9CMtULeYtR-YLFtGcLZetP2Q0b0DGV1q3BCqU='
KEY = "730a107cecab83da37f6468d831dcdbbdedf156dc0c45bb037d4f7b0f31cf860"  ### ==>test
################

print("database exist: ", database.check())
print("database create:", database.create())

def add_password_click():
    print("add password click")
def view_passwords_click():
    print("view passwords click")

def validation():
    if crypto.generate(master_password_entry.get()) == KEY:
        print("correct password")
        login_window.destroy() 
        main_window = tk.Tk()
        main_window.title("Password Manager")
        main_window.geometry("400x300")
        service_label = tk.Label(main_window, text="Service")
        service_label.pack()
        service_entry = tk.Entry(main_window)
        service_entry.pack()

        username_label = tk.Label(main_window, text="Username")
        username_label.pack()
        username_entry = tk.Entry(main_window)
        username_entry.pack()

        password_label = tk.Label(main_window, text="Password")
        password_label.pack()
        password_entry = tk.Entry(main_window, show="*")
        password_entry.pack()

        add_button = tk.Button(main_window, text="Add Password", command=add_password_click)
        add_button.pack()

        view_button = tk.Button(main_window, text="View Passwords", command=view_passwords_click)
        view_button.pack()
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