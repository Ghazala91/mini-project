# 1. Use the below list to write all names to a file where each name is on a new line.


# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# file = open('data-persistence.txt', 'w+')
# for person in people:
#     file.write(person+'\n')


# 2. Extend this to use try-catch.

# try:
#         file = open('data-persistence.txt', 'r')

# except FileNotFoundError as fnfe:

#     print('Unable to open file: ' + str(fnfe))


# 3. Extend this to use try-catch-finally.


    
# try:
#     file = open('data-persistence.txt', 'w')
    

# except FileNotFoundError as fnfe:
#     print('Unable to open file: ' + str(fnfe))

# finally:
#     file.close()


# 4.Extend this to make use of the file context manager.
# try:

#     with open('data-persistence.txt', 'w') as items_file:
#         for item in items_file:

#             items_file.write(item + '\n')

# except:
#     print('Failed to open file')


# Create a text file with repeated names such as:
# John
# James
# John
# Sally
# John
# Sally
# Mark
# John



# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# file = open('data-persistence.txt', 'w+')
# for person in people:
#     file.write(person+'\n')