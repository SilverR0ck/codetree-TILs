row = 2
col = 4

arr = [
    list(map(int, input().split()))
    for _ in range(row)
]

r = []
c = []
t = []
row_avg = 0.0
col_avg = 0.0
total_avg=0.0

for i in range(row):
    for j in range(col): #가로줄 평균
        col_avg += arr[i][j]
        total_avg += arr[i][j]
    c.append(col_avg/4)
    col_avg = 0
    
for j in range(col):
    for i in range(row):
        row_avg += arr[i][j]
    r.append(row_avg/2)
    row_avg = 0


for i in c:
    print(i, end=' ')
    
print()
for i in r:
    print(i, end=' ')
print()
print(round(total_avg/8, 2))