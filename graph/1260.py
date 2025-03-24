from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline
setrecursionlimit(1000)

class DFSInvoker:
    def __init__(self, N, M, V, conn):
        self.N = N
        self.M = M
        self.V = V
        self.conn = conn
        self.visited = [False for _ in range(self.N + 1)]
        self.result = []
    
    def step(self, now: int):
        if self.visited[now]:
            return
        self.result.append(now)
        self.visited[now] = True
        for next in conn[now]:
            if self.visited[next]:
                continue
            self.step(next)

def dfs(N, M, V, conn):
    invoker = DFSInvoker(N, M, V, conn)
    invoker.step(V)
    return invoker.result

def bfs(N, M, V, conn):
    # Init
    visited = [False for _ in range(N + 1)]
    result = []
    q: deque[int] = deque()
    q.append(V)

    while q:
        now: int = q.popleft()
        if visited[now]:
            continue
        result.append(now)
        visited[now] = True
        for next in conn[now]:
            if visited[next]:
                continue
            q.append(next)

    return result

if __name__ == '__main__':
    N, M, V = map(int, input().split())
    
    conn: dict[int, list[int]] = {}
    for _ in range(M):
        a, b = map(int, input().split())
        if a not in conn:
            conn[a] = []
        if b not in conn:
            conn[b] = []
        conn[a].append(b)
        conn[b].append(a)
    # 정점 번호가 더 작은 것을 먼저 방문하므로
    for key in conn:
        conn[key].sort()
    
    print(*dfs(N, M, V, conn))
    print(*bfs(N, M, V, conn))
