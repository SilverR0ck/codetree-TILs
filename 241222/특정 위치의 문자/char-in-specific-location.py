word = ['L', 'E', 'B', 'R', 'O', 'S']
w = input()
idx = -1

for i, char in enumerate(word):
    if char == w:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)
