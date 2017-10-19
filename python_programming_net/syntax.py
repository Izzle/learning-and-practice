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
1 + 1
# Subtraction
5 - 2
# Multiplication
4 * 4
# Division. Gives you 2.5, a Float
5 / 2
# Exponent, 'Four to the power of Four'. Gives you 256
4 ** 4

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