'''
century
'''
from math import trunc
def get_century(year_in):
    '''
    return century
    '''
    def be_to_ad(be_year):
        '''
        convert B.E. to A.D.
        '''
        return be_year - 543 if be_year > 543 else False

    try:
        prefix, year = year_in.split()
        year = int(year)
        match prefix:
            case "B.E.":
                year = be_to_ad(year)
                if not year:
                    return "ERROR"
            case "A.D.":    # No conversion needed
                pass
            case _:
                return "ERROR"

        century = trunc(year / 100)
        if century * 100 < year:
            century += 1
        return century

    except ValueError:
        return "ERROR"

def main():
    '''
    main
    '''
    loop = int(input())
    for _ in range(loop):
        # Input will always be in B.E. {year} or A.D. {year} format
        print(get_century(input()))

if __name__ == "__main__":
    main()
