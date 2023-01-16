# 1. Write a python program to create a simple function which prints “MySirG” .
 def simple():
     print("MySirG")

 simple()

# 2. Write a python program to create a function which expects two arguments and print
# them in the function body.
 def simple(a,b):
     print("a=",a,"b=",b)

 simple(3,5)

# 3. Write a python program to create a function which expects an unknown number of
# arguments.
def create(*t):
    print(t)
    
create(55,64,33,222,8,76,33,454,35)
# 4. Write a python program to create a function which expects kwargs arguments.
 def simple(a,b):
     print("a=",a,"b=",b)

 simple(b=3,a=5)

# 5. Write a python program to create a function which expects a list as an argument.
 def simple(a):
     print(t)
 l=[345,56,2,9,4,2,5,22]
 simple(l1)

# 6. Write a python program to create a function that finds a maximum of four numbers.
 def maximum(a,b,c,d):
     print("max",max(a,b,c,d))
    
 maximum(78,56,9,5)
# 7. Write a python program to sum all the numbers in a list.
 def sum_all(t):
     print("Sum = ",sum(t))

 li=[45,56,3,53,5,342]

 sum_all(li)
# 8. Write a python program to multiply all the numbers in a list.
 def multi_all(t):
     result=1
     for i in t:
         result=i*result
        
     print("Multipication = ",result)
 li=[45,56,3,53,5,342]
 multi_all(li)
# 9. Write a python program to create a function to check whether a number falls in a
# given range.
 def check(a):
         if a in range(9):
             print("True")
         else:
             print("Falls")

 check(194)
# 10. Write a python program to create a function to check whether a given number is even
# or odd.
def check(a):

    
    if a%2==0:
            print("Even")
        else:
            print("ODD")

check(3)
