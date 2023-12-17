import math

with open('input', 'r') as f:
    data = f.read().splitlines()


instructions = data[0].replace('L', '0').replace('R', '1')
elements = {}
keys = []

for line in data[2:]:
    key, value = line.split(' = ')
    if key.endswith('A'):
        keys.append(key)
    value = value.strip('()').split(', ')
    elements[key] = value

nums = []
for key in keys:
    counter = 1
    key_counters = []
    while True:
        index = int(instructions[counter%len(instructions)])

        key = elements[key][index]

        if key.endswith('Z'):
            key_counters.append(counter)
            if len(key_counters) == 2:
                nums.append(key_counters[1] - key_counters[0])
                break
        counter += 1

print(nums)

print(math.lcm(*nums))