# Exercise 28, 29
# Reading from CSV spreadsheet in Python 3
# & Try and Except error handling
#
# CSV stands for Comma Separated Value and is commonly used
# in spreadsheets and in large data sets

import csv

# LEARN MORE ABOUT 'with'
with open('example.csv') as csvfile:
    # We imported csv which lets us use the .reader() method
    # A delimiter is anything that separates values. Anything can be a
    # delimiter (triple spaces, TABs, new lines, x), but commas are most common
    read_csv = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []
    # To print a CSV you must iterate like this. Also Python generally reads in
    # data as a string. To do math on this data you must convert to int/float
    for row in read_csv:
        color = row[3]
        date = row[0]

        colors.append(color)
        dates.append(date)

    print('Dates:', dates)
    print('Colors:', colors)

    # The Try Except is used here as a catch-all if we miss any errors
    # Otherwise errors should be excepted in part of the logic(if/else, etc)
    try:
        whatColor = input('What color do you wish to know the date of? ')
        # Basic code validation
        whatColor = whatColor.lower().strip()

        if whatColor in colors:
            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of', whatColor.capitalize(), 'is', theDate)
        else:
            print('Color not found, or it is not a color!')

    except Exception as e:
        print('Shits broke. Here\'s what happened: ', e)

    # This should never print, but is great at showing HOW you can
    # specify multiply errors in a single except
    except (NameError, ValueError, EnvironmentError,
            ZeroDivisionError, RuntimeError, OSError) as e:
        print('This should never print')
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

print('End of program.')
