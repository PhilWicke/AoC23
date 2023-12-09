mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = f_in.readlines()
instructs = [0 if x=="L" else 1  for x in lines[0].strip()]
lines = lines[2:]
data = {line.split(" = ")[0]:line.split(" = (")[1][:-2].split(", ") for line in lines}

entry = "AAA"
idx, count = 0, 0
while entry != "ZZZ":
    options = data[entry]
    entry = options[instructs[idx]]
    idx+=1
    if idx == len(instructs): idx = 0
    count+=1

print(count)
