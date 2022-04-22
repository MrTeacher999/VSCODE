

# we want to write a parsing algorithm wich is meant to access every item in the list on it's own 

#lst =[1,2,3,4,5]


#for a in lst:   # this parses a list and prints every item in it
#    print(a)







#for item in new_data_structure:    # this algorithm prints the items in the 2d list where every item is a list
#    print(item)



#  ?? how do i access/print/edit single values in a 2dlist


new_data_structure = [[1,2,3,4],[1,5,7,3],[2,2,5,2,5,2,5,5,2,5,2],[1,4,5,6,7,]]

for item in new_data_structure:      # nested loop = A loop inside a loop 
    print(item)
    for singleitem in item:
        print(singleitem)
    print('hi')
    
# find the largest number in this 2d list

new_data_structure = [[1,2,3,4],[1,5,7,3],[2,2,5,2,5,2,5,5,2,5,2],[1,4,5,6,7]]



largestnum = new_data_structure[0][0]

for item in new_data_structure:      
    for singleitem in item:
        if (largestnum < singleitem):
            largestnum = singleitem

print("The largest number in this list is:",largestnum)


# using for loops find the smallest and largest number  
# *bonus*  switch thier positions when you are done 
# it would be smart to use a for loop with range for the bonus



for listposition in range(len(new_data_structure)):    # this more tedious but much more helpful when you want to save certain positions/indexes

    print(new_data_structure[listposition])

    for single_item_position in range(len(new_data_structure[listposition])):


        print(new_data_structure[listposition][single_item_position])










