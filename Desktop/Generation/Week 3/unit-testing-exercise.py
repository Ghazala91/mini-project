
# Write a number of unit tests to test the following scenarios:
# adds two whole numbers

def adds_two_numbers(a, b):
    return a + b

def test_adds_two_numbers():
    a = 3
    b = 3
    expected = 6

    result = test_adds_two_numbers(a,b)

    assert result == expected

test_adds_two_numbers()


# adds a positive whole number to a negative whole number

def test_number_and_negative():
    a = 4
    b = -5
    expected = -1

    result = test_number_and_negative(a, b)

    assert result ==expected

test_number_and_negative()

# adds two floating point numbers
def test_two_floats():
    a = 2.2
    b = 1.2
    expected = 3.4

    result = test_two_floats(a, b)
    
    assert result == expected

test_two_floats()


# adds a string to a whole number

def test_add_string_number():
     a = 'Ghazala'
     b = 2
     expected = TypeError

     result = test_add_string_number(a, b)

     assert result == expected

test_add_string_number()


# adds two strings
def test_adds_two_strings():
    a = 'Ghazala'
    b = 'Rehman'
    expected = 'GhazalaRehman'

    result = test_adds_two_strings(a, b)

    assert result == expected

test_adds_two_strings()