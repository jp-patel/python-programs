# how to use while loop
i = 1
while i < 6:
    print(i)
    i += 1
print()

# the break keyword
print("==================================================")
print("break:")
print()
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print()

# the continue keyword
print("==================================================")
print("continue:")
print()
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print()

# the else keyword
print("==================================================")
print("else statement:")
print()
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
print()
