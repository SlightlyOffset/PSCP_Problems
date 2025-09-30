'''Stair'''
def main():
    '''main'''
    max_step_lenght = int(input())
    stair_step = int(input())
    steps = [int(input()) for _ in range(stair_step)]

    possible = True     # assume True
    if max_step_lenght < max(steps):
        possible = False

    step_counter = 0
    lenght = 0
    if possible:
        for step in steps:
            lenght += step
            if lenght > max_step_lenght:
                step_counter += 1 # Count the previous step group
                lenght = step     # Start a new step group with the current step

    # account for last step if needed
    step_counter += 1 if lenght > 0 else 0
    print(step_counter if possible else "NO")

if __name__ == "__main__":
    main()
