import unittest # Importing the unittest module
from locker import Credentials # Importing the credentials class
import pyperclip # Pyperclip will allow us to copy and paste items to our clipboard 

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
        '''
        tearDown method that does clean up after test case has run
        '''
        Credentials.credentials_list=[]

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Instagram","martingathu","mypassword") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"Instagram")
        self.assertEqual(self.new_credentials.username,"martingathu")
        self.assertEqual(self.new_credentials.password,"mypassword")
        
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","username","123pass") # new credential
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","username","123pass") # new credentials
            test_credentials.save_credentials()
            
            self.new_credentials.delete_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_account(self):
        '''
        test to check if we can find a credentials by account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","username","123passw") # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account("Test")

        self.assertEqual(found_credentials.account,test_credentials.account)
    
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","username","123pas",) # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Test")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    # def test_copy_username(self):
    #     '''
    #     Test to confirm that we are copying the username from a found account
    #     '''

    #     self.new_credentials.save_credentials()
    #     Credentials.copy_username("martingathu")

    #     self.assertEqual(self.new_credentials.password,pyperclip.paste())

    # def test_copy_password(self):
    #     '''
    #     Test to confirm that we are copying the password from a found account
    #     '''

    #     self.new_credentials.save_credentials()
    #     Credentials.copy_password("mypassword")

    #     self.assertEqual(self.new_credentials.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()