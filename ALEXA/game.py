import random
def get_choices():
    """Gets the player's choice and a random computer choice."""
    player_choice = input("Enter you choice(rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    # Input validation for player's choice
    while player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        choices = {"player": player_choice, "computer": computer_choice}
        return choices

    def determine_winner(player_choice, computer_choice):
        """Determines the winner of the game."""
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
                (player_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "Computer wins!" 
    def play_game():
        """Plays a round of Rock, Paper, Scissors."""
        print("Welcome to Rock, Paper, Scissors!")

        while True:
            choices = get_choices()
            player_choices["player"]
            computer_choice = choices["computer"]

            result = determine_winner(player_choice, computer_choice)
            print(result)

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            print("Thanks for playing!")

            if __name__ == "__main__":
                play_game()   

