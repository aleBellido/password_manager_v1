import random
import string

def create_password():
    characters = string.digits + string.punctuation + string.ascii_letters # Lower, upper, numbers and symbols combined
    password= []
    lenght = int(input("Lenght (1 - 12) --> "))
    
    for i in range(lenght):
        password.append(random.choice(characters))

    password = "".join(password)
    return password
        
print(f'Password Generated --> {create_password()}' ) # Temporal comprobation

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