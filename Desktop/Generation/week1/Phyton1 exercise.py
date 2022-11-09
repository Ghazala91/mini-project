# Strings

# 1. Create a variable which will store your first name. Print out the variable.

from operator import truediv


first_name = 'Ghazala'
print(first_name)

# 2. Create a second variable which will store your last name. Concatenate the two variables and print out the result.

last_name = 'Rehman'
print(first_name + " " + last_name)


# 3. Extend the above to print the following using an f-string: Hi, my name is {first_name}{last_name}.

print(f'Hi, my name is {first_name} {last_name}')

# Integers
# 1. Create two variables that store integer values. Calculate the product (the number you get by
# multiplying two or more other numbers together) of the two integers and store it in a third variable.
# Print the value of this variable.

int1 = 31
int2 = 2
result = int1 * int2
print(result)



# Lists
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# 1. Retrieve the third element (the second-indexed element) and store it in its own variable. Print the variable.

print(people[2])


# 2. Retrieve the element third from the back of the list and store it in its own variable. 
# Print the variable.

print(people[-3])


# 3. Split the list into a new list with just the names Mark, Lisa, Joe and Barry.

print(people[2:6])


# 4. Print whether or not the first and last element in the list are equal to one another.

print(people[0==-1])


# INPUT

# 1. Accept input from the user for their name. Print their name out.
name = input('What is your name?')
print('Your name is',name)

# 2. Accept two integer inputs from the user and calculate the product. Print out the product.
number1 = int(input('Enter 1st number'))
number2 = int(input('Enter 2nd number'))
result = number1 + number2

print(result)


# 3. Accept two integer inputs from the user. Use the comparison operator to print out if the two values are equal (True), or if they're not (False).

number1 = int(input('Enter 1st number'))
number2 = int(input('Enter 2nd number'))

print(f'The entered value are equal {number1 == number2}')


# PART 2

# 1. Accept an integer input from the user. If the number is even, print out an appropriate message, and vice versa if it is odd.
# Hint: Using modulus may help you here


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# 2. Extend the above to print a different message if the number is a multiple of four.

num = int(input("Enter a number: "))
mod = num % 4
if int(num) % 4 == 0:
    print("This is an multiple of four.")
else:
    print("This is not an multiple of four    .")

# 3. Accept an integer input from the user. If the number is a multiple of three, print the word fizz. If the number is a multiple of five, print buzz. If it is neither then do not print anything.

num = int(input("Enter a number: "))

if int(num) % 3 == 0:
    print("This is an multiple of three FIZZ.")

elif int(num) % 5 == 0:
    print("This is an multiple of five BUZZ.")
else:
    print()


# 4. Write a program that will convert celsius to fahrenheit, and vice versa. Accept two inputs from the user. The first will be a letter which is either c, which means you should convert from fahrenheit to celsius, or f which is vice versa. For the second input, accept an integer value representing the temperature. 
# Print out the converted value, along with the correct temperature type.





# PART 3

# 1. In your own words, describe each of the following logical operators: and, or and not.

# AND , both sides need to be true
# OR ,  at least one need to be true
# NOT,   opposite

# 2. Consider the below code. Write down what you think the expected output will be.
a = False
b = False
x = not(a)
y = not(b)
print(a or b)
print(x or y)
print(a or x)
print(x or b)


# 1- False
# 2-true
# 3-true
# 4-true

# 3. Consider the below code. Write down what you think the expected output will be.

a = False
b = False
x = not(a)
y = not(b)
print(a and b)
print(a and x)
print(y and b)
print(x and y)

# 1= false
# 2= False
# 3= False
# 4= true

# 4. Without referring back to the slides, write down the truth table for each of the three logical operators.



# 5. Create a program for the following specification:
# A bank will offer a customer a loan if they are old enough and have a large enough salary. Ask
# the user for input of both their age and their salary. If the user is over 21 and has a salary of at
# least £21000, offer them a loan of up to £50,000. If the user is over 30 and has a salary of at
# least £35000, offer them a loan of up to £75,000. If the user is over 30 and has a salary of at
# least £50000, offer them a loan of up to £100,000. If none of the above, do not offer them a
# loan.

age = int(input('Enter your age'))

salary = int(input(' Enter your Salary'))

if age > 30 and salary >= 50000:
    print('Loan available up to £100,000')

elif age > 30 and salary >= 35000:
    print('Loan available up to £ 75,000')

elif age > 21 and salary >= 21000:
    print('Loan available up to £50,000')

else:
    print('Loan not available')