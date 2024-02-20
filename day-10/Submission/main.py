import json
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_food = input("Enter your favorite food: ")

user = {
    "name": name,
    "age": age,
    "favorite_food": favorite_food
}

data = json.dumps(user, indent=2)

with open("output.json", "w") as file:
    file.write(data)
