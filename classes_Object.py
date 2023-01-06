# 1. Write a python program to create a user class with 3 properties : name, age, email.
# class User:
#     name="Niharika Sahu"
#     age=19
#     email="niharika@gmail.com"

# u1=User()
# print(u1.name)
# print(u1.age)
# print(u1.email)

# 2. Write a python program to create a user class with a method to greet the user.
# class User:
#     def greet():
#         print("Good Morning")

# User.greet()

# 3. Write a python program to create 2 objects of the user class and assign different
# values.
# class User:
    # value=None
# u1=User()
# u2=User()
# u1.value=5
# u2.value=6
# print(u1.value)
# print(u2.value)
# 4. Write a python program to init default values for user object using __init__ method.
# class User:
    
#     def __init__(self,value=0):
#         self.value=value

# u1=User()
# print("Default value = ",u1.value)
# 5. Write a python program to delete the age property of the user.
# class Delete:
#     age=None

# u1=Delete()
# u1.age=12
# print(u1.age)
# del u1.age
# print(u1.age)
# 6. Write a python program to create 3 user objects and find the youngest of all.
# class Find_youngest:
#     def __init__(self,age):
#         self.age=age
        
# obg1=Find_youngest(89)
# obg2=Find_youngest(88)
# obg3=Find_youngest(45)
# list_obj=[obg1.age,obg2.age,obg3.age]
# print(min(list_obj),"is a Youngest of all")
# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).
# class Laptop:
#     def __init__(self,brand,ram,cpu,hdd):
#         self.brand=brand
#         self.ram=ram
#         self.cpu=cpu
#          self.hdd=hdd
    
    # def showConfig(self):
#         print("brand : ",self.brand)
#         print("cpu : ",self.cpu)
#         print("ram : ",self.ram)
#         print("hdd : ",self.hdd)

# l1=Laptop("Hp","4gb","12th Generation Intel® Core™ i5 processor","1TB")
# l1.showConfig()
# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.
# class Laptop:
#     def __init__(self,brand,ram,cpu,hdd):
#         self.brand=brand
#         self.ram=ram
#         self.cpu=cpu
#         self.hdd=hdd
   
#     def showConfig(self):
#         print("brand : ",self.brand)
#         print("cpu : ",self.cpu)
#         print("ram : ",self.ram,"gb")
#         print("hdd : ",self.hdd)

# l1=Laptop("Hp",88,"12th Generation Intel® Core™ i5 processor","1TB")
# l2=Laptop("Hp",42,"12th Generation Intel® Core™ i5 processor","1TB")
# l3=Laptop("Hp",5,"12th Generation Intel® Core™ i5 processor","1TB")
# list_ram=[l1.ram,l2.ram,l3.ram]
# sortlist=sorted(list_ram)
# for x in sortlist:
#     print(x,"gb")
# l1.showConfig()
# l2.showConfig()
# l3.showConfig()
# # 9. Write a python program to create a School class and 3 instance variables and 1 class
# # variable.
# class School:
#     school_name="Samdariya Public School"
#     def __init__(self,name,age,persent):
#         self.name=name
#         self.age=age
#         self.persent=persent


# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field valuesv
# class Employee:
#     def __init__(selfemployee,empid, name, salary):
#         selfemployee.empid=empid
#         selfemployee.name = name
#         selfemployee.salary = salary
 
#     def details(selfemployee):
#         print("Employee Name:",  selfemployee.name)
#         print("Employee id:", selfemployee.empid)
#         print("Employee salary:", selfemployee.salary)
 
 
# emp = Employee(68656855, "Niharika Sahu",36)
# emp.details()