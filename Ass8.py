import hashlib

def register_user(name, email, password):
    if "@" not in email:
        print("Invalid Email")
        return

    if len(password) < 8:
        print("Password too short")
        return

    hashed = hashlib.sha256(password.encode()).hexdigest()

    print("Registration Successful")
    print("Name:", name)
    print("Email:", email)
    print("Hashed Password:", hashed)

name = input("Enter Name: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

register_user(name, email, password)