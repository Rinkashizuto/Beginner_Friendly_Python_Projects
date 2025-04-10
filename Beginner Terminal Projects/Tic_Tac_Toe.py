import random as rng

cell = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

characters = ("X", "O")

def display_board():
  print("-------------")
  print(f"| {cell[1]} | {cell[2]} | {cell[3]} |")
  print("-------------")
  print(f"| {cell[4]} | {cell[5]} | {cell[6]} |")
  print("-------------")
  print(f"| {cell[7]} | {cell[8]} | {cell[9]} |")
  print("-------------")

def player_choice():
  choice = int(input("Choose (1-9) "))
  if cell[choice] == " ":
    cell[choice] = characters[0]
  else:
    print("Occupied! Choose Again!")
    player_choice()

def get_empty_cells():
  return [i for i in range(1,10) if cell[i] == " "]

def computer_choice():
  empty_cells = get_empty_cells()
  random_choice = rng.choice(empty_cells)
  if random_choice in cell:
    cell[random_choice] = characters[1]
    
def check_winner():
  winning_combinations = [(1,2,3),
                        (4,5,6),
                        (7,8,9),
                        (2,5,8),
                        (3,6,9),
                        (1,5,9),
                        (3,5,7)
                        ]
  for combinations in winning_combinations:
    if cell[combinations[0]] == cell[combinations[1]] == cell[combinations[2]] and cell[combinations[0]] != " ":
      return cell[combinations[0]]
  return None

while True:
  display_board()
  player_choice()
  winner = check_winner()
  if winner:
     display_board()
     print(f"{winner} wins!")
     break

  computer_choice()
  winner = check_winner()
  if winner:
        display_board()
        print(f"{winner} wins!")
        break

    # Check for a draw
  if not get_empty_cells():
     display_board()
     print("It's a draw!")
     break