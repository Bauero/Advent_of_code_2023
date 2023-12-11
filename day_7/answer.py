def ile(tekst, szukaj):
    counter = 0
    for i in tekst:
        if i == szukaj:
            counter += 1
    return counter

def rank(x):
    rankx = None
    unikatX = len(set(x))
    if unikatX == 1:
        rankx = 7
    elif unikatX == 2 and ile(x,list(set(x))[0]) in (1,4):
        rankx = 6
    elif unikatX == 2 and ile(x,list(set(x))[0]) in (2,3):
        rankx = 5
    elif unikatX == 4 and ile(x,list(set(x))[0]) in (1,3):
        rankx = 4
    elif unikatX == 3 and ile(x,list(set(x))[0]) in (1,2):
        rankx = 3
    elif unikatX == 4 and ile(x,list(set(x))[0]) in (1,2):
        rankx = 2
    elif unikatX == 5:
        rankx = 1
    return rankx

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def greater(x,y):
    rankx = rank(x)
    ranky = rank(y)

    if rankx == ranky:
        for xi, yi in (x,y):
            if xi == yi: continue
            else:
                for i in range(5):
                    xv = 14 - cards.index(xi[i])
                    yv = 14 - cards.index(yi[i])
                    if xv > yv:
                        return True
                    elif xv < yv:
                        return False
                    else:
                        return -1

hands = []
with open('data.txt') as data:
    for l in data:
        hands.append(l.strip().split(" "))

# for x in range(len(hands)):
#     for y in range(-1,1-len(hands),-1):
#         verdict = greater(hands[y-1],hands[y])
#         if verdict == -1: continue
#         else:
#             if not verdict:
#                 hands[y-1],hands[y] = hands[y],hands[y-1]



suma = 0

# for i in range()

print(hands)
