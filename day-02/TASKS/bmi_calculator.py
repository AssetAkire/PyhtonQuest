# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
print("Simple Calculator for Alf")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")
result = 0.0
# Be cautious when reading input of various data types.









# Write the code ↓ to perform the calculations of user's BMI and categorize its status.

if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2
elif operator == 'x':
    answer = num1 * num2
elif operator == '/':
    answer = num1 / num2
else:
    print("Invalid input")






# Write the code ↓ to display the user's BMI and its classification.
print("The result of %.2f %s %.2f is %.2f" %(num1, operator, num2, result))

# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.







