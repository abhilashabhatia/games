# Tic-Tac-Toe

Tic-Tac-Toe is a two-player game where both players take turn marking a 3x3 grid with either an **X** or an **O**. The player who is successful in achieving their mark in three consecutive vertical, horizontal or diagonal cells before other player, wins the game. It is a solved game with a forced draw assuming best play from both players. 

## Approach

### Game Play

- Given a grid 3x3, i.e., 3 rows, 3 columns, total 9 cells.
- Player selecting X will get the first play, i.e., will start the game.
- Player claiming a horizontal row or a vertical column or a diagonal line (cells) first, wins the game.
- A draw occurs when either of winning combination is not claimed and all cells have been claimed.
- Cells are depicted by blank spaces
- An empty grid is represented as below:
  
  <p>  |   |  <p>
  <p>---------<p>
  <p>  |   |  <p>
  <p>---------<p>
  <p>  |   |  <p>
- If the first chance is played on cell [1,1], the resultant grid representation is as below:

  <p>  |   |  <p>
  <p>---------<p>
  <p>  | X |  <p>
  <p>---------<p>
  <p>  |   |  <p>

### Winning Combination

- Horizontal row: Claiming a row means all elements in the row are of same sign, either Xs or Os.
  - either all cells of first row, i.e., (0,0), (0,1), (0,2), are claimed by a player before other player.
  - either all cells of second row, i.e., (1,0), (1,1), (1,2), are claimed by a player before other player.
  - either all cells of third row, i.e., (2,0), (2,1), (2,2), are claimed by a player before other player.


- Vertical column: Claiming a column means all elements in the column are of same sign, either Xs or Os.
  - either all cells of first column, i.e., (0,0), (1,0), (2,0), are claimed by a player before other player. 
  - either all cells of second column, i.e., (0,1), (1,1), (2,1), are claimed by a player before other player.
  - either all cells of third column, i.e., (0,2), (1,2), (2,2), are claimed by a player before other player.

- Diagonal: Claiming a diagonal means all elements in the diagonal are of same sign, either Xs or Os.
  - Either all cells in the diagonal, i.e., (0,0), (1,1), (2,2), are claimed by a player before other player.
  - Or all cells in the diagonal, i.e., (0,2), (1,1), (2,0), are claimed by a player before other player.

### Inputs

- Select the sign for Player 1 (**X** or **O**). Player 2 will be assigned next sign.
- At game start, player selecting **X** will be asked to choose a cell. Player needs to provide a coordinate from 9 available coordinates (00,01,02,10,11,12,20,21,22)
- Second chance will be given to player selecting **O**. Second chance will have 8 available coordinates to claim from.
- Each player will be given a chance to pick a coordinate until all 9 cells are claimed.
- An input will be invalid if it is not one of the acceptable coordinates (00,01,02,10,11,12,20,21,22).
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
- Add win predictability for each player based on each chance played.
