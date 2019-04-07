import os
import time
from user import User
from credential import Credential

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("""
            Welcome to the password locker app :) 
            You first of all need to create an account
            """)

time.sleep(5)
clear_screen()

print("You will need a username and password")

time.sleep(2)
clear_screen()

name= input("Name: ")

time.sleep(3)
clear_screen()

password = input("Password:  ")


