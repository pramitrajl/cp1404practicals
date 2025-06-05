""" P1404/CP5632 - Practical
Do-from-scratch-exercises"""

# #1.
file_name= open("name.txt", "w")
name = input("Enter your name: ")
file_name.write(name)
file_name.close()

# #2.
file_name = open("name.txt", "r")
user_name = file_name.read()
file_name.close()
print(f"Hi {user_name}!")

#3.
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
print(first_number+second_number)

#4.
with open("numbers.txt", "r") as file:
    total=0
    for line in file:
        total += int(line)
print(total)