# Exercise 28
# Reading from CSV spreadsheet in Python 3
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

    whatColor = input('What color do you wish to know the date of? ')
    whatColor = whatColor.lower().strip()
    coldex = colors.index(whatColor)

    theDate = dates[coldex]

    print('The date of', whatColor.capitalize(), 'is', theDate)
