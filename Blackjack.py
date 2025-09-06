'''Blackjack'''
def best_hand_value(cards):
    '''return best hand value'''
    card_values = {
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10,
        "J" : 10,
        "Q" : 10,
        "K" : 10,
        "A" : 11 # Assume 11 initially, adjust later if needed
    }

    value = 0
    ace_count = 0
    for card in cards:
        if card == "A":
            ace_count += 1
        value += card_values.get(card, 0)

    # If the total is over 21 and there are aces,
    # convert aces from 11 to 1 until the total is 21 or less.
    while value > 21 and ace_count > 0:
        value -= 10 # (Changing an 11 to a 1 is a reduction of 10)
        ace_count -= 1

    return value

def main():
    '''main'''
    card_n = int(input())
    cards = []
    for _ in range(card_n):
        cards.append(input())
    print(best_hand_value(cards))
if __name__ == '__main__':
    main()
