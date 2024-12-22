n, q = map(int, input().split())
l = list(map(int, input().split()))

for i in range(q):
    func = list(map(int, input().split()))
    if func[0] == 1:
        idx = func[1]-1
        print(l[idx])
        
    elif func[0] == 2:
        if func[1] not in l:
            print("0")
        else:
            print(l.index(func[1])+1)
    else:
        for k in range(func[1]-1, func[2], 1):
            print(l[k], end=' ')
        print()
        