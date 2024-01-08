# Decorator
def singleton(class_):
    instances = {} # keep every instances into a dictionary

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs) # if not in instance -> call it with the arguments and keyword arguments
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database')

# Loading the database only once
if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)