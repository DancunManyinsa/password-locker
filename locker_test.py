from locker import Credentials,UsersDat
import unittest, pyperclip

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
       
        self.new_user = Credentials(1,"Dan","programmer")
    
    def tearDown(self):
        
        Credentials.users_list = []
    
    def test_init(self):
        
        self.assertEqual(self.new_user.identify,1)
        self.assertEqual(self.new_user.user_name,"Dan")
        self.assertEqual(self.new_user.password,"programmer")
    
    def test_create(self):
       
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list),1)
    
    def test_authenticate(self):
        
        self.new_user.create_account()
        test_account = Credentials(1,"Test","Password")
        test_account.create_account()

        found_user = Credentials.authenticate_account("Test","Password")
        self.assertEqual(found_user.identify , test_account.identify)

class TestUserData(unittest.TestCase):
   
    def setUp(self):
        
        self.new_data = UsersData(1,1,"twitter.com","programmer")
    
    def tearDown(self):
        
        UsersData.data_list = []
    
    def test_init(self):
        
        self.assertEqual(self.new_data.ident,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.website,"twitter.com")
        self.assertEqual(self.new_data.web_key,"programmer")

    def test_add_password(self):
        
        self.new_data.add_password()
        self.assertEqual(len(UsersData.data_list),1)

    def test_display_data(self):
        
        self.new_data.add_password()
        test_data = UsersData(1,1,"twitter.com","programmer")
        test_data.add_password()

        data_found = UsersData.display_data(1,1)
        self.assertEqual(data_found.website,test_data.website)
    
    def test_data_exists(self):
       
        self.new_data.add_password()
        test_data = UsersData(1,1,"twitter.com","programmer")
        test_data.add_password()

        data_exists = UsersData.existing_data(1)
        self.assertTrue(data_exists)
    
    def test_copy_password(self):
       
        self.new_data.add_password()
        UsersData.copy_password(1,1)

        self.assertEqual(self.new_data.web_key,pyperclip.paste())


if __name__ == "__main__":
    unittest.main()
