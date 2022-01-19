# clear
print("==================================================")
print("clear:")
print()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before clear:")
print(car)
print()
car.clear()
print("After clear:")
print(car)
print()

# copy
print("==================================================")
print("copy:")
print()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before copy:")
print(car)
print()
x = car.copy()
print("After copy:")
print(x)
print()

# fromkeys
print("==================================================")
print("fromkeys:")
print()

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
print()

# get
print("==================================================")
print("get:")
print()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)
print()

# items
print("==================================================")
print("items:")
print()

x = car.items()
print(x)
print()

# keys
print("==================================================")
print("keys:")
print()

x = car.keys()
print(x)
print()

# pop
print("==================================================")
print("pop:")
print()

print("Before pop:")
print(car)
print()
car.pop("model")
print("After pop:")
print(car)
print()

# popitem
print("==================================================")
print("popitems:")
print()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before popitem:")
print(car)
print()
car.popitem()
print("After popitem:")
print(car)
print()

# setdefault
print("==================================================")
print("setdefault:")
print()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
print()

# update
print("==================================================")
print("update:")
print()

print("Before update:")
print(car)
print()
car.update({"color": "White"})
print("After update:")
print(car)
print()

# values
print("==================================================")
print("values:")
print()

x = car.values()
print(x)
