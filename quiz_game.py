print("Welcome to the Quiz Game!!!")

playing = input("Do you want to play? yes/no ")

if playing.lower() != "yes":
    quit()
print("Let's play!")

score = 0
answer = input("What's the full form of CPU? ")
if (answer.lower()).strip() == "central processing unit":
    score += 1
    print("Correct! Your current score is: {}".format(score))
else:
    print("Wrong answer")

answer = input("What's the full form of GPU? ")
if (answer.lower()).strip() == "graphics processing unit":
    score += 1
    print("Correct! Your current score is: {}".format(score))
else:
    print("Wrong answer")

answer = input("What's the full form of RAM? ")
if (answer.lower()).strip() == "random access memory":
    score += 1
    print("Correct! Your current score is: {}".format(score))
else:
    print("Wrong answer")

answer = input("What's the full form of PSU? ")
if (answer.lower()).strip() == "power supply":
    score += 1
    print("Correct! Your current score is: {}".format(score))
else:
    print("Wrong answer")

answer = input("What's the full form of PC? ")
if (answer.lower()).strip() == "personal computer":
    score += 1
    print("Correct! Your current score is: {}".format(score))
else:
    print("Wrong answer")

print("Your answered {} questions correctly!".format(str(score)))
print("Your score is {}%!".format(str((score / 5) * 100)))

