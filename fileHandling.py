# 1. Write a Python script to print the following status of a file:
# a. Whether a file is read only
f.read()
# b. Whether a file is closed or not
f.closed
# c. Which file opening mode is used
f.mode
# d. Name of the file
f.name
# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
def createFile(data):
    f=open("myfile.txt","w")
    f.write(data)
    
createFile("jhfskjjcnvhshkj")
# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on
# the console.
try:
    f=open("myfile.txt","r")
    text=f.read()
    print(text)
except FileNotFoundError:
    print("File Not Found")
# 4. Write a Python script to store a list of city names in a file ‘cities.txt’
l1=["Jabalpur\n","bhopal\n","Indor\n","Pune\n"]
f=open('cities.txt', 'w')
f.writelines(l1)
f.close()
# 5. Write a Python script to append list of city names in a file ‘cities.txt’
l1=["Jaipur\n","Bihar\n"]
f=open('cities.txt', 'a')
f.writelines(l1)
f.close()
# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or
# not
def search(filename,word):
    try:
        f=open(filename,"r")
        line_count=0
        for line in f.readlines():
            line_count+=1
            strlist=line.split('\n')
            word_count=0
            for w in strlist:
                word_count+=1
                if word==w:
                    print("Present")
        f.close()
    except FileNotFoundError:
        print("File Not Found")
            
search("cities.txt","Bihar")
# 7. Write a Python script to count the number of Python keywords occurring in a python
# source file.
count = 0
f = open("cities.txt", "r")
for line in f:
	word = line.split("\n")
	count += len(word)

print("Total Number of Words: " + str(count))
f.close()

# 8. Write a Python script to create a copy of a file.
import os
os.system("command")
os.system('copy cities.txt destination.txt')
# 9. Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile)
import pickle
Bookfile={"Physics":400,"Physics":400,"Chemistry":500,"English":300,"Math":1200}
f=open("Bookfiles.txt","ab")
pickle.dump(Bookfile,f)
f.close()
# 10. Write a Python script to extract book data from a bookfile using pickle. Also print
# extracted book data.
f=open("Bookfiles.txt","rb")
s=pickle.load(f)
for key in s:
    print(key,s[key],sep=" : ")
f.close()