table = [["   ", "   ", "   "], 
         ["   ", "   ", "   "], 
         ["   ", "   ", "   "]]
playerX = True
playerO = True
pX_ls = []
pO_ls = []
pX = []
pO = []
game = True

# print the table
def table_print():
    line1 = f"|{table[0][0]}|{table[0][1]}|{table[0][2]}|"
    line2 = f"|{table[1][0]}|{table[1][1]}|{table[1][2]}|"
    line3 = f"|{table[2][0]}|{table[2][1]}|{table[2][2]}|"
    print(" ---" * 3)
    print(line1)
    print(" ---" * 3)
    print(line2)
    print(" ---" * 3)
    print(line3)
    print(" ---" * 3)
table_print()

# debug
def debug(x, y):
    picture = True
    x = int(x)
    y = int(y)
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Error: Coordinate outside grid.")
        picture = False
    elif table[x][y] != "   ":
        print("Error: Illegal move. Square is already filled.")
        picture = False
    return picture


# playerX's turn
def pX_fn(playerX, playerO):
    while playerX:
        pX_turn = input("Player X's turn: ")
        pX_ls = pX_turn.split(" ")
        for i in pX_turn:
            pX_ls.append(i)
        picture = debug(pX_ls[0], pX_ls[1])
        pX.append(10 * int(pX_ls[0]) + int(pX_ls[1]))
        pX.sort()
        if picture:
            table[int(pX_ls[0])][int(pX_ls[1])] = " X "
            table_print()
            playerX = False
            playerO = True
    return playerX, playerO

# playerO's turn
def pO_fn(playerX, playerO):
    while playerO:
        pO_turn = input("Player O's turn: ")
        pO_ls = pO_turn.split(" ")
        for i in pO_turn:
            pO_ls.append(i)
        picture = debug(pO_ls[0], pO_ls[1])
        pO.append(10 * int(pO_ls[0]) + int(pO_ls[1]))
        pO.sort()
        if picture:
            table[int(pO_ls[0])][int(pO_ls[1])] = " O "
            table_print()
            playerO = False
            playerX = True
    return playerX, playerO

# win checking
def win_check(game):
    print(pO)
    tie = 0
    win_ls = [[0, 1, 2], [0, 10, 20], [1, 11, 21], [2, 12, 22], [10, 11, 12], [20, 21, 22], [0, 11, 22], [2, 11, 20]]
    for i in win_ls:
        win_X = 0
        win_O = 0
        for k in range(len(table)):
            if i[k] in pX:
                win_X += 1

            elif i[k] in pO:
                win_O += 1
    
        if win_X == 3:
            print("Game over: Player X won!")
            game = False
        
        if win_O == 3:
            print("Game over: Player O won!")
            game = False

    if game:
        for i in range(len(table)):
            for k in range(len(table)):
                if table[i][k] == "   ":
                    tie = 1

        if tie != 1:
            print("Game over: Tie!")
            game = False

    return game

while game:
    playerX, playerO = pX_fn(playerX, playerO)
    game = win_check(game)
    if game:
        playerX, playerO = pO_fn(playerX, playerO)
        game = win_check(game)