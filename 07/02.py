from collections import defaultdict

with open('input', 'r') as f:
    data = f.read().splitlines()

rank = defaultdict(list)


def find_type(card):
    if len(set(card)) == 1:
        return 7
    elif len(set(card)) == 2:
        #6,5
        for i in card:
            if card.count(i) == 4:
                return 6
        else:
            return 5
    elif len(set(card)) == 3:
        #4,3
        for i in card:
            if card.count(i) == 3:
                return 4
        else:
            return 3
    elif len(set(card)) == 4:
        return 2
    elif len(set(card)) == 5:
        return 1


for line in data:
    card, value = line.split()
    card = card.replace('T','B').replace('J','1').replace('Q','D').replace('K','E').replace('A','F')
    
    if '1' in card:
        types = []
        for i in '23456789BDEF':
            types.append(find_type(card.replace('1', i)))
        rank[max(types)].append((card, int(value)))
    else:
        card_type = find_type(card)
        rank[card_type].append((card, int(value)))


total = 0
counter = 1
total_bids = []
for item, value in sorted(rank.items()):
    for _, bid in sorted(value):
        total += (counter*int(bid))
        counter +=1

print(total)