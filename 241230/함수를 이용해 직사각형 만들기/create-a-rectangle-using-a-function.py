def s(n, m):
    for i in range(n):
        for j in range(m):
            print('1', end='')
        print()

n, m = map(int, input().split())
s(n, m)

