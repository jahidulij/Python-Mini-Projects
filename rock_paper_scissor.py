import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/ paper/ scissors or q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_choose = options[random_number]

    if user_input == computer_choose:
        print("It's a draw")
    elif user_input == "rock" and computer_choose == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_choose == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_choose == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost :(")
        computer_wins += 1
    print("Your score: {}".format(user_wins))
    print("Computer's score: {}".format(computer_wins))

print("You won {} times".format(user_wins))
print("Computer won {} times".format(computer_wins))
if user_wins > computer_wins:
    print("Congratulations! You Won!!!")
elif user_wins < computer_wins:
    print("Sorry! Computer won. Good luck next time.")
else:
    print("Series draw.")
print("Goodbye!")
