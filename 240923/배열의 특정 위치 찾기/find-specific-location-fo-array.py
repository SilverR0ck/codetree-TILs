import math
n = list(map(int, input().split()))
n_sum = 0
n_avg_sum = 0
cnt = 0 

for i in range(1, len(n), 2):
    n_sum += n[i]
    
for j in range(2, len(n), 3):
    n_avg_sum += n[j]
    cnt += 1
print(n_sum, round(n_avg_sum/cnt, 1))