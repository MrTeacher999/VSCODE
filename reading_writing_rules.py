''''
Here are certain rules you must follow / common mistakes students make 


1.  when we call  obj = open("filename.extention","r")

we MUST make sure : 

                  > we include the files extention (meaning include the .py or .txt or .png, or .pdf)
                  > Make sure the file you are accessing is in the same folder as your code file 
                  > dont forget to include an access mode  'r' for read  and  'a' or 'w' for writing

2.  'w'  will result in overwriting everything in the file that was there before we openend it 
    'a'  will result in writing at the end of the file so as not to overwrite anything


3. Calling readline 3 times will not cause you to read the same line 3 times, you will read the first 3 lines


this is because when we call readline(), the function moves the ponter one line down 
so that next time we call readline() it is reading the next line 



4. Once you are done reading or writing a file, you MUST RUN THE COMMAND 

myobj = open("filename.txt","r")

line= myobj.read() 

Let's say we are done reading, now me MUST RUN 

myobj.close()

# This closes the file that your program has been reading / or writing from 

# it is necissary you make this call or else you will not be able to open another file to r or write




5. FOR WRITING


 if you run  :   myobject = open('filename.txt','w')

 and lets say filename.txt is nowhere to be found in the folder

 then your code will actually create a new file then write on to it.

 This means if you like, you can always create your own file to write on to 

 if you want to add a line break as you are writing , meaining you want to indicate to the computer
 that you want to write the next words on a new line, we use  \n  <--- this means newline


For example , 
'''

myobj = open('filename.txt','w')

myobj.write("hey!\nwelcome to ics!\nI am excited to meet you!!")

myobj.close()

myobj = open('differentfile.txt','r')

myobj.close()