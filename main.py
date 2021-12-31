import random

def start():
    print("\nThis program allows you to see how minesweeper works\n")
    size = int(input("Size (e.g.: 5): "))
    land = []
    for x in range(size):
        land.append([None]*size)

    difficulty = input("Difficulty (E-Easy, M-Medium, H-Hard, G-God): ").lower()
    if (difficulty == "e"): 
        mines = int(0.2*size**2)
    elif (difficulty == "m"):
        mines = int(0.4*size**2)
    elif (difficulty == "h"):
        mines = int(0.6*size**2)
    elif (difficulty == "g"):
        mines = int(0.8*size**2)

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

    visualize(land,size)

def visualize(land,size):
    vis = "\n"
    for x in range(size):
        vis += "|"
        for y in range(size):
            vis += (" " + str(land[x][y]) + " ")
        vis += "|\n"
    print(vis)

start()