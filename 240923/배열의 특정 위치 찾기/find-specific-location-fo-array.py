n = list(map(int, input().split()))
n_sum = 0
for i in range(1, len(n), 2):
    n_sum += n[i]

avg = n_sum/(len(n)/2)
print(n_sum, round(avg, 1))