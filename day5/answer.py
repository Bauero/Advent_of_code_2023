seeds  = []
sekcje = []
with open("/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day5/data.txt","r") as data:
    
    seeds = data.readline().split(": ")[1].split(" ")
    data.readline()
    sekcje = data.read().split("""

""")
full_dict = {}
for s in sekcje:
    name, values = s.split(":")
    full_dict[name] = values.strip().split("\n")

results = []

def search_for_seed(seeds):
    for i, s in enumerate(seeds):
        s = int(s)
        for transformation in full_dict:
            for elem_range in full_dict[transformation]:
                    dest_range_star, source_range_start, iter = elem_range.strip().split(" ")
                    dest_range_star = int(dest_range_star)
                    source_range_start = int(source_range_start)
                    iter = int(iter)
                    if s >= source_range_start and s <= (source_range_start + iter - 1):
                        s = dest_range_star + (s - source_range_start)
                        break
        seeds[i] = s
    verdict = min([int(x) for x in seeds])
    results.append(verdict)
    print("Minimum: ",verdict,flush=True)


for x in range(0,len(seeds),2):
    val = int(seeds[x])
    values = [val + i for i in range(int(seeds[x+1]))]
    search_for_seed(values)


# Might work but is too complicated to compute in reasonable time
# for transformation in full_dict:
    
#     # prepare transformation
#     trans_dict = {}
#     for elem_range in full_dict[transformation]:
#         source_range_start, dest_range_star, iter = elem_range.strip().split(" ")
#         dest_range_star = int(dest_range_star)
#         source_range_start = int(source_range_start)
#         iter = int(iter)
#         for i in range(iter):
#             trans_dict[str(dest_range_star+i)] = str(source_range_start+i)
    
#     keys = list(trans_dict.keys())
#     for i, seed in enumerate(seeds):
#         if seed in keys:
#             seeds[i] = trans_dict[seed]


# print("Minimum:",min(list(map(int,seeds)))) 