from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi class, a subclass of Taxi."""
    flagfall = 4.50 #new fair charge

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, based on the parent class Taxi."""
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km *=fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the total price for the Silver Service Taxi trip"""
        return super().get_fare() + self.flagfall