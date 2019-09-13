# -*- coding: utf-8 -*-

myfile = open ('C:\\Users\\k.shabunin\\PycharmProjects\\FirstProject\\file examples\\example_1.txt','w+') # Open file, if file does not exist then file will be created
myfile.write("Dismay'd not this\nOur captains, Macbeth and Banquo?")
myfile.close()

myfile = open ('example_1.txt','r')
print(myfile.read())
myfile.close()

myfile = open('example_1.txt','r')
my_list = myfile.readlines()
print(my_list)

#For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
#myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")

#For MacOS and Linux you use slashes in the opposite direction:
#myfile = open("/Users/YouUserName/Folder/myfile.txt")