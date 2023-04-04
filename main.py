import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import sqlite3
import database
import crypto

###temp key#####
#KEY = b'mzItZH9CMtULeYtR-YLFtGcLZetP2Q0b0DGV1q3BCqU='
KEY = "730a107cecab83da37f6468d831dcdbbdedf156dc0c45bb037d4f7b0f31cf860"
################

print("database exist: ", database.check())
print("database create:", database.create())

def validation():
    if crypto.generate(password_entry.get()) == KEY:
        print("correct password")
        main_window.destroy() # kill the current window
        # create a new window with a text box
        new_window = tk.Tk()
        new_window.geometry("400x300")
        text_label = tk.Label(new_window, text="Enter your text:")
        text_label.pack()
        text_entry = tk.Entry(new_window, width=50)
        text_entry.pack()
        new_window.mainloop()
    else:
        print("wrong password")

main_window = tk.Tk()
main_window.title("Password Manager")
main_window.geometry("400x300")
password_lable = tk.Label(main_window, text="Master Password")
password_lable.pack()

password_entry = tk.Entry(main_window, show="*")
password_entry.pack()
add_button = tk.Button(main_window, text="submit", command=validation)
add_button.pack()


main_window.mainloop()