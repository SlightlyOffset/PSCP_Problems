'''
sum of all
'''

def main():
    '''
    main
    '''
    target = int(input())
    current = 0
    while current != target:
        num = int(input())
        if num == -1:
            break
        current += num
    print(current)
if __name__ == "__main__":
    main()
