# 1. Write a python program to create and print a dictionary which stores your information.
# (name, age, gender .....)
# info={"name":"niharika sahu","age":56,"gender":"femail"}
# print(info)
# 2. Write a python program to access the items of a dictionary by referring to its key
# name.
# info={"name":"niharika sahu","age":56,"gender":"femail"}
# print(info["name"])
# 3. Write a python program to get a list of the values from a dictionary.
# info={"name":"niharika sahu","age":56,"gender":"femail"}
# print(info.values())
# 4. Write a python program to change the value of a specific item by referring to its key
# name.
# info={"name":"niharika sahu","age":56,"gender":"femail"}
# info["name"]="nihu"
# print(info["name"])
# 5. Write a python program to print all key names in the dictionary, one by one.
# info={"name":"niharika sahu","age":56,"gender":"femail"}
# for i in info:
#     print(i)
# 6. Write a python program to create a dictionary that contains three dictionaries.
# (nested)
# 7. Write a python program to create three dictionaries, then create one dictionary that
# will contain the other three dictionaries.
d1={"name":"niharika sahu","age":56,"gender":"femail"}
d2= {'C': 92,'Java': 66,'Python': 85}
d3={"address":"Dixit colony","city":"jabalpur"}
d=d1 | d2 | d3
print(d)
# 8. Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.
# l1=[1,2,3,4]
# l2=["niharika","nihu","nushant","surbhi"]
# d=dict(zip(l1,l2))
# print(d)
# 9. Write a python program to merge two python dictionaries into one dictionary.
# info={"name":"niharika sahu","age":56,"gender":"femail"}
# info1={"address":"Dixit colony","city":"jabalpur"}
# information=info | info1
# print(information)
# 10. Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {'C': 92,'Java': 66,'Python': 85}
# lowest_value=min(sample_dict.values())
# for key in sample_dict:
#     if sample_dict[key]==lowest_value:
#         print(key)
