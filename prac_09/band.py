class Band:
    """Band class for storing musicians"""

    def __init__(self, name=""):
        """Initialise a Band with a name and collection"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of the class Band """
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation showing variables"""
        return str(vars(self))

    def add(self, musician):
        """Add a musician"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument"""
        return "\n".join(musician.play() for musician in self.musicians)