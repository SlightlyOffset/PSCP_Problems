'''
pongya
'''

def main():
    '''
    main
    '''
    number = input()
    print("PONG" if not int(number) % 3 or number[-1] == "3" else number)

if __name__ == "__main__":
    main()
