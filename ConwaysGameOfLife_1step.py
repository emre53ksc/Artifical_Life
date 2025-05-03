import itertools
# Conway's Game Of Life
# this code finds configuraitons with 1 step lifespan
# and at least 1 crowd death


def get_neighbors(x, y, rows, cols):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),         ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def count_alive_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    neighbors = get_neighbors(x, y, rows, cols)
    return sum(grid[nx][ny] for nx, ny in neighbors)

def has_no_survivors_or_births(grid):
    rows, cols = len(grid), len(grid[0])
    for x in range(rows):
        for y in range(cols):
            alive_neighbors = count_alive_neighbors(grid, x, y)
            if grid[x][y] == 1:
                if alive_neighbors == 2 or alive_neighbors == 3:
                    return False  # living cell continues to live
            else:
                if alive_neighbors == 3:
                    return False  # new cell born
    # No living cells or births found
    return True

def has_overcrowding_death(grid):
    rows, cols = len(grid), len(grid[0])
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                alive_neighbors = count_alive_neighbors(grid, x, y)
                if alive_neighbors > 3:
                    return True  # overcrowding death occurs
    # No overcrowding deaths found
    return False

def generate_all_combinations(rows, cols):
    total_cells = rows * cols
    for bits in itertools.product([0, 1], repeat=total_cells):
        grid = [[0]*cols for _ in range(rows)]
        for idx, val in enumerate(bits):
            r, c = divmod(idx, cols)
            grid[r][c] = val
        yield grid

def get_alive_cells(grid):
    alive = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                alive.append((i, j))
    return alive

def main():
    rows = int(input("row count: "))
    cols = int(input("columns count: "))
    print("searching...")

    found = []
    for grid in generate_all_combinations(rows, cols):
        if has_no_survivors_or_births(grid) and has_overcrowding_death(grid):
            found.append(get_alive_cells(grid))

    print(f"\n1 step completely dead and overcrowding death combinations found: ({len(found)} found):")
    for idx, combo in enumerate(found, 1):
        print(f"{idx}. {combo}")

if __name__ == "__main__":
    main()
