# how to handle an exception
try:
  print(x)
except:
  print("An exception occurred")
print()

# how to define multiple exception
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
print()

# how to use else keyword after except
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
print()

# use of finally keyword
# program 1
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
print()

# program 2
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
print()

# how to raise an exception
# program 1
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# program 2
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
