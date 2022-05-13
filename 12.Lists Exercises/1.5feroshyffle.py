card_deck = input().split(' ')
numbers_of_shuffles = int(input())

final_deck = []
for shuffle in range(numbers_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(card_deck) // 2
    left_half = card_deck[0:middle_of_the_deck]
    right_half = card_deck[middle_of_the_deck::]
    for idndex_of_card in range(len(left_half)):
        final_deck.append(left_half[idndex_of_card])
        final_deck.append(right_half[idndex_of_card])
    card_deck = final_deck

print(card_deck)