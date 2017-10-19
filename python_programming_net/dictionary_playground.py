# Exercise 31 Dictionaries
# Dictionaries are Python specific key:value pairs
# They are unordered. Technically dictionaries can hold anything:
# strings, bools, functions, lists, or even other dictionaries!
#
# Syntax example:  exDict = {'Joe': 12, 'Mary': 13}

exDict = {'Jack': 32, 'Beth': 17, 'Bob': 22, 'Alice': 19, 'Kevin': 18}

# NOTE: Doesnt always keep order
print(exDict)
# Prints out the age of Jack
print('Jack\'s age:', exDict['Jack'])

# Adding new key:value pair to dictionary
exDict['Tim'] = 14

print(exDict)

# Overwrites the value of Tim (may replace it entirely)
# IMPORTANT: Keys must be UNIQUE in dictionaries!
exDict['Tim'] = 15

print(exDict)

# Removes Tim from the dictionary. Removes the KEY and VALUE.
del exDict['Tim']

# This dictionary holds 2 Values for each Key
# Syntax: exDict = {'Bob': [21, 'Ginger']}
# In second_dict the Keys are the names and the values are Age and Hair color
second_dict = {'Billy': [15, 'blonde'], 'Sally': [18, 'brown'],
               'Joe': [35, 'brown'], 'Rebecca': [28, 'black'],
               'Kevin': [20, 'red'], 'Tony': [41, 'blonde']
               }

print(second_dict)
print('Joe\'s age and hair color:', second_dict['Joe'])
# Ex. how to reference a particular value when the Key has many Values
# The first [] is the KEY and the second [] is the INDEX of the Value
# Syntax: exDict['Tony'][0]
print('Kevin\'s hair is:', second_dict['Kevin'][1])
'''
   PRACTICE
Ask the user for input, validate it, then ask them more information and add
it to the dictionary. Then print out specific information using notation:
dict[key][valueIndex]
'''
try:
    name = input('What is your name? ')
    if name in second_dict:
        # TODO use formatting to include the name in the print statement
        print('Someone already has that name.')
    else:
        pass
# TODO more specific exception handling
except Exception as e:
    print('[-] ERROR: ', e)
# Use the multi-line print method you learned recently
pass
