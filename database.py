import os
# acc num acting as user_id(primary key)
# ------>
# create user file
# read user info
# update user info
# delete user info

# userdetailtest = ['test', 'test2', 'test@hh22a.com', 'Pasowrd', 11220]
# userdetails = ' '.join(str(x) for x in userdetailtest)

def create(account_number, userdetails):
    userdetail_final = ' | '.join(str(x) for x in userdetails)
    

    file = open('data/' + str(account_number) + '.txt', 'x')
    file.write(userdetail_final);
    file.close();


def read(account_number):
    my_file = open('data/' + str(account_number) + '.txt', 'r')
    return my_file.readline()
    

def update(account_number, userdetails):
    return 'Try again'

def delete(account_number):
    try:
        os.remove('data/' + str(account_number) + '.txt')
    except FileNotFoundError:
        print('You don\'t have an Account with us')


# create(131, userdetails1)
# print(read(1662724734))
# delete('131q')