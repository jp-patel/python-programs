# how to create and call a function
print("==================================================")
print("how to create a function:")
print()

def my_function():
  print("Hello from a function")

my_function()
print()

# arguments
print("==================================================")
print("arguments:")
print()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()

# number of arguments
print("number of arguments:")
print()

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
print()

# arbitrary arguments
print("arbitrary arguments:")
print()

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print()

# keyword arguments
print("keyword arguments:")
print()
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print()

# arbitrary keyword arguments
print("arbitrary keyword arguments:")
print()

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
print()

# default parameter value
print("==================================================")
print("default parameter:")
print()

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print()

# passing a list as an argument
print("==================================================")
print("passing a list as an argument:")
print()

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print()

# returning values
print("==================================================")
print("returning a value:")
print()

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print()
