# Exercise 36
# Regular Expressions / Regex with re

import re


'''
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character, except for a newline
\b the whitespace around words
\. a period

Modifiers:
{1,4} we're expecting 1-4 of something (amount)
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ match the beginning of a string
| either or (an OR operator)
[] range or "variance" [1-5a-qA-Z]
[x] expecting "x" amount
() pattern to search for 

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

DON'T FORGET!:
. + * ? [ ] $ ^ ( ) { } | \
If you really want to use these you have to escape them.
'''

example_string = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 67, and his grandfather, Oscar, is 102.
'''

# For Python to know you're using a REGEX you must type: r''
# Searching ages, so all numbers 1-3 in length
ages = re.findall(r'\d{1,3}', example_string)
names = re.findall(r'[A-Z][a-z]*', example_string)

print(ages)
print(names)
