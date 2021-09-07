# #Register
# userName, email, password

# #Login
# AccountNumber & password.

# #Bank Operations
# Operations such as Withdraw, Deposit, Complain etc
import database
import random  # import random module
from getpass import getpass

# database = {
#     8639605981: ['test', 'test', 'test@test.com', 'password', 2000]
# }  # create a dictionary called database 
def init():  # initializion function

    actions = input('Do you have an account ? 1. Yes 2. No 3. Exit ')
    if actions.isdigit():
        actions = int(actions)
        if actions == 1:
            Login()
        elif actions == 2:
            registerAccount()
            
        elif actions == 3:
            exit()
        else:
            print('Sorry try again!')
    else: 
        print('Please enter a number')


def registerAccount():
    print('******** REGISTRATION PORTAL *********** \n')
    email = input('email: ')
    first_name = input('FirstName: ')
    last_name = input('LastName: ')
    password = getpass('Password: ')
    accountnumber = generateAcctNumber()
    
    detailed = [ first_name ,last_name ,email, password, 0] 
    database.create(accountnumber, detailed) # create account from database.py
    
    print('Your account has been successfully created and here is your account number:', accountnumber)
    Login(detailed, accountnumber)
    return detailed


def Login(detailed, accountnumber):
    print('******* Login Portal ********')
    typedAccountNumber = input('Enter your Account number to Login: ')
    if typedAccountNumber.isdigit():
        typedAccountNumber = int(typedAccountNumber)
        typedPwd = getpass('Enter your password here: ')

        if typedAccountNumber == accountnumber:    
            if detaile[3] == typedPwd:
                print('Successfully Logged-In')
                bankOperations(detaile)
        else:
                print('*** Login Portal closed due to wrong Username/Pass, Kindly logging again: *** ')
    else: 
        print('Please enter your account number again')
        Login(detaile, accountnumber)
    # bankOperations(userDetails)


def bankOperations(user):
    print('Welcome %s %s' %( user[0] , user[1]))

    operationOption = input('Choose an option 1) Withdraw 2) Deposit 3)Complain 4)logout \n')
    if operationOption.isdigit():
        operationOption = int(operationOption)

        if operationOption == 1:
            Withdraw(user)

        elif operationOption == 2:
            Deposit(user)
    
        elif operationOption == 3:
            Complain(user)
    
        elif operationOption == 4:
            Login()

        else:
            print('Please enter a valid option')
    else:
        print('Please enter a number')
    


def Withdraw(detailed):
   
    wid_amt = input('Enter the amount you: ')
    if wid_amt.isdigit():
        wid_amt = int(wid_amt)
        for k in detailed: 
            if wid_amt <= detailed[4]:
                balance_wid = detailed[4] - wid_amt
                print('Please take your $%d cash and your have $%d left' % ( wid_amt , balance_wid )) 
                exit_option()
            else:
                print('Ooops, the cash exceeds the amount you have left')
                
        
    else:
        print('Please enter a number')
    
def Deposit():
    w_dep = input('Enter the amount you: ')
    if w_dep.isdigit():
        w_dep = int(w_dep)
        
        for z, p in database.items():
            new_balace_after_dep = p[4] + w_dep 
            
        print('Your new balance is', new_balace_after_dep)    
         #   depo_amt = y[4] + w_dep
          #  print('You have paid $%d cash. You now have $%d in your account' % ( w_dep, depo_amt ))   
    else:
        print('Please enter a number')

def Complain():
    print('Complaint submitted')

def generateAcctNumber():
    return random.randrange(1111111111,9999999999)

def exit_option():
    exit_opt = input('Would you like to login again or exit? 1.(Login) 2.(Exit) ')
    if exit_opt.isdigit():
        exit_opt = int(exit_opt)
        if exit_opt == 1:
            Login()
        else:
            exit()

init()