# Password Locker
#### By **Karanja Martin Gathu** 17TH April 2020
## Description
Password Locker is a python application run in the terminal that allows users to store details such as usernames and passwords for various accounts.

## SetUp / Installation Requirements
### Prerequisites
* python 3.6
* pip

### Cloning
* In your terminal:
        
        $ git clone https://martingathu.github.io/Password-Locker
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 locker_test.py

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Do you want to sign up or login : Click 's' to sign up or 'l' to login |
| Display prompt for creating an account | **Enter: s** | Enter your prefered username and password |
| Display prompt for login in | **Enter: l** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Use these short codes : sc - save an already existing account credential, cc - create a new credential, vc - view your credentials, fc -find a credential,copy - copy credentials, dl - delete an account, ex -logout |
| Display prompt for saving an already existing credential | **Enter: sc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: vc** | Prints a list of saved credentials |
| Delete ab account |**Enter: dl** | delete an account | 
| Copy credentials|**Enter: copy** | copy account credentials | 
| Exit application |**Enter: ex** | logout the current logged in account |



## Known bugs
No known bugs at the moment

## Technologies Used
+ Python 3.6


## Support and contact details
for any querries contact me via Martin5gathu@gmail.com.

## MIT License
Copyright(c)2020 **Karanja Martin Gathu**