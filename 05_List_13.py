n = int(input())

set1 = []
for i in range(n):
    set1.append(int(input()))

set2 = [int(x) for x in input().split()]

set3 = []

while True:
    a = int(input())
    if(a == -1):
        break
    set3.append(a)

lst = set1 + set2 + set3

ans = []
for i in range(len(lst)):
    if i % 2 == 0:
        ans += [lst[i]]
    else:
        ans = [lst[i]] + ans

print(ans)