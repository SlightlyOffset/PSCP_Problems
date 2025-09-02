'''Chonk Rabbit'''
def main():
    '''main'''
    n = int(input())
    rabbit = {}
    for _ in range(n):
        name, weight = input().split()
        weight = int(weight)
        rabbit[name] = weight
    print(rabbit)
if __name__ == "__main__":
    main()
