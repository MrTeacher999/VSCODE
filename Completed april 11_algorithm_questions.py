# create a 2d list of 4 lists with 5 items each 

mylist = [[1,2,3,4,5],[6,7,8,9,10],[2,4,6,8,10], [9,8,7,6,5]]

print(mylist)

# write for loop(s) that wil print every even number in the list in order

#     even number % 2 = 0  
#  

for a in mylist:
    for b in a :
        if (b %2 == 0):
            print(b)





# write for loop(s) that will print every odd number in the list in reverse 

for index in range (len(mylist)-1,-1,-1):
    for second_index in range (len(mylist[index])-1,-1,-1):
        if (mylist[index][second_index] % 2 != 0):
            print(mylist[index][second_index])



# write a for loop(s)
# 
#  that will print 3 things every loop 
# 
# 1.every item in the list in order from first to last every loop is the next item 
# 2.it's sum with the next item in the list 
# 3.(item - previous item) in the list 


#  The error you will encounter is an index out of range error. 
# this can be fxed by writing an if statement that only does the operation 1 if we are past the first item 
# and only does the operation #2 if we are not at the last item in the list