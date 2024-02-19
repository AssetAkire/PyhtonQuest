# Write the code ↓ to read the user's input for a positive integer.
print("PERFECT NUMBER DETERMINATOR FOR ALF")
number = int(input("Please, enter a positive integer: "))
# Be cautious when reading input of various data types.










# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
while number <= 0:
    print("Invalid input")
    number = int(input("Please, enter a non-negative integer: "))
    
result = number

perfect = 0
for i in range(1, number):
    if number % i == 0:
        perfect = perfect + i






# Write the code ↓ to display the Perfect Number check result.
if perfect == result:
    print("%d is a Perfect Number: "%(result))
else:
    print("%d is not a Perfect Number: " %(result))
# NOTE : You can use if-else statement or ternary operator to display the result.






