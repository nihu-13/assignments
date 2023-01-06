# 1. Write a python script to display the number of days in a given month number.
# month=int(input("Enter The Month number\n"))
# match month:
#     case month if month in(1,3,5,7,8,10,12):
#          print("31 Days")
#     case month if month in(4,6,9,11):
#          print("30 Days")
#     case month if month in(2):
#          print("28/29 Days")
#     case _:
#         print("Enter month number between 1-12")
# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, c
# a=int(input("Enter Two Number : "))
# b=int(input())
# print("***** Menu *****\nEnter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n")
# menu=int(input("Enter Number Between 1-4 : "))
# match menu:
#     case 1:
#         print("Ans = ",a+b)
#     case 2:
#         print("Ans = ",a-b)
#     case 3:
#         print("Ans = ",a*b)
#     case 4:
#         print("Ans = ",a/b)
#     case _:
#         print("Please Enter Number Between 1-4 !")
# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.
# a=int(input("Enter Three Number : "))
# b=int(input())
# c=int(input())
# print("***** Menu *****\nEnter 1 for Check whether a given set of three numbers are lengths of an isosceles triangle or not\nEnter 2 for Check whether a given set of three numbers are lengths of sides of a right angled triangle or not\nEnter 3 forCheck whether a given set of three numbers are equilateral triangle or not\nEnter 4 for Exit.\n")
# menu=int(input("Enter Number Between 1-4 : "))
# match menu:
#     case 1:
#         if a==b or b==c or c==a:
#             print("A given set of three numbers are lengths of an isosceles triangle")
#         else:
#             print("A given set of three numbers are lengths is not of an isosceles triangle")
#     case 2:
#         if a==90 or b==90 or c==90:
#             print("A given set of three numbers are lengths of sides of a right angled triangle ")
#         else:
#             print("a given set of three numbers are lengths of sides is not of a right angled triangle ")
#     case 3:
#         if a==b==c :
#             print("A given set of three numbers are equilateral triangle")
#         else:
#             print("A given set of three numbers are not a equilateral triangle")
#     case 4:
#         print("Exit")
#     case _:
        # print("Please Enter Number Between 1-4 !")
# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.
# age=int(input("Enter Age : "))
# print("The category of person : " ,end=" ")
# if 0<age<=10:
#     print("Kid")
# elif age==0:
#     print("Enter valid age ")
# elif 10<age<=20:
#     print("Teen")
# elif 20<age<=40:
#     print("Young")
# elif 40<age<=60:
#     print("Senior Citizen")
# else:
#     print("Experienced")
# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.
# num=int(input("Enter a Number : "))
# match num:
#     case num if num<0 and (num % 2) != 0:
#         print("Prateek Jain ")
#     case num if num % 2 == 0:
#         print("Saurabh Shukla")
#     case num if num>0 and (num % 2) != 0:
#         print("Aditya Choudhary ")
         
# 6. Write a python program to check whether a given string is a multiword string or single
# word string using match case statement
# string=str(input("Enter a string : "))
# string.strip()
# match string:
#     case string if ' ' in string:
#         print("multiword string")
#     case string if ' ' not in string:
#         print("single word")
    
# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement
# num=int(input("Enter a Number : "))
# match num:
#     case num if num>0:
#         print("positive ")
#     case num if num<0:
#         print("negative")
#     case num if num == 0:
#         print("zero")
# 8. Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement
# s1=str(input("Enter a first string : "))
# s2=str(input("Enter a second string : "))
# match (s1,s2):
#     case (s1,s2) if s1==s2:
#         print("strings are identical")
#     case (s1,s2) if s1>s2:
#         print("{} comes before the {}".format(s1,s2))
#     case (s1,s2) if s1<s2:
#         print("{} comes before the {}".format(s2,s1))
# 9. Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year

# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday
s=str(input("What is your favourite color : "))
l1=["yellow","blue","orange","white","black","red"]
for color in l1:
    if color in s:
        c=color
        break
else:
    c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")