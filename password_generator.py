import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Use at least 4 characters!")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Password: {password}")
    except ValueError:
        result_label.config(text="Enter a valid number")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
