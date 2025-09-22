'''RemoveTag'''
def main():
    '''main'''
    extracted_list = []
    extracted_txt = ''
    raw_txt = input()
    in_tag = False
    for char in raw_txt:
        if char == '<':
            in_tag = True
            if not extracted_txt:
                continue
            extracted_list.append(extracted_txt.strip())
            extracted_txt = ''
            continue
        if char == '>':
            in_tag = False
            continue
        if not in_tag:
            if char == ' ':
                extracted_list.append(extracted_txt.strip())
                extracted_txt = ''
                continue
            extracted_txt += char

    # Add last segment if exists
    if extracted_txt:
        extracted_list.append(extracted_txt.strip())

    print([text for text in extracted_list if text])

if __name__ == '__main__':
    main()
