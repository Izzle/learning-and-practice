# Misc practice

x = 17
y = 32
z = 12

while x < y:
    x += 1
    print(x / 2)

if x < y > z:  # Bad example
    print('y is greater than x and z')
elif x > y:
    print('x is greater than y')
elif y < z:
    print('z is greater than y')
else:
    print('this shouldnt run unless I don\'t understand logic')
    print('which is a possibility')
