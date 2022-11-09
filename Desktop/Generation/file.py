# File modes:
# r: read-only
# r+: both read and write
# w: write-only - overwrites the file
# w+: both read and write - overwrites the file
# a: write-only - appends to the file
# a+: both read and write - appends to the file


# Some more modes:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist



# my_file = open('exercise.txt', 'x')

# my_file = open('exercise.txt', 'r')
# contents = my_file.read()
# print(contents)



# file = open("exercise.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line)



# Exercise
# Create a text file in your text editor and add some names of people on each line

# my_file = open('exercise.txt', 'x')

# Read the names from the file in your application and populate an empty list with the names
# Print out the list!

# list = []

# file = open("exercise.txt", "r")

# for line in file.readlines():
    
#     list.append(line)
    
# print(list)




# remove n

# list = []

# file = open("exercise.txt", "r")

# for line in file.readlines():
    
#     list.append(line.strip())
    

# print(list)





# list = []
# # file = open("exercise.txt", "r")
# # lines = file.readlines()
# # for line in lines:
# list.append(line)

# #     print(list)


#  Use the below list to write all names to a file where each name is on a new line.



people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

file = open('people.txt', 'w+')
for person in people:
    file.write(person+'\n')


#  Extend this to use try-catch.

