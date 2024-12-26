l = list(map(int, input().split()))
up = []
down = []

for i in l:
    if i > 500:
        up.append(i)
    else: 
        down.append(i)

print(max(down), min(up))