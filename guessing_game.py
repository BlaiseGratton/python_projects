import random

def repeat():
  print("To play again, type PLAY")
  response = input("> ")
  if response == "PLAY":
    game()
  
def game():
  rand = random.randint(1, 10)
  guesses = 0
  guessed = 0;
  
  print("Welcome to the Number Guessing Game.")
  
  while guessed != rand:
    if guesses == 5:
      print("You ran out of guesses! The number was {}.".format(rand))
      break
      
    print("Guesses remaining: {}".format(5 - guesses))
    guessed = input("Please guess a whole number from 1 to 10: ")
    guessed = int(guessed)
    
    if guessed == rand:
      print("Congratulations! {} is the right number!".format(guessed))
      break
      
    if guessed > rand:
      print("The random number is lower!")
      guesses = guesses + 1
      continue
      
    if guessed < rand:
      print("The random number is higher!")
      guesses = guesses + 1
      continue
      
game()

repeat()
