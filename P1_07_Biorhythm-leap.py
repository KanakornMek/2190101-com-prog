import math

def calMonthDays(start, end, y):
    day = 0
    for i in range(start, end + 1):
        n = 31
        if i == 4 or i == 6 or i == 9 or i == 11:
            n = 30
        else:
            if i == 2:
                n = 28
                if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                    n = 29
        day += n
    return day

bd,bm,by,d,m,y = map(int, input().split())
by -= 543
y -= 543
total_days = 0
for i in range(by+1, y):
    n = 365
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        n = 366
        print(i +543)
    total_days += n

red_days = calMonthDays(bm,12,by)
red_days -= (bd-1)

blue_days = calMonthDays(1, m-1,y)
blue_days += (d-1)

total_days += (red_days + blue_days)

print("{} {:.2f} {:.2f} {:.2f}".format(total_days, math.sin(2*math.pi*total_days/23), math.sin(2*math.pi*total_days/28), math.sin(2*math.pi*total_days/33)))
