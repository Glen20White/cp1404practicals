from guitar import Guitar

def main():
    guitars = load_guitars("guitars.csv")
    sort_guitars(guitars)


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


if __name__ == "__main__":
    main()
