# Project idea from the subreddit /r/dailyprogrammer
#
#
# Author:  Ron Martin
# Created: 11/17/2017

gifts = ('Partridge in a Pear Tree', 'Turtle Doves', 'French Hens',
         'Calling Birds', 'Golden Rings', 'Geese-a-Laying',
         'Swans-a-Swimming', 'Maids-a-Milking', 'Ladies Dancing',
         'Lords-a-Leaping', 'Pipers Piping', 'Drummers Drumming')
day_dict = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th',
            5: 'th', 6: 'th', 7: 'th', 8: 'th',
            9: 'th', 10: 'th', 11: 'th', 12: 'th'}

for i in range(len(gifts)):
    x = day_dict[i + 1]
    print('On the', i + 1, x, ' day of Christmas my true love gave to me')
    for j in range(i, -1, -1):
        a = j + 1
        if i == 0 and a == 1:
            print('a', gifts[j])
        elif a == 1:
            print('and a', gifts[j])
        else:
            print(j + 1, gifts[j])
