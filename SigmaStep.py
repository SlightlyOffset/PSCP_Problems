'''
SigmaStep
'''

def main():
    '''
    main
    '''
    total = 0
    x = int(input())
    y = int(input())
    n = int(input())
    try:
        if y < x:
            for num in range(x ,y-1, n):
                total += num
        else:
            for num in range(x ,y+1, n):
                total += num
        print(total)
    except ValueError:
        print("error")
if __name__ == "__main__":
    main()
