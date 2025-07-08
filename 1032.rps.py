import random 

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    print("Welcome to Rock_paper_scissors GAME!")
    
    while True:
        print("\n Your choices: rock, paper,scissors")
        user_choice = input("Enter your choice (or 'quit'to exit):")
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            print(f"Final scores: You:{user_score}, Computer: {computer_score}")
            
        if user_choice not in choices:
            print("Invalid value. Please choose from 'rock','paper'and 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It is a tie!")
        elif (user_choice == 'rock'and computer_choice == 'scissors') or \
             (user_choice == 'scissors'and computer_choice == 'paper') or \
             (user_choice == 'paper'and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        print(f"Current scores: You: {user_score} ,Computer: {computer_score}") 

if __name__ == "__main__":
    rock_paper_scissors()

