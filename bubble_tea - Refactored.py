'''
bubble tea
'''
def estimate_cal(btype, amo, ttype, swtl, vol):
    '''
    estimate calorie gain
    '''

    # Base calorie per gram for boba types
    boba_calories = {
        "H" : 5,     # Honey boba
        "O" : 3,     # Original boba
        "J" : 2      # Jelly boba
    }

    # Base calorie per cc for tea type and sweetness levels (nested dictionaries)
    tea_calories = {
        "R" : {"1" : 12, "2" : 18, "3" : 25},       # Rose tea
        "T" : {"1" : 15, "2" : 20, "3" : 30},       # Taiwan tea
        "M" : {"1" : 10, "2" : 15, "3" : 20}        # Macha tea
    }

    estimate = 0
    estimate += boba_calories.get(btype, 0) * int(amo)
    estimate += tea_calories.get(ttype, {}).get(swtl, 0) * int(vol)
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
