"""
CP1404 Practical 09
Test taxi
"""

from prac_09.taxi import Taxi

def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100)    # 1. New taxi object, named Prius 1, contains 100 units of fuel, (at a price of $1.23/km (moved to taxi class as a class variable))
    my_taxi.drive(40)                 # 2. Drive the taxi 40 km
    # 3. Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fair is ${my_taxi.get_fare()}")

    # 4. Restart meter and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    # 5. Print the details and the current fare
    print(my_taxi)
    print(f"Current fair is ${my_taxi.get_fare()}")

main()
