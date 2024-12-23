_list = list(map(int, input().split()))

if min(_list) == -999:
    _list.remove(-999)

if max(_list) == 999:
    _list.remove(999)

print(max(_list), min(_list))