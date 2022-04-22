import signup   # we call these green highlighted filenames as modules   
import login_file
import dashboard
'''
import filename

from filename import variable_name/function_name
'''

# we call multi file programming, "modular programming"


print("welcome user, do you have an account with us?")
resp = input()

if resp == "yes":
    print("ok please give me the username")
    user = input()
    print("great! what is the password?")
    password = input()
    if login_file.login_verify(user,password) == True:
        print("great! You have now signed in")
        dashboard.nice()
    else:
        print('sorry I do not recognize you, you imposter!')
        print("dont come here again")



    
if resp == "no":
    print("would you like to make an account?")
    resp = input()
    if resp == 'yes':

        print("ok please give me a username")
        user = input()
        print("great! what is ur password?")
        password = input()
        print("great! what is ur email?")
        email = input()
        signup.signup_function(user,password,email)

    if resp == "no":
        print("ok loser, this app was too good for you anyway")    
    

