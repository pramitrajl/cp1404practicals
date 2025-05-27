"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 10
    else:
        bonus_rate = 15
    bonus =  (bonus_rate/100)* sales
    print (f"your bonus is ${bonus:.0f}")
    sales = float(input("Enter sales: $"))