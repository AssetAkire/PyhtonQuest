# Write the code ↓ to read user's input for two operands and selected operation.
print("SIMPLE CALCULATOR FOR ALF\n")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")
# NOTE: The two operands must be read as floats.









# Write the code ↓ to perform the calculations based on the selected operation.

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "x":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator. Please choose +, -, x, or /.")
    exit()






 
# Write the code ↓ to display the result.
print(f"The result of {num1:.1f} {operator} {num2:.1f} is {result:.1f}")
# Select and employ a string concatenation method based on your personal preference and comfort level.







