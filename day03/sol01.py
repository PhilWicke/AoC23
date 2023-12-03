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

    num_sum = 0
    for num in strt_stop_num:
        all_sides = top[num[0]-1:num[1]+1] + bot[num[0]-1:num[1]+1] + mid[num[0]-1]+mid[num[1]]
        if all_sides != len(all_sides)*".":
            num_sum+=int(num[2])
    return num_sum

sheet_len = max(sheet.keys())
sheet_wdt = len(sheet[1])
sheet[0]="."*sheet_wdt
sheet[sheet_len+1]="."*sheet_wdt

result = 0
for i in range(1,sheet_len+1):
    result += three_line_check(sheet[i-1],sheet[i],sheet[i+1])
print(result)
            