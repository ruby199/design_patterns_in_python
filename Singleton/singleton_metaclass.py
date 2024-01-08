class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database() #  Attempts to create another instance of Database. However, because of the Singleton pattern, it doesn't actually create a new instance; instead, it retrieves the existing instance created earlier.
    print(d1 == d2) # True: This confirms that only one instance of Database exists.
