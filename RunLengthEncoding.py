'''
Run length encoding
'''

def main():
    '''
    main
    '''
    seq_in = input()
    if not seq_in:
        print("")
        return

    encoded = []
    count = 1
    for i in range(1, len(seq_in)):
        if seq_in[i] == seq_in[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{seq_in[i - 1]}")
            count = 1

    encoded.append(f"{count}{seq_in[-1]}")
    print(''.join(encoded))
if __name__ == "__main__":
    main()
