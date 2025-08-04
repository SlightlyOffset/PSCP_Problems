'''
Progressive tax
'''
def calculate_tax(net_income):
    '''
    calculate tax based on category
    '''
    brackets = [
        (150000, 0),
        (300000, 0.05),
        (500000, 0.10),
        (750000, 0.15),
        (1000000, 0.20),
        (2000000, 0.25),
        (4000000, 0.30),
        (float('inf'), 0.35)
    ]

    tax = 0
    prev_limit = 0
    for limit, rate in brackets:
        if net_income > limit:
            taxable = limit - prev_limit
        else:
            taxable = net_income - prev_limit

        if taxable > 0:
            tax += taxable * rate

        if net_income <= limit:
            break

        prev_limit = limit
    return int(tax)

def main():
    '''
    main
    '''
    net_income = int(input())
    print(calculate_tax(net_income))
if __name__ == "__main__":
    main()
