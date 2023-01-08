# 01 Write a python script to check whether a given number is positive or non-positive :
 a=int(input("Enter a Number\n"));
 print("positive" if a>0 else "non-positive");

# 02 Write a python script to check whether a given number is divisible by 5 or not :
 number=int(input("Enter A Number\n"))
 print("Divisible By 5" if number%5==0 else "Not Divisible By 5");

# 03 Write a python script to check whether a given number is even or odd : 
 number=int(input("Enter A Number\n"))
 print("Even" if number%2==0 else "Odd")

# 04 Write a python script to print greater between two numbers. Print number only once even if the numbers are the same :
 num1=int(input("Enter A Number 1:\n"))
 num2=int(input("Enter A Number 2:\n"))
 if num1>num2:
     print(num1,"is greater\n")
 elif num1<num2:
     print(num2,"is greater\n")
 else:
     print("Both Number are equal")

# 05 Write a python script to print two given words in dictionary order :
 a=input("Enter a word\n")
 b=input("Enter second word")
 if a<b:
     print(b,a)
 else:
     print(a,b)

# 06 Write a python script to check whether a given number is a three digit number or not. :
 number=(input("Enter A Number\n"))
 print("Three Digit Number" if len(number)==3 else "Not")

# 07 Write a python script to check whether a given number is positive, negative or zero. :
 number=int(input("Enter A Number \n"))
 if number>0:
     print("Positive")
 elif number<0:
     print("Negative")
 else:
     print("Zero")

# 08 Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots :
import math

a = int(input('Enter values of a: '))
b = int(input('Enter values of b: '))
c = int(input('Enter values of c: '))

d = b*b - 4*a*c

if d == 0:
    root1 = ( - b) / (2 * a)
    root2 = root1
    print('Roots are real & equal, Root1 =',root1,' Root2 = ',root2)

elif d > 0:
    root1 =  - (b + math.sqrt(d)) / (2 * a)
    root2 =  - (b - math.sqrt(d)) / (2 * a)
    print('Roots are real & distinct, Root1 =',root1,' Root2 = ',root2)

else:
    print('Roots are imaginary')


# 09 Write a python script to check whether a given year is a leap year or not :
 year=int(input("Enter year\n"))
 if year%4==0 :
     print(year,"Leap Year")
 else:
     print("NOT")

# 10 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same :
 num1=int(input("Enter A Number 1:\n"))
 num2=int(input("Enter A Number 2:\n"))
 num3=int(input("Enter A Number 3:\n"))
 if num1>num2>num3:
      print(num1,"is greater\n")
 elif num1<num2<num3:
      print(num3,"is greater\n")
 elif num1<num2 and num2>num3:
       print(num2,"is greater")
 else:
      print("Numbers are equal")

# 11 Write a python script to take the month value in numeric format and display the number of days in it :
 month=int(input("Enter The Month Value In Numeric Format\n"))
 match month:
      case 1:
          print("January : 31 Days")
      case 2:
          print("February : 28/29 Days")        
      case 3:
          print("March : 30 Days")
      case 4:
          print("April : 31 Days")
      case 5:
          print("May : 30 Days")
      case 6:
          print("June : 31 Days")
      case 7:
          print("July : 30 Days")
      case 8:
          print("August : 31 Days")
      case 9:
          print("September : 30 Days")
      case 10:
          print("October : 31 Days")
      case 11:
          print("November : 30 Days")
      case 12:
          print("December : 31 Days")
      case _:
          print("Enter number between 1-12")
    
# 12 Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part :
 number=complex(input("Enter Complex Number\n"))
 if number.real>number.imag:
     print(number.real,"is greater")
 else:
     print(number.imag, "is greater")
