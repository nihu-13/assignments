# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).
 class Profile:
    
     def __init__(self,name,age,email):
         self.name=name
         self.age=age
         self.email=email
        
# 2. Write a python script to update the above Profile class with encapsulation.
 class Profile:
    
     def __init__(self,name,age,email):
         self.name=name
         self.age=age
         self.email=email

# 3. Write a python script to update 2nd Question, change email and age to __email and
# # __age.
 class Profile:
     __age=56
     __email="niharika@gmail.com"
     def __init__(self,name):
         self.name=name

 b1=Profile("niharika ")
 print(b1.__age)
# 4. Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.
# 5. Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values.
 class Calculator:
     def adding(self,a,b):
         return a+b
   
     def subtracting(self,a,b):
         return a-b
    
 o1=Calculator()
 print("A + B = ",o1.adding(3,5))
 print("A - B = ",o1.subtracting(3,5))
# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.
 class Calculator:
     def adding(self,a,b):
         return a+b
    
     def subtracting(self,a,b):
         return a-b
    
 class Calculator2(Calculator):
     def mutiplication(self,a,b):
         return a*b
     def division(self,a,b):
         return a/b
    
 o1=Calculator2()
 print("A + B = ",o1.adding(3,5))
 print("A - B = ",o1.subtracting(3,5))
 print("A * B = ",o1.mutiplication(3,5))
 print("A / B = ",o1.division(3,5))
# 7. Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).
 class Phone:
     def call(self):
         print("Calling")
    
     def sms(self):
         print("SMS")
        
 o1=Phone()
 o1.call()
 o1.sms()
# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.
 class Calculator:
     def adding(self,a,b):
         return a+b
    
     def subtracting(self,a,b):
         return a-b
    
 class Calculator2(Calculator):
     def mutiplication(self,a,b):
         return a*b
     def division(self,a,b):
         return a/b

 class Phone:
     def call(self):
         print("Calling")
    
     def sms(self):
         print("SMS")
 class SmartPhone(Calculator2,Phone):
     def smartphone(self):
         print("This is smartphone")

 o1=SmartPhone()
 o1.smartphone()
 print("A + B = ",o1.adding(4,5))
 o1.call()
 print("A * B = ",o1.mutiplication(1,2))
# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).
class Truecaller:
    def add_entry(self,name,number):
        self.name=name
        self.number=number
    
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.add_entry(self.name,self.number)
        
    def getinfo(self):
        print(self.name,self.number,sep=",")

person=Truecaller("niharika",3483902349)
person.add_entry("nishant",26637979)
person.getinfo()

        
# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.        
class Truecaller:
    def add_entry(self,name,number):
        self.name=name
        self.number=number
    
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.add_entry(self.name,self.number)
        
    def getinfo(self):
        print(self.name,self.number,sep=",")


class SmartPhone:
     def smartphone(self):
         print("This is smartphone")
        
     def __init__(self):
        self.obj=Truecaller("niharika",3483902349)
        
person1=SmartPhone()        
person2=person1.obj

print(person2)
