from sys import stdin
input = stdin.readline

def compute(n: int, k: int) -> int:
    res = 1
    for i in range(n, n - k, -1):
        res *= i
    for i in range(1, k + 1):
        res //= i
    return res

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(compute(n, k))
