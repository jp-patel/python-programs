# how to use module
import module_1

module_1.greeting("Kerry")
print()

a = module_1.person1["age"]
print(a)
print()

# renaming a module
import module_2 as m2

a = m2.person1["age"]
print(a)
print()

# built in modules
import platform

x = platform.system()
print(x)
print()

x = dir(platform)
print(x)
print()

# how to import from module
from module_3 import person1

print (person1["age"])
