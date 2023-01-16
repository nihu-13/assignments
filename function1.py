# 1. Write a python program to create a function that takes a list and returns a new list
# with the original list's unique elements.
 def list1(a):
     set1=set(a)
     l1=list(set1)
     print("List of unique numbers : ",l1)
    
 l=[55,64,23,444,11,11,22,33]
 print("Original List : ",l)    
 list1(l)
# 2. Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not.
 def is_prime(n):
   for i in range(2,n):
     if (n%i) == 0:
       return False
   return True
 if is_prime(9)==True:
     print("Number Is Prime Number")
 else:
     print("Number Is Not Prime Number")
# 3. Write a python program to create a function that prints the even numbers from a
# given list
 def check_Even(a):
     for i in a:
         if i%2==0:
             print(i,end=" ")
         else:
             pass
 Sample_List=[1, 2, 3, 4, 5, 6, 7, 8, 9]
 check_Even(Sample_List)

# 4. Write a python program to create a function that checks whether a passed string is
# palindrome or not.
 def is_palindrome(string):
     if string==string[::-1]:
         print("palindrome")
     else:
         print("Not palindrome")

 is_palindrome("abcdcb")
# 5. Write a python program to create a function to find the Min of three numbers.
 def minimum(a,b,c):
     print("min = ",min(a,b,c))
    
 minimum(45,3,5)
# 6. Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.
 def square():
     l=list()
     for i in range(1,30,1):
         l.append(i**2)
     print(l)
        
 square()
# 7. Write a python program to access a function inside a function.
 def make_adder(x):
     def adder(y):
         return x+y
     return adder

 a=make_adder(2)
 print(a(5))
# 8. Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.
 def check(a):
     cout=0
     cout1=0
     for i in a:
         if (i.isupper()):
             cout+=1
         else:
             cout1+=1
     print("count for Uppercase : ",cout,"count for Lower case : ",cout1)
    
 check(input("Enter a string :"))
# 9. Write a python program to create a function to check whether a string is a pangram
# or not.
 def pangram(a):
     alpha="abcdefghijklmnopqrstuvwxyz"
     for c in alpha:
         if c not in a: 
             return False
     return True

 if pangram(input("Enter a string:"))==False:
     print("not pangram")
 else:
     print("pangram")
# 10. Write a python program to create a function to check whether a string is an anagram
# or not.
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         

check(input("Enter 1st string : "), input("Enter 2nd string : "))
