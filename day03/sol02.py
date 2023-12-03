mode = "code"
with open(mode+".txt", "r") as f_in:
    sheet = {idx+1:"."+line.strip()+"." for idx, line in enumerate(f_in.readlines())}


def three_line_check(top, mid, bot):
    clear_mid = "".join([c if c.isdigit() else "." for c in mid])
    strt_stop_num = []
    num_len = 0
    for idx, x in enumerate(clear_mid.split(".")):
        if x.isdigit():
            strt_stop_num.append((idx+num_len,idx+num_len+len(x) ,x))
            num_len += len(x)

    star_parts = []
    for num in strt_stop_num:
        all_sides = top[num[0]-1:num[1]+1] + bot[num[0]-1:num[1]+1] + mid[num[0]-1]+mid[num[1]]
        if "*" in all_sides:
            star_parts.append(num)
    return star_parts

def check_gear(top, mid, bot, idx):
    t_parts = [t_part[2] for t_part in top if t_part[0]-1 <= idx <= t_part[1]]
    b_parts = [b_part[2] for b_part in bot if b_part[0]-1 <= idx <= b_part[1]]
    m_parts = [m_part[2] for m_part in mid if m_part[0]-1 <= idx <= m_part[1]]    

    if len(t_parts)+len(b_parts)+len(m_parts) == 2:
        parts = [t_parts+b_parts+m_parts][0]
        return int(parts[0])*int(parts[1])
    return 0

sheet_len = max(sheet.keys())
sheet_wdt = len(sheet[1])
sheet[0]="."*sheet_wdt
sheet[sheet_len+1]="."*sheet_wdt

rel_nums = [three_line_check(sheet[i-1],sheet[i],sheet[i+1]) for i in range(1,sheet_len+1)]
result = 0
for i in range(1,sheet_len+1):
    for idx, symb in enumerate(sheet[i]):
        if symb=="*":
            result += check_gear(rel_nums[i-2],rel_nums[i-1], rel_nums[i],idx)

print(result)
            