# . Read the ford_escort.csv example file using the Python csv library and print each row.
# Remember there's a header line!

import csv
# open people.csv and read as string
with open("ford_escort.csv", 'r') as file:
 reader = csv.reader(file, delimiter=',')
 for row in reader:
    print(row)
