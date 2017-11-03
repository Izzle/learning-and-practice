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


with open('../Work/org_address_book.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    # The lists that will hold our CSV columns
    first_names = []
    last_names = []
    nick_names = []
    emails = []
    block_notes = []
    # print(csv_reader.fieldnames)

    # for line in csv_reader:
    #     #print(line['Notes'])
    #     print(line)

    with open('../Work/newer_address_book.csv', 'w') as new_file:
        fieldnames = csv_reader.fieldnames

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        
        # Goes over each list in the CSV
        for line in csv_reader:
            # Goes over each field in the list
            for field in fieldnames:
                print(line[field])


    #print(dir(csv_reader))
    #for line in csv_reader:
        #print(line[20:33])
'''
    for row in csv_reader:
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
    
    print(block_notes)
'''