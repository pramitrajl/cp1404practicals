""" Estimated: 30 mins
Actual : 45 mins """
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """ """
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)
    guitars = add_guitars(guitars)
    save_guitars(FILENAME, guitars)
    print("Guitars saved to file.")

def load_guitars(filename):
    """ Read guitars from file and return objects """
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
    """ Display guitars from file """
    for guitar in guitars:
        print(guitar)

def add_guitars(guitars):
    """ Add guitars """
    name = input("Enter name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Enter name: ")
    return guitars

def save_guitars(filename, guitars):
    """ Save the new ones in file """
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()
