# using for loops find the smallest and largest number  in a 2d list
# *bonus*  switch thier positions when you are done 
# it would be smart to use a for loop with range for the bonus

new_data_structure = [[1,2,3,4],[1,5,7,3],[2,2,5,2,5,2,5,5,2,5,2],[1,4,5,6,7]]
largestnum = new_data_structure[0][0]
smallestnum = new_data_structure[0][0]


largestnumlistposition = 0
largestnumitemposition = 0
smallestnumlistposition = 0 
smallestnumitemposition = 0


list_position = 0
item_position = 0  # represents the index we are looking at
for listitem in new_data_structure:      
    for singleitem in listitem:
        if (largestnum < singleitem):
            largestnum = singleitem
            largestnumlistposition = list_position
            largestnumitemposition = item_position

        if (smallestnum > singleitem):
            smallestnum = singleitem
            smallestnumitemposition = item_position
            smallestnumlistposition = list_position

        item_position = item_position +1
    item_position = 0
    list_position = list_position+1

new_data_structure[smallestnumlistposition][smallestnumitemposition] = largestnum
new_data_structure[largestnumlistposition][largestnumitemposition] = smallestnum


print(new_data_structure)
# better version 

new_data_structure = [[1,2,3,4],[1,5,7,3],[2,2,5,2,5,2,5,5,2,5,2],[1,4,5,6,7]]

for listitem in range(len(new_data_structure)):      
    for singleitem in range(len(new_data_structure[listitem])):
        if (largestnum < new_data_structure[listitem][singleitem]):
            largestnum = singleitem
            largestnumlistposition = listitem
            largestnumitemposition = singleitem

        if (smallestnum > new_data_structure[listitem][singleitem]):
            smallestnum = singleitem
            smallestnumitemposition = listitem
            smallestnumlistposition = singleitem


new_data_structure[smallestnumlistposition][smallestnumitemposition] = largestnum
new_data_structure[largestnumlistposition][largestnumitemposition] = smallestnum


print(new_data_structure)





# write a function that takes in a td list
# using for loops
# print a full 2d list in reverse


new_data_structure = [[1,2,3,4],[1,5,7,3],[2,2,5,2,5,2,5,5,2,5,2],[1,4,5,6,7]]



# for Item in range :
# (the value you begin at, the value you will end before (if 0 then we end before 0), value of increase/decrease per loop)



# the index of the last item in a list   is  len(list)-1 

for i in range (len(new_data_structure)-1,-1,-1):
    for x in range (len(new_data_structure[i])-1,-1,-1):
        print(new_data_structure[i][x])





# create a 2d list of 3 lists with 4 items. 

mynewlist = [[5]*4]*3


print(mynewlist)
# write for loops that change every value in the 2dlist to 0 

for index in range (len(mynewlist)):
    for second_index in range (len(mynewlist[index])):
        mynewlist[index][second_index] = 0 



print(mynewlist)

newlist = [[0 for a in range(4)]]*3
mynewlist = [[0]*4]*3

print(newlist)