import math
file = open("/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day_9/data.txt")

sum_of_extrapolations = 0
sum_of_back_extrapolation = 0

def only_zero(l : list) -> bool:
    for i in l:
        if not (i == 0 or i == 0.0):
            return False
    return True

for line in file:
    line = line.strip().split(" ")
    line = [int(x) for x in line]
    list_of_permutations = [line]
    while not only_zero(list_of_permutations[-1]):
        last_one = list_of_permutations[-1]
        list_of_permutations.append([last_one[i+1] - last_one[i] for i in range(len(last_one)-1)])

    for l in range(len(list_of_permutations)-1,0,-1):
        if list_of_permutations[l] == []:
            list_of_permutations[l] = [0]
        value_at_end = list_of_permutations[l][-1] + list_of_permutations[l-1][-1]
        value_at_front = list_of_permutations[l-1][0] - list_of_permutations[l][0]
        
        list_of_permutations[l-1].append(value_at_end)
        list_of_permutations[l-1].insert(0,value_at_front)

    sum_of_extrapolations += list_of_permutations[0][-1]
    sum_of_back_extrapolation += list_of_permutations[0][0]

print("Solution for part one",sum_of_extrapolations)
print("Solution for part two",sum_of_back_extrapolation)