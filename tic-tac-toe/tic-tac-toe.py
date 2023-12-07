# Tic Tac Toe
  
def print_board(board):
  for row in board:
    print("|".join(row))
    print("-----")

def tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  print_board(board)
  signs = {}
  signs = sign_allocation()
  player1 = signs["player1"]
  player2 = signs["player2"]
  
def sign_allocation():
  player1_symbol = input("Player, choose your symbol (X or O)").upper()
  if player1_symbol != "X" and player1_symbol != "O":
    print("invalid symbol!")
    sign_allocation()
  else:
    player2_symbol = "X" if player1_symbol == "O" else "O"
    print("player selecting X gets first chance")
  return {"player1": player1_symbol, "player2": player2_symbol}
  

tic_tac_toe()