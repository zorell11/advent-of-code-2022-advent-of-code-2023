with open('input', 'r') as f:
    data = f.read().splitlines()

race = []
for line in data:
    race.append(int(line.split(':')[1].replace(' ','')))

win = 0
for i in range(race[0]):
    if ((race[0]-i) * i) > race[1]:
        win += 1
print(win)