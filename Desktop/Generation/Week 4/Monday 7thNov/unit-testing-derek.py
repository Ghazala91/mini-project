# def add_two_numbers(a, b):
    
#     if type(a) is int and type(b) is int:
#         print('adds two whole numbers, or adds a positive whole number to a negative whole number')   
#     elif type(a) is float and type(b) is float:
#         print('adds two floating point numbers')
#     elif (type(a) is str and type(b) is not str) or (type(a) is not str and type(b) is str):
#         if type(a) is not str:
#             a = str(a)
#         elif type(b) is not str:
#             b = str(b)
#         print('adds a string to a whole number')           
#     elif (type(a) is str and type(b) is str):
#         print('adds two strings')
    
#     return a + b
    
    
    

def add_two_numbers(a, b):
    # print(f'type a is: {type(a)}, type b is {type(b)}')    
    if (type(a) is str and type(b) is not str) or (type(a) is not str and type(b) is str):
        if type(a) is not str:
            a = str(a)
        elif type(b) is not str:
            b = str(b)    

    return a + b
    

    
def test_add_two_numbers(a, b, expected):
    # Act
    actual = add_two_numbers(a, b)    
    # Assert - pass
    assert expected == actual
    print(f'{a} + {b} = {expected}')


    
test_add_two_numbers(10, 10, 20) # 10 + 10 = 20

test_add_two_numbers(-10, -15, -25) # -10 + -15 = -25

test_add_two_numbers(1.7, 12.333, 14.033) # 1.7 + 12.333 = 14.033

test_add_two_numbers(10, 'this is me', '10this is me') # 10 + 'this is me' = '10this is me'

test_add_two_numbers('hello there', 'this is me', 'hello therethis is me') # 'hello there' + 'this is me' = 'hello therethis is me'