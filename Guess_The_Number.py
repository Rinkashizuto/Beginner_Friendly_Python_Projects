import random as rng
import os

STARTING_RANGE_OF_GUESSING = 1
END_RANGE_OF_GUESS = 50

def retry():
    retry = input("Would You Like To Try Again? (y/n)").lower()
    if retry == "y":
      os.system("cls")
      show_menu()
    elif retry == "n":
      print("Thank You")
      return False
    else:
      print("Error")

def show_end_results(score, attempts):
  print(f"Score : {score}")
  print(f"Attempts : {attempts}")
  if score == 100:
    print("First Try")
  if score <= 80 and score <= 50:
    print("Great!")
  if score <= 50:
    print("Nice!")

def create_line():
  for i in range(30):
    print("-", end="")
  print()

def guess_checker(guess, rng_number):
  if rng_number == guess:
    return True
  elif guess <= rng_number:
    print("Your Guess Is Lower Than The Number")
  elif guess >= rng_number:
    print("Your Guess Is Higher Than The Number")

def show_menu():
    create_line()
    print("Number Guessing Game")
    create_line()
    print("1. Easy")
    print("2. Intermediate")
    print("3. Hard")
    option = int(input("Chose The Difficulty (1-3) : "))
    choices = (1,2,3)
    if option in choices:
     start_game(option)
    else:
      print("Please Choose Only From The Following Options!")
    os.system("cls")

def start_game(option):
  lives = None
  score = 100
  attempt = 0
  match option:
    case 1:
      lives = 10
      difficulty = "Easy"
    case 2:
      lives = 5
      difficulty = "Intermediate"
    case 3:
      lives = 3
      difficulty = "Hard"
  print(f"Difficulty : {difficulty}")
  print(f"Lives : {lives}")
  random_number = rng.randint(STARTING_RANGE_OF_GUESSING,END_RANGE_OF_GUESS)
  while True:
   guessed_number = int(input(f"Guess The Number ({STARTING_RANGE_OF_GUESSING}-{END_RANGE_OF_GUESS}) "))
   checker = guess_checker(guess=guessed_number, rng_number=random_number)
   print(random_number)
   if checker != True:
     lives -= 1
     attempt += 1
     score -= 10
     print(f"Life : {lives}")
     if lives <= 0:
       print("You Ran Out Of Lives!")
       again = retry()
       if again == False:
         break
   elif checker == True:
     show_end_results(attempts=attempt,score=score)
     again = retry()
     if again == False:
       break

show_menu()