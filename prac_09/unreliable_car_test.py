"""
Test the Unreliable Car class.
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Run multiple tests on two UnreliableCar objects with different reliability."""
    good_car = UnreliableCar("Hilux", 100, 90)
    bad_car = UnreliableCar("Triton", 100, 30)

    attempts = 10
    good_car_success_count = 0
    bad_car_success_count = 0

    # Test high reliability car
    for i in range(attempts):
        driven = good_car.drive(10)
        if driven > 0:
            good_car_success_count +=1
    print(f"The Hilux Successfully drove {good_car_success_count/attempts*100}% of the time")

    # Test low reliability car
    for j in range(attempts):
        driven = bad_car.drive(10)
        if driven > 0:
            bad_car_success_count +=1
    print(f"The Triton successfully drove {bad_car_success_count/attempts*100}% of the time")

    print(good_car)
    print(bad_car)

main()