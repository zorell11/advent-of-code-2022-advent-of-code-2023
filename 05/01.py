
with open('input', 'r') as f:
    data = f.read().splitlines()

data.append('EOF')

seeds = list(map(int, data[0].split(':')[1].split()))

actual = []
for index,seed in enumerate(seeds):
    for line in data[2:]:
        if not line:
            continue
        elif line and line[0].isdecimal():
            actual.append(list(map(int, line.split())))
            
        elif line[0].isalnum():
            for line in actual:
                if seeds[index] in range(line[1], line[1]+line[2]):
                    seeds[index] += line[0] - line[1]
                    break

            actual = []
    
print(min(seeds))