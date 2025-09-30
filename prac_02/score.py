"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    print(determine_score(score))

    random_score = random.uniform(0,100)
    print(f"Random score is {random_score:.2f} which is {determine_score(random_score)}")

def determine_score(score: float):
    if score < 0 or score > 100:
        return "invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()