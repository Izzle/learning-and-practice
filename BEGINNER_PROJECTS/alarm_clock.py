# Ron Martin
# 10/30/2017
#
# Project idea is from the subreddit /r/beginnerprojects


import datetime
import os
import webbrowser

# Checks for 'youtube.txt' and creates the file if it doesn't exist
if os.path.isfile('youtube.txt') is False:
    print('ERROR: The file \"youtube.txt\" does not exist in your '
          'current directory.\nCreating file...')
    links = '''https://www.youtube.com/watch?v=ueRzA9GUj9c
             https://www.youtube.com/watch?v=siwpn14IE7E
             https://www.youtube.com/watch?v=ZTidn2dBYbY
             https://www.youtube.com/watch?v=btPJPFnesV4
             https://www.youtube.com/watch?v=MN3x-kAbgFU'''
    savedFile = open('youtube.txt', 'w')
    savedFile.write(links)
    savedFile.close()
    # read = open('youtube.txt', 'r').read()
    # print(read)

# Asking for time that alarm should go off
time_format = '%H:%M'
while True:

    try:
        wake_up = input('What time do you want the alarm to go off? ')
        # Creates a datetime object from the string entered and in the format
        # specified it throws a ValueError if the information is not valid time
        valid_time = datetime.datetime.strptime(wake_up, time_format)
    except Exception as e:
        print(str(e))
        print('Sorry, I didn\'t understand that.')
        print('Please enter Hour and Minutes in the following format:  6:30')
    else:
        break

# If user didnt enter military time we add 12 hours
if valid_time.hour > 12:
    # Military time
    print('Military time, eh? Thank you for your service.')
else:
    try:
        ans = input('AM or PM? ')
        if ans.lower() == 'pm':
            print('Late start, eh?')
            valid_time += datetime.timedelta(hours=12)
        elif ans.lower() == 'am':
            print('Early bird gets the worm!')
        else:
            print('Incorrect input: ABORT! ABORT!')
    except Exception as e:
        print(str(e))
        print('Sorry, I didn\'t understand that.')

# Opens the text file
with open('youtube.txt') as l:
    # Stores the urls into the 'videos' variable
    videos = l.readlines()


# IF TIME != ALARM -> PRINT TIME
# IF TIME == ALARM -> OPEN RANDOM VIDEO
# WORKS - using military time!
print('Ok, so', str(valid_time))

# Now we just need to open the browser to a random youtube page
# when it is time for the alarm to go off!
if datetime.datetime.now() == valid_time:
    # open a random youtube page
    pass
