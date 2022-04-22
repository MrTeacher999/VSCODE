'''
What is an object?

An object is simply a collection of data (variables) and methods (functions) that act on those data. 
Similarly, a class is a blueprint for that object. We can think of a class as a blueprint (prototype)
of a house. and an object as the house itself


'''

# an object is a datatype 


'''
An object is not a variable but it is a data type

An object is a data type such that it may contain many variables associated with it
It can have it's own functions associated with it

kind of like how we have 

list.append(i)  <--- this is a function associated with list

len(list)  <-- same thing

list.insert(1,3) <--- same thing

All variables and functions associated with an object are introduced and defined
in the class definition of the object


'''


# let's say I want to create an object/datatype  student :
'''
This student should have the following attributes :

grade, age, mark , email

Also, we want to be able to change the students mark using a function


'''




class Student : 

    def __init__(self,name,grade,mark,email):
        self.name = name 
        self.grade = grade
        self.mark = mark
        self.email = email

    def change_mark(self,newmark):
        self.mark = newmark

newstudent = Student("Zahy",12,100,"mrcoolguybossman@hotmail.com")


print(newstudent.name)
print(newstudent.email)

newstudent.mark = 101

print(newstudent.mark, "before")
newstudent.change_mark(1000)
print(newstudent.mark, "after")


anylist = []

anylist.append(2)




# how to read and write on to other files 


