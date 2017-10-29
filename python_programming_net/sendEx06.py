# Exercise 7, 8 and 9
# If statements in Python 3

x = 5
y = 8
z = 5
line = '.' * 16

if x > y:
    print('x is greater than y')

if z < y > x:
    print('y is greater than z and greater than x')

if z <= x:
    print('z is less than or equal to x')

if z == x:
    print('z is equal to x')

if z != y:
    print('z is not equal to y')

print(line)

# If Else in Python 3
if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')

print(line)

# If Elif Else
a = 6
b = 11
c = 23

if x > y:
    print('x is greater than y')  # False
elif x < z:
    print('x is less than z')  # True
elif 5 > 2:
    print('5 is greater than 2')  # True, but won't print
else:
    print('if and elif(s) never ran')
