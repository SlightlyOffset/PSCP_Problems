"""CokeV1 / V2"""

def main():
    """Calculates the minimum cost to buy a number of cokes with a promotion."""
    a = int(input())    # Original price
    b = int(input())    # Number of point require to get promotion
    c = int(input())    # New promotion price
    d = int(input())    # Number of bottles to buy

    if not d:
        print(0)
        return

    # If no promotion is available (b=0) or promotion price is not better, buy all at full price.
    if not b or c >= a:
        print(a * d)
        return

    # The first bottle must be bought at full price.
    total_cost = a
    bottles_to_buy = d - 1

    # Calculate cost for the remaining bottles.
    # A promotion cycle consists of (b-1) full-price bottles and 1 promo bottle.
    num_cycles = bottles_to_buy // b
    total_cost += num_cycles * ((b - 1) * a + c)

    # Cost for any remaining bottles after full cycles.
    remaining_bottles = bottles_to_buy % b
    total_cost += remaining_bottles * a

    print(total_cost)

if __name__ == "__main__":
    main()
