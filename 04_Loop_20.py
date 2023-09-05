min_1, min_2, max_1, max_2 = 10**8, 10**8, -10**8, -10**8
#1 = x1 y2 x3 y4
#2 = y1 x2 y3 x4

for i in range(3):
    x, y = map(int, input().split())
    
    if(i % 2 == 0):
        min_1 = min(min_1, x)
        max_1 = max(max_1, x)
        min_2 = min(min_2, y)
        max_2 = max(max_2, y)
    else:
        min_1 = min(min_1, y)
        max_1 = max(max_1, y)
        min_2 = min(min_2, x)
        max_2 = max(max_2, x)

type = (input() == "Zig-Zag")

if(type):
    print(min_1, max_2)
else:
    print(min_2, max_1)
