"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
def main():
    """ Get the score and show result """
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

def generate_random_score():
    """ Generate random score and show result """
    score = random.randint(0,100)
    result = get_score_result(score)
    print(result)

def get_score_result(score):
    """ Determine result """
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Pass"
        else:
            return "Bad"


main()

