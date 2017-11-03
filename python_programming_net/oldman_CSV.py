
import csv
import re


def fix(re_search, csv_col):
    diction = {}
    for x in range(len(csv_col)):
        result = re.search(re_search, csv_col[x])
        if result:
            diction[x] = result.group(0)
        else:
            diction[x] = 'NONE'

    return diction


with open('org_address_book.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # The lists that will hold our CSV columns
    first_names = []
    last_names = []
    nick_names = []
    emails = []
    block_notes = []

    with open('new_address_book.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

# Used to sort through terminal easily
        print('*' * 40)
    # Remove "" then iterate into the correct list

        for row in readCSV:
            # Rows are where each category of relevant data is saved
            FN = row[0]
            LN = row[2]
            NN = row[3]
            EM = row[27]
            note = row[30]
            # Creates lists of each column
            first_names.append(FN)
            last_names.append(LN)
            nick_names.append(NN)
            emails.append(EM)
            block_notes.append(note)


        # Getting the information from Notes (emails, first, last)
        dataDict = {}
        dataDict['Email'] = fix(r'Email\sAddress\:\s[A-Za-z0-9.@_]+', block_notes)
        dataDict['First Name'] = fix(r'First\sName\:\s[A-Za-z0-9.@_]+', block_notes)
        # Name is currently not working
        # dataDict['Name'] = fix(r'\SName\:\s[A-Za-z0-9.@_\s-]+', block_notes)
        # print(dataDict['First Name'])
        #for line in dataDict['Email']:
         #   csv_writer.writerow(dataDict['Email'][line])
        for line in dataDict['Email']:
            # Cutting out the substring that says 'Email Address: '
            if dataDict['Email'][line][0:15] == 'Email Address: ':
                line_len = len(dataDict['Email'][line])
                dataDict['Email'][line] = dataDict['Email'][line][15:line_len]
                # print(dataDict['Email'][line][15:line_len])
            else:
                print('NO EMAIL ON FILE')
        #print(dataDict['Email'][1][0:15])
        #print(dataDict['Email'][5][34])
        #print(len(dataDict['Email'][5]))




# [^First\s]N\w{3}\:\s[A-Za-z0-9.@_\s-]+
# First\sName\:\s[A-Za-z0-9.@_]+
# Email\sAddress\:\s[A-Za-z0-9.@_]+

