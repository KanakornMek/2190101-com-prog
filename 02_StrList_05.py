import re
a = input()

sales = re.split("\s+", a)
sum = 0
for s in sales:
    sum += int(s)

print(sum)
