mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip().split(":")[1].split(" ") for line in f_in.readlines()]
    ts = [int(t) for t in lines[0] if t]
    ds = [int(d) for d in lines[1] if d]

result = 1
for race in range(0, len(ts)):
    t = ts[race]
    result *= len([n for n in range(t+1) if n*(t-n) > ds[race]])
print(result)
