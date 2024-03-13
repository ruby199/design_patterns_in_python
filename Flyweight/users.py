"""
[DEF] Flyweight Design pattern:
A space optimization technique that lets us use less memory by storing externally the data associated with similar objects. 


Motivation:
- Avoid redundancy when storing data
    E.g. MMORPG
    - Plently of users with identical first/last names
    - No sense in storing same first/lsat name over and over again
    - Store a list of names and references to them

    E.g. bold or italic tect formatting
    - We don't want each character to have a formatting character
    - Operate on ranges(e.g. line number, start/end positions)

"""



import random
import string
import sys

class User: # Stores the name of the user
    def __init__(self, name):
        self.name = name

class User2: # point to the common store
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1
        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])

def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


if __name__ == '__main__':
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))

    u2 = User2('Jim Jones')
    u3 = User2('Frank Jones')
    print(u2.names)
    print(u3.names)
    print(User2.strings)

    users2 = []

    for first in first_names:
        for last in last_names:
            users2.append(User2(f'{first} {last}'))
