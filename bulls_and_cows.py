import random


def generate_secret_code():
    while True:
        code = str(random.randint(1000, 9999))
        if len(set(code)) == 4:
            return code


def generate_hint(secret_code, guess):
    bulls = sum(secret_code[i] == guess[i] for i in range(4))
    secret_code_digits = set(secret_code)
    cows = len(secret_code_digits.intersection(guess)) - bulls
    return bulls, cows


def play_game(tries):
    secret_code = generate_secret_code()
    print("Guess the secret code, a 4-digit number with no repeated digits.")
    num_tries = 0
    while num_tries < tries:
        guess = input("Enter your guess: ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid guess. Please enter a 4-digit number with no repeated digits.")
            continue
        num_tries += 1
        bulls, cows = generate_hint(secret_code, guess)
        if bulls == 4:
            print("Congratulations! You guessed the secret code in", num_tries, "tries.")
            return
        else:
            print(bulls, "bulls,", cows, "cows")
            print("You have", tries - num_tries, "tries remaining.")
    print("Sorry, you ran out of tries. The secret code was", secret_code)


print("Welcome to the cows and bulls game!")
while True:
    tries = int(input("How many tries do you want? "))
    play_game(tries)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break