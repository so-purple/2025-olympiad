from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    is_passed = True
    try:
        eval(input().strip())
    except SyntaxError:
        is_passed = False
    except TypeError:
        is_passed = False
    print('YES' if is_passed else 'NO')
