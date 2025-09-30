MENU_EXERCISE = """(H)ello
(G)oodbye
(Q)uit"""
name = input("Enter your name: ")
print(MENU_EXERCISE)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello")
    elif choice == "G":
        print("Goodbye")
    else:
        print("Invalid option")
    print(MENU_EXERCISE)
    choice = input(">>> ").upper()
print("You Have Quit")