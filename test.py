a=input().split()
x=a[0]
y=a[1]
x1=int(x,2)
y1=int(y,2)
summ=x1+y1
ans=bin(summ)[2:]
print(ans)