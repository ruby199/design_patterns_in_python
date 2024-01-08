"""
[Def] Singleton - A compnent which is instanticated only once.

[Motivation]
For some components it only makes sense to have one in the system
- Database repository
- object factory

A Singleton design pattern is used to ensure that a class has only one instance and provides a global point of access to that instance. 

This pattern is often used when exactly one object is needed to coordinate actions across the system. 

e.g., the initializer call is expensive
"""
import random

class Database:
    initialized = False

    def __init__(self):
        self.id = random.randint(1, 101)
        print('Generated an id of ', self.id)
        pass
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)
        return cls._instance
    

database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1.id, d2.id)
    print(d1 == d2)
    print(database == d1)


