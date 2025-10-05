"""
CP1404/CP5632 - Practical
Random Numbers
"""
import random

print(random.randint(5, 20))  # line 1
"""
What did you see on line 1?
The number 12
Smallest possible number: 5
Largest possible number: 20
"""
print(random.randrange(3, 10, 2))  # line 2
"""
What did you see on line 2?
The number 5
Smallest possible number: 3
Largest possible number: 9
Could line 2 have produced a 4?
No, it can only produce every second number starting at 3, so the only possible numbers are 3, 5, 7 and 9
"""
print(random.uniform(2.5, 5.5))  # line 3
"""
What did you see on line 3?
4.564584323811162
Smallest possible number: 2.5
Largest possible number: 5.5
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
