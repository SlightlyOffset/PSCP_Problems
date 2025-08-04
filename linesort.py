'''
line sort
'''

def main():
    '''
    main
    '''
    print('\n'.join(sorted((input() for _ in range(int(input()))), key=len)))
if __name__ == "__main__":
    main()
