# some built -in math functions

# how to use min(), max()
print("==================================================")
print("min and max:")
print("==================================================")
print()
x = min(5, 10, 25)
y = max(5, 10, 25)

print("maximum of 5,10, and 25 is ",end='')
print(x)
print("minimum of 5,10, and 25 is ",end='')
print(y)
print()

# how to use abs()
print("==================================================")
print("absolute function:")
print("==================================================")
print()
x = abs(-7.25)

print("absolute value of -7.25 is ",end='')
print(x)
print()

# how to use pow()
print("==================================================")
print("power function:")
print("==================================================")
print()
x = pow(4, 3)

print("pow(4, 3) = ",end='')
print(x)
print()

# ==================================================
# use of math module
# ==================================================

import math

# use of sqrt function to find square root of a number
print("==================================================")
print("square root function:")
print("==================================================")
print()
x = math.sqrt(64)

print(x)
print()

# how to use ceil() and floor()
print("==================================================")
print("ceil and floor function:")
print("==================================================")
print()
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
print()

# how to get the value of pi
print("==================================================")
print("value of pi:")
print("==================================================")
print()
x = math.pi

print(x)
print()
