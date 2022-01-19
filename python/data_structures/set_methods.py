# add
print("==================================================")
print("add:")
print()

fruits = {"apple", "banana", "cherry"}
print("Before add:")
print(fruits)
print()
fruits.add("orange")
print("After add:")
print(fruits)
print()

# clear
print("==================================================")
print("clear:")
print()

print("Before clear:")
print(fruits)
print()
fruits.clear()
print("After clear:")
print(fruits)
print()

# copy
print("==================================================")
print("copy:")
print()

fruits = {"apple", "banana", "cherry"}
print("Before copy:")
print(fruits)
print()
x = fruits.copy()
print("After copy:")
print(x)
print()

# difference
print("==================================================")
print("difference:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before difference:")
print(x)
print()
z = x.difference(y)
print("After difference:")
print(z)
print()

# difference_update
print("==================================================")
print("difference_update:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before difference_update:")
print(x)
print()
x.difference_update(y)
print("After difference_update:")
print(x)
print()

# discard
print("==================================================")
print("discard:")
print()

fruits = {"apple", "banana", "cherry"}
print("Before discard:")
print(fruits)
print()
fruits.discard("banana")
print("After discard:")
print(fruits)
print()

# intersection 
print("==================================================")
print("intersection:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before intersection:")
print(x)
print()
z = x.intersection(y)
print("After intersection:")
print(z)
print()

# intersection_update
print("==================================================")
print("intersection_update:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before intersection_update:")
print(x)
print()
x.intersection_update(y)
print("After intersection_update:")
print(x)
print()

# isdisjoint
print("==================================================")
print("isdisjoint:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
print()

# issubset
print("==================================================")
print("issubset:")
print()

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
print()

# issuperset
print("==================================================")
print("issuperset:")
print()

z = y.issuperset(x)
print(z)
print()

# pop
print("==================================================")
print("pop:")
print()

fruits = {"apple", "banana", "cherry"}
print("Before pop:")
print(fruits)
print()
fruits.pop()
print("After pop:")
print(fruits)
print()

# remove
print("==================================================")
print("remove:")
print()

fruits = {"apple", "banana", "cherry"}
print("Before remove:")
print(fruits)
print()
fruits.remove("banana")
print("After remove:")
print(fruits)
print()

# symmetric_difference
print("==================================================")
print("symmetric_difference:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before symmetric_difference:")
print(x)
print()
z = x.symmetric_difference(y)
print("After symmetric_difference:")
print(z)
print()

# symmetric_difference_update
print("==================================================")
print("symmetric_difference_update:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before symmetric_difference_update:")
print(x)
print()
x.symmetric_difference_update(y)
print("After symmetric_difference_update:")
print(x)
print()

# union
print("==================================================")
print("union:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Before union:")
print(x)
print()
z = x.union(y)
print("After union:")
print(z)
print()

# update
print("==================================================")
print("update:")
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Beforeupdate:")
print(x)
print()
x.update(y)
print("After update:")
print(x)
