row, col = map(int, input().split())

arr = [
    [0 for _ in range(col)]
    for _ in range(row)
]
cnt = 1

for i in arr:
    for elem in i:
        print(elem+cnt, end=' ')
        cnt += 1
    print()
