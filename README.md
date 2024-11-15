Blindfold chess game in python.

Download stockfish and put the executable in the folder and name it stockfish_15.exe

Run python main.py
Select colour
Select difficulty
Enter your moves via text input and the computer will give its move after yours.

Uses Stockfish 15 which can be found at https://stockfishchess.org/

Example output:

    Welcome to Blindfold Chess
    Play as (w)hite, (b)lack, (r)andom: w
    You are playing as White.
    Enter difficulty level (1 to 10): 1
    Level 1 difficulty chosen.
    Enter move: e4
    White (Player) moves e4
    Black (Engine) moves e6
    Enter move: f4
    White (Player) moves f4
    Black (Engine) moves d5
    Enter move: exd5
    White (Player) moves exd5
    Black (Engine) moves exd5
    Enter move: Nf3
    White (Player) moves Nf3
    Black (Engine) moves Nf6
    Enter move:
    
On Ubuntu you may need to specify the absolute path to stockfish_15.exe in main.py

On Ubuntu you may need to change permissions to execute stockfish.exe, e.g. by running: 

```
chmod +rwx stockfish_15.exe
```

### Puzzles

Sample puzzle:

```
Puzzle number 1 - Checkmate in 1:

    White: King e6 / Rook a2
    
    Black: King e8
    
Enter your move for White:
```

Correct answer:

```
ra8
```

