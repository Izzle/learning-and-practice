# Exercise 33 & 34
# The OS and Sys modules in Python 3
#

import os
import sys
import time

# =======================================
#             OS module
# =======================================

# getcwd() gets Current Working Directory
curr_dir = os.getcwd()
# example output: Users/Owner/Documents/Code/python_hax
print(curr_dir)

# If no path is specified, creates directory in CWD (aka PWD)
os.mkdir('new_directory')

# Delays executing of code for x seconds. Gives us time to
# watch the process execute in File Explorer / Finder
time.sleep(2)

# os.rename('oldName', 'newName')
os.rename('new_directory', 'newer_directory')
print('Say goodbye to our new directory-friend!')
time.sleep(2)

print('BOOM!')
os.rmdir('newer_directory')


# =======================================
#             Sys module
# =======================================

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

# sys.argv takes any arguments passed to it and puts them in a list.
# Important! We can pass arguments into a Python file using the commmandline
# - which means we can pass arguments from almost any other programming
# languages PHP to Python, Ruby to Python, Perl " ",  batch files etc.
#
# If you run this script in the terminal with 'python3.6 sendEx16.py'
# it would be: sys.argv == 'sendEx16.py' because we passed that argument to it
# Or we can run 'python3.6 sendEx16.py "LOOK AT THAT!"' and sys.argv would get
# passed both values. So then, sys.argv == ['sendEx16.py', 'LOOK AT THAT!']
# The default value of sys.argv is the current filepath

# This will print out the value in a list i.e. ['sendEx16.py']
print(sys.argv)

if len(sys.argv) > 1:
    # This will print out the value specifically, without list brackets or ''
    print(sys.argv[1])
    # We can manipulate the values that come in Python!
    print(float(sys.argv[1]) + 5)


# Example how to pass an argument from another language (PHP, JS) to Python
def main(arg):
    print(arg)
    if type(arg) == str or float:
        globx = int(arg)
    elif type(arg) == int:
        globx = arg
    else:
        globx = '[-] Error!'

    return globx


# Notice how we can pass sys.argv[1] asking for the index immediately
# This is possible because the list is created at terminal when run
main(sys.argv[1])


