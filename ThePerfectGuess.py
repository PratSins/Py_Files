import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0
#print(randNumber)
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore2.txt", "r") as f:
    hiscore2 = int(f.read())

if(guesses<hiscore2):
    print("You have just broken the high score!")
    with open("hiscore2.txt", "w") as f:
        f.write(str(guesses))
