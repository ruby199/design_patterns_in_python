# Single Responsibility Principle (SRP) # Seperation of concerns (SOC)
# Class
 
# This class represents a journal, which is a collection of entries.
class Journal:
    # The constructor initializes the journal
    def __init__(self):
        self.entries = []
        self.count = 0

    # This method adds a new entry to the journal.
    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    # This method removes an entry from the journal at the specified position.
    def remove_entry(self, pos):
        del self.entries[pos]

    # This method defines how the journal object is represented as a string.
    def __str__(self):
        return "\n".join(self.entries)

    # break SRP - anti pattern. The single responsibility principle prevents you from making God objects.
    # It enforces this idea that class should have a single reason to change and that change should be somehow related to its primary responsibility.
#     def save(self, filename):
#         file = open(filename, "w")
#         file.write(str(self))
#         file.close()

#     def load(self, filename):
#         pass

#     def load_from_web(self, uri):
#         pass

# This class handles the persistence of the Journal.
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# file = r'c:\temp\journal.txt'
# PersistenceManager.save_to_file(j, file) 

# verify!
with open(file) as fh:
    print(fh.read())
