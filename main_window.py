import tkinter as tk
from tkinter import messagebox
import database

def create(KEY):
    def add_password_click():
        service = service_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        if not service or not username or not password:
           messagebox.showerror("Error", "Please enter all fields.")
        else:
            database.add_password(service, username, password, KEY)
            messagebox.showinfo("Success", "Password added.")
            service_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

    def view_passwords_click():
        passwords = database.read_passwords(KEY)
        if passwords:
            popup = tk.Toplevel()
            popup.geometry("400x300")
            popup.title("Passwords")
            passwords_text = "\n".join([f"{p[0]} | {p[1]} | {p[2]}" for p in passwords])
            passwords_label = tk.Label(popup, text=passwords_text)
            passwords_label.pack()

            def close_window():
                popup.destroy()
            close_button = tk.Button(popup, text="Close", command=close_window)
            close_button.pack()


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
    