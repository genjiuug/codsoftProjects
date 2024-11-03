#import the library
import random

#get the choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

#winner determining
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

#display result
def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

#play game
def play_game():
    user_score, computer_score = 0, 0

    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to end): ").lower()
        if user_choice == 'quit':
            print("\nGame over!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Current Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank you for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break


play_game()