def rotate_shell(shell, r):
    # Shell 길이
    length = len(shell)
    r %= length  # 실제로는 r번 회전하는 것이 아닌, r % length번 회전
    return shell[r:] + shell[:r]

def get_shell(matrix, x, y, layer):
    n, m = len(matrix), len(matrix[0])
    shell = []

    # 상단 가로
    for j in range(y + layer, m - layer):
        shell.append(matrix[x + layer][j])
    # 우측 세로
    for i in range(x + layer + 1, n - layer):
        shell.append(matrix[i][m - layer - 1])
    # 하단 가로
    for j in range(m - layer - 2, y + layer - 1, -1):
        shell.append(matrix[n - layer - 1][j])
    # 좌측 세로
    for i in range(n - layer - 2, x + layer, -1):
        shell.append(matrix[i][y + layer])

    return shell

def set_shell(matrix, x, y, layer, shell):
    n, m = len(matrix), len(matrix[0])
    idx = 0

    # 상단 가로
    for j in range(y + layer, m - layer):
        matrix[x + layer][j] = shell[idx]
        idx += 1
    # 우측 세로
    for i in range(x + layer + 1, n - layer):
        matrix[i][m - layer - 1] = shell[idx]
        idx += 1
    # 하단 가로
    for j in range(m - layer - 2, y + layer - 1, -1):
        matrix[n - layer - 1][j] = shell[idx]
        idx += 1
    # 좌측 세로
    for i in range(n - layer - 2, x + layer, -1):
        matrix[i][y + layer] = shell[idx]
        idx += 1

def rotate_matrix(matrix, r):
    n, m = len(matrix), len(matrix[0])
    layers = min(n, m) // 2

    for layer in range(layers):
        shell = get_shell(matrix, 0, 0, layer)
        rotated_shell = rotate_shell(shell, r)
        set_shell(matrix, 0, 0, layer, rotated_shell)

    return matrix

# 예제 입력
n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 배열 회전
rotated_matrix = rotate_matrix(matrix, r)

# 출력
for row in rotated_matrix:
    print(' '.join(map(str, row)))
