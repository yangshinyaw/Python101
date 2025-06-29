import math

'''
radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")
'''

'''
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)

print(f"The area is: {round(area, 2)}")
'''

value_a = int(input("Enter the value of a: "))
value_b = int(input("Enter the value of b: "))

a_power = pow(value_a, 2)
b_power = pow(value_b, 2)

value_c = math.sqrt(a_power + b_power)

print(f"The square root is: {value_c}")