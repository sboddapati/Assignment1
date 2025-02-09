import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password length should be at least 8 characters"
    if not re.search("[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter"
    if not re.search("[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter"
    if not re.search("[0-9]", password):
        return "Weak: Password should contain at least one digit"
    if not re.search("[!@#$%^&*]", password):
        return "Weak: Password should contain at least one special character"
    return True

def main():
    password = input("Enter the password: ")
    result = check_password_strength(password)
    if result == True:
        print("Strong password")
    else:
        print(result)
        
if __name__ == "__main__":
    main()
