from sys import stdin
input = stdin.readline

def compute(N: int) -> list | None:
    n = N
    components = [1]
    for i in range(2, N // 2 + 1):
        if n == 0:
            break
        if n % i == 0:
            components.append(i)
    return components if sum(components) == N else None

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == -1:
            break
        computed = compute(n)
        if computed:
            print(f"{n} = " + " + ".join(map(str, computed)))
        else:
            print(f"{n} is NOT perfect.")
