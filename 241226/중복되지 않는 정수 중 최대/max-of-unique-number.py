N = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
for i in l:
    if l.count(i)>1:
        while i in l:
            l.remove(i)

print(max(l))


