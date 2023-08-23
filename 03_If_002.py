d, m, y = map(int, input().split())

y -= 543
n = 31

if m == 4 or m == 6 or m == 9 or m == 11:
    n = 30
else:
    if m == 2:
        n = 28
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            n = 29

d += 15
if d > n:
    d -= n
    m += 1
if m > 12:
    m = 1
    y += 1

print("{}/{}/{}".format(d, m, y + 543))
