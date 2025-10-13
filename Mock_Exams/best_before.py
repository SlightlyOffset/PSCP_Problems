'''best before'''
from datetime import datetime
def valid_date(date: str, pattern: str) -> bool:
    '''check for suitable date time format for given imput'''
    try:
        first = date[0:2]
        middle = date[2:4]
        year = date[4:6]

        match pattern:
            case 'ddmmyy':
                full_date_str = f'{first}{middle}{year}'
                full_date_format = '%d%m%y'
            case 'mmddyy':
                full_date_str = f'{first}{middle}{year}'
                full_date_format = '%m%d%y'
            case _:
                return False

        datetime.strptime(full_date_str, full_date_format)
        return True
    except ValueError:
        return False

def main():
    '''main'''
    check = int(input())
    date_to_check = [input() for _ in range(check)]
    all_dmy_valid = True
    all_mdy_valid = True
    for date in date_to_check:
        if not valid_date(date, pattern='ddmmyy'):
            all_dmy_valid = False
        if not valid_date(date, pattern='mmddyy'):
            all_mdy_valid = False
        if not all_dmy_valid and not all_mdy_valid:
            break

    if all_mdy_valid and not all_dmy_valid:
        print('mmddyy')
    elif all_dmy_valid and not all_mdy_valid:
        print('ddmmyy')
    else:
        print('no clue')
if __name__ == "__main__":
    main()
