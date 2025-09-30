"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        input_celsius = float(input("Celsius: "))
        convert_fahrenheit = input_celsius * 9.0 / 5 + 32
        print(f"Result: {convert_fahrenheit:.2f} F")
    elif choice == "F":
        input_fahrenheit = float(input("Fahrenheit: "))
        convert_celsius = 5 / 9 * (input_fahrenheit - 32)
        print(f"Result: {convert_celsius:.2f} F")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")