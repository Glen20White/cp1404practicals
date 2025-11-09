from guitar import Guitar

def main():
    guitars = load_guitars("guitars.csv")
    print("These are the existing guitars:")
    display_guitars(guitars)
    add_new_guitars(guitars)
    guitars.sort()
    save_guitars("guitars.csv", guitars)
    print("Guitars have been saved to guitars.csv")


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def sort_guitars(guitars):
    """ Sort guitars by year."""
    guitars.sort()
    print("Guitars sorted by year:")
    for guitar in guitars:
        print(guitar)


def display_guitars(guitars):
    """Display guitars in a formatted list with vintage identification."""
    print("\nGuitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage}")


def add_new_guitars(guitars):
    """Add new guitars to the csv file."""
    print("Add a guitar")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Write new guitars to the CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
