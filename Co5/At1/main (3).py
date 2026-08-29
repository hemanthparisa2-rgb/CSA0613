N = 9

def is_safe(grid, row, col, num):
    for i in range(N):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    sr = row - row % 3
    sc = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[sr + i][sc + j] == num:
                return False

    if row == col:
        for i in range(N):
            if grid[i][i] == num:
                return False

    if row + col == N - 1:
        for i in range(N):
            if grid[i][N - 1 - i] == num:
                return False

    return True


def solve(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:

                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num

                        if solve(grid):
                            return True

                        grid[row][col] = 0

                return False

    return True


def print_grid(grid):
    for row in grid:
        print(*row)


grid = [
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Diagonal Sudoku Solver")
print("----------------------")

if solve(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")