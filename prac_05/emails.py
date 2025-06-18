""" Emails
Estimate: 30 minutes
Actual: 35 minutes
"""


def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != 'y':
            name = input("Name: ").strip()

        email_to_name[email] = name

    for key in email_to_name.keys():
        print(f"({email_to_name[key]} {key})")

def extract_name(email):
    """ Extract name from given email """
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

main()
