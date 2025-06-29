'''
age = int(input("Enter your real age: "))

if age >= 18:
    print("You are eligible to have credit card")
else:
    print("You are NOT eligible")
'''

response = input("Do you have any question/s? (Y/N): ")

if response == "Y":
    print("What is your question?: ")
elif response == "N":
    print("You are good to go!")
else:
    print("Try again!")