from stockfish import Stockfish

def getPossible(moves):
    try:
        return stinkfish.get_top_moves(moves)
    except:
        getPossible(moves-1)           # I don't know how to recursion


def getWorst(turn, moves):
    worst = 0
    for index, d in enumerate(moves):
        if turn == "w":
            if d["Centipawn"] < moves[worst]["Centipawn"]:
                worst = index
        elif turn == "b":
            if d["Centipawn"] > moves[worst]["Centipawn"]:
                worst = index

    return moves[worst]["Move"]


def evaluate(Centipawn):
    if Centipawn > 0:
        return "WHITE"
    elif Centipawn == 0:
        return "EQUAL"
    else:
        return "BLACK"


stinkfish = Stockfish() # READ BELOW YOU WILL GET AN ERROR HERE
# ^^^ If you already have the Stockfish Engine installed enter the path of the stockfish executable inside the parentheses
# IF NOT, INSTALL STOCKFISH

fen = "r1bqk2r/pp1p1ppp/n3pn2/2P5/2P5/P1P5/4PPPP/R1BQKBNR w KQkq - 0 1" # ...

stinkfish.set_fen_position(fen)
stinkfish._parameters["Contempt"] = 20 # NO DRAWS
stinkfish.set_elo_rating(200)          # ONLY GOOD MOVES

while True:
    top = getPossible(100)
    print(top)

    turn = fen.split(' ')[1]
    print("Turn: " + turn)

    worst = getWorst(turn, top)       # GET THE BEST MOVE
    stinkfish.make_moves_from_current_position([worst])
    print("Move:", worst)
    fen = stinkfish.get_fen_position()

    print(stinkfish.get_board_visual())

    advantage = stinkfish.get_evaluation()["value"]
    
    print(advantage, evaluate(advantage), "is WINNING")
    if input("Continue? (Y/N): ").upper() == "N":
        break
    print("\n\n")
