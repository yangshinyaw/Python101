# compound interest calculator

principal_balance = 0
interest_rate = 0
time_periods = 0

while principal_balance <= 0:
    principal_balance = float(input("Enter a valid number: "))
    if principal_balance <= 0:
        print("The value can't be 0 or less than")

while interest_rate <= 0:
    interest_rate = float(input("Enter a valid number: "))
    if interest_rate <= 0:
        print("The value can't be 0 or less than")

while time_periods <= 0:
    time_periods = float(input("Enter a valid number: "))
    if time_periods <= 0:
        print("The value can't be 0 or less than")

total = principal_balance * pow(1 + interest_rate/100, time_periods)

print(principal_balance)
print(interest_rate)
print(time_periods)
print(f"The balance after {time_periods} years: ${total:.2f}")
    