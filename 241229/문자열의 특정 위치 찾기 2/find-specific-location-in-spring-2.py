arr = ["apple", "banana", "grape", "blueberry", "orange"]
s = input()
cnt = 0
corr = []
for i in arr:
    if i[2] == s or i[3] == s:
        cnt += 1
        corr.append(i)

for i in corr:
    print(i)
print(len(corr))