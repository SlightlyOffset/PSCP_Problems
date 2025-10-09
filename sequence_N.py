'''Sequence N'''
def main():
    '''main'''
    n = int(input())
    for i in range(1, n+1):
        output = ''
        for j in range(1, n+1):
            if j in (i, n, 1):
                output += '*'
            else:
                output += ' '
        print(output)
if __name__ == "__main__":
    main()
