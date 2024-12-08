import random
import string
import tkinter as tk

def generate_password():
    special_char = '!@#$%^&*()_+-.<>?'
    capital_letter = random.choice(string.ascii_uppercase)
    digits = string.digits
    letters = string.ascii_lowercase
    special = random.choice(special_char)

    password = random.choices(letters, k=6) + [capital_letter] + [special] + random.choices(digits, k=2)
    random.shuffle(password)
    return ''.join(password)

def generate_and_display_password():
    generated_password = generate_password()
    password_var.set(generated_password)

root = tk.Tk()
root.title("Password Generator")

password_var = tk.StringVar()
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)

password_display = tk.Entry(root, textvariable=password_var, state='readonly')
password_display.pack(padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

root.mainloop()
