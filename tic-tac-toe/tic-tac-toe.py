# Tic Tac Toe
import ast

def print_board(board):
  for row in board:
    print("|".join(row))
    print("-----")
  
def sign_allocation():
  signs = {}
  while True:
    player1_symbol = input("Player, choose your symbol (X or O)").upper()
    if player1_symbol != "X" and player1_symbol != "O":
      print("invalid symbol!")
      continue
    else:
      player2_symbol = "O" if player1_symbol == "X" else "X"
      print("player selecting X gets first chance")
      signs = {"player1": player1_symbol, "player2": player2_symbol}
      break
    
  return signs
  
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  print_board(board)
  signs = {}
  signs = sign_allocation()
  player1 = signs["player1"]
  player2 = signs["player2"]
  current_symbol = signs["player1"] if signs["player1"] == 'X' else signs["player2"]
  
  while True:
    print_board(board)
    
    # Accept coordinates 
    while True:
      try:
        row,col = input(f"Player {current_symbol}, enter row and col from list (00,01,02,10,11,12,20,21,22) : ")
        if ast.literal_eval(row) not in range(3) or ast.literal_eval(col) not in range(3):
          print("invalid entry")
          continue
        else:
          row = int(row)
          col = int(col)
          break
      except ValueError as e:
        print ("Cannot be a string")
        continue
    
    # Check board status
    if board[row][col] == ' ':
      board[row][col] = current_symbol
      
      if check_winner(board, current_symbol):
        print_board(board)
        print(f"Player {current_symbol} wins!")
        break
      elif is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break
      else:
        current_symbol = player2 if current_symbol == player1 else player1
    else:
      print("That cell is already taken. Try again.")
    

tic_tac_toe()