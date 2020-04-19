#!/usr/bin/env python3.6
from locker import Credentials # Importing the credentials class

def create_credentials(account,username,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    Function that finds a credential by account and returns the credentials
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if a credential exists with that account and return a Boolean
    '''
    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

# def copy_password():
#     '''
#     Function that allows copy and paste the password to the clipboard
#     '''
#     return Credentials.copy_password()

# def main():
#             print("Hello Welcome to your credentials list. What is your name?")
#             user_name = input()

#             print(f"Hello {user_name}. what would you like to do?")
#             print('\n')

#             while True:
#                     print(f"Use these short codes below to:\n cc - create a new credentials,\n dc - display credentials,\n fc -find credentials,\n rc - Deleting credentials,\n cp - Copying a credentials password,\n ex -exit the credentials list ")
#                     print("\n")
#                     short_code = input().lower()

#                     if short_code == 'cc':
#                             print("Create new Credentials")
#                             print("-"*10)

#                             print(" Account ...")
#                             account = input()

#                             print(f"\n username ...")
#                             username = input()

#                             print("\n password ...")
#                             password = input()


#                             save_credentials(create_credentials(account,username,password)) # create and save new credentials.
#                             print ('\n')
#                             print(f"New Credentials for {account}  username: {username}  password: {password} created")
#                             print ('\n')

#                     elif short_code == 'dc':

#                             if display_credentials():
#                                     print("Here is a list of all your credentials")
#                                     print('\n')

#                                     for credentials in display_credentials():
#                                             print(f"account:{credentials.account}  username:{credentials.username}  password:{credentials.password}")

#                                     print('\n')
#                             else:
#                                     print('\n')
#                                     print("You dont seem to have any credentials saved yet")
#                                     print('\n')

#                     elif short_code == 'fc':

#                             print(f"Enter the account you want to search for \n")

#                             search_account = input()
#                             if check_existing_credentials(search_account):
#                                     search_credentials = find_credentials(search_account)
#                                     print(f"Account:{search_credentials.account}  username:{search_account.username}  password:{search_account.password}")
#                                     print('-' * 20)

                                  
#                             else:
#                                     print("Account does not exist")
                                
#                     # elif short_code == 'fc':

#                     #     print("Enter the account you want to delete")


#                     # elif short_code == 'fc':
#                     #     print("Enter the account you want to copy")

#                     elif short_code == "ex":
#                             print("Bye .......")
#                             break
#                     else:
#                             print("I really didn't get that. Please use the short codes")

# if __name__ == '__main__':

#     main()