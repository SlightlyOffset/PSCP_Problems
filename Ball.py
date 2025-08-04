'''
Ball
'''

def main():
    '''
    main
    '''
    initial_height = float(input())
    bounce_back = 0
    while initial_height > 0.01:
        initial_height = initial_height * (3/5)
        bounce_back += 1

    if bounce_back > 0:
        print(bounce_back - 1)
    else:
        print(bounce_back)
if __name__ == "__main__":
    main()
