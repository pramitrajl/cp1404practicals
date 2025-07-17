from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)

def load_guitars(filename):
    """Read guitars from a file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Print all Guitar objects in the list."""
    for guitar in guitars:
        print(guitar)

main()
