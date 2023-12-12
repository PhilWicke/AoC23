mode = "test2"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]