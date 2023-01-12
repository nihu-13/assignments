# 1.Write a python program to store all the programming languages known to you using
# # Set.
 languages={"c","c++","python","java"}
 print(languages)
# 2. Write a python program to store your own information {name, age, gender, so on..}
 info={input("Enter your name : "),int(input("Enter your age : ")),input("Enter your gender : "),input("Enter your adress : ")}
 print(info)
# 3. Write a python script to get the data type of a Set.
 s1={7,8,7,4}
 print(s1(type(s1)))
# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
 "Python", "Django"}
 thisset = {"Java","Python", "Django"}
 print("Python" in thisset)
# 5. Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}
 secondset= {"C", "Cpp", "NoSQL"}
 thisset ={"Java", "Python", "SQL"}
 secondset= {"C", "Cpp", "NoSQL"}
 thisset.update(secondset)
 print(thisset)
# 6. Write a python program to add elements of list to a set
 thisset = {"Python", "Django", "JavaScript"}
 mylist = ["Java", "C"]
 thisset.update(mylist)
 print(thisset)
# 7. Write a python program to remove last item of the given set
 thisset = {"Python", "Django", "JavaScript", “SQL”}
 thisset = {"Python", "Django", "JavaScript", "SQL"}
 thisset.remove("SQL")
 print(thisset)
# 8. Write a python program to delete the set completely.
 thisset = {"Python", "Django", "JavaScript", "SQL"}
 thisset.clear()
 print(thisset)
# 9. Write a python program to loop through the set and print values
 thisset = {"Python", "Django", "JavaScript", "SQL"}
 for i in thisset:
     print(i)
# 10. Write a python program to find the maximum and minimum value in a set.
 l1={3,55,2,7,45,64,34}
 print(max(l1))

