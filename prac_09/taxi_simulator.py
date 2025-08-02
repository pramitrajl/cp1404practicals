from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Display menu and do tasks accoring to choices """
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill_to_date = 0.0
    current_taxi = None

    display_menu()
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            selected_taxi = choose_taxi(taxis)
            if selected_taxi:
                current_taxi = selected_taxi
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        display_menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)

def display_menu():
    print("q)uit, c)hoose taxi, d)rive")

def list_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Choose a taxi and return the selected taxi or None if invalid """
    list_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input; please enter a number.")
    return None

def drive_taxi(current_taxi):
    """Drive the currently selected taxi and return the trip cost"""
    try:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid input; please enter a number.")
        return 0.0



main()
