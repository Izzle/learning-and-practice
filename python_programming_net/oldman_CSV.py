
import csv

with open('oldman_address_book.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

emails = []
first_names = []
last_names = []

# Remove "" then iterate into the corret list
for row in readCSV:
	print(row)
    print(row[0])
    print(row[0], row[1])
    em = row[0]
    fn = row[1]
    ln = row[2]


    emails.append(em)
    first_names.append(fn)
    last_names.append(ln)

