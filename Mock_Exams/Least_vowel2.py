import re

def count_vowels(word):
    '''Count vowels in a word'''
    return len(re.findall(r'[aeiou]', word, re.IGNORECASE))

def main():
    '''Main function'''
    str_in = input()
    words = re.sub(r'[^a-zA-Z\s]', '', str_in).split()
    cleaned_words = [word for word in words if word.isalpha()]

    # Count vowels in each word
    vowel_counts = [(word, count_vowels(word)) for word in cleaned_words]
    if not vowel_counts:
        print("")
        return

    # Find minimum vowel count
    min_vowel = min(count for _, count in vowel_counts)

    # Print words with minimum vowel count
    result = [word for word, count in vowel_counts if count == min_vowel]
    print(" ".join(result))

if __name__ == "__main__":
    main()
