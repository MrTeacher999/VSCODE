# create a 2d list  consisting of 5 lists with 4 items in each list

mytwod = [[1,1000,3,4],[5,6,7,8],[9,1,1,1],[1,2,3,4],[5,4,3,2]]

print(mytwod)
# print the fourth item in the third list
print(mytwod[2][3])
#print the second item in the fifth list
print(mytwod[4][1])
# insert 4 to the second position of the fifth list
mytwod[4].insert(1,4)
# insert 5 to the third position of the 3rd list
mytwod[2].insert(2,5)
# append 3 to the first list
mytwod[0].append(3)
# pop the second element from the second list
mytwod[1].pop(1)
# pop the fourth element from the fourth list
mytwod[3].pop(3)
# return the length of the entire 2dlist
len(mytwod)
#return the length of the first list

len(mytwod[0])

