import random
import tkinter as tk
from tkinter import messagebox
import pyperclip
import re

def generate_password():
    nr_letters = int(letters_entry.get())
    nr_numbers = int(numbers_entry.get())
    nr_symbols = int(symbols_entry.get())

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    password_list = []

    # Generating the password
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''.join(password_list)

    messagebox.showinfo("Generated Password", f"Your password is: {password}")

    password_strength = check_strength(password)
    messagebox.showinfo("Password Strength", f"Password strength: {password_strength}")

    save_password_to_file(password)

    copy_to_clipboard(password)

def check_strength(password):
    length = len(password)
    if length < 8:
        return "Weak"
    if re.search(r'[A-Z]', password) and re.search(r'[0-9]', password):
        return "Strong"
    return "Medium"

def save_password_to_file(password):
    with open("password.txt", "w") as file:
        file.write(password)

def copy_to_clipboard(password):
    pyperclip.copy(password)

def create_gui():
    global letters_entry, numbers_entry, symbols_entry

    window = tk.Tk()
    window.title("Password Generator")

    label_letters = tk.Label(window, text="Enter number of letters:")
    label_letters.pack()
    letters_entry = tk.Entry(window)
    letters_entry.pack()

    label_numbers = tk.Label(window, text="Enter number of numbers:")
    label_numbers.pack()
    numbers_entry = tk.Entry(window)
    numbers_entry.pack()

    label_symbols = tk.Label(window, text="Enter number of symbols:")
    label_symbols.pack()
    symbols_entry = tk.Entry(window)
    symbols_entry.pack()

    button = tk.Button(window, text="Generate Password", command=generate_password)
    button.pack()

    window.mainloop()

create_gui()
