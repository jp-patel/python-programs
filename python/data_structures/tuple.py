# tuple
# tuple is a collection which is:
# ordered
# unchangable
# allow duplicate

# how to initialize a tuple
my_tuple = ("firstname","secondname","lastname")

# how to print tuple items
print(my_tuple)
print()

# how to print length of tuple
print(len(my_tuple))
print()

# how to see type of tuple
print(type(my_tuple))
print()

# how to make tuple using tuple constructor

my_tuple=tuple(("firstname","secondname","lastname","email","DOB","address","pincode","state","country"))
print(my_tuple)
print()

# how to access tuple items
print(my_tuple[1])
print()

# how to use negative indexing
print(my_tuple[-1])
print()

# how to use range of indexing
print(my_tuple[2:5])
print(my_tuple[2:])
print(my_tuple[:5])
print()

# how to use range of negative indexing
print(my_tuple[-5:-1])
print(my_tuple[-5:])
print(my_tuple[:-5])
print()

# how to check if an item exists in a tuple or not
print("DOB" in my_tuple)
print("mobile_no" in my_tuple)
print()

# how to loop through tuple
for x in my_tuple:
    print(x)
print()

# how to loop through index numbers in tuple
for i in range(len(my_tuple)):
    print(my_tuple[i])
print()

# how to unpack a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print()

# how to unpack using asterisk
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# how to join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
print()

# how to multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
print()
