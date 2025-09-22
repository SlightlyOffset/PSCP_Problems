'''RemoveTag'''
def main():
    '''main'''
    raw_txt = input()

    # Replace tags with spaces to separate words
    processed_text = ""
    is_in_tag = False
    for char in raw_txt:
        if char == '<':
            is_in_tag = True
            processed_text += " " # Add space to separate text before tag
        elif char == '>':
            is_in_tag = False
            processed_text += " " # Add space to separate text after tag
        elif not is_in_tag:
            processed_text += char

    # Split by spaces and filter out empty strings
    # Using list comprehension for conciseness
    extracted_words = [word for word in processed_text.split() if word]

    print(extracted_words)

if __name__ == '__main__':
    main()
