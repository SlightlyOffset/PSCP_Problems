'''
grocery
'''

def main():
    '''
    main
    '''
    groceries_price = {
        "carrot" : 10,
        "cabbage" : 25,
        "tomato" : 3
    }
    price = 0
    buy_carrot, buy_cabbage, buy_tomato = input().split()
    price += groceries_price.get("carrot", 0) * int(buy_carrot)
    price += groceries_price.get("cabbage", 0) * int(buy_cabbage)
    price += groceries_price.get("tomato", 0) * int(buy_tomato)
    print(price)
if __name__ == "__main__":
    main()
