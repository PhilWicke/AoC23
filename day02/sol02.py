mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

result = 0
for idx, game in enumerate(lines):
    content = game.split(": ")[1]
    samples = content.replace(", ","; ").split("; ")
    g_max = max([int(s.split(" ")[0]) for s in samples if s.endswith("n")])
    b_max = max([int(s.split(" ")[0]) for s in samples if s.endswith("e")])
    r_max = max([int(s.split(" ")[0]) for s in samples if s.endswith("d")])
    result += g_max*b_max*r_max

print(result)