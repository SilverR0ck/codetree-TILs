def func(n, m):
    i=1
    arr = []
    while(1):
        if n%i==0 and m%i==0:
            arr.append(i)
        if i>=n or i>=m:
            break
        i+=1
    print(max(arr))

n, m = map(int, input().split())
func(n, m)