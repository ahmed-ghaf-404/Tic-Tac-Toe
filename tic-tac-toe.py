board = [   [1,2,3], 
            [4,5,6], 
            [7,8,9]
        ]
players = ("X", "O")
round = 0
global winner
winner = None


def show_board():
    """
    This function returns a visual representation of the board
    """
    board_visual = "-------------\n"
    for i in range(3):
        board_visual += "| "
        for j in range(3):
            board_visual += str(board[i][j]) + ' | '
        board_visual += "\n-------------\n"
    print(board_visual)


def input_tile(player, tile):
    # check 
    print()


def process_tile(tile ):
    x = int(tile//3)
    y = int(tile%3)
    return (x,y)


def choose_tile(player, tile_id):
    """Fills a tile with either X or O

    Args:
        player (str): Either X or O
        tile_id (int): tile number
    """
    # x = [tile_id//3] 
    # y =[tile_id%3] is how to determine which tile to use
    x, y = process_tile(tile_id)
    board[x][y] = player
    clear()
    
    return check_winner(player, x, y)

def clear():
    print("\n"*100)

def check_winner(player, x, y):
    """Checking for a winner from last move

    Args:
        player (string): the player id. Either X or O
        x (int): the x of the last move
        y (int): the y of the last move
    """
    has_row = True
    has_col = True
    has_left_diagonal = True
    has_right_diagonal = True
    for i in range(3):
        if board[x][i] != player:
            has_row = False
        if board[i][y] != player:
            has_col = False
        if board[i][i] != player:
            has_left_diagonal = False
        if board[i][2-i] != player:
            has_right_diagonal = False
    
    has_won = has_row or has_col or has_left_diagonal or has_right_diagonal
    print(player)
    if has_won:
        global winner
        winner = player
        print(winner)
    return  has_won

def terminate():
    print("Thanks for playing. :) <3")
    exit()

if __name__ == "__main__":    
    
    print("Welcome to Ahmed's Tic-Tac-Toe!\n")
    
    want_to_play = input("Do you want to play?\nenter yes or no\n")
    clear()
    if(want_to_play == "no"):
        terminate()
    print("Player 1 will be X.\nPlayer 2 will be O.\nAnd as the rules say, X starts!\n\n")
    show_board()
    
    for round in range(0,9):    
        vacant = False
        while not vacant:
            print("Round: {0}. It's {1}'s turn".format(round+1, players[round%2]))
            tile = int(input("Enter the tile's number."))
            if 1<= tile <= 9:
                x, y = process_tile(tile-1)
                if not (board[x][y] == "X" or board[x][y] == "O"):
                    vacant = True
                    choose_tile(players[round%2], tile-1)
                else:
                    print("This tile is not vacant")
            else:
                print("please choose an integer between 0 and 9")
            clear()
            show_board()
        if winner != None:
            break
        
    if(winner == None):
        print("Draw. Good luck next time")
    else:
        print("GG. {} has won!".format(winner))