'''CaesarV1'''
def main():
    '''main'''
    shift = int(input())
    message = input()
    new_message = ''
    for char in message:
        if char in [" ", ",", ".", "!", "?", "'", ":", ";", "-", "_", "\'"]:
            new_message += char
            continue
        char_code = ord(char)
        if 'a' <= char <= 'z':
            new_char_code = ((char_code - ord('a') + shift) % 26) + ord('a')
        elif 'A' <= char <= 'Z':
            new_char_code = ((char_code - ord('A') + shift) % 26) + ord('A')
        else:
            new_char_code = char_code
        new_message += chr(new_char_code)
    print(new_message)

if __name__ == '__main__':
    main()
