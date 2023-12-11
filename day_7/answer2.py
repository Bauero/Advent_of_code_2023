cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def rank(x):
    x = x[0]
    backup = len(set(x))

    spis = dict.fromkeys(set(x),0)
    for l in x: spis[l] += 1

    if "J" in x and spis['J'] < 5:
        jcount = spis['J']
        spis.pop('J')
        letter = sorted(list(spis.items()), key = lambda x: x[1], reverse = True)[0][0]
        x = x.replace('J',letter)
        spis[letter] += jcount
    
    match len(list(spis.keys())):

        case 1: return 7

        case 2:
            values = list(spis.values())
            if min(values) == 1 and max(values) == 4:
                return 6
            elif min(values) == 2 and max(values) == 3:
                return 5

        case 3:
            values = list(spis.values())
            if sorted(values) == [1,1,3]:
                return 4
            elif sorted(values) == [1,2,2]:
                return 3

        case 4: return 2
        case 5: return 1
        case _: return backup


hands = []
with open('/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day_7/data.txt') as data:
    for l in data:
        hands.append(l.strip().split(" "))


for i, h in enumerate(hands):
    identifier = [14 - cards.index(h[0][i]) for i in range(5)]
    identifier.insert(0,rank(h))
    h.append(tuple(identifier))
    # if i == 741:
    #     print(i)

# for i, h in enumerate(hands):
#     print(i, h)

hands_sorted = sorted(hands, key = lambda x: x[2],reverse=True)

for i, h in enumerate(hands_sorted):
    print(i, h)

number_of_hands = len(hands)
suma = 0 
for h in hands_sorted:
    suma += int(h[1]) * number_of_hands
    number_of_hands -= 1
print(suma)
