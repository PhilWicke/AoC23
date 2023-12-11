mode = "code"
with open(mode+".txt", "r") as f_in:
    data = [line.strip() for line in f_in.readlines()]

def distance(t1, t2):
    return abs(t1[0]-t2[0])+abs(t1[1]-t2[1])

universeA = [] # expand columns
for row in data:
    universeA.append(row)
    if "#" not in row:
        universeA.append(row)

universeB = [] # transpose to expand rows
for column in range(len(universeA[0])):
    col = "".join([universeA[i][column] for i in range(len(universeA))])
    universeB.append(col)
    if "#" not in col:
        universeB.append(col)

# transpose again
universe = [ "".join([universeB[i][column] for i in range(len(universeB))]) for column in range(len(universeB[0]))]
# collect galaxies
galaxies = [(x,y) for y,line in enumerate(universe) for x, val in enumerate(line) if val == "#"]
# sum up manhattan distances
result = sum([distance(g, galaxies[j]) for i,g in enumerate(galaxies) for j in range(i+1,len(galaxies))])

print(result)