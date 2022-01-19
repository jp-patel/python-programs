# the lambda function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# how to use a labda function
print("==================================================")
print("lambda function:")
print()
# program 1
x = lambda a : a + 10
print(x(5))
print()

# program 2
x = lambda a, b : a * b
print(x(5, 6))
print()

# program 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print()

# how to use lambda with a function
print("==================================================")
print("returning a value returned by lambda from function:")
print()

# program 1
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
print()

# program 2
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
print()
