# Guess The Number Game
# You have 6 tries to guess the number the program has randomly selected
# 2022-04-23
# jwillder
import random
print("\t___GUESS THE NUMBER GAME___\n")
name = input("Hi, what is your name?: ")
def main():
  number = random.randint(1,10)
  #print(number)
  goes = 6
  print("\nWell", name, "I'm thinking of a number between 1 and 10.")
  print("You have", goes, "goes to guess it, good luck!\n")
  # Guess loop
  tries = 0
  win = False
  while tries < goes:
    tries = tries + 1
    guess = input("Guess " + str(tries) + ": ")
    if not guess.isdigit():
      tries = tries - 1
      print("You must enter a number")
    else:
      guess = int(guess)
      if guess == number:
        win = True
        break
      else:
        # As long as it's not the last try, print if too high or low
        if tries != goes:
          if guess < number:
            print("Try higher")
          else:
            print("Try lower")
          
  # Display if won or failed
  if win == True:
    print("\nCongratulations, you guessed correctly in", tries, "tries!")
  else:
    print("\nBad luck, you didn't guess it, I was thinking of the number " + str(number) + ".")
  # Ask to play again
  again = input("\nWould you like to play again? (y/n) : ")
  if again == "y" or again == "Y":
    main()
  else:
    return 0
  
main()