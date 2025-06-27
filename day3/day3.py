'''
first_name = input("What is your name?: ")
age = int(input("How old are you?: "))

age += 1

print(f"You are {first_name}")
print(f"{age} years old")
'''

'''
#Computation of Area of Rectangle

length = int(input("What is the length of the Rectangle?: "))
width = int(input("What is the width of the Rectangle?: "))

area = length * width

print(f"The Area of the Rectangle is {area}")
'''
#Shopping Cart
item = input("What will you buy on the store: ")
price = float(input("What is the price of the item: "))
quantity = int(input("How many would you like to buy: "))

total_payment = price * quantity

print(f"You've bought {quantity} {item} that's valued ${price} each item")
print(f"Your total bill is ${total_payment}")