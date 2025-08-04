'''
Season
'''

def main():
    '''
    main
    '''
    month = int(input())
    day = int(input())

    season_pointer = 0
    season = ["winter", "spring", "summer", "fall"]
    match month:
        case 1 | 2 | 3:     # Winter
            season_pointer = 0
        case 4 | 5 | 6:     # Spring
            season_pointer = 1
        case 7 | 8 | 9:     # Summer
            season_pointer = 2
        case 10 | 11 | 12:  # Fall
            season_pointer = 3

    if day >= 21 and not month % 3:
        season_pointer += 1
        if season_pointer > 3:
            season_pointer = 0

    print(season[season_pointer])

if __name__ == "__main__":
    main()
