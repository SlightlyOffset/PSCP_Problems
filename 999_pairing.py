'''
999 pairing
'''

def main():
    '''
    main
    '''
    length = int(input())
    seq_1 = input()
    seq_2 = input()

    index = 0
    non_valid = 0
    is_valid = True     # Assume true
    while index < length:
        if int(seq_1[index]) + int(seq_2[index]) != 9:
            is_valid = False
            non_valid += 1
        index += 1
    print("YES" if is_valid else f"NO {non_valid}")
if __name__ == "__main__":
    main()
