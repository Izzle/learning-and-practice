# Exercise 16 & 17 
# Writing and Appending to Files
# Yes I know my naming convention is not standard.. I wrote it at 2AM 

text = 'Sample Text to Save\nNew line!'

# Using the open() function to Write the file. WARNING - Write will overwrite any old file.
# First parameter is the name of the file to open. If none exists, it'll create it.
# Second parameter 'w' tells it to Write to the specifed file.
saveFile = open('exampleFile.txt', 'w') # Notifys Python our intentions

saveFile.write(text) # Tells Python to write text
saveFile.close() # IMPORTANT to close or the file will hang open for a long time

# Appendding to a file

appendMe = 'New bit of information'

appendFile = open('exampleFile.txt', 'a') # open() with 'a' is for APPEND
appendFile.write('\n')     # Adds a new line before we append more data
appendFile.write(appendMe) # Tells Python WHAT to append
appendFile.close()         # closes the file