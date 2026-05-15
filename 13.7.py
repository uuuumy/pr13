from itertools import permutations

nums = sorted(set(map(int, input().split())))
for p in permutations(nums):
    print(*p)