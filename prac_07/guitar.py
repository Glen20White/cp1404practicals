class Guitar:
    CURRENT_YEAR = 2025

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        """Return True if this guitar is older (smaller year) than another."""
        return self.year < other.year