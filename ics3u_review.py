# variables in programming are values that you can save to your computer that can be used/modified whenever
# there are different types of variables in programming 

mystring = "hello!"  # a string variable is a variable that represents symbols in quotation marks
myint = 7 # an integer variable is a variable that represents a whole number!
myfloat = 3.14 # a float variable is a variable that represents a number with decimals!!
myboolean = True # a boolean variable is a variable that can represent one of only 2 states
                 # a boolean can either be true or false only 
character_variable = 'a' # a char variable is a string variable but with only 1 symbol, 
                         # only one thing in between the quotation marks

list = [1,3,5,56,"hello",True, 3.14, 'a'] # a list is a variable that holds multiple values, accessed using an index

array = [1,2,3,4,5]

array2 = ["a","b"]


# the third item in this list is accessed by writing 
print(list[2])


#  An if statement is a block of code that is only excecuted if a certain condition is true


if (3<=4):
    print("3 is less than 4")

# conditions that we can set are anything that can be proven true or false

if (3 == 5):
    print("3 is equal to 5")


is_it_raining = True

# and   &&
# or    |
if (is_it_raining == True and 3>4 ):
    print("It is raining!")

# loops


# a loop is kind of similar to an if statement. In an if statement, we have a block of code that will only run if 
# a certain condition is true

# a loop is a block of code that will continue to repeat itself as long as the loop condition is true 


count = 0 

while (count <10 ):    # be careful of falling into infinite loops 
    print("hello", count)
    count = count+1


condition = False

while (condition == False):
    print("type stop to stop")
    var =input()
    if(var == "stop"):
        condition = True


#functions

# a function is a block of code that is meant to be reused in different cases. 
# Functions accept parameters wich allow them to work with different values 

def f(x,y,z):
    return x**2 + y - z


print(f(5,4,3))

# functions can also not have any parameters 


def myprint_hello():
    print("heelloooooooooooooooo")


myprint_hello()



# create a function that use a loop to print the first 10 numbers in the 12 times table 

count = 0 
while(count <= 10):
    print("hello,   12 *",count, "=",count*12)
    count = count +1 


# New loop !!!!!

# parse a list and return the largest number 


mylist = [1,2,3,4,5,6]     
count = 0
largestnumber = mylist[0]
while (count <len(mylist)):     # len(anylist) = the number of items in that list

    if(largestnumber<mylist[count]):
        largestnumber = mylist[count]
    count += 1

print("largest number is :", largestnumber)
     

# We want to do this in an easier way... is there an easier way?  YES 

# INTRODUCING FOR LOOPS

secondlist = [2,4,6,8,10]
largestnumber = list[0]

for item in secondlist:
    if (item > largestnumber):
        largestnumber = item

print("the largest num is :")


