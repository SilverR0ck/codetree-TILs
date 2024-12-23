n = int(input())
l = list(map(int, input().split()))

m = min(l)
cnt = l.count(m)
print(m, cnt)