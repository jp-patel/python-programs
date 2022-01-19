# dictionary
# dictionary is a collection which is:
# unordered (As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.)
# changable
# do not allow duplicate

# how to initialize a dictionary
my_dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

# how to print dictionary items
print(my_dictionary)
print()

# how to print length of dictionary
print(len(my_dictionary))
print()

# how to see type of dictionary
print(type(my_dictionary))
print()

# how to access dictionary items
print(my_dictionary["brand"])
print()

# how to check if an item exists in a dictionary or not
print("color" in my_dictionary)
print("brand" in my_dictionary)
print()

# how to add item in dictionary
my_dictionary["color"]="white"
print(my_dictionary["color"])
print()

# how to change item value in dictionary
my_dictionary["color"]="black"
print(my_dictionary["color"])
print()

# how to loop through dictionary
for x in my_dictionary:
    print(x)
print()

# how to get keys from dictionary
for x in my_dictionary.keys():
    print(x)
print()

# how to get values from dictionary
for x in my_dictionary:
    print(my_dictionary[x])
print()

# how to get values from dictionary
for x in my_dictionary.values():
    print(x)
print()

# how to get itemss from dictionary
for x in my_dictionary.items():
    print(x)
print()
