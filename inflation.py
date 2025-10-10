'''Inflation'''
def main():
    '''main'''
    price = int(float(input()) * 100)
    years = int(input())

    for i in range(years):
        inflate = (price * 381) // 10000
        price += inflate
        i += i
    price_int = price // 100
    decimal = price % 100

    print(f"{price_int}.{decimal:02d}")

if __name__ == "__main__":
    main()
