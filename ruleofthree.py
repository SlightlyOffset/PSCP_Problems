'''
rule of three
'''
def get_cheapest(items):
    '''
    "DO NOT TOUCH—Tuple Handling by a Licensed Chaos Alchemist."
    
    Get the most valuable item (highest volume per price).
    If multiple have equal value, pick the one with lowest price.
    '''
    volume_per_unit_price_list = []
    for price, volume in items:
        volume_per_unit_price = volume / price
        volume_per_unit_price_list.append((price, volume, volume_per_unit_price))

    # Initialize with first item's stats
    cheapest = volume_per_unit_price_list[0][2]
    found_equal_value = [(volume_per_unit_price_list[0][0], volume_per_unit_price_list[0][1])]
    cheapest_tuple = (volume_per_unit_price_list[0][0], volume_per_unit_price_list[0][1])

    for price, volume, unit_price in volume_per_unit_price_list[1:]:
        if unit_price == cheapest:
            found_equal_value.append((price, volume))
        elif unit_price > cheapest:
            cheapest = unit_price
            cheapest_tuple = (price, volume)
            found_equal_value = [(price, volume)]

    # Among equals, pick lowest price
    if len(found_equal_value) > 1:
        cheapest_price = found_equal_value[0][0]
        cheapest_volume = found_equal_value[0][1]
        for price, volume in found_equal_value:
            if price < cheapest_price:
                cheapest_price = price
                cheapest_volume = volume
        cheapest_tuple = (cheapest_price, cheapest_volume)

    return cheapest_tuple

def main():
    '''
    Main function to read input and output the most cost-effective item.
    '''
    items = [(float(input()), float(input())) for _ in range(int(input()))]
    price, volume = get_cheapest(items)
    print(f"{price:.2f} {volume:.2f}")

if __name__ == "__main__":
    main()
