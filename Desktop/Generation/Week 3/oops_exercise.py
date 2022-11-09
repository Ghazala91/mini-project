# 1. Create a Vehicle class without any attribute and methods.


# class vehicle:
#     pass


# 2. Extend the Vehicle class to contain attributes for max speed and colour. Instantiate the class and print out the attributes.


# class Vehicle:
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour

# vehicle1 = Vehicle(240, 'black')
# print(vehicle1.max_speed, vehicle1.colour)


# 3. Extend the Vehicle class to contain methods for the below. Instantiate the class and call the two methods to update the attributes. Print the changes out.
# Change the value of max speed
# Change the car colour

# class Vehicle:
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour


#  # method 1
#     def changeMaxSpeed(self, max_speed):
#         self.max_speed = max_speed

#     # method 2
#     def changeColour(self, colour):
#         self.colour = colour

# # method 3
#     def showDescription(self):
#         print("This vehicle has a speed of", self.max_speed, "and is", self.colour)

# vehicle1 = Vehicle(240, 'black')


# # call method 1 and set color
# vehicle1.changeMaxSpeed(100)

# # call method 2 and change value of max speed 
# vehicle1.changeColour('White')

# vehicle1.showDescription()






# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and nothing else. Instantiate a Bus instance and print out the attributes.

# class Vehicle:
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour


#  # method 1
#     def changeMaxSpeed(self, max_speed):
#         self.max_speed = max_speed

#     # method 2
#     def changeColour(self, colour):
#         self.colour = colour

# # method 3
#     def showDescription(self):
#         print("This vehicle has a speed of", self.max_speed, "and is", self.colour)

# vehicle1 = Vehicle(240, 'black')


# # call method 1 and set color
# vehicle1.changeMaxSpeed(100)

# # call method 2 and change value of max speed 
# vehicle1.changeColour('White')

# vehicle1.showDescription()




# class Bus(Vehicle):
#     pass

# bus1 = Bus(180, 'yellow')
# print(bus1.max_speed, bus1.colour)



# 5. Use one of the built-in Python functions to print out the underlying object type of the Bus object.
# Python's built-in type()

# class Vehicle:
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour


#  # method 1
#     def changeMaxSpeed(self, max_speed):
#         self.max_speed = max_speed

#     # method 2
#     def changeColour(self, colour):
#         self.colour = colour

# # method 3
#     def showDescription(self):
#         print("This vehicle has a speed of", self.max_speed, "and is", self.colour)

# vehicle1 = Vehicle(240, 'black')


# # call method 1 and set color
# vehicle1.changeMaxSpeed(100)

# # call method 2 and change value of max speed 
# vehicle1.changeColour('White')

# vehicle1.showDescription()




# class Bus(Vehicle):
#     pass

# bus1 = Bus(180, 'yellow')
# print(bus1.max_speed, bus1.colour)


# print(type(bus1))


# 6. Use one of the built-in Python functions to print out if the Bus object is an instance of Vehicle .




class Vehicle:
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour


 # method 1
    def changeMaxSpeed(self, max_speed):
        self.max_speed = max_speed

    # method 2
    def changeColour(self, colour):
        self.colour = colour

# method 3
    def showDescription(self):
        print("This vehicle has a speed of", self.max_speed, "and is", self.colour)

vehicle1 = Vehicle(240, 'black')


# call method 1 and set color
vehicle1.changeMaxSpeed(100)

# call method 2 and change value of max speed 
vehicle1.changeColour('White')

vehicle1.showDescription()




class Bus(Vehicle):
    pass

bus1 = Bus(180, 'yellow')
print(bus1.max_speed, bus1.colour)


print(type(bus1))

# Python's built-in isinstance() function
print(isinstance(bus1, Vehicle))

# 7. Extend the Bus class to also contain an attribute of seating_capacity . Add a method to calculate the price of a ticket. This is calculated as seating_capacity * 0.05 , with an extra 10% of the total of seating_capacity * 0.05 on top. Instantiate a Bus instance and print the ticket price.

