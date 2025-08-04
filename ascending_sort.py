'''
ascending sort
'''

def main():
    '''
    main
    '''
    print('\n'.join(map(str, sorted(int(input()) for _ in range(int(input()))))))
if __name__ == "__main__":
    main()
