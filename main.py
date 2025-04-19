import random
import string
import json
import os

FILE = 'passwords.json'

def load_passwords():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, 'r') as file:
        return json.load(file)
    
def save_passwords(data):
    with open(FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_password():
    try:
        length = int(input("Length (1 - 20) --> "))
        if not 1 <= length <= 20:
            print("Invalid length. Must be between 1 and 20.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    platform = input("Platform (Discord, Github, X) --> ").capitalize()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=length))

    passwords = load_passwords()
    passwords[platform] = password
    save_passwords(passwords)
    
    print(f"✅ Password for {platform} generated and saved!")

def view_passwords():
    passwords = load_passwords()
    if not passwords:
        print("No passwords saved yet.")
        return
    print("\n--- SAVED PASSWORDS ---")
    for platform, password in passwords.items():
        print(f"{platform}: {password}")

def password_config():
    #capital_letters = input("Capital Letters? Y/n --> ").lower()
    #symbols = input("Symbols Y/n --> ").lower()
    #platform = input("Platform: ")
    pass

def menu():
    while True:
        print("\nWelcome to Password Manager v1")
        print("1. Create Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        option = input("--> ")
        if option == "1":
            create_password()
        elif option == "2":
            view_passwords()
        elif option == "3":
            delete_password()
        elif option == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

menu()