# Exercise 5 and 6
# While and For loops in python 3

# Basic while loop

condition = 1

while condition < 10:
    print(condition)
    condition += 1

# Basic For loop

exampleList = [1, 5, 6, 5, 8, 8, 6, 7, 5, 309, 23, 1]

for eachNumber in exampleList:  # Iterates each item in the list and puts it into the variable 'eachNumber'
    print(eachNumber)
    print('continue program')

# range() is a built in Python function
# range() will go from the starting number up to the last number
# range() will use up your RAM for every slot. If you need to do range(1,10000000000000000000000)
# do not use range(), use xrange() instead
for x in range(1, 11):
    print(x)
