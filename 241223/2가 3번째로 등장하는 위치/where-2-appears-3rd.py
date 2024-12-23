n = int(input())
array = list(map(int, input().split()))
cnt = 0

for i, char in enumerate(map(str, array)):
    if char == "2":
        cnt += 1
        if cnt == 3:
            print(i+1)
    
