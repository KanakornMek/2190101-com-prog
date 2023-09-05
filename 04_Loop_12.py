n = int(input())
x,y = [],[]
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

type = (input() == "Zag-Zig")

min_num = 1e9
max_num = -1e9

if(type):
    for i in range(n):
        if(i % 2):
            min_num = min(min_num, x[i])
            max_num = max(max_num, y[i])
        else:
            max_num = max(max_num, x[i])
            min_num = min(min_num, y[i])
else:
    for i in range(n):
        if(i % 2):
            min_num = min(min_num, y[i])
            max_num = max(max_num, x[i])
        else:
            max_num = max(max_num, y[i])
            min_num = min(min_num, x[i])

print(min_num, max_num)