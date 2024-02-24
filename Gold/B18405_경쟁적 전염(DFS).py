n, k = map(int, input().split())
lab = []
visited = [[0]* n for _ in range(n)]
for i in range(n):
    lab.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for time in range(s):
    for virus in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if lab[i][j] == virus and visited[i][j] == time:
                    visited[i][j] = time
                    for way in range(4):
                        if i+ dx[way] >= 0 and i+dx[way] < n and j+dy[way] >= 0 and j+dy[way] < n:
                            if lab[i+dx[way]][j+dy[way]] == 0:
                                lab[i + dx[way]][j + dy[way]] = virus
                                visited[i + dx[way]][j + dy[way]] = time+1
        #print(lab)

print(lab[x-1][y-1])
#print(lab)