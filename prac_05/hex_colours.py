"""
CP1404/CP5632 Practical
Intermediate exercises
"""
COLOR_TO_CODE = {
    "ABSOLUTE ZERO": "#0048ba",
    "ALICEBLUE": "#fof8ff",
    "AQUA": "00ffff",
    "BLACK": "000000",
    "BLOND": "faf0be",
    "BROWN": "a52a2a",
    "CAMEL": "c196ab",
    "CHOCOLATE": "d2691e",
    "MANGO": "fdbe02",
    "MINT": "3eb489"
}
print(COLOR_TO_CODE)
color_name = input("Enter color name: ").upper()
while color_name != "":
    try:
        print(f"The code for {color_name} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").upper()