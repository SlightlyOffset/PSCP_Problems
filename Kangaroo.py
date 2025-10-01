'''Kangaroo'''
def main():
    '''main'''
    a = int(input())
    b = int(input())
    c = int(input())
    print(max(b - a, c - b) - 1)
if __name__ == "__main__":
    main()
