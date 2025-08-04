'''
color
'''

def main():
    '''
    main
    '''
    color1 = input().lower().strip()
    color2 = input().lower().strip()

    if color1 == color2:
        print("Error")
    elif color1 in ["red", "yellow"] and color2 in ["red", "yellow"]:
        print("Orange")
    elif color1 in ["red", "blue"] and color2 in ["red", "blue"]:
        print("Violet")
    elif color1 in ["yellow", "blue"] and color2 in ["yellow", "blue"]:
        print("Green")
    else:
        print("Error")
if __name__ == "__main__":
    main()
