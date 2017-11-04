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


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


with open('../Work/org_address_book.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')

    # The lists that will hold our CSV columns
    first_names = []
    last_names = []
    emails = []
    block_notes = []
    # ISSUE IS WITH CSV READER BEING REFERENCED TWICE!
    # 111111111111111111111111
    for row in csv_reader:
        # Rows are where each category of relevant data is saved
        FN = row['First Name']
        EM = row['E-mail Address']
        note = row['Notes']
        # Creates lists of each column
        first_names.append(FN)
        emails.append(EM)
        block_notes.append(note)

    # Finding data in 'Notes' using our fix function - this will parse out
    # data and sort it using REGEX
    dataDict = {}
    dataDict['Email'] = fix(r"Email\sAddress\:\s[A-Za-z0-9.@_]+", block_notes)
    dataDict['First Name'] = fix(r"First\sName\:\s[A-Za-z0-9.@_' ]+", block_notes)

    # Slicing out the header data from the contents
    for line in dataDict['Email']:
        # Cutting out the substring that says 'Email Address: '
        if dataDict['Email'][line][0:15] == 'Email Address: ':
            line_len = len(dataDict['Email'][line])
            dataDict['Email'][line] = dataDict['Email'][line][15:line_len]
        else:
            pass

    # YES I KNOW REPEATING IS BAD
    # But I have a time crunch and this is free work so cut me some slack!
    # It works, doesnt it?
    for line in dataDict['First Name']:
        # Cutting out the substring that says 'Email Address: '
        if dataDict['First Name'][line][0:12] == 'First Name: ':
            line_len = len(dataDict['First Name'][line])
            dataDict['First Name'][line] = dataDict['First Name'][line][12:line_len]
        # If NO NAME then we use EMAIL
        if dataDict['First Name'][line] == 'NONE':
            dataDict['First Name'][line] = dataDict['Email'][line]
        else:
            pass

    with open('../Work/newer_address_book.csv', 'w') as new_file:
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()

        for line in csv_reader:
            print('FUCK')
            csv_writer.writerow(line)

        # for line in csv_reader:
        #     print(csv_reader)
