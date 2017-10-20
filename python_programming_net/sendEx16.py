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

