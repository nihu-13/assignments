# 1. Write a python script to add comments and print “Learning Python” on screen.
print("Learning Python")   # print “Learning Python”
# 2. Write a python script to add multi line comments and print values of four variables,
# each in a new line. Variable contains any values.
num1=9
num2=7
num3=5
num4=2.3
print(num1,num2,num3,num4,sep="\n") 
''' print value of num1 ,num2,num3,num4 
    9
    7
    5
    2.3  '''
# 3. Write a python script to print types of variables. Create 5 variables each of them
# containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
num1=2
num2=2.3
num3=True
num4=3+4j
num5="nihu"
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))
# 4. Write a python script to print the id of two variables containing the same integer
# values.
num1=5
num2=5
print(id(num1))
print(id(num2))
# 5. Create four variables in a Python script and assign values of different data types to
# them. Write a Python script to print value, its type and id of each variable
num1=2
num2=2.3
num3=True
num4=3+4j
num5="nihu"
print(num1,type(num1),id(num1),sep=" ")
print(num2,type(num2),id(num2),sep=" ")
print(num3,type(num3),id(num3),sep=" ")
print(num4,type(num4),id(num4),sep=" ")
print(num5,type(num5),id(num5),sep=" ")
# 6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)
# 7. On Python shell use help() function and display the list of keywords
help(keyword)
# 8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
# value to it. Write a python script to import A1 module in A0 and print value of the
# variable created in A0.py
from A1 import x
print(x)
# 9. Name the keywords, used as data in the Python script.
‘if’ and ‘else’ ‘for’ and ‘in’ ‘def’ ‘import’ and ‘as’
# 10. Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and
# 9:00 PM)
from datetime import datetime
date=datetime.now()
print(date.strftime("%d-%m-%Y")," and ",date.strftime("%I:%M %p"))