""" Estimated time: 5 minutes
Actual time = 7 minutes"""
class ProgrammingLanguage:
    """ Represent a ProgrammingLanguage object """
    def __init__(self, name, typing, reflection, year):
        """ Initialize instances """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Return whether its dynamic or not """
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year} "
