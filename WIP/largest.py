'''
largest
'''

def main():
    '''
    cal
    '''
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 >= num2 and num2 >= num3:
        locate = [num1, num2, num3]
    elif num1 >= num3 and num3 >= num2:
        locate = [num1, num3, num2]
    elif num2 >= num1 and num1 >= num3:
        locate = [num2, num1, num3]
    elif num2 >= num3 and num3 >= num1:
        locate = [num2, num3, num1]
    elif num3 >= num1 and num1 >= num2:
        locate = [num3, num1, num2]
    else:
        locate = [num3, num2, num1]

    print(locate[0], locate[1], locate[2], sep = "")

if __name__ == "__main__":
    main()