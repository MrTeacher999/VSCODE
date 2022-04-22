#.Write a function that takes in a 2d list as a parameter then :
# take every element in that list and multiply it by the value of the item in the list before it. 
# If we are at the first value in the list, then print that value to the power of 3

twoDlist = [[12,3,4],[4,5,2,5,2],[54,3,5,2,5,2,5]]

def myfunction(any2dlist):

    for index in range (len(any2dlist)):   # len(list) = the number of items in the list , # len(2DLIST) = the number of lists in the 2d list

        for secondindex in range(len(any2dlist[index])): # len(2dlist[index])  returns the number of items in the list at given index

            if secondindex == 0 :  # if   2dlist[index][0], then we have the first item in a list 

                print(any2dlist[index][secondindex]**3)
            else:
                 # any2dlist[2][3]  =  any2dlist[2][3] * any2dlist[2][2]
                any2dlist[index][secondindex] =  any2dlist[index][secondindex]*any2dlist[index][secondindex-1]
        


myfunction(twoDlist)

myfunction([[1,2,3,4],[5,4,5,2,],[1,4,5,6,2]])
           


#HINT 2**3  is 2^3 in python ,   ** is the exponent operator
# 
# 
# 
# When you are done ask the user if they
#would like to repeat the process and add new numbers, if yes repeat, if no, print (‘have
#


# write a for loop(s)
# 
#  that will print 3 things every loop 
# 
# 1.every item in the list in order from first to last every loop is the next item 
# 2.it's sum with the next item in the list 
# 3.(item - previous item) in the list 




# write a function that goes through a 2D list and returns the number of 
# even numbers in the list



# write a for loop that prints every item of a tuple! test it with a tuple you have created

# ---------------------------------------------------------------------------------------------------------------------------
# creating an object

[1,2,3,4]

class linked_list():

    def __init__(self,value,next = None):
        self.next = next
        self.value = value


    def append(self,value):
        curr = self
        while (curr.next != None):
            print(self.value)
            curr = curr.next
        curr.next = value
        print('after,',self)
        return self
        

item1 = linked_list("first")
item2 = linked_list("second")
item3 = linked_list("third")

item1.next = item2
item2.next = item3

item1.append("hey")

print(item1)


