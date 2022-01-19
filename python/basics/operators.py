# operators

# arithmetic operators
print()
print("Arithmetic Operators:")

first=10
second=4
print("first =",first)
print("second =",second)
print()

answer=first+second
print("first + second =",answer)

answer=first-second
print("first - second =",answer)

answer=first*second
print("first * second =",answer)

answer=first/second
print("first / second =",answer)

answer=first%second
print("first % second =",answer)

answer=first**second
print("first ** second =",answer)

answer=first//second
print("first // second =",answer)
print()
print("==================================================")

# assignment operators
print()
print("Assignment Operators:")

number=10
operand=2
hold=number
print("number =",number)
print("operand =",operand)
print()

number+=operand
print("number += operand = ",number)
number=hold

number-=operand
print("number -= operand = ",number)
number=hold

number*=operand
print("number *= operand = ",number)
number=hold

number/=operand
print("number /= operand = ",number)
number=hold

number%=operand
print("number %= operand = ",number)
number=hold

number//=operand
print("number //= operand = ",number)
number=hold

number**=operand
print("number **= operand = ",number)
number=hold

number&=operand
print("number &= operand = ",number)
number=hold

number|=operand
print("number |= operand = ",number)
number=hold

number^=operand
print("number ^= operand = ",number)
number=hold

number>>=operand
print("number >>= operand = ",number)
number=hold

number<<=operand
print("number <<= operand = ",number)
print()
print("==================================================")

# comparision operators
print()
print("Comparision Operators:")

value_1=10
value_2=20
value_3=10
print("value_1 =",value_1)
print("value_2 =",value_2)
print("value_3 =",value_3)
print()

print("value_1 == value_2  => ",value_1==value_2)
print("value_1 != value_2  => ",value_1!=value_2)
print("value_1 == value_3  => ",value_1==value_3)
print("value_1 != value_3  => ",value_1!=value_3)
print("value_1 > value_2  => ",value_1>value_2)
print("value_1 < value_2  => ",value_1<value_2)
print("value_1 >= value_2  => ",value_1>=value_2)
print("value_1 <= value_2  => ",value_1<=value_2)

print()
print("==================================================")

# logical operators
print()
print("Logical Operators:")

a=0
b=1
print("a =",a)
print("b =",b)

print()
print("a and b  => ",a and b)
print("a or b  => ",a or b)
print("not(a and b)  => ",not(a and b))

print()
print("==================================================")

# Identity Operators
print()
print("Identity Operators:")

x=["value_1","value_2"]
y=["value_1","value_2"]
z=x
print("x =",x)
print("y =",y)
print("z =",z)

print()
print("x is y  => ",x is y)
print("x is z  => ",x is z)
print("x is not y  => ",x is not y)
print("x is not z  => ",x is not z)

print()
print("==================================================")

# bitwise operators
print()
print("Bitwise Operators:")

value_1=0
value_2=1
print("value_1 =",value_1)
print("value_2 =",value_2)

print()
print("value_1 & value_2 =",value_1&value_2)
print("value_1 | value_2 =",value_1|value_2)
print("value_1 ^ value_2 =",value_1^value_2)
print("value_1 << value_2 =",value_1<<value_2)
print("value_1 >> value_2 =",value_1>>value_2)
print("~value_1 =",~value_1)

print()
print("==================================================")
