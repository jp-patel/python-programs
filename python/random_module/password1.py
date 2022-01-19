import random

my_list=[]
my_symbols=['#','_','@']

for i in range (48,58):
    my_list.append(chr(i))

for i in range (65,91):
    my_list.append(chr(i))

for i in range (97,123):
    my_list.append(chr(i))

my_list.extend(my_symbols)

random.shuffle(my_list)

password=''
for i in range(8):
    password = password + str(random.choice(my_list))
print("password is:",password)
print()
