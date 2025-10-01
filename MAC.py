'''MAC address'''
def check_format(seperator, mac_list):
    '''check format'''
    def check_char(octet):
        '''check char'''
        valid_char = "0123456789ABCDEF"
        for char in octet:
            if char.upper() not in valid_char:
                return False
        return True

    match seperator:
        case "-" | ":":
            if len(mac_list) != 6:
                return False
            for octet in mac_list:
                if len(octet) != 2 or not check_char(octet):
                    return False
        case ".":
            if len(mac_list) != 3:
                return False
            for octet in mac_list:
                if len(octet) != 4 or not check_char(octet):
                    return False
        case _:
            return False
    return True

def main():
    '''main'''
    mac_in = input()
    mac_type = None
    valid = True # assume valid MAC format
    if '-' in mac_in:
        mac_type = 1
        mac_list = mac_in.split("-")
        valid = check_format("-", mac_list)

    elif ':' in mac_in:
        mac_type = 2
        mac_list = mac_in.split(":")
        valid = check_format(":", mac_list)

    elif "." in mac_in:
        mac_type = 3
        mac_list = mac_in.split(".")
        valid = check_format(".", mac_list)
    else:
        valid = False

    if valid:
        print(f"VALID {mac_type}")
    else:
        print("ERROR")
if __name__ == "__main__":
    main()
