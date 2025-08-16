'''
BrickBridge
'''
def main():
    '''
    main
    '''
    a = int(input())
    b = int(input())
    goal = int(input())
    big_used = min(b, goal//5)
    remaining = goal - big_used * 5
    print(remaining if remaining <= a else -1)
if __name__ == "__main__":
    main()
