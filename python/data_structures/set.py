# set
# set is a collection which is:
# unordered
# unchangable (Set items are unchangeable, but you can remove items and add new items.)
# do not allow duplicate

# how to initialize a set
my_set = {"firstname","secondname","lastname"}

# how to print set items
print(my_set)
print()

# how to print length of set
print(len(my_set))
print()

# how to see type of set
print(type(my_set))
print()

# how to make set using set constructor

my_set=set(("firstname","secondname","lastname","email","DOB","address","pincode","state","country"))
print(my_set)
print()

# how to check if an item exists in a set or not
print("DOB" in my_set)
print("mobile_no" in my_set)
print()

# how to loop through set
for x in my_set:
    print(x)
print()
