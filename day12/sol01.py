import itertools

mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

def get_ops(sequence):
    return [len(op) for op in sequence.split(".") if len(op)]

def permute(sequence):
    idxs_varsymb = [idx for idx,x in enumerate(sequence) if x=="?"]
    replace_lists = []
    for i in range(len(idxs_varsymb)+1):
        replace_lists.extend(list(set(itertools.permutations(i*"#"+"."*((len(idxs_varsymb))-i)))))
    
    sequences = []
    for rep_num, replacements in enumerate(replace_lists):
        #print("\t",rep_num,"/",len(replacements))
        seq_list = list(sequence)
        for count, idx_varsymb in enumerate(idxs_varsymb):
            seq_list[idx_varsymb] = replacements[count]
        sequences.append("".join(seq_list))
    
    return sequences

result = 0
for lnum, line in enumerate(lines):
    print(lnum,"/",len(lines))
    seq, conf = line.split()
    conf = [int(x) for x in conf if x != ","]
    perms = permute(seq)
    count = len([perm for perm in perms if get_ops(perm) == conf])
    result+=count


print(result)