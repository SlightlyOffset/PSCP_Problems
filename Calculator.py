"""Calculator"""
def main():
    '''main'''
    num = int(input())
    if num == 1:
        print(1)
    elif num > 1:
        count = 0
        for i in range(1, num + 1):
            ic = str(i)
            count += len(ic) + 1
        print(count)

if __name__ == "__main__":
    main()
