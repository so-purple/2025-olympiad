from sys import stdin
input = stdin.readline

def compute(n: str) -> bool:
    ln = len(n)
    mid = ln // 2

    for i in range(mid):
        if n[i] != n[-(i + 1)]:
            return False
    return True

if __name__ =='__main__':
    while True:
        # 입력 부분
        # 0이 입력되면 반복 중단
        n = input().strip()
        if n == '0':
            break
        print('yes' if compute(n) else 'no')
