# append
print("==================================================")
print("Append:")
print()

fruits = ['apple', 'banana', 'cherry']
print("Before Append:")
print(fruits)
print()
print("After Append:")
fruits.append("orange")
print(fruits)
print()

# clear
print("==================================================")
print("Clear:")
print()

print("Before Clear:")
print(fruits)
print()
fruits.clear()
print("After Clear:")
print(fruits)
print()

# copy
print("==================================================")
print("Copy:")
print()

fruits = ['apple', 'banana', 'cherry', 'orange']
print("Before Copy:")
print(fruits)
print()
print("After Copy:")
x = fruits.copy()
print(x)
print()

# count
print("==================================================")
print("Count:")
print()

x = fruits.count("cherry")
print(x)
print()

# extend
print("==================================================")
print("Extend:")
print()

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
print("Before Extend:")
print(fruits)
print()
fruits.extend(cars)
print("After Extend:")
print(fruits)
print()

# index
print("==================================================")
print("Index:")
print()

x = fruits.index("cherry")
print(x)
print()

# insert
print("==================================================")
print("Insert:")
print()

fruits = ['apple', 'banana', 'cherry']
print("Before Insert:")
print(fruits)
print()
fruits.insert(1, "orange")
print("After Insert:")
print(fruits)
print()

# pop
print("==================================================")
print("Pop:")
print()

print("Before Pop:")
print(fruits)
print()
fruits.pop(1)
print("After Pop:")
print(fruits)
print()

# remove
print("==================================================")
print("Remove:")
print()

fruits = ['apple', 'banana', 'cherry']
print("Before Remove:")
print(fruits)
print()
fruits.remove("banana")
print("After Remove:")
print(fruits)
print()

# reverse
print("==================================================")
print("Reverse:")
print()

fruits = ['apple', 'banana', 'cherry']
print("Before Reverse:")
print(fruits)
print()
fruits.reverse()
print("After Reverse:")
print(fruits)
print()

# sort
print("==================================================")
print("Sort:")
print()

cars = ['Ford', 'BMW', 'Volvo']
print("Before Sort:")
print(cars)
print()
cars.sort()
print("After Sort:")
print(cars)
print()
