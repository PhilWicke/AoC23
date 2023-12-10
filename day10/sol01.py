import time
mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = f_in.readlines()

GRID = ["|"+line.strip()+"|" for line in lines]
GRID.insert(0,"-"*len(GRID[-1]))
GRID.append("-"*len(GRID[-1]))

def findNextPipe(pos, prvPos):
    y,x = pos[0],pos[1]
    symb = GRID[y][x]
    py,px = prvPos[0],prvPos[1]
    prevSymb = GRID[py][px]

    if symb == "S":
        if GRID[y-1][x] in ["|","7","F"]:
            return (y-1,x)
        elif GRID[y][x+1] in ["-","7","J"]:
            return (y,x+1)
        elif GRID[y+1][x] in ["|","J","L"]:
            return (y+1,x)
        elif GRID[y][x-1] in ["-","L","F"]:
            return (y,x-1)
    elif symb == "-":
        if px == x-1: return (y,x+1)
        else: return (y,x-1)
    elif symb == "|":
        if py == y-1: return (y+1,x)
        else: return (y-1,x)
    elif symb == "L":
        if py == y-1: return (y,x+1)
        else: return (y-1,x)
    elif symb == "J":
        if py == y-1: return (y,x-1)
        else: return (y-1,x)
    elif symb == "7":
        if py == y+1: return (y,x-1)
        else: return (y+1,x)
    elif symb == "F":
        if py == y+1: return (y,x+1)
        else: return (y+1,x)

startYX = (0,0)
for y,line in enumerate(GRID):
    for x, val in enumerate(line):
        if val == "S":
            startYX = (y,x)

prevPipe = (None, None)
currPipe = (None, None)
nextPipe = (None, None)
start = True
count=0
while nextPipe != startYX:
    count+=1
    if start: 
        currPipe = startYX
        prevPipe = currPipe
        start = False
    
    nextPipe = findNextPipe(currPipe, prevPipe)
    prevPipe = currPipe
    currPipe = nextPipe

print(count/2)