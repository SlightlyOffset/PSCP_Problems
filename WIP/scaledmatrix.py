"""ScaledMatrix"""

def print_matrix(rows, cols, data_list):
    """Matrix constructor"""
    for i in range(rows):
        for j in range(cols):
            if j != cols - 1:
                print(f"{data_list[(i * cols) + j]:.2f} ", end="")
            else:
                print(f"{data_list[(i * cols) + j]:.2f}")

def main():
    """main"""
    rows = int(input())
    cols = int(input())
    num_elements = rows * cols
    original_list = []
    for _ in range(num_elements):
        original_list.append(float(input()))

    min_val = min(original_list)

    # Step 1: Subtract the minimum value from each element
    shifted_list = [x - min_val for x in original_list]

    # Step 2: Divide by the maximum value of the shifted list
    max_shifted_val = max(shifted_list)
    scaled_list = [x / max_shifted_val for x in shifted_list]

    print_matrix(rows, cols, scaled_list)


if __name__ == "__main__":
    main()
