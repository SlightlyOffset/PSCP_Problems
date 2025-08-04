'''
rule of three
'''
def get_cheapest(items):
    '''
    Get the most cost-effective item (highest value = volume/price).
    If multiple items have equal value, return the one with the lowest price.
    '''
    best_value = -1
    best_price = float('inf')
    best_volume = 0.0

    for price, volume in items:
        value = volume / price
        if value > best_value:
            best_value = value
            best_price = price
            best_volume = volume
        elif value == best_value and price < best_price:
            best_price = price
            best_volume = volume

    return best_price, best_volume

def main():
    '''
    Main function to read input and output the most cost-effective item.
    '''
    items = [(float(input()), float(input())) for _ in range(int(input()))]

    price, volume = get_cheapest(items)
    print(f"{price:.2f} {volume:.2f}")

if __name__ == "__main__":
    main()