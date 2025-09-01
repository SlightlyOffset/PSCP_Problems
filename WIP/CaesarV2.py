'''CaesarV2'''
def shifting(message, shift):
    '''shift and return the message'''
    new_message_parts = []
    for char in message:
        if not char.isalpha():
            new_message_parts.append(char)
            continue

        # Determine the correct alphabet start ('a' or 'A')
        start = ord('a') if char.islower() else ord('A')

        # Apply the shift
        char_code = ord(char)
        new_char_code = ((char_code - start + shift) % 26) + start
        new_message_parts.append(chr(new_char_code))

    return "".join(new_message_parts)

def main():
    '''main'''
    # Using a set provides faster lookups
    common_words = {
        "what", "when", "why", "which", "this", "there", "where",
        "the", "is", "am", "are", "you", "we", "they", "he", "she",
        "it"
    }

    message = input()
    for shift in range(1, 26):
        # To decrypt, we shift backwards. A positive shift of N is undone by a negative shift of N.
        decrypted_message = shifting(message, -shift)
        word_list = decrypted_message.lower().split()
        for word in word_list:
            if word in common_words:
                # If a common word is found, we assume this is the correct shift.
                # Print the results and exit the function immediately.
                print(decrypted_message)
                return

if __name__ == '__main__':
    main()
