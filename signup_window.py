import tkinter as tk
from tkinter import messagebox
import crypto
import database
import main_window

def create():
    def validation():
        password1 = password1_entry.get()
        password2 = password2_entry.get()
        # checks password1 and password2 field are filled
        if not password1 or not password2:
            messagebox.showerror("Error", "Please enter all fields.")
        # checks password1 and password2 are not same
        elif (password1 != password2):
            messagebox.showerror("Error", "Passwords missmatch.")
        else:
            KEY = crypto.generate(password1)
            database.create()
            signup_window.destroy()
            main_window.create(KEY)

    
    signup_window = tk.Tk()
    signup_window.title("Password Manager")
    signup_window.geometry("400x300")
    password_label = tk.Label(signup_window, text="Password")
    password_label.pack()
    password1_entry = tk.Entry(signup_window, show="*")
    password1_entry.pack()
    repassword_label = tk.Label(signup_window, text="Re-enter Password")
    repassword_label.pack()
    password2_entry = tk.Entry(signup_window, show="*")
    password2_entry.pack()
    submit = tk.Button(signup_window, text="submit", command=validation)
    submit.pack()
    signup_window.mainloop()    