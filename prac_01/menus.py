"""
Menus
CP1404/CP5632 - Practical
"""
name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
       print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
       print("Invalid choice")
       choice = input(">>> ")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

print("Finished.")