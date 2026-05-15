from itertools import combinations

a = sorted(set(map(int, input().split())))
for r in range(len(a) + 1):
    for sub in combinations(a, r):
        print(*sub)