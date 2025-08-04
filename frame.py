'''
frame
'''

def main():
    '''
    main
    '''
    in_frame = input()
    framed = f"*{in_frame}*"

    print("*" * (len(in_frame) + 2))
    print(framed)
    print("*" * (len(in_frame) + 2))
if __name__ == "__main__":
    main()
