import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []

for i in c:
    if i < b:
        d.append(i)

print(*d)
