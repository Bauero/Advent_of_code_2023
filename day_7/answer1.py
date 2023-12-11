cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def rank(x):
    x = x[0]
    rankx = None
    
    match len(set(x)):

        case 5: rankx = 7

        case 4:
            spis = dict.fromkeys(set(x),0)
            for l in x: spis[l] += 1
            values = list(spis.values())
            if min(values) == 1 and max(values) == 4:
                rankx = 6
            elif min(values) == 2 and max(values) == 3:
                rankx = 5

        case 3:
            spis = dict.fromkeys(set(x),0)
            for l in x: spis[l] += 1
            values = list(spis.values())
            if sorted(values) == [1,1,3]:
                rankx = 4
            elif sorted(values) == [1,2,2]:
                rankx = 3

        case 4: rankx = 2
        case 5: rankx = 1

    return rankx


hands = []
with open('/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day_7/data.txt') as data:
    for l in data:
        hands.append(l.strip().split(" "))


for h in hands:
    identifier = [14 - cards.index(h[0][i]) for i in range(5)]
    identifier.insert(0,rank(h))
    h.append(tuple(identifier))

hands_sorted = sorted(hands, key = lambda x: x[2],reverse=True)

for i, h in enumerate(hands):
    print(i, h)

number_of_hands = len(hands)
suma = 0 
for h in hands_sorted:
    suma += int(h[1]) * number_of_hands
    number_of_hands -= 1
print(suma)
