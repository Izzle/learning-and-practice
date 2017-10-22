gifts = ('Partridge in a Pear Tree', 'Turtle Doves', 'French Hens',
         'Calling Birds', 'Golden Rings', 'Geese-a-Laying',
         'Swans-a-Swimming', 'Maids-a-Milking', 'Ladies Dancing',
         'Lords-a-Leaping', 'Pipers Piping', 'Drummers Drumming')

for i in range(len(gifts)):
    print('On the', i + 1, '-th day of Christmas my true love gave to me')
    for j in range(i, -1, -1):
        a = j + 1
        if i == 0 and a == 1:
            print('a', gifts[j])
        elif a == 1:
            print('and a', gifts[j])
        else:
            print(j + 1, gifts[j])
        print('.')
