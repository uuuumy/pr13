first = set(input().split())
second = set(input().split())
n = input()

if n in (first & second):
    print('да')
else:
    print('нет')

