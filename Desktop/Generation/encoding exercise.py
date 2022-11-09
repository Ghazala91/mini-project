# Reading and writing CSV


# 1. Read the ford_escort.csv example file using the Python csv library and print each row.
# Remember there's a header line!


# import csv

# with open("ford_escort.csv", 'r') as file:
#  reader = csv.reader(file, delimiter=',')
#  for row in reader:
#     print(row)


# 2. Extend the above so that the data is read into a dictionary.

# open people.csv and read as dict

# with open("ford_escort.csv", 'r') as file:
#  csv_file = csv.DictReader(file)
#  for row in csv_file:
#     print(row)

# 3. Write the following data as CSV to a file. Add a header row with likely column titles.
# ['Joe', 'Bloggs', 40]
# ['Jane', 'Smith', 50]


# import csv

# with open('people.csv', mode='w') as file:
#   writer = csv.writer(file, delimiter=',')

#   writer.writerow(['Joe', 'Bloggs', 40])
#   writer.writerow(['Jane', 'Smith', 50])


# # open the people.csv and write row from dict
# with open('people.csv', mode='w') as file:
# #  # set the headers for the CSV
#  fieldnames = ['first_name', 'last_name', 'age']
#  writer = csv.DictWriter(file, fieldnames=fieldnames)
# #  # instruct the writer to know to write the headers
#  writer.writeheader()

# #  # instruct the writer to write the row
#  writer.writerow({
#  'first_name': 'Jan',
#  'last_name': 'Smith',
#  'age': 60
#  })


#3.1 . Write another block of code that will append the following data to the file created in #3.
# ['Mike', 'Wazowski', 40]

# import csv

# with open('people.csv', mode='a') as file:
#   writer = csv.writer(file, delimiter=',')

#   writer.writerow(['Mike', 'Wazowski', 40])


# JSON

# 1. Read the example.json handout file using the native Python json library. Print the object that is created

# loads() converts JSON String to a python object

# import json

# with open("example.json") as file:
#     data = json.load(file)

# print(data)


# 2. Print the "id" of all the items in the menu

# import json
# with open ("example.json") as file:
#     data = json.load(file)

# for item in data['menu']['items']:
#     print (item['id'])



# 3. Write the following data as JSON to a file.


# import json

# data ={
#  'president': {
#  'name': 'Zaphod Beeblebrox',
#  'species': 'Betelgeusian'
#  }
# }

# with open('output.json', 'w+') as file:
#    json.dump(data, file)

# with open('output.json') as file1:
#    data1 = json.load(file1)
#    print(data1)