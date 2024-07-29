def find_path(N, M, board):
    # Direction vectors for moving in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Check if a position is within the grid boundaries
    def in_bounds(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    # Perform DFS to find a valid path
    def dfs(x, y, current_sum, steps, path):
        if steps == M:
            if current_sum == N:
                return True, path
            else:
                return False, []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and (nx, ny) not in path:
                if steps % 2 == 0:  # This should be a number cell
                    if board[nx][ny].isdigit():
                        new_sum = current_sum + int(board[nx][ny]) if board[x][y] == '+' else current_sum - int(
                            board[nx][ny])
                        found, new_path = dfs(nx, ny, new_sum, steps + 1, path + [(nx, ny)])
                        if found:
                            return True, new_path
                else:  # This should be an operator cell
                    if board[nx][ny] in '+-':
                        found, new_path = dfs(nx, ny, current_sum, steps + 1, path + [(nx, ny)])
                        if found:
                            return True, new_path

        return False, []

    # Start DFS from all number cells
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                found, path = dfs(i, j, int(board[i][j]), 1, [(i, j)])
                if found:
                    return 1, path

    return 0, []


# Read input
N, M = map(int, input().split())
board = [input() for _ in range(3)]
result, path = find_path(N, 2*M-1, board)
print(result)
if result:
    for (x, y) in path:
        print(x, y)
