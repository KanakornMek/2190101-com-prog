n = int(input())

lst = []

for i in range(n):
    x,y = map(float, input().split())
    
    lst.append([(x**2+y**2)**(1/2), i+1, x, y])

lst.sort()

print("#{}: ({}, {})".format(lst[2][1], lst[2][2], lst[2][3]))
