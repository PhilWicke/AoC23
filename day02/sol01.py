mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

result = 0
for idx, game in enumerate(lines):
    valid = True
    overlimit = [(int(x), game.split(" ")[i+1][0]) for i, x in enumerate(game.split(" ")[:-1]) if x.isdigit() and int(x) > 12]
    for val in overlimit:
        if valid and val[1] == "r" and val[0]>12 or val[1] == "g" and val[0]>13 or val[1] == "b" and val[0]>14:
            valid = False
    if valid:
        result+=idx+1
print(result)