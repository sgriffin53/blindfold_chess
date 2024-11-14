import chess
import chess.engine
import chess.svg
import os, sys
import random


from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self, board):
        super().__init__()

        self.setGeometry(100, 100, 600, 600)

        self.widgetSvg = QSvgWidget(parent = self)
        self.widgetSvg.setGeometry(10, 10, 580, 580)

        self.chessboard = board

        self.chessboardSvg = chess.svg.board(self.chessboard, orientation=board.turn).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

def showBoard(board):
    app = QApplication([])
    window = MainWindow(board)
    window.show()
    app.exec()

engine_file = "stockfish_15.exe"
if not os.path.exists(engine_file):
    print("Engine file not found:", engine_file)
    sys.exit()

print("Welcome to Blindfold Chess")
puzzle_input_str = ' '
while puzzle_input_str[0].lower() != 'p' and puzzle_input_str[0].lower() != 'g':
    puzzle_input_str = input("Select (g)ame or (p)uzzles: ")
    
if puzzle_input_str == 'p':
    import puzzles 
    puzzles.run_puzzles(puzzles.puzzles_mate1)
    
input_str = ' '
while input_str[0].lower() != 'w' and input_str[0].lower() != 'b' and input_str[0].lower() != 'r':
    input_str = input("Play as (w)hite, (b)lack, (r)andom: ")
in_c = input_str[0]
player_col = 'White'
if in_c == 'b':
    player_col = 'Black'
if in_c == 'r':
    rand_num = random.randint(0,1)
    if rand_num == 1: player_col = 'Black'
print("You are playing as " + player_col + ".")
engine = chess.engine.SimpleEngine.popen_uci(engine_file)
diff = -1
while diff not in range(1,11):
    in_str = input("Enter difficulty level (1 to 10): ")
    if not in_str.isnumeric(): continue
    diff = int(in_str)
engine.configure({"Skill Level": diff})
print("Level", str(diff), "difficulty chosen.")
show_only_last = False
in_str = '-'
while in_str[0].lower() != 'y' and in_str[0].lower() != 'n':
    in_str = input("Show only last move (y/n): ")
if in_str[0].lower() == 'y':
    show_only_last = True
print("Type 'board' at any time to see the current board.")
print("Type 'moves' at any time to see the legal moves.")
print("---")
print("Game begins.")
board = chess.Board()
keep_running = True
while keep_running:
    if board.is_stalemate():
        print("Game drawn by stalemate.")
        break
    if board.is_insufficient_material():
        print("Game drawn by insufficient material.")
        break
    if board.can_claim_fifty_moves():
        print("Game drawn by 50-move rule.")
        break
    if board.can_claim_threefold_repetition():
        print("Game drawn by threefold repetition.")
        break
    if board.is_checkmate():
        col = "White"
        if board.turn: col = "Black"
        winner = "Engine"
        if col == player_col: winner = "Player"
        print(col, "(" + winner + ") wins by checkmate.")
        break
    if (board.turn and player_col == 'White') or (not board.turn and player_col == 'Black'):
        move = input("Enter move: ")
        if move.lower() == "board":
            showBoard(board)
            continue
        elif move.lower() == "moves":
            legal_moves = ""
            for i, legal_move in enumerate(board.legal_moves):
                legal_moves += str(board.san(legal_move)) + " "
            print("Legal moves:", legal_moves)
            continue
        try:
            push = board.push_san(move)
            if show_only_last: os.system("cls")
            print(player_col, "(Player) moves", move)
        except ValueError:
            print(move, "is not a legal move.")
    else:
        col = "White"
        if not board.turn: col = "Black"
        with engine.analysis(board, chess.engine.Limit(time=(1.5))) as analysis:
            for info in analysis:
                pass
        move = analysis.info['pv'][0]
        move_san = board.san(move)
        board.push(move)
        if show_only_last: os.system("cls")
        print(col, "(Engine) moves", str(move_san))
print("Thanks for playing!")
