"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

def generate_random_score():
    score = random.randint(0,100)
    result = get_score_result(score)
    print(result)

def get_score_result(score):
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
generate_random_score()
