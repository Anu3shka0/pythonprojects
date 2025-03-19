import re
email_cond = "^[a-z0-9]+[\._]?[a-z 0-9]+@[a-z]\w+[.]\w"
def validate_email(email):
    if re.search(email_cond,email):
        print("Valid Email")
    else:
        print("Invalid Email")
    
user_email = input("Enter your email: ")
print(validate_email(user_email)) # Output: True
