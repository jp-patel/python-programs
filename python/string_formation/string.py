# how to print a string
print("Hello")
print()

# how to print a string stored in a variable
a="Hello"
print(a)
print()

# how to print a multiline string
a="""this is
a multiline
string"""
print(a)
print()

# how to print a character of string
my_string="Hello World!"
print(my_string[1])
print()

# how to loop through the string
my_string="apple"
for x in my_string:
    print(x)
print()

# how to get string length
print(len(my_string))
print()

# how to check for a work in a string
txt = "The best things in life are free!"
print("free" in txt)
print()

# how to check for absence of a word in string
txt = "The best things in life are free!"
print("expensive" not in txt)
print()

# string slicing
b = "Hello, World!"
print(b[2:5])
print()

# slice from the start
b = "Hello, World!"
print(b[:5])
print()

# slice to the end
b = "Hello, World!"
print(b[2:])
print()

# negative indexing
b = "Hello, World!"
print(b[-5:-2])
print()

# string concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print()
