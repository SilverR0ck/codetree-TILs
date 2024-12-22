n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

suc = 0

for i, char in enumerate(A):
    if char==B[0] and n2 <= n1-i:
        for j in range(n2):
            if A[i+j] != B[j]:
                suc = 1

if suc == 1:
    print("Yes")
else:
    print("No")

    
    