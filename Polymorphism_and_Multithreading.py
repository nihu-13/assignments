# 1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
# a class using method overloading.
class Multiple:
    
    def mul(self, a = None, b = None, c = None,d=None):
        if  a != None and b != None and c != None and d!=None:
            print(a*b*c*d)
        elif a != None and b != None and c != None:
            print(a*b*c)
        elif a != None and b != None:
            print(a*b)
        else:
            print(a)
                    
    
    
obj1=Multiple()
obj1.mul(2,3)
obj1.mul(2,3,2)
obj1.mul(2,3,4)
# 2. Write a python script to create a user account class with 2 instance variables (userid
# and balance). Create 3 user objects and add all the users using operator
# overloading.
class UserAccount:
    def __init__(self,userid, balance):
        self.userid=userid
        self.balance=balance
        
    def __add__(self, a):
        tuserid=self.userid+a.userid
        tbalance=self.balance+a.balance
        return UserAccount(tuserid,tbalance)
    
obj=UserAccount(1,10022)
obj1=UserAccount(2,10022)
obj2=UserAccount(3,10022)
t=obj+obj1+obj2
print(t.userid,t.balance)

# 3. Write a python script to create a to print the above user account object using operator
# overloading (hint __str__ method).
class UserAccount:
    def __init__(self,userid, balance):
        self.userid=userid
        self.balance=balance
        
    def __str__(self):
        return 'UserAccount(userid = '+self.userid + 'balance = '+self.balance +')'
    
obj=UserAccount('1','10022')

print(obj.__str__())
# 4. Write a python script to create two Threads. First thread will print all Even numbers
# and Second thread will print all Odd numbers till 100.
from threading import *
from time import sleep


class First(Thread):
    
    def run(self):
       print("Even Numbers : ")
       for i in range(100):
           if i%2==0 :
               print(i,sep=" ",end="")
               sleep(2)
 
 
            
class Second(Thread):
    def run(self):
       print("Odd Numbers : ")
       for i in range(100):
           if i%2!=0 :
               print(i,sep=" ",end="")
               sleep(2)
       
obj1=First()
obj2=Second()

obj1.start()
obj2.start()   


# 5. Write a python script to create 2 threads to add all the values from 1 to 100.
class First(Thread):
    def run(self):
        s=sum(range(100))
        print(s)
        sleep(2)



class Second(Thread):
    def run(self):
        s=sum(range(100))
        print(s)
        sleep(2)


obj1 = First() 
obj2 = Second() 

obj1.start() 
sleep(1)
obj2.start()


# 6. Write a python script to create 5 threads to fill a list with random numbers till 100.
import random
class First(Thread):
    def run(self):
        res = random.sample(range(100),49)
        print ("Random number list is : " +  str(res))
        sleep(2)



class Second(Thread):
    def run(self):
        res = random.sample(range(100),5)
        print ("Random number list is : " +  str(res))
        sleep(2)

class Third(Thread):
    def run(self):
        res = random.sample(range(100),3)
        print ("Random number list is : " +  str(res))
        sleep(2)

class Fourth(Thread):
    def run(self):
        res = random.sample(range(100),8)
        print ("Random number list is : " +  str(res))
        sleep(2)

class Fifth(Thread):
    def run(self):
        res = random.sample(range(100),9)
        print ("Random number list is : " +  str(res))
        sleep(2)

obj1 = First() 
obj2 = Second() 
obj3=Third()
obj4=Fourth()
obj5=Fifth()

obj1.start() 
sleep(1)
obj2.start()
obj3.start() 
sleep(1)
obj4.start()
obj5.start() 
# 7. Write a python script to create a clock where 1st thread will print the current time
# every second and 2nd will print “1 Minute Completed” after every 1 minute.

# 8. Write a python script to change the name of the Thread.
thread=Thread()
print(thread.name)
thread.name="Niharka"
print(thread.name)
# 9. Write a python script to join 2 threads after printing completing the first Question.

# 10. Write a python script to check whether a given number is prime or armstrong number
# using 2 different threads.
class First(Thread):
    def run(self,num):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
                else:
                    print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
            
            
class Second(Thread):
    def run(self,number):
        digits = len(str(number))
        temp = number
        add_sum = 0
        while temp != 0:
            k = temp % 10
            add_sum += k**digits
            temp = temp//10
        if add_sum == number:
            print('Given number is an Armstrong Number')
        else:
            print('Given number is not a Armstrong Number')


obj1=First()
obj2=Second()

obj1.start()
obj2.start()
