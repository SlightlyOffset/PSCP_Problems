"""Donut"""
def main():
    """
    Calculates the minimum cost to acquire a target number of donuts
    with a "buy X, get Y free" promotion.
    """
    donut_price = int(input())
    promo_buy_count = int(input())  # Number of donuts to buy to get the promotion
    promo_free_count = int(input()) # Number of free donuts from the promotion
    donuts_wanted = int(input())

    # If no promotion is available (buy 0), just buy what's wanted.
    if not promo_buy_count:
        total_cost = donuts_wanted * donut_price
        donuts_got = donuts_wanted
        print(total_cost, donuts_got)
        return

    # A "bundle" is one activation of the promotion
    donuts_per_bundle = promo_buy_count + promo_free_count
    bundle_price = promo_buy_count * donut_price

    # Calculate how many full bundles can be bought
    num_bundles = donuts_wanted // donuts_per_bundle
    total_cost = num_bundles * bundle_price
    donuts_got = num_bundles * donuts_per_bundle

    # Calculate remaining donuts needed after buying full bundles
    remaining_needed = donuts_wanted - donuts_got
    if remaining_needed > 0:
        # If remaining donuts are enough to trigger another promotion, buy another bundle
        if remaining_needed >= promo_buy_count:
            total_cost += bundle_price
            donuts_got += donuts_per_bundle
        # Otherwise, buy the remaining donuts individually
        else:
            total_cost += remaining_needed * donut_price
            donuts_got += remaining_needed

    print(total_cost, donuts_got)

if __name__ == "__main__":
    main()
