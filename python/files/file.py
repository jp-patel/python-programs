# how to open a file in reading mode
f = open("read.txt", "r")

# how to read a file
print(f.read())
print()

# how to close a file
f.close()


# how to open a file from different location or with complete path
# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())
# print()
# f.close()


# how to read first n characters of file
f = open("read.txt", "r")
print(f.read(5))
print()
f.close()

# how to read a file line by line
# sample 1
f = open("read.txt", "r")
print(f.readline())
print()
f.close()

# sample 2
f = open("read.txt", "r")
print(f.readline())
print(f.readline())
print()
f.close()

# how to loop through the file line by line
f = open("read.txt", "r")
for x in f:
  print(x)
print()
f.close()

f = open("write.txt", "r")
#reading file befor writing
print("Data in write.txt before writing to it:")
print(f.read())
print()
f.close()

# how to write to the file
f = open("write.txt", "w")
f.write("Writing first line\nWriting secong line\nWriting third line")
f.close()

#open and read the file after the writing:
f = open("write.txt", "r")
print("Data in write.txt after writing to it:")
print(f.read())
print()
f.close()

f = open("append.txt", "r")
#reading file befor appending
print("Data in append.txt before appending to it:")
print(f.read())
print()
f.close()

# how to append to the file
f = open("append.txt", "a")
f.write("Appending first line\nAppending secong line\nAppending third line")
f.close()

#open and read the file after the appending:
f = open("append.txt", "r")
print("Data in append.txt after appending to it:")
print(f.read())
print()
f.close()

# how to use with keyword
with open("text.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

# how to delete files
import os
if os.path.exists("delete.txt"):
  os.remove("delete.txt")
else:
  print("The file does not exist")
print()
