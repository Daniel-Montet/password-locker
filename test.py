#Create a pwd locker account with a username and password
    #username should be str
    #password should not be less than 6 characters
import unittest

from credential import Credential
from login import add_credential

class CreateTest(unittest.TestCase):
    
    def setUp(self):
        self.new_account= Credential("","")

    
    def test_login(self):
        self.assertEqual(self.new_account.name,self.new_account.name)
        self.assertEqual(self.new_account.password,self.new_account.password)
    
    
    def test_addcredential(self):
        self.new_account.account.update({"login": ["don", "123456"]})
        self.assertTrue(len(self.new_account.account)==1)

    

if __name__=='__main__':
    unittest.main()