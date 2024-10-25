import json

file_path = 'users.json'

try:
    with open(file_path, 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

curency = '$'
new_user = input("Are you a new user? (yes/no): ").strip().lower()

if new_user == "yes":
    name = input("What is your name: ")
    
    user_id = len(users) + 1
    
    balance = 0
    
    user = {
        'id': user_id,
        'name': name,
        'balance': balance
    }
    
    # Add user to list
    users.append(user)

    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)
    
    # welcome msg
    print(f"Welcome {name}, your current balance is {curency}{balance}. Your user ID is {user_id}.")

if new_user == 'no':
    name = input('What is your name?: ')
    
    user_found = False
    

    for user in users:
        if name == user['name']:
            
            print(f"Welcome {name}, your current balance is {curency}{user['balance']}. Your user ID is {user['id']}.")
            user_found = True
            break
    
    if not user_found:
        print('No such user exists.')
