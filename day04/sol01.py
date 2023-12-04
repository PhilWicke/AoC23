mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

result = 0
for line in lines:
    win, my = line.split(": ")[1].split("|")
    win, my = win.strip().replace("  "," ").split(" "), my.strip().replace("  "," ").split(" ")
    result += int(2**(len([int(w) for w in win if w in my])-1))
print(result)
    