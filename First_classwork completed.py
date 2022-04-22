# use a for loop to parse a list in reverse
list = [1,2,3]
#for item in list:
#    print(item)

for number in range(len(list)-1,-1,-1):
    print(list[number])

# use a for loop to only print the first odd numbers from 0 to 101 ( INCLUDING 101)

for i in range(1,102,2):
    print(i)

# use a for loop to print the first 15 numbers in the 16 times table 

for number in range(16):
    print(16*number)


# use a for loop to parse a string, if the letter a is found during a loop print ("there is an a here!")

mystringvariable = "this is my string"   

for character in mystringvariable:
    if character == "a":
        print("I have found the a")
        
    

# write a funciton that takes in a string parameter
# then using a for loop, return the amount of characters in that string 

def charactercounter(anystring):
    #1
    count = 0
    for character in anystring:
        count +=1
    print(count)
    #2
    for number in range(1,len(anystring)+1):
        print(number)
    

charactercounter("this is a string")

