from collections import defaultdict

with open('input', 'r') as f:
    data = f.read().splitlines()

rank = defaultdict(list)

for line in data:
    card, value = line.split()
    card = card.replace('T','B').replace('J','C').replace('Q','D').replace('K','E').replace('A','F')
    if len(set(card)) == 1:
        rank[7].append((card, int(value)))
    elif len(set(card)) == 2:
        #6,5
        for i in card:
            if card.count(i) == 4:
                rank[6].append((card, int(value)))
                break
        else:
            rank[5].append((card, int(value)))
    elif len(set(card)) == 3:
        #4,3
        for i in card:
            if card.count(i) == 3:
                rank[4].append((card, int(value)))
                break
        else:
            rank[3].append((card, int(value)))
    elif len(set(card)) == 4:
        rank[2].append((card, int(value)))
    elif len(set(card)) == 5:
        rank[1].append((card, int(value)))


total = 0
counter = 1
total_bids = []
for item, value in sorted(rank.items()):
    for _, bid in sorted(value):
        total += (counter*int(bid))
        counter +=1

print(total)