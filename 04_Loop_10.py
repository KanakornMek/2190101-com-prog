a = float(input())

steps = 0
temp = a
while temp > 0:
    temp //= 10
    steps += 1

l = 0
u = steps
x = (l+u)/2
while abs(a-10**x) > 1e-10* max(a,10**x):
    if 10**x > a:
        u = x
    else:
        l = x
    x = (l+u)/2

print(round(x,6))
