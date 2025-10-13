n = int(input())
m = int(input())

# Read grid
grid = [list(map(int, input().split())) for _ in range(n)]
direction = input().strip()

def render_view(lines, width):
    height = max(max(row) for row in lines)
    output = []
    for level in range(height, 0, -1):
        row = ''
        for count in lines:
            row += 'x' if count >= level else ' '
        output.append(row)
    return output

if direction == "Front":
    # Front: max per column from top to bottom
    view = [max(grid[i][j] for i in range(n)) for j in range(m)]
    result = render_view(view, m)

elif direction == "Back":
    # Back: same as Front but reversed column order
    view = [max(grid[i][j] for i in range(n)) for j in reversed(range(m))]
    result = render_view(view, m)

elif direction == "Left":
    # Left: max per row from left to right
    view = [max(row) for row in grid]
    result = render_view(view, n)

elif direction == "Right":
    # Right: same as Left but reversed row order
    view = [max(row) for row in reversed(grid)]
    result = render_view(view, n)

# Print result
for line in result:
    print(line)
