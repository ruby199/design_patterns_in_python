"""
Builder facets is an extension of the basic Builder pattern.
It is used when the object that needs to be built is so complex that a single Builder class becomes too large or unwieldy. 

In such cases, the Builder is split into multiple classes, each of which is responsible for building a particular aspect or "facet" of the object. 

Faceted Builder: Instead of using a single Builder, the construction process is split into several smaller builders, each focusing on a specific aspect of the object. Each of these smaller builders is a facet of the main builder.

Fluent Interface: Typically, Builder Facets employ a fluent interface. This means that each method in the builder returns the builder object itself, allowing for method chaining. This approach makes the client code more readable and intuitive.


"""

class Person:
    def __init__(self):
        print('Creating an instace of Person')
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


class PersonBuilder:  # facade
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person

    
    
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
    
    def at(self, company_name):
        self.person.company_name = company_name
        return self
    
    def as_a(self, position):
        self.person.position = position
        return self
    
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self



class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person) # person should be an exisiting instance

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self



if __name__ == '__main__':
    pb = PersonBuilder()
    p = pb\
        .lives\
            .at('123 London Road')\
            .in_city('London')\
            .with_postcode('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()
    print(p)
    person2 = PersonBuilder().build()
    print(person2)
