# try:

#   print(x)

# except:

#   print("An exception occurred")




# try:
#     x = input("Enter number: ")
#     x = x + 1
#     print(x)
# except:
#     print("Invalid input")



# in class exercise

# Arbitrary Arguments
# You can call a function with many different arguments using *args.
# Effectively,
# *args creates a list of arguments.

def my_function(*people):
    for person in people:
        print(person)
my_function("Alice", "Bob", "John")



# def concatenate(**kwargs):
#       result = ""
#   # Iterating over the Python kwargs dictionary
#   for arg in kwargs.values():
#     result += arg
#   print (result)

# concatenate(a="Real", b="Python", c="Is", d="Great", e="!")



 