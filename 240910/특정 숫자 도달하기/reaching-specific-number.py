arr = list(map(int, input().split()))
total = 0
cnt = 0
for elem in arr:
    if elem >= 250:
        break
    else:
        total += elem
        cnt += 1
avg = total/cnt
print(total, "%.1f" %avg)