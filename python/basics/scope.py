# ==================================================
# local scope
# ==================================================


print("local scope:")
print()
def myfunc():
  x = 300
  print(x)

myfunc()
print()

# function inside function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()
print()


# ==================================================
# global scope
# ==================================================


print("==================================================")
print("global scope:")
print()

# program 1
x = 300

def myfunc():
    print("Inner value:")
    print(x)

myfunc()
print("Outer value:")
print(x)
print()

# program 2
x = 300

def myfunc():
    print("Inner value:")
    x = 200
    print(x)

myfunc()
print("Outer value:")
print(x)
print()

# use of global keyword
x = 300

def myfunc():
    global x
    x = 200

myfunc()
print(x)
print()
