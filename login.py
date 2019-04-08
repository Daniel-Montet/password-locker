import os
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

#time.sleep(2)
#clear_screen()

print("You will need a username and password")

#time.sleep(2)
#clear_screen()

name= input("Name: ")

#time.sleep(1)
#clear_screen()

password = input("Password:  ")

#time.sleep(1)
#clear_screen()

print("Your have successfully created an account")

createduser= Credential(name,password)
createduser.account.update({"login":[name,password]})

#time.sleep(1)
#clear_screen()

print("Log in to continue :)")

def add_credential(social,username,password):
    createduser.account.update({social:[username,password]})
def display_credential(social):
    return social
def delete_credential(social):

def generate_password(stringLength):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    password=''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    return password


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

print("""
Enter a credential you need added:

""")

social= input("> Social name e.g. Facebook:   ")
username= input("> Username:  ")
socialpwd= input("> Password: Enter 'auto' to autogenerate a password: >   ")

while True:
    if socialpwd == 'auto':
        print("Please wait as we generate password for you")



