# Minesweeper
A good old minesweeper game.

## Description
Currently just created a simple Board Class to create the board.

Spaces are represented by 'S'. Bombs are represented by 'B'. Numbers represent amount of bombs surrounded by.

## Example
To Play, create a game and set difficulty (Easy, Medium, Hard) and use the play function to start.

```python
from minesweeper import Minesweeper

game = Minesweeper('medium')
game.play()


# B 1 1 2 2 1 S S S S
# 1 1 1 B B 3 2 1 1 S
# S S 1 3 B B 2 B 1 S
# S S S 1 2 2 2 1 1 S
# S S S S 1 1 1 S S S
# S S S S 1 B 2 1 1 S
# S S S S 1 1 2 B 2 1
# S S S S 1 1 2 1 2 B
# 1 1 S S 1 B 1 S 1 1
# B 1 S S 1 1 1 S S S
```
