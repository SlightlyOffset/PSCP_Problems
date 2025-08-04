'''
head legs
'''

def main():
    '''
    main
    '''
    a = int(input())    # total
    b = int(input())    # legs

    bird = (b - 2*a)/2

    rabbit = a - bird

    if bird >= 0 and rabbit >= 0 and bird.is_integer() and rabbit.is_integer():
        print(int(bird), int(rabbit))
    else:
        print('Impossible')
if __name__ == "__main__":
    main()
