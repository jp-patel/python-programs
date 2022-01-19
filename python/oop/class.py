# how to create a class
class MyClass:
  x = 5

# how to create an object
p1 = MyClass()
print(p1.x)
print()

# the __init__ function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print()

# how to make object methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print()

# how to modify the object property
p1.age = 40

# how to delete theobject property
del p1.age

# how to delete the object
del p1
