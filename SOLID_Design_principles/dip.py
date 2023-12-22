"""
# DIP: Dependency Inversion Principle(DIP) is one of the five fundamental SOLID principles of oop with two main principle:

1. High-Level modules should not depend on low-level models
- Both should depend on abstractions. The core functionality of your application shouldn't depend on the details but rather on interfaces or abstract classes. For instance, if you are writing a reporting system, the main logic of the system should not depend directly on a specific database or data source. 

2. Abstractions should not depend on details
- Details should depend on abstractions. This part of the principle em[hasizes that the high-level definitions (interfaces or abstract classes) should not be comcerned with the implementation details. Instead, the implementation details should be designed to fulfill the needs of the high-level definitions. 

"""

from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass

# Low-level module
class Relationships(RelationshipBrowser):
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))
            
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

# High-level module that performs operations on relationships
class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)