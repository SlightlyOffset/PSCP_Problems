'''TicTacToe'''
def main():
    '''main'''
    a = input()
    b = input()
    c = input()

    # Define all winning line
    lines = [
        a[0] + a[1] + a[1],     # Row 1
        b[0] + b[1] + b[2],     # Row 2
        c[0] + c[1] + c[2],     # Row 3
        a[0] + b[0] + c[0],     # Col 1
        a[1] + b[1] + c[1],     # Col 2
        a[2] + b[2] + c[2],     # Col 3
        a[0] + b[1] + c[2],     # Diag 1
        a[2] + b[1] + c[0]      # Diag 2
    ]

    # Check if XXX or OOO is in the l1st
    if "XXX" in lines:
        print("X WIN")
    elif "OOO" in lines:
        print("O WIN")
    else:
        print("DRAW")
if __name__ == '__main__':
    main()
