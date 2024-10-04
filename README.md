# Minesweeper Game

## Overview
The Minesweeper game I created uses the Pygame library. It's pretty fun to play and includes some cool features. I used graph algorithms like BFS and DFS to help reveal the necessary empty spaces when you click on a safe tile. It was challenging but exciting to put it all together!

## Features
- **Flag Placement**: Users can flag potential mines on the grid to avoid clicking on them later.
- **Mine Handling**: If the user clicks on a mine at the start of the game, the program automatically transforms the clicked block into a normal block and places the mine in another block.
- **Smooth End Animation**: When a mine is clicked, the game freezes, and the remaining mines are revealed through a smooth animation.

## How to Play
1. Left click on any block to reveal it. If it's a mine, the game will end.
2. Use the flag option(right click) to mark blocks you suspect contain mines.
3. The goal is to reveal all non-mine blocks without triggering any mines.

## Installation
Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/minesweeper.git](https://github.com/razimograbi/Minesweeper.git)
   cd minesweeper
   pip install pygame
   python main.py
   ```
## Screenshots

### Game Start
![Game Start]((https://github.com/razimograbi/Minesweeper/blob/main/MyMinesweeperGame1.png))


### Mid Game
![Mid Game]((https://github.com/razimograbi/Minesweeper/blob/main/MyMinesweeperGame2.png))


### Game Over Screen, You Lost!
![Game Over]((https://github.com/razimograbi/Minesweeper/blob/main/GameOver.png))


   
