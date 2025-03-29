from sys import stdin
from collections import deque
input = stdin.readline

def compute(N: int, req: list) -> list | None:
    peek = 0
    simq = deque()
    oper = []  # True: + / False: -
    for each in req:
        while each > peek:
            peek += 1
            simq.append(peek)
            oper.append(True)
        now = simq.pop()
        oper.append(False)
        if now != each:
            return None
    return oper

if __name__ == "__main__":
    N = int(input())
    req = [int(input()) for _i in range(N)]
    computed = compute(N, req)
    if not computed:
        print("NO")
    else:
        for each in computed:
            print("+" if each else "-")
