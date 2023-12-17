with open('input', 'r') as f:
    data = f.read().splitlines()


instructions = data[0].replace('L', '0').replace('R', '1')
elements = {}
for line in data[2:]:
    key, value = line.split(' = ')
    value = value.strip('()').split(', ')
    elements[key] = value

counter = 0
key = 'AAA'

while key != 'ZZZ':
    index = int(instructions[counter%len(instructions)])
    key = elements[key][index]
    counter += 1

print(counter)