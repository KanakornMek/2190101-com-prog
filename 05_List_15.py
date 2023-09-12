a = [int(x) for x in input().split()]

vals = set()

count = 0
for i in a:
    if i not in vals:
        vals.add(i)
        count += 1
    

print(count)
vals = list(vals)[:10]
print(vals)
