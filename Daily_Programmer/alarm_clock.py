# Project idea is from the subreddit /r/beginnerprojects
#
#
# Ron Martin
# 10/30/2017


from datetime import datetime as dt
import time
import os
import webbrowser
import random

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

# Asking for time that alarm should go off
ALARM_TIME_FORMAT = '%H:%M'
CURR_TIME_FORMAT = '%I:%M'

while True:

    try:
        wake_up = input('What time do you want the alarm to go off? ')
        # Creates a datetime object from the string entered and in the format
        valid_time = dt.strptime(wake_up, ALARM_TIME_FORMAT)
    except Exception as e:
        print(str(e))
        print('Sorry, I didn\'t understand that.')
        print('Please enter Hour and Minutes in the following format:  6:30')
    else:
        break

# If the user entered military time then change CURR_TIME_FORMAT for comparison
if valid_time.hour > 12:
    # Military time
    print('Military time, eh? Thank you for your service.')
    CURR_TIME_FORMAT = ALARM_TIME_FORMAT
else:  # If user didn't use military time add 12hrs to valid_time " "
    try:
        ans = input('AM or PM? ')
        if ans.lower() == 'pm':
            valid_time += dt.timedelta(hours=12)
        elif ans.lower() == 'am':
            pass
        else:
            print('Incorrect input: ABORT! ABORT!')
    except Exception as e:
        print(str(e))
        print('Sorry, I didn\'t understand that.')


# Creates format strings from our datetime objects so we
# can use them correctly in comparisons and loops
current_time = dt.now().strftime(CURR_TIME_FORMAT)
alarm = valid_time.strftime(ALARM_TIME_FORMAT)

print('Alarm is set for:', alarm)

while current_time != alarm:
    # We used a 24 hour clock to do the logic, but when printing we
    # will display a 12 hour clock with AM/PM denoted
    print('The time is now:', dt.now().strftime('%I:%M:%p'))

    # Must declare time again inside the loop or the time will never refresh
    # and cause an infinite loop
    current_time = dt.now().strftime(CURR_TIME_FORMAT)

    # Prevents spam and checks time every second
    time.sleep(1)


# Opens the text file
with open('youtube.txt') as tube:
    # Stores the urls into the 'videos' variable
    videos = tube.readlines()

# When its time for the alarm, this section selects and plays a random video
# in the browser.
if current_time == alarm:
    print('Good morning beautiful!')
    # Selects a random youtube link
    selected_video = random.choice(videos)
    # Opens the browser to the random video and tries to open it in a new tab
    # otherwise it will open the browser if necessary.
    webbrowser.open_new_tab(selected_video)
