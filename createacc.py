class CreateAcc:
    def __init__(self, name="",password="", **kwargs):
        self.name = name

        for key,value in kwargs.items():
            setattr(self,key,value)