def RLE(t):
    t += '/'
    temp = t[0]
    ans = []
    count = 1
    for i in range(1,len(t)):
        # print(i, t[i], temp, count)
        if t[i] == temp:
            count+=1
        else:
            ans.append([temp, count])
            temp = t[i]
            count = 1
    return ans

exec(input())