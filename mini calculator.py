import tkinter as tk

root = tk.Tk()
root.title("Mini Calculator")
root.geometry("400x400")

tk.Label(root, text = "Enter the expression: ").pack(pady=20)
entry = tk.Entry(root)
entry.pack(pady = 20)

def cal():
    try:
        eval(entry.get())
        return True
    except:
        return False
    
def on_submit():
    if cal():
        result_var.set(eval(entry.get()))
    else:
        result_var.set("Invalid Expression")

tk.Button(root, text= "Submit", command = on_submit).pack(pady=20)

result_var = tk.StringVar() 
tk.Entry(root, textvariable = result_var, state = "readonly", width = 30).pack(pady=20)

root.mainloop()
