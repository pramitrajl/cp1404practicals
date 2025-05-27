def main():
    """ Check the validity of password """
    min_length = 8
    password = get_password()
    while len(password) < min_length:
        print(f"Error: Password must be at least {min_length} characters long.")
        password = get_password()
    print_asterisks(password)
    print("Password accepted")


def get_password():
    """ Get password """
    password = input("Enter password: ")
    return password


def print_asterisks(password):
    """ Print in asterisks """
    print('*' * len(password))


main()
