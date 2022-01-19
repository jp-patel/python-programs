import random

my_char=[]
my_num=[]
my_symbols=['#','_','@']
my_password=[]
password=''

for i in range (48,58):
    my_num.append(chr(i))

for i in range (65,91):
    my_char.append(chr(i))

for i in range (97,123):
    my_char.append(chr(i))


for i in range(6):
    my_password = my_password + (random.choices(my_char))

my_password = my_password + (random.choices(my_num))
my_password = my_password + (random.choices(my_symbols))

random.shuffle(my_password)

for x in my_password:
    password=password+x

print()
print("password is:",password)
print()
