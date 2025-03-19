import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

tk.Label(root, text = "Enter your choice: ").pack(pady=20)
entry = tk.Entry(root)

entry.pack(pady = 20)

def rps():
    try:
        if entry.get().lower() in ["rock", "paper", "scissors"]:
            return True
        else:
            return False
    except:
        return False

def on_submit():
    if rps():
        user_choice = entry.get().lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result_var.set(f"Computer's choice: {computer_choice}")
        if user_choice == computer_choice:
            result_var.set("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            result_var.set("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            result_var.set("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            result_var.set("You win!")
        else:
            result_var.set("Computer wins!")
    else:
        result_var.set("Invalid Choice")
        
tk.Button(root, text= "Submit", command = on_submit).pack(pady=20)

result_var = tk.StringVar()
tk.Entry(root, textvariable = result_var, state = "readonly", width = 30).pack(pady=20)

root.mainloop()
# In this snippet, we have created a simple Rock Paper Scissors game using Tkinter.
# The user can enter their choice in the entry widget and click the submit button to see the result.
