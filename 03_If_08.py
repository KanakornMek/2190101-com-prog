d = int(input())
m = int(input())
y = int(input())
sum = 0
y -= 543
for i in range(1,m):
    n = 31
    if i == 4 or i == 6 or i == 9 or i == 11:
        n = 30
    else:
        if i == 2:
            n = 28
            if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                n = 29
    sum += n

sum += d

print(sum)
