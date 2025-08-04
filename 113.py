'''
113
'''

def main():
    '''
    main
    '''
    number_seq = input()
    no_more = False
    while not no_more:
        number_seq = number_seq.replace("113", "")
        if number_seq.find("113") == -1:
            no_more = True
    print(number_seq)
if __name__ == "__main__":
    main()
