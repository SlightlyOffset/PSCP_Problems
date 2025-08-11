'''
hamming
'''

def main():
    '''
    main
    '''
    string_1 = input()
    string_2 = input()
    str_difference = 0
    for index, letter in enumerate(string_1):
        if letter == string_2[index]:
            continue
        str_difference += 1
    print(str_difference)
if __name__ == "__main__":
    main()
