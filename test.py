#Create a pwd locker account with a username and password
    #username should be str
    #password should not be less than 6 characters
import unittest

class CreateTest(unittest.TestCase):

    def SetUp(self):
        self.account= CreateAcc(name="Daniel",password="155637339")
    