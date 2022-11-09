class Person:
  def __init__(self, name, age, height):
        self.name = name
        self.age = age 
        self.height = height

        # print(self.name, self.age)

        def increment_age(self):
          self.age = self.age +1


# name = input('Enter Name')
# age = int(input('Enter Age'))
obj_person = Person('Ghazala', 31, '5.3')
obj_person.increment_age()