'''PhoneNumber'''
def format_from_right(phone_number):
    '''format phone number from right'''
    formatted_number = ''
    counter = 0
    for number in reversed(phone_number):       # Format from last digit to first
        formatted_number += number
        counter += 1
        if counter == 4:
            formatted_number += ' '
            counter = 0
    return ''.join(reversed(formatted_number))  # Undo the reverse and return

def main():
    '''main'''
    phone_number = input().strip()
    call = input().lower().strip()

    # Check call type if "International" or "Domestic"
    match call:
        case 'international':
            # format phone number for international
            print(f"+66{format_from_right(phone_number[1:])}")
        case 'domestic':
            # format phone number for domestic
            print(format_from_right(phone_number))

if __name__ == '__main__':
    main()
