"""
Expected: 20 minutes
Actual: 15 minutes
"""


class Guitar:
    current_year = 2025

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return Guitar.current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50