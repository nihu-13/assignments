# 1. Write a python script to create a String in 3 different possible ways
s1="iNeuron"
s1=str("iNeuron")
s1='iNeuron'
# 2. Write a python script to Get the characters from the start to position 5 (Given String
# “iNeuron” using the slice syntax)
s1="iNeuron"
print(s1[5::1])
# 3. Write a python script to Get the characters from position 2 to position 5 (Given String
# “Hello Learners” using the slice syntax)
s1="Hello Learners"
print(s1[2:5:1])
# 4. Write a python script to demonstrate String Concatenation adding space in between (
# Given Strings a=”Learning” b=”Python” )
a="Learning" 
b="Python"
print(" ".join([a,b]))
# 5. Write a python script to get the count of total number of characters in String a=
# “iNeuron”
a="iNeuron"
Count = len([ele for ele in a if ele.isalpha()])
print(Count)
# 6. Write a python script to reverse a String. (“iNeuron”)
s1="iNeuron"
print(s1[-1::-1])
# 7. Write a python script to determine whether a string contains a specific substring.
string="Niharika Sahu"
substring="Sahu"
if string.find(substring)==-1:
    print("Not Found")
else:
    print("Found")
# 8. Write a python script to check if a string contains only numbers.
s1=str(input("Enter String : "))
if s1.isdigit():
    print("String contain number")
else:
    print("String not contain number")
# 9. Write a python script to check if a string contains only characters of the alphabet.
s1=str(input("Enter String : "))
if s1.isalpha():
    print("String contain character")
else:
    print("String  not contain character")
# 10. Write a python script to convert an integer to a string.
num=13
str_num=str(num)
print(type(str_num))
