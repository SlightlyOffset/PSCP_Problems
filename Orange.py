"""Orange"""
def remaining_layers(total_layer, saled):
    """ to calculate orange """
    layers = []

    for i in range(1, total_layer + 1):
        layers.append(i * i)

    for i in range(total_layer):
        if saled >= layers[i]:
            saled -= layers[i]
        else:
            return total_layer - i

    return 0

def main():
    '''main'''
    l = int(input())
    n = int(input())

    print(remaining_layers(l, n))

if __name__ == "__main__":
    main()
