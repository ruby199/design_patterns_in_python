"""
Builder design pattern: commonly ised pattern for constructing compplex objects. It addresses several issues and provides specific benefits in the design and construction of objects/

1. Separation of Construction and Representation
- The builder pattern separates the construction of a complex object from its representation - allowing the same construction process to create different representations.

2. Encapsulation of Construction logic
- By encapsulating the construction logic in a separate builder class, the complexity of constructing an object is hidden from the client. 
The client only needs to specify the type and content of the object it needs, and the builder handles the actual construction process. 

3. Control over the Construction Process
- The bulider pattern provides finer control over the construction process. 
- Unlike other creational patterns, it allows step-by-step construction of a complex object and can defer the assembly of parts until the final step. 

4. Immutability of the Final Object
- Once constructed, the object can be made immutable, which is beneficial for multi-threaded applications. The object does not need to support a separate mutable state for construction.

5. Improved Readablity and Maintainability: Using the Builder pattern can lead to more readable code.
"""

class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self # allows you to chain the invocations one after another

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)


# if you want to build a simple HTML paragraph using a list
hello = 'hello'
parts = ['<p>', hello, '</p>']
print(''.join(parts))

# now I want an HTML list with 2 words in it
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

# ordinary non-fluent builder
# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# fluent builder
builder.clear()
builder.add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print('Fluent builder:')
print(builder)
