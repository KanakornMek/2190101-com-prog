sum = 0
cnt = 0
while True:
    n = input()
    if n == 'q':
        break
    sum += float(n)
    cnt += 1
if cnt == 0:
    print("No Data")
else:
    print(round(sum/cnt, 2))


    
