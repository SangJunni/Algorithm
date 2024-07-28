def read_grid():
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    return H, W, grid


def get_coin_positions(H, W, grid):
    positions = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 'O':
                positions.append((r, c))
    return positions


def min_moves_to_match(source_positions, target_positions):
    min_moves = float('inf')
    max_shift = 10  # From -10 to 10

    # Iterate over all possible shifts (a, b)
    for a in range(-max_shift, max_shift + 1):
        for b in range(-max_shift, max_shift + 1):
            shifted_target_positions = [(x + a, y + b) for x, y in target_positions]
            # Check how many coins are misplaced
            misplaced = 0
            target_set = set(shifted_target_positions)
            for s in source_positions:
                if s not in target_set:
                    misplaced += 1
            min_moves = min(min_moves, misplaced)

    return min_moves


# Read the first grid
H1, W1, grid1 = read_grid()
# Read the second grid
H2, W2, grid2 = read_grid()

# Get coin positions in both grids
source_positions = get_coin_positions(H1, W1, grid1)
target_positions = get_coin_positions(H2, W2, grid2)

# Calculate minimum moves
result = min_moves_to_match(source_positions, target_positions)

print(result)
