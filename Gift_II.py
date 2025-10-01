'''Gift II'''
def recursion(num):
    '''recursion'''
    if not num % 2:
        return num
    return recursion(int(input()))

def main():
    '''main'''
    print(recursion(int(input())))
if __name__ == '__main__':
    main()
