# 1. Write a unit test for the below function.

# def add_two_numbers(a, b):
#  return a + b

# def test_add_two_numbers():
#     a = 3
#     b = 3
#     expected = 6

#     result = test_add_two_numbers(a,b)

#     assert result == expected

# test_add_two_numbers()


# 2. Write a unit test for the below function add_number_with_random_number. You will need to update the code to make use of dependency injection and create a mock function.

import random
from unittest import expectedFailure
def get_random_number():
 return random.randint(1, 10)

def add_number_with_random_number(a):
     return a + get_random_number()


def add_number_with_random_number(a, get_random):
 return a + get_random()



def test_add_number_with_random_number():
     a = 3
     expected = 6
     def mock_get_random_number():
        return 3

     actual = add_number_with_random_number(a, mock_get_random_number)

     assert actual == expected
     print("It was a success")


test_add_number_with_random_number()

# 3. Write a unit test for the below function add_two_random_numbers. You will need to update the code to make use of dependency injection and create a mock function.

from random import randint

def get_random_number():
 return randint(1, 10)

def add_two_random_numbers():
     return get_random_number() + get_random_number()


def add_two_random_numbers(get_random):
     return get_random() + get_random()

def test_add_two_random_numbers():
     expected = 6
     def mock_get_random_number():
         return 3
     actual = add_two_random_numbers(mock_get_random_number)

     assert actual == expected
     print (" It was a success")

test_add_two_random_numbers()


# 4. Write a unit test for the below function get_random_number. This time it's slightly different as we need to mock a function we haven't written, but the same principles apply. Hint: you need to match the number of arguments that the randint function takes for the mock function you will write.

from random import randint

def get_random_number():
 return randint(1, 10)


