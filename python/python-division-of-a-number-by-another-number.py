#A Python program that asks for two numbers, the divides the first one by the second one and prints the entire calculation.

first_number = float(input("Provide the number to be divided: "))
second_number = float(input("Provide the number to didive the first number by: "))

result = second_number / first_number

print(f"{second_number:g} / {first_number:g} = {result:}")