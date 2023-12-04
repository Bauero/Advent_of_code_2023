counter = 0
with open("/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day4/data.txt","r") as d:
    for r in d:
        r = r.strip().split(": ")[1]
        r = r.replace("  "," ")
        # lucky | guessed
        l, g = r.split(" | ")
        l, g = l.split(" "), g.split(" ")
        len_L = len(l)
        len_G = len(g)
        len_gl = len(set(g+l))
        if len_L + len_G > len_gl:
            counter += 2**(len_G + len_L - len_gl - 1)

print(counter)
