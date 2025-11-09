"""
Expected: 30 minutes
Actual: 35 minutes
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    guitar_name = input("Guitar name: ")
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, year, cost))
        print(f"{guitar_name} ({year}) : ${cost:.2f} added.")
        guitar_name = input("Guitar name: ")

    print("\nThese are my guitars:\n")

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()