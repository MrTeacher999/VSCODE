def login_verify(user,passw):
    parser = open("database.txt","r")
    line = parser.readline()
    while (line != ""):
        if line == user+"\n":
            password = parser.readline()
            if password == passw+"\n":
                return True
        line = parser.readline()

    return False
