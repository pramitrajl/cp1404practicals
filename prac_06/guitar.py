""" Estimated time: 10 minutes
Actual time = 8 minutes"""
CURRENT_YEAR = 2025

class Guitar:
    """ Represent guitar object """
    def __init__(self, name="", year=0, cost=0 ):
        """ Initialize instances """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """ Return the age of guitar """
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """ Check if the guitar is vintage or not """
        return self.get_age() >= 50