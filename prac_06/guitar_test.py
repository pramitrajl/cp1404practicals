""" Estimated time: 30 minutes
Actual time = 40 minutes"""
from guitar import Guitar

CURRENT_YEAR = 2025

# def test():
""" Test code for the program"""
#
#
#     gibson = Guitar("Gibson L-5 CES", 1925, 16035.40)
#     another = Guitar("Another Guitar", 2011, 10000)
#
#     expected_age_gibson = CURRENT_YEAR - 1925
#     expected_age_another = CURRENT_YEAR - 2011
#
#     print(f"{gibson.name} get_age() - Expected {expected_age_gibson}. Got {gibson.get_age()}")
#     print(f"{another.name} get_age() - Expected {expected_age_another}. Got {another.get_age()}")
#     print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
#     print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")
#
#
# test()

def main():
    """ Actual function to get the data and print it """
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name,year,cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
    print()

    print("... snip ...")

    print()

    while guitars:
        print("These are my guitars: ")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "vintage" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth {guitar.cost:7,.2f}{vintage_string} ")

main()