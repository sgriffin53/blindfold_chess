

puzzles_mate1 = {
    1: ["    White: King e6 / Rook a2\n    Black: King e8", "ra8", "w"],
    2: ["    White: King g2 / Pawns f2 & g3 / Rook a1\n    Black: Pawns f7 & g7 & h7 / King g8", "ra8", "w"],
    3: ["    White: King h2 / Pawns g3 & h6  / Rook c2\n    Black: Pawns f7 & h7 / King g8", "rc8", "w"],
    4: ["    White: King d3 / Rooks a7 & h1\n    Black: King e8", "rh8", "w"],
    5: ["    White: King c7 / Rook h3\n    Black: King a8 / Pawn b7", "ra3", "w"],
    6: ["    White: King b2 / Pawns c2 & b3 / Rook c1 / Knight d7\n    Black: King a7 / Pawns b7 & c7", "ra1", "w"],
    7: ["    White: King g2 / Rook h1 / Pawn f2 / Bishop f6\n    Black: King g8 / Pawns f7 & g6 / Rook f8", "rh8", "w"],
    8: ["    White: King b3 / Knight c6 / Rook d7\n    Black: King a8 / Bishop c8 / Pawns a7 & b6", "ra7", "w"],
    9: ["    White: King f3 / Rook a8\n    Black: King g1 / Pawn h2", "ra1", "w"],
    10: ["    White: King b3 / Rook c4 / Bishop c6\n    Black: King a6 / Pawns b6 & c7 / Rook c8", "ra4", "w"],
    11: ["    White: King g2 / Rook c8 / Knight f6 / Pawn g5\n    Black: King g7 / Pawns  f7 & g6 & h7", "rg8", "w"],
    12: ["    White: King d6 / Knight e6 / Rook h7\n    Black: King e8", "re7", "w"],
    13: ["    White: King f6 / Queen a2\n    Black: King f8 / Pawn a7", "qf7", "w"],
    14: ["    White: King g6 / Queen a7\n    Black: King g8 / Queen f8", "qh7", "w"],
    15: ["    White: King h4 / Pawn g4 / Queen a8\n    Black: King g6 / Queen f4 / Rook e4 / Pawns f6 & h6", "qg8", "w"],
    16: ["    White: King h2 / Pawns g2 & h3 / Queen b2 / Bishop a1\n    Black: King g8 / Queen e8 / Rook f8 / Pawns f7 & g7 & h7", "qg7", "w"],
    17: ["    White: King c4 / Queen g7 / Pawn b6\n    Black: King a8 / Rook b8", "qa7", "w"],
    18: ["    White: King h7 / Queen a6\n    Black: King h1 / Queen e5 /  Pawns h2 & h3", "qf1", "w"],
    19: ["    White: King b2 / Queen h8\n    Black: King d3 / Queen e4 / Pawn e2", "qc3", "w"],
    20: ["    White: King f2 / Queen b8 / Pawns g3 & h4\n    Black: King g4 / Queen a1 / Pawns g6 & h5", "qc8", "w"],
    21: ["    White: King g1 / Queen c3 / Bishop a4 / Rook e8 / Pawns a3 & b2 & f2 & g2 & h6\n    Black: King f7 / Queen c7 / Rook c8 / Bishop b7 / Pawns a7 & b6 & d5 & e5 & g6 & h7", "qf3", "w"],
    22: ["    White: King g1 / Queen g5 / Bishop b5 / Pawns a6 & b2 & f2 & g3 & h2\n    Black: King f8 / Queen b4 / Rook h6 / Knight c8 / Pawns a7 & b6 & d4 & f7 & g7 & h3", "qd8", "w"],
    23: ["    White: King g1 / Queen a5 / Rook d7 / Pawns a2 & c3 & f2 & g2 & h4\n    Black: King f6 / Queen e4 / Rooks c4 & h8 / Pawns a6 & b7 & e6 & g6 & h7", "qg5", "w"],
    24: ["    White: King b5 / Queen c8 / Bishop a1 \n    Black: King d5 / Queen g1 / Pawn a3", "qc6", "w"]
    }
    

def run_puzzles(puzzles_mate1):
    for puzzle_num in puzzles_mate1.keys():
        print(f"\nPuzzle number {puzzle_num} - Checkmate in 1:")
        print(puzzles_mate1[puzzle_num][0])

        correct_result = puzzles_mate1[puzzle_num][1]
        colour_to_move = puzzles_mate1[puzzle_num][2]
        
        answer_input_str= ""
        while (answer_input_str.lower() != correct_result) and (colour_to_move == "w"):
            answer_input_str = input("Enter your move for White:")
        while (answer_input_str.lower() != correct_result) and (colour_to_move == "b"):
            answer_input_str = input("Enter your move for Black:")  
        print("\n*** Well done! That's the correct answer ***")
        continue_str = " "
        while continue_str != "":
            continue_str = input("Press Enter to continue...")
    print("\nThat's the last puzzle.\n")

