import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import database
import crypto
import main_window
import signup_window

def create():

    #checks whether generated key and database saved key are same
    def validation():
        generated_key = crypto.generate(master_password_entry.get())
        if generated_key == KEY:
            login_window.destroy() 
            main_window.create(KEY) 
        else:
            messagebox.showinfo("Error", "Wrong Password")

    login_window = tk.Tk()
    login_window.title("Password Manager")
    login_window.geometry("400x300")
    password_lable = tk.Label(login_window, text="Master Password")
    password_lable.pack()
    master_password_entry = tk.Entry(login_window, show="*")
    master_password_entry.pack()
    def enter(event):
        command=validation()
    # bind enter key to validate function
    master_password_entry.bind('<Return>',enter)
    add_button = tk.Button(login_window, text="submit", command=validation)
    add_button.pack()

    login_window.mainloop()

# check whether database is exist or not
if database.check()== True:
    print("database exist")
    KEY=database.getkey()
    KEY=KEY[2:-1].encode('utf-8')
    create()
else:
    print("database not exist")
    signup_window.create()