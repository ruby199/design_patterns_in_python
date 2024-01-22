"""
Decorators:

[Motivation]
- Want to augment an object with additional functionality
- Do not want to rewrite or alter existing code (OCP; Open-Closed Principle)
- Want to keep new functionality separate (SRP; Single Responsibility Principle)
- Need to be able to interact with exisiting structures
- Two options:
    - Inherit from required object (if possible)
    - Build a Decorator, which simply references decorated object(s)

    
[DEF] Facilitates the addition of behaviors to individual objects without inheriting from them. 

"""

import time


def time_it(func): # time_it is a function that returns a function
  def wrapper(): # wrapper of the original
    start = time.time()
    result = func()
    end = time.time()
    print(f'{func.__name__} took {int((end-start)*1000)}ms')
  return wrapper


@time_it
def some_op():
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123

if __name__ == '__main__':
  # some_op()
  time_it(some_op)()
#   some_op()