'''CaesarV2'''
import re

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

def find_decryption(message, common_words):
    '''Tries all shifts to find a decryption containing a common word.'''
    for shift in range(1, 26):
        # To decrypt, we shift backwards. A positive shift of N is undone by a negative shift of N.
        decrypted_message = shifting(message, -shift)
        # Count how many common words are found.
        found_counter = 0
        # Use regex to find all alphabetic words, ignoring attached punctuation.
        for word in re.findall(r'[a-zA-Z]+', decrypted_message.lower()):
            if word in common_words:
                # If a common word is found, increment found counter by 1.
                found_counter += 1
                if found_counter >= 2:
                    # If two or more common words are found, we assume this is the correct shift.
                    return decrypted_message

    return None

def main():
    '''main'''
    # Using a set provides faster lookups
    common_words = {
        "what", "when", "why", "which", "this", "there", "where",
        "the", "is", "am", "are", "you", "we", "they", "he", "she", "it",
        "and", "but", "or", "not", "for", "with", "have", "had", "has", "do", "does", "did",
        "can", "could", "will", "would", "should", "may", "might", "must", "been", "being"
    }

    message = input()
    decrypted_message = find_decryption(message, common_words)
    if decrypted_message:
        print(decrypted_message)

if __name__ == '__main__':
    main()
