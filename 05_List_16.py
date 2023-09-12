n = int(input())

ans = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2 #remove decimal
    else:
        n = 3*n + 1
    ans.append(n)

ans = ans[-15:]

for i in ans:
    end_char = "->" if i != 1 else "\n"
    print(i, end=end_char)
