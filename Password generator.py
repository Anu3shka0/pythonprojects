import tkinter as tk
import random
import string

def generate_password():
    length = int(entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

# Label and Entry for password length
tk.Label(root, text="Enter Password Length:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Button to generate password
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Display the password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, state="readonly", width=30).pack(pady=10)

# Run the application
root.mainloop()
