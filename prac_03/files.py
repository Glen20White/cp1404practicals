"""
CP1404/CP5632 - Practical
Read and write files
"""
"""Question 1"""
name = input("Enter your name: ")

out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

"""Question 2"""
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()

print(f"Hi {name}!")

"""Question 3"""
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    total = number1 + number2

print(total)