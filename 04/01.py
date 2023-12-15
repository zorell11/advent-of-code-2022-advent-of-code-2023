with open('input', 'r') as f:
    data = f.read().splitlines()


points = 0 
for full_card in data:

    card1, card2 = full_card.split(':')[1].split('|')
    winning_numbers = set(map(int, card1.split())) & set(map(int, card2.split()))

    if winning_numbers:
        points += 2**(len(winning_numbers)-1)

print(points)