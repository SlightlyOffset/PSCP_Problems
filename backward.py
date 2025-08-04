'''
backward
'''

def main():
    '''
    main
    '''
    print_list = []
    while True:
        input_str = input()
        if input_str == "NULL":
            break
        print_list.append(input_str)
    print('\n'.join(print_list[::-1]))
if __name__ == "__main__":
    main()
