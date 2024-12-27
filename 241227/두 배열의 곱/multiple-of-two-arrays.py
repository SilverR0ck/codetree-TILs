row=3
arr1 = []
for _ in range(row):
    arr1.append(list(map(int, input().split())))
input()
arr2 = []
for _ in range(row):
    arr2.append(list(map(int, input().split())))

mul = [
    [0 for i in range(3)]
    for _ in range (3)
]
for i in range(row):
    for j in range(row):
        mul[i][j] = arr1[i][j]*arr2[i][j]


for i in mul:
    for elem in i:
        print(elem, end=' ')
    print()