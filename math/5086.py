from sys import stdin
input = stdin.readline

def compute(a: int, b: int) -> str:
    if b % a == 0:
        return 'factor'
    if a % b == 0:
        return 'multiple'
    return 'neither'
    
if __name__ == "__main__":
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        print(compute(a, b))
