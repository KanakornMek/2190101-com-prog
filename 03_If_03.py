a = [ float(x) for x in input().split()]

min = 0
max = 0
for i in range(4):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
sum = 0
for i in range(4):
    if(i == max or i == min):
        continue
    sum += a[i]

avg = sum/2

print(round(avg, 2))
