'''Least vowel'''
# Given a long string of text
# (may contain noise such as special characters and number)
# Find and put together a new string of text
# Such that each word only contain one vowel

# main goal: Find word contianing only one vowel
import re
def has_one_vowel(word):
    '''check word for single vowel'''
    return len(re.findall(r'[aeiou]', word, re.IGNORECASE)) == 1

def main():
    '''main'''
    str_in = input()

    # 1. Remove punctuation, 2. Split into words, 3. Filter and print
    words = re.sub(r'[^a-zA-Z\s]', '', str_in).split()
    print(" ".join([word for word in words if has_one_vowel(word)]))
if __name__ == "__main__":
    main()
