"""Saitama"""
def main():
    """Find M1nimum day"""
    target_1 = int(input())
    target_2 = int(input())
    target_3 = int(input())
    target_4 = int(input())
    perday_1 = int(input())
    perday_2 = int(input())
    perday_4 = int(input())
    perday_3 = int(input())
    require_day = 0
    require_day2 = 0
    for _ in range(0,target_1,perday_1):
        require_day += 1
    for _ in range(0,target_2,perday_2):
        require_day2 += 1
    if require_day2 > require_day:
        require_day = require_day2
    require_day2 = 0
    for _ in range(0,target_3,perday_3):
        require_day2 += 1
    if require_day2 > require_day:
        require_day = require_day2
    require_day2 = 0
    for _ in range(0,target_4,perday_4):
        require_day2 += 1
    if require_day2 > require_day:
        require_day = require_day2
    require_day2 = 0
    print(require_day)
if __name__ == "__main__":
    main()
