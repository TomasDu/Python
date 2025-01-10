import json
import re
import os

# Determine file path based on operating system
if os.name == 'nt':  # Windows
    file_path = 'users.json'
else:  # Linux and others
    file_path = './users.json'

def load_users():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)

def password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    return "Strong"

def add_new_user(users):
    name = input("What is your name: ")
    
    while True:
        password = input("Enter a password: ")
        strength = password_strength(password)
        if strength == "Strong":
            break
        print(strength)

    user_id = len(users) + 1
    balance = 0
    
    user = {
        'id': user_id,
        'name': name,
        'password': password,
        'balance': balance
    }
    
    users.append(user)
    save_users(users)
    print(f"Welcome {name}, your current balance is $0. Your user ID is {user_id}.")

def existing_user(users):
    name = input('What is your name?: ')
    password = input('Enter your password: ')
    
    for user in users:
        if name == user['name'] and password == user['password']:
            print(f"Welcome {name}, your current balance is ${user['balance']}. Your user ID is {user['id']}.")
            return user
    print('No such user exists or incorrect password.')
    return None

def add_balance(users, user):
    if not user:
        return

    try:
        amount = float(input("Enter the amount to add: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        user['balance'] += amount
        save_users(users)
        print(f"${amount} has been added to your account. Your new balance is ${user['balance']}.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def main():
    users = load_users()
    new_user = input("Are you a new user? (yes/no): ").strip().lower()
    
    if new_user == "yes":
        add_new_user(users)
    elif new_user == "no":
        user = existing_user(users)
        if user:
            add_balance(users, user)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
