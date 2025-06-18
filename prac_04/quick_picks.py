"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""
import random
MIN_NUM = 1
MAX_NUM = 45
NUMBERS_PER_PICK = 6
quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUM, MAX_NUM)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(" ".join(f"{num:2}" for num in numbers))
