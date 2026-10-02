#A Python program that asks for two numbers, then subtracts the second one from the first one and prints the entire calculation.

first_number = float(input("Provide the number to subtract from: "))
second_number = float(input("Provide a number to be subtracted from the first one: "))

result = first_number - second_number

print(f"{first_number} - {second_number} = {result}")