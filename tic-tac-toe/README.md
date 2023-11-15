# Tic-Tac-Toe

Tic-Tac-Toe is a two-player game where both players take turn marking a 3x3 grid with either an **X** or an **O**. The player who is successful in achieving their mark in three consecutive vertical, horizontal or diagonal cells before other player, wins the game. It is a solved game with a forced draw assuming best play from both players. 

## Approach

### Game Play

- Given a grid 3x3, i.e., 3 rows, 3 columns, total 9 cells.
- Player selecting X will get the first play, i.e., will start the game.
- Player claiming a horizontal row or a vertical column or a diagonal line (cells) first, wins the game.
- A draw occurs when either of winning combination is not claimed and all cells have been claimed.
- Cells are depicted by numbers 1,2,3,4,5,6,7,8,9
- An empty grid is represented as below:
  
  <p>1 | 2 | 3<p>
  <p>4 | 5 | 6<p>
  <p>7 | 8 | 9<p>
- If the first chance is played on cell 5, the resultant grid representation is as below:

  <p>1 | 2 | 3<p>
  <p>4 | X | 6<p>
  <p>7 | 8 | 9<p>

### Winning Combination

- Horizontal row: Claiming a row means all elements in the row are of same sign, either Xs or Os.
  - either all cells of first row (1,2,3), i.e., (0,0), (0,1), (0,2), are claimed by a player before other player.
  - either all cells of second row (4,5,6), i.e., (1,0), (1,1), (1,2), are claimed by a player before other player.
  - either all cells of third row (7,8,9), i.e., (2,0), (2,1), (2,2), are claimed by a player before other player.


- Vertical column: Claiming a column means all elements in the column are of same sign, either Xs or Os.
  - either all cells of first column (1,4,7), i.e., (0,0), (1,0), (2,0), are claimed by a player before other player. 
  - either all cells of second column (2,5,8), i.e., (0,1), (1,1), (2,1), are claimed by a player before other player.
  - either all cells of third column (3,6,9), i.e., (0,2), (1,2), (2,2), are claimed by a player before other player.

- Diagonal: Claiming a diagonal means all elements in the diagonal are of same sign, either Xs or Os.
  - Either all cells in the diagonal represented by (1,5,9), i.e., (0,0), (1,1), (2,2), are claimed by a player before other player.
  - Or all cells in the diagonal represented by (3,5,7), i.e., (0,2), (1,1), (2,0), are claimed by a player before other player.

### Inputs

- Select the sign for Player 1 (**X** or **O**). Player 2 will be assigned next sign.
- At game start, player selecting **X** will be asked to choose a cell. Player needs to provide a number from 9 available digits (1,2,3,4,5,6,7,8,9)
- Second chance will be given to player selecting **O**. Second chance will have 8 available digits to claim from.
- Alternatively, each place will be given a chance to pick a digit until all 9 cells are claimed.
- An input will be invalid if it is not one of the acceptable numbers (1,2,3,4,5,6,7,8,9). Characters not in the range above will be invalid including spaces, special characters.
- Player can exit the game by typing character "***e***" or "***E***"

### Game End

- Game ends when:
  - there is a win. A player claims a row, column or diagonal before another player.
  - all cells are claimed resulting in a win or draw on the last cell.
  - player exits the game

## TODO

- Improve the solution to add game play options: computer player 1 & 2 play, human vs computer play
- Add early draw prediction when no more inputs would win the game
- Add levels of ease for human vs computer play

