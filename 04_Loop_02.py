a = float(input())

l,u = 0, a

x = (l+u)/2
while abs(a-10**x) > 1e-10* max(a,10**x):
    if 10**x > a:
        u = x
    else:
        l = x
    x = (l+u)/2

print(round(x,6))



