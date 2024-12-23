def parse_input(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid

def find_guard_position_and_direction(grid):
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                return (x, y), directions[cell]
    return None, None

def turn_right(direction):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    idx = directions.index(direction)
    return directions[(idx + 1) % 4]

def simulate_patrol(grid):
    guard_pos, guard_dir = find_guard_position_and_direction(grid)
    if not guard_pos or not guard_dir:
        return 0

    visited = set()
    rows, cols = len(grid), len(grid[0])
    x, y = guard_pos
    dx, dy = guard_dir

    while 0 <= x < cols and 0 <= y < rows:
        visited.add((x, y))

        # Determine the next position
        nx, ny = x + dx, y + dy

        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] != '#':
            # Move forward if there's no obstacle
            x, y = nx, ny
        else:
            # Turn right if there's an obstacle
            dx, dy = turn_right((dx, dy))

    return len(visited)

def main(file_path):
    grid = parse_input(file_path)
    distinct_positions = simulate_patrol(grid)
    print(f"Distinct positions visited: {distinct_positions}")

# Usage
file_path = "C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt"
main(file_path)
