'''
bill
'''

def main():
    '''
    main
    '''
    raw_price = int(input())
    service_charge = raw_price * 0.1

    if 50 <= service_charge <= 1000:
        raw_price += service_charge
    elif service_charge < 50:
        raw_price += 50
    elif service_charge > 1000:
        raw_price += 1000

    include_vat = raw_price + (raw_price * 0.07)
    print(f"{include_vat:.2f}")
if __name__ == "__main__":
    main()
