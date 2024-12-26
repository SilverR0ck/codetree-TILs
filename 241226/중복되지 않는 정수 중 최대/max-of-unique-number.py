N = int(input())
l = list(map(int, input().split()))
x = []

for i in l:
    if l.count(i)==1:
       x.append(i) 
    

if x:
    print(max(x))
else:
    print("-1")

