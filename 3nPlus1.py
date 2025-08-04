'''
3nPlus1
'''
def get_steps(num):
    '''
    return step require till reach 1
    '''
    step = 1    # Default 1
    while num != 1:
        if not num % 2:
            num = num // 2
        else:
            num = (num * 3) + 1
        step += 1
    return step

def main():
    '''
    main
    '''
    while True:
        num_in = int(input())
        if not num_in:
            break
        print(get_steps(num_in))

if __name__ == '__main__':
    main()
