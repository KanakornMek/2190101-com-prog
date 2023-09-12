x = list(input())
lst = []
for i in range(10):
    if str(i) in x:
        continue
    lst += str(i)
lst.sort()
if len(lst) != 0:
    for i in range(len(lst)):
        if i != len(lst)-1:
            print(lst[i], end=",")
        else:
            print(lst[i])
else:
    print("None")