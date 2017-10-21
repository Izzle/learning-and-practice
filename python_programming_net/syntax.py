# A personal catalog of Python syntax


import sys
import socket as s
from statistics import mean, median, mode, stdev, variance as v

x = '\"I\'m a variable\"'
num = 5.273
print('You can print a string using single or double quotes.')
print("Just make sure you know what happens if you have to mix them "
      "in the same string.")
print('You can print variables in different ways such as', x,
      '\nAnd this ' + x,
      '\nNotice that using \" + x\" requires that you enter spaces.'
      '\nBut using \", x\" notation does not!\n')
print('Now onto numbers in Python. Python uses ints, floats, and bools.'
      '\nYou can use conversion to turn this float', num,
      '\nInto an integer like so: ' + str(int(num)) +
      '\nTo do that you have to use int(num) to covert it to an int'
      '\nand then convert that into a string with str(int(num))')
#Multi-line Print
print('''
So this is a simple
multi-line
print, pretty cool, huh?

==============
|            |
|            |
|    BOX     |
|            |
|            |
==============


''')

# =======================================
#          Arithmetic Operators
# =======================================

1 + 1
# Subtraction
5 - 2
# Multiplication
4 * 4
# Division. Gives you 2.5, a Float
5 / 2

# FLoor DivisionThe division of operands where the result is the
# quotient in which the digits after the decimal point are removed.
# But if one of the operands is negative, the result is floored,
# i.e., rounded away from zero (towards negative infinity) −
13 // 4
# Modulus
7 % 2
# Exponent, 'Four to the power of Four'. Gives you 256
4 ** 4

# =======================================
#   Comparison & Assignment Operators
# =======================================
a = 4
b = 2

# Equal
a == b
# Not equal
a != b
# a Greater Than b ?
a > b
# a Less than b ?
a < b
# Greater than or equal to
a >= b
# Lesser than or equal to
a <= b

a += b
a -= b
a *= b
a /= b
a %= b
a **= b
a //= b


# =======================================
#    Membership & Identity Operators
# =======================================

# Python’s membership operators test for membership in a sequence,
# such as strings, lists, or tuples.

memList = [1, 2, 3, 4, 5]

# x in y, here in results in a 1 if x is a member of sequence y.
truth = 2 in memList
print("the truth is", truth)

# x not in y, here not in results in a 1 if x is not a member of sequence y.
diet_truth = 'weirdo' in memList
print("diet truth is:", diet_truth)


# Identity operators compare the MEMORY LOCATIONS of two objects.

# Evaluates to true if the variables on either side of the operator point to
# the same OBJECT and false otherwise. Example:
# x is y, here is results in 1 if id(x) equals id(y).
first_dict = {'Fish': 13, 'Cat': 4, 'Dog': 7, 'Mice': 2302}
different_dict = first_dict

if different_dict is first_dict:
    print('\"different_dict is a copycat!\"\n  - first_dict')
else:
    print('\"pfft.. first_dict is so unoriginal\"\n  - different_dict')


# Evalutes to false if the point to the same object, true otherwise. Ex:
# x is not y, here is not results in 1 if id(x) is not equal to id(y).
j = 777
k = 777
print('Both \'j\' and \'k\' equal', j, 'but they were each set to equal', k,
      'separately and we never set j=k or k=j.')
print('The question then becomes: Since they are both the same type:', type(k),
      '\nAnd have the same value. Does Python store them in the same memory'
      ' location?', j is k)
print('But a guy I know said they are saved in different spots:', j is not k)


# =======================================
#      Boolean & Bitwise Operators
# =======================================

# Boolean logic uses English:
# and       or        not
a and b
j or k
not x





# =======================================
#            Tuples & Lists
# =======================================

# Tuple notation. Tuples are immutable (they cannot be changed).
# Tuples are generated faster and are iterated faster than Lists.
ex_tuple = 1, 2, 3, 4, 5
ex_tuple2 = (1, 2, 3, 4, 5)
# List. Lists can be changed (they're mutable).
ex_list = [1, 2, 3, 4, 5, 14, 12, 9, 55, 8, 6, 13, 7]

# Printing tuples and lists. Uses the same notation!
# Prints the second item in the tuple (ie 2)
print(ex_tuple[1])
# Prints the first and 4th item in the list
print(ex_list[0], ex_list[3])
# Prints the Second THROUGH Sixth element 
# format is list[x:y] it starts at x and
# prints up to but not including the y-th element
print(ex_list[1:7])