structure = None
order = None
with open("data.txt") as data:
    order = data.readline().strip()

    data.readline()
    structure = {row.split(" = ")[0] : tuple(row.split(" = ")[1].strip()[1:-1].split(", ")) for row in data}

order_len = len(order)
counter = 0

direction = order[0]

starting_points = list(filter(lambda x: x.endswith("A"),structure.keys()))

# This is my first solution - it's propably correct but given the answer is enormous
# 21083806112641

# while True:

#     ends_with_Z = True

#     for i, sp in enumerate(starting_points):
#         starting_points[i] = structure[sp][0 if direction == "L" else 1]
#         ends_with_Z *= starting_points[i].endswith('Z')

#     counter += 1
#     direction = order[counter % order_len]

#     if ends_with_Z: break


# So after inspiration from other code let's modify my to implement the same approach

from itertools import cycle
import math

directions = [0 if d == 'L' else 1 for d in order]
cycles = []
for node in starting_points:
    for steps, d in enumerate(cycle(directions), start=1):
        node = structure[node][d]
        if node[2] == 'Z':
            cycles.append(steps)
            break

print(math.lcm(*cycles))