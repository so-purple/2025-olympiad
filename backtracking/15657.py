from sys import stdin
input = stdin.readline

def compute(N: int, M: int, arr: list[int]):
    for each in arr:
        step(M, [each])

def step(M, collected):
    if len(collected) == M:
        print(*collected)
        return
    
    for each in arr:
        # 수열은 비내림차순이다
        # 모은 값들 중 가장 뒤 값이 현재 넣으려고 하는 값보다 작아야 한다
        if collected[-1] > each:
            # collected[-1] => len(collected)는 1 이상이어야 한다.
            continue
        collected.append(each)
        step(M, collected)
        collected.pop()

class Runner:
    def __init__(self, N, M, arr):
        self.N = N
        self.M = M
        self.arr = arr
        self.results = []
    
    def step(self, collected):
        if len(collected) == self.M:
            self.results.append(collected)
            return
        
        for each in self.arr:
            # 수열은 비내림차순이다
            # 모은 값들 중 가장 뒤 값이 현재 넣으려고 하는 값보다 작아야 한다
            if collected[-1] < each:
                # collected[-1] => len(collected)는 1 이상이어야 한다.
                continue
            collected.append(each)
            self.step(collected)
            collected.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = sorted([*map(int, input().split())])
    compute(N, M, arr)
