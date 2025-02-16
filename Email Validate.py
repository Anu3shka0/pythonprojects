import tkinter as tk

digits = "0123456789"
allowed_sp ="@._"

root = tk.Tk()
root.title("Email Validator")
root.geometry("400x400")

tk.Label(root, text = "Enter your Email id: ").pack(pady=30)
entry = tk.Entry(root)
entry.pack(pady = 30)

def validate_email(email):
    if len(email)>6:
        if email.count("@")==1:
            if email.islower():
                if email[0] not in digits:
                    if email[-1] not in digits:
                        if all(c.isalnum() or c in allowed_sp for c in email):
                            if email.count(".")>0:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
def on_submit():
    email = entry.get()
    if validate_email(email):
        result_var.set("Email is Valid")
    else:
        result_var.set("Email is Invalid")
        
tk.Button(root, text= "Submit", command = on_submit).pack(pady=30)

result_var = tk.StringVar()
tk.Entry(root, textvariable = result_var, state = "readonly", width = 30).pack(pady=30)

root.mainloop()