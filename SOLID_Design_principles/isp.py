"""
# ISP

Interface Segregation Principle (ISP) states that no client should be forced to depend on methods it does not use. 

This principle is aimed at reducing the side effects and frequency of required changes by splitting the software into multiple, independent parts. 

"""

from abc import abstractmethod

# Base class Machine with general functions
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError

# A multifunctional printer class that inherits from Machine
# used if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

# Class for an old-fashioned printer, implementing the Machine interface
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!') # could be problematic in larger applications. This approach, while it might be acceptable in a small script, can lead to issues in a more complex system.

## Using ISP

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document): pass

    def scan(self, document): pass 


class Printer:
    @abstractmethod
    def print(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass



class MultiFunctionDevice(Printer, Scanner):
    # instead of simply overwriting them, use abstractmethod
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer
    
    @abstractmethod
    def print(self, document):
        self.printer.print(document)

    @abstractmethod
    def scan(self, document):
        self.scanner.scan(document)

printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
# printer.scan(123)  # error!
