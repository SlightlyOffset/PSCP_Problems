'''CoinChangev1'''
def main():
    '''main'''
    change = int(input())
    coin_given_out = 0
    while change > 0:
        if change - 25 >= 0:
            change -= 25
            coin_given_out += 1
        elif change - 10 >= 0:
            change -= 10
            coin_given_out += 1
        elif change - 5 >= 0:
            change -= 5
            coin_given_out += 1
        elif change - 1 >= 0:
            change -= 1
            coin_given_out += 1
        else:
            break
    print(coin_given_out)
if __name__ == '__main__':
    main()
