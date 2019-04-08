from user import User

class Credential(User):
    """
    Extend User class and accept any number of arguments
    """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for key,value in kwargs.items():
            setattr(self,key,value)