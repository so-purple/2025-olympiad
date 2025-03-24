nums = []
for _ in range(int(input())):
    get = int(input())
    if get != 0:
        nums.append(get)
    else:
        nums.pop()

print(sum(nums))
