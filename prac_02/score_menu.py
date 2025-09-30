def main():
    MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"
    score = None
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = user_input_score()
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            score_as_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("You Have Quit, Farewell")


def user_input_score():
    score = int(input("Enter score: "))
    return score


def determine_score(score):
    if score is None:
        return "No score entered yet, please enter a score first"
    elif score < 0 or score > 100:
        return "invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def score_as_stars(score):
    if score is None:
        print("No score entered yet, please enter a score first")
    else:
        print('*' * score)


main()