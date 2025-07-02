#while loop
'''
name = input("Enter your name: ")

while name == "":
    print("Please enter your name!")
    name = input("Enter your name: ")
print(f"Hello {name}, Welcome to the System!")
'''

'''
age = int(input("How old are you: "))

while age < 0:
    print("Not valid age!")
    age = int(input("How old are you: "))
print(f"You are {age} years old")
'''

food = input("Enter your favorite food (Q to quit): ")

while not food == "Q":
    print(f"You like {food}")
    food = input("Enter your favorite food (Q to quit): ")
print("Good Bye, See you again!")



