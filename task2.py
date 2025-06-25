# Task2: String Slicing & Simple Calculator


full_name = input("Enter your full name (first and last): ").strip()

# Finding space for slicing first and last name
space_index = full_name.find(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index+1:]

print(f"First name: {first_name}")
print(f"Last name: {last_name}")

# Take two numeric inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Results
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")