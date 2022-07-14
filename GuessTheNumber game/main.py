#Vedanth M 
#Guessing a number game in python
import random
randNum = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNum):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNum):
        print("You guessed it right!")
    else:
        if(userGuess>randNum):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
