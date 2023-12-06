mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

# Parsing Data
seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]
maps = {}
buffer = []
previous_map = ""
for line in lines[1:]:
    if "map" in line and buffer == []:
        previous_map = line.strip(" map:")
    if "map" in line and buffer:
        maps[previous_map] = buffer
        previous_map = line.strip(" map:")
        buffer = []
    if line and line[0].isdigit():
        buffer.append(line)
maps[previous_map] = buffer

# Evaluating Data
current_seeds = seeds
for name, map in maps.items():
    for idx, seed in enumerate(current_seeds):
        for entry in map:
            entry = entry.split(" ")
            start_source = int(entry[1])
            start_destin = int(entry[0])
            ranging = int(entry[2])

            if start_source <= seed <= start_source+ranging:
                seed_map_idx = seed-start_source
                current_seeds[idx] = start_destin+seed_map_idx

print(min(current_seeds))