from sys import stdin
from collections import deque
input = stdin.readline

def compute(N: int, M: int, q: list) -> int:
    dq = deque(q)
    targeted = M
    printed = 0
    while dq:
        _max = max(dq)
        now = dq.popleft()

        if _max == now:
            printed += 1
            if targeted == 0:
                return printed
        else:
            dq.append(now)
        targeted -= 1
        if targeted < 0:
            targeted += len(dq)

if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int, input().split())
        q = [*map(int, input().split())]
        print(compute(N, M, q))
