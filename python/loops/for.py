# how to loop through a list using for loop
print("==================================================")
print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print()

# how to loop through a string using for loop
print("==================================================")
print()
for x in "banana":
  print(x)
print()

# the break keyword
print("==================================================")
print("break keyword:")
print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print()

# the continue keyword
print("==================================================")
print("continue keyword:")
print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print()

# the range function
print("==================================================")
print("range function:")
print()
# program 1
for x in range(6):
  print(x)
print()

# program 2
for x in range(2, 6):
  print(x)
print()

# program 3
for x in range(2, 30, 3):
  print(x)
print()

# else in for loop
print("==================================================")
print("else in for loop:")
print()
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print()

# nested for loop
print("==================================================")
print("nested for loop:")
print()
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
print()
