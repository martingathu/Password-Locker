import pyperclip # Pyperclip will allow us to copy and paste items to our clipboard 
class User:
    """
    Class that generates new instances of users
    """
    users_list = [] #empty users list

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.users_list.append(self)

    @classmethod
    def user_exist(cls, user_name, password):
        '''
        Method that checks if a user exists from the users list.
        Args:
            user_name: user name to search if it exists
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return True

        return False

class Credentials:
    """
    Class that generates new instances of Credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,account,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account: New credentials account name.
            username : New credentials password.
            password: New credentials password.
           
        '''
        self.account = account
        self.username = username
        self.password = password
        
    
    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
       
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a account and returns a credentials that matches that account.

        Args:
            account: account to search for
        Returns :
            credentials of account that matches the account.
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def credentials_exist(cls,account):
        '''
        Method that checks if an account credential exists from the credentials list.
        Args:
            account: account to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    
    @classmethod
    def copy_password(cls,account):
        '''
        method that copies a credentials infor after the account name is entered
        '''
        credentials_found = Credentials.find_by_account(account)
        pyperclip.copy(credentials_found.password)

    