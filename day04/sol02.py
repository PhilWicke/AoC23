mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

result = {}
for idx, line in enumerate(lines):
    win, my = line.split(": ")[1].split("|")
    win, my = win.strip().replace("  "," ").split(" "), my.strip().replace("  "," ").split(" ")
    result[idx+1] = int(len([int(w) for w in win if w in my]))

card_counts = {k:0 for k,v in result.items()}
for idx, count in result.items():
    card_counts[idx] += 1
    for i in range(idx+1,idx+count+1):
        card_counts[i] += 1*card_counts[idx]

print(sum(card_counts.values()))