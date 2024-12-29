n = int(input())
arr = [
    input()
    for _ in range(n)
]

total = 0
cnt = 0
for i in arr:
    if i[0] == 'a':
        cnt += 1
    total += len(i)
print(total, cnt)