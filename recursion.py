# 1. Write a recursive python function to print first N natural numbers.
# def printN(n):
#     if n>0:
#         printN(n-1)
#         print(n)

# printN(10)
# 2. Write a recursive python function to print first N natural numbers in reverse order
# def printN(n):
#     if n>0:
#         print(n)
#         printN(n-1)

# printN(10)
# 3. Write a recursive python function to print first N odd natural numbers
# def Odd(n,count=1):
#     if n>=count:
#         print(2*count-1)
#         Odd(n,count+1)

# Odd(10)
# 4. Write a recursive python function to print first N odd natural numbers in reverse order
# def Odd(n,count=1):
#     if n>=count:
#         Odd(n,count+1)
#         print(2*count-1)

# Odd(10)
# 5. Write a recursive python function to print first N even natural numbers.
# def Even(n,count=1):
#     if n>=count:
#         print(2*count)
#         Even(n,count+1)

# Even(10)
# 6. Write a recursive python function to print first N even natural numbers in reverse
# order.
# def Even(n,count=1):
#     if n>=count:
#         Even(n,count+1)
#         print(2*count)

# Even(10)
# 7. Write a recursive python function to print squares of first N natural numbers
# def squares(n):
#     if n>0:
#         squares(n-1)
#         print(n*n)

# ssquares(10)
# 8. Write a recursive python function to print cubes of first N natural numbers
# def cube(n):
#     if n>0:
#         cube(n-1)
#         print(n**3)

# cube(10)
# 9. Write a recursive python function to print first N multiples of a given number.
# def printN(n):
#     if n>0:
#         printN(n-1)
#         print(number*n)
# number=2
# printN(10)
# 10. Write a recursive python function to print a number in reverse order.
def printN(n):
    if n>0:
        print(n)
        printN(n-1)

printN(10)