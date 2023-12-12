structure = None
order = None
with open("data.txt") as data:
    order = data.readline().strip()

    data.readline()
    structure = {row.split(" = ")[0] : row.split(" = ")[1].strip()[1:-1].split(", ") for row in data}

order_len = len(order)
counter = 0

direction = order[0]

curr_point = list(structure.keys())[0]

while curr_point != "ZZZ":
    counter += 1
    
    if direction == "L":
        curr_point = structure[curr_point][0]
    else:
        curr_point = structure[curr_point][1]

    direction = order[counter % order_len]

print(counter)