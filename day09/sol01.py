mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = f_in.readlines()

data = [line.strip().split() for line in lines]

def get_dif_seq(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

result = 0
for seq in data:
    seq = [int(x) for x in seq]
    lasts = [seq[-1]]
    deriv_seq = seq
    while deriv_seq != [0]*len(deriv_seq):
        #print(deriv_seq)
        deriv_seq = get_dif_seq(deriv_seq)
        lasts.append(deriv_seq[-1])
        
    result+= sum(lasts)
    #print()

print(result)