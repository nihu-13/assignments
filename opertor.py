# 1. Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)
number=int(input("Enter Number : "))
num=int(number/10)
print(num)
# 2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)
number=int(input("Enter Number : "))
num=int(number%10)
print(num)
# 3. Write a python script to swap data of two variables
a,b=5,6
a,b=b,a
print(a,b)
# 4. Write a python script to find x power y, where values of x and y are given by user
x=int(input("Enter number : "))
y=int(input("Enter power of number : "))
print(x**y)
# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.
number=int(input("Enter Three Digit Number : "))
num=int(number/100)
print(num)
# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.
number=int(input("Enter Three Digit Number : "))
num=int(number/10)
print(num%10)
# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.
number=int(input("Enter Three Digit Number : "))
num=int(number%10)
print(num)
# 8. Write a python script to use IN operator to display the data present in the list
list1=[45,67,53,3535,35]
print(45 in list1)
# 9. Write a python script to use NOT IN operator to display the data not present in list
list1=[45,67,53,3535,35]
print(47 not in list1)
# 10. Write a python script to use IS operator to display if both variables are the same
# object or not?
a,b=5,8
print(a is b)
