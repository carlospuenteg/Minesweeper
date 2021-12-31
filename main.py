import random

# pyinstaller --onefile main.py

alpha = "abcdefghijklmnopqrstuvwyz"

def start():
    #-----------------------------------------------------------------------------
    print("\nThis program allows you to see how minesweeper works\n")
    size = int(input("Size (e.g.: 5): "))
    #-----------------------------------------------------------------------------
    land = []
    visLand = []  # visible land
    for x in range(size):
        land.append([None]*size)
        visLand.append(["�"]*size)
    play = True
    #-----------------------------------------------------------------------------
    difficulty = input("Difficulty (E-Easy, M-Medium, H-Hard, G-God): ").lower()
    if (difficulty == "e"): 
        mines = int(0.2*size**2)
    elif (difficulty == "m"):
        mines = int(0.4*size**2)
    elif (difficulty == "h"):
        mines = int(0.6*size**2)
    elif (difficulty == "g"):
        mines = int(0.8*size**2)
    #-----------------------------------------------------------------------------
    minesLoc = []
    for x in range(mines):
        r = random.randint(0,size**2-1)
        if (r not in minesLoc): minesLoc.append(r)

    for i in range(len(minesLoc)):
        x = minesLoc[i]//size  # 11//4 = 2
        y = minesLoc[i]%size  # 11%4 = 3
        land[x][y] = "⨀"

    for i in range(size):
        for j in range(size):
            nMines = 0
            if (not land[i][j]): # If there isn't a mine
                if (j==0): 
                    if (land[i][j+1]=="⨀"): nMines += 1
                elif (j==size-1):
                    if (land[i][j-1]=="⨀"): nMines += 1
                else: 
                    if (land[i][j+1]=="⨀"): nMines += 1
                    if (land[i][j-1]=="⨀"): nMines += 1

                if (i==0): 
                    if (land[i+1][j]=="⨀"):  nMines += 1
                    if (j==0):
                        if (land[i+1][j+1]=="⨀"):  nMines += 1
                    elif (j==size-1):
                        if (land[i+1][j-1]=="⨀"):  nMines += 1
                    else:
                        if (land[i+1][j+1]=="⨀"):  nMines += 1
                        if (land[i+1][j-1]=="⨀"):  nMines += 1
                elif (i==size-1): 
                    if (land[i-1][j]=="⨀"):  nMines += 1
                    if (j==0):
                        if (land[i-1][j+1]=="⨀"):  nMines += 1
                    elif (j==size-1):
                        if (land[i-1][j-1]=="⨀"):  nMines += 1
                    else:
                        if (land[i-1][j+1]=="⨀"):  nMines += 1
                        if (land[i-1][j-1]=="⨀"):  nMines += 1
                else:
                    if (land[i+1][j]=="⨀"):  nMines += 1
                    if (land[i-1][j]=="⨀"):  nMines += 1
                    if (j==0):
                        if (land[i+1][j+1]=="⨀"):  nMines += 1
                        if (land[i-1][j+1]=="⨀"):  nMines += 1
                    elif (j==size-1):
                        if (land[i+1][j-1]=="⨀"):  nMines += 1
                        if (land[i-1][j-1]=="⨀"):  nMines += 1
                    else:
                        if (land[i+1][j+1]=="⨀"):  nMines += 1
                        if (land[i-1][j+1]=="⨀"):  nMines += 1
                        if (land[i+1][j-1]=="⨀"):  nMines += 1
                        if (land[i-1][j-1]=="⨀"):  nMines += 1

                land[i][j] = nMines

    #-----------------------------------------------------------------------------
    while play:
        visualize(visLand,size)
        print("\nThere are "+str(mines)+" mines")
        while True:
            loc = input("What location do you want to choose? (e.g. Aa): ").lower()
            loc_x = alpha.index(loc[0])
            loc_y = alpha.index(loc[1])
            if (loc_x < size and loc_x >=0 and loc_y < size and loc_y >= 0): 
                break
            else:
                print("\nInvalid location!\n")

        if (visLand[loc_x][loc_y] == "�"):
            if (land[loc_x][loc_y] == "⨀"):
                play = False
                print("\n YOU LOST \n")
            else:
                visLand[loc_x][loc_y] = land[loc_x][loc_y]
        else:
            print("\nYou've already chosen that location!\n")

        locLeft = 0
        for x in range(size):
            for y in range(size):
                if (visLand[x][y] == "�"): locLeft += 1
        if (locLeft == mines):
            visualize(visLand,size)
            print("\nYOU WON!\n")
            play = False


##################################################################################

def visualize(land,size):
    vis = "\n   "
    for x in range(size):
        vis += " " + alpha[x] + " "
    vis += " \n"

    for x in range(size):
        vis += alpha[x].upper() + " |"
        for y in range(size):
            vis += (" " + str(land[x][y]) + " ")
        vis += "|\n"
    print(vis)

start()