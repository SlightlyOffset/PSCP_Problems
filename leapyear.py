'''
leap year
'''

def main():
    '''
    main
    '''
    year = int(input())
    if (not year % 4 and year % 100) or (not year % 400):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
