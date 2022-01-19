# list
# list is a collection which is:
# ordered
# changable
# allow duplicate

# how to initialize a list
my_list = ["firstname","secondname","lastname"]

# how to print list items
print(my_list)
print()

# how to print length of list
print(len(my_list))
print()

# how to see type of list
print(type(my_list))
print()

# how to make list using list constructor

my_list=list(("firstname","secondname","lastname","email","DOB","address","pincode","state","country"))
print(my_list)
print()

# how to access list items
print(my_list[1])
print()

# how to use negative indexing
print(my_list[-1])
print()

# how to use range of indexing
print(my_list[2:5])
print(my_list[2:])
print(my_list[:5])
print()

# how to use range of negative indexing
print(my_list[-5:-1])
print(my_list[-5:])
print(my_list[:-5])
print()

# how to check if an item exists in a list or not
print("DOB" in my_list)
print("mobile_no" in my_list)
print()

# how to change item value in list
my_list[2]="surname"
print(my_list[2])
print()

# how to change a range of item values
my_list[0:3]=["fullname"]
print(my_list)
print()

# how to loop through list
for x in my_list:
    print(x)
print()

# how to loop through index numbers in list
for i in range(len(my_list)):
    print(my_list[i])
print()
