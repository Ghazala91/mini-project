# 1. Print the numbers 0 to 10 using a for loop.

for i in range(11):
    print(i)


# 2. Print the numbers 0 to 10 using a while loop.

i = 1
while(i<=10):
    print(i)
    i += 1


# 3. Print the list of numbers below using a for loop.
nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]

for num in nums:
    print(num)

# for num in [0, 2, 8, 20, 43, 82, 195, 204, 367]:
#     print(num)

# 4. Print the message 'Done!' after printing the numbers 0 to 10 with a for loop. Hint: use the for-else construct.

for x in range(11):
    print(x)
else:
    print("Done!")


# 5. Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of
# the element.

main_list=[]
list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for i in list1:
        
       if i in list2:
            main_list.append(i)

print(main_list)

# for first in list1:
#     for second in list2:
#         if first == second:
#             print(first)


# 6. Using a while loop, on every iteration generate a random number. If it's a multiple of 5, break from the loop. If it's a multiple of 3, end the current iteration with
# continue and print a message to show you are skipping. If it's neither, print the number and continue the loop.
# When the loop has been broken, print a message indicating that this has happened before the program exits.
# Hint:
import random
while True:
    x = random.randint(1,100)
    if x % 5 == 0:
        print('Break the loop')
        break

    elif x %3  ==0:
       print( 'Skipping') 
    continue
    

else:
        print(x)


#  Dictionaries
# 1. Add a new key-value pair to the below car dictionary for the colour. Print out the colour to verify it worked.

car ={
'brand': 'Ford',
'model': 'Mustang',
'year' : 1964,
'isNew': False
}

car['colour'] = 'black'
print('add colour', car)


# 2. Update the value of the model in the car dictionary. Print out the new value to verify it worked.

car ['model'] = 'fiesta'

print(car['model'])


# 3. Delete the model key-pair from the car dictionary. Print out the entire dictionary to verify it worked.

del car['model']

print(car)



# 4. Use the items() function to loop through the dictionary and print each key-value pair like so:
# key: x, value: y
# Hint: for key, value in x.items(): Hint: You will need to cast the values to a string

car ={
'brand': 'Ford',
'model': 'Mustang',
'year' : 1964,
'isNew': False
}

for key, value in car.items():
    print("key:" + key + ", value: " + str(value))


# Functions
# 1. Create a function that takes two numbers as arguments and return the sum. Print the result.

def add_number( a,b):
     return a+b

sum = add_number(2,3)
    
print(sum)

# 2. Extend the above by passing an arbitrary amount of integers to a function and return the result. Print the result. Hint: use *args .


