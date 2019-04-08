import unittest
from credential import Credential
from login import add_credential



class CreateTest(unittest.TestCase):
    
    def setUp(self):
        """
        Instanciate the user account creation

        """
        self.new_account= Credential("montet","123456")

    
    def test_login(self):
        """
        Test login functionality
        """
        self.assertEqual(self.new_account.name,"montet")
        self.assertEqual(self.new_account.password,"123456")
    
    
    def test_addcredential(self):
        """
        Test if an instance is able to save its keyword arguments to its dictionary thats set on init
        """
        self.new_account.account.update({"login": ["don", "123456"]})
        self.assertTrue(len(self.new_account.account)==1)

    def test_delcredential(self):
        """
        Test if a user can delete a key from its particular dictionary
        """
        self.new_account.account.update({"login": ["don", "123456"]})
        del self.new_account.account["login"]
        self.assertTrue(len(self.new_account.account)==0)

   

if __name__=='__main__':
    unittest.main()