row = 5
col = 3

arr_2d = [
    list(input().split())
    for _ in range(row)
]

for i in range(row):
    for j in range(col):
        print(arr_2d[i][j].upper(), end=' ')
    print()