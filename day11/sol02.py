mode = "code"
with open(mode+".txt", "r") as f_in:
    data = [line.strip() for line in f_in.readlines()]

EXPANSION = 1_000_000

def distance(t1, t2, vRs, vCs):
    dist = 0
    for vR in vCs:
        if t1[0] < vR < t2[0] or t1[0] > vR > t2[0]:
            dist+=EXPANSION-1 # minus the original
    for vC in vRs:
        if t1[1] < vC < t2[1] or t1[1] > vC > t2[1]:
            dist+=EXPANSION-1

    return dist+abs(t1[0]-t2[0])+abs(t1[1]-t2[1])

universeA = [] # expand columns
vastRows = []
for i,row in enumerate(data):
    if "#" not in row:
        universeA.append("*"*len(row))
        vastRows.append(i)
    else:
        universeA.append(row)

vastColumns = []
universeB = [] # transpose to expand rows
for column in range(len(universeA[0])):
    col = "".join([universeA[i][column] for i in range(len(universeA))])
    if "#" not in col:
        universeB.append("*"*len(col))
        vastColumns.append(column)
    else:
        universeB.append(col)

# transpose again
universe = [ "".join([universeB[i][column] for i in range(len(universeB))]) for column in range(len(universeB[0]))]
# collect galaxies
galaxies = [(x,y) for y,line in enumerate(universe) for x, val in enumerate(line) if val == "#"]
# sum up manhattan distances
result = sum([distance(g, galaxies[j], vastRows, vastColumns) for i,g in enumerate(galaxies) for j in range(i+1,len(galaxies))])

print(result)