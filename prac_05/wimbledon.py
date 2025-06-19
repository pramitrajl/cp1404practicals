""" Emails
Estimate: 30 minutes
Actual: 45 minutes
"""


FILENAME= "wimbledon.csv"
def main():
    " Run the program using step by step functions "
    data = load_data(FILENAME)
    champion_to_count, countries = process_data(data)
    print_data(champion_to_count,countries)




def load_data(filename):
    """ Read each line from the file """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        return [line.strip().split(",") for line in in_file]

def process_data(data):
    """ Process the data together """
    champion_to_count = {}
    countries = set()
    for row in data:
        country = row[1]
        champion = row[2]
        countries.add(country)
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count, countries

def print_data(champion_to_count, countries):
    """ Display data appropriately """
    print("Wimbledon Champions:")
    for champion in sorted(champion_to_count):
        print(f"{champion} {champion_to_count[champion]}")
    print()
    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(sorted(countries)))



main()