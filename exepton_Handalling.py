# 1. Write a python script to create a ArithmeticError
a=99
b=0
c=a/b    # ArithmeticError
print(c)
# 2. Write a python script to create a ValueError
a=99
b=int(input("Enter A Number"))
c=a/b    # ValueError
print(c)
# 3. Write a python script to handle the ArithmeticError
a=99
b=0
try:
    c=a/b    # ArithmeticError
except ZeroDivisionError:
    print("Division By Zore")

# 4. Write a python script to handle a ValueError
a=99
try:
    b=int(input("Enter A Number"))
    c=a/b
except ValueError:
    print("Please Enter Only Number ")
# 5. Write a python script to handle multiple Exception in one try
a=2
b="niharika"
c=0
try:
    c=a+b
except Exception:
    print("Some Error Is Accour")
# 6. Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exception
# s.
class Calculater:
    def add(self,a,b):
        print("Addition : ",a+b)
    def sub(self,a,b):
        print("Subtraction : ",a-b)
    def mul(self,a,b):
        print("Multipication : ",a*b)
    def div(self,a,b):
        print("Division : ",a/b)

obj=Calculater()
try:
    obj.add(3,5)
    obj.div(6,6)
    obj.mul(3,6)
    obj.sub(1,5)
except Exception:
    print("Some Error ")
    

# 7. Write a python script to add a finally block for the above script
class Calculater:
    def add(self,a,b):
        print("Addition : ",a+b)
    def sub(self,a,b):
        print("Subtraction : ",a-b)
    def mul(self,a,b):
        print("Multipication : ",a*b)
    def div(self,a,b):
        print("Division : ",a/b)

obj=Calculater()
try:
    obj.add(3,5)
    obj.div(6,6)
    obj.mul(3,6)
    obj.sub(1,5)
except Exception:
    print("Some Error ")
finally:
    print("Succecfull")
# 8. Write a python script to implement try except and else block for division
a=23
b=int(input("Enter Only Number : "))
c=0
try:
    c=a/b
except Exception:
    print("Some Error IS Accour ")
else:
    print(c)
# 9. Write a python script to raise a ValueError.
a=2
b=2
c=0
if a==b:
    raise ValueError()
try:
   c=a+b
except ValueError:
    print("Valueerror ") 
# 10. Write a python script to implemented a nested Try Except block
def f2():
    try:
        a = 4
        raise SyntaxError
    except SyntaxError as se:
        print('log SE')
        raise se from None
    finally:
        try:
            raise ValueError
        except ValueError as ve:
            a = 5
            print('log VE')
            raise ve from None
        finally:
            return 6
        return a

f2()

