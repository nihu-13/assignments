# 1. Write a python script to calculate sum of first N natural numbers
k=0
for i in range(int(input("Enter number : "))):
    k=k+i
print(k)
# 2. Write a python script to calculate sum of squares of first N natural numbers
k=0
for i in range(int(input("Enter number : "))):
    k=k+(i**2)
print(k)
# 3. Write a python script to calculate sum of cubes of first N natural numbers
k=0
for i in range(int(input("Enter number : "))):
    k=k+(i**3)
print(k)
# 4. Write a python script to calculate sum of first N odd natural numbers
k=0
for i in range(int(input("Enter number : "))):
    k=k+2*i-1
print(k)
# 5. Write a python script to calculate sum of first N even natural numbers
k=0
for i in range(int(input("Enter number : "))):
    k=k+2*i
print(k)
# 6. Write a python script to calculate factorial of a given number
n=int(input("Enter Number : "))
p,i=1,1
while i<=n:
    p=p*i
    i+=1
    
print("Factorial is : ",p)
print()
# 7. Write a python script to count digits in a given number
n=int(input("Enter Number : "))
count=0
while n!=0:
    n=n//10
    count+=1
    
print(str(count))
# 8. Write a python script to calculate sum of digits of a given number
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)
# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)
n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)

print("Enter the Decimal Number: ")
decnum = int(input())

i = 0
octnum = []
while decnum!=0:
    rem = decnum%8
    octnum.insert(i, rem)
    i = i+1
    decnum = int(decnum/8)

print("\nEquivalent Octal Value is: ")
i = i-1
while i>=0:
    print(octnum[i], end="")
    i = i-1
print()