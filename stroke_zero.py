'''
Stroke Zero
'''

def main():
    '''
    main
    '''
    zero = ["0"]
    limit = int(input())
    for edge in range(1,limit+1):
        if edge > 2 and edge != limit:
            print(f"0{" 1" * (edge - 2)} 0")
        else:
            print(' '.join(edge * zero))

if __name__ == "__main__":
    main()
