""" CP1404/CP5632 Practical
Basic list operations
"""
list_of_numbers = []
for i in range (0,5,1):
    number = int(input("Number:"))
    list_of_numbers.append(number)
print(f"The first number is {list_of_numbers[0]}")
print(f"The last number is {list_of_numbers[-1]}")
print(f"The smallest number is {min(list_of_numbers)}")
print(f"The largest number is {max(list_of_numbers)}")
print(f"The average of numbers is {sum(list_of_numbers)/len(list_of_numbers)}")


