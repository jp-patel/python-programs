# capitalize
print("==================================================")
print("capitalize:")
print()

txt = "hello, and welcome to my world."
print("Before capitalize:")
print(txt)
print()
x = txt.capitalize()
print("After capitalize:")
print (x)
print()

# casefold
print("==================================================")
print("casefold:")
print()

print("Before casefold:")
print(txt)
print()
x = txt.casefold()
print("After casefold:")
print(x)
print()

# center
print("==================================================")
print("center:")
print()

txt = "grapes"
print("Before center:")
print(txt)
print()
x = txt.center(20)
print("After center:")
print(x)
print()

# count
print("==================================================")
print("count:")
print()

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
print()

# encode
print("==================================================")
print("encode:")
print()

txt = "My name is Ståle"
x = txt.encode()
print(x)
print()

# endswith
print("==================================================")
print("endswith:")
print()

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
print()

# expandtabs
print("==================================================")
print("expandtabs:")
print()

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print()

# find
print("==================================================")
print("find:")
print()

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
print()

# format
print("==================================================")
print("format:")
print()

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
print()

# index
print("==================================================")
print("index:")
print()

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
print()

# isalnum
print("==================================================")
print("isalnum:")
print()

txt = "Company12"
x = txt.isalnum()
print(x)
print()

# isalpha
print("==================================================")
print("isalpha:")
print()

txt = "CompanyX"
x = txt.isalpha()
print(x)
print()

# isdecimal
print("==================================================")
print("isdecimal:")
print()

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())
print()

# isdigit
print("==================================================")
print("isdigit:")
print()

txt = "50800"
x = txt.isdigit()
print(x)
print()

# isidentifier
print("==================================================")
print("isidentifier:")
print()

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print()

# islower
print("==================================================")
print("islower:")
print()

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())
print()

# isnumeric
print("==================================================")
print("isnumeric:")
print()

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
print()

# isprintable
print("==================================================")
print("isprintable:")
print()

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
print()

# isspace
print("==================================================")
print("isspace:")
print()

txt = "   "
x = txt.isspace()
print(x)
print()

# istitle
print("==================================================")
print("istitle:")
print()

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
print()

# isupper
print("==================================================")
print("isupper:")
print()

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())
print()

# join
print("==================================================")
print("join:")
print()

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
print()

# ljust
print("==================================================")
print("ljust:")
print()

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
print()

# lower
print("==================================================")
print("lower:")
print()

txt = "Hello my FRIENDS"
print("Before lower:")
print(txt)
print()
x = txt.lower()
print("After lower:")
print(x)
print()

# lstrip
print("==================================================")
print("lstrip:")
print()

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
print()

# maketrans
print("==================================================")
print("maketrans:")
print()

txt = "Hi Sam!"
x = "mSa"
y = "eJo"

mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
print()

# partition
print("==================================================")
print("partition:")
print()

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print()

# replace
print("==================================================")
print("replace:")
print()

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
print()

# rfind
print("==================================================")
print("rfind:")
print()

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
print()

# rindex
print("==================================================")
print("rindex:")
print()

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
print()

# rjust
print("==================================================")
print("rjust:")
print()

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
print()

# rpartition
print("==================================================")
print("rpartition:")
print()

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
print()

# rsplit
print("==================================================")
print("rsplit:")
print()

txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)
print()

# rstrip
print("==================================================")
print("rstrip:")
print()

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
print()

# split
print("==================================================")
print("split:")
print()

txt = "welcome to the jungle"
x = txt.split()
print(x)
print()

# splitlines
print("==================================================")
print("splitlines:")
print()

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
print()

# startswith
print("==================================================")
print("startswith:")
print()

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
print()

# strip
print("==================================================")
print("strip:")
print()

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
print()

# swapcase
print("==================================================")
print("swapcase:")
print()

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
print()

# title
print("==================================================")
print("title:")
print()

txt = "Welcome to my world"
x = txt.title()
print(x)
print()

# translate
print("==================================================")
print("translate:")
print()

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
print()

# upper
print("==================================================")
print("upper:")
print()

txt = "Hello my friends"
print("Before upper:")
print(txt)
print()
x = txt.upper()
print("After lower:")
print(x)
print()

# zfill
print("==================================================")
print("zfill:")
print()

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
print()