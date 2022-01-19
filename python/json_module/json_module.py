# how to use json
import json

# how to convert from json to python
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print()

# how to convert from python to json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print()

# converting all possible python objects into json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print()

# converting a python object containing all the legal data types
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print("==================================================")
print("result withuout formatting:")
print(json.dumps(x))
print()

print("result with indent:")
print(json.dumps(x, indent=4))
print()

print("result with indent and separators:")
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print()

print("result with indent and sorting:")
print(json.dumps(x, indent=4, sort_keys=True))
print()
