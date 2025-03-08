from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    gets = input().strip()
    opens = 0
    invalid = False
    for each in gets:
        if each == '(':
            opens += 1
        else:
            if opens > 0:
                opens -= 1
            else:
                invalid = True
                break
    print('YES' if not invalid else 'NO')
