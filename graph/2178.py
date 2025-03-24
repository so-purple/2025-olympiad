from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
_map = [[each == '1' for each in input().strip()] for _ in range(m)]
distance = [[int(1e10) for _i in range(n)] for _j in range(m)]
# _map[a][b]  (a, b) True: 이동 가능 / False: 이동 불가능

q = deque((0, 0))
distance[0][0] = 0

while q:
    y, x = q.popleft()
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < m):
            continue
        if not _map[ny][nx]:
            continue
        q.append((ny, nx))
        distance[ny][nx] = min(distance[ny][nx], distance[y][x] + 1)

print(distance[n - 1][m - 1])
