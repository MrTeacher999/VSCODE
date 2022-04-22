# Today we will learn about how to use code in order to write on different files


# One time I was working of a software company. I had to create code that reads a file
# written in one coding language then be able to translate it into another
# by parsing/reading from the file of original code.
# then translating/writing on to a different file 


# soon we will use loops to parse files not lists.... 

# but lets start with learning how to read a file, line by line


# step number one decide wether you would like to read
# or if you would like to write on a file 

 

# so in the beginning you have to pick, are you reading this file or are you writing on to this file? 

''' the reason you need to pick if you are reading or writing is that 
you CANNOT do both with the same at the same 

'''
# what is an access mode 

# well there are a few access modes: 

"r" #represents only reading a file
'w' #represents only writing on to a file
'a' # represends append only 


# Difference between 'w' and 'a'
# w will erase everything on the original file then start writing from beginning
# w will overwrite basically
# however a will write only at the end of the file,
# so a will not delete anything

'''
myreadingobject = open("filename.extention","access mode")
'''
#so let's say you pick reading. 

'''
let's say I want to read from the file  "mybook.txt"
'''

myreadingobject = open("mybook.txt","r")

firstline = myreadingobject.readline() 
secondline = myreadingobject.readline()

fullthing = myreadingobject.read()
'''
when reading a file, we will focus on 2 different functions :


1. readline() this will read and return only a single line from the file, then set the reading 
pointer to the next line. Such that if we call readline() again, we start from the second line 


2. read()  this will read and return all of the contents in the file 


'''

'''

Let's try to write now 

'''

# to do this we create an object

# obj = open("file_name.extention","Access_mode")
myobject = open("newtxt.txt","a")
myobject.write("\nhello\tIt's me")
myobject.close()


"""
In order to write a line on to a different file we call

writingobject.write("whatever we want to write on the other file")

we may write the values of a list on to a different file by calling 

writingobject.writeline(list)

"""


#when using  # obj = open("file_name","Access_mode")
# it is important to know that, lets say inside our folder, if we have a text file called first.txt
# then to open this file for reading only, we would do: 


# obj = open("file_name.extention","Access_mode")

obj= open("first.txt","r")

 # to start reading the first line written in the txt file, i must write
firstline = obj.readline()
#print(firstline)
#print(obj)   #<-- this is an error doesnt print anything
secondline = obj.readline()
#print(secondline)


# what if i dont want to read line by line, and I want to read the whole thing at once

the_rest = obj.read()
#print(the_rest)

repeat = obj.read()
# after you finish reading or writing, make sure you close your file 
obj.close()


# print(the_while_thing)



# lets say I want to read line by line using a loop?
obj = open("file.txt","r")
#while(True):
#    line = obj.readline()
#    print(line)
#    if(line == ""):
#       print(" I am ending it")
#       break                          # <----- this stops a loop from running once it is read this is a new tool for you to use
#obj.close()




# break is used in while loops or any other loops to stop the loop from continuing to run
# this is an easy way to end a loop, without having to do somthing like 

#obj = open("first.txt","r")

condition = True

while(condition == True):
    line = obj.readline()
    print(line)
    if(line ==""):  # then we have reached the end of the file, end  the loop 
      condition = False      # end 
      print("I am ending it")
obj.close()
    


# \n  , not to be confused with /n  , \n is used to signify that we need a new line  
obj=open("newnew.txt","w")
obj.write("ICS4U")
obj.write(" Is the best class\n")
obj.write("In the world")
obj.close()


list_of_lines = ["hello\n","how are you?\n","I am doing alright,\nhow about you?"]

obj = open("first.txt","w")
obj.writelines(list_of_lines)
obj.close()

# \t , not to be confused with /t  , \t is used to signify that we need a tab, meaning 4 spaces 
obj = open("first.txt","a")
obj.write("\nhello?\tcan you see this?")
obj.close()








myobj = open("function.py","w")

list_of_function = ["def myfunction(param1,param2):\n","\tprint('Hello, this works')"]

myobj.writelines(list_of_function)