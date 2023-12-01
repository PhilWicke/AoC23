mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = f_in.readlines()

result = 0
for line in lines:
    digits = [x for x in line if x.isdigit()]
    result+=int(digits[0]+digits[-1])
        
print(result)

# One line
print(sum([int([x for x in line if x.isdigit()][0]+[x for x in line if x.isdigit()][-1]) for line in open("code.txt", "r").readlines()]))