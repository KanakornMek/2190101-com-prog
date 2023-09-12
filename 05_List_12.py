fullName = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickName = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

n = int(input())
arr = []
for i in range(n):
    arr += [input()]

for i in arr:
    found = False
    for j in range(len(fullName)):
        if i == fullName[j]:
            found = True
            print(nickName[j])
            break
        elif i == nickName[j]:
            found = True
            print(fullName[j])
    if(not found):
       print("Not found")
    