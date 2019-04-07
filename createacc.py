import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("""
            Welcome to the password locker app :) 
            You first of all need to create an account
            """)

class CreateAcc:
    def __init__(self, name="",password="", **kwargs):
        
        try:
            
            self.name= input(">Username:  ")
            self.password= input(">Password:  ")
            
            if int(len(self.name)) < 1:
                raise ValueError("Name is required")

            if int(len(self.password)) < 6:
                raise ValueError("Password must be 6 characters or more")

        except ValueError as err:
            print("""something went wrong, :(
                {} !!
                
                """.format(err))


        else:
            self.name = name
            self.password = password
            for key,value in kwargs.items():
                setattr(self,key,value)
            print("Your details have been saved")
            clear_screen()
    

        

        