"""
Builder inheritance is a technique in object-oriented programming (OOP) used to extend the capabilities of the Builder design pattern, especially when dealing with inheritance hierarchies.

When you have a class hierarchy where a base class is extended by one or more derived classes, builder inheritance can be a useful approach to maintain the fluency and simplicity of the Builder pattern across the hierarchy.

1. Base Builder for Base Class: You start by creating a Builder class for the base class in the hierarchy. This Builder is responsible for constructing instances of the base class and setting its properties.


2. Derived Builders for Derived Classes: For each derived class, you create a corresponding derived Builder class. This derived Builder extends the base Builder, adding methods to set properties specific to the derived class.


3. Fluent Interface with Covariant Return Types: To maintain a fluent interface and allow chaining of builder methods across the hierarchy, the derived Builders override the methods of the base Builder and change their return type to the type of the derived Builder. This technique is known as using covariant return types.

4. Building Process: When constructing an object, you use the Builder corresponding to the specific class you want to instantiate. You can call methods from the base Builder as well as methods from the derived Builder, thanks to the fluent interface.


**Example:
- Suppose you have a Vehicle class (base class) and a Car class that extends Vehicle (derived class). 
You would create a VehicleBuilder for the Vehicle class and a CarBuilder for the Car class. 
The CarBuilder would extend VehicleBuilder, adding methods specific to building a Car.

"""


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb\
        .called('Dmitri')\
        .works_as_a('quant')\
        .born('1/1/1980')\
        .build()  # this does NOT work in C#/C++/Java/...
    print(me)
