kv_pair = []

total_sum = 0

with open("/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day4/data.txt","r") as d:
    for r in d:
        r = r.strip().split(": ")[1]
        r = r.replace("  "," ")
        # lucky | guessed
        l, g = r.split(" | ")
        l, g = l.split(" "), g.split(" ")
        kv_pair.append({"k" : l, "v" : g, "c" : 1})

for n, p in enumerate(kv_pair):
    elem_sum = len(p["k"]) + len(p["v"])
    num_uniq_elem = len(set(p["k"] + p["v"]))
    elem_diff = elem_sum - num_uniq_elem
    for i in range(elem_diff):
        kv_pair[n+i+1]["c"] += p['c']
    total_sum += p["c"]

print(total_sum)
