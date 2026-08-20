# AI Tic Tac Toe

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/AI-Minimax-purple)]()
[![Optimization](https://img.shields.io/badge/Optimization-Alpha--Beta-orange)]()

**AI Tic Tac Toe** is a command-line Tic-Tac-Toe game written in Python where a human player competes against an AI opponent. The AI uses the **Minimax algorithm with Alpha-Beta pruning** to evaluate possible game states and select the best available move.

The player controls `O`, while the AI controls `X`. The game runs on a standard 3×3 board and automatically detects wins, losses, and ties. fileciteturn2file1L3-L6

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Architecture Diagram](#architecture-diagram)
- [Project Flow Diagram](#project-flow-diagram)
- [Game Rules](#game-rules)
- [AI Algorithm](#ai-algorithm)
- [Key Components](#key-components)
- [Setup & Installation](#setup--installation)
- [Running the Game](#running-the-game)
- [Gameplay](#gameplay)
- [Troubleshooting](#troubleshooting)
- [Potential Improvements](#potential-improvements)

---

## Overview

The game uses a 3×3 board represented as a nested Python list.

```text
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
```

The human player uses:

```text
O
```

and the AI uses:

```text
X
```

The player enters a number from `1` to `9` to select a board position. fileciteturn2file1L80-L96

---

## Features

### Human vs AI

The user plays against an automated opponent.

### Minimax AI

The AI recursively evaluates possible future game states and chooses the move with the highest evaluation.

### Alpha-Beta Pruning

Alpha-Beta pruning reduces unnecessary branches of the Minimax search tree.

### Win Detection

The game checks:

- Rows
- Columns
- Main diagonal
- Opposite diagonal

for a winning combination. fileciteturn2file1L17-L26

### Tie Detection

The game detects when every board position is occupied without a winner.

### Input Validation

The program rejects:

- Numbers outside `1–9`
- Non-numeric input
- Already occupied cells

---

## Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Interface | Command Line |
| AI Algorithm | Minimax |
| Search Optimization | Alpha-Beta Pruning |
| External Dependencies | None |

---

## Project Structure

```text
AI_Tic_Tac_Toe/
│
├── Tic_Tac_Toe.py       # Complete game and AI implementation
└── README.md             # Project documentation
```

---

## Architecture Diagram

```text
+-------------------------+
|       Human Player      |
|          O              |
+------------+------------+
             |
             v
+-------------------------+
|      Player Input       |
|        1 - 9            |
+------------+------------+
             |
             v
+-------------------------+
|       Game Board        |
|         3 x 3           |
+------------+------------+
             |
             +-----------------------+
             |                       |
             v                       v
+--------------------+     +----------------------+
|   Win / Tie Check  |     |      AI Player       |
+--------------------+     |         X            |
                           +----------+-----------+
                                      |
                                      v
                           +----------------------+
                           |    Best Move Search  |
                           | Minimax + Alpha-Beta |
                           +----------+-----------+
                                      |
                                      v
                           +----------------------+
                           |    Updated Board     |
                           +----------------------+
```

---

## Project Flow Diagram

```text
Start Game
   │
   ▼
Create Empty 3×3 Board
   │
   ▼
Display Board
   │
   ▼
Human Player Move (O)
   │
   ▼
Check Winner / Tie
   │
   ├── Player Wins ──► End
   │
   ├── Tie ──────────► End
   │
   ▼
AI Calculates Best Move
   │
   ▼
Minimax Search
   │
   ├── Alpha-Beta Pruning
   │
   ▼
AI Move (X)
   │
   ▼
Check Winner / Tie
   │
   ├── AI Wins ──────► End
   │
   ├── Tie ──────────► End
   │
   ▼
Display Board
   │
   ▼
Next Player Turn
```

---

## Game Rules

The board contains nine positions.

The player selects a position using:

```text
1 2 3
4 5 6
7 8 9
```

A player wins by placing three of their symbols in:

- A horizontal row
- A vertical column
- The main diagonal
- The opposite diagonal

The implementation checks all of these cases. fileciteturn2file1L17-L26

---

## AI Algorithm

### Minimax

The AI uses Minimax to evaluate possible future moves.

The scoring system is:

```text
AI X wins   → 10 - depth
Player O wins → depth - 10
Tie         → 0
```

This encourages the AI to win as quickly as possible while delaying a loss. fileciteturn2file1L31-L37

### Maximizing Player

The AI (`X`) is the maximizing player.

For every empty cell, the algorithm:

1. Places `X`.
2. Recursively evaluates the resulting state.
3. Restores the cell.
4. Keeps the highest score.

### Minimizing Player

The human player (`O`) is treated as the minimizing player during search.

The algorithm:

1. Places `O`.
2. Recursively evaluates the state.
3. Restores the cell.
4. Keeps the lowest score.

### Alpha-Beta Pruning

The implementation maintains:

```text
alpha
beta
```

and stops exploring a branch when:

```text
beta <= alpha
```

This reduces the number of game states that must be evaluated. fileciteturn2file1L39-L64

---

## Key Components

### `print_board()`

Displays the current 3×3 game board in the terminal.

### `is_winner()`

Checks all rows, columns, and diagonals for a winning combination.

### `is_full()`

Returns whether every board position is occupied.

### `minimax()`

Recursively evaluates possible game states using Minimax and Alpha-Beta pruning.

### `best_move()`

Tests every available AI move and selects the move with the highest Minimax evaluation. fileciteturn2file1L66-L78

### `player_move()`

Reads and validates the player's input.

The player must enter a number from `1` to `9`, and the selected cell must be empty.

### `ai_move()`

Calls `best_move()` and places `X` on the selected position.

### `play_game()`

Controls the main game loop:

```text
Player Move
    ↓
Check Result
    ↓
AI Move
    ↓
Check Result
    ↓
Repeat
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/KavanAnselm/AI_Tic_Tac_Toe.git
cd AI_Tic_Tac_Toe
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

No third-party Python packages are required.

The program uses Python's built-in functionality, including `random`, although the current AI implementation does not depend on random move selection.

---

## Running the Game

```bash
python Tic_Tac_Toe.py
```

The board is displayed and the program prompts:

```text
Enter your move (1-9):
```

Enter a number corresponding to the desired empty cell.

---

## Gameplay

The human player is:

```text
O
```

The AI is:

```text
X
```

After the human move, the AI calculates its best move and displays:

```text
AI is making its move...
```

The game ends when:

```text
Player O (You) wins!
```

or:

```text
AI (Player X) wins!
```

or:

```text
It's a tie!
```

fileciteturn2file1L103-L125

---

## Troubleshooting

### Invalid input

Enter only an integer between:

```text
1 and 9
```

### Cell already occupied

Choose another position if the selected cell already contains `X` or `O`.

### AI takes time to move

Minimax evaluates future game states recursively. Alpha-Beta pruning reduces the search, but the implementation still performs a full game-tree search appropriate to Tic-Tac-Toe.

---

## Potential Improvements

- Add difficulty levels.
- Add a random/easy AI mode.
- Allow the player to choose `X` or `O`.
- Add replay functionality without restarting the program.
- Add a GUI using Tkinter, Pygame, or a web interface.
- Track wins, losses, and draws.
- Add unit tests for game-state evaluation.
- Improve the AI architecture by separating game logic from user-interface code.
