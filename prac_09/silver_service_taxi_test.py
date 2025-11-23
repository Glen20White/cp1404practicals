from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test Silver Service Taxi trip"""
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"${taxi.get_fare()}")

main()