# Create a program that keeps asking the user to guess a number until they get it right. Use while True to loop continuously until the correct number is guessed.

secret_number = 7

while True:
    guess_number = int(input("Enter your guess: "))
    if guess_number != secret_number:
        print("Wrong Guess!")
    else:
        print(f"You got it right! The number is {secret_number}")
        break