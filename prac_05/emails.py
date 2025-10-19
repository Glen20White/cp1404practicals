"""
CP1404/CP5632 Practical 5
Question 4
Email to name dictionary
Estimate: 20 minutes
Actual:   25 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    username = email.split('@')[0]
    name_split = username.split('.')
    name = " ".join(name_split).title()
    return name


main()