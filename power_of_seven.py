'''
seven
'''
def get_first_digit(expo):
    '''
    return first digit of seven to the p0wer of n
    '''
    digit_cycle = [7, 9 , 3, 1]
    cycle_index = (expo - 1) % 4
    return digit_cycle[cycle_index]

def main():
    '''
    main
    '''
    expo = int(input())
    print(get_first_digit(expo))
if __name__ == "__main__":
    main()
