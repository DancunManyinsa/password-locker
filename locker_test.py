from locker import Credentials,UsersData
import unittest, pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for creating and authenticating credentials
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_user = Credentials(1,"richie","uiui")
    
    def tearDown(self):
        '''
        Cleans up after each test has run
        '''
        Credentials.users_list = []
    
    def test_init(self):
        '''
        Test case to test if the case has been initialized properly
        '''
        self.assertEqual(self.new_user.identify,1)
        self.assertEqual(self.new_user.user_name,"richie")
        self.assertEqual(self.new_user.password,"uiui")
    
    def test_create(self):
        '''
        Testing if the new credential is saved into the list
        '''
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list),1)
    
    def test_authenticate(self):
        '''
        Testing to check if the authenticate function can sign in a user properly
        '''
        self.new_user.create_account()
        test_account = Credentials(1,"Test","Password")
        test_account.create_account()

        found_user = Credentials.authenticate_account("Test","Password")
        self.assertEqual(found_user.identify , test_account.identify)

class TestUserData(unittest.TestCase):
    '''
    Test class that defines the test cases for creating websites log in credentials
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_data = UsersData(1,1,"facebook.com","poiii")
    
    def tearDown(self):
        '''
        Cleans up the test after test is complete
        '''
        UsersData.data_list = []
    
    def test_init(self):
        '''
        Test case to evaluate if the case has been initialized properly
        '''
        self.assertEqual(self.new_data.ident,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.website,"facebook.com")
        self.assertEqual(self.new_data.web_key,"poiii")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(UsersData.data_list),1)

    def test_display_data(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_data.add_password()
        test_data = UsersData(1,1,"facebook.com","poiii")
        test_data.add_password()

        data_found = UsersData.display_data(1,1)
        self.assertEqual(data_found.website,test_data.website)
    
    def test_data_exists(self):
        '''
        Testing to check if the function for checking data works well
        '''
        self.new_data.add_password()
        test_data = UsersData(1,1,"facebook.com","poiii")
        test_data.add_password()

        data_exists = UsersData.existing_data(1)
        self.assertTrue(data_exists)
    
    def test_copy_password(self):
        '''
        Testing if the copy password function works
        '''
        self.new_data.add_password()
        UsersData.copy_password(1,1)

        self.assertEqual(self.new_data.web_key,pyperclip.paste())


if __name__ == "__main__":
    unittest.main()