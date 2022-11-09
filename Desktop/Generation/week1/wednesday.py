# a = 12

# if a > 15:
#     print ('a is greater 15')

# if a > 10:
#     print ( 'a is greater than 10')

# if a > 5:
#     print(' a is greater than 5')

# if a > 0:
#     print(' a is greater than 0')
# Accept an integer input from the user. If the number is even, print out an appropriate message, and
# vice versa if it is odd.


# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")


# # . Extend the above to print a different message if the number is a multiple of four.
# num = int(input("Enter a number: "))
# mod = num % 4
# if int(num) % 4 == 0:
#     print("This is an multiple of four.")
# else:
#     print("This is not an multiple of four    .")

#  Accept an integer input from the user. If the number is a multiple of three, print the word fizz. If the
# number is a multiple of five, print buzz. If it is neither then do not print anything.
       





# num = int(input("Enter a number: "))
# # mod = num % 3
# if int(num) % 3 == 0:
#     print("This is an multiple of three FIZZ.")

# elif int(num) % 5 == 0:
#     print("This is an multiple of five BUZZ.")
# else:
#     print()

# a = False
# b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)


# a = False
# b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)



age = int(input('Enter your age'))

salary = int(input(' Enter your Salary'))

if age > 30 and salary >= 50000:
    print('Loan availabke up to £100,000')

elif age > 30 and salary >= 35000:
    print('Loan available up to £ 75,000')

elif age > 21 and salary >= 21000:
    print('Loan available up to £50,000')

else:
    print('Loan not available')