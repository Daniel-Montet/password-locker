#Create a pwd locker account with a username and password
    #username should be str
    #password should not be less than 6 characters
import unittest
from createacc import CreateAcc


class CreateTest(unittest.TestCase):

    def setUp(self):
        self.new_account= CreateAcc("Daniel")
    
    def test_init(self):
        self.assertEqual(self.new_account.name,"Daniel") 

if __name__=='__main__':
    unittest.main()