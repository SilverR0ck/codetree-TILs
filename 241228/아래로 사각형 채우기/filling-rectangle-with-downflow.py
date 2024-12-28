n = int(input())

# 배열 초기화
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt = 1
for j in range(n):
    for i in range(n):
        arr[i][j] = cnt
        cnt+=1


for i in arr:
    for elem in i:
        print(elem, end=' ')
    print()
