#Python calculator

'''
operator = input("Enter an operator (+ - * /): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 /num2)
else:
    print(f"{operator} is not valid")
'''

#Weight Conversion

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid")


