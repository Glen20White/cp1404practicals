"""
CP1404/CP5632 Practical
Basic list operations
"""

""" number stuff """
print("Please enter 5 numbers")
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# first number
print("The first number is", numbers[0])
# last number
print("The last number is", numbers[-1])
# smallest number
print("The smallest number is", min(numbers))
# largest number
print("The largest number is", max(numbers))
# average
print("The average of the numbers is", sum(numbers) / len(numbers))

""" username checker """
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")