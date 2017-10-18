# Exercise 16, 17, & 18
# Writing, Appending, and Reading Files
# Yes I know my naming convention is not standard.. I wrote it at 2AM

text = 'Sample Text to Save\nNew line!'

# Using the open() function to Write the file. WARNING - Write will overwrite any old file.
# First parameter is the name of the file to open. If none exists, it'll create it.
# Second parameter 'w' tells it to Write to the specifed file.
saveFile = open('exampleFile.txt', 'w')  # Notifys Python our intentions

saveFile.write(text)  # Tells Python to write text
saveFile.close()  # IMPORTANT to close or the file will hang open for a long time

# Appendding to a file

appendMe = 'New bit of information'

appendFile = open('exampleFile.txt', 'a')  # open() with 'a' is for APPEND
appendFile.write('\n')     # Adds a new line before we append more data
appendFile.write(appendMe)  # Tells Python WHAT to append
appendFile.close()         # closes the file

# Testing how 2 appends work in the same scope
appendMeToo = 'Writing test code at 4am'

appendFile = open('exampleFile.txt', 'a')
appendFile.write('\n')
appendFile.write(appendMeToo)
appendFile.close()

# How to READ a file. This allows me to read the content
# from the terminal instead of opening a text editor.
# NOTE: You do NOT have to close a file when you read it!!!
readMe = open('exampleFile.txt', 'r').read()
print(readMe)

# Reads line by line. Saves into a python list
readMe2 = open('exampleFile.txt', 'r').readlines()
print(readMe2)
