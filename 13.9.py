from itertools import combinations

a = sorted(set(map(int, input().split())))
k = int(input())
for comb in combinations(a, k):
    print(*comb)