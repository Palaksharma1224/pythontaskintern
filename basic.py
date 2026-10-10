# f=open("C:\\Users\\khush\\OneDrive\\Desktop\\palak intern\\file handling\\demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# read and text mode

# f=open("C:\\Users\\khush\\OneDrive\\Desktop\\palak intern\\file handling\\demo.txt","rt")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# to read particular word from the file 
# f=open("C:\\Users\\khush\\OneDrive\\Desktop\\palak intern\\file handling\\demo.txt","r")
# data=f.read(5)
# print(data)
# print(type(data))
# f.close()

#reads a file one line at a time 

# f=open("c:\\users\\khush\\onedrive\\desktop\\palak intern\\file handling\\demo.txt","r")
# line1=f.readline()
# print(line1)
# f.close()

#writing to a file 
# f=open("c:\\users\\khush\\onedrive\\desktop\\palak intern\\file handling\\demo.txt","w")
# f.write("i want to learn javascript")
# f.close()

#appending to a file
# f=open("c:\\users\\khush\\onedrive\\desktop\\palak intern\\file handling\\demo.txt","a")
# f.write("i also want to study about web technology")
# f.close()

#to create new file using writing mode
# f=open("sample.txt","w")
# f.write("hi i am student of computer science.")
# f.close()

#also using append method
# f=open("sample.txt","a")
# f.write("i will also pursue my studies after my bachelors")
# f.close()

#using "+" method r+ means reading and writing method mode 

# f=open("sample.txt","r+")
# f.write("\n after this i am thinking to done my masters in computer science.")
# print(f.read())
# f.close()

#using w+ method 
# f=open("sample.txt","w+")
# f.write("\n after this i am thinking to done my masters in computer science.")
# print(f.read())
# f.close()

# using a+ method

# f=open("sample.txt","a+")
# f.write("\n my classes are started from 20th july .")
# print(f.read())
# f.close()

 #with method
# with open("sample.txt","r") as f:
#     print(f.read())
#     f.close()


# del method using import os 
import os
os.remove("sample.txt")