# we know a data structure in programming is a type of variable that hold multiple points of data
# each data structure is different and has it's on rules




# so, we have learned the rules of lists

# a list is a bunch of items indexed from 0 to (number of items)-1

# for example 

list1 = [4,6,8,10]

list1[0] = 4


two_dimentional_list = [[2,2,3,4],[5,2,6,7] ,[6,2,5,2] ,[1,3,5,7]]

# how do i access the third item in the second list ????


print(two_dimentional_list[1][2])


# first item in last list

print(two_dimentional_list[3][0])


# last item in first list

print(two_dimentional_list[0][3])


# last semester we learned a bunch of built in python list function
# I told you during final exam review that , the most important ones we focus on are :

# .append(number)  this function adds the value "number" to the end of the list

# 
#   , list.pop(index)    this function deletes the item in the list that has the index "index"
# 
# 
# 
#    ,len(list)     # this function returns the number of items in a list 
#
#
#
#     list.insert(index,item) # this function will add the value "item" to the index "index" of the list
#
 
# ok but we learned this for 1d lists.... how tf am I supposed to do it with 2D ???



# append 2 to the first list

two_dimentional_list[0].append(2)


# append 4 to the fourth list

two_dimentional_list[3].append(4)

# pop the second item from the first list

two_dimentional_list[0].pop(1)

# return the length of the entire 2d list

print(len(two_dimentional_list))

# return the length of the third list

print(len(two_dimentional_list[2]))

# insert 5 to the fourth position of the second list


two_dimentional_list[1].insert(3,5)

#  insert 1 to the third position in the third list


two_dimentional_list[2].insert(2,1)




