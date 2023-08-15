n = input()

a = ""
b = ""
for i in range(len(n)):
    if(i%7 == 3):
        a += n[i]
    if(i%5 == 2 and i >=7):
        b += n[i]

sum = int(a)+int(b)+10000
cN = str(sum)
cN = (cN[-4:])[:3]
sumC = 0
for i in cN:
    sumC += int(i)

cC = sumC % 10 + 1

cC = chr(64 + cC)

print(cN + cC)
