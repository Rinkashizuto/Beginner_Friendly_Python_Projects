import random as rng
import time

def main():
  start()

def line():
  for i in range(30):
    print("-",end="")

def start():
  choice = {"R":"Rock", "P":"Paper", "S":"Scissors"}
  line()
  print("\nRock Paper Scissors Game CLI")
  line()
  option = input("\nRock(R) Paper(P), (S)Scissors? : ").upper()
  if option in choice:
    print(f"You have chosen : {choice.get(option)}")
  else:
    print("Error")
  print("Computer chose...")
  time.sleep(0.5)
  print(computer_choice())
  check_results(player_choice=choice.get(option), com_choice=computer_choice())
  show_results(check_results())
  retry()

  
def computer_choice():
  com_choice_list = {"1":"Rock", "2":"Paper", "3":"Scissors"}
  rng_number = rng.randint(1,3+1)
  com_choice = com_choice_list.get(rng_number)
  return com_choice
  
def check_results(player_choice, com_choice):
  if player_choice == "Rock" and com_choice == "Scissor":
    return True
  elif player_choice == "Paper" and com_choice == "Rock":
    return True
  elif player_choice == "Scissors" and com_choice == "Paper":
    return True
  elif player_choice == "Rock" and com_choice == "Rock":
    return "D"
  elif player_choice == "Paper" and com_choice == "Paper":
    return "D"
  elif player_choice == "Scissors" and com_choice == "Scissors":
    return "D"
  
  else:
    return False

def show_results(result):
  if result == True:
    print("Player Wins!")
  elif result == "D":
    print("Its A Draw!")
  else:
    print("Player Loss!")

def retry():
  option = input("Would You Like To Try Again? (y/n): ").upper()
  if option == "Y":
    main()
  elif option == "N":
    print("Thank You!")
    return
  else:
    return

if __name__ == "__main__":
  main()
