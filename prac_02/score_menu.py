""" Do from scratch exercises - Menu """
menu = """ Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """ Display menu and do tasks according the input """
    score = 0
    print(menu)
    choice = input("Enter your choice: ").upper()
    while choice!= 'Q':
        if choice == 'G':
            score = get_valid_score("Enter your score: ", 0, 100)
        elif choice == 'P':
            grade = get_score_result(score)
            print(grade)

        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid Choice")
        choice = input("Enter your choice: ").upper()
    print("Farewell")

def get_valid_score(prompt, low, high):
    """ Get valid score """
    marks = int(input(prompt))
    while marks < low or marks > high:
        print("Invalid score")
        marks = int(input(prompt))
    return marks

def show_stars(score):
    """Show stars according to score """
    for i in range (score):
        print("*", end='')
        print()

def get_score_result(score):
    """ Get result from the score """
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
    
