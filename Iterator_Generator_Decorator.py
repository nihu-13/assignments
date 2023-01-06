# 1. Use iter and next method to access all the elements of a given set using while loop
# t1=(5,46,6,34,3)
# it=iter(t1)
# for e in t1:
#     print(next(it))
# 2. Create a generator to produce first n odd natural numbers
# def oddGenrator(n):
#     x=1
#     while n:
#         yield x
#         x+=2
#         n-=1
# for i in oddGenrator(int(input("Enter howmany number you want to genrate : "))):         
#     print(i)
    
# 3. Create a generator to produce first n even natural numbers
# def oddGenrator(n):
#     x=2
#     while n:
#         yield x
#         x+=2
#         n-=1
# for i in oddGenrator(int(input("Enter howmany number you want to genrate : "))):         
#     print(i)
# 4. Create a generator to produce squares of first N natural numbers
# def oddGenrator(n):
#     x=1
#     while n:
#         yield x**2
#         x+=1
#         n-=1
# for i in oddGenrator(int(input("Enter howmany number you want to genrate : "))):         
#     print(i)
# 5. Create a generator to produce first n terms of Fibonacci series
# def fib(n):
#     x,y=0,1
#     while n:
#         yield x
#         x,y=y,x+y
#         n-=1
# for i in fib(int(input("Enter howmany number you want to genrate : "))):         
#     print(i)
# 6. Create a generator to produce first n prime numbers
# def isprime( num ) :
#     for i in range ( 2, num ) :
#         if num % i == 0 :
#             return False
#     return True
# def primeGenrator( n ) :
#     num=2
#     while n:
#         if isprime(num):
#             yield num
#             n-=1
#         num+=1
#     return
        
# for i in primeGenrator(int(input("Enter howmany number you want to genrate : "))):      
#     print(i)
# 7. Create an endless iterator using generator method to produce terms of Fibonacci
# series
# def fib_Genrator():
#     x,y=0,1
#     while True:
#         yield x
#         x,y=y,x+y
# l1=[]
# it=fib_Genrator()
# while True:
#     n=input("Do you want to  genrate another element [y/n] : ")
#     if n=="y":
#         x=next(it)
#         print(x)
#         l1.append(x)
#     else:
#         break
# print(l1)
# 8. Create an endless iterator using generator method to produce Prime numbers
def isprime(num ) :
    for i in range ( 2, num ) :
        if num % i == 0 :
            return False
    return True
def primeGenrator( ) :
    num=2
    while True:
        if isprime(num):
            yield num
        num+=1
    return
        
l1=[]
it=primeGenrator()
while True:
    n=input("Do you want to  genrate another element [y/n] : ")
    if n=="y":
        x=next(it)
        print(x)
        l1.append(x)
    else:
        break
print(l1)
# 9. Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.
# 10. Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not.