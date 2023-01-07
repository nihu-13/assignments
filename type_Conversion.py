# 1. Write a python script to convert a number into str type.
num1=6
print(type(str(num1)))
# 2. Write a python script to print Unicode of the character ‘m’
print(ord("m"))
# 3. Write a python script to print character representation of a given unicode 100.
print(chr(100))
# 4. Write a python script to print any number and its binary equivalent
num=67
print(bin(num))
# 5. Write a python script to print any number and its octal equivalent.
num=17
print(oct(num))
# 6. Write a python script to print any number and its hexadecimal equivalent.
num=67
print(hex(num))
# 7. Write a python script to store binary number 1100101 in a variable and print it in
# decimal format.
num=0b1100101
print(num)
# 8. Write a python script to store a hexadecimal number 2F in a variable and print it in
# octal format.
num=0x2F
print(oct(num))
# 9. Write a python script to store an octal number 125 in a variable and print it in binary
# format.
num=0o125
print(bin(num))
# 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
# display the result in binary format.
num1=0o25
num2=0x39
add=num1+num2
print(bin(add))