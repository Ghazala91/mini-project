# Python 2 Exercises

## Functions

# 1. Create a function that takes two numbers as arguments and return the sum. Print the result.

def add_number( a,b):
     return a+b

sum = add_number(2,3)
    
print(sum)

# 2.Extend the above by passing an arbitrary amount of integers to a function and return the result. Print the result. Hint: use `*args`.

def add_number(*nums):
        sum = 0

        for num in nums:
         
         sum += num
      
        return sum

        sum = add_number(1, 2, 3, 4)
        print(sum)

  
#   3. Pass an arbitrary amount of named arguments to a function and create a dictionary. The keys will be the names of the arguments and the values are assigned values of the named arguments. Hint: use `**kwargs`

def create_dictionary(**kwargs):
    dictionary = {}
    
    for key, value in kwargs.items():
      dictionary[key] = value
      
    return dictionary

dic = create_dictionary(title="The Matrix", director="Wachowski", year=1999)

print(dic)

