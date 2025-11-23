from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """A Car subclass that only sometimes drives based on its reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on its reliability."""
        chance_driving = randint(0, 100)
        if chance_driving < self.reliability: # car drives if the random number is less than the car's reliability
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0


