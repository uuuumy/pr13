sladkoezhkin = input().split()
N = int(input())
friends = set()

for _ in range(N):
    prefer = input().split() # предпочтения
    for p in prefer:
        friends.add(p)

only_sladkoezhkin = [p for p in sladkoezhkin if p not in friends]

print(len(only_sladkoezhkin))