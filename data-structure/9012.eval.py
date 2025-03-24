from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    is_passed = True
    try:
        eval(input().strip())
    except SyntaxError:
        is_passed = False
    except TypeError:
        # In case of `()()`
        # Python raises "TypeError: 'tuple' object is not callable"
        pass
    print('YES' if is_passed else 'NO')
