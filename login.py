import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(1)

print("""
            Welcome to the password locker app :) 
            You first of all need to create an account
            """)
