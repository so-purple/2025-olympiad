from sys import stdin
from collections import deque
input = stdin.readline

def compute(N: int) -> int:
    q = deque([i for i in range(1, N + 1)])
    now = -1
    while q:
        now = q.popleft()
        if not q:
            break
        q.append(q.popleft())
    return now

if __name__ == "__main__":
    print(compute(int(input())))
