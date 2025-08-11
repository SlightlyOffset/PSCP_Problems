def main():
    """
    Generates a grid of sequential numbers based on user input.
    Each row contains 'n' numbers, and there are 'm' rows in total.
    """

    # Get the number of rows (m) and columns (n) from user input
    m = int(input("Enter number of rows (m): "))
    n = int(input("Enter number of columns (n): "))

    # Create the grid as a list of strings, each representing a row
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            number = i * n + j + 1
            row.append(str(number))
        grid.append(" ".join(row))

    # Print the grid line by line
    for line in grid:
        print(line)

if __name__ == "__main__":
    main()