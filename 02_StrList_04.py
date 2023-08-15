m = input()
n = int(input())

output = ""
if(len(m) < n):
    for i in range(n-len(m)):
        output += "0"
output += m

print(output)
