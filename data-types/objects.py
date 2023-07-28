"""
Objects (instances of classes) are more powerful and customizable data structures, allowing you to define complex data structures and behaviors to suit your specific requirements.
"""

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

person_object = Person('John', 30, 'Engineer')
print(person_object.name)  
# output: 'John'