import tkinter as tk
import string
import random


def generate_password():
    global password_entry
    length = int(length_entry.get())
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def reset_password():
    global password_entry
    password_entry.delete(0, tk.END)

def accept_password():
    global password_entry
    password = password_entry.get()
    print(f"Accepted password: {password}")

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for i in range(length))

root = tk.Tk()
root.title("Password Generator")

username_label = tk.Label(root, text="User Name:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=1, column=0, padx=5, pady=5)
length_entry = tk.Spinbox(root, from_=1, to=100, width=5)
length_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
password_entry.grid(row=2, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset Password", command=reset_password)
reset_button.grid(row=3, column=1, padx=5, pady=5)

accept_button = tk.Button(root, text="Accept Password", command=accept_password)
accept_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()