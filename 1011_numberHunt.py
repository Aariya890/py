import random

print("=" * 40)
print("Welcome to the Number Hunt Game!")
print("=" * 40)
print("Instructions: ")
print(" - Guess the number between 1 and 10.")
print(" - You have 5 attempts to guess the correct number.")
print(" - After each guess, you will receive feedback on whether your guess was too high, too low, or correct.")
print(" - enter 'score' to see your score.")
print(" - enter 'exit' or 'quit' anytime to quit the game.")
print(" - If you guess wrong, then you lose 2 point.")
print("=" * 40)

secret_number = random.randint(1, 10)
attempts = 0
score = 0

while True:
    user_input = input("Enter your guess (1-10): ").strip().lower()
    
    if user_input in ['exit', 'quit']:
        print("Thanks for playing! Your final score is:", score)
        break
    elif user_input == 'score':
        print("Your current score is:", score)
        continue
    
    try:
        guess = int(user_input)
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue
        
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
        continue
    attempts += 1
    
    if guess == secret_number:
        score += 10
        print(f"Correct! you guessed the number. Your score is now: {score}")
        print("=" * 40)
        print("\n")
        secret_number = random.randint(1, 10)
        attempts = 0
        continue
    elif guess < secret_number:
        score -= 2
        print(f"Too low! The secret number is higher. Your score is now: {score}")
        
    elif guess > secret_number:
        score -= 2
        print(f"Too high! The secret number is lower. Your score is now: {score}")  
    
    if attempts >= 5:
        print(f"You've used all your attempts! The secret number was: {secret_number}.")
        print("Game over! Your final score is now:", score)
        break
    else:
        print(f"You have {5 - attempts} attempts left.")
        print("=" * 40)