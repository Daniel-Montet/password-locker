class User:
    
    def __init__(self, name="",password="", account={},**kwargs):
        self.name=name
        self.password=password
        self.account=account