with open('input', 'r') as f:
    data = f.read().splitlines()

game = 0 
for i in data:
    part1, part2 = i.split(':')
    
    for sets in part2.split('; '):
        combinations = { 'red':12, 'green': 13, 'blue': 14 }

        for set in sets.split(', '):
            number, color = set.split()
            combinations[color] -= int(number)

        if combinations['red'] < 0 or combinations['green'] < 0 or combinations['blue'] < 0:
            break

    else:
        actual_game = int(part1.split()[1])
        game += actual_game

print(game)   