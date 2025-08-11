'''
sequence VII
'''

def main():
    '''
    main
    '''
    x = int(input())
    seq = []
    for i in range(1, x+1):
        seq.append(i)
        print(' '.join(map(str, seq)))
    for _ in range(x - 1):
        seq.pop()
        print(' '.join(map(str, seq)))
if __name__ == "__main__":
    main()
