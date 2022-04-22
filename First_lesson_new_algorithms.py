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
largestnumber = secondlist[0]

for item in secondlist:     # this will literally loop through every item in the list one by one
    if (item > largestnumber):    # until it reaches the end 
        largestnumber = item

print("the largest num is :",largestnumber)


# so in the first loop,  item = 2
# second loop, item = 4
# third loop, item = 6


# the statement 
list = [1,3,5,7]

#for i in list:    # we can use a foor loop to parse a list one by one very easily 
#    print(i)


#for b in range(len(list)):   # using a for loop with range to parse a list one by one 
#    print(b, list[b])


string = "I am the best in the world"

#for character in string :    # can also use for loops to parse a string character by character 
#    print(character)


# a really powerful part of for loops is  the range addition.. why ?


for a in range(-5,10,2):
    print(a)


for number in range(1000,-1,-50):
    print(number)


for even in range(0,1001,2):
    print(even)


list = [1,4,5,7,6,8,9,5,56]

for item in list:
    print(item)
    