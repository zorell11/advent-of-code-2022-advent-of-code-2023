with open('input', 'r') as f:
    data = f.read().splitlines()


scratchcards = {}
num_of_matches = []
for full_card in data:
    header, cards = full_card.split(':')
    index = int(header.split()[1])
    scratchcards[index] = 1
    card1, card2 = cards.split('|')
    num_of_matches.append(len(set(map(int, card1.split())) & set(map(int, card2.split()))))

for index,num in enumerate(num_of_matches,1):
    for _ in range(scratchcards[index]):
        for i in range(index+1, index+num+1):
            scratchcards[i] += 1


print(sum(scratchcards.values()))