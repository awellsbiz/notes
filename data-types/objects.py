

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

person_object = Person('John', 30, 'Engineer')
print(person_object.name)  
# output: 'John'