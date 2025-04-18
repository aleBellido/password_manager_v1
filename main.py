import random
import string

def create_password():
    characters = string.digits + string.punctuation + string.ascii_letters
    platform = input('Platform (Discord, Github, X) --> ')
    length = int(input("Length (1 - 12) --> "))
    password = "".join(random.choices(characters, k=length))
    
    # Save password in a .txt file at the moment. It will be .json
    with open("passwords.txt", 'a') as file:
        file.write(str({platform: password}) + '\n')
    print('Password generated and saved!')

create_password()

def password_config():
    #capital_letters = input("Capital Letters? Y/n --> ").lower()
    #symbols = input("Symbols Y/n --> ").lower()
    #platform = input("Platform: ")
    pass


def menu():
    print("Welcome to Password Manager V1")
    print("1. Create Password\n 2. Delete Password\n 3. View Passwords\n 4. Exit")
    
    selection = int(input("--> "))
    
    if selection == 1:
        create_password()
    elif selection == 2:
        delete_password()
    elif selection == 3:
        view_passwords()
    elif selection == 4:
        print("Goodbye")