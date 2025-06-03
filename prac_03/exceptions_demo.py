""" CP1404/CP5632 - Practical
 """
"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
--- when the input is not an integer number
2. When will a ZeroDivisionError occur?
--- when denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
--- Yes, I changed the code
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator==0:  #added part
        print("Denominator cannot be 0") #added
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")