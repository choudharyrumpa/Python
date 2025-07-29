import random

def get_user_choice():
    print("Choose one: Stone, Paper, or Scissors")
    choice = input("Your choice: ").strip().lower()
    if choice in ['stone', 'paper', 'scissors']:
        return choice
    else:
        print("Invalid choice! Please choose Stone, Paper, or Scissors.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'stone' and computer == 'scissors') or \
         (user == 'paper' and computer == 'stone') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Stone-Paper-Scissors Game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print("\nResult:", determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
