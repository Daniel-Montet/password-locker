from user import User

class Credential(User):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for key,value in kwargs.items():
            setattr(self,key,value)