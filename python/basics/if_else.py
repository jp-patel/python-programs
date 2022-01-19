# simple if
print("==================================================")
print("simple if:")
print()

a = 33
b = 200
if b > a:
    print("b is greater than a")
print()

# elif
print("==================================================")
print("elif:")
print()

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
print()

# else
# program 1
print("==================================================")
print("else:")
print()

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print()

# program 2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print()

# use of and
print("==================================================")
print("use of and:")
print()

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
print()

# use of or
print("==================================================")
print("use of or:")
print()

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
print()

# nested if
print("==================================================")
print("use of or:")
print()

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print()
