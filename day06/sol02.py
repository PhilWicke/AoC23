mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip().split(":")[1].replace(" ","") for line in f_in.readlines()]
    time = int(lines[0])
    dist = int(lines[1])

result = len([n for n in range(time+1) if n*(time-n) > dist])
print(result)

