"""
Shop calculator
CP1404/CP5632 - Practical
"""
total = 0
total_items = int(input("Number of items: "))
while total_items <= 0 :
    print ("Invalid number of items!")
    total_items = int(input("Number of items: "))
for i in range (total_items):
    price = float(input("Price of item: "))
    total += price
if total >=100:
    final_cost = total - (0.1*total)
else:
    final_cost = total
print(f"Total price for {total_items} items is ${final_cost:.2f} ")