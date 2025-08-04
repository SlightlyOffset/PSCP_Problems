'''
Right Arrow
'''

def main():
    '''
    main
    '''
    arrow_construct = ["*"]
    width = int(input())
    height = int(input())
    arrow_construct_str = ''.join(arrow_construct * width)

    halfway_limit = (height - 1) // 2
    current = 0
    while current < halfway_limit:
        print(f"{" " * current}{arrow_construct_str}")
        current += 1

    current = halfway_limit
    while current >= 0:
        print(f"{" " * current}{arrow_construct_str}")
        current -= 1
if __name__ == "__main__":
    main()
