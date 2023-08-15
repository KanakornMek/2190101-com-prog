id = input()

idA = []

for d in id:
    d = int(d)
    idA.append(d)

n12 = (11 - (13*idA[0]+12*idA[1]+11*idA[2]+10*idA[3]+9*idA[4]+8*idA[5]+7*idA[6]+6*idA[7]+5*idA[8]+4*idA[9]+3*idA[10]+2*idA[11])%11)%10

idA.append(n12)

output = ""
for i in range(13):
    if(i == 1 or i == 5 or i == 10 or i == 12):
        output += " "
    output += str(idA[i])
print(output)    

