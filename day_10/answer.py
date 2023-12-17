all_data = []
S = []
with open('/Users/piotrbauer/Developer/projekty/Advent_of_code_2023/day10/data.txt') as data:
    for i, line in enumerate(data):
        if 'S' in line:
            S = [i+1,line.index('S')+1]
        all_data.append(list(line.strip()))

for row in range(len(all_data)):
    all_data[row].insert(0,'.')
    all_data[row].append('.')

row = ['.' for i in range(len(all_data[0]))]
all_data.insert(0,row)
all_data.append(row)
del(row)

possible_directions = {"|":{'g':"|7FS",'d':"|LJS"},
                       "-":{'l':'S-FL','p':'S-7J'},
                       "L":{'p':'SJ7-','g':'S|F7'},
                       "7":{'l':'S-LF','d':'S|JL'},
                       "J":{'l':'S-FL','g':'|SF7'},
                       "F":{'p':'S-J7','d':'S|JL'},
                       "S":{'l':'L-','p':'J7-','g':'F|7','d':'L|J'},
                       ".":{}}

# this code is suppose to clear the file - doesn't work
"""for wiersz in range(1,len(all_data)-1):
    for kolumna in range(1,len(all_data[0])-1):
        point = all_data[wiersz][kolumna]
        matching = True
        for direciton in possible_directions[point]:
            match direciton:
                case 'l':
                    matching *= all_data[wiersz][kolumna-1] in possible_directions[point][direciton]
                case 'p':
                    matching *= all_data[wiersz][kolumna+1] in possible_directions[point][direciton]
                case 'g':
                    matching *= all_data[wiersz-1][kolumna] in possible_directions[point][direciton]
                case 'd':
                    matching *= all_data[wiersz+1][kolumna] in possible_directions[point][direciton]
        if not matching:
            cleared_data[wiersz][kolumna] = '.'"""

last_match = 'S'
previous_direction = ''

start = True

points = [S]

while start or last_match != 'S':
    if start: start = False

    wiersz, kolumna = points[-1]
    point = all_data[wiersz][kolumna]

    where = []
    for direciton in possible_directions[last_match]:
        match direciton:
            case 'l':
                if all_data[wiersz][kolumna-1] in possible_directions[point][direciton]:
                    where.append(direciton)
            case 'p':
                if all_data[wiersz][kolumna+1] in possible_directions[point][direciton]:
                    where.append(direciton)
            case 'g':
                if all_data[wiersz-1][kolumna] in possible_directions[point][direciton]:
                    where.append(direciton)
            case 'd':
                if all_data[wiersz+1][kolumna] in possible_directions[point][direciton]:
                    where.append(direciton)

    if point != 'S':
        where = list("".join(where).replace(previous_direction,''))
    
    match where[-1]:
        case 'l':
            points.append([wiersz,kolumna-1])
            previous_direction = 'p'
            last_match = all_data[wiersz][kolumna-1]
        case 'p':
            points.append([wiersz,kolumna+1])
            previous_direction = 'l'
            last_match = all_data[wiersz][kolumna+1]
        case 'g':
            points.append([wiersz-1,kolumna])
            previous_direction = 'd'
            last_match = all_data[wiersz-1][kolumna]
        case 'd':
            points.append([wiersz+1,kolumna])
            previous_direction = 'g'
            last_match = all_data[wiersz+1][kolumna]

print("Amount of steps to get to the middle:",len(points)//2,sep="\t")