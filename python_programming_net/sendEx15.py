# Exercise 32
# Built-in Functions in Python 3

#
# IMPORTANT: The help() function which you can run in IDLE
# or in the Terminal (just run python3.6 in terminal w/o running a file)
# is like MAN pages in linux. Very helpful documentation.
#

import math

# =======================================
#          Built-in Functions
# =======================================

# Absolute value: abs()
ex_num1 = -5
ex_num2 = 5

print('Value of num1:', ex_num1,
      '\nAbsolute value of num1:', abs(ex_num1),
      '\nValue of num2:', ex_num2)

if abs(ex_num1) == ex_num2:
    print('These are the same.')

# min(), max(), round()

exList = [2, 4, 5, 9, 1, 0, 13]
print(max(exList))
print(min(exList))

x = 5.621
print('x equals:', x,
      '\nx rounded:', round(x))


# math.ceil() & math.floor() are great if you
# ALWAYS want to round UP or ALWAYS round down
# (NOT a built-in as you must import math first)
y = 7.11
print('\'y\' is equal to:', y,
      '\n\'y\' rounded down:', math.floor(y),
      '\n\'y\' rounded up:', math.ceil(y))

# Conversions
# int(), float(), str()
int_me = '56'
print('int_me equals:', int_me,
      '\nint_me is a', type(int_me),
      '\nLet\'s change that. int_me is a', type(int(int_me)),
      '\nHuzzah! However, int_me believes types are only a social construct. '
      '\nIt identifies as \"type-fluid\". Today, int_me feels like a:',
      type(float(int_me)))

string_me = 77.0
print('\nstring_me is a', type(str(string_me)))
print('string_me is equal to:', str(string_me))

float_me = 1
line = '=' * 27
print()
print(line + '\nEverything is all mixed up!\n' + line, '\nint_me is a:',
      type(int_me), '\nstring_me is a:', type(string_me), '\nfloat_me is a:',
      type(float_me), '\n' + line, '\nTime to fix all this.\n' + line)

int_me = int(int_me)
string_me = str(string_me)
float_me = float(float_me)

print('int_me you are now a:', type(int_me), 'And equal:', int_me,
      '\nstring_me you are now a:', type(string_me), 'And equal:', string_me,
      '\nfloat_me you are now a:', type(float_me), 'And equal:', float_me)
