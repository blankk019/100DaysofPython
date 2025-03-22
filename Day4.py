import random

#ROCK_PAPER_SCISSORS GAME
"""if __name__ == "__main__":
    random_number = random.randint(0, 1)
    if random_number == 1:
        print("Heads")
    else:
        print("Tails")
"""

if __name__ == "__main__":
    import random

# ASCII Art
rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """ 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices
choices = ["rock", "paper", "scissors"]
ascii_art = {"rock": rock, "paper": paper, "scissors": scissors}

# Game Loop
while True:
    # User choice
    user_choice = input("Choose Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye.")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again!")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    # Show choices
    print("\nYou chose:")
    print(ascii_art[user_choice])
    
    print("Computer chose:")
    print(ascii_art[computer_choice])

    # Determine winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    print("\n" + "-"*30 + "\n")
