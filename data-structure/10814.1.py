from sys import stdin
input = stdin.readline

def compute(gets: list[list[str]]):
    _list = []
    ln = len(gets)
    for i in range(ln):
        age, name = gets[i]
        age = int(age)
        _list.append([age, name, i])
    for row in sorted(_list,
        key=lambda each: (each[0], each[2])
    ):
        print(*row[:2])
        
if __name__ == '__main__':
    n = int(input())
    compute([input().split() for _ in range(n)])
