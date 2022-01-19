import random

otp=''

for i in range(6):
    otp=otp + str(random.randrange(0, 9))

print()
print("otp is:",otp)
print()
