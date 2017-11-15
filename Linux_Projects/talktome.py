#!/usr/bin/env python3

import sys

''' sys.argv is all the arguments passed, so if we run this script by
# typing 'python talktome.py' it will print 'talktome.py' since the
# filename is the only argument, but if you type:
# d'python talktome.py "hello world"' youll get 'talktome.py' and 'hello world'
# this can be used to talk between 2 different programming languages
'''
# print(sys.argv)

''' This will ignore the filename if any other arguments are passed
if len(sys.argv) > 1:
    print(sys.argv[1])
'''

# This is a more flexible way of doing the same thing
def main(arg):
    print(arg)


main(sys.argv[1])

