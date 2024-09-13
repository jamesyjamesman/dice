import random

sides = 0
valid = False
while not valid:
    sides = input("How many sides on your die?\n")
    if sides.isnumeric():
        sides = int(sides) + 1
        if sides == 1:
            print("Cannot enter 0! Try a value of 1 or higher.")
        else:
            valid = True
    else: print("Not a valid input! Try a value of 1 or higher.")

output = random.randrange(1, sides)
print(f"It landed on {output}!")