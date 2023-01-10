# 1. Write a Python script to create a list of first N natural numbers.
l1=[x for x in range(1,int(input("Enter Number : ")))]
print(l1)
# 2. Write a Python script to create a list of first N odd natural numbers.
l1=[x for x in range(1,int(input("Enter Number : ")),2)]
print(l1)
# 3. Write a Python script to create a list of first N even natural numbers.
l1=[x for x in range(2,int(input("Enter Number : ")),2)]
print(l1)
# 4. Write a Python script to find the greatest number in a given list of numbers.
l1=[56,43,646,355,6,5,88,76]
print(max(l1))
# 5. Write a Python script to find the smallest number in a given list of numbers.
l1=[56,43,646,355,6,5,88,76]
print(min(l1))
# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
l1=[56,43,646,355,6,5,88,76]
print(sum(l1))
# 7. Write a Python script to remove all non int values from a list.
l1=[45,6,"hg",5.6,3+5j,666,True]
l1=[x for x in l1 if type(x)==int]
print(l1)
# 8. Write a Python script to print distinct elements along with their frequencies of
# occurrence in the list.
mylist=['a', 'a', 'b', 'b', 'b']
mylist=[ (i,mylist.count(i)) for i in set(mylist) ]
print(mylist)
# 9. Write a Python script to print indices of all occurrences of a given element in a given
# list.
l1=[56,43,646,355,6,5,88,76]
for x in l1:
    print(x,"[",l1.index(x),"], ")
# 10. Write a python script to sort a list.
l1=[56,43,646,355,6,5,88,76]
l1.sort()
print(l1)