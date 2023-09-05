n = int(input())

for i in range(n-1):
    for j in range(i+n):
        if j == i + n - 1 or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("*"*(2*n-1))

