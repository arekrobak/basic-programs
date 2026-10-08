#A Python program that asks for two numbers, the multiplies the first one by the second one and prints the entire calculation.

first_number = float(input("Provide the first number in the multiplication of two numbers: "))
second_number = float(input("Provide the second number in the multiplication of two numbers: "))

result = first_number * second_number

print(f"{first_number:g} * {second_number:g} = {result:g}")