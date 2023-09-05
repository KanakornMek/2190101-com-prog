s = input() + '/'
curr = s[0]
count = 0
ans = []
for i in s:
    if(i == curr):
        count += 1
    else:
        ans.append((curr, count))
        curr = i
        count = 1
for x,y in ans:
    print(x,y,end=" ")
