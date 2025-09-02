'''Chonk Rabbit'''

OVERWEIGHT_THRESHOLD = 15

def get_overweight_rabbits(all_rabbits):
    '''Filters a list of rabbits, returning only the overweight ones.'''
    return [rabbit for rabbit in all_rabbits if rabbit[1] > OVERWEIGHT_THRESHOLD]

def main():
    '''main'''
    n = int(input())
    all_rabbits = []
    for _ in range(n):
        name, weight = input().split()
        weight = int(weight)
        all_rabbits.append((name, weight))

    overweight_rabbits = get_overweight_rabbits(all_rabbits)
    heaviest_rabbit = max(all_rabbits, key=lambda r: r[1])
    print(len(overweight_rabbits))
    print(heaviest_rabbit[0], heaviest_rabbit[1])
if __name__ == "__main__":
    main()
