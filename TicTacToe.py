#TicTacToe game

X = "X"
O = "O"
LENGTH = 3

def draw(board):
    for i, y in enumerate(board):
        #Simplify and generalize the string formatting 
        print "{}|{}|{}".format(y[0],y[1],y[2])
        if i <> 2:
            print "-----"

def turn(players, activePlayer):
    active_player_info = [players.keys()[activePlayer],players[players.keys()[activePlayer]]]
    print "{} playing with {}, it's your turn!".format(active_player_info[0], active_player_info[1])
    while True:
        inp = raw_input("Please enter the coordinates (two integers, each 1 to 3) to place your mark in the format 'xy'")
        #check format
        if len(inp)<>2:
            print "Are you stupid, the format is wrong!"
            continue
        try:
            inpx = int(inp[0])
            inpy = int(inp[1])
        except:
            print "Are you stupid, these are not two integers!"
        else:
            if inpx not in [1,2,3] or inpy not in [1,2,3]:
                print "Are you stupid, the format is wrong!"
                continue
            #check if the cell is available
            if board[inpy-1][inpx-1] == " ":
                return (inpy, inpx, players[players.keys()[activePlayer]])
            else:
                print "Are you stupid, this cell is already taken!"
                continue
                #retry input of the same player
        
def checkWin(board):
    winner = ''
    #check horizontals
    for y in board:
        #print "Set(y) is %r" % set(y)
        if set(y) == set(['X']):
            return (False, "Player 1")
        elif set(y) == set(['O']):
            return (False, "Player 2")            
    #check verticals
    for i in range(len(board)):
        x = []
        for j in range(len(board)):
            x.append(board[j][i])
        #print "Set(x) is %r" % set(x)
        if set(x) == set(['X']):
            return (False, "Player 1")
        elif set(x) == set(['O']):
            return (False, "Player 2")
    #check diagonals
    d1 = [board[0][0],board[1][1],board[2][2]]
    d2 = [board[0][2],board[1][1],board[2][0]]
    if set(d1) == set(['X']):
        return (False, "Player 1")
    elif set(d1) == set(['O']):
        return (False, "Player 2")
    if set(d2) == set(['X']):
        return (False, "Player 1")
    elif set(d2) == set(['O']):
        return (False, "Player 2")
    else:
        return None


    
def reset(length):
    board = []
    for i in range(length):
        board.append([" "]*length)
    return board

#starting a new game, reset the board and gamestate
board = reset(LENGTH)
#gamestate gs - dictionary containing changing parameters about the current game
#The game is active, unless changed to inactive after one of the players wins
#Starting with Xs (order reversed in dict??)
gs = {"mode":"vs","active":True, "activePlayer":1, "winner":""}
#two players in tictactoe, one playing with Xs and another with Os
players = {"Player 1" : X, "Player 2" : O}

active_player = 1
#starting the game
#draw the board before the turn
draw(board)
while(gs["active"]):
    #ask for input
    turnResult = turn(players, gs["activePlayer"])
    board[turnResult[0]-1][turnResult[1]-1] = turnResult[2]
    #draw the board after the turn
    draw(board)
    #check if the player has won
    result = checkWin(board)
    if result <> None:
        (gs["active"], gs["winner"]) = result
    if not gs["active"]:
        print "Game is over! The winner is {}".format(gs["winner"])
    #continue to next player
    if gs["activePlayer"] == 1:
        gs["activePlayer"] = 0
    elif gs["activePlayer"] == 0:
        gs["activePlayer"] = 1


    
