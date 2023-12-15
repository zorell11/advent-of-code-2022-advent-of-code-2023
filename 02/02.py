with open('input', 'r') as f:
    data = f.read().splitlines()

game = 0 
for i in data:
    part1, part2 = i.split(':')
    
    combinations = { 'red': 0, 'green': 0, 'blue': 0 }

    part2 = part2.replace(';', ',')

        
    for sets in part2.split(','):
        number, color = sets.split()
        if combinations[color] < int(number):
            combinations[color] = int(number)
    
    multiple = 1
    for i in combinations.values():
        multiple *= i
    game += multiple

print(game)   