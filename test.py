#Create a pwd locker account with a username and password
    #username should be str
    #password should not be less than 6 characters
import unittest
from createacc import CreateAcc


class CreateTest(unittest.TestCase):
    values=[]
    def setUp(self):
        self.new_account= CreateAcc("","")
    
    def test_init(self):
        self.assertEqual(self.new_account.name,self.new_account.name)
        self.assertEqual(self.new_account.password,self.new_account.password)
    
    #def test_err(self):
       # with self.assertRaises(ValueError):
        #    self.new_account.password

    def test_login(self):
        self.values.append(self.new_account.name)
        self.values.append(self.new_account.password)
        self.assertEqual(self.values[0],self.new_account.name)
        self.assertEqual(self.values[1],self.new_account.password)
        print(self.new_account.name)

if __name__=='__main__':
    unittest.main()