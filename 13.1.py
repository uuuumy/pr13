sequence = input().split()
n =input()

count = sequence.count(n)
if count > 1:
    print("да")
else:
    print("нет")