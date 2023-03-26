import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import sqlite3
import database
import crypto

###temp key#####
KEY = b'mzItZH9CMtULeYtR-YLFtGcLZetP2Q0b0DGV1q3BCqU='
################

print("database check: ", database.check())
print("database create:", database.create())
def temp():
    print(password_entry.get())
    passs=crypto.generate(password_entry.get())
    print(passs)

main_window = tk.Tk()
main_window.title("Password Manager")
main_window.geometry("400x300")
password_lable = tk.Label(main_window, text="Master Password")
password_lable.pack()

password_entry = tk.Entry(main_window, show="*")
password_entry.pack()
add_button = tk.Button(main_window, text="submit", command=temp)
add_button.pack()


main_window.mainloop()