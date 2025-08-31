'''
Shorten
'''

def main():
    '''
    main
    '''
    output = ''
    num_str = ''
    while True:
        num_in = int(input())
        if num_in == -1:
            break
        num_str += str(num_in)

    current_num = None
    
    print(num_str)
if __name__ == "__main__":
    main()
