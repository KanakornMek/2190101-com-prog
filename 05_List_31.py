cards = input().split()
actions = input()

for i in actions:
    if i == 'C':
        cut_pos = int(len(cards)/2)
        part1 = cards[:cut_pos]
        part2 = cards[cut_pos:]

        cards = part2+part1
    elif i == 'S':
        shuffled = []
        card_halved = int(len(cards)/2)
        for j in range(card_halved):
            shuffled.append(cards[j])
            shuffled.append(cards[j+card_halved])
        cards = shuffled

for i in cards:
    print(i, end=" ")