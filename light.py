'''
light
'''

def main():
    '''
    main
    '''
    light = ["R", "G", "B"]
    light_order = []

    start_light = input().upper()
    amount = int(input())

    pointer = light.index(start_light)
    for _ in range(amount):
        if pointer > 2:
            pointer = 0
        light_order.append(light[pointer])
        pointer += 1

    translation_table = {
        "R" : "Red",
        "G" : "Green",
        "B" : "Blue"
    }

    translated_light_code = [translation_table[code] for code in light_order]
    print(" ".join(translated_light_code))
if __name__ == "__main__":
    main()
