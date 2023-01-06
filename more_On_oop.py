# Write a python script to reverse a number.
# for e in range(10,0,-1):
#     print(e)

# 2. Write a python script to check whether a given number is Prime or not
n=int(input("Enter Number : "))
for e in range(2,n):
    if n%e==0:
        print("this is not a prime number ")
        break
else:
    print("this is a prime number ",e+1)
# 3. Write a python script to print all Prime numbers under 100
# for e in range(1,101):
#     if e>1:
#         for i in range(2,e):
#             if e%i==0:
#                 break
#         else:
#             print(e,end=" ")
# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
# 5. Write a python script to find next prime number of a given number
# 6. Write a python script to print first N prime numbers
# 7. Write a python script to check whether a given pair of numbers are co-Prime
# numbers or not.
# 8. Write a python script to print first N terms of a Fibonacci series
# a,b=0,1
# sum=0
# for e in range(0,int(input("Enter NUmber : "))):
#     print(b,end=" ")
#     sum=a+b
#     a=b
#     b=sum
# 9. Write a python script to calculate LCM of two numbers
# a=int(input("Entre number 1 : "))
# b=a=int(input("Entre number 1 : "))
# for e in range(0,):
#     print(b,end=" ")
#     sum=a+b
#     a=b
#     b=sum
# 10. Write a python script to calculate HCF of two numbers