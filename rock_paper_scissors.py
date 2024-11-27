import random

# Print the rules of the game
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

# Function to get the choice from the player
def get_choice(player):
    print(f"Enter {player}'s choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    # Take the input from user and loop until valid choice is entered
    choice = int(input(f"{player}, Enter your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input(f"Enter a valid choice for {player} please ☺: "))
    
    # Convert choice into a string (Rock, Paper, or Scissors)
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissors'

# Function to decide the winner between two choices
def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "DRAW"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        return 'User'
    else:
        return 'Computer'

# Function to play the game against computer
def play_against_computer():
    # Get user choice
    user_choice = get_choice("User")

    # Computer randomly selects a choice
    comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    
    # Print choices
    print(f"User choice is: {user_choice}")
    print(f"Computer choice is: {comp_choice}")
    
    # Decide the winner
    winner = decide_winner(user_choice, comp_choice)
    
    # Print the result
    if winner == "DRAW":
        print("<== It's a tie! ==>")
    elif winner == "User":
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

# Function to play the game between two players
def play_against_player():
    # Get choices for both players
    player1_choice = get_choice("Player 1")
    player2_choice = get_choice("Player 2")
    
    # Print the choices
    print(f"Player 1 choice is: {player1_choice}")
    print(f"Player 2 choice is: {player2_choice}")
    
    # Decide the winner
    winner = decide_winner(player1_choice, player2_choice)
    
    # Print the result
    if winner == "DRAW":
        print("<== It's a tie! ==>")
    elif winner == "User":
        print("<== Player 1 wins! ==>")
    else:
        print("<== Player 2 wins! ==>")

# Main game loop
while True:
    # Ask if the user wants to play against the computer or another player
    print("Choose the game mode: \n 1 - Play against Computer \n 2 - Play against Player 2")
    mode = int(input("Enter your choice: "))
    
    # Validate the mode choice
    while mode not in [1, 2]:
        mode = int(input("Please choose a valid option (1 or 2): "))
    
    if mode == 1:
        # Play against the computer
        play_against_computer()
    else:
        # Play against another player
        play_against_player()
    
    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thank you so much for playing!")
