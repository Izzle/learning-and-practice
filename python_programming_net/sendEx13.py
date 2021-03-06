# Exercise 24, 25, & 26
# Custom modules and Lists


# imports example_mod.py locally. For this to work in IDLE,
# the module must be saved in 'lib' or 'site-packages'.
import example_mod

example_mod.ex('I hope this works.')
print('...\n' * 3)
# Although our text editor doesn't register it correctly in color
# Most terminals understand ANSI escape codes.
# "\033[F" goes to the previous line, it is the opposite of "\n"
print('\033[FIt worked! Ok, now onto lists and tuples!\n')

x = [2, 3.01, 4, 6, 3, 2.9, 5, 1.19, 5, 6, 7]
y = ['Jenny', 'Joey', 'Kelly', 'Kenlson',
     'Becky', 'Bradford', 'Daisy', 'Dodsworth']
print('Our list', x)

# Appends a value to the end of the list
x.append(17)
print('Appended:', x)

# Inserting into the list. Using list.insert(x, y)
# x is the index (WHERE) and y is the object (WHAT)
x.insert(0, 'bitch I\'m first now!')
print('Inserting:', x)

# You can remove explictly or implictly
x.remove('bitch I\'m first now!')
print('CENSORING BAD LANGUAGE:', x)

x.remove(x[5])
print('Removing 6th value:', x)

# If you don't iterate put the WHOLE list in one value
refill = [9, 7, 89, 'GG no re', 42, 20, 17]
for thing in refill:
    x.append(thing)

print('REFILLING LIST.. BEEP..'
      '\nList refilled:', x)

# You can also perform "slicing" on a range of values using
# list[x, y]. REMEMBER it goes UP TIL BUT NOT INCLUDING 'y'
print('Programmers Birthday:', x[11:14])

# Accessing the last element on a list with -1
print('Last element:', x[-1],
      '\nSecond to last element:', x[-2])

# Find the index value. This will find the first element with that value
print('The index of the the first \"7\" is:', x.index(7),
      '\nNumber of 7\'s in this list:', x.count(7))

# Sorting lists
print('\nOkay thats enough!'
      '\nLook at this mess:', x,
      '\nTime to sort this mess out.'
      '\nFirst by removing any strings from the list...')

# list.sort() can't sort lists that contain both ints and strings.
# Iterates over each element and checks if it is a string. If it is,
# appends the string to another list and removes it from the orginal list.
for word in x:
    if type(word) == str:
        y.append(word)
        x.remove(word)
        print('Removing \'' + word + '\' from list.')

# With the strings removed, we can now use list.sort()
x.sort()
print('Sorting the list out:', x)
# NOTE: You print using + with a list, in this situation you must use commas.
print('A new list of strings:', y,
      '\nNotice our little friend from before? Time to sort this out.')
y.sort()
print('SORTED BITCH:', y)
