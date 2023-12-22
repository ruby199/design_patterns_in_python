"""
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)

The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
"""

class CodeBuilder:
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []

    def add_field(self, field_name, field_value):
        self.fields.append((field_name, field_value))
        return self

    def __str__(self):
        code = [f"class {self.class_name}:"]
        if not self.fields:
            code.append("  pass")
        else:
            code.append("  def __init__(self):")
            for field_name, field_value in self.fields:
                # Using single quotes for string values
                formatted_value = field_value if not isinstance(field_value, str) else f"'{field_value}'"
                code.append(f"    self.{field_name} = {formatted_value}")
        return '\n'.join(code)
    
    
# Sample usage of the CodeBuilder
cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)