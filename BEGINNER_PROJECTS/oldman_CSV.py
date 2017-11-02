
import csv
import re

with open('new_address_book.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    # The lists that will hold our CSV columns
    first_names = []
    last_names = []
    nick_names = []
    emails = []
    block_notes = []


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


    # PRINT BELOW HERE OR YOULL GET REPEATS

    newDict = {}
    for x in range(len(block_notes)):
        notes_results = re.search(r'Email\sAddress\:\s[A-Za-z0-9.@_]+', block_notes[x])
        # notes_results is a CLASS object returned by re.search
        if notes_results:
            newDict[x] = notes_results.group(0)
        else:
            newDict[x] = 'NONE'
# newDict has the INDEX as its KEYS and the first value are EMAILS from NOTES
    print(newDict)



# Email\sAddress\:\s[A-Za-z0-9.@_]+

