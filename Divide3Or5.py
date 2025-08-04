'''
Divide3Or5
'''

def main():
    '''
    main
    '''
    print(sum(number for number in range(1, int(input())+1) if not number % 3 or not number % 5))
if __name__ == "__main__":
    main()
