# 1. Write a python script to store multiple items in a single variable ( Items are “Java”
# ,“Python”, “SQL”, “C” ) using list
l1=["Java","Python","SQL","C"]
# 2. Write a python script to get the data type of a list.
l1=["Java","Python","SQL","C"]
print(l1)
# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print(mylist[-1])
# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
# "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist[1]="NoSQL"
thislist[3]="Flutter"
print(thislist)
# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
# ["Java", "SQL", "C", "Reactnative"]
mylist =["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print(mylist)

# 6. Write a python program to append elements from another list to the current list.(
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 
thirdlist=firstlist+secondlist
print(thirdlist)
# 7. Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
# "C", "Reactjs", "Javascript", "Python"]
thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)
# 9. Write a Python script to create a list of city names taken from the user.
ls=[]
for i in range(0,int(input("Enter number of cities you wnat to enter : "))):
    city=str(input("Enter city name : "))
    ls.append(city)
print(ls)
# 10. Write a Python script to create a list, where each element of the list is a digit of a
# given number.
k=5
ls=[]
for i in range(0,int(input("Howmany elment you wnat to enter : "))):
    el=str(input("Enter element : "))
    if str(k) in str(el):
        ls.append(el)
print("orignal list : ",str(ls))