from sys import stdin
input = stdin.readline

def compute(gets: list[list[str]]):
    _dict = {}
    for age, name in gets:
        age = int(age)
        if age not in _dict:
            _dict[age] = [name]
        else:
            _dict[age].append(name)
    for age in sorted(_dict.keys()):
        for name in _dict[age]:
            print(f'{age} {name}')

if __name__ == '__main__':
    n = int(input())
    compute([input().split() for _ in range(n)])
