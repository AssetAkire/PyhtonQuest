import math

# Write the code ↓ to read the radius and height of a cylinder from the user.
print("HYPOTENUSE CALCULATOR FOR ALF")
# Be cautious when reading input of various data types.






# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
side1 = float(input("Please, enter the length of side A: "))
while side1 < 0:
    print("Invalid input")
    side1 = float(input("Please, enter the length of side A: "))

side2 = float(input("Please, enter the length of side B: "))
while side2 < 0:
    print("Invalid input")
    side2 = float(input("Please, enter the length of side B: "))
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h





# Write the code ↓ to display the calculated volume with 2 decimal places.
hypotenuse = math.sqrt((side1 * side1) + (side2 * side2))

print("The hypotenuse of the right-angled triangle is: %.2f" %(hypotenuse))
# Select and employ a string concatenation method based on your personal preference and comfort level.





