import os
import sys
import time
import random
import string
from user import User
from credential import Credential


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("""
            Welcome to the password locker app :) 
            You first of all need to create an account
            """)

time.sleep(2)
clear_screen()

print("You will need a username and password")

time.sleep(2)
clear_screen()

name = input("Name: ")

time.sleep(1)
clear_screen()

password = input("Password:  ")

time.sleep(1)
clear_screen()

print("Your have successfully created an account")

createduser = Credential(name, password)
createduser.account.update({"login": [name, password]})

time.sleep(1)
clear_screen()

print("Log in to continue :)")


def add_credential(social, username, password):
    createduser.account.update({social: [username, password]})


def generate_password(stringLength):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    password = ''.join(random.choice(lettersAndDigits)
                       for i in range(stringLength))
    add_credential(social, username, password)
    print(">Generated password: {}".format(password))
    return

def del_credential(credentialname):
    del createduser.account[credentialname]
    return


while True:
    loginname = input(">Username:  ")
    loginpwd = input(">Password:  ")

    try:
        if loginname != createduser.account['login'][0]:
            raise ValueError("This is not a recognised user name !!")
            continue
        if loginpwd != createduser.account['login'][1]:
            raise ValueError("Incorrect password !!")
            continue
    except ValueError as err:
        print("""Something is wrong :(
            {}
            
            """.format(err))
    else:
        print("Welcome {}. You have successfully logged in".format(name))
        break


while True:
    print("""
    Enter a credential you need added:
    Enter 'EXIT' to exit

    """)
    social = input("> Social name e.g. Facebook:   ")
    username = input("> Username:  ")
    socialpwd = input(
        "> Password: Enter 'auto' to autogenerate a password: >   ")
    if social == 'EXIT':
        sys.exit()
        break
    elif socialpwd == 'auto':
        length = int(input("How long do you want the password to be?  "))
        print("Please wait as we generate password for you")
        generate_password(length)

    else:
        add_credential(social, username, socialpwd)
        print("credential added")
        option = input(""" Enter 'VIEW' to see credentials
        
        Enter 'DEL' to delete a credential
        Enter 'EXIT' to quit program
        
        """)

        if option == 'VIEW':
            search = input(">Enter social name to search for: ")
            print("Here are the credentials: {}".format(
                createduser.account[search]))
        elif option == 'DEL':
            todelete = input("> Enter social name to delete: ")
            del_credential(todelete)
            print("You have successfully deleted {}".format(todelete))

        else:
            print("Good Bye")
            sys.exit()
    continue
