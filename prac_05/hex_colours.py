"""
CP1404/CP5632 Practical 5
Question 2
Colour Lookup
"""

COLOUR_CODES = {"absolute Zero": "#0048ba", "acid green": "#b0bf1a",
                "aliceBlue": "#f0f8ff", "alizarin crimson": "#e32636",
                "amaranth": "#e52b50", "amber": "#ffbf00",
                "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()