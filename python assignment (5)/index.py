'''We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:
1. Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!
2. You make a guess, saying your number is either higher than or lower than the computer's number
3. If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!
4. These steps make up one round of the game. The game is over after all rounds have been played.
'''
import random

def generate_random_number():
    """Generate a random number between 1 and 100 (inclusive)."""
    return random.randint(1, 100)

def play_high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Generate random numbers for the player and computer
    player_number = generate_random_number()
    computer_number = generate_random_number()

    # Initialize player's score
    player_score = 0

    # Play rounds until the game is over
    while True:
        print(f"\nRound {player_score + 1}")
        print(f"Your number is {player_number}")

        # Ask for player's guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Determine the winner of the round
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            player_score += 1
        else:
            print(f"Sorry, the computer's number was {computer_number}. You guessed incorrectly.")

        # Ask if the player wants to play another round
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

        # Generate new random numbers for the next round
        player_number = generate_random_number()
        computer_number = generate_random_number()

    print(f"\nGame over! Your final score: {player_score}")

# Call the function to play the High-Low game
play_high_low_game()
