# Write the code ↓ to read user's input.
print("PUP Enrollment Form")
user_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
GWA = float(input("Enter your previous average: "))
is_cloudArchitect = input("Are you a member of the AWS Cloud Club - Department of Cloud Computing? (yes/no): ").lower() == "yes"
# Be cautious when reading input of various data types.






# Write the code ↓ to display the user's personal information.
print("\nPersonal Information:")
print(f"Name: {user_name}")
print(f"Age: {age} years")
print(f"Previous average: {GWA:.2f}")
if is_cloudArchitect:
    print("AWS Cloud Club Member: Yes")
else:
    print("AWS Cloud Club Member: No")
# Select and employ a string concatenation method based on your personal preference and comfort level.





