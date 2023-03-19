import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import sqlite3
import database

print("database check: ",database.check())
print("database create:",database.create())


main_window = tk.Tk()
main_window.title("Password Manager")
main_window.geometry("400x300")
password_lable = tk.Label(main_window, text="Master Password")
password_lable.pack()

main_window.mainloop()