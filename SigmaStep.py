'''sigmastep'''
def main():
    '''main'''
    x = int(input())
    y = int(input())
    n = int(input())
    summ = 0
    if x == y:
        print(x)
    elif x == y == n == 0 or not n:
        print('error')
    elif x < y and n < 0:
        print('error')
    elif x > y and n >= 0:
        print('error')
    else:
        if n > 0:
            for i in range(x, y + 1, n):
                summ += i
            print(summ)
        else:
            for i in range(x, y - 1, n):
                summ += i
            print(summ)
main()
