
# there are multiple ways to store information in programming

# the ways in wich we store this information are what we call data structures

# for example, when we want to store information in a variable of items seperated by commas
#  we may use the list data structure


#so far, the only data structure we have been really focused is lists/2dlists


# there are upwards of 10 different very popular data structures, 4 of wich we will not even talk about 

# but listed below are the most popular data structures
# list  

# we know this.

# Tuple 

# A tuple is just like a list because it is ordered with index and allows duplicate values.
# HOWEVER a tuple is immatuble meaning unchangable. 

# we declare a tuple as such :

mytuple = (1,2,3,4,5,6)  # <-- round bracket

# because a tuple is unchangeable we cannot do : 

#mytuple.append(2)

#mytuple[1] = 3

# we cannot assign new values to a tuple, we cannot append to a tuple 

tuple1 = (1,2,3)
tuple2 = (5,6,7)

tuple3 = tuple1+tuple2

# you can only create a new tuple by added 2 tuples together
print(tuple3[0])

# however, we can access any item in a tuple the same way we access items in a list

#tuple3[1] = 3

# tuple is meant to not be changed/tampered with.. working with tuples does not give us a lot of room to play
# that is by design.. tuples are more secure this way 



# In conclusion : A tuple is an ordered sequence that allows duplicate values however tuples are unchangable/immutable'
# you can only combine mutliple tuples together by adding them to each other 

tuple3 = tuple1+tuple2

# set

#Set items are:
# 1. unordered, 
# 2. unchangeable, 
# 3. does not allow duplicate values.

# pro's of using a set is :
# accessing an item in a set is much more effecient speed and memory wise than accessing an item in a list 

# con's 

# it is literally unordered, you cand specifically acess an item at a certain location
# meaning sets have no indexes 

myset = {1,2,3,3,4,5,6}
myset = set(myset)

if 6 in myset:
    print("6 is in the set")


# we use sets as a very effecient way to store data that is not meant to be repeated 

# the value in storing it in a set is that checking if an item is in a set is much faster than checking if an item is in a list

# you can imagine if you have 10 million datapoints that dont repeat and you always just want to check if a certain value is in the set
# then we would use sets 



#Once a set is created, you cannot change its items, but you can remove items and add new items.


# we initialize a set by using curly brackets

# dictionary/map/hashmap

# I would argue that dictionaries are as useful as lists.


#Dictionaries are used to store data values in key:value pairs.

mydict = {
    "Height":180,
    "Weight":165,
    "age":300
}

mydict = {
    1:180,
    2:165,
    3:300
}

# NOTE in some languages, keys are only alloud to be strings, not python 


#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# the point of a dictionary is, is that items are not ordered by index from 0-len(list)-1

# it is actually ordered by it's keys

#meaning to access any value in a dictionary, in the index section of the dictionary we will write our key value


# so we no longer acess items in a dictionary by index, we access by key

mydict1 = {
    "Height":180,
    "Weight":165,
    "age":300
}

mydict2 = {

    1:[180,18],
    3:300
}

print(mydict1["Weight"])

print(mydict2[1])


# there are no duplicates, this is because every key must be unique. We cannot have 2 of the same key.
# Hoewever, we can have 2 same values



# stack  (form of list)

# a stack is actually just a list but with 2 rules.

# 1. whenever we want to add to the stack, we add to the end (meaning we are only alloud to append in a stack)
# 2. when we want to remove an item, we only remove from the end  (meaning we are only alloud to do pop() when removing

# why? 

#the whole point of a stack is that it is a special list data structure where :

# the item that has most recently been added will be the first to be removed

# we call this structure  LIFO  last in, first out 


# queue  (form of list)

# A queue follows similar philosophy, only we call it FIFO  first in, first out


# The best way to describe a Qeueue is that a queue is modelled after a line to any store

# the person in the front of the line is the first to finish and go (be removed from the queue)
# the person last in line needs to wait until everyone in front of them has left

# The whole point about queues is that, similarly to stacks, they follow 2 specific rules


# 1. you are only alloud to add at the end (same as rule #1 for stack)  meaning only alloud to append
# 2. you are only alloud to remove the current first item from the list. Meaning you are only alloud to use  pop(0<----)


# why is this relevant? # why do we use queues ?   

# this perfecty models people in line  <---- 

# programmers use queues to code people waiting on a phone line 

# automated messages when you call the bank they say :

# estimated wait time 40 mins, there are 25 people ahead of you 





# these are datastructures that are created by creating it's object


# linked list
# trees  *
# heaps  *
# graphs **  <-- hardest


