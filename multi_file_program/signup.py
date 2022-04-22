def signup_function(username,password,email):
    newfile = open("database.txt","a")
    newfile.write("New user\n")
    newfile.write(username+"\n")
    newfile.write(password+"\n")
    newfile.write(email+"\n")




