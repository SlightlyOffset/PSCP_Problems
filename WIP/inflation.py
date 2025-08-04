'''
inflation
'''
from math import floor
def trunc(number, dplace):
    '''
    Return a truncated version of the input number up to dplace
    '''
    return floor(number * 10 ** dplace) / 10 ** dplace

def main():
    '''
    main
    '''
    P = float(input())
    n = int(input())
    rate = 3.81/100

    inflation = P * ((1 + rate) ** n)
    print(trunc(inflation, 2))
if __name__ == "__main__":
    main()