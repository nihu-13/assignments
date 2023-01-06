# 1. Write a recursive python function to calculate sum of first N natural numbers
# def sum_num(n):
#     if n==1:
#         return 1
    
#     return n+sum_num(n-1)
       

# print(sum_num(5))
# 2. Write a recursive python function to calculate sum of first N odd natural numbers
# def SumOdd(num1,num2):
#     if num1>num2:
#         return 0

#     return num1+SumOdd(num1+2,num2)
# num1=1
# print("Enter your Limit:")
# num2=int(input())
# print("Sum of all odd numbers in the given range is:",SumOdd(num1,num2))

# 3. Write a recursive python function to calculate sum of first N even natural numbers
# def sum_of_even(n):
#     return 0 if n<2 else sum_of_even(n-1) if n%2 else n + sum_of_even(n-2)
# print(sum_of_even(4))
# 4. Write a recursive python function to calculate sum of squares of first N natural
# numbers
# def squares(n):
#     if n==0:
#         return 0
#     return (n**2)+squares(n-1)
   
# print(squares(3))
# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers
# def cube(n):
#     if n==0:
#         return 0
#     return (n**3)+cube(n-1)
   
# print(cube(2))
# 6. Write a recursive python function to calculate the factorial of a number.
# def fac(n):
#     if n==0:
#         return 0
#     return n+fac(n-1)
   
# print(fac(3))
# 7. Write a recursive python function to calculate sum of the digits of a given number
# l=[]
# def sum_digit(n):
#     if n==0:
#         return 0
#     dis=n%10
#     l.append(dis)
#     sum_digit(n/10)

# sum_digit(int(input("Enter number : ")))
# print(int(sum(l)))
# 8. Write a recursive python function to print binary of a given decimal number.
# def binary(n):
#     if n>1:
#         binary(n//2)
#     print(n%2,end="")

# binary(int(input("Enter a decimal number")))
# 9. Write a recursive python function to print octal of a given decimal number
# def octal(n):
#     if n>1:
#         octal(n//8)
#     print(n%8,end="")

# octal(int(input("Enter a decimal number : ")))
# 10. Write a recursive python function to find the Nth term of the Fibonacci series.
# def Fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

# print(Fibonacci(int(input("Which term of Fibonacci series? "))))
    