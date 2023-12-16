with open('input', 'r') as f:
    data = f.read().splitlines()

races = []
for line in data:
    races.append(list(map(int, line.split(':')[1].split())))

races = list(zip(*races))

wins = 1

for time, distance in races:
    win = 0
    for i in range(time):
         if ((time-i) * i) > distance:
            win += 1
    wins *= win
print(wins)

