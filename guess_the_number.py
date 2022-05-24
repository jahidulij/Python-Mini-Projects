import random

number = random.randint(0, 11)

guess_left = 3
score = 0

while guess_left > 0:
    guess_number = int(input("Enter a number between 1 & 10: "))
    if guess_number > 10 or guess_number <= 0:
        print("Please try next time")
        quit()
    else:
        if guess_number == number:
            print("You got it right :D ")
            break
        else:
            if guess_number > number:
                print("Magic number is less than your guess")
            else:
                print("Magic number is higher than your guess")
            guess_left -= 1
            print("You have {} guess left.".format(guess_left))
            continue


