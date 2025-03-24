count = {}

for _ in range(10):
    n = int(input())
    if n not in count:
        count[n] = 0
    count[n] += 1

_max_count = -1
_max_value = -1
for key in count:
    if _max_count < count[key]:
        _max_count = count[key]
        _max_value = key

print(_max_value)
