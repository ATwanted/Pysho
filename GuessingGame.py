import random
x = random.randint(0, 100)

playAgain = True

print("Hello, welcome to Andrew Taylor's first guessing game in Python." + '\n' + "What is your name?")
name = input()
print("Hello, " + name + "!" + " This is a simple guessing game. You have six tries to guess a number between 1 and 100. Good luck!")

while playAgain == True:
  for i in range(6):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == x:
        print("Congratulations! You guessed the number in " + str(i + 1) + " tries!")
        break
    elif guess < x:
        print("Too low. Try again.")
        print("You have " + str(6 - (i+1)) + " tries left.")
    elif guess > x:
        print("Too high. Try again.")
        print("You have " + str(6 - (i+1)) + " tries left.")

  if guess != x and i == 5: print("Sorry, you ran out of tries. The number was " + str(x))
  print("Would you like to play again?")
  playAgain = input()

  if playAgain == "yes" or playAgain == "y":
    playAgain = True
    i == 0
  elif playAgain == "no" or playAgain == "n":
    playAgain = False

print("Thanks for playing!")






