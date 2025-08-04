'''
bubble tea
'''
def estimate_cal(btype, amo, ttype, swtl, vol):
    '''
    estimate calorie gain
    '''
    estimate = 0
    match btype:
        case "H":       # 5 cal for base multiply by amount(gram)
            estimate += 5 * int(amo)
        case "O":       # 3 cal for base multiply by amount(gram)
            estimate += 3 * int(amo)
        case "J":       # 2 cal for base multiply by amount(gram)
            estimate += 2 * int(amo)

    match ttype:
        case "R":       # Rose tea
            match swtl:
                case "1":       # Sweetness level 1
                    estimate += 12 * int(vol)        # 12 cal base multiply by volume(cc)
                case "2":       # Sweetness level 2
                    estimate += 18 * int(vol)        # 18 cal base multiply by volume(cc)
                case "3":       # Sweetness level 3
                    estimate += 25 * int(vol)        # 25 cal base multiply by volume(cc)
        case "T":       # Taiwan tea
            match swtl:
                case "1":       # Sweetness level 1
                    estimate += 15 * int(vol)        # 15 cal base multiply by volume(cc)
                case "2":       # Sweetness level 2
                    estimate += 20 * int(vol)        # 20 cal base multiply by volume(cc)
                case "3":       # Sweetness level 3
                    estimate += 30 * int(vol)        # 30 cal base multiply by volume(cc)
        case "M":       # Macha tea
            match swtl:
                case "1":       # Sweetness level 1
                    estimate += 10 * int(vol)        # 10 cal base multiply by volume(cc)
                case "2":       # Sweetness level 2
                    estimate += 15 * int(vol)        # 15 cal base multiply by volume(cc)
                case "3":       # Sweetness level 3
                    estimate += 20 * int(vol)        # 20 cal base multiply by volume(cc)
    return estimate
def main():
    '''
    main
    '''
    boba = input()
    tea = input()
    boba_type, amount = boba.split()
    tea_type, sweetness_level, volume = tea.split()
    print(estimate_cal(boba_type, amount, tea_type, sweetness_level, volume))
if __name__ == "__main__":
    main()
