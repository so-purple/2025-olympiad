from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    gets = set([int(input()) % 42 for _ in range(10)])
    print(len(gets))
