import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors GAME!")
    
    while True:
        print("\n Your choice: rock, paper and scissors")
        user_choice = input("Enter your choice(or 'quit' to exit): ")
        
        if user_choice == "quit":
            print("Thanks for playing!")
            print(f"Your final score:{user_score}, Computer's final score: {computer_score}")
        
        if user_score not in choices:
            print("Invalid value. Please choose from rock, paper and scissors.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if computer_choice == user_choice:
            print("It is a Tie!")
            continue
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper") :
                print("You won this round!")
                user_score += 1
        else:
            print("Computer won this round!")
            computer_score += 1
if __name__ == "__main__":
    rock_paper_scissors()
        