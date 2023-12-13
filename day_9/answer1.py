import math
file = open("data.txt")

sum_of_extrapolations = 0

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
        value = list_of_permutations[l][-1] + list_of_permutations[l-1][-1]
        list_of_permutations[l-1].append(value)

    sum_of_extrapolations += list_of_permutations[0][-1]

print("Solution for part one",sum_of_extrapolations)