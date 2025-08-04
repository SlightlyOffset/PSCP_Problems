'''
fivex
'''

def main():
    '''
    main
    '''
    print(''.join(('X' if not number % 5 else '*' for number in range(1, int(input())+1))))
if __name__ == "__main__":
    main()
