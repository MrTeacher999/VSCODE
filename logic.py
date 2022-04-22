new_data_structure = [[1,2,3,4],[1,5,7,3],[2,2,5,2,5,2,5,5,2,5,2],[1,4,5,6,7]]



largestnum = new_data_structure[0][0]  # = 1 then 2 then 3 then 4 then 5 then 7 

for item in new_data_structure:      
    for singleitem in item:
        if (largestnum < singleitem):
            largestnum = singleitem